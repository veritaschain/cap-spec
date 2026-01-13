# Hash Test Vectors

Test vectors for SHA-256 EventHash computation.

## Overview

CAP uses SHA-256 for computing EventHash values. The hash is computed over the canonical JSON representation of the event, excluding the `EventHash` and `Signature` fields.

## Hash Computation Process

1. Remove `EventHash` and `Signature` fields from event
2. Canonicalize using RFC 8785 (JCS)
3. Encode as UTF-8 bytes
4. Compute SHA-256 hash
5. Format as `sha256:{hex}` (lowercase)

## Test Cases

### test-001-simple-event.json

Minimal event hash computation.

### test-002-full-ingest.json

Complete INGEST event hash verification.

### test-003-srp-event.json

SRP GEN_DENY event hash verification.

## Verification Script

```python
import json
import hashlib

def compute_event_hash(event: dict) -> str:
    """Compute EventHash for a CAP event."""
    # Remove fields that are not included in hash
    event_copy = {k: v for k, v in event.items() 
                  if k not in ['EventHash', 'Signature']}
    
    # Canonicalize (RFC 8785)
    canonical = json.dumps(event_copy, sort_keys=True, 
                          separators=(',', ':'), ensure_ascii=False)
    
    # Hash
    hash_bytes = hashlib.sha256(canonical.encode('utf-8')).digest()
    
    return f"sha256:{hash_bytes.hex()}"

# Verify test vector
with open('test-001-simple-event.json') as f:
    test = json.load(f)

computed = compute_event_hash(test['input'])
assert computed == test['expectedHash'], f"Mismatch: {computed}"
print("✓ Test passed")
```

## References

- [FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final) - Secure Hash Standard
- [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785) - JSON Canonicalization Scheme
