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

### test-002-unicode.json

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

### test-003-numbers.json

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

### test-004-nested.json

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

```python
import json
import hashlib

def canonicalize(obj):
    """Simple JCS implementation for testing"""
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False)

def compute_hash(canonical_json):
    return "sha256:" + hashlib.sha256(canonical_json.encode('utf-8')).hexdigest()
```

## References

- [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785) - JSON Canonicalization Scheme
