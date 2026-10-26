# CAP vs VCP: Relationship and Alignment

## Overview

**CAP (Content / Creative AI Profile)** and **VCP (VeritasChain Protocol)** are both
domain profiles of the **VAP (Verifiable AI Provenance Framework)** metaframework. Within
the VAP family the designation "Protocol" is reserved for VCP, which defines a wire
protocol; CAP is a profile. This document describes their relationship, shared
mechanisms and differences.

> **Revision — 25 October 2026.** This page previously gave CAP's status as v0.2
> and VCP's as v1.1, expanded VCP-RTA as "Real-Time Attestation", listed VCP fields and
> events that VCP does not define, and described a planned "CAP v0.3". It has been
> corrected; see the [Git history](https://github.com/veritaschain/cap-spec/commits/main/docs/CAP-vs-VCP.md) for the earlier text.

Current statuses follow the VAP v1.2 profile registry (§4.5.2), which prevails over this
page. Neither CAP v1.0 nor VCP v1.2 has established conformance to VAP v1.2 (VAP v1.2
§10.4).

---

## Hierarchical Relationship

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│     VAP (Verifiable AI Provenance Framework)                    │
│     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                    │
│     Cross-domain metaframework: common minimum requirements     │
│     (v1.2, Draft 3)                                             │
│                                                                 │
│                          │                                      │
│                          ▼                                      │
│                                                                 │
│     ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐            │
│     │   VCP   │ │   CAP   │ │   CPP   │ │   OAP   │  ...       │
│     │ Finance │ │Content /│ │ Capture │ │Observed │            │
│     │Protocol │ │Creative │ │ Profile │ │Artifact │            │
│     └─────────┘ └─────────┘ └─────────┘ └─────────┘            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Comparison Matrix

| Aspect | VCP (Finance) | CAP (Content) |
|--------|---------------|---------------|
| **Full Name** | VeritasChain Protocol | Content / Creative AI Profile |
| **Domain** | Algorithmic and AI-driven trading | Content creation, creative industries |
| **Subject** | Signals, orders, executions, risk controls | Content assets, AI-generated media |
| **Core Events** | SIG, ORD, ACK, EXE, CLS (also PRT, CXL, REJ, MOD) | INGEST, TRAIN, GEN, EXPORT |
| **Refusal records** | — | SRP: GEN_ATTEMPT; outcomes GEN, GEN_DENY, GEN_ERROR |
| **Conformance levels** | Silver / Gold / Platinum (anchoring every 24 h / 1 h / 10 min) | Bronze / Silver / Gold (anchoring optional / daily / hourly) |
| **Regulatory relevance** | MiFID II (Art. 17, RTS 25), EU AI Act Art. 12, CAT | EU AI Act Art. 50, DSA, copyright |
| **Specification Status** | v1.2 Released (tag `v1.2.0`) | v1.0 Released (tag `v1.0`) |

Regulatory relevance is not compliance (VAP v1.2 §1.6).

---

## Shared Mechanisms (VAP Common Layer)

### Cryptographic Primitives

| Component | Algorithm | Standard |
|-----------|-----------|----------|
| Event Hash | SHA-256 | FIPS 180-4 |
| Digital Signature | Ed25519 | RFC 8032 |
| Canonicalization | JCS | RFC 8785 |
| UUID Generation | UUID v7 | RFC 9562 |

### Integrity Mechanisms

| Mechanism | VCP v1.2 | CAP v1.0 |
|-----------|----------|----------|
| PrevHash chain | OPTIONAL at every tier (RECOMMENDED for Gold/Platinum, VCP v1.2 §9.1.3 HCH-002) | Required |
| Merkle tree | Required | Required at Silver and Gold |
| External anchoring | Required at every tier | Optional at Bronze; required at Silver and Gold |
| Crypto agility (`HashAlgo`, `SignAlgo`) | Yes | Yes |

VAP v1.2 requires external anchoring at every conformance level (INT-006), so CAP Bronze
without anchoring does not meet the VAP v1.2 requirement set. Both profiles have
known divergences from VAP v1.2 in their Merkle and AnchorRecord details; see the
[CAP draft mapping](conformance/CAP-v1.0-VAP-v1.2-Draft3-Conformance-Mapping.md) and the
[VCP known issues](https://github.com/veritaschain/vcp-spec#-known-issues-in-v12-informative).

---

## Domain-Specific Differences

### VCP: Trading Focus

```
Signal → Order → Acknowledged → Executed → Position Closed
  │        │          │             │             │
  ▼        ▼          ▼             ▼             ▼
 SIG      ORD        ACK           EXE           CLS
```

Key modules: VCP-CORE, VCP-TRADE, VCP-GOV (`AlgoID`, decision factors), VCP-RISK,
VCP-PRIVACY, VCP-RECOVERY, VCP-XREF.

### CAP: Content Focus

```
Input → Training → Generation → Export
  │         │          │          │
  ▼         ▼          ▼          ▼
INGEST   TRAIN       GEN      EXPORT
```

Key concepts: `AssetID`, `RightsBasis`, `ConsentBasis` (CAP v1.0 §7.2–§7.3). `ConfidentialityLevel`
is a CAP v0.2 field (v0.2 repository schemas) and is not defined in CAP v1.0.

### CAP-SRP (Safe Refusal Provenance)

Purpose: make refusal decisions auditable and attributable after the fact. SRP records
decisions; it does not block generation.

| Feature | Description |
|---------|-------------|
| GEN_ATTEMPT | Records each request before evaluation |
| GEN_DENY | Records each refusal |
| SRP attempt–outcome invariant | Each recorded attempt has exactly one recorded outcome (GEN, GEN_DENY or GEN_ERROR); requests never recorded leave nothing to detect. Distinct from VAP INT-008 |
| Evidence Pack | Shareable audit package |

### VCP-RTA

"VCP-RTA" names the reference trading-agent repositories
([vcp-rta-reference](https://github.com/veritaschain/vcp-rta-reference) and related);
it is not a protocol extension. Those repositories are first-party reference code.

---

## Using Both Profiles

| Scenario | VCP | CAP |
|----------|-----|-----|
| AI-generated trading reports | ✓ Trading | ✓ Content |
| Automated market commentary | ✓ Signal data | ✓ Text generation |

Events from different profiles can be related through cross-references in context fields
or, where both parties log corresponding events, through VAP XREF (TRC-005) (VCP-XREF only;
CAP v1.0 defines none). Neither
profile defines a cross-profile chain format.

Organizations implementing both can share cryptographic libraries, serialization code,
verification tools and anchoring infrastructure.

---

## References

- [VCP Specification v1.2](https://github.com/veritaschain/vcp-spec/tree/v1.2.0/spec/v1.2)
- [CAP Specification v1.0](CAP-Specification-v1.0.md)
- [VAP Framework Specification v1.2 (Draft 3)](https://github.com/veritaschain/vap-spec/blob/main/spec/v1.2/VAP_Framework_Specification.md)

---

*Last updated: 2026-10-26*
