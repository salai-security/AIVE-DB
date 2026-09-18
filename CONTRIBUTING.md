# Contributing to AIVE

AIVE is maintained by SALAI. Use issues for schema proposals and pull requests for concrete changes.

## Propose a finding

Describe one reusable failure pattern, the affected component classes, the boundary crossed, the minimum control and a reproducible verification method. Use synthetic data in examples. Do not submit customer identifiers, credentials, confidential incident details or working payloads against live systems.

For a new record, propose an example without assigning a permanent AIVE ID yourself; a maintainer will allocate the ID. Keep the record at `draft` and `unreviewed` until a maintainer records an actual review. Schema validation checks the format, not the truth of the finding.

Support claims about real-world exploitation, affected products and severity with appropriate public evidence. Omit unsupported optional claims. Record taxonomy mappings only when the mapping is justified.

## Validate changes

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python validate.py examples/*.json
```

When changing the schema, explain compatibility effects and include an example that exercises the change. Keep the schema identifier and documented hosted path in agreement.

## Licensing

Contributions to the schema, records and documentation use CC-BY-4.0. Contributions to the validator and other code use Apache-2.0. Submit only material you have the right to contribute under the applicable license, and preserve attribution and third-party notices.
