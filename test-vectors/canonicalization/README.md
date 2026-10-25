# Canonicalization Test Vectors

Test vectors for RFC 8785 JSON Canonicalization Scheme (JCS) compliance.

## Overview

CAP uses RFC 8785 for deterministic JSON serialization before computing EventHash.
These test vectors verify correct implementation of JCS.

## Test Cases

### test-001-basic-object.json

Basic object canonicalization with sorted keys.

**Input:**
```json
{
  "zebra": 1,
  "apple": 2,
  "mango": 3
}
```

**Expected Canonical Output:**
```
{"apple":2,"mango":3,"zebra":1}
```

### test-002-cap-event.json

Canonicalization of a CAP event.

## Further cases (no vector file yet)

The cases below illustrate RFC 8785 behaviour. They have no vector files in this directory.

### Unicode

Unicode handling per RFC 8785.

**Input:**
```json
{
  "emoji": "🔒",
  "japanese": "日本語"
}
```

**Expected Canonical Output:**
```
{"emoji":"🔒","japanese":"日本語"}
```

### Numbers

Number formatting (no trailing zeros, no exponential for integers).

**Input:**
```json
{
  "integer": 42,
  "float": 3.14,
  "zero": 0.0,
  "negative": -17
}
```

**Expected Canonical Output:**
```
{"float":3.14,"integer":42,"negative":-17,"zero":0}
```

### Nested objects

Nested object key ordering.

**Input:**
```json
{
  "outer": {
    "z": 1,
    "a": 2
  },
  "array": [3, 2, 1]
}
```

**Expected Canonical Output:**
```
{"array":[3,2,1],"outer":{"a":2,"z":1}}
```

## Verification

Use an RFC 8785 implementation, for example the `rfc8785` package for Python or the `canonicalize` package for JavaScript. `json.dumps(obj, sort_keys=True, separators=(',', ':'))` is **not** RFC 8785: it formats numbers differently (for example `0.0` instead of `0`) and sorts keys by code point rather than by UTF-16 code unit.

```python
import hashlib
import rfc8785  # pip install rfc8785

def compute_hash(obj):
    return "sha256:" + hashlib.sha256(rfc8785.dumps(obj)).hexdigest()
```

`expectedHash` in `test-001-basic-object.json` was corrected on 2026-10-25; the earlier value was a placeholder.

## References

- [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785) - JSON Canonicalization Scheme
