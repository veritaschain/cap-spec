# CAP Threat Model

## Overview

This document provides a comprehensive threat analysis for CAP (Content/Creative AI Profile) implementations. It identifies threats, actors, attack surfaces, and CAP's mitigations.

---

## Threat Taxonomy

CAP addresses five primary threat categories in AI content workflows:

```
┌─────────────────────────────────────────────────────────────────┐
│                      CAP Threat Taxonomy                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  TH-1: IP Dilution                                              │
│  ├─ Unique style/worldview easily mimicked by AI                │
│  └─ Brand value erosion, market differentiation difficulty      │
│                                                                 │
│  TH-2: Reverse Flow (Rights Infringement via Outflow)           │
│  ├─ Third parties use AI trained on proprietary materials       │
│  └─ Near-identical generated outputs appear in market           │
│                                                                 │
│  TH-3: Confidential Leakage                                     │
│  ├─ Unreleased characters/designs/footage/code fed to AI        │
│  └─ Leakage via training data pathways                          │
│                                                                 │
│  TH-4: Deepfake / Persona Abuse                                 │
│  ├─ Private images/video used without consent                   │
│  └─ Defamation, sexual content, harassment                      │
│                                                                 │
│  TH-5: Brand/Style Mimicry                                      │
│  ├─ Corporate web/IR/design tone imitated                       │
│  └─ Generated content mistaken for official                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Threat Actor Analysis

### Actor Categories

| Actor | Description | Motivation | Capability |
|-------|-------------|------------|------------|
| **External Attackers** | Malicious third parties | Financial gain, reputation damage | Variable |
| **Internal Actors** | Employees, contractors | Negligence, malice, espionage | High access |
| **AI Vendors** | Model providers, SaaS | Data harvesting, competitive intel | System access |
| **End Users** | Generative AI service users | Content theft, harassment | Low-medium |
| **Competitors** | Industry rivals | Market advantage | Targeted |

### Actor-Threat Mapping

| Actor | TH-1 | TH-2 | TH-3 | TH-4 | TH-5 |
|-------|------|------|------|------|------|
| External Attackers | | ✓ | | ✓ | ✓ |
| Internal Actors | | ✓ | ✓ | | |
| AI Vendors | | ✓ | ✓ | | |
| End Users | ✓ | | | ✓ | ✓ |
| Competitors | ✓ | ✓ | | | ✓ |

---

## Attack Surface Analysis

### Lifecycle-Based Attack Surface

```
Asset Input       Training        Generation       Distribution
(INGEST)          (TRAIN)         (GEN)            (EXPORT)
    │                │                │                │
    ▼                ▼                ▼                ▼
┌────────┐      ┌────────┐      ┌────────┐      ┌────────┐
│ Rights │      │Consent │      │Similarity│     │ Leak   │
│Unclear │      │Violation│     │ Issues  │      │ Path   │
└────────┘      └────────┘      └────────┘      └────────┘
    │                │                │                │
    ▼                ▼                ▼                ▼
