# Content / Creative AI Profile (CAP)

> **Cryptographic Audit Trails for AI Content Systems**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Specification](https://img.shields.io/badge/spec-v1.0%20Released-blue.svg)](docs/CAP-Specification-v1.0.md)
[![VAP](https://img.shields.io/badge/VAP-profile-orange.svg)](https://github.com/veritaschain/vap-spec)
[![GitHub](https://img.shields.io/badge/GitHub-veritaschain-181717.svg?logo=github)](https://github.com/veritaschain)

---

## CAP v1.0 Release

**January 13, 2026** — CAP v1.0 was released (tag `v1.0`), featuring:

- **Conformance Levels** (Bronze/Silver/Gold)
- **External Anchoring Specification** for independent timestamp verification
- **C2PA/SCITT Integration** for ecosystem interoperability
- **Regulatory relevance mapping** (EU AI Act, DSA, Colorado AI Act, TAKE IT DOWN Act) — not compliance determinations

📄 [Full Specification](docs/CAP-Specification-v1.0.md) | 📋 [Changelog](docs/CHANGELOG.md) | 📚 [Academic Paper](https://doi.org/10.5281/zenodo.18213616)

---

## Implementation Status (mandatory disclosure)

As of 25 October 2026: **zero external implementations** of CAP or any other VAP profile, and **zero Evidence Packs accepted in any proceeding**. How these items will be counted is set out in VSO's [proposed counting criteria](https://github.com/veritaschain/vap-spec/blob/main/disclosures/2026-10-24-counting-criteria.md).

**Commercial disclosure correction — 24 October 2026:** the previously published paid-service contract figure and associated commercial details have not been substantiated through reconciliation with primary records. The claim is withdrawn pending verification; this does **not** establish a count of zero. No verified contract count, customer count or revenue figure is asserted here. Commercial activity is separate from external implementation, independent validation and Evidence Pack acceptance. See the [dated correction and counting criteria](https://github.com/veritaschain/vap-spec/blob/main/disclosures/2026-10-24-commercial-contracts.md). Fixed distributions and historical evidence remain unchanged.

The reference implementation below is first-party: VSO and VeritasChain Co., Ltd. share a founder.

**VAP v1.2 status.** CAP v1.0 predates VAP v1.2. A [draft conformance mapping against VAP v1.2 Draft 3](docs/conformance/CAP-v1.0-VAP-v1.2-Draft3-Conformance-Mapping.md) and an [unadopted change proposal](docs/conformance/CAP-VAP-v1.2-Minimal-Change-Proposal.md) are available for review. The mapping identifies unresolved normative divergences, including Bronze external anchoring and shared batch-verification, continuity, policy and data-model requirements. **CAP v1.0 conformance to VAP v1.2 has not been established.** Publication of these review documents is not a conformance declaration or certification. The released CAP v1.0 specification remains unchanged.

**Completeness Invariant wording.** The released CAP v1.0 text describes the Completeness Invariant as a "mathematical guarantee that all attempts have outcomes". The invariant is checked over recorded events: it can show that a recorded attempt has no recorded outcome, but it cannot show that an attempt that was never recorded took place. VAP v1.2 Draft 3 claims omission-evidence only at anchor granularity, not as mathematical completeness (§4.1.7; Appendix A, "Pre-measurement drop"). The released text is unchanged.

---

## Known issues in the released CAP v1.0 text (informative)

The released text ([`docs/CAP-Specification-v1.0.md`](docs/CAP-Specification-v1.0.md), tag `v1.0`) is not edited in place. The following passages are not current; they are errata candidates for the next revision. Recorded on 25 October 2026 unless stated otherwise.

| Location | Issue |
|----------|-------|
| §3.1 diagram | Describes VSO as an "Independent standards body". VSO is operated by VeritasChain Co., Ltd.; its neutrality rests on published mechanisms, not on legal form ([GOVERNANCE.md](GOVERNANCE.md)). The diagram's statuses date from January 2026 (VCP "v1.1", DVP "draft"); current statuses are in the VAP v1.2 registry (§4.5.2): VCP v1.2 Released, DVP Planned |
| Abstract, §1.3, §13.1, Part III, §18.2, §20 | "Completeness Invariant ensuring all attempts have recorded outcomes", "the foundational guarantee of SRP", "it enables compliance with regulations", "Regulatory Compliance", "CAP Compliance Mapping", "Prevention documentation". The invariant is checked over recorded events and cannot show that an unrecorded request took place; CAP records decisions and prevents nothing; conformance is not compliance (VAP v1.2 §1.6, §4.1.7, Appendix A "Pre-measurement drop"). The "mathematical guarantee" wording is noted above |
| §10.2, §18.3, Appendix C.1 | Attribute a six-month retention period to "Article 12(4)" and list Article 12 items as 12(2)(a)–(d). Article 12 of Regulation (EU) 2024/1689 has three paragraphs; the items on period of use, reference database, matched input data and verifying persons are Article 12(3) and apply only to remote biometric identification systems (Annex III point 1(a)); minimum log retention is set by Article 19(1) (providers) and Article 26(6) (deployers) |
| §18.4, §21.1 | Application dates predate Regulation (EU) 2026/1744. High-risk obligations apply from 2 December 2027 (Article 6(2), Annex III) and 2 August 2028 (Article 6(1), Annex I); Article 50 transparency applies from 2 August 2026 (Article 50(2) from 2 December 2026 for systems already on the market); prohibited practices applied from 2 February 2025. See [EU-AI-Act.md](docs/Regulatory-Mapping/EU-AI-Act.md). The Colorado and TAKE IT DOWN rows are superseded by the notes in the regulatory table below |
| §23.3 | "draft-kamimura-scitt-cap (planned)" was not submitted. The related individual Internet-Draft is [`draft-kamimura-scitt-refusal-events`](https://datatracker.ietf.org/doc/draft-kamimura-scitt-refusal-events/) (revision -04, 2026-10-24), not adopted by any IETF Working Group |
| Informative References | "[SCITT] draft-ietf-scitt-architecture" is now RFC 9943 (June 2026). "[VAP] … v1.1" and "[VCP] … v1.1": current versions are VAP v1.2 (Draft 3) and VCP v1.2 (Released) |
| §8.2, §8.3 | §8.2 excludes only `Signature` from the hashed form; the test vectors exclude `EventHash` and `Signature` (draft mapping I04). §8.3 signs the raw 32-byte digest; the [signature test vector](test-vectors/signature/) follows §8.3 |
| §6 event model vs VAP v1.2 §4.3.4 | VAP lists "Transformation" in the CAP causal chain; CAP v1.0 defines no transformation event. To be resolved in the conformance mapping |

---

## Research Records

- **World-First Claims Verification: Final Consolidated Research Report** (historical research record)  
  https://github.com/veritaschain/cap-spec/blob/main/docs/CAP_WorldFirst_Final_Consolidated_Report.md  
  This report predates VSO's naming rule reserving the "world's first" designation for VCP. Its conclusion is retained as a research record and is not a current VSO claim about CAP.
  The released CAP v1.0 specification also describes Safe Refusal Provenance as "the world's first standardized mechanism" for proving refusals. That wording predates the same rule and is not a current VSO claim; the released text is unchanged.

---

## Reference Implementations

First-party proof-of-concept code (not certified; not a conformance claim):

- **[cap-srp](https://github.com/veritaschain/cap-srp)** — PoC library and dashboard using the CAP v1.0 SRP event set (GEN_ATTEMPT, GEN, GEN_DENY, GEN_ERROR) in a local format.
- **[cap-safe-refusal-provenance](https://github.com/veritaschain/cap-safe-refusal-provenance)** — legacy PoC of the v0.2 SRP extension (WARN / ESCALATE / QUARANTINE as outcome events; no GEN_ERROR). It records refusal decisions; it does not show that content was never generated.

---

## What is CAP?

**CAP (Content / Creative AI Profile)** is a domain-specific profile of the [VAP (Verifiable AI Provenance Framework)](https://github.com/veritaschain/vap-spec) metaframework, establishing cryptographically verifiable audit trails for AI workflows in content and creative industries.

CAP is **NOT** a regulation that prohibits or censors AI usage.  
CAP **IS** a profile for preserving verifiable evidence that third parties can audit when disputes arise.

> *"Verify, Don't Trust"*

---

## The Problem: Refusals Leave No Verifiable Record

Content-generation systems commonly keep records of what they generated. Requests they received and refused typically leave no record that a third party can check. When a provider states that its safeguards worked, an auditor, regulator, or court has no independent way to test that statement against a complete, tamper-evident record of what was requested and how each request was handled.

CAP-SRP addresses the record-keeping side of that gap: it makes refusal decisions auditable and attributable after the fact. It does not evaluate whether a safeguard was adequate, and it does not itself block any generation.

---

## Conformance Levels

CAP v1.0 defines three conformance levels (see the VAP v1.2 divergence note above regarding Bronze):

| Level | Target | Key Requirements | Regulatory Relevance |
|-------|--------|------------------|---------------------|
| **Bronze** | SMEs, Early Adopters | Hash chain, basic logging, 6-month retention | Voluntary transparency |
| **Silver** | Enterprise, VLOPs | + SRP, external anchoring (daily), 2-year retention | EU AI Act Article 12 |
| **Gold** | Regulated Industries | + Real-time verification, HSM, SCITT, 5-year retention | DSA Article 37 audits |

---

## CAP Event Model

CAP defines core events covering the AI content lifecycle:

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ INGEST  │───▶│  TRAIN  │───▶│   GEN   │───▶│ EXPORT  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
     │              │              │              │
     ▼              ▼              ▼              ▼
 Asset Input    Model         Generation      Output
 (Material      Training      (Create new     Delivery
  intake)                      content)
```

---

## SRP Extension: Safe Refusal Provenance

**SRP (Safe Refusal Provenance)** extends CAP so that the recorded handling of a request — **received, evaluated, and refused** — is tamper-evident and verifiable by a third party.

### The Core Innovation

```
Request Received
      │
      ▼
┌─────────────────┐
│  GEN_ATTEMPT    │ ← recorded for every request (MUST at Silver/Gold; SHOULD at Bronze)
└────────┬────────┘
         │
         ▼
   Risk Assessment
         │
    ┌────┴────┬───────────┐
    │         │           │
    ▼         ▼           ▼
┌───────┐ ┌─────────┐ ┌─────────┐
│  GEN  │ │GEN_DENY │ │GEN_ERROR│
│(allow)│ │(refuse) │ │(failure)│
└───────┘ └─────────┘ └─────────┘
```

### The Completeness Invariant (SRP attempt–outcome invariant)

> **∑ GEN_ATTEMPT = ∑ GEN + ∑ GEN_DENY + ∑ GEN_ERROR**

This is a CAP profile-level invariant (CAP v1.0 §13). It is distinct from the VAP v1.2 Completeness Invariant (INT-008), which binds the event count, first and last event identifiers and policy identifier in each AnchorRecord.

Checked against anchored records, this invariant makes the following detectable:
- Hiding successful generations of recorded requests
- Selectively logging only favorable outcomes
- Claiming refusals without corresponding attempts

**Scope.** The invariant covers requests that were recorded as GEN_ATTEMPT and anchored. A request that was never recorded leaves nothing to detect (pre-measurement drop). SRP makes refusal records auditable after the fact; it does not itself block or filter any generation.

---

## Specification

| Document | Description | Status |
|----------|-------------|--------|
| [CAP-Specification-v1.0](docs/CAP-Specification-v1.0.md) | Normative specification | **Released** (tag `v1.0`) |
| [CAP-Specification-v0.2](docs/CAP-Specification-v0.2.md) | Previous version | Superseded |
| [Threat Model](docs/Threat-Model.md) | Security threat analysis | Current |
| [CAP vs VCP](docs/CAP-vs-VCP.md) | Relationship to VCP | Current |
| [Glossary](docs/CAP-Glossary.md) | Terminology reference | Current |

---

## JSON Schema

<a id="schemas"></a>**Status of these files.** The schemas below carry the CAP **v0.2** event model and `$id`s (`…/schemas/cap/v0.2/…`). They are not the normative CAP v1.0 schemas, which are given in CAP v1.0 Appendix A (`…/schemas/cap/v1.0/…`). In particular, CAP v1.0 defines GEN_ERROR (no schema file here yet) and treats WARN, ESCALATE and QUARANTINE as `ModelDecision` values on GEN_DENY rather than as event types; the v0.2 schemas also differ from Appendix A in several enums and required fields. Use them for v0.2-format data only.

Schemas (v0.2):

### CAP Core Events
- [`core-event.schema.json`](schemas/cap/core-event.schema.json) — Common event fields
- [`ingest.schema.json`](schemas/cap/ingest.schema.json) — Asset ingestion
- [`train.schema.json`](schemas/cap/train.schema.json) — Model training
- [`gen.schema.json`](schemas/cap/gen.schema.json) — Content generation
- [`export.schema.json`](schemas/cap/export.schema.json) — Asset delivery

### SRP Extension
- [`gen-attempt.schema.json`](schemas/srp/gen-attempt.schema.json) — Request received
- [`gen-deny.schema.json`](schemas/srp/gen-deny.schema.json) — Request refused
- [`gen-warn.schema.json`](schemas/srp/gen-warn.schema.json) — Allowed with warning (v0.2 event type)
- [`gen-escalate.schema.json`](schemas/srp/gen-escalate.schema.json) — Escalated to human (v0.2 event type)
- [`gen-quarantine.schema.json`](schemas/srp/gen-quarantine.schema.json) — Generated but quarantined (v0.2 event type)

---

## Examples

The examples are illustrative. Their `EventHash` and `Signature` values are placeholders and do not verify, several identifiers are not valid UUIDv7, and some numeric values are not string-encoded as VAP v1.2 §7.2 requires. The Evidence Pack sample uses the v0.2 manifest format (`capVersion`). Use the [test vectors](test-vectors/) for hash and signature checks.

### CAP Core
- [INGEST event](examples/cap-core/ingest.json) — Recording asset intake
- [GEN event](examples/cap-core/gen.json) — Recording content generation
- [EXPORT event](examples/cap-core/export.json) — Recording asset delivery

### SRP Extension
- [GEN_ATTEMPT event](examples/cap-srp/gen_attempt.json) — Request received
- [GEN_DENY event](examples/cap-srp/gen_deny.json) — Request refused
- [Evidence Pack](examples/cap-srp/evidence-pack-sample/) — Complete audit package

---

## Regulatory Alignment

CAP produces evidence relevant to the provisions below. This is not a compliance mapping: conformance to CAP or any VAP profile does not constitute compliance with any law or regulation (VAP v1.2 §1.6), and each regime applies only within its own jurisdiction.

| Regulation | Jurisdiction | CAP Alignment |
|------------|--------------|---------------|
| [EU AI Act](docs/Regulatory-Mapping/EU-AI-Act.md) | EU | Article 50 transparency for generated content; Article 12 logging where a system is high-risk |
| [Digital Services Act](docs/Regulatory-Mapping/DSA.md) | EU | Article 35 systemic risk mitigation, Article 37 audits |
| [GDPR](docs/Regulatory-Mapping/GDPR.md) | EU | Processing records, consent management, crypto-shredding |
| [Colorado AI Act](docs/Regulatory-Mapping/US-AI-Laws.md) | USA | SB24-205 was repealed and replaced by SB26-189 (signed 2026-05-14, applies from 2027-01-01): impact assessments dropped, 3-year record retention kept; the mapping has not been redone for SB26-189 |
| [TAKE IT DOWN Act](docs/Regulatory-Mapping/US-NCII.md) | USA | Records of NCII-related generation refusals (the Act's 48-hour removal duty for platforms is not covered by CAP v1.0) |
| [Copyright Act Art. 30-4](docs/Regulatory-Mapping/JP-Copyright-30-4.md) | Japan | AI training exception documentation |
| South Korea AI Framework Act | Korea | High-impact AI logging (effective Jan 2026) |

> **Legal scope (VAP v1.2 §1.6, adopted verbatim).** VAP and its domain profiles define mechanisms for producing **cryptographically verifiable evidence** of AI system decisions. Conformance to VAP or any profile: (a) does **not** constitute compliance with the EU AI Act, GDPR, MiFID II/III, CAT Rule 613, NIS2, FDA SaMD guidance, or any other law or regulation; (b) does **not** constitute a legal determination that any technical mechanism (including crypto-shredding) satisfies a specific legal obligation; (c) does **not** warrant the correctness, fairness, or safety of the underlying AI decisions — only the integrity, completeness (at anchor granularity), and attributability of their records. VAP generates evidence; competent authorities and courts evaluate it.

---

## Academic Foundation

The theoretical foundations of CAP-SRP are detailed in a preprint (not peer-reviewed; first-party — the author is the VSO founder):

- **Title**: "Proving Non-Generation: Cryptographic Completeness Guarantees for AI Content Moderation Logs — A Case Study and Protocol Design Inspired by the Grok Incident"
- **DOI**: [10.5281/zenodo.18213616](https://doi.org/10.5281/zenodo.18213616)
- **Published**: January 11, 2026

---

## Related Projects

| Project | Description |
|---------|-------------|
| [VCP Specification](https://github.com/veritaschain/vcp-spec) | VeritasChain Protocol for financial/trading systems |
| [VAP Framework](https://github.com/veritaschain/vap-spec) | Parent metaframework (v1.2, Draft 3) for domain-specific profiles |
| [CPP Specification](https://github.com/veritaschain/cpp-spec) | Capture Provenance Profile |
| [VCP Explorer](https://github.com/veritaschain/vcp-explorer-gui) | Visualization and verification tools |

---

## Repository Structure

```
cap-spec/
├── README.md                    # This file
├── LICENSE                      # CC BY 4.0
├── SECURITY.md                  # Security policy
├── GOVERNANCE.md                # VSO governance
├── VERSIONING.md                # Semantic versioning policy
├── docs/
│   ├── CAP-Specification-v1.0.md    # Normative specification (v1.0)
│   ├── CAP-Specification-v0.2.md    # Previous version (superseded)
│   ├── CHANGELOG.md                  # Version history
│   ├── CAP-vs-VCP.md                 # Relationship to VCP
│   ├── CAP-Glossary.md               # Terminology
│   ├── CAP_WorldFirst_Final_Consolidated_Report.md  # World-first claims verification (historical research record)
│   ├── Threat-Model.md               # Security analysis
│   └── Regulatory-Mapping/           # Regulatory relevance mappings (not compliance determinations)
│       ├── EU-AI-Act.md
│       ├── DSA.md
│       ├── GDPR.md
│       ├── JP-Copyright-30-4.md
│       ├── US-AI-Laws.md
│       └── US-NCII.md
├── schemas/
│   ├── cap/                     # Core event schemas
│   └── srp/                     # SRP extension schemas
├── examples/
│   ├── cap-core/               # Core event examples
│   └── cap-srp/                # SRP event examples
└── test-vectors/               # Conformance test data
    ├── canonicalization/       # RFC 8785 JCS tests
    ├── hash/                   # EventHash tests
    ├── signature/              # Ed25519 tests
    └── completeness/           # SRP invariant tests
```

---

## Contributing

We welcome contributions. Please see:
- [GOVERNANCE.md](GOVERNANCE.md) — How decisions are made
- [SECURITY.md](SECURITY.md) — Reporting security issues

To propose changes:
1. Open an issue describing the proposed change
2. Reference relevant specification sections
3. Include test vectors if applicable

---

## License

This specification is published under [CC BY 4.0 International License](LICENSE).

---

## Contact

- **Website:** https://veritaschain.org
- **Email:** standards@veritaschain.org
- **GitHub:** https://github.com/veritaschain
- **Media:** media@veritaschain.org

---

**© 2025-2026 VeritasChain Standards Organization (VSO).** Licensed under [CC BY 4.0](LICENSE).

*VSO is a vendor-neutral standards body. References to specific products or organizations are for interoperability documentation purposes only and do not constitute endorsement.*
