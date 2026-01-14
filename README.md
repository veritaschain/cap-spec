# Content / Creative AI Profile (CAP)

> **Cryptographic Audit Trails for AI Content Systems**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Specification](https://img.shields.io/badge/spec-v1.0.0-blue.svg)](docs/CAP-Specification-v1.0.md)
[![VAP](https://img.shields.io/badge/VAP-v1.2-orange.svg)](https://github.com/veritaschain/vap-framework)
[![GitHub](https://img.shields.io/badge/GitHub-veritaschain-181717.svg?logo=github)](https://github.com/veritaschain)

---

## 🎉 CAP v1.0.0 Official Release

**January 13, 2026** — CAP v1.0.0 is now officially released, featuring:

- **Unified Conformance Levels** (Bronze/Silver/Gold) aligned with VAP v1.2
- **External Anchoring Specification** for independent timestamp verification
- **C2PA/SCITT Integration** for ecosystem interoperability
- **Comprehensive Regulatory Mapping** (EU AI Act, DSA, Colorado AI Act, TAKE IT DOWN Act)

📄 [Full Specification](docs/CAP-Specification-v1.0.md) | 📋 [Changelog](docs/CHANGELOG.md) | 📚 [Academic Paper](https://doi.org/10.5281/zenodo.18213616)

---

## World-First Verification Report

CAP-SRP represents the **world's first** open specification for cryptographic AI content refusal logging:

- **CAP World-First Claims – Final Consolidated Research Report**  
  https://github.com/veritaschain/cap-spec/blob/main/docs/CAP_WorldFirst_Final_Consolidated_Report.md

---

## Reference Implementations

- **CAP Safe Refusal Provenance (SRP) – Reference Implementation**  
  A reference implementation and evidence repository demonstrating Safe Refusal Provenance (SRP), including non-generation proofs and cryptographic audit artifacts based on this specification.  
  👉 https://github.com/veritaschain/cap-safe-refusal-provenance

---

## What is CAP?

**CAP (Content / Creative AI Profile)** is a domain-specific profile within the [VAP (Verifiable AI Provenance Framework)](https://github.com/veritaschain/vap-framework) v1.2, establishing cryptographically verifiable audit trails for AI workflows in content and creative industries.

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

CAP v1.0 defines three conformance levels aligned with VAP v1.2:

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

**SRP (Safe Refusal Provenance)** extends CAP to provide cryptographic proof that harmful content was **received, evaluated, and refused**.

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

This mathematical constraint prevents:
- Hiding successful generations of harmful content
- Selectively logging only favorable outcomes
- Claiming refusals without corresponding attempts

---

## Specification

| Document | Description | Status |
|----------|-------------|--------|
| [CAP-Specification-v1.0](docs/CAP-Specification-v1.0.md) | Normative specification | **Official Release** |
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

CAP provides technical capabilities aligned with regulatory requirements:

| Regulation | Jurisdiction | CAP Alignment |
|------------|--------------|---------------|
| [EU AI Act](docs/Regulatory-Mapping/EU-AI-Act.md) | EU | Article 12 logging, Article 53 transparency |
| [Digital Services Act](docs/Regulatory-Mapping/DSA.md) | EU | Article 35 systemic risk mitigation, Article 37 audits |
| [GDPR](docs/Regulatory-Mapping/GDPR.md) | EU | Processing records, consent management, crypto-shredding |
| [Colorado AI Act](docs/Regulatory-Mapping/US-NCII.md) | USA | Impact assessments, 3-year retention |
| [TAKE IT DOWN Act](docs/Regulatory-Mapping/US-NCII.md) | USA | NCII evidence requirements |
| [Copyright Act Art. 30-4](docs/Regulatory-Mapping/JP-Copyright-30-4.md) | Japan | AI training exception documentation |
| South Korea AI Framework Act | Korea | High-impact AI logging (effective Jan 2026) |

---

## Academic Foundation

The theoretical foundations of CAP-SRP are detailed in our peer-reviewed preprint:

- **Title**: "Proving Non-Generation: Cryptographic Completeness Guarantees for AI Content Moderation Logs"
- **DOI**: [10.5281/zenodo.18213616](https://doi.org/10.5281/zenodo.18213616)
- **Published**: January 11, 2026

---

## Related Projects

| Project | Description |
|---------|-------------|
| [VCP Specification](https://github.com/veritaschain/vcp-spec) | VeritasChain Protocol for financial/trading systems |
| [VAP Framework](https://github.com/veritaschain/vap-framework) | Parent framework (v1.2) for domain-specific profiles |
| [VCP Explorer](https://github.com/veritaschain/vcp-explorer) | Visualization and verification tools |

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
│   ├── CAP_WorldFirst_Final_Consolidated_Report.md  # World-first verification
│   ├── Threat-Model.md               # Security analysis
│   └── Regulatory-Mapping/           # Compliance guides
│       ├── EU-AI-Act.md
│       ├── DSA.md
│       ├── GDPR.md
│       ├── JP-Copyright-30-4.md
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
