# CAP Alignment: US NCII Legislation (TAKE IT DOWN Act)

## Overview

The **TAKE IT DOWN Act** (S.4569, 118th Congress) addresses non-consensual intimate imagery (NCII), including AI-generated deepfakes. This document maps CAP/SRP capabilities to NCII prevention and response requirements.

---

## TAKE IT DOWN Act Summary

### Key Provisions

| Section | Requirement | CAP Relevance |
|---------|-------------|---------------|
| §2 | 48-hour removal obligation | Timestamp evidence |
| §3 | Criminal penalties for distribution | Intent documentation |
| §4 | Civil remedies for victims | Forensic evidence |
| §5 | Platform liability provisions | Moderation evidence |

### Covered Content

The Act covers:
- Non-consensual intimate imagery (NCII)
- AI-generated intimate imagery (deepfakes)
- Digital forgeries depicting real persons

---

## SRP for NCII Prevention

### The Core Problem

| Challenge | Traditional Systems | SRP Solution |
|-----------|-------------------|--------------|
| Prove NCII request blocked | No evidence | GEN_DENY event |
| Prove content never generated | Cannot prove negative | Completeness Invariant |
| Forensic timeline | Limited logging | Hash chain timestamps |
| Victim notification | Manual process | Evidence Pack sharing |

### Risk Categories for NCII

```json
{
  "RiskCategory": "NCII_RISK",
  "RiskSubCategories": [
    "UPLOADED_PERSON",
    "CLOTHING_REMOVAL",
    "NON_CONSENSUAL_INTIMATE"
  ]
}
```

| Category | Description | Severity |
|----------|-------------|----------|
| NCII_RISK | Non-consensual intimate imagery | Critical |
| MINOR_SEXUALIZATION | Sexual content involving minors | Critical |
| REAL_PERSON_DEEPFAKE | Unauthorized real person imagery | High |

---

## 48-Hour Response Evidence

### Timeline Documentation

The Act requires 48-hour response. CAP provides:

```json
{
  "EventType": "GEN_DENY",
  "Timestamp": "2026-01-10T14:23:45.150Z",
  "AttemptID": "...",
  "RiskCategory": "NCII_RISK",
  "RefusalReason": "NCII request detected and blocked",
  "ResponseTimeline": {
    "requestReceived": "2026-01-10T14:23:45.100Z",
    "riskDetected": "2026-01-10T14:23:45.120Z",
    "decisionMade": "2026-01-10T14:23:45.150Z",
    "totalLatency": "50ms"
  }
}
```

### Proof of Non-Generation

| Victim Question | CAP Evidence |
|-----------------|--------------|
| "Was content generated of me?" | GEN_DENY event exists |
| "When was request blocked?" | Timestamp field |
| "Can you prove it was never created?" | Completeness Invariant |
| "Is this evidence authentic?" | Hash chain verification |

---

## Evidence Pack for Victims

### Structure for Legal Proceedings

```
evidence-pack-ncii/
├── manifest.json
├── events/
│   ├── gen_attempt.json      ← Request received
│   └── gen_deny.json         ← Request blocked
├── statistics/
│   └── ncii_prevention.json  ← Aggregate data
├── verification/
│   ├── instructions.md
│   └── chain_verification.py
└── legal/
    └── take_it_down_compliance.md
```

### Shareable Proof

Victims can receive Evidence Pack showing:
1. Request was received (GEN_ATTEMPT)
2. NCII risk detected (RiskCategory)
3. Generation blocked (GEN_DENY)
4. Timeline documented (Timestamps)
5. Chain integrity verified (Hash chain)

---

## Platform Compliance

### Moderation Evidence Requirements

| Platform Obligation | CAP/SRP Support |
|---------------------|-----------------|
| Block NCII generation | GEN_DENY events |
| Document refusals | Evidence Pack |
| Respond within 48 hours | Timestamp proof |
| Preserve evidence | Hash chain immutability |
| Support investigations | Third-party verification |

### Aggregated Statistics

```json
{
  "period": {
    "start": "2026-01-01T00:00:00Z",
    "end": "2026-01-31T23:59:59Z"
  },
  "nciiPrevention": {
    "totalNCIIAttempts": 1523,
    "blocked": 1523,
    "allowed": 0,
    "blockRate": 1.0,
    "averageBlockTime": "45ms"
  },
  "bySubCategory": {
    "UPLOADED_PERSON": 892,
    "CLOTHING_REMOVAL": 456,
    "FACE_SWAP_INTIMATE": 175
  },
  "completenessVerified": true
}
```

---

## Criminal Investigation Support

### Forensic Evidence

| Investigation Need | CAP Evidence |
|-------------------|--------------|
| Request timing | Timestamp (millisecond precision) |
| Request fingerprint | PromptHash (for matching) |
| Actor identification | ActorHash (with legal process) |
| Request pattern | SessionID correlation |
| Model version | ModelVersion field |

### Chain of Custody

1. Events created with hash chain integrity
2. External anchoring provides independent timestamp
3. Evidence Pack exported with verification guide
4. Third-party can independently verify

---

## Child Safety (CSAM Prevention)

### Enhanced Protections

| CSAM Concern | SRP Response |
|--------------|--------------|
| Minor detection | CSAM_RISK category |
| Age estimation | RiskSubCategories detail |
| Immediate blocking | ModelDecision: DENY |
| Zero tolerance | 100% block rate requirement |

### CSAM-Specific Events

```json
{
  "EventType": "GEN_DENY",
  "RiskCategory": "CSAM_RISK",
  "RiskSubCategories": ["MINOR_DETECTED", "SEXUAL_CONTEXT"],
  "RiskScore": 0.99,
  "ModelDecision": "DENY",
  "HumanOverride": false,
  "ImmediateAction": "BLOCKED_AND_LOGGED"
}
```

---

## Implementation Recommendations

### Minimum Compliance

1. Implement GEN_ATTEMPT + GEN_DENY for all requests
2. Use NCII_RISK and CSAM_RISK categories
3. Enable Evidence Pack export for victims
4. Maintain 100% block rate for detected NCII/CSAM

### Enhanced Protection

1. L3 implementation with external anchoring
2. Real-time monitoring dashboards
3. Automated law enforcement notification (where required)
4. Victim notification workflow integration

---

## State Law Considerations

Many US states have additional NCII laws:

| State | Law | CAP Support |
|-------|-----|-------------|
| California | Civil Code §1708.86 | Evidence for civil action |
| New York | Penal Law §245.15 | Criminal investigation support |
| Texas | Penal Code §21.165 | Timeline documentation |
| Florida | FS §784.049 | Victim evidence sharing |

CAP's Evidence Pack format supports multi-jurisdiction compliance.

---

## Disclaimer

This document provides technical capability mapping only. TAKE IT DOWN Act compliance requires comprehensive platform policies, trained moderators, and legal counsel. CAP provides evidentiary infrastructure, not complete compliance.

---

## References

- [TAKE IT DOWN Act (S.4569)](https://www.congress.gov/)
- [NCII Criminal Provisions](https://www.justice.gov/)
- [CAP Specification](../CAP-Specification-v0.2.md)
- [SRP Extension](../CAP-Specification-v0.2.md#12-srp-introduction)

---

*Last updated: 2026-01-13*
