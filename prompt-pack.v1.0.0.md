# Control / PDCA / CIPDA–ROMER intervention prompt pack

**Version:** 1.0.0 · **Prepared:** 25 November 2026  
**Purpose:** prospective cross-domain prompt comparison, with three reusable condition templates and three small demonstration cases.  
**Status:** newly designed intervention materials. **Not the original 2026 study prompts, not an exact replication, and not model-experiment results.**

## 1. Evidence boundary and provenance

The supplied profile record, `.academia-profile/works/openalex-7163160945.json`, describes Kenneth Tombs's 2026 paper, *From PDSA to PDCA to CIPDA: structured improvement in AI-supported management reasoning*, DOI [10.1108/IJQRM-01-2026-0029](https://doi.org/10.1108/IJQRM-01-2026-0029). Its abstract distinguishes an unstructured Control, PDCA, and Context–Intent–Plan–Deliver–Assure (CIPDA), with ROMER as the AI-operated evidential mechanism within Assure. It also describes resets and identical scenario inputs. These descriptions motivate this pack; they do not supply its wording.

The record is an abstract/metadata entry, with `pdf_path: null` and `pdf_status: unavailable`; the abstract is truncated at its end. The full paper and original study prompts were not available for this task. The requested conversation, `ba844388-a506-429f-9579-db6413785b4e`, was not accessible through the available tools or workspace. **No statements or definitions are attributed to that conversation.** The brief in the current conversation was used directly.

