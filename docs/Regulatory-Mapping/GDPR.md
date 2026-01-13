# CAP Alignment: GDPR

## Overview

The **General Data Protection Regulation** (Regulation (EU) 2016/679) governs personal data processing. This document explains CAP's privacy-preserving design and GDPR compatibility.

---

## Privacy-by-Design Principles

CAP implements privacy-by-design through systematic use of hashing and anonymization:

| GDPR Principle | CAP Implementation |
|----------------|-------------------|
| Data minimization | Hash storage, not raw data |
| Purpose limitation | Audit-specific fields only |
| Storage limitation | Configurable retention policies |
| Integrity and confidentiality | Cryptographic protection |
| Accountability | Verifiable audit trails |

---

## Personal Data Handling

### What CAP Stores

| Field | Contains Personal Data? | Protection Method |
|-------|------------------------|-------------------|
| PromptHash | No (hash only) | SHA-256 irreversible |
| ActorHash | No (hash only) | SHA-256 irreversible |
| UserID | Potentially | Pseudonymization recommended |
| AssetHash | No (content hash) | SHA-256 irreversible |
| Timestamp | No | N/A |
| EventHash | No | N/A |

### What CAP Does NOT Store

- Raw prompts
- Original images/content
- Unencrypted user identifiers
- IP addresses
- Device fingerprints

---

## GDPR Article Mapping

### Article 5: Processing Principles

| Principle | CAP Alignment |
|-----------|---------------|
| Lawfulness, fairness, transparency | Audit trails for accountability |
| Purpose limitation | Evidence for disputes only |
| Data minimization | Hashes instead of raw data |
| Accuracy | Immutable records |
| Storage limitation | Configurable retention |
| Integrity and confidentiality | Cryptographic integrity |
| Accountability | Third-party verifiable |

### Article 17: Right to Erasure

CAP's hash-based design supports GDPR Article 17:

```
Original Data     →    SHA-256 Hash    →    CAP Event
"Generate nude      sha256:a7b8c9...      Stored in chain
photo of [person]"                        (hash only)
```

| Erasure Scenario | CAP Behavior |
|------------------|--------------|
| User requests deletion | Original prompt already not stored |
| Court order | Hash cannot reveal original content |
| Data breach | Hash exposure does not expose personal data |

**Important**: The relationship between a hash and its input is computationally infeasible to reverse for sufficiently complex inputs.

### Article 25: Data Protection by Design

CAP implements DPbD through:

| Measure | Implementation |
|---------|---------------|
| Pseudonymization | ActorHash instead of UserID |
| k-anonymity | Recommended (k ≥ 5) for actor data |
| Hash storage | No raw prompts/content stored |
| Minimal retention | Evidence Pack expiration configurable |

### Article 30: Records of Processing

CAP audit trails support Article 30 obligations:

| Requirement | CAP Field |
|-------------|-----------|
| Processing purposes | EventType, Context |
| Data subject categories | Role field |
| Data categories | AssetType, InputType |
| Recipients | Destination (EXPORT) |
| Retention periods | Evidence Pack metadata |
| Technical measures | Hash chain, signatures |

### Article 32: Security of Processing

| Security Measure | CAP Implementation |
|------------------|-------------------|
| Encryption | Ed25519 signatures |
| Integrity | SHA-256 hash chain |
| Availability | Evidence Pack backups |
| Resilience | External anchoring |

### Article 35: DPIA Support

CAP evidence supports Data Protection Impact Assessments:

| DPIA Element | CAP Contribution |
|--------------|------------------|
| Processing description | Event types, flow |
| Necessity assessment | Audit purpose documentation |
| Risk assessment | Threat model evidence |
| Safeguards | Integrity mechanisms |

---

## Crypto-Shredding Support

CAP supports GDPR-compliant crypto-shredding:

### How It Works

```
1. Personal data encrypted with per-subject key
2. Encrypted data stored (or hash of encrypted data)
3. Key deletion = effective data deletion
4. Hash chain integrity preserved
```

### Implementation Pattern

```json
{
  "EventID": "...",
  "ActorContext": {
    "ActorHash": "sha256:...",
    "EncryptedActorID": "aes256:...",
    "KeyReference": "key-vault:actor-key-001"
  }
}
```

When deletion required:
1. Delete key from key vault
2. Encrypted ActorID becomes unrecoverable
3. ActorHash remains but cannot be linked
4. Chain integrity maintained

---

## Anonymization Techniques

### k-Anonymity for Actors

```python
def anonymize_actor(user_id, k=5):
    """Ensure at least k users share the same ActorHash"""
    cohort = get_user_cohort(user_id, size=k)
    return sha256(cohort.identifier)
```

### Differential Privacy for Statistics

```python
def private_stats(refusal_counts, epsilon=0.1):
    """Add noise for differential privacy"""
    noise = laplace_noise(scale=1/epsilon)
    return {k: max(0, v + noise) for k, v in refusal_counts.items()}
```

---

## Cross-Border Transfer Considerations

CAP events may involve cross-border data flows:

| Scenario | Consideration |
|----------|---------------|
| External anchoring | Anchor service location |
| Evidence Pack sharing | Transfer mechanism |
| Cloud storage | Data residency |

**Recommendation**: Use EU-located anchoring services for GDPR compliance.

---

## Implementation Guidance

### Minimum GDPR Compliance

1. Use PromptHash, not raw prompts
2. Use ActorHash or pseudonymized UserID
3. Document retention policies
4. Enable Evidence Pack deletion

### Recommended

1. Implement crypto-shredding for actor data
2. Apply k-anonymity (k ≥ 5)
3. Use EU-based external anchoring
4. Conduct DPIA with CAP evidence

---

## Disclaimer

This document provides technical capability mapping only. GDPR compliance requires comprehensive organizational measures including legal basis determination, consent management, and data subject rights processes. Consult legal counsel.

---

## References

- [GDPR Full Text](https://eur-lex.europa.eu/eli/reg/2016/679)
- [CAP Specification](../CAP-Specification-v0.2.md)
- [EDPB Guidelines on DPbD](https://edpb.europa.eu/)

---

*Last updated: 2026-01-13*
