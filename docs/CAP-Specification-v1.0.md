# Content / Creative AI Profile (CAP)

## Technical Specification v1.0

**Document ID:** VSO-CAP-SPEC-001  
**Status:** Official Release  
**Version:** 1.0  
**Date:** 2026-01-13  
**Maintainer:** VeritasChain Standards Organization (VSO)  
**License:** CC BY 4.0 International  
**Website:** https://veritaschain.org  
**Contact:** standards@veritaschain.org  
**DOI:** 10.5281/zenodo.18213616 (Academic Paper)

---

## Abstract

**CAP (Content / Creative AI Profile)** is an open technical specification for cryptographic audit trails in AI content generation systems. CAP enables organizations to create tamper-evident records of AI system behavior, including the world's first standardized mechanism for proving that AI systems **refused** to generate harmful content.

This specification addresses a critical gap in AI governance: while AI providers can claim their safeguards function correctly, no mechanism previously existed for independent verification of such claims. CAP, through its Safe Refusal Provenance (SRP) extension, provides the cryptographic infrastructure for verification-based AI accountability.

**Key Capabilities:**
- Cryptographic proof of AI content refusals (GEN_DENY events)
- Completeness Invariant ensuring all attempts have recorded outcomes
- Privacy-preserving verification via hash-based attestation
- External anchoring for independent timestamp verification
- Regulatory alignment with EU AI Act, DSA, Colorado AI Act, and emerging global standards

---

## Table of Contents

