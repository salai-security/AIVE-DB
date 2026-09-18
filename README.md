AIVE is a SALAI project.

# AIVE-DB

**AI Vulnerabilities & Exploits:** a proposed record format and identifier scheme for reusable AI security findings.

AIVE describes one failure pattern per record: what can go wrong, which components and trust boundaries are involved, how to detect it, and how to verify a mitigation. It covers patterns such as prompt injection, tool abuse and delegation-chain abuse.

This repository contains the v3 schema proposal, a validator and two illustrative draft records. It is the starting point for a registry; it does not yet provide a production database, ingestion service or API. Example IDs and records remain subject to maintainer approval.

## Start here

| File | Purpose |
| --- | --- |
| [aive.schema.v3.json](aive.schema.v3.json) | JSON Schema, Draft 7 |
| [validate.py](validate.py) | Validate records against the schema |
| [AIVE-2026-00001](examples/AIVE-2026-00001.json) | Indirect prompt injection leading to an unauthorized outbound tool call |
| [AIVE-2026-00002](examples/AIVE-2026-00002.json) | Delegation-chain abuse through authority expansion |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Finding proposals and schema contributions |
| [LICENSE-CONTENT](LICENSE-CONTENT) | CC-BY-4.0 for the schema, records and documentation |
| [LICENSE-CODE](LICENSE-CODE) | Apache-2.0 for the validator and other code |

## What a record contains

- A permanent identifier in the form `AIVE-YYYY-NNNNN`.
- A pattern description, attack vectors, affected component classes and control layers.
- Agent context where applicable: tools, identities, delegation depth and crossed boundaries.
- Impact, detection indicators and a minimum control with a verification method.
- Optional taxonomy mappings and public evidence references.
- Lifecycle and review status, with a changelog.

Incident-specific details stay outside the record. Opaque incident references may link a reusable finding to a separate incident process. AIVE IDs identify findings; they do not assert a CVE assignment, vendor confirmation or endorsement by another organization.

## Validate a record

Requires Python 3.9 or later and the `jsonschema` package.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python validate.py examples/*.json
```

The validator exits with status 0 when all supplied records pass and 1 when a record fails schema validation. It checks structure and formats, not whether a finding is true or a mitigation is effective.

## Schema location

The intended hosted identifier for this proposal is:

`https://raw.githubusercontent.com/salai-security/AIVE-DB/main/aive.schema.v3.json`

The local validator loads the schema from this repository. The hosted URL must serve the same JSON before a public release is announced. A versioned release can later provide an immutable schema URL.

## Review and lifecycle

The bundled examples are illustrative drafts, marked `unreviewed`. They do not claim that the described conditions have been tested in a specific product or observed in a real incident. Their proposed IDs are not final registry assignments until accepted by the maintainer.

Drafts carry `last_updated` and omit `published_date`. A non-draft record requires `published_date`. Human review, vendor confirmation and real-world exploitation must be supported before those claims are recorded. Once assigned, an ID is never reused; superseded records retain their ID and point to the successor.

## Publisher and contact

Published by [SALAI](https://github.com/salai-security). Maintainer: Salah Khan (SALAI).

Use repository issues for public format questions and contribution proposals. The project-domain contact address will be added when configured. Do not put confidential vulnerability reports or assessment responses in a public issue.

## License

Copyright 2026 Salah Khan (SALAI).

- Schema, example records and documentation: **CC-BY-4.0**, in [LICENSE-CONTENT](LICENSE-CONTENT).
- Validator and other code: **Apache-2.0**, in [LICENSE-CODE](LICENSE-CODE).

These licenses permit commercial use subject to their terms. Attribution does not imply endorsement. Referenced third-party materials retain their own terms.
