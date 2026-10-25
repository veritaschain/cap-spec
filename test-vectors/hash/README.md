# Hash Test Vectors

Test vectors for SHA-256 EventHash computation.

## Overview

CAP uses SHA-256 for computing EventHash values. The hash is computed over the canonical JSON representation of the event, excluding the `EventHash` and `Signature` fields.

These vectors follow the corrected exclusion rule proposed in the [draft conformance mapping](../../docs/conformance/CAP-v1.0-VAP-v1.2-Draft3-Conformance-Mapping.md) (I04). The released CAP v1.0 text (§8.2) excludes only `Signature`; see the README known issues.

## Hash Computation Process

1. Remove `EventHash` and `Signature` fields from event
2. Canonicalize using RFC 8785 (JCS)
3. Use the resulting UTF-8 bytes
4. Compute SHA-256 hash
5. Format as `sha256:{hex}` (lowercase)

## Test Cases

### test-001-simple-event.json

Minimal event hash computation. The existing vector is unchanged.

### test-002-jcs-regressions.json

Three serializer regressions: integral floats (`1.0` becomes `1`), positive and negative floating-point zero (both become `0`), and property ordering by UTF-16 code units (U+10000 precedes U+E000). These minimal objects test canonicalization and hashing; they are not complete CAP events and do not establish CAP conformance.

Planned cases with no vector file yet: a complete INGEST event and an SRP GEN_DENY event.

## Verification Script

Install `rfc8785` and run all four cases from the repository root:

```sh
python -m pip install rfc8785
python test-vectors/hash/verify_hash_vectors.py
```

The [runner](verify_hash_vectors.py) checks both the exact canonical UTF-8 bytes and the expected SHA-256 digest. Its hash function uses:

```python
import hashlib
import rfc8785


def compute_event_hash(event: dict) -> str:
    """Compute the illustrative CAP hash using the draft exclusion rule."""
    event_copy = {key: value for key, value in event.items()
                  if key not in ("EventHash", "Signature")}
    canonical = rfc8785.dumps(event_copy)  # RFC 8785 UTF-8 bytes
    return "sha256:" + hashlib.sha256(canonical).hexdigest()
```

`json.dumps(..., sort_keys=True, separators=(',', ':'), ensure_ascii=False)` is not a replacement for RFC 8785. It retains representations such as `1.0` and `0.0` and sorts keys by Unicode code point rather than UTF-16 code unit. The three new regressions distinguish that old example from JCS.

Canonicalization errors must propagate. Do not silently round integers, convert numbers to strings, or fall back to `json.dumps`. The Python `rfc8785` implementation rejects integers outside its safe-integer domain; that library constraint is not a newly adopted CAP numeric-encoding rule.

This change corrects an illustrative test helper. It does not amend the released CAP v1.0 specification, adopt the draft exclusion rule, rewrite historical signed data, or establish independent third-party reproduction.

## References

- [FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final) - Secure Hash Standard
- [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785) - JSON Canonicalization Scheme