TH-1,TH-3        TH-2,TH-3        TH-1,TH-4        TH-2,TH-5
```

### Attack Vectors

#### INGEST Phase
| Vector | Description | Threats |
|--------|-------------|---------|
| Unauthorized ingestion | Materials fed without rights | TH-1, TH-2 |
| Classification bypass | Confidential assets not marked | TH-3 |
| Consent forgery | False consent claims | TH-4 |

#### TRAIN Phase
| Vector | Description | Threats |
|--------|-------------|---------|
| Opt-out bypass | Training despite creator refusal | TH-2 |
| Data exfiltration | Training data extracted | TH-3 |
| Model poisoning | Malicious training injection | TH-5 |

#### GEN Phase
| Vector | Description | Threats |
|--------|-------------|---------|
| Style extraction | Generating mimicking content | TH-1 |
| Deepfake generation | Unauthorized person imagery | TH-4 |
| Selective logging | Hiding harmful generations | TH-4 |

#### EXPORT Phase
| Vector | Description | Threats |
|--------|-------------|---------|
| Distribution leakage | Content escapes controls | TH-2, TH-3 |
| Attribution stripping | Provenance removed | TH-5 |
| Audit trail tampering | Evidence modified | All |

---

## CAP Mitigations

### Threat-to-Field Mapping

CAP fields provide evidence for investigation and deterrence:

| Threat | Mitigation Fields | Evidence Captured |
|--------|-------------------|-------------------|
| TH-1: IP Dilution | AssetID, AssetHash, RightsBasis | Original asset identification |
| TH-2: Reverse Flow | AssetID, ModelContext, TrainingType | Training provenance |
| TH-3: Confidential Leak | ConfidentialityLevel, Timestamp, UserID | Access timing and actor |
| TH-4: Persona Abuse | ConsentBasis, GEN_ATTEMPT, GEN_DENY | Consent state and moderation |
| TH-5: Brand Mimicry | AssetHash, PromptHash, OutputAssetHash | Input/output fingerprints |

`TrainingType`, `ConfidentialityLevel` and `OutputAssetHash` are CAP v0.2 fields (v0.2 repository
schemas); CAP v1.0 does not define them.

### Integrity Mechanisms

| Mechanism | Threat Mitigated | How |
|-----------|------------------|-----|
| Hash Chain | Evidence tampering | Detects modifications |
| Digital Signature | Event forgery | Authenticates issuer |
| Merkle Anchoring | Timestamp manipulation | Independent proof |
| SRP attempt–outcome invariant | Selective omission of recorded outcomes | Detects recorded attempts without a recorded outcome; cannot detect attempts that were never recorded |

---

## SRP-Specific Threats

### Content Moderation Evasion

| Attack | Description | SRP Mitigation |
|--------|-------------|----------------|
| Selective logging | Only log favorable outcomes | SRP attempt–outcome invariant (recorded attempts only; GEN_ATTEMPT must be recorded before evaluation) |
| Backdated refusals | Claim refusal after generation | Timestamp + anchoring |
| Log tampering | Modify refusal records | Hash chain integrity |
| False refusals | Claim refusals that didn't happen | AttemptID linking |

### Illustrative Gap Pattern

Public controversy over AI image generation in December 2025 (including Grok) illustrated a general evidentiary gap: a provider's statement that safeguards worked could not be checked by a third party. VSO has not examined any provider's internal records; the table below describes the general pattern, not the facts of any case.

| Gap | Consequence | What SRP records |
|-----|-------------|------------------|
| No attempt record | Safeguard activation cannot be checked | GEN_ATTEMPT, recorded before evaluation |
| No refusal record | Refusal statements cannot be checked | GEN_DENY in the hash chain |
| No outcome check | Omitted outcomes go unnoticed | SRP attempt–outcome invariant over recorded attempts |
| No external anchoring | Record times depend on the producer | Merkle root anchoring |

SRP records decisions; it does not block generation, and it cannot reveal requests that were never recorded.

---

## Threat Severity Assessment

### STRIDE Classification

| Threat | Spoofing | Tampering | Repudiation | Information Disclosure | DoS | Elevation |
|--------|----------|-----------|-------------|----------------------|-----|-----------|
| TH-1 IP Dilution | | | ✓ | ✓ | | |
| TH-2 Reverse Flow | | | ✓ | ✓ | | |
| TH-3 Confidential Leak | | | | ✓ | | |
| TH-4 Deepfake | ✓ | | ✓ | | | |
| TH-5 Brand Mimicry | ✓ | | | | | |

### Risk Matrix

| Threat | Likelihood | Impact | Risk Level |
|--------|------------|--------|------------|
| TH-1 IP Dilution | High | Medium | High |
| TH-2 Reverse Flow | Medium | High | High |
| TH-3 Confidential Leak | Medium | Very High | Critical |
| TH-4 Deepfake | High | Very High | Critical |
| TH-5 Brand Mimicry | Medium | Medium | Medium |

---

## Security Assumptions

### What CAP Assumes

1. **Cryptographic primitive security**: SHA-256 and Ed25519 remain unbroken
2. **Time source reliability**: Timestamps are reasonably accurate
3. **Key management**: Signing keys are properly protected
4. **Storage integrity**: Append-only storage or equivalent controls

### What CAP Does NOT Assume

1. **Trusted operators**: for anchored records (Silver/Gold), given trusted keys and anchors and subject to [draft mapping](conformance/CAP-v1.0-VAP-v1.2-Draft3-Conformance-Mapping.md) I16/I27, alteration and post-anchor omission of recorded events are detectable without relying on operator honesty. An operator can still fail to record an event in the first place (see Residual Risks)
2. **Network security**: Hash chains detect tampering regardless of transport
3. **Single point of trust**: External anchoring provides independent verification

---

## Implementation Security Considerations

CAP v1.0 defines Bronze, Silver and Gold conformance levels (§2). The L1/L2/L3 levels of CAP v0.2 are superseded.

### Bronze Risks

- External anchoring optional in CAP v1.0 → timestamps depend on the producer. VAP v1.2 (INT-006) requires external anchoring at every level, so Bronze without anchoring does not meet the VAP v1.2 requirement set (see the [README](../README.md))
- Software-held keys → key compromise affects all events
- Local storage → easier tampering before detection

**Recommendation**: Use for low-risk internal workflows only.

### Silver Risks

- Daily anchoring → batch-level completeness only, with a gap of up to 24 hours
- May lack redundancy

**Recommendation**: Use for production workflows.

### Gold Risks

- Anchor system availability
- HSM and key ceremony complexity
- Operational overhead

**Recommendation**: Recommended for high-stakes evidence. No level constitutes regulatory compliance (VAP v1.2 §1.6).

---

## Residual Risks

CAP cannot mitigate:

| Risk | Reason |
|------|--------|
| Pre-logging attacks | Events before CAP integration |
| Unrecorded requests | A request never recorded as GEN_ATTEMPT leaves nothing to detect (pre-measurement drop) |
| Side-channel attacks | Outside event model |
| Quantum computing | Future algorithm break (crypto agility addresses) |
| Collusion | Multiple trusted parties cooperating |
| Physical security | Hardware-level attacks |

---

## Related Documents

- [SECURITY.md](../SECURITY.md) — Vulnerability reporting
- [CAP Specification v1.0](CAP-Specification-v1.0.md) — Full specification
- [CAP Glossary](CAP-Glossary.md) — Terminology

---

*Last updated: 2026-10-25*