For ROMER, public search excerpts for [the author's profile](https://www.linkedin.com/in/kennethtombs/) and [a Society for Computers & Law article](https://www.scl.org/go-and-try-it-ai-the-enron-corpus-and-a-witness-who-was-there/) give **Reasoning, Observations, Method, Evidence, Report**. The latter's full page returned HTTP 403, so this is supplementary snippet-level corroboration, not verification against the paper. The functional instructions assigned to those five terms below are **provisional, newly authored operational definitions**, not quotations or a validated implementation of the original intervention. Confirm them against the author/full paper before describing a future study as a replication.

All cases, instructions, schemas, settings and software in this pack were newly generated for this request. No external casebook was copied. The local checks described below are software/material checks only; no model responses were generated or model experiments run.

## 2. Contents and unit of use

| Deliverable | Role |
|---|---|
| `templates.v1.0.0.json` | Authoritative three templates, shared system/user framing, common input schema, configurable settings, reset protocol and exactly three synthetic case inputs. |
| `filled_prompts.v1.0.0.jsonl` | Nine fully rendered message pairs: each of the three cases under all three conditions. The common response schema is already embedded in each system message. |
| `response.schema.v1.0.0.json` | Standalone JSON Schema, Draft 2020-12, identical for all conditions/domains. |
| `validate_pack.py` | Standard-library-only renderer and validator, including deliberate-corruption self-tests and optional response validation. |
| This document | Treatment contrasts, exact treatment blocks, use/reset instructions and limitations. |

**One experimental request = one JSONL row's `messages` array**, in a fresh session, with its resolved `run_config` applied by the runner. The wrapper is bookkeeping; do not send it, this guide, the other conditions, source descriptions, or any assessor material to the model. Nothing here executes a purchase, deletes records, restarts machinery or calls a model API.

The same three condition templates apply unchanged across purchasing, records governance and operational management. There is one newly generated synthetic case per domain, not a case bank and not enough cases to estimate domain-general effects.

## 3. Treatment contrast table

| Feature | Control `control-1.0.0` | PDCA `pdca-1.0.0` | CIPDA–ROMER `cipda-romer-1.0.0` |
|---|---|---|---|
| Added process instruction | Usual approach; no named sequence required | Plan → Do → Check → Act | Context → Intent → Plan → Deliver → Assure |
| Context and intent | Only what is supplied in the common case; no prescribed handling | Addressed through objective/requirements in Plan and Check; no separate Context/Intent stages | Explicit decision boundary, authority, material unknowns, and objective-versus-permission distinction |
| Option assessment | Not sequenced | Plan an approach; desk-assess options in Do | Compare options against Context and Intent in Plan; provisional recommendation in Deliver |
| Review instruction | No additional review stage | Check discrepancies; Act to retain/revise and identify follow-up | Assure through five specified ROMER evidential checks; revise unsupported recommendation |
| ROMER | Not prescribed | Not prescribed | Reasoning / Observations / Method / Evidence / Report within Assure |
| Response contract | Same compact decision JSON | Same compact decision JSON; no PDCA stage fields | Same compact decision JSON; no CIPDA or ROMER stage fields |
| Case facts, options and objective | Identical within each matched case | Identical within each matched case | Identical within each matched case |
| System instructions, schema, effective settings, reset policy | Matched | Matched | Matched |

**Interpretation:** Control is a **no-process-scaffold baseline under a common structured-output contract**, not literally unconstrained or fully unstructured prompting. Shared instructions prohibit invented approvals and require short justification/evidence references; this may reduce differences from the active treatments. PDCA also explicitly checks requirements: it is not instructed to ignore constraints.

CIPDA–ROMER is a bundled intervention: explicit Context/Intent, more detailed assurance and a longer treatment block all change together. This design does not isolate ROMER, acronym effects, token length, or any single stage. Common input and response schemas do **not** imply token-length matching. No chain-of-thought is requested or used as an outcome: the common rationale is a concise public justification. Consequently, these materials do not operationalise the original paper's complete traceability measure or provide its scoring rubric.

## 4. Exact versioned treatment blocks

Each block occupies exactly the same position: after the common user prefix and before the delimited case JSON. The authoritative renderer inserts the shared schema in the common system template. All other visible framing remains identical.

### Control — `control-1.0.0`

```text
Use your usual approach to make the recommendation. No named improvement framework or prescribed sequence is required.
```

### PDCA — `pdca-1.0.0`

```text
Apply Plan–Do–Check–Act (PDCA) to make the recommendation. Plan: formulate an approach to the stated objective using the supplied case. Do: apply that approach to the available options as a desk-based assessment, not a real-world action. Check: compare the provisional result with the case requirements and identify discrepancies. Act: retain or revise the recommendation and identify any needed follow-up. Return only the common JSON response, not separate stage outputs.
```

### CIPDA with ROMER — `cipda-romer-1.0.0`

```text
Apply Context–Intent–Plan–Deliver–Assure (CIPDA) to make the recommendation. Context: establish the decision boundary, applicable case constraints, available authority and material unknowns from the supplied facts. Intent: distinguish the stated objective from the authority and conditions under which it may be achieved; do not create a new objective. Plan: compare the available options against that context and intent, identifying evidence needed for a defensible choice. Deliver: formulate a provisional recommendation, not a real-world action. Assure: apply ROMER (Reasoning, Observations, Method, Evidence, Report) as an evidential check on that recommendation. Reasoning: check that its concise justification follows from the case rather than an unstated assumption. Observations: separate supplied observations from inferences and unknowns. Method: check that the option assessment addresses the material constraints and conflicts. Evidence: link material conclusions to supplied fact IDs and flag unsupported claims. Report: finalise the disposition, brief justification, uncertainties and next steps in the common response format. Revise an unsupported recommendation before returning it. Return only the common JSON response, not separate stage or ROMER outputs, and do not expose private deliberation.
```

No individual stage is a separate model turn. All three conditions receive one system message and one user message, and return one answer.

## 5. Shared input and response contracts

### Input

`templates.v1.0.0.json` contains the complete `input_schema`. Every case has exactly:

- `case_id`, `domain`, `provenance`, `objective`;
- `facts`: ordered `{id, text}` entries, with unique `F1`, `F2`, … identifiers;
- `options`: ordered `{id, label}` entries, with unique `O1`, `O2`, … identifiers.

Facts include the fictional policy, decision authority, operational constraints and available/missing evidence. Do not add condition-specific facts or hints. Do not silently introduce external law, purchasing thresholds or safety policies. Unknowns are explicitly identified as unknown; they are not permissions. The rendered `<CASE_JSON>` block is byte-identical across the three conditions for each case, including ordering, objective, options and synthetic provenance.

### Response

All conditions use the standalone response schema without modification:

| Field | Meaning |
|---|---|
| `schema_version` | Always `1.0.0`. |
| `case_id` | Echo the input case ID. |
| `disposition` | `proceed`: authorise an available compliant substantive action now; `do_not_proceed`: reject the substantive action as currently specified; `defer`: withhold authorisation pending information or authority. |
| `selected_option_id` | A supplied option ID, or `null`. `proceed` requires an option. A hold/escalation option may be selected with `defer` or `do_not_proceed`; it does not authorise the original action. |
| `rationale` | Brief decision justification, maximum 1,800 characters; not private deliberation or a stage transcript. |
| `supporting_fact_ids` | Unique supplied fact IDs supporting the decision. |
| `uncertainties` | Material unknowns; empty array if none. |
| `next_steps` | Recommended follow-up, not claims of completed actions; empty array if none. |

There are no condition-specific response fields. The validator checks references but does not judge whether the cited facts support the reasoning. It does not enforce one expected answer for a case. If later scoring distinguishes rejection from deferral, specify that adjudication rule before collection; do not infer correctness from JSON validity.

## 6. Newly generated synthetic filled-in prompts

**All three cases below are newly generated fiction, created on 25 November 2026. Their 2027 decision dates, organisations, prices and policies are invented. They are not original study cases or observed organisational incidents.**

| Case | Domain | Illustrative decision features, not an answer key |
|---|---|---|
| `SYN-PUR-001` | Purchasing | Two scanner quotes, a single-order authority ceiling, fixed delivery requirement and managerial preference. |
| `SYN-REC-001` | Records governance | Expired normal retention, an active legal hold, whole-batch deletion and an untested selective-disposal script. |
| `SYN-OPS-001` | Operational management | A restart deadline, post-maintenance evidence requirements, pre-maintenance test evidence and non-waivable prerequisites. |

`filled_prompts.v1.0.0.jsonl` contains **nine complete, filled-in prompts**, ordered purchasing/Control, purchasing/PDCA, purchasing/CIPDA–ROMER, then the same order for records governance and operational management. These are inputs only; no fabricated model answers are included. The canonical case objects live once in `templates.v1.0.0.json`; their repetition in the nine rendered prompts is necessary for independent, matched requests, not an additional casebook.

For immediate manual use, read one JSONL row and copy its two `messages` contents into the corresponding system and user fields. Its response schema is already filled in. Do not paste the entire JSONL row as a user prompt.

## 7. Configure before collection

`run_config` is a provider-neutral specification, **not** a provider-native API payload. Map it explicitly to the selected API/client; native structured-output enforcement is not enabled in this version. The prompt requests JSON in ordinary text output for all conditions.

| Configuration | v1.0.0 requested value / required action |
|---|---|
| Provider, exact model ID, revision, endpoint/runtime | Replace each `REPLACE_WITH_…` value. Pin a revision if possible; otherwise record that it is unavailable and record the served model identifier and timestamp on every attempt. |
| Temperature | `0.2` |
| Top-p | `1.0` |
| Output token ceiling | `1200`; map to the provider's correct parameter and record whether it includes hidden reasoning tokens. |
| Seed | `1729` for the illustrative first replicate, if supported. Prespecify later seeds; match each case-replicate seed across conditions. |
| Frequency/presence penalties | `0.0` / `0.0`, if supported. |
| Reasoning effort | `OMIT_EXPLICITLY_UNSET` is a bookkeeping sentinel, **not** a literal API value. Omit it and record the effective provider default, or choose a supported explicit value for all conditions before collection. |
| Stop sequences | None (`[]`). |
| Tools / tool choice / web / memory | No tools; `none`; web off; memory off. Omit a rejected no-tools `tool_choice` argument for all conditions, recording that mapping. |
| Output mode | Ordinary text, one JSON object; not a provider-native schema mode. |

Do not send unsupported parameters blindly. Resolve support before collection, document requested and effective settings/provider defaults, then remove or change unsupported settings **for all three conditions** and regenerate the filled prompts. If a platform cannot disable tools or memory, do not describe it as equivalent to this protocol; change platforms or declare the limitation. A seed is not a guarantee of determinism, and temperature zero is not a substitute for repeated observations.

Changing runner-only provider values does not change the intervention wording version, but record the effective configuration with each attempt. Changes to case content, treatment wording, shared framing or schemas require a new material version, not silent edits to a frozen release. No API-specific runner is supplied, and no API credentials are needed for the local checks.

## 8. Reset and execution instructions

1. Before **every case × condition × replicate**, create a new independent request or fresh session. Never carry a condition's answer into another condition, or reuse a thread/previous-response ID.
2. Send exactly one system and one user message from the chosen record. Disable custom instructions, persistent memory, retrieval, browsing, tools and conversation continuation. Do not supply this guide, example answers, earlier responses or evaluator expectations.
3. If a platform's hidden system instructions or reset behaviour cannot be controlled, record that limitation; never claim they were removed. Keep the visible and effective platform configuration matched across conditions.
4. Obtain one completion. Preserve the raw answer and completion metadata, including refusals, invalid JSON, truncation and transport errors. Do not silently repair an answer or selectively retry a condition. Prespecify any retry rule and retain all attempts separately.
5. Before a prospective comparison, prespecify condition ordering/counterbalancing and replicate seeds. Keep the same seed within a case-replicate triplet where supported. Log actual order, exact messages or their hashes, model/revision, effective settings, time and reset method with every attempt. No run order has been executed here.

A text “reset” instruction inside an existing conversation is insufficient. Reset is a runner/session action. Do not use the requested historical conversation as the model's active experimental context.

## 9. Run the local checks

Run these from the workspace root; Python 3's standard library is sufficient:

```bash
# Validate the distributed examples and execute four in-memory negative tests.
python3 co-scientist-outputs/cipda-prompt-pack-v1.0.0/validate_pack.py --self-test

# After deliberately configuring the canonical pack, regenerate all nine rows.
# This overwrites the existing filled-prompts file; it does not call a model.
python3 co-scientist-outputs/cipda-prompt-pack-v1.0.0/validate_pack.py --render --self-test
```

With `--pack-dir`, you may point at another directory containing the same versioned filenames. The default is the script's own directory, so validation does not depend on the current working directory. Exit code `0` means pass; `1` means a validation/read failure. The renderer is intentionally v1.0.0-specific: a new material version requires updating its version constants/file references as well as the templates and schema.

For optional future model-output checks, provide `--responses PATH_TO_JSONL`. Each response line must be a wrapper with exactly `case_id`, `condition`, `replicate_id` (a nonempty string), and `response` (the parsed common-schema object). Recognised condition values are `Control`, `PDCA`, `CIPDA_ROMER`. This accepts a partial response collection and does not check experimental completeness. Preserve raw outputs separately before parsing; a parse failure is an outcome, not permission to invent or repair an answer.

### What the validator checks

- Exactly three versioned conditions and one demonstration case per domain.
- Required input fields, types, domain/provenance labels and unique case/fact/option IDs.
- Exactly nine records, with no duplicate or missing case-condition pairs.
- Each record equals a fresh rendering of the canonical template, case, schema and settings.
- Exact shared system/schema equality, exact case-text equality and equal configurations within each case triplet.
- A SHA-256 fingerprint of each canonical case, including objective and options, matching the filled prompt.
- Four negative tests: one-condition fact drift, setting drift, a missing condition and system/schema drift.
- Optional responses: the schema's field/type/length/enum constraints, known fact/option references, unique case-condition-replicate keys, and a selected option when `proceed` is used.

The script implements only the JSON Schema keyword subset used in this pack, rejecting unknown keywords. The standalone schema remains compatible with standard Draft 2020-12 validators.

### Checks actually performed for this delivery

The nine prompts were rendered and passed local parity/structure validation. All four deliberate-corruption tests were rejected. The input and response schemas were also checked with the installed Draft 2020-12 validator. These results establish internal material consistency, **not** semantic equivalence of treatments, model adherence, decision accuracy, reliability, reduced variance or replication of the 2026 findings. Hash parity detects drift relative to the supplied canonical cases; it does not authenticate the original study or detect coordinated edits to all source and rendered materials.
