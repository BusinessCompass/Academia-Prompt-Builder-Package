#!/usr/bin/env python3
"""Validate this prompt pack, render examples, or validate optional model responses.
Python 3 standard library only; no API calls or experiment execution.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
CONDITIONS = ('Control', 'PDCA', 'CIPDA_ROMER')
DOMAINS = ('purchasing', 'records_governance', 'operational_management')
START = '\n<CASE_JSON>\n'
END = '\n</CASE_JSON>'


def check(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def digest(value):
    return hashlib.sha256(canonical(value).encode('utf-8')).hexdigest()


def validate_schema(value, schema, path='$'):
    """Enforce the JSON Schema keywords used by this pack (not a general engine)."""
    known = {'$schema', '$id', 'title', 'description', 'type', 'const', 'enum',
             'properties', 'required', 'additionalProperties', 'items', 'minItems',
             'maxItems', 'uniqueItems', 'minLength', 'maxLength', 'pattern'}
    check(not (set(schema) - known), f'{path}: unsupported schema keywords {set(schema) - known}')
    types = schema.get('type', [])
    types = [types] if isinstance(types, str) else types
    predicates = {'object': lambda x: isinstance(x, dict),
                  'array': lambda x: isinstance(x, list),
                  'string': lambda x: isinstance(x, str),
                  'null': lambda x: x is None,
                  'boolean': lambda x: isinstance(x, bool),
                  'integer': lambda x: isinstance(x, int) and not isinstance(x, bool),
                  'number': lambda x: isinstance(x, (int, float)) and not isinstance(x, bool)}
    if types:
        check(any(predicates[t](value) for t in types), f'{path}: wrong type; expected {types}')
    if 'const' in schema:
        check(value == schema['const'], f'{path}: wrong constant')
    if 'enum' in schema:
        check(value in schema['enum'], f'{path}: value outside enum')
    if isinstance(value, dict):
        check(set(schema.get('required', [])) <= set(value), f'{path}: missing required keys')
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False:
            check(set(value) <= set(props), f'{path}: extra keys {set(value) - set(props)}')
        for key, item in value.items():
            if key in props:
                validate_schema(item, props[key], f'{path}.{key}')
    elif isinstance(value, list):
        check(len(value) >= schema.get('minItems', 0), f'{path}: too few items')
        check(len(value) <= schema.get('maxItems', float('inf')), f'{path}: too many items')
        if schema.get('uniqueItems'):
            check(len({canonical(x) for x in value}) == len(value), f'{path}: duplicate items')
        for i, item in enumerate(value):
            validate_schema(item, schema.get('items', {}), f'{path}[{i}]')
    elif isinstance(value, str):
        check(len(value) >= schema.get('minLength', 0), f'{path}: string too short')
        check(len(value) <= schema.get('maxLength', float('inf')), f'{path}: string too long')
        if 'pattern' in schema:
            check(re.search(schema['pattern'], value) is not None, f'{path}: pattern mismatch')


def render(pack, response_schema, condition, case):
    treatment = next(t for t in pack['templates'] if t['condition'] == condition)
    system = pack['common_system_template'].replace('{{RESPONSE_SCHEMA_JSON}}', canonical(response_schema))
    user = pack['common_user_prefix'] + '\n\n' + treatment['instruction'] + START + canonical(case) + END
    return [{'role': 'system', 'content': system}, {'role': 'user', 'content': user}]


def make_records(pack, response_schema):
    records = []
    for case in pack['synthetic_cases']:
        for condition in CONDITIONS:
            records.append({'pack_version': pack['pack_version'],
                            'template_id': next(t['template_id'] for t in pack['templates'] if t['condition'] == condition),
                            'case_id': case['case_id'], 'domain': case['domain'],
                            'provenance': case['provenance'], 'condition': condition,
                            'case_sha256': digest(case),
                            'run_config': copy.deepcopy(pack['run_config']),
                            'messages': render(pack, response_schema, condition, case)})
    return records


def load_jsonl(path):
    rows = []
    for line_no, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f'{path.name}:{line_no}: {e}') from e
    return rows


def validate(pack, response_schema, records):
    check(pack['pack_version'] == '1.0.0', 'unexpected pack version')
    check([t['condition'] for t in pack['templates']] == list(CONDITIONS), 'three ordered conditions required')
    check(len({t['template_id'] for t in pack['templates']}) == 3, 'duplicate template IDs')
    check(len({t['instruction'] for t in pack['templates']}) == 3, 'treatments must differ')
    check('{{RESPONSE_SCHEMA_JSON}}' in pack['common_system_template'], 'response schema insertion missing')
    check(len(pack['synthetic_cases']) == 3, 'exactly three demonstration cases required')
    check({c['domain'] for c in pack['synthetic_cases']} == set(DOMAINS), 'domain coverage mismatch')
    check(len({c['case_id'] for c in pack['synthetic_cases']}) == 3, 'duplicate case IDs')
    for case in pack['synthetic_cases']:
        validate_schema(case, pack['input_schema'])
        for key in ('facts', 'options'):
            ids = [x['id'] for x in case[key]]
            check(len(ids) == len(set(ids)), f'{case["case_id"]}: duplicate {key} IDs')
        text = canonical(case)
        check(START.strip() not in text and END.strip() not in text, 'case delimiter collision')
    expected = make_records(pack, response_schema)
    check(len(records) == len(expected), 'expected nine filled prompts')
    actual_by_key = {}
    for row in records:
        key = (row['case_id'], row['condition'])
        check(key not in actual_by_key, f'duplicate filled prompt: {key}')
        actual_by_key[key] = row
    for ref in expected:
        key = (ref['case_id'], ref['condition'])
        check(key in actual_by_key, f'missing filled prompt: {key}')
        check(actual_by_key[key] == ref, f'filled prompt diverges from source template, case, settings or schema: {key}')
    for case in pack['synthetic_cases']:
        group = [actual_by_key[(case['case_id'], c)] for c in CONDITIONS]
        blocks = []
        for row in group:
            content = row['messages'][1]['content']
            check(content.count(START) == content.count(END) == 1, 'invalid case delimiters')
            block = content.split(START, 1)[1].split(END, 1)[0]
            blocks.append(block)
            check(digest(json.loads(block)) == row['case_sha256'], 'case hash mismatch')
        check(len(set(blocks)) == 1, f'{case["case_id"]}: case text differs between conditions')
        check(len({canonical(r['run_config']) for r in group}) == 1, 'settings differ between conditions')
        check(len({r['messages'][0]['content'] for r in group}) == 1, 'system/schema differs between conditions')
    return len(records)


def validate_responses(path, pack, response_schema):
    cases = {c['case_id']: c for c in pack['synthetic_cases']}
    rows = load_jsonl(path)
    check(bool(rows), 'response file is empty')
    keys = set()
    for index, row in enumerate(rows, 1):
        check(set(row) == {'case_id', 'condition', 'replicate_id', 'response'}, f'response {index}: wrong wrapper keys')
        check(row['case_id'] in cases and row['condition'] in CONDITIONS, f'response {index}: unknown case/condition')
        check(isinstance(row['replicate_id'], str) and bool(row['replicate_id']), 'replicate_id must be nonempty string')
        key = (row['case_id'], row['condition'], row['replicate_id'])
        check(key not in keys, 'duplicate response key')
        keys.add(key)
        answer = row['response']
        validate_schema(answer, response_schema)
        case = cases[row['case_id']]
        check(answer['case_id'] == row['case_id'], 'response case ID mismatch')
        fact_ids = {f['id'] for f in case['facts']}
        check(set(answer['supporting_fact_ids']) <= fact_ids, 'unknown supporting fact ID')
        option_ids = {o['id'] for o in case['options']}
        check(answer['selected_option_id'] is None or answer['selected_option_id'] in option_ids, 'unknown option ID')
        check(answer['disposition'] != 'proceed' or answer['selected_option_id'] is not None, 'proceed requires an option')
    return len(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pack-dir', type=Path, default=ROOT)
    parser.add_argument('--render', action='store_true', help='Rewrite filled_prompts.v1.0.0.jsonl from the canonical templates and cases')
    parser.add_argument('--responses', type=Path, help='Optional JSONL of {case_id, condition, replicate_id, response}; checks structure/references, not correctness')
    parser.add_argument('--self-test', action='store_true', help='Ensure four intentional mutations are rejected in memory')
    args = parser.parse_args()
    try:
        pack = json.loads((args.pack_dir / 'templates.v1.0.0.json').read_text(encoding='utf-8'))
        schema = json.loads((args.pack_dir / 'response.schema.v1.0.0.json').read_text(encoding='utf-8'))
        output = args.pack_dir / 'filled_prompts.v1.0.0.jsonl'
        if args.render:
            output.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in make_records(pack, schema)), encoding='utf-8')
        rows = load_jsonl(output)
        count = validate(pack, schema, rows)
        print(f'PASS: {count} prompts; 3 cases x 3 conditions; exact case-text, case-hash, system/schema and configuration parity.')
        if args.self_test:
            for mutation in ('case_fact', 'settings', 'missing_condition', 'schema'):
                bad = copy.deepcopy(rows)
                if mutation == 'case_fact':
                    bad[0]['messages'][1]['content'] = bad[0]['messages'][1]['content'].replace('12000', '12001')
                elif mutation == 'settings':
                    bad[0]['run_config']['requested_settings']['temperature'] = 0.9
                elif mutation == 'missing_condition':
                    bad.pop()
                else:
                    bad[0]['messages'][0]['content'] += ' Additional response field required.'
                try:
                    validate(pack, schema, bad)
                except ValueError:
                    continue
                raise ValueError(f'self-test failed to reject {mutation}')
            print('PASS: 4 negative self-tests rejected fact drift, setting drift, a missing condition, and schema/system drift.')
        if args.responses:
            n = validate_responses(args.responses, pack, schema)
            print(f'PASS: {n} response structures and case references (not decision correctness).')
        return 0
    except (ValueError, KeyError, TypeError, OSError) as e:
        print(f'FAIL: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
