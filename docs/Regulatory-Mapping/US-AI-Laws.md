# US Regulatory Mapping

## CAP Alignment with US AI Regulations

This document maps CAP v1.0 capabilities to US federal and state AI regulatory requirements.

---

## 1. TAKE IT DOWN Act (Federal)

**Full Name:** Tools to Address Known Exploitation by Immobilizing Technological Deepfakes on Websites and Networks Act (S. 146, 119th Congress; Pub. L. 119-12)  
**Status:** Signed 2025-05-19; covered platforms had until 2026-05-19 to establish the notice-and-removal process  
**Scope:** Non-consensual intimate imagery (NCII)

### Requirements and CAP Mapping

| Requirement | CAP relevance | Conformance Level |
|-------------|---------------|-------------------|
| Covered platforms remove NCII within 48 hours of a valid request | Not covered: CAP v1.0 defines no removal-request or removal event. GEN_DENY timestamps record generation refusals, not platform removals | — |
| Reasonable efforts to remove known identical copies | Not covered by CAP v1.0 | — |
| Evidence where a generation service is involved | GEN_ATTEMPT / GEN_DENY with NCII_RISK; Evidence Pack export | Silver |

See [US-NCII.md](US-NCII.md) for the corrected summary of the Act.

### CAP Event Flow for NCII-Related Generation Requests

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

**Status:** Enacted 2024; effective date extended to June 30, 2026 by SB25B-004 (signed 2025-08-28). **Repealed and replaced by SB26-189**, signed on 2026-05-14, which regulates automated decision-making technology that materially influences consequential decisions, applies to decisions made on or after 2027-01-01, drops SB24-205's risk-management and impact-assessment requirements, keeps a three-year record-retention duty for developers and deployers, and gives the Attorney General exclusive enforcement (no private right of action). Source: Davis Wright Tremaine analysis (May 2026); the enacted text was not retrieved for this update. The effective date may be affected by pending litigation.  
**This section's mapping below refers to SB24-205 as enacted and is kept for reference. It has not been redone for SB26-189; the impact-assessment rows no longer correspond to a requirement.**  
**Scope:** High-risk AI systems with consequential decisions

### Requirements and CAP Mapping

| Requirement | CAP Implementation | Conformance Level |
|-------------|-------------------|-------------------|
| Impact assessment documentation | Evidence Pack with statistics | Silver |
| 3-year retention of assessments | Retention Framework (Silver: 2yr, Gold: 5yr) | Gold recommended |
| Algorithmic discrimination documentation | RiskCategory: HATE_CONTENT logging | Silver |
| Consumer notification records | EXPORT events with notification flag | Bronze |
| Risk management program | SRP attempt–outcome invariant check (recorded attempts only) | Silver |

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
| **Measure** | RiskScore, SRP attempt–outcome invariant |
| **Manage** | GEN_DENY logging, Evidence Pack |

---

## 3. SEC Rule 17a-4 (Financial AI)

**Scope:** AI systems in securities trading (overlap with VCP)

For financial AI systems, see [VCP Specification](https://github.com/veritaschain/vcp-spec) which addresses SEC requirements directly.

CAP-VCP integration enables:
- Cross-reference between content decisions and trading actions
- Unified audit trail across domains
- Shared VAP infrastructure (conformance to VAP v1.2 has been established for neither CAP v1.0 nor VCP v1.2)

---

## 4. State AI Laws Landscape

| State | Law | Status | CAP Relevance |
|-------|-----|--------|---------------|
| **Colorado** | SB26-189 (replaces SB24-205; see §2) | Signed 2026-05-14; applies from 2027-01-01 | Medium (3-year record retention; impact assessments dropped) |
| **California** | Various pending | Legislative | Medium |
| **Illinois** | BIPA extensions | Enacted | Medium (biometric) |
| **Texas** | HB 2060 | Under review | Low |

Rows other than Colorado have not been re-verified since 2026-01-13.

---

## 5. Federal AI Initiatives

### OMB Memoranda M-25-21 and M-25-22

Federal AI procurement requirements (effective October 2025):

| Requirement | CAP Support |
|-------------|-------------|
| Ongoing testing/monitoring | SRP attempt–outcome invariant check |
| Vendor performance standards | Declared CAP conformance level. Levels are declared by the implementer (CAP v1.0 §2.5); no CAP-specific certification is offered (VC-Certified covers VCP only) and no independent CAB is registered (VAP ERRATA E-2026-10-21). CAP v1.0 calls for third-party audit at Gold (§2.5 item 4; Appendix D.3); an audit is not a certification |
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

### Where the TAKE IT DOWN Act is relevant

1. Implement Silver Level conformance minimum
2. Record GEN_ATTEMPT for all image generation requests
3. Record NCII_RISK refusal decisions as GEN_DENY
4. Keep platform removal-request handling in separate records (not covered by CAP v1.0)
5. Establish Evidence Pack export procedures for legal requests

### Colorado (SB24-205, repealed — retained for reference; not redone for SB26-189)

1. Implement Gold Level conformance recommended
2. Enable impact assessment documentation via Evidence Pack (SB26-189 drops impact assessments)
3. Implement algorithmic discrimination logging (HATE_CONTENT)
4. Configure 3-year retention (Gold Level provides 5 years)
5. Document NIST AI RMF alignment for affirmative defense

---

## References

- [TAKE IT DOWN Act (S. 146, 119th Congress)](https://www.congress.gov/bill/119th-congress/senate-bill/146)
- [Colorado SB24-205](https://leg.colorado.gov/bills/sb24-205)
- [Davis Wright Tremaine, "Colorado AI Act repeal and new transparency law" (May 2026)](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/colorado-ai-act-repeal-new-transparency-law) — summary of SB26-189
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [OMB M-25-21](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf)

---

**Document ID:** VSO-CAP-REG-US-001  
**Version:** 1.0  
**Last Updated:** 2026-10-25 (TAKE IT DOWN Act, invariant and certification wording corrected; earlier text in Git history)