**Part I: Core Specification**
1. [Introduction](#1-introduction)
2. [Conformance Levels](#2-conformance-levels)
3. [Position within VAP Framework](#3-position-within-vap-framework)
4. [Target Industries](#4-target-industries)
5. [Threat Model](#5-threat-model)
6. [Event Model](#6-event-model)
7. [Data Model](#7-data-model)
8. [Integrity Layer](#8-integrity-layer)
9. [External Anchoring](#9-external-anchoring)
10. [Retention Requirements](#10-retention-requirements)

**Part II: Safe Refusal Provenance (SRP)**
11. [SRP Introduction](#11-srp-introduction)
12. [SRP Event Model](#12-srp-event-model)
13. [Completeness Invariant](#13-completeness-invariant)
14. [SRP Data Model](#14-srp-data-model)
15. [Evidence Pack Structure](#15-evidence-pack-structure)
16. [Privacy-Preserving Verification](#16-privacy-preserving-verification)
17. [Third-Party Verification Protocol](#17-third-party-verification-protocol)

**Part III: Regulatory Compliance**
18. [EU AI Act Article 12 Mapping](#18-eu-ai-act-article-12-mapping)
19. [Digital Services Act Alignment](#19-digital-services-act-alignment)
20. [US State Law Compliance](#20-us-state-law-compliance)
21. [International Regulatory Landscape](#21-international-regulatory-landscape)

**Part IV: Interoperability**
22. [C2PA Integration](#22-c2pa-integration)
23. [SCITT Transparency Services](#23-scitt-transparency-services)
24. [Enterprise Platform Integration](#24-enterprise-platform-integration)

**Appendices**
- [Appendix A: JSON Schema](#appendix-a-json-schema)
- [Appendix B: Event Examples](#appendix-b-event-examples)
- [Appendix C: Regulatory Mapping Tables](#appendix-c-regulatory-mapping-tables)
- [Appendix D: Implementation Checklist](#appendix-d-implementation-checklist)
- [References](#references)

---

# Part I: Core Specification

---

## 1. Introduction

### 1.1 Purpose

CAP (Content / Creative AI Profile) is an evidentiary framework designed to address the following structural challenges in AI content generation:

| Challenge | Description | CAP Solution |
|-----------|-------------|--------------|
| **Accountability Gap** | No way to prove AI refused harmful content | SRP extension with GEN_DENY events |
| **Selective Logging** | Providers can omit inconvenient records | Completeness Invariant enforcement |
| **Tampering Risk** | Logs can be modified after the fact | Hash chain with external anchoring |
| **Verification Impossibility** | Third parties cannot independently verify | Merkle proofs and transparency services |
| **Regulatory Non-compliance** | No standardized format for AI audit trails | EU AI Act Article 12 alignment |

### 1.2 Design Philosophy

CAP is founded on this core principle:

> **"Verify, Don't Trust"**  
> (検証せよ、信頼するな)

The January 2026 Grok incident demonstrated that trust-based AI governance has reached its limits. When AI providers claim their safeguards function correctly, independent parties must be able to verify such claims cryptographically. CAP provides the infrastructure for this verification.

### 1.3 What CAP Is and Is Not

**CAP IS:**
- A specification for creating tamper-evident AI audit trails
- A mechanism for proving AI system decisions (including refusals)
- A framework enabling independent third-party verification
- An open standard compatible with existing transparency infrastructure

**CAP IS NOT:**
- A content filtering or moderation system
- A real-time intervention mechanism
- A replacement for C2PA (it complements C2PA)
- A mandatory regulation (it enables compliance with regulations)

### 1.4 Conformance Language

Keywords in this specification are interpreted per RFC 2119:

- **MUST** / **REQUIRED** / **SHALL**: Absolute requirement
- **MUST NOT** / **SHALL NOT**: Absolute prohibition
- **SHOULD** / **RECOMMENDED**: Recommended with valid exceptions
- **MAY** / **OPTIONAL**: Truly optional

### 1.5 Terminology

| Term | Definition |
|------|------------|
| **CAP** | Content / Creative AI Profile — This specification |
| **VAP** | Verifiable AI Provenance Framework — Parent framework |
| **VSO** | VeritasChain Standards Organization — Standards body |
| **SRP** | Safe Refusal Provenance — Extension for proving non-generation |
| **Event** | Atomic unit of AI workflow activity |
| **Evidence Pack** | Collection of CAP events forming an audit package |
| **Completeness Invariant** | Mathematical guarantee that all attempts have outcomes |
| **External Anchor** | Timestamp from independent third-party service |

---

## 2. Conformance Levels

CAP defines three conformance levels to accommodate different organizational capabilities and regulatory requirements:

### 2.1 Level Overview

| Level | Target | Key Requirements | Regulatory Alignment |
|-------|--------|------------------|---------------------|
| **Bronze** | SMEs, Early Adopters | Hash chain, basic event logging | Voluntary transparency |
| **Silver** | Enterprise, VLOPs | + External anchoring, SRP | EU AI Act Article 12 |
| **Gold** | Regulated Industries | + Real-time verification, HSM | DSA Article 37 audits |

### 2.2 Bronze Level (基礎レベル)

**Minimum requirements for CAP conformance.**

| Requirement | Description | MUST/SHOULD |
|-------------|-------------|-------------|
| Event Logging | All INGEST, TRAIN, GEN, EXPORT events recorded | MUST |
| Hash Chain | Events linked via SHA-256 hash chain | MUST |
| Digital Signature | Ed25519 signatures on all events | MUST |
| Timestamp | ISO 8601 timestamps with timezone | MUST |
| Retention | Minimum 6 months | MUST |
| Event Schema | Conformance to CAP JSON Schema | MUST |

### 2.3 Silver Level (標準レベル)

**Recommended for organizations subject to EU AI Act or similar regulations.**

Includes all Bronze requirements, plus:

| Requirement | Description | MUST/SHOULD |
|-------------|-------------|-------------|
| SRP Extension | GEN_ATTEMPT and GEN_DENY event types | MUST |
| Completeness Invariant | Verifiable ∑ATTEMPT = ∑OUTCOMES | MUST |
| External Anchoring | Merkle root to RFC 3161 TSA (≥daily) | MUST |
| Evidence Pack | Structured export format | MUST |
| Privacy Hashing | PromptHash for sensitive content | MUST |
| Retention | Minimum 2 years | SHOULD |

### 2.4 Gold Level (最上位レベル)

**Required for Very Large Online Platforms (VLOPs) and high-risk AI systems.**

Includes all Silver requirements, plus:

| Requirement | Description | MUST/SHOULD |
|-------------|-------------|-------------|
| Real-time Anchoring | External anchor within 1 hour | MUST |
| HSM Key Management | Hardware security module for signing keys | MUST |
| Transparency Log | SCITT-compatible transparency service | MUST |
| Audit API | Programmatic access for auditors | MUST |
| Retention | Minimum 5 years | MUST |
| Incident Response | 24-hour evidence preservation capability | MUST |

### 2.5 Conformance Declaration

Organizations claiming CAP conformance MUST:

1. Specify their conformance level (Bronze/Silver/Gold)
2. Publish a conformance statement
3. Make Evidence Packs available upon legitimate request
4. Undergo periodic self-assessment or third-party audit (Gold only)

---

## 3. Position within VAP Framework

### 3.1 VAP/VSO/CAP Hierarchy

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│     VAP (Verifiable AI Provenance Framework)                        │
│     ─────────────────────────────────────────                       │
│     Cross-domain conceptual framework for AI audit trails           │
│                                                                     │
│                          ▲                                          │
│                          │ defines & maintains                      │
│                          │                                          │
│     VSO (VeritasChain Standards Organization)                       │
│     ─────────────────────────────────────────                       │
│     Independent standards body (Tokyo, Japan)                       │
│                                                                     │
│                          │                                          │
│                          │ publishes domain profiles                │
│                          ▼                                          │
│                                                                     │
│     ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐               │
│     │   VCP   │ │   CAP   │ │   DVP   │ │   MAP   │  ...          │
│     │Finance  │ │Content/ │ │Automotive│ │Medical │               │
│     │Profile  │ │Creative │ │ Profile │ │Profile │               │
│     │ v1.1    │ │ v1.0    │ │ (draft) │ │(draft) │               │
│     └─────────┘ └─────────┘ └─────────┘ └─────────┘               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Relationship to VCP

| Aspect | VCP (Finance Profile) | CAP (Content Profile) |
|--------|----------------------|----------------------|
| **Subject** | Algorithmic trading decisions | Content generation decisions |
| **Industries** | Finance, Trading, Prop Firms | Games, Film, Publishing, AI Platforms |
| **Core Events** | SIG/ORD/EXE/CXL | INGEST/TRAIN/GEN/GEN_DENY/EXPORT |
| **Regulations** | MiFID II, EU AI Act | EU AI Act, DSA, Copyright Law |
| **Time Precision** | Nanosecond–Millisecond | Second–Minute |
| **SRP Extension** | Not applicable | Core feature |
| **Shared Foundation** | VAP Integrity Layer | VAP Integrity Layer |

### 3.3 Shared VAP Infrastructure

CAP inherits the following VAP common infrastructure:

- **Hash Chain**: Tamper detection via event chain linkage (SHA-256)
- **Merkle Tree**: Efficient verification of bulk events (RFC 6962)
- **Digital Signature**: Ed25519 issuer authentication (RFC 8032)
- **Crypto Agility**: Future algorithm migration support (ML-DSA planned)
- **UUIDv7**: Time-ordered unique identifiers (RFC 9562)

---

## 4. Target Industries

### 4.1 Priority Classification

| Priority | Industries | Primary Use Cases |
|----------|------------|-------------------|
| **A (Critical)** | Image Generation Platforms, Social Media | NCII prevention, content moderation accountability |
| **A (Critical)** | Enterprise AI (Azure OpenAI, AWS Bedrock) | Regulatory compliance, audit trails |
| **B (High)** | Games, Film/Animation, VFX | IP protection, confidential leak prevention |
| **B (High)** | Publishing, Advertising | Rights management, consent tracking |
| **C (Medium)** | Music, Voice Synthesis | Voice cloning prevention, consent verification |
| **C (Medium)** | Education, Research | Academic integrity, model provenance |

### 4.2 Image Generation Platform Requirements

Given the Grok incident and regulatory response, image generation platforms face specific requirements:

| Requirement | Bronze | Silver | Gold |
|-------------|--------|--------|------|
| GEN_ATTEMPT logging | SHOULD | MUST | MUST |
| GEN_DENY logging | SHOULD | MUST | MUST |
| NCII detection records | SHOULD | MUST | MUST |
| CSAM screening records | N/A | MUST | MUST |
| External anchoring | OPTIONAL | Daily | Hourly |
| Audit API | OPTIONAL | SHOULD | MUST |

### 4.3 Enterprise AI Platform Requirements

For organizations deploying AI through cloud platforms:

| Requirement | Bronze | Silver | Gold |
|-------------|--------|--------|------|
| Prompt/response logging | MUST | MUST | MUST |
| Model version tracking | MUST | MUST | MUST |
| User attribution | SHOULD | MUST | MUST |
| PII redaction capability | OPTIONAL | SHOULD | MUST |
| Integration with SIEM | OPTIONAL | SHOULD | MUST |

---

## 5. Threat Model

### 5.1 Adversary Capabilities

CAP is designed to resist the following threats:

| Threat | Description | Mitigation |
|--------|-------------|------------|
| **Log Modification** | Attacker modifies event content | Hash chain breaks on modification |
| **Log Deletion** | Attacker removes events | Completeness Invariant violation |
| **Log Insertion** | Attacker adds fabricated events | Signature verification fails |
| **Selective Omission** | Provider omits unfavorable events | Completeness Invariant check |
| **Timestamp Manipulation** | Backdate or forward-date events | External anchoring verification |
| **Key Compromise** | Attacker obtains signing key | HSM requirement (Gold), key rotation |

### 5.2 Trust Assumptions

CAP assumes:

1. **Cryptographic Primitives**: SHA-256 and Ed25519 remain secure
2. **External TSA**: RFC 3161 timestamping authorities are honest
3. **Initial Event**: Genesis event is correctly initialized
4. **Key Security**: Signing keys are protected (Bronze: software, Gold: HSM)

### 5.3 Out of Scope

CAP does NOT protect against:

- Compromise of all signing keys simultaneously
- Nation-state adversaries with quantum computing capability (until PQC migration)
- Physical destruction of all storage systems
- Collusion between provider and all external anchoring services

---

## 6. Event Model

### 6.1 Core Event Types

| Event Type | Description | When Generated |
|------------|-------------|----------------|
| **INGEST** | Asset ingested into AI workflow | Asset upload/import |
| **TRAIN** | Asset used for model training | Training job execution |
| **GEN** | Content successfully generated | Generation complete |
| **GEN_ATTEMPT** | Generation request received (SRP) | Request arrival |
| **GEN_DENY** | Generation refused (SRP) | Content policy violation |
| **GEN_ERROR** | Generation failed (SRP) | System error |
| **EXPORT** | Generated content exported | Content download/publish |

### 6.2 Event Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   INGEST ─────► TRAIN ─────► [Model Ready]                      │
│                                                                 │
│   [User Request]                                                │
│        │                                                        │
│        ▼                                                        │
│   GEN_ATTEMPT ─────┬─────► GEN ─────► EXPORT                    │
│                    │                                            │
│                    ├─────► GEN_DENY (policy violation)          │
│                    │                                            │
│                    └─────► GEN_ERROR (system failure)           │
│                                                                 │
│   Completeness Invariant:                                       │
│   ∑ GEN_ATTEMPT = ∑ GEN + ∑ GEN_DENY + ∑ GEN_ERROR             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.3 Event Ordering

Events MUST be ordered by:

1. **UUIDv7 Timestamp Component**: Primary ordering
2. **Hash Chain Linkage**: Cryptographic ordering
3. **External Anchor**: Independent verification

---

## 7. Data Model

### 7.1 Common Event Fields

All CAP events MUST include:

```json
{
  "EventID": "UUIDv7 (RFC 9562)",
  "ChainID": "UUIDv7 identifying the event chain",
  "PrevHash": "sha256:... (null for genesis)",
  "Timestamp": "ISO 8601 with timezone",
  "EventType": "INGEST|TRAIN|GEN|GEN_ATTEMPT|GEN_DENY|GEN_ERROR|EXPORT",
  "HashAlgo": "SHA256",
  "SignAlgo": "ED25519",
  "EventHash": "sha256:...",
  "Signature": "ed25519:..."
}
```

### 7.2 Asset Object

For INGEST and EXPORT events:

```json
{
  "Asset": {
    "AssetID": "urn:cap:asset:{org}:{id}",
    "AssetType": "IMAGE|VIDEO|AUDIO|TEXT|MODEL|OTHER",
    "AssetHash": "sha256:...",
    "AssetName": "Human-readable name",
    "AssetSize": 1234567,
    "MimeType": "image/png"
  }
}
```

### 7.3 Rights Object

```json
{
  "Rights": {
    "RightsBasis": "OWNED|LICENSED|PUBLIC_DOMAIN|FAIR_USE|UNKNOWN",
    "RightsHolder": "Organization or individual ID",
    "ConsentBasis": "EXPLICIT|IMPLIED|NOT_REQUIRED|UNKNOWN",
    "ConsentEvidence": "Reference to consent documentation",
    "PermittedUse": {
      "Training": true,
      "Generation": true,
      "Distribution": false,
      "Commercial": true
    }
  }
}
```

### 7.4 Context Object

```json
{
  "Context": {
    "UserID": "Pseudonymized user identifier",
    "UserHash": "sha256:... (for privacy)",
    "Role": "CREATOR|REVIEWER|ADMIN|SYSTEM",
    "Department": "Optional organizational unit",
    "SessionID": "UUIDv7 for session tracking",
    "ClientIP_Hash": "sha256:... (optional, privacy-preserving)"
  }
}
```

### 7.5 Model Context Object

```json
{
  "ModelContext": {
    "ModelID": "urn:cap:model:{provider}:{name}",
    "ModelVersion": "Semantic version string",
    "ModelType": "IMAGE_GEN|TEXT_GEN|AUDIO_GEN|VIDEO_GEN|MULTIMODAL",
    "ModelProvider": "Provider name",
    "Environment": "LOCAL|CLOUD|HYBRID",
    "PolicyVersion": "Content policy version applied"
  }
}
```

---

## 8. Integrity Layer

### 8.1 Hash Chain Construction

Events are linked in a tamper-evident chain:

```
Event[0] ──► Event[1] ──► Event[2] ──► ... ──► Event[n]
   │            │            │                    │
   ▼            ▼            ▼                    ▼
 hash₀    ◄── hash₁    ◄── hash₂    ◄── ... ◄── hashₙ
(genesis)  (includes    (includes              (includes
            hash₀)       hash₁)                 hashₙ₋₁)
```

### 8.2 Event Hash Computation

```python
def compute_event_hash(event: dict) -> str:
    # Remove signature before hashing
    event_copy = {k: v for k, v in event.items() if k != "Signature"}
    
    # Canonicalize per RFC 8785 (JCS)
    canonical = json_canonicalize(event_copy)
    
    # Compute SHA-256
    hash_bytes = hashlib.sha256(canonical.encode('utf-8')).digest()
    
    return f"sha256:{hash_bytes.hex()}"
```

### 8.3 Digital Signature

All events MUST be signed using Ed25519 (RFC 8032):

```python
def sign_event(event: dict, private_key: Ed25519PrivateKey) -> str:
    # Compute hash first
    event_hash = compute_event_hash(event)
    event["EventHash"] = event_hash
    
    # Sign the hash
    signature = private_key.sign(bytes.fromhex(event_hash[7:]))  # Remove "sha256:"
    
    return f"ed25519:{base64.b64encode(signature).decode()}"
```

### 8.4 Chain Verification

```python
def verify_chain(events: List[dict]) -> bool:
    for i, event in enumerate(events):
        # Verify hash computation
        computed_hash = compute_event_hash(event)
        if event["EventHash"] != computed_hash:
            return False
        
        # Verify chain linkage (skip genesis)
        if i > 0:
            if event["PrevHash"] != events[i-1]["EventHash"]:
                return False
        
        # Verify signature
        if not verify_signature(event):
            return False
    
    return True
```

---

## 9. External Anchoring

### 9.1 Purpose

External anchoring provides independent proof that events existed at a specific time, preventing:

- Backdating of events
- Forward-dating of events
- Undetectable log forking

### 9.2 Merkle Tree Construction

Events are aggregated into Merkle trees for efficient anchoring:

```
                    Merkle Root
                   /           \
              Hash₀₁           Hash₂₃
             /      \         /      \
        H(E₀)    H(E₁)    H(E₂)    H(E₃)
```

### 9.3 Anchoring Frequency Requirements

| Conformance Level | Minimum Frequency | Maximum Delay |
|-------------------|-------------------|---------------|
| Bronze | Optional | N/A |
| Silver | Daily | 24 hours |
| Gold | Hourly | 1 hour |

### 9.4 Supported Anchoring Services

CAP supports anchoring to:

1. **RFC 3161 Timestamping Authorities (TSA)**: Traditional PKI timestamping
2. **SCITT Transparency Services**: IETF-standardized transparency logs
3. **Blockchain Anchoring**: Public blockchains (Bitcoin, Ethereum) for maximum decentralization

### 9.5 Anchor Record Format

```json
{
  "AnchorID": "UUIDv7",
  "AnchorType": "RFC3161|SCITT|BLOCKCHAIN",
  "MerkleRoot": "sha256:...",
  "EventCount": 1000,
  "FirstEventID": "UUIDv7",
  "LastEventID": "UUIDv7",
  "Timestamp": "ISO 8601",
  "AnchorProof": "Base64-encoded proof",
  "ServiceEndpoint": "URL of anchoring service"
}
```

---

## 10. Retention Requirements

### 10.1 Minimum Retention Periods

| Conformance Level | Events | Anchor Records | Evidence Packs |
|-------------------|--------|----------------|----------------|
| Bronze | 6 months | N/A | On request |
| Silver | 2 years | 5 years | 2 years |
| Gold | 5 years | 10 years | 5 years |

### 10.2 Regulatory Alignment

| Regulation | Required Retention | CAP Mapping |
|------------|-------------------|-------------|
| EU AI Act Article 12 | 6 months minimum | Silver: 2 years |
| Colorado AI Act | 3 years | Silver/Gold |
| China AI Regulations | 6 months | Silver: 2 years |
| GDPR (for personal data) | Purpose limitation | Crypto-shredding support |

### 10.3 Crypto-Shredding Support

For GDPR compliance, CAP supports crypto-shredding:

1. Sensitive fields encrypted with per-user keys
2. Key deletion renders data unrecoverable
3. Hash chain integrity preserved (hashes remain, content inaccessible)

---

# Part II: Safe Refusal Provenance (SRP)

---

## 11. SRP Introduction

### 11.1 The Negative Proof Problem

Traditional AI logging can record what was generated, but cannot prove what was **not** generated. This creates an accountability gap:

> When AI providers claim "we blocked millions of harmful requests," no independent party can verify this claim.

SRP solves this by treating **non-generation as a first-class, provable event**.

### 11.2 SRP Design Goals

1. **Prove refusals occurred**: Cryptographic evidence of GEN_DENY events
2. **Ensure completeness**: Every GEN_ATTEMPT has exactly one outcome
3. **Preserve privacy**: Verify refusals without exposing harmful content
4. **Enable independence**: Third parties can verify without trusting the provider

### 11.3 SRP Applicability

SRP is REQUIRED for:
- Silver and Gold conformance levels
- Image generation platforms
- Systems subject to EU AI Act high-risk classification
- VLOPs under DSA Article 37

---

## 12. SRP Event Model

### 12.1 SRP Event Types

| Event Type | Description | Trigger |
|------------|-------------|---------|
| **GEN_ATTEMPT** | Generation request received | Request arrival (before processing) |
| **GEN** | Generation succeeded | Successful completion |
| **GEN_DENY** | Generation refused | Content policy violation detected |
| **GEN_ERROR** | Generation failed | System error (not policy-related) |

### 12.2 Event Flow

```
User Request
     │
     ▼
┌─────────────────┐
│  GEN_ATTEMPT    │ ◄─── MUST be logged FIRST
│  (recorded)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Safety Check   │
└────────┬────────┘
         │
    ┌────┴────┬─────────────┐
    │         │             │
    ▼         ▼             ▼
┌───────┐ ┌────────┐ ┌───────────┐
│  GEN  │ │GEN_DENY│ │ GEN_ERROR │
│(pass) │ │(block) │ │ (failure) │
└───────┘ └────────┘ └───────────┘
```

### 12.3 Timing Requirements

| Event Pair | Maximum Delay |
|------------|---------------|
| Request → GEN_ATTEMPT | 100ms |
| GEN_ATTEMPT → Outcome | 60 seconds |
| Outcome event logging | 1 second |

---

## 13. Completeness Invariant

### 13.1 Mathematical Definition

The **Completeness Invariant** is the foundational guarantee of SRP:

```
∑ GEN_ATTEMPT = ∑ GEN + ∑ GEN_DENY + ∑ GEN_ERROR
```

For any time window [t₁, t₂]:

```
COUNT(GEN_ATTEMPT WHERE t₁ ≤ timestamp ≤ t₂) 
  = COUNT(GEN WHERE t₁ ≤ timestamp ≤ t₂)
  + COUNT(GEN_DENY WHERE t₁ ≤ timestamp ≤ t₂)
  + COUNT(GEN_ERROR WHERE t₁ ≤ timestamp ≤ t₂)
```

### 13.2 Invariant Enforcement

Every GEN_ATTEMPT MUST have exactly one corresponding outcome:

```python
def verify_completeness(events: List[dict]) -> bool:
    attempts = {}
    outcomes = {}
    
    for event in events:
        if event["EventType"] == "GEN_ATTEMPT":
            attempts[event["EventID"]] = event
        elif event["EventType"] in ["GEN", "GEN_DENY", "GEN_ERROR"]:
            attempt_id = event["AttemptID"]
            if attempt_id in outcomes:
                return False  # Duplicate outcome
            outcomes[attempt_id] = event
    
    # Every attempt must have exactly one outcome
    return set(attempts.keys()) == set(outcomes.keys())
```

### 13.3 Invariant Violation Detection

Violations indicate:

| Violation | Meaning | Severity |
|-----------|---------|----------|
| Attempts > Outcomes | Missing outcome events | Critical |
| Outcomes > Attempts | Fabricated outcomes | Critical |
| Duplicate Outcomes | Data integrity failure | Critical |
| Orphaned Outcomes | Missing attempt records | High |

---

## 14. SRP Data Model

### 14.1 GEN_ATTEMPT Event

```json
{
  "EventID": "019467a1-0001-7000-0000-000000000001",
  "ChainID": "019467a0-0000-7000-0000-000000000000",
  "PrevHash": "sha256:...",
  "Timestamp": "2026-01-13T14:23:45.100Z",
  "EventType": "GEN_ATTEMPT",
  "HashAlgo": "SHA256",
  "SignAlgo": "ED25519",
  
  "PromptHash": "sha256:7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069",
  "ReferenceImageHash": "sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "InputType": "text+image",
  "PolicyID": "cap.safety.v1.0",
  "ModelVersion": "img-gen-v4.2.1",
  "SessionID": "019467a1-0001-7000-0000-000000000000",
  "ActorHash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  
  "EventHash": "sha256:a1b2c3d4e5f6...",
  "Signature": "ed25519:MEUCIQDhE3H4..."
}
```

### 14.2 GEN_DENY Event

```json
{
  "EventID": "019467a1-0001-7000-0000-000000000002",
  "ChainID": "019467a0-0000-7000-0000-000000000000",
  "PrevHash": "sha256:a1b2c3d4e5f6...",
  "Timestamp": "2026-01-13T14:23:45.150Z",
  "EventType": "GEN_DENY",
  "HashAlgo": "SHA256",
  "SignAlgo": "ED25519",
  
  "AttemptID": "019467a1-0001-7000-0000-000000000001",
  "RiskCategory": "NCII_RISK",
  "RiskSubCategories": ["REAL_PERSON", "CLOTHING_REMOVAL_REQUEST"],
  "RiskScore": 0.94,
  "RefusalReason": "Non-consensual intimate imagery request detected",
  "PolicyID": "cap.safety.v1.0",
  "PolicyVersion": "2026-01-01",
  "ModelDecision": "DENY",
  "HumanOverride": false,
  "EscalationID": null,
  
  "EventHash": "sha256:e5f6g7h8i9j0...",
  "Signature": "ed25519:MEQCIFRt..."
}
```

### 14.3 Risk Categories

| Category | Description | Example |
|----------|-------------|---------|
| `CSAM_RISK` | Child sexual abuse material | Minor sexualization request |
| `NCII_RISK` | Non-consensual intimate imagery | Deepfake pornography |
| `REAL_PERSON_DEEPFAKE` | Unauthorized realistic depiction | Celebrity face swap |
| `VIOLENCE_EXTREME` | Graphic violence | Gore, torture |
| `HATE_CONTENT` | Discriminatory content | Racist imagery |
| `TERRORIST_CONTENT` | Terrorism-related | Propaganda, recruitment |
| `SELF_HARM_PROMOTION` | Self-harm encouragement | Suicide methods |
| `COPYRIGHT_VIOLATION` | Clear IP infringement | Trademarked characters |
| `OTHER` | Other policy violations | Custom policies |

---

## 15. Evidence Pack Structure

### 15.1 Purpose

An **Evidence Pack** is a self-contained, cryptographically verifiable collection of CAP events suitable for regulatory submission or audit.

### 15.2 Structure

```
evidence_pack/
├── manifest.json           # Pack metadata and integrity info
├── events/
│   ├── events_001.json     # Event batch 1
│   ├── events_002.json     # Event batch 2
│   └── ...
├── anchors/
│   ├── anchor_001.json     # External anchor records
│   └── ...
├── merkle/
│   ├── tree_001.json       # Merkle tree structure
│   └── proofs/             # Selective disclosure proofs
└── signatures/
    └── pack_signature.json # Pack-level signature
```

### 15.3 Manifest Format

```json
{
  "PackID": "019467b2-0000-7000-0000-000000000000",
  "PackVersion": "1.0",
  "GeneratedAt": "2026-01-13T15:00:00Z",
  "GeneratedBy": "urn:cap:org:example-platform",
  "ConformanceLevel": "Silver",
  "EventCount": 150000,
  "TimeRange": {
    "Start": "2026-01-01T00:00:00Z",
    "End": "2026-01-13T14:59:59Z"
  },
  "Checksums": {
    "events_001.json": "sha256:...",
    "events_002.json": "sha256:...",
    "anchor_001.json": "sha256:..."
  },
  "CompletenessVerification": {
    "TotalAttempts": 145000,
    "TotalGEN": 140000,
    "TotalGEN_DENY": 4500,
    "TotalGEN_ERROR": 500,
    "InvariantValid": true
  }
}
```

---

## 16. Privacy-Preserving Verification

### 16.1 Hash-Based Verification

CAP enables verification without exposing harmful content:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Regulator/Auditor                    Platform                  │
│  ─────────────────                    ────────                  │
│                                                                 │
│  1. Receives complaint with           Maintains CAP audit trail │
│     harmful prompt                                              │
│                                                                 │
│  2. Computes:                                                   │
│     hash = SHA256(prompt)                                       │
│                                                                 │
│  3. Queries: "Does GEN_DENY          Searches for matching     │
│     exist with PromptHash=hash?"      PromptHash               │
│                                                                 │
│  4. Receives: Yes/No + Merkle proof   Returns proof            │
│                                                                 │
│  5. Verifies proof independently      Never sees original      │
│                                       complaint                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 16.2 Selective Disclosure

Merkle proofs enable proving specific events without revealing others:

```python
def verify_event_in_pack(event: dict, merkle_proof: List[str], merkle_root: str) -> bool:
    """Verify event exists in Evidence Pack without accessing other events."""
    current_hash = compute_event_hash(event)
    
    for sibling_hash, direction in merkle_proof:
        if direction == "left":
            current_hash = sha256(sibling_hash + current_hash)
        else:
            current_hash = sha256(current_hash + sibling_hash)
    
    return current_hash == merkle_root
```

---

## 17. Third-Party Verification Protocol

### 17.1 Verification Levels

| Level | Verifier Access | Verification Scope |
|-------|-----------------|-------------------|
| **Public** | Merkle roots only | Anchor existence |
| **Auditor** | Evidence Packs | Full chain verification |
| **Regulator** | Real-time API (Gold) | Live monitoring |

### 17.2 Verification Steps

1. **Anchor Verification**: Confirm Merkle root in external TSA
2. **Chain Verification**: Validate hash chain integrity
3. **Signature Verification**: Authenticate all events
4. **Completeness Verification**: Check invariant holds
5. **Selective Query**: Verify specific events via Merkle proofs

### 17.3 Verification Report Format

```json
{
  "VerificationID": "UUIDv7",
  "PackID": "019467b2-0000-7000-0000-000000000000",
  "VerifiedAt": "2026-01-13T16:00:00Z",
  "VerifierID": "urn:cap:verifier:audit-firm-xyz",
  "Results": {
    "AnchorVerification": "PASS",
    "ChainIntegrity": "PASS",
    "SignatureValidity": "PASS",
    "CompletenessInvariant": "PASS",
    "OverallResult": "PASS"
  },
  "VerifierSignature": "ed25519:..."
}
```

---

# Part III: Regulatory Compliance

---

## 18. EU AI Act Article 12 Mapping

### 18.1 Article 12 Requirements

EU AI Act Article 12 requires high-risk AI systems to:

> "technically allow for the automatic recording of events ('logs') over the lifetime of the system"

### 18.2 CAP Compliance Mapping

| Article 12 Requirement | CAP Implementation |
|------------------------|-------------------|
| Automatic recording | Event-driven logging (INGEST/TRAIN/GEN/etc.) |
| Lifetime coverage | Chain continuity from genesis |
| Risk identification | RiskCategory, RiskScore fields |
| Post-market monitoring | Evidence Pack export |
| Human oversight logging | HumanOverride field |
| Traceability | Hash chain, UUIDv7 ordering |

### 18.3 Minimum Retention

Article 12(4) specifies minimum 6-month retention. CAP Silver requires 2 years, exceeding this requirement.

### 18.4 Implementation Timeline

| Deadline | Requirement | CAP Readiness |
|----------|-------------|---------------|
| August 2, 2025 | Prohibited AI practices | N/A |
| August 2, 2026 | High-risk AI obligations | CAP v1.0 ready |
| August 2, 2027 | Full application | CAP Gold recommended |

---

## 19. Digital Services Act Alignment

### 19.1 DSA Article 37 (Independent Audits)

VLOPs must undergo annual independent audits. CAP provides:

| Audit Requirement | CAP Support |
|-------------------|-------------|
| Algorithm transparency | Model version tracking |
| Content moderation records | GEN_DENY events |
| Risk mitigation documentation | RiskCategory, PolicyID |
| Structured evidence | Evidence Pack format |

### 19.2 DSA Article 35 (Risk Assessments)

```json
{
  "DSA_Article35_Mapping": {
    "SystemicRisks": "RiskCategory enumeration",
    "MitigationMeasures": "PolicyID, PolicyVersion",
    "EffectivenessMonitoring": "RiskScore trends",
    "IndependentVerification": "External anchoring"
  }
}
```

---

## 20. US State Law Compliance

### 20.1 Colorado AI Act (SB24-205)

Effective February 1, 2026:

| Requirement | CAP Implementation |
|-------------|-------------------|
| Impact assessments | Evidence Pack with risk analysis |
| 3-year retention | Silver: 2 years, Gold: 5 years |
| Algorithmic discrimination documentation | RiskCategory: HATE_CONTENT |
| Consumer notification records | EXPORT events |

### 20.2 TAKE IT DOWN Act

Platform compliance deadline: May 2026

| Requirement | CAP Implementation |
|-------------|-------------------|
| NCII removal evidence | GEN_DENY with NCII_RISK |
| 48-hour response proof | Timestamp verification |
| Prevention documentation | Completeness Invariant |

---

## 21. International Regulatory Landscape

### 21.1 Multi-Jurisdictional Compliance Matrix

| Jurisdiction | Regulation | Effective | CAP Alignment |
|--------------|------------|-----------|---------------|
| EU | AI Act | Aug 2026 | Silver/Gold |
| EU | DSA | In force | Gold (VLOPs) |
| USA (CO) | SB24-205 | Feb 2026 | Silver |
| USA (Fed) | TAKE IT DOWN | May 2026 | Silver |
| South Korea | AI Framework Act | Jan 2026 | Silver |
| China | AI Labeling | Sep 2025 | Bronze+ |
| UK | Online Safety Act | In force | Gold (Cat 1) |

### 21.2 South Korea AI Framework Act

First comprehensive AI law in Asia-Pacific. CAP addresses:

- Pre-deployment assessment documentation
- High-impact AI logging requirements
- Foreign company representative obligations

### 21.3 China AI Regulations

6-month log retention, explicit labeling. CAP provides:

- Retention: Silver exceeds requirement
- Labeling: Model metadata in events

---

# Part IV: Interoperability

---

## 22. C2PA Integration

### 22.1 Complementary Positioning

| Aspect | C2PA | CAP |
|--------|------|-----|
| Question Answered | "Is this content authentic?" | "What did the AI decide?" |
| Focus | Content provenance | System accountability |
| Scope | Individual assets | System-wide behavior |
| Metaphor | Content passport | System flight recorder |

### 22.2 Integration Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  AI Generation Request                                          │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────┐                                            │
│  │  CAP: GEN_ATTEMPT│ ◄─── System-level logging                 │
│  └────────┬────────┘                                            │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                            │
│  │  Safety Check   │                                            │
│  └────────┬────────┘                                            │
│           │                                                     │
│      ┌────┴────┐                                                │
│      │         │                                                │
│      ▼         ▼                                                │
│  ┌───────┐ ┌────────┐                                           │
│  │CAP:GEN│ │CAP:DENY│                                           │
│  └───┬───┘ └────────┘                                           │
│      │                                                          │
│      ▼                                                          │
│  ┌─────────────────┐                                            │
│  │ C2PA Manifest   │ ◄─── Asset-level provenance                │
│  │ attached to     │                                            │
│  │ generated image │                                            │
│  └─────────────────┘                                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 22.3 Cross-Reference Format

Generated content MAY include C2PA manifest with CAP reference:

```json
{
  "c2pa:assertions": {
    "cap:reference": {
      "EventID": "019467a1-...",
      "ChainID": "019467a0-...",
      "VerificationEndpoint": "https://api.example.com/cap/verify"
    }
  }
}
```

---

## 23. SCITT Transparency Services

### 23.1 SCITT Overview

IETF SCITT (Supply Chain Integrity, Transparency, and Trust) provides general-purpose transparency infrastructure. CAP integrates as a domain-specific profile.

### 23.2 SCITT Integration Points

| SCITT Component | CAP Usage |
|-----------------|-----------|
| Transparency Service | External anchoring destination |
| Signed Statements | CAP events as SCITT statements |
| Receipts | Anchor proofs |
| Feeds | Event streams |

### 23.3 CAP as SCITT Profile

```
draft-kamimura-scitt-cap (planned)
├── Defines CAP events as SCITT signed statements
├── Specifies CAP-specific claim types
├── Maps Evidence Pack to SCITT receipt format
└── Enables cross-domain transparency
```

---

## 24. Enterprise Platform Integration

### 24.1 Azure OpenAI Service

Integration pattern:

```python
# Azure APIM → CAP Logger → Azure OpenAI
def cap_logging_middleware(request, response):
    # Log GEN_ATTEMPT before forwarding
    attempt_event = cap_logger.log_attempt(
        prompt_hash=sha256(request.prompt),
        model_version=request.model,
        user_hash=sha256(request.user_id)
    )
    
    # Forward to Azure OpenAI
    azure_response = azure_openai.complete(request)
    
    # Log outcome
    if azure_response.filtered:
        cap_logger.log_deny(attempt_event.id, azure_response.filter_reason)
    else:
        cap_logger.log_gen(attempt_event.id, azure_response.output_hash)
    
    return azure_response
```

### 24.2 AWS Bedrock

Integration with CloudWatch:

```python
# Bedrock Guardrails → CAP Logger → CloudWatch
def bedrock_cap_handler(event, context):
    cap_event = convert_guardrail_event_to_cap(event)
    
    # Write to CAP chain
    cap_chain.append(cap_event)
    
    # Also send to CloudWatch for operational monitoring
    cloudwatch.put_metric_data(cap_event.metrics())
```

### 24.3 Google Cloud Vertex AI

Integration with Cloud Audit Logs:

```python
# Vertex AI → CAP Logger → Cloud Audit Logs
def vertex_cap_integration(prediction_request):
    # CAP logging
    cap_event = cap_logger.log_vertex_prediction(prediction_request)
    
    # Cloud Audit Log (existing)
    audit_log.write(prediction_request.audit_entry())
    
    # Link records
    cap_event.external_ref = audit_log.entry_id
```

---

# Appendices

---

## Appendix A: JSON Schema

### A.1 Common Event Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://veritaschain.org/schemas/cap/v1.0/event-common.json",
  "title": "CAP v1.0 Common Event",
  "type": "object",
  "required": ["EventID", "ChainID", "Timestamp", "EventType", "HashAlgo", "SignAlgo", "EventHash", "Signature"],
  "properties": {
    "EventID": {
      "type": "string",
      "format": "uuid",
      "description": "UUIDv7 event identifier"
    },
    "ChainID": {
      "type": "string",
      "format": "uuid",
      "description": "UUIDv7 chain identifier"
    },
    "PrevHash": {
      "type": ["string", "null"],
      "pattern": "^sha256:[a-f0-9]{64}$",
      "description": "SHA-256 hash of previous event (null for genesis)"
    },
    "Timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp with timezone"
    },
    "EventType": {
      "type": "string",
      "enum": ["INGEST", "TRAIN", "GEN", "GEN_ATTEMPT", "GEN_DENY", "GEN_ERROR", "EXPORT"]
    },
    "HashAlgo": {
      "type": "string",
      "enum": ["SHA256", "SHA384", "SHA512"],
      "default": "SHA256"
    },
    "SignAlgo": {
      "type": "string",
      "enum": ["ED25519", "ML-DSA-65"],
      "default": "ED25519"
    },
    "EventHash": {
      "type": "string",
      "pattern": "^sha256:[a-f0-9]{64}$"
    },
    "Signature": {
      "type": "string",
      "pattern": "^ed25519:[A-Za-z0-9+/=]+$"
    }
  }
}
```

### A.2 GEN_ATTEMPT Schema

```json
{
  "$id": "https://veritaschain.org/schemas/cap/v1.0/gen-attempt.json",
  "title": "CAP v1.0 GEN_ATTEMPT Event",
  "allOf": [
    { "$ref": "event-common.json" },
    {
      "type": "object",
      "required": ["PromptHash", "InputType", "PolicyID", "ModelVersion"],
      "properties": {
        "EventType": { "const": "GEN_ATTEMPT" },
        "PromptHash": {
          "type": "string",
          "pattern": "^sha256:[a-f0-9]{64}$"
        },
        "ReferenceImageHash": {
          "type": "string",
          "pattern": "^sha256:[a-f0-9]{64}$"
        },
        "InputType": {
          "type": "string",
          "enum": ["text", "image", "text+image", "video", "audio", "multimodal"]
        },
        "PolicyID": { "type": "string" },
        "ModelVersion": { "type": "string" },
        "SessionID": { "type": "string", "format": "uuid" },
        "ActorHash": {
          "type": "string",
          "pattern": "^sha256:[a-f0-9]{64}$"
        }
      }
    }
  ]
}
```

### A.3 GEN_DENY Schema

```json
{
  "$id": "https://veritaschain.org/schemas/cap/v1.0/gen-deny.json",
  "title": "CAP v1.0 GEN_DENY Event",
  "allOf": [
    { "$ref": "event-common.json" },
    {
      "type": "object",
      "required": ["AttemptID", "RiskCategory", "RiskScore", "ModelDecision"],
      "properties": {
        "EventType": { "const": "GEN_DENY" },
        "AttemptID": {
          "type": "string",
          "format": "uuid",
          "description": "Reference to GEN_ATTEMPT EventID"
        },
        "RiskCategory": {
          "type": "string",
          "enum": [
            "CSAM_RISK",
            "NCII_RISK",
            "MINOR_SEXUALIZATION",
            "REAL_PERSON_DEEPFAKE",
            "VIOLENCE_EXTREME",
            "HATE_CONTENT",
            "TERRORIST_CONTENT",
            "SELF_HARM_PROMOTION",
            "COPYRIGHT_VIOLATION",
            "OTHER"
          ]
        },
        "RiskSubCategories": {
          "type": "array",
          "items": { "type": "string" }
        },
        "RiskScore": {
          "type": "number",
          "minimum": 0.0,
          "maximum": 1.0
        },
        "RefusalReason": { "type": "string" },
        "PolicyID": { "type": "string" },
        "PolicyVersion": { "type": "string" },
        "ModelDecision": {
          "type": "string",
          "enum": ["DENY", "WARN", "ESCALATE", "QUARANTINE"]
        },
        "HumanOverride": { "type": "boolean" },
        "EscalationID": {
          "type": ["string", "null"],
          "format": "uuid"
        }
      }
    }
  ]
}
```

---

## Appendix B: Event Examples

### B.1 Complete SRP Flow Example

**Step 1: GEN_ATTEMPT (Request Received)**

```json
{
  "EventID": "01947a00-0001-7000-0000-000000000001",
  "ChainID": "01947a00-0000-7000-0000-000000000000",
  "PrevHash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "Timestamp": "2026-01-13T14:30:00.000Z",
  "EventType": "GEN_ATTEMPT",
  "HashAlgo": "SHA256",
  "SignAlgo": "ED25519",
  "PromptHash": "sha256:7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069",
  "ReferenceImageHash": "sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "InputType": "text+image",
  "PolicyID": "cap.safety.v1.0",
  "ModelVersion": "flux-pro-1.5",
  "SessionID": "01947a00-0001-7000-0000-000000000000",
  "ActorHash": "sha256:2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae",
  "EventHash": "sha256:a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
  "Signature": "ed25519:MEUCIQDhE3H4xKjT..."
}
```

**Step 2: GEN_DENY (Refusal)**

```json
{
  "EventID": "01947a00-0001-7000-0000-000000000002",
  "ChainID": "01947a00-0000-7000-0000-000000000000",
  "PrevHash": "sha256:a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
  "Timestamp": "2026-01-13T14:30:00.150Z",
  "EventType": "GEN_DENY",
  "HashAlgo": "SHA256",
  "SignAlgo": "ED25519",
  "AttemptID": "01947a00-0001-7000-0000-000000000001",
  "RiskCategory": "NCII_RISK",
  "RiskSubCategories": ["REAL_PERSON", "CLOTHING_REMOVAL_REQUEST", "UPLOADED_REFERENCE"],
  "RiskScore": 0.97,
  "RefusalReason": "Request to generate non-consensual intimate imagery of identifiable person",
  "PolicyID": "cap.safety.v1.0",
  "PolicyVersion": "2026-01-01",
  "ModelDecision": "DENY",
  "HumanOverride": false,
  "EscalationID": null,
  "EventHash": "sha256:b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3",
  "Signature": "ed25519:MEQCIFRtK7m3..."
}
```

---

## Appendix C: Regulatory Mapping Tables

### C.1 EU AI Act Article 12 Detailed Mapping

| Article 12 Clause | Requirement | CAP Field/Feature |
|-------------------|-------------|-------------------|
| 12(1) | Automatic recording capability | Event-driven architecture |
| 12(2)(a) | Period of use recording | Timestamp, SessionID |
| 12(2)(b) | Reference database used | ModelContext.ModelID |
| 12(2)(c) | Input data identification | PromptHash, ReferenceImageHash |
| 12(2)(d) | Human oversight | HumanOverride field |
| 12(3) | Technical measures | Hash chain, signatures |
| 12(4) | Retention period | 6 months (Silver: 2 years) |

### C.2 DSA Compliance Mapping

| DSA Article | Requirement | CAP Support |
|-------------|-------------|-------------|
| 14 | Content moderation transparency | GEN_DENY events |
| 15 | Transparency reporting | Evidence Pack aggregation |
| 35 | Risk assessment | RiskCategory, RiskScore |
| 37 | Independent audits | Third-party verification protocol |
| 40 | Data access for research | Privacy-preserving verification |

---

## Appendix D: Implementation Checklist

### D.1 Bronze Level Checklist

- [ ] Event logging for INGEST, TRAIN, GEN, EXPORT
- [ ] SHA-256 hash chain implementation
- [ ] Ed25519 signature on all events
- [ ] ISO 8601 timestamp with timezone
- [ ] UUIDv7 event identifiers
- [ ] JSON Schema validation
- [ ] 6-month retention capability
- [ ] Basic export functionality

### D.2 Silver Level Checklist

All Bronze requirements, plus:

- [ ] GEN_ATTEMPT event logging (pre-processing)
- [ ] GEN_DENY event logging with RiskCategory
- [ ] GEN_ERROR event logging
- [ ] Completeness Invariant verification
- [ ] External anchoring (daily minimum)
- [ ] Evidence Pack generation
- [ ] PromptHash for privacy preservation
- [ ] 2-year retention capability
- [ ] Merkle tree construction
- [ ] Third-party verification endpoint

### D.3 Gold Level Checklist

All Silver requirements, plus:

- [ ] Hourly external anchoring
- [ ] HSM for signing key storage
- [ ] SCITT transparency service integration
- [ ] Real-time audit API
- [ ] 5-year retention capability
- [ ] 24-hour incident response capability
- [ ] Crypto-shredding support (GDPR)
- [ ] Multi-region redundancy
- [ ] Automated completeness monitoring
- [ ] Annual third-party audit

---

## References

### Normative References

- **[RFC 2119]** Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997
- **[RFC 8032]** Josefsson, S. and I. Liusvaara, "Edwards-Curve Digital Signature Algorithm (EdDSA)", RFC 8032, January 2017
- **[RFC 8785]** Rundgren, A., Jordan, B., and S. Erdtman, "JSON Canonicalization Scheme (JCS)", RFC 8785, June 2020
- **[RFC 9562]** Davis, K., Peabody, B., and P. Leach, "Universally Unique IDentifiers (UUIDs)", RFC 9562, May 2024
- **[RFC 3161]** Adams, C., Cain, P., Pinkas, D., and R. Zuccherato, "Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)", RFC 3161, August 2001
- **[RFC 6962]** Laurie, B., Langley, A., and E. Kasper, "Certificate Transparency", RFC 6962, June 2013

### Informative References

- **[EU AI Act]** Regulation (EU) 2024/1689 of the European Parliament and of the Council, laying down harmonised rules on artificial intelligence
- **[EU DSA]** Regulation (EU) 2022/2065 of the European Parliament and of the Council, the Digital Services Act
- **[C2PA]** Coalition for Content Provenance and Authenticity, Technical Specification v2.0
- **[SCITT]** IETF SCITT Working Group, draft-ietf-scitt-architecture
- **[Colorado AI Act]** Colorado SB24-205, Concerning Consumer Protections for Artificial Intelligence
- **[VAP]** VSO-VAP-SPEC-001, Verifiable AI Provenance Framework Specification v1.2
- **[VCP]** VSO-VCP-SPEC-001, VeritasChain Protocol Specification v1.1

### Academic References

- Kamimura, T. (2026). "Proving Non-Generation: Cryptographic Completeness Guarantees for AI Content Moderation Logs." Zenodo. https://doi.org/10.5281/zenodo.18213616

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2025-12-27 | VSO | Initial draft (Japanese) |
| 0.2.0 | 2026-01-10 | VSO | English version, SRP extension |
| 1.0 | 2026-01-13 | VSO | **Official Release**: Conformance levels, regulatory mapping, external anchoring requirements, SCITT/C2PA integration, Evidence Pack specification |

---

## Acknowledgments

The development of CAP v1.0 was informed by:

- Regulatory guidance from EU AI Act implementation discussions
- Industry feedback on AI content moderation challenges
- Academic research on cryptographic audit trails
- Open source community contributions

Special thanks to the early adopters and reviewers who provided invaluable feedback during the draft phase.

---

**© 2025-2026 VeritasChain Standards Organization. All rights reserved.**

This specification is published under CC BY 4.0 International License.

---

**Contact:**
- Website: https://veritaschain.org
- Email: standards@veritaschain.org
- GitHub: https://github.com/veritaschain
- Media: media@veritaschain.org
