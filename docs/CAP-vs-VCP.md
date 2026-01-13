# CAP vs VCP: Relationship and Alignment

## Overview

**CAP (Content/Creative AI Profile)** and **VCP (VeritasChain Protocol)** are both domain-specific profiles within the **VAP (Verifiable AI Provenance Framework)**. This document clarifies their relationship, shared infrastructure, and domain-specific differences.

---

## Hierarchical Relationship

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│     VAP (Verifiable AI Provenance Framework)                    │
│     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                    │
│     Conceptual framework for AI decision audit trails           │
│     Defines cross-domain minimum requirements                   │
│                                                                 │
│                          │                                      │
│                          ▼                                      │
│                                                                 │
│     ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│     │   VCP   │ │   CAP   │ │   DVP   │ │   MAP   │  ...      │
│     │Finance  │ │Content/ │ │Automotive│ │Medical │           │
│     │Profile  │ │Creative │ │ Profile │ │Profile │           │
│     └─────────┘ └─────────┘ └─────────┘ └─────────┘           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Comparison Matrix

| Aspect | VCP (Finance) | CAP (Content) |
|--------|---------------|---------------|
| **Full Name** | VeritasChain Protocol | Content/Creative AI Profile |
| **Domain** | Algorithmic trading, financial services | Content creation, creative industries |
| **Subject** | Transactions, orders, executions | Content assets, AI-generated media |
| **Target Users** | Prop firms, brokers, exchanges | Game studios, film production, publishers |
| **Core Events** | SIG, ORD, EXE, CXL, POS | INGEST, TRAIN, GEN, EXPORT |
| **Key Extension** | RTA (Real-Time Attestation) | SRP (Safe Refusal Provenance) |
| **Regulatory Focus** | MiFID II, SEC Rule 17a-4, EU AI Act | EU AI Act, DSA, Copyright Law |
| **Time Precision** | Nanosecond–Millisecond | Second–Minute |
| **Specification Status** | v1.1 (stable) | v0.2 (pre-release) |

---

## Shared Infrastructure (VAP Common Layer)

Both CAP and VCP inherit the following from VAP:

### Cryptographic Primitives

| Component | Algorithm | Standard |
|-----------|-----------|----------|
| Event Hash | SHA-256 | FIPS 180-4 |
| Digital Signature | Ed25519 | RFC 8032 |
| Canonicalization | JCS | RFC 8785 |
| UUID Generation | UUID v7 | RFC 9562 |

### Integrity Mechanisms

| Mechanism | Purpose |
|-----------|---------|
| Hash Chain | Event linking and tamper detection |
| Merkle Tree | Efficient bulk verification |
| External Anchoring | Independent timestamp proof |
| Crypto Agility | Algorithm migration support |

### Common Event Fields

Both profiles include these core fields:

| Field | Description |
|-------|-------------|
| `EventID` | UUID v7 unique identifier |
| `ChainID` | Evidence chain identifier |
| `PrevHash` | Link to previous event |
| `Timestamp` | ISO 8601 with precision |
| `EventType` | Domain-specific event code |
| `HashAlgo` | Hash algorithm identifier |
| `SignAlgo` | Signature algorithm identifier |
| `EventHash` | Computed hash |
| `Signature` | Digital signature |

---

## Domain-Specific Differences

### VCP: Trading Focus

```
Signal → Order → Execution → Cancellation
  │        │         │            │
  ▼        ▼         ▼            ▼
 SIG      ORD       EXE          CXL
```

**Key Concepts:**
- `StrategyID`: Links events to trading algorithm
- `SymbolChain`: Integrity per trading symbol
- `MarketContext`: Market conditions at event time
- Nanosecond precision for HFT compliance

### CAP: Content Focus

```
Input → Training → Generation → Export
  │         │          │          │
  ▼         ▼          ▼          ▼
INGEST   TRAIN       GEN      EXPORT
```

**Key Concepts:**
- `AssetID`: Content asset identifier
- `RightsBasis`: Copyright justification
- `ConsentBasis`: Consent state tracking
- `ConfidentialityLevel`: Pre-release protection

---

## SRP vs RTA: Key Extensions

### VCP-RTA (Real-Time Attestation)

Purpose: Prove algorithmic trading integrity in real-time

| Feature | Description |
|---------|-------------|
| External Anchoring | Merkle roots to public timestamping |
| Hardware Timestamping | PTP-synchronized precision |
| Regulatory Alignment | MiFID II RTS 25, SEC 17a-4 |

### CAP-SRP (Safe Refusal Provenance)

Purpose: Prove content moderation decisions

| Feature | Description |
|---------|-------------|
| GEN_ATTEMPT | Record all generation requests |
| GEN_DENY | Record all refusals |
| Completeness Invariant | Attempts = Outcomes |
| Evidence Pack | Shareable audit package |

---

## Cross-Profile Interoperability

### When to Use Both

Some organizations may need both profiles:

| Scenario | VCP | CAP |
|----------|-----|-----|
| AI-generated trading reports | ✓ Trading | ✓ Content |
| Automated market commentary | ✓ Signal data | ✓ Text generation |
| Algorithmic social media trading | ✓ Execution | ✓ Content moderation |

### Event Chain Linking

Events from different profiles can be linked via:
- Shared `ChainID` for related workflows
- Cross-references in `Context` fields
- Merkle tree aggregation at VAP level

---

## Specification Alignment

### VCP v1.1 → CAP v0.3 (Planned)

CAP v0.3 will align with VCP v1.1:

| Feature | VCP v1.1 | CAP v0.3 |
|---------|----------|----------|
| Three-layer architecture | ✓ Implemented | ✓ Planned |
| External Anchor tiering | L1/L2/L3 | L1/L2/L3 |
| Crypto Agility | Enhanced | Enhanced |
| Policy Identification | PolicyID field | PolicyID field |

### Implementation Reuse

Organizations implementing both can share:
- Cryptographic libraries
- Event serialization code
- Verification tools
- Anchoring infrastructure

---

## Choosing the Right Profile

### Use VCP When:
- Subject is financial transactions
- Regulatory requirements include MiFID II, SEC rules
- Nanosecond timing precision needed
- Focus is algorithmic trading integrity

### Use CAP When:
- Subject is content/media assets
- Regulatory requirements include EU AI Act Art. 12, DSA
- Focus is AI content moderation evidence
- Need to prove refusal decisions

### Use Both When:
- AI generates both trading decisions and content
- Organization spans financial and media sectors
- Cross-domain audit trail needed

---

## References

- [VCP Specification v1.1](https://github.com/veritaschain/vcp-spec)
- [CAP Specification v0.2](CAP-Specification-v0.2.md)
- [VAP Framework](https://veritaschain.org)

---

*Last updated: 2026-01-13*
