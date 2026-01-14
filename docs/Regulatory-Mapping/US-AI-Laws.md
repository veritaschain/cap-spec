# US Regulatory Mapping

## CAP Alignment with US AI Regulations

This document maps CAP v1.0 capabilities to US federal and state AI regulatory requirements.

---

## 1. TAKE IT DOWN Act (Federal)

**Full Name:** Tools to Address Known Exploitation of Images Today Act  
**Status:** Enacted, Platform compliance deadline May 2026  
**Scope:** Non-consensual intimate imagery (NCII)

### Requirements and CAP Mapping

| Requirement | CAP Implementation | Conformance Level |
|-------------|-------------------|-------------------|
| Remove NCII within 48 hours of notice | Timestamp verification via GEN_DENY | Silver |
| Document removal actions | GEN_DENY with NCII_RISK category | Silver |
| Prevent re-upload | Hash-based detection logging | Silver |
| Evidence for legal proceedings | Evidence Pack export | Silver |

### CAP Event Flow for NCII Prevention

```
NCII Request Detected
        │
        ▼
┌───────────────────┐
│   GEN_ATTEMPT     │ ← Records request receipt timestamp
│   InputType: image│
│   PolicyID: ncii  │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│    GEN_DENY       │ ← Records refusal with evidence
│ RiskCategory:     │
│   NCII_RISK       │
│ RiskSubCategories:│
│   [REAL_PERSON,   │
│    INTIMATE_REQ]  │
└───────────────────┘
```

---

## 2. Colorado AI Act (SB24-205)

**Status:** Enacted, Effective February 1, 2026  
**Scope:** High-risk AI systems with consequential decisions

### Requirements and CAP Mapping

| Requirement | CAP Implementation | Conformance Level |
|-------------|-------------------|-------------------|
| Impact assessment documentation | Evidence Pack with statistics | Silver |
| 3-year retention of assessments | Retention Framework (Silver: 2yr, Gold: 5yr) | Gold recommended |
| Algorithmic discrimination documentation | RiskCategory: HATE_CONTENT logging | Silver |
| Consumer notification records | EXPORT events with notification flag | Bronze |
| Risk management program | Completeness Invariant verification | Silver |

### Deployer Obligations Mapping

| SB24-205 Section | Requirement | CAP Feature |
|------------------|-------------|-------------|
| §6-1-1702(2)(a) | Risk management policy | PolicyID, PolicyVersion fields |
| §6-1-1702(2)(b) | Impact assessment | Evidence Pack statistics |
| §6-1-1702(2)(c) | Data governance | Rights.ConsentBasis tracking |
| §6-1-1702(2)(d) | Human oversight | HumanOverride field |
| §6-1-1702(3) | Consumer disclosure | EXPORT event logging |

### Affirmative Defense via NIST AI RMF

Colorado AI Act provides affirmative defense for NIST AI RMF compliance. CAP supports this through:

| NIST AI RMF Function | CAP Implementation |
|---------------------|-------------------|
| **Govern** | GOVERNANCE.md, PolicyID tracking |
| **Map** | Threat-Model.md, RiskCategory taxonomy |
| **Measure** | RiskScore, Completeness Invariant |
| **Manage** | GEN_DENY logging, Evidence Pack |

---

## 3. SEC Rule 17a-4 (Financial AI)

**Scope:** AI systems in securities trading (overlap with VCP)

For financial AI systems, see [VCP Specification](https://github.com/veritaschain/vcp-spec) which addresses SEC requirements directly.

CAP-VCP integration enables:
- Cross-reference between content decisions and trading actions
- Unified audit trail across domains
- Shared VAP v1.2 infrastructure

---

## 4. State AI Laws Landscape

| State | Law | Status | CAP Relevance |
|-------|-----|--------|---------------|
| **Colorado** | SB24-205 | Effective Feb 2026 | High (impact assessments) |
| **California** | Various pending | Legislative | Medium |
| **Illinois** | BIPA extensions | Enacted | Medium (biometric) |
| **Texas** | HB 2060 | Under review | Low |

---

## 5. Federal AI Initiatives

### OMB Memoranda M-25-21 and M-25-22

Federal AI procurement requirements (effective October 2025):

| Requirement | CAP Support |
|-------------|-------------|
| Ongoing testing/monitoring | Completeness Invariant verification |
| Vendor performance standards | Conformance Level certification |
| Risk management practices | Evidence Pack documentation |

### NIST AI RMF Integration

CAP provides technical implementation for NIST AI RMF requirements:

```
NIST AI RMF                    CAP Implementation
───────────────                ──────────────────
Govern 1.1 (Legal compliance)  → Regulatory-Mapping docs
Map 1.1 (Context establishment)→ Threat-Model.md
Measure 2.1 (AI risks)         → RiskCategory, RiskScore
Manage 1.1 (Risk priorities)   → PolicyID, GEN_DENY logging
```

---

## Implementation Recommendations

### For TAKE IT DOWN Act Compliance

1. Implement Silver Level conformance minimum
2. Enable GEN_ATTEMPT logging for all image generation requests
3. Implement NCII_RISK detection and GEN_DENY logging
4. Configure 48-hour evidence retrieval capability
5. Establish Evidence Pack export procedures for legal requests

### For Colorado AI Act Compliance

1. Implement Gold Level conformance recommended
2. Enable impact assessment documentation via Evidence Pack
3. Implement algorithmic discrimination logging (HATE_CONTENT)
4. Configure 3-year retention (Gold Level provides 5 years)
5. Document NIST AI RMF alignment for affirmative defense

---

## References

- [TAKE IT DOWN Act](https://www.congress.gov/bill/118th-congress/senate-bill/4569)
- [Colorado SB24-205](https://leg.colorado.gov/bills/sb24-205)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [OMB M-25-21](https://www.whitehouse.gov/omb/information-regulatory-affairs/)

---

**Document ID:** VSO-CAP-REG-US-001  
**Version:** 1.0  
**Last Updated:** 2026-01-13
