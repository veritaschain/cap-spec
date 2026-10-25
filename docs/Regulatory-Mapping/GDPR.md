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
| PromptHash | Possibly (pseudonymous) | SHA-256; common or short inputs can be guessed by hashing candidates (see [SECURITY.md](../../SECURITY.md)) |
| ActorHash | Yes, where it can be linked to a person (pseudonymous data) | SHA-256; salting or keyed hashing recommended |
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
| Accuracy | Tamper-evident, append-only records |
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
| Data breach | Hash exposure can still expose personal data where inputs are guessable |

**Important**: A hash cannot be inverted directly, but a short or predictable input can be recovered by hashing candidate inputs. Hashes of personal data are pseudonymous data, which remains personal data under the GDPR.

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
| Authenticity | Ed25519 signatures (signatures are not encryption) |
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

CAP supports crypto-shredding. Crypto-shredding may support erasure obligations under Article 17 but does not itself determine legal compliance (VAP v1.2 §6.3.4):

### How It Works

```
1. Personal data encrypted with per-subject key
2. Encrypted data stored (or hash of encrypted data)
3. Key deletion = effective data deletion
4. Hash chain integrity preserved
5. An erasure record is appended (see below)
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
3. ActorHash remains; whether it can still be linked to the person depends on how it was derived
4. Chain integrity maintained
5. Record the erasure as a new, append-only event. VAP v1.2 §6.3.3 requires an ERASURE event (`erasure_target_event_ids`, `erasure_reason`, `key_destruction_proof`, optional `retention_exemption`, `operator_id`) whenever crypto-shredding is performed. CAP v1.0 does not define that event; this gap is recorded in the [draft conformance mapping](../conformance/CAP-v1.0-VAP-v1.2-Draft3-Conformance-Mapping.md) (D09–D10).

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

**Recommendation**: Consider EU-located anchoring services where transfer rules apply. Anchors normally carry only Merkle roots, not personal data.

---

## Implementation Guidance

### Minimum data-protection measures

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
- [CAP Specification v1.0](../CAP-Specification-v1.0.md)
- [EDPB Guidelines on DPbD](https://edpb.europa.eu/)

---

*Last updated: 2026-10-25 (hash-pseudonymity, erasure-record and framing corrections; earlier text in Git history)*
