# CAP Alignment: EU AI Act

## Overview

The **EU AI Act** (Regulation (EU) 2024/1689) establishes comprehensive requirements for AI systems deployed in the European Union. This document maps CAP capabilities to relevant EU AI Act provisions.

---

## Applicable Articles

### Article 12: Record-Keeping (Logging)

High-risk AI systems must enable automatic recording of events ("logs").

| Requirement | CAP Implementation | Status |
|-------------|-------------------|--------|
| Automatic event logging | EventID, Timestamp auto-generated | ✓ Supported |
| Logging period (start/end) | Evidence Pack period field | ✓ Supported |
| Input data reference | AssetID, AssetHash, PromptHash | ✓ Supported |
| Reference database/dataset | ModelContext, TrainingType | ✓ Supported |
| Output identification | OutputAssetID, OutputAssetHash | ✓ Supported |
| Human oversight activities | UserID, Role, HumanOverride | ✓ Supported |
| Retention for AI lifetime | Hash chain + external anchoring | ✓ Supported |
| Risk identification | RiskCategory, RiskScore | ✓ Supported (SRP) |

### Article 14: Human Oversight

| Requirement | CAP Implementation |
|-------------|-------------------|
| Human oversight records | UserID, Role fields |
| Override documentation | HumanOverride field in GEN_DENY |
| Escalation tracking | GEN_ESCALATE event type |
| Audit trail of interventions | Event chain with timestamps |

### Article 53: Transparency Obligations

| Requirement | CAP Implementation |
|-------------|-------------------|
| AI system identification | ModelContext fields |
| Provider identification | Signature with public key |
| Technical documentation | Evidence Pack structure |
| Instruction provision | verification/instructions.md |

### Article 72: Post-Market Monitoring

| Requirement | CAP Implementation |
|-------------|-------------------|
| Continuous monitoring data | Real-time event logging |
| Incident documentation | Event chain with context |
| Trend analysis support | statistics/refusal_stats.json |

---

## SRP Extension Alignment

The SRP extension specifically addresses content moderation evidence requirements:

| EU AI Act Concern | SRP Capability |
|-------------------|----------------|
| Prove safety measures exist | GEN_DENY events |
| Prove measures were applied | GEN_ATTEMPT → GEN_DENY linking |
| Prove completeness | Completeness Invariant |
| Auditable records | Evidence Pack |

---

## High-Risk AI Categories

CAP is particularly relevant for these EU AI Act high-risk categories:

| Category | Annex III Reference | CAP Application |
|----------|--------------------|-----------------| 
| Biometric identification | 1(a) | Deepfake detection evidence |
| Critical infrastructure | 2 | Content system audit trails |
| Education/training | 3 | Training material provenance |
| Employment | 4 | AI-generated content in hiring |
| Essential services | 5 | Content moderation in platforms |

---

## Implementation Levels

### Minimum Compliance (L2)

For EU AI Act compliance, implementations SHOULD:
- Log all events in hash chain
- Include all Article 12 fields
- Retain logs for system lifetime
- Enable third-party verification

### Recommended (L3)

For robust compliance, implementations SHOULD also:
- Use external anchoring (Merkle roots)
- Implement SRP for content moderation
- Generate Evidence Packs for auditors
- Support crypto agility for future requirements

---

## Regulatory Submission Support

### Documentation Package

CAP Evidence Packs can support regulatory submissions:

```
evidence-pack/
├── manifest.json           # Pack metadata
├── events/                 # Logged events
├── statistics/            
│   └── refusal_stats.json  # Article 72 monitoring
├── verification/
│   └── instructions.md     # Article 53 transparency
└── regulatory/
    └── eu-ai-act-mapping.json  # Article mappings
```

### Audit Readiness

| Auditor Need | CAP Provision |
|--------------|---------------|
| Event completeness | Completeness Invariant |
| Timestamp verification | External anchoring |
| Chain integrity | Hash chain verification |
| Statistics summary | refusal_stats.json |

---

## Timeline Considerations

| EU AI Act Milestone | Date | CAP Readiness |
|--------------------|------|---------------|
| Prohibited practices | Feb 2025 | Logging available |
| GPAI transparency | Aug 2025 | Evidence Packs |
| High-risk compliance | Aug 2027 | Full L3 support |

---

## Disclaimer

This document provides technical capability mapping only. It does not constitute legal advice. Consult legal counsel for jurisdiction-specific compliance requirements.

---

## References

- [EU AI Act Full Text](https://eur-lex.europa.eu/eli/reg/2024/1689)
- [CAP Specification](../CAP-Specification-v0.2.md)
- [SRP Extension](../CAP-Specification-v0.2.md#12-srp-introduction)

---

*Last updated: 2026-01-13*
