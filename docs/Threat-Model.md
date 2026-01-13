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

### Integrity Mechanisms

| Mechanism | Threat Mitigated | How |
|-----------|------------------|-----|
| Hash Chain | Evidence tampering | Detects modifications |
| Digital Signature | Event forgery | Authenticates issuer |
| Merkle Anchoring | Timestamp manipulation | Independent proof |
| Completeness Invariant | Selective logging | Ensures all attempts recorded |

---

## SRP-Specific Threats

### Content Moderation Evasion

| Attack | Description | SRP Mitigation |
|--------|-------------|----------------|
| Selective logging | Only log favorable outcomes | Completeness Invariant |
| Backdated refusals | Claim refusal after generation | Timestamp + anchoring |
| Log tampering | Modify refusal records | Hash chain integrity |
| False refusals | Claim refusals that didn't happen | AttemptID linking |

### The Grok Incident Pattern

The December 2025 Grok incident demonstrated:

| Gap | Consequence | SRP Solution |
|-----|-------------|--------------|
| No attempt logging | Can't prove safeguards triggered | GEN_ATTEMPT required |
| No refusal proof | Can't prove content blocked | GEN_DENY with hash chain |
| No completeness check | Could hide allowed generations | Completeness Invariant |
| No external anchoring | Timestamps unverifiable | Merkle root anchoring |

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

1. **Trusted operators**: CAP provides evidence regardless of operator honesty
2. **Network security**: Hash chains detect tampering regardless of transport
3. **Single point of trust**: External anchoring provides independent verification

---

## Implementation Security Considerations

### L1 (Basic) Risks

- No external anchoring → timestamps unverifiable
- Single signature → key compromise fatal
- Local storage → easier tampering

**Recommendation**: Use for low-risk internal workflows only.

### L2 (Standard) Risks

- No external anchoring → timestamps unverifiable
- May lack redundancy

**Recommendation**: Use for medium-risk production workflows.

### L3 (Enterprise) Risks

- Anchor system availability
- Key ceremony complexity
- Operational overhead

**Recommendation**: Required for regulatory compliance and high-stakes evidence.

---

## Residual Risks

CAP cannot mitigate:

| Risk | Reason |
|------|--------|
| Pre-logging attacks | Events before CAP integration |
| Side-channel attacks | Outside event model |
| Quantum computing | Future algorithm break (crypto agility addresses) |
| Collusion | Multiple trusted parties cooperating |
| Physical security | Hardware-level attacks |

---

## Related Documents

- [SECURITY.md](../SECURITY.md) — Vulnerability reporting
- [CAP Specification](CAP-Specification-v0.2.md) — Full specification
- [CAP Glossary](CAP-Glossary.md) — Terminology

---

*Last updated: 2026-01-13*
