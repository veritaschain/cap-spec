# Content / Creative AI Profile (CAP)

> **Cryptographic Audit Trails for AI Content Systems**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Specification](https://img.shields.io/badge/spec-v1.0%20Released-blue.svg)](docs/CAP-Specification-v1.0.md)
[![VAP](https://img.shields.io/badge/VAP-profile-orange.svg)](https://github.com/veritaschain/vap-spec)
[![GitHub](https://img.shields.io/badge/GitHub-veritaschain-181717.svg?logo=github)](https://github.com/veritaschain)

---

## 🎉 CAP v1.0 Official Release

**January 13, 2026** — CAP v1.0 is now officially released, featuring:

- **Unified Conformance Levels** (Bronze/Silver/Gold)
- **External Anchoring Specification** for independent timestamp verification
- **C2PA/SCITT Integration** for ecosystem interoperability
- **Comprehensive Regulatory Mapping** (EU AI Act, DSA, Colorado AI Act, TAKE IT DOWN Act)

📄 [Full Specification](docs/CAP-Specification-v1.0.md) | 📋 [Changelog](docs/CHANGELOG.md) | 📚 [Academic Paper](https://doi.org/10.5281/zenodo.18213616)

---

## Implementation Status (mandatory disclosure)

As of September 2026: **zero external implementations** of CAP or any other VAP profile, and **zero Evidence Packs accepted in any proceeding**. VeritasChain Co., Ltd., which provides the operating base of VSO, holds ten paid service contracts with European organizations in regulatory technology, financial trading, and audit and assurance (client names withheld pending individual consent); those contracts are not external implementations and are not independent validation of CAP. The reference implementation below is first-party: VSO and VeritasChain Co., Ltd. share a founder.

**VAP v1.2 status.** CAP v1.0 predates VAP v1.2. Its VAP v1.2 conformance mapping is due and not yet published, so CAP may not yet be described as VAP v1.2 conformant (VAP v1.2 §10.4). Known divergence: VAP v1.2 requires external anchoring at every conformance level (INT-006, §8.1), while CAP v1.0 makes it OPTIONAL at Bronze.

---

## Prior-Art Research Report

- **CAP-SRP prior-art review – Final Consolidated Research Report**  
  https://github.com/veritaschain/cap-spec/blob/main/docs/CAP_WorldFirst_Final_Consolidated_Report.md

---

## Reference Implementations

- **CAP Safe Refusal Provenance (SRP) – Reference Implementation**  
  A reference implementation and evidence repository demonstrating Safe Refusal Provenance (SRP), including non-generation proofs and cryptographic audit artifacts based on this specification.  
  👉 https://github.com/veritaschain/cap-safe-refusal-provenance

---

## What is CAP?

**CAP (Content / Creative AI Profile)** is a domain-specific profile of the [VAP (Verifiable AI Provenance Framework)](https://github.com/veritaschain/vap-spec) metaframework, establishing cryptographically verifiable audit trails for AI workflows in content and creative industries.

CAP is **NOT** a regulation that prohibits or censors AI usage.  
CAP **IS** a framework for preserving verifiable evidence that third parties can audit when disputes arise.

> *"Verify, Don't Trust"*

---

## The Problem: AI's Accountability Vacuum

In January 2026, the Grok incident exposed a critical gap in AI content moderation:

| What Happened | The Problem |
|---------------|-------------|
| NCII generation capability discovered | Systems lacked provable refusal mechanisms |
| 8+ regulatory jurisdictions launched investigations | No cryptographic proof of safeguard effectiveness |
| xAI claimed "our safeguards work" | Could not prove which requests were actually refused |
| UK IWF found AI-generated CSAM | No verifiable evidence of prevention measures |

**Current AI systems can prove what they generated. They cannot prove what they refused to generate.**

---

## Conformance Levels

CAP v1.0 defines three conformance levels (see the VAP v1.2 divergence note above regarding Bronze):

| Level | Target | Key Requirements | Regulatory Alignment |
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
│  GEN_ATTEMPT    │ ← MUST be recorded for every request
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

### The Completeness Invariant

> **∑ GEN_ATTEMPT = ∑ GEN + ∑ GEN_DENY + ∑ GEN_ERROR**

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

Schemas for machine validation:

### CAP Core Events
- [`core-event.schema.json`](schemas/cap/core-event.schema.json) — Common event fields
- [`ingest.schema.json`](schemas/cap/ingest.schema.json) — Asset ingestion
- [`train.schema.json`](schemas/cap/train.schema.json) — Model training
- [`gen.schema.json`](schemas/cap/gen.schema.json) — Content generation
- [`export.schema.json`](schemas/cap/export.schema.json) — Asset delivery

### SRP Extension
- [`gen-attempt.schema.json`](schemas/srp/gen-attempt.schema.json) — Request received
- [`gen-deny.schema.json`](schemas/srp/gen-deny.schema.json) — Request refused
- [`gen-warn.schema.json`](schemas/srp/gen-warn.schema.json) — Allowed with warning
- [`gen-escalate.schema.json`](schemas/srp/gen-escalate.schema.json) — Escalated to human
- [`gen-quarantine.schema.json`](schemas/srp/gen-quarantine.schema.json) — Generated but quarantined

---

## Examples

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
| [EU AI Act](docs/Regulatory-Mapping/EU-AI-Act.md) | EU | Article 12 logging, Article 53 transparency |
| [Digital Services Act](docs/Regulatory-Mapping/DSA.md) | EU | Article 35 systemic risk mitigation, Article 37 audits |
| [GDPR](docs/Regulatory-Mapping/GDPR.md) | EU | Processing records, consent management, crypto-shredding |
| [Colorado AI Act](docs/Regulatory-Mapping/US-AI-Laws.md) | USA | Impact assessments, 3-year retention |
| [TAKE IT DOWN Act](docs/Regulatory-Mapping/US-NCII.md) | USA | NCII evidence requirements |
| [Copyright Act Art. 30-4](docs/Regulatory-Mapping/JP-Copyright-30-4.md) | Japan | AI training exception documentation |
| South Korea AI Framework Act | Korea | High-impact AI logging (effective Jan 2026) |

---

## Academic Foundation

The theoretical foundations of CAP-SRP are detailed in a preprint (not peer-reviewed):

- **Title**: "Proving Non-Generation: Cryptographic Completeness Guarantees for AI Content Moderation Logs"
- **DOI**: [10.5281/zenodo.18213616](https://doi.org/10.5281/zenodo.18213616)
- **Published**: January 11, 2026

---

## Related Projects

| Project | Description |
|---------|-------------|
| [VCP Specification](https://github.com/veritaschain/vcp-spec) | VeritasChain Protocol for financial/trading systems |
| [VAP Framework](https://github.com/veritaschain/vap-spec) | Parent metaframework (v1.2) for domain-specific profiles |
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
│   ├── CAP_WorldFirst_Final_Consolidated_Report.md  # Prior-art research report
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

**© 2025-2026 VeritasChain Standards Organization (VSO). All rights reserved.**

*VSO is a vendor-neutral standards body. References to specific products or organizations are for interoperability documentation purposes only and do not constitute endorsement.*
