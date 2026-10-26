# CAP Relevance Mapping: EU AI Act

## Overview

The **EU AI Act** (Regulation (EU) 2024/1689), as amended by **Regulation (EU) 2026/1744**
(Digital Omnibus on AI), sets requirements for AI systems placed on the market or used
in the European Union. This document identifies which CAP v1.0 records may be relevant
to which provisions.

This is a relevance mapping, not a compliance mapping. Implementing CAP does not
constitute compliance with the EU AI Act or any other law (VAP v1.2 §1.6, adopted
in the [README](../../README.md)). CAP makes the recorded events auditable and
attributable after the fact; it does not perform, prevent or block any AI behaviour.

> **Revision — 25 October 2026.** This page previously cited Article 53 for content
> transparency, attributed Article 12(3) items to all systems, used the v0.2 levels
> (L2/L3) and event types, and stated application dates that predate Regulation (EU)
> 2026/1744. It has been corrected; see the [Git history](https://github.com/veritaschain/cap-spec/commits/main/docs/Regulatory-Mapping/EU-AI-Act.md) for the earlier text.

---

## Applicable Provisions

### Article 50: Transparency obligations for providers and deployers of certain AI systems

Article 50(2) requires providers of AI systems that generate synthetic audio, image,
video or text content to mark the outputs in a machine-readable format and make them
detectable as artificially generated or manipulated. This is the provision most often
relevant to content and creative AI.

| Provision | CAP record that may be relevant | Note |
|-----------|---------------------------------|------|
| Art. 50(2) marking of generated outputs | GEN event (CAP v1.0 §6.1; output-hash fields such as `OutputAssetHash` exist only in CAP v0.2 and its repository schema), EXPORT event with Asset object (§7.2 `AssetID`, `AssetHash`) | CAP records that an output was generated and exported. It does not itself mark or watermark content; marking is performed by the provider (for example with C2PA manifests) |
| Art. 50(4) disclosure of deep fakes by deployers | EXPORT event | CAP can record export of generated content; the disclosure itself is the deployer's act |

### Article 12: Record-keeping (high-risk AI systems)

Article 12 applies to **high-risk** AI systems. Most content-generation systems are not
high-risk under Article 6; where a system is, the following CAP records may be relevant.

| Provision | CAP record that may be relevant |
|-----------|---------------------------------|
| Art. 12(1) automatic recording of events over the lifetime of the system | Signed, hash-chained CAP events (§7–§8) with external anchoring (§9) |
| Art. 12(2) logging relevant to risk identification, post-market monitoring and operational monitoring | GEN_ATTEMPT / GEN_DENY with `RiskCategory`, `RiskScore`, `PolicyID` (SRP, §12–§14) |
| Art. 12(3)(a)–(d) period of use, reference database, matched input data, verifying persons | Applies **only** to remote biometric identification systems (Annex III point 1(a)); not generally applicable to CAP deployments |

Log retention periods are set by **Article 19(1)** (providers: at least six months,
unless other Union or national law provides otherwise) and **Article 26(6)**
(deployers), not by Article 12. CAP v1.0 §10 states its own minimum retention per
conformance level.

### Article 14: Human oversight

| Oversight aspect | CAP record |
|------------------|------------|
| Identity and role of the person acting | `UserID`, `Role` |
| Override of an automated refusal | `HumanOverride` on GEN_DENY (§14.2) |
| Escalation | `ModelDecision` = `ESCALATE` on GEN_DENY, with `EscalationID` (Appendix A.3). In CAP v1.0, `GEN_ESCALATE` is not an event type; it was a v0.2 event type |

CAP records oversight actions; it does not provide oversight, intervention or override
capability.

### Article 53: Obligations for providers of general-purpose AI models

Article 53 applies to providers of general-purpose AI models (technical documentation,
information for downstream providers, copyright policy, training-content summary). Where
a CAP user is such a provider, INGEST and TRAIN events may help document training-data
provenance. Article 53 is not the content-transparency provision; that is Article 50.

### Article 72: Post-market monitoring (high-risk AI systems)

| Provision | CAP record that may be relevant |
|-----------|---------------------------------|
| Post-market monitoring data | Event chain with timestamps; Evidence Pack manifest `CompletenessVerification` counts (§15.3) |

---

## SRP Extension

| Evidentiary question | What SRP records | Limit |
|----------------------|------------------|-------|
| Was a refusal policy applied to a recorded request? | GEN_ATTEMPT → GEN_DENY linking with `PolicyID` | Does not show that the policy was adequate |
| Does every recorded attempt have a recorded outcome? | SRP attempt–outcome invariant (§13): ∑GEN_ATTEMPT = ∑GEN + ∑GEN_DENY + ∑GEN_ERROR | Covers recorded attempts only. A request that was never recorded leaves nothing to detect (pre-measurement drop, VAP v1.2 Appendix A). This profile-level invariant is distinct from the VAP v1.2 Completeness Invariant (INT-008) |
| Can the records be checked by a third party? | Evidence Pack (§15) | Subject to trusted keys and anchors |

---

## Conformance levels

CAP v1.0 defines Bronze, Silver and Gold (§2). Silver adds daily external anchoring and
SRP; Gold adds hourly anchoring and HSM-protected keys. In CAP v1.0, external anchoring is
optional at Bronze; VAP v1.2 (INT-006) requires it at every conformance level, so a
Bronze deployment cannot be described as meeting the VAP v1.2 requirement set (see the
[README](../../README.md)). Levels are declared by the implementer (§2.5); no
CAP-specific certification is offered (VC-Certified covers VCP only) and no independent
CAB is registered (VAP ERRATA E-2026-10-21). CAP v1.0 calls for third-party audit at Gold
(§2.5 item 4; Appendix D.3, annual); an audit is not a certification.

---

## Application dates

| Provision | Applies from | Source |
|-----------|--------------|--------|
| Prohibited practices (Art. 5) | 2 February 2025 | Regulation (EU) 2024/1689, Art. 113 |
| General-purpose AI model obligations (Chapter V, incl. Art. 53) | 2 August 2025 | Regulation (EU) 2024/1689, Art. 113 |
| Transparency obligations (Art. 50) | 2 August 2026 | Regulation (EU) 2024/1689, Art. 113 |
| Art. 50(2) marking, for systems placed on the market before 2 August 2026 | 2 December 2026 | Art. 111(4), inserted by Regulation (EU) 2026/1744 |
| High-risk obligations for systems classified under Art. 6(2) and Annex III | 2 December 2027 | Art. 113, third paragraph, point (c), as amended by Regulation (EU) 2026/1744 |
| High-risk obligations for systems classified under Art. 6(1) and Annex I | 2 August 2028 | Same |

Dates are stated as of 25 October 2026 and may change; confirm them against the
Official Journal of the European Union.

---

## Disclaimer

This document provides a technical relevance mapping only. It does not constitute legal
advice or a compliance determination. Consult legal counsel for jurisdiction-specific
requirements.

---

## References

- [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj)
- [CAP Specification v1.0](../CAP-Specification-v1.0.md)
- [SRP Introduction (§11)](../CAP-Specification-v1.0.md#11-srp-introduction)
- [VAP v1.2 Draft 3](https://github.com/veritaschain/vap-spec/blob/main/spec/v1.2/VAP_Framework_Specification.md)

---

*Last updated: 2026-10-25*
