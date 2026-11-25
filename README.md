#Academia.edu 'Co-Scientist' AI Prompt-Builder-Package
Posting outline: Control, PDCA and CIPDA–ROMER prompt pack by Academia
GitHub posting outline: Control, PDCA and CIPDA–ROMER prompt pack
Suggested repository name: cipda-cross-domain-prompt-pack
Suggested short description: Versioned Control, PDCA and CIPDA–ROMER prompts for matched synthetic management decisions, with shared schemas and local parity validation.

1. Project overview
State the purpose: provide transparent, reusable intervention materials for prospective comparisons of three prompt conditions.
Name the conditions: Control, Plan–Do–Check–Act (PDCA), and Context–Intent–Plan–Deliver–Assure (CIPDA) with ROMER in the Assure stage.
Name the three domains: purchasing, records governance and operational management.
Explain the central design: the same case facts, objective, options and response schema are used across conditions; only the process instruction changes.
Identify the release as v1.0.0.

2. Important status and provenance notice

This repository contains newly designed prompt materials informed by the available abstract describing the 2026 CIPDA study. It does not reproduce the original study intervention: the full paper and original prompts were not available during preparation. The historical conversation referenced in the preparation brief was also unavailable and was not used as evidence. The synthetic cases are newly generated fiction. No model experiments were run in preparing this release.

Identify the source paper: Kenneth Tombs, From PDSA to PDCA to CIPDA: structured improvement in AI-supported management reasoning, International Journal of Quality & Reliability Management (2026), DOI: https://doi.org/10.1108/IJQRM-01-2026-0029.
Explain that the available source was a profile metadata/abstract record, not the full paper.
State that ROMER is provisionally expanded as Reasoning, Observations, Method, Evidence, Report, with supplementary public-search-excerpt corroboration rather than verification against the full study.
State that the detailed ROMER instructions are newly authored operational definitions, not quotations from the original intervention.
Avoid publishing the private profile directory or historical conversation contents/identifiers unless the owner deliberately chooses to share them. The current materials contain workspace provenance references; review these before public release.

3. What is included
Describe the five core files:

File	                Purpose
prompt-pack.v1.0.0.md	Full guide, treatment contrast table, exact treatment blocks, settings, reset instructions and limitations.

templates.v1.0.0.json	Canonical templates, common input schema, configuration and three synthetic cases.

filled_prompts.v1.0.0.jsonl	Nine complete message pairs: three cases crossed with three conditions.

response.schema.v1.0.0.json	Common machine-readable response contract.

validate_pack.py	Local rendering, fact-parity checks, negative self-tests and optional response checks.

There is one example case per domain, not a large casebook.

The package does not include a model/API runner, model credentials, model-generated answers or experimental results.

4. Treatment comparison
Summarise the differences without reproducing the full guide:

Condition	Added instruction
Control	Use the model's usual approach, without a prescribed improvement sequence.
PDCA	Apply Plan, Do, Check and Act.
CIPDA–ROMER	Explicitly establish Context and Intent, Plan and Deliver a recommendation, then Assure it through ROMER checks.
List what stays fixed: case input, system framing, response schema, effective model settings and reset protocol.
Clarify that Control still has a common structured-output contract.
Clarify that CIPDA–ROMER is a bundled, longer instruction—not a length-matched test isolating ROMER alone.

5. Repository layout
Choose one layout before posting the quick-start commands.
For the simplest public layout, place the five core files together at the repository root.
Alternatively, retain the versioned subfolder and adjust all example paths consistently.
Keep the required files together: the validator locates its companion files relative to its own location by default.
Do not upload API keys, raw private conversations, .academia-profile/, Python caches or unrelated workspace files.

6. Quick start
The commands below assume the five core files are at the repository root and the terminal is already open there.

Prerequisite: Python 3; validation uses only the Python standard library.
Validate the distributed materials and run the negative self-tests:
python3 validate_pack.py --self-test
Explain the two expected PASS messages: one for nine matched prompts and one for four rejected mutations.
Configure provider/model details and supported settings in templates.v1.0.0.json.
Regenerate all filled prompts after configuration changes:
python3 validate_pack.py --render --self-test
Warn that --render overwrites the filled-prompts file.
State explicitly that neither command calls a model.

7. How to submit a prompt to a model
Select one JSONL record.
Apply its resolved settings in an API client or playground that supports separate system and user messages.
Send only that record's two messages: one system message and one user message.
Do not send the bookkeeping wrapper, other conditions, guide or expected answers.
Start a fresh session/request for every case-condition-replicate.
Disable memory, browsing, retrieval and tools where controllable; disclose any platform limitations.
Record raw answers, effective settings, model/revision, execution order, timestamps and errors.
Prespecify repetition, ordering and retry rules before collecting comparison data.

8. Response format and optional checks
List the common response fields: schema_version, case_id, disposition, selected_option_id, rationale, supporting_fact_ids, uncertainties, next_steps.
Explain that the rationale is a concise public justification, not a request for private chain-of-thought.
Describe the optional response-file wrapper: case_id, condition, replicate_id, response.
Give the optional validation command, with responses.jsonl identified as a user-supplied file:
python3 validate_pack.py --responses responses.jsonl
State that optional validation checks structure and case references, not decision correctness or completeness of an experimental collection.
Preserve raw invalid outputs; do not silently repair or replace them.

9. Validation performed for this release
Nine rendered prompts passed local case-text, case-hash, common-system/schema and configuration parity checks.
Four deliberate mutations were rejected: fact drift, setting drift, a missing condition and system/schema drift.
Input and response schemas were checked with a Draft 2020-12 validator during preparation; users do not need that library to run the supplied script.
Label these as software/material checks, not model-performance findings.

10. Limitations and interpretation
The full original study intervention was unavailable; exact replication is not claimed.
The referenced historical conversation was unavailable; its contents are not reconstructed.
ROMER's detailed implementation remains provisional pending source/author confirmation.
Three small synthetic cases cannot establish domain-general validity or real-world effectiveness.
Shared structure in Control may attenuate treatment differences.
Treatment length and multiple scaffolding features vary together.
The package contains no original-study outcome rubric and does not measure private reasoning.
Seeds and matched requested settings do not guarantee deterministic outputs or identical provider behaviour.
Fact hashes detect drift relative to this pack, not authenticity against the original study.

11. Versioning and contributions
Preserve v1.0.0 as a frozen materials release once published.

