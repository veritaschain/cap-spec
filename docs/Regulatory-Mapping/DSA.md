# CAP Alignment: Digital Services Act (DSA)

## Overview

The **Digital Services Act** (Regulation (EU) 2022/2065) establishes obligations for digital service providers, including content moderation transparency and systemic risk mitigation. This document maps CAP/SRP capabilities to DSA requirements.

---

## Applicable Articles

### Article 15: Transparency Reporting

Very large online platforms (VLOPs) must publish transparency reports on content moderation.

| Requirement | CAP Implementation | Status |
|-------------|-------------------|--------|
| Number of content moderation decisions | refusal_stats.json counts | ✓ Supported |
| Categories of moderation | RiskCategory taxonomy | ✓ Supported |
| Automated vs human decisions | HumanOverride field | ✓ Supported |
| Time for decision | Timestamp precision | ✓ Supported |
| Accuracy of automated tools | RiskScore field | ✓ Supported |

### Article 34: Risk Assessment

VLOPs must assess systemic risks from their services.

| Risk Category | CAP Evidence |
|---------------|--------------|
| Illegal content dissemination | GEN_DENY events by category |
| Fundamental rights impacts | Evidence of moderation decisions |
| Electoral/civic discourse | RiskCategory tracking |
| Public security | VIOLENCE_EXTREME, TERRORIST_CONTENT |
| Minors' wellbeing | CSAM_RISK, MINOR_SEXUALIZATION |

### Article 35: Risk Mitigation Measures

VLOPs must implement reasonable mitigation measures.

| Requirement | SRP Capability |
|-------------|----------------|
| Record that a refusal policy exists | GEN_DENY events with `PolicyID` |
| Record that it was applied to recorded requests | GEN_ATTEMPT → GEN_DENY linking |
| Show every recorded attempt has a recorded outcome | SRP attempt–outcome invariant (CAP v1.0 §13). This does not measure effectiveness, and a request never recorded leaves nothing to detect |
| Provide audit evidence | Evidence Pack |

### Article 37: Independent Audits

VLOPs must undergo independent audits.

| Auditor Need | CAP/SRP Provision |
|--------------|-------------------|
| Access to logs | Evidence Pack export |
| Verification capability | Third-party verification guide |
| Statistical analysis | refusal_stats.json |
| Outcome check over recorded attempts | SRP attempt–outcome invariant (§13) |

### Article 40: Data Access for Research

Vetted researchers may access platform data.

| Research Need | CAP Support |
|---------------|-------------|
| Anonymized data | ActorHash, PromptHash |
| Moderation patterns | Aggregated statistics |
| Temporal analysis | Timestamp precision |
| Category breakdown | RiskCategory enumeration |

---

## SRP Evidence Relevant to the DSA

The SRP extension produces records that may be relevant to DSA risk-mitigation and audit work. It does not itself determine compliance (VAP v1.2 §1.6), and it does not block content; blocking is performed by the platform.

### Records of Moderation Decisions

Platforms commonly state that moderation took place without a record a third party can check. SRP records refusal decisions so that such statements can be checked against recorded events.

| DSA Question | SRP Answer |
|--------------|------------|
| "Which recorded requests were refused?" | GEN_DENY events with risk categories |
| "How many recorded requests were refused?" | refusal_stats.json totals |
| "Does every recorded attempt have a recorded outcome?" | SRP attempt–outcome invariant check (recorded attempts only) |
| "Are these records authentic?" | Hash chain + signatures |

### Evidence Pack for DSA Auditors

```
evidence-pack-dsa/
├── manifest.json
├── events/
│   ├── 0001-gen_attempt.json
│   ├── 0002-gen_deny.json
│   └── ...
├── statistics/
│   └── refusal_stats.json    ← Primary DSA focus
├── verification/
│   └── instructions.md
└── dsa-report/
    └── article-15-transparency.json
```

### Statistics for Article 15 Reports

```json
{
  "reportingPeriod": {
    "start": "2026-01-01T00:00:00Z",
    "end": "2026-06-30T23:59:59Z"
  },
  "moderationDecisions": {
    "total": 2847,
    "automated": 2834,
    "humanReview": 13,
    "humanOverride": 3
  },
  "byCategory": {
    "CSAM_RISK": 12,
    "NCII_RISK": 1523,
    "MINOR_SEXUALIZATION": 89,
    "REAL_PERSON_DEEPFAKE": 956,
    "VIOLENCE_EXTREME": 124,
    "HATE_CONTENT": 98,
    "TERRORIST_CONTENT": 0,
    "SELF_HARM_PROMOTION": 0,
    "OTHER": 45
  },
  "averageDecisionTime": "50ms",
  "attemptOutcomeInvariant": "VALID (recorded attempts only)"
}
```

---

## Very Large Online Platform (VLOP) Focus

DSA imposes enhanced obligations on VLOPs (>45M EU monthly users).

| VLOP Obligation | CAP/SRP Support |
|-----------------|-----------------|
| Enhanced transparency | Detailed refusal_stats |
| Annual audits | Evidence Pack + verification |
| Systemic risk assessment | RiskCategory analysis |
| Crisis response | Real-time event logging |
| Researcher access | Anonymized data export |

---

## Generative AI Considerations

DSA applies to AI-generated content distributed via platforms:

| Concern | CAP/SRP Capability |
|---------|-------------------|
| AI-generated illegal content | GEN_DENY records for refused generations |
| Deepfakes | REAL_PERSON_DEEPFAKE category |
| CSAM generation | CSAM_RISK refusal records |
| Disinformation | Event chain provenance |

---

## Implementation Recommendations

### Minimum for DSA

- Implement GEN_ATTEMPT and GEN_DENY events
- Generate refusal_stats.json for reporting
- Enable Evidence Pack export for auditors

### Recommended for VLOPs

- Silver or Gold conformance level (external anchoring daily or hourly)
- Real-time statistics aggregation
- Automated Article 15 report generation
- Researcher-accessible anonymized exports

---

## Disclaimer

This document provides technical capability mapping only. It does not constitute legal advice. DSA compliance requires holistic organizational measures beyond technical logging.

---

## References

- [Digital Services Act Full Text](https://eur-lex.europa.eu/eli/reg/2022/2065)
- [CAP Specification v1.0](../CAP-Specification-v1.0.md)
- [SRP Introduction (§11)](../CAP-Specification-v1.0.md#11-srp-introduction)

---

*Last updated: 2026-10-25 (framing and level corrections; earlier text in Git history)*
