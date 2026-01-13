# Signature Test Vectors

Test vectors for Ed25519 digital signature verification.

## Overview

CAP uses Ed25519 (RFC 8032) for digital signatures. The signature is computed over the EventHash value.

## Signature Process

1. Compute EventHash (see hash test vectors)
2. Encode EventHash as UTF-8 bytes
3. Sign with Ed25519 private key
4. Format as `ed25519:{base64}` (standard Base64)

## Test Cases

### test-001-signature-verify.json

Basic signature verification with known keypair.

**Test Key Pair (FOR TESTING ONLY):**
```
Private Key (hex): 9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60
Public Key (hex): d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a
```

### test-002-invalid-signature.json

Detection of invalid/tampered signatures.

## Verification Script

```python
from nacl.signing import VerifyKey
import base64

def verify_signature(event_hash: str, signature: str, public_key_hex: str) -> bool:
    """Verify Ed25519 signature on EventHash."""
    
    # Parse signature (remove prefix)
    if not signature.startswith('ed25519:'):
        raise ValueError("Invalid signature format")
    sig_b64 = signature[8:]
    sig_bytes = base64.b64decode(sig_b64)
    
    # Parse public key
    pk_bytes = bytes.fromhex(public_key_hex)
    verify_key = VerifyKey(pk_bytes)
    
    # Verify
    try:
        verify_key.verify(event_hash.encode('utf-8'), sig_bytes)
        return True
    except Exception:
        return False

# Example usage
public_key = "d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a"
event_hash = "sha256:5a8c7d9e1f2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d"
signature = "ed25519:MEUCIQDhE3H4..."

result = verify_signature(event_hash, signature, public_key)
print(f"Signature valid: {result}")
```

## Key Management Notes

**WARNING:** The test keys in this directory are for testing only. Never use these keys in production.

Production implementations MUST:
- Generate unique keypairs using cryptographically secure random number generators
- Store private keys in HSMs or secure enclaves
- Implement key rotation procedures
- Maintain public key directories for verification

## References

- [RFC 8032](https://www.rfc-editor.org/rfc/rfc8032) - Edwards-Curve Digital Signature Algorithm (EdDSA)
- [Ed25519 High-Level Functions](https://ed25519.cr.yp.to/)
