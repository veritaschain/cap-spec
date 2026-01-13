# Content / Creative AI Profile (CAP)

> **Cryptographic Audit Trails for AI Content Systems**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Specification](https://img.shields.io/badge/spec-v0.2.0-blue.svg)](docs/CAP-Specification-v0.2.md)
[![GitHub](https://img.shields.io/badge/GitHub-veritaschain-181717.svg?logo=github)](https://github.com/veritaschain)

---

## What is CAP?

**CAP (Content / Creative AI Profile)** is a domain-specific profile within the [VAP (Verifiable AI Provenance Framework)](https://github.com/veritaschain/vap-framework), establishing cryptographically verifiable audit trails for AI workflows in content and creative industries.

CAP is **NOT** a regulation that prohibits or censors AI usage.  
CAP **IS** a framework for preserving verifiable evidence that third parties can audit when disputes arise.

> *"Leave Evidence, Not Barriers"*

---

## The Problem: AI's Accountability Vacuum

In December 2025, the Grok image generation incident exposed a critical gap in AI content moderation:

| What Happened | The Problem |
|---------------|-------------|
| 6,700+ harmful images generated per hour | Systems lacked provable refusal mechanisms |
| 6 regulatory jurisdictions launched investigations | No cryptographic proof of safeguard effectiveness |
| xAI claimed "we have filters" | Could not prove which requests were actually refused |

**Current AI systems can prove what they generated. They cannot prove what they refused to generate.**

This asymmetry creates:
- **Regulatory liability**: No evidence that safety measures actually worked
- **Litigation exposure**: No proof of specific refusal decisions
- **Trust deficit**: "Trust us" is no longer acceptable

---

## What CAP Provides

CAP provides **evidentiary infrastructure**, not content judgment:

| CAP Does | CAP Does NOT |
|----------|--------------|
| ✓ Record AI workflow events | ✗ Prohibit or censor AI |
| ✓ Create tamper-evident audit trails | ✗ Determine copyright infringement |
| ✓ Enable third-party verification | ✗ Evaluate content quality |
| ✓ Prove what was (and wasn't) generated | ✗ Make real-time intervention decisions |

---

## CAP Event Model

CAP defines four core events covering the AI content lifecycle:

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
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌─────────┐
│  GEN  │ │GEN_DENY │
│(allow)│ │(refuse) │
└───────┘ └─────────┘
```

### The Completeness Invariant

> **Every `GEN_ATTEMPT` MUST have exactly one corresponding `GEN` or `GEN_DENY` event.**

This mathematical constraint prevents:
- Hiding successful generations of harmful content
- Selectively logging only favorable outcomes
- Claiming refusals without corresponding attempts

---

## Specification

| Document | Description | Status |
|----------|-------------|--------|
| [CAP-Specification-v0.2](docs/CAP-Specification-v0.2.md) | Normative specification | Current |
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
| [Digital Services Act](docs/Regulatory-Mapping/DSA.md) | EU | Article 35 systemic risk mitigation |
| [GDPR](docs/Regulatory-Mapping/GDPR.md) | EU | Processing records, consent management |
| [Copyright Act Art. 30-4](docs/Regulatory-Mapping/JP-Copyright-30-4.md) | Japan | AI training exception documentation |
| [TAKE IT DOWN Act](docs/Regulatory-Mapping/US-NCII.md) | USA | NCII evidence requirements |

---

## Reference Implementation

For working implementations and PoC tools, see:

- **[cap-safe-refusal-provenance](https://github.com/veritaschain/cap-safe-refusal-provenance)** — SRP proof-of-concept with verification tools, Evidence Pack generator, and demonstration scenarios

---

## Related Projects

| Project | Description |
|---------|-------------|
| [VCP Specification](https://github.com/veritaschain/vcp-spec) | VeritasChain Protocol for financial/trading systems |
| [VAP Framework](https://veritaschain.org) | Parent framework for domain-specific profiles |
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
│   ├── CAP-Specification-v0.2.md    # Normative specification
│   ├── CHANGELOG.md                  # Version history
│   ├── CAP-vs-VCP.md                 # Relationship to VCP
│   ├── CAP-Glossary.md               # Terminology
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

---

**© 2025-2026 VeritasChain Standards Organization (VSO). All rights reserved.**

*VSO is a vendor-neutral standards body. References to specific products or organizations are for interoperability documentation purposes only and do not constitute endorsement.*
