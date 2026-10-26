# CAP Glossary

Terminology and definitions for the Content/Creative AI Profile specification.

---

## A

### Actor
An entity (human or system) that performs actions within a CAP-enabled workflow. Actors are identified via `UserID` or `ActorHash` fields.

### ActorHash
SHA-256 hash of an actor identifier, used for privacy-preserving audit trails. Enables verification without exposing personal information.

### Anchor
See [External Anchor](#external-anchor).

### Asset
Any content or intellectual property subject to AI processing. Assets include images, video, audio, text, code, and other digital materials.

### AssetHash
SHA-256 hash of asset content. Provides a fingerprint for verification without storing the actual content.

### AssetID
Unique identifier for an asset, formatted as a URN (e.g., `urn:cap:asset:studio-a:char-design-001`).

### Audit Trail
A chronological record of events that provides evidence of AI system activities. CAP creates cryptographically verifiable audit trails.

---

## C

### CAP (Content/Creative AI Profile)
A domain-specific profile within VAP for AI workflows in content and creative industries. Defines events, data models, and integrity mechanisms.

### Chain
See [Hash Chain](#hash-chain).

### ChainID
UUID identifying an evidence chain. All events in a chain share the same ChainID.

### Completeness Invariant
In CAP v1.0 (§13), the SRP attempt–outcome invariant: every recorded `GEN_ATTEMPT` must have exactly one corresponding outcome event (`GEN`, `GEN_DENY` or `GEN_ERROR`). It is checked over recorded events; a request that was never recorded leaves nothing to detect. It is a profile-level invariant and is distinct from the VAP v1.2 Completeness Invariant (INT-008), which binds event count, first and last event identifiers and policy identifier in each AnchorRecord.

### Confidentiality Level
Classification of asset sensitivity: PUBLIC, INTERNAL, CONFIDENTIAL, SECRET, or PRE_RELEASE. CAP v0.2 field (`ConfidentialityLevel`, v0.2 repository schemas); CAP v1.0 does not define it.

### Consent Basis
The state of consent for asset usage. CAP v1.0 (§7.3): EXPLICIT, IMPLIED, NOT_REQUIRED or UNKNOWN. The v0.2 values EXPLICIT_WRITTEN, EXPLICIT_VERBAL and OPTED_OUT appear in the v0.2 repository schemas only.

### Crypto Agility
Design principle enabling migration to new cryptographic algorithms without breaking compatibility.

---

## D

### Deepfake
Synthetic media using AI to create realistic but fabricated content. CAP threat category TH-4.

### Digital Signature
Cryptographic proof of event authenticity using Ed25519 (default) or other algorithms.

---

## E

### Ed25519
The default digital signature algorithm in CAP. Provides 128-bit security level.

### Event
An atomic unit of activity in a CAP workflow. Core events: INGEST, TRAIN, GEN, EXPORT. SRP events: GEN_ATTEMPT, GEN_DENY, etc.

### Event Hash
SHA-256 hash of an event's canonical JSON representation. Computed per RFC 8785 (JCS).

### Evidence Pack
A structured collection of CAP events forming a complete audit package. Includes manifest, events, chain, statistics, and verification materials.

### EXPORT
CAP event type recording asset delivery or publication.

### External Anchor
A timestamp or hash recorded in an independent system (blockchain, RFC 3161 TSA, etc.) to prove existence at a point in time.

---

## G

### GEN
CAP event type recording content generation (when allowed).

### GEN_ATTEMPT
SRP event type recording that a generation request was received (before risk assessment).

### GEN_DENY
SRP event type recording that a generation request was refused.

### GEN_ERROR
SRP outcome event recording a failed generation (a system error, not a policy decision) (CAP v1.0 §12.1).

### GEN_ESCALATE
SRP event type recording that a request was escalated to human review (CAP v0.2 event type; in CAP v1.0, `ESCALATE` is a `ModelDecision` value on GEN_DENY, Appendix A.3).

### GEN_QUARANTINE
SRP event type recording that content was generated but quarantined for review (CAP v0.2 event type; in CAP v1.0, `QUARANTINE` is a `ModelDecision` value on GEN_DENY, Appendix A.3).

### GEN_WARN
SRP event type recording that generation was allowed with a warning (CAP v0.2 event type; in CAP v1.0, `WARN` is a `ModelDecision` value on GEN_DENY, Appendix A.3).

### Genesis Event
The first event in a hash chain. Has `PrevHash` set to null.

---

## H

### Hash Chain
A linked sequence of events where each event includes the hash of the previous event. Provides tamper detection.

### HashAlgo
Field specifying the hash algorithm used. Default: "SHA256".

---

## I

### INGEST
CAP event type recording asset ingestion into an AI workflow.

### Integrity Layer
The cryptographic mechanisms (hash chain, Merkle tree, signatures, anchoring) that ensure event integrity.

---

## J

### JCS (JSON Canonicalization Scheme)
RFC 8785 standard for deterministic JSON serialization. Required for consistent hash computation.

---

## L

### L1/L2/L3
Implementation levels of CAP v0.2, superseded in CAP v1.0 by Bronze / Silver / Gold (CAP v1.0 §2):
- **L1 (Basic)**: INGEST/GEN events only
- **L2 (Standard)**: All events + hash chain
- **L3 (Enterprise)**: L2 + Merkle anchoring + external verification

---

## M

### Merkle Root
The root hash of a Merkle tree containing multiple events. Enables efficient bulk verification.

### Merkle Tree
Binary tree structure where leaf nodes are event hashes and each parent is the hash of its children. Used for external anchoring.

### Model Context
Information about the AI model used: ModelID, ModelVersion, ModelType, ModelProvider, Environment.

---

## N

### NCII (Non-Consensual Intimate Imagery)
Intimate images shared without consent. CAP risk category NCII_RISK.

### Non-Goals
Explicit exclusions from CAP scope: prohibition, auto-detection, real-time control, quality evaluation.

---

## P

### Permitted Use
Object specifying allowed usage of an asset. CAP v1.0 (§7.3): Training, Generation, Distribution, Commercial. Derivative, Attribution and Restrictions are CAP v0.2 fields.

### Policy ID
Identifier for the content moderation policy applied during risk assessment.

### PrevHash
Hash of the previous event in the chain. Null for genesis events.

### Prompt Hash
SHA-256 hash of a generation prompt. Stored instead of raw prompt for privacy.

### Provenance
The origin and history of an asset, recorded as cryptographically verifiable events.

---

## R

### Refusal Stats
Aggregated statistics in Evidence Packs showing total attempts, refusals, and breakdown by risk category. The `statistics/refusal_stats.json` file belongs to the v0.2 sample Evidence Pack; a CAP v1.0 manifest carries `CompletenessVerification` counts (§15.3).

### Rights Basis
The justification for using an asset. CAP v1.0 (§7.3): OWNED, LICENSED, PUBLIC_DOMAIN, FAIR_USE or UNKNOWN. STATUTORY_EXCEPTION appears in the v0.2 repository schemas only.

### Risk Category
Classification of content risks (CAP v1.0 §14.3, Appendix A.3): CSAM_RISK, NCII_RISK, MINOR_SEXUALIZATION, REAL_PERSON_DEEPFAKE, VIOLENCE_EXTREME, HATE_CONTENT, TERRORIST_CONTENT, SELF_HARM_PROMOTION, COPYRIGHT_VIOLATION, OTHER.

### Risk Score
Numerical confidence (0.0-1.0) in risk assessment.

---

## S

### SHA-256
The default hash algorithm in CAP. Part of SHA-2 family, FIPS 180-4.

### SignAlgo
Field specifying the signature algorithm used. Default: "ED25519".

### SRP (Safe Refusal Provenance)
Extension to CAP providing cryptographic evidence of content moderation decisions.

---

## T

### Timestamp
ISO 8601 formatted date-time with millisecond precision in UTC.

### TRAIN
CAP event type recording model training or fine-tuning activities.

### Threat Model
Analysis of security threats addressed by CAP: IP Dilution, Reverse Flow, Confidential Leakage, Deepfake/Persona Abuse, Brand Mimicry.

---

## U

### UUID v7
Time-ordered UUID format per RFC 9562. Used for EventID to ensure chronological ordering.

---

## V

### VAP (Verifiable AI Provenance Framework)
Parent framework defining cross-domain requirements for AI audit trails. CAP is a VAP profile.

### VCP (VeritasChain Protocol)
VAP profile for financial/trading domains. Sibling to CAP.

### Verification
The process of checking event integrity: hash validation, chain linkage, signature verification, completeness check.

### VSO (VeritasChain Standards Organization)
Standards organization maintaining the VAP, VCP and CAP specifications, operated by VeritasChain Co., Ltd. (see [GOVERNANCE.md](../GOVERNANCE.md)).

---

## Related Documents

- [CAP Specification v1.0](CAP-Specification-v1.0.md)
- [Threat Model](Threat-Model.md)
- [CAP vs VCP](CAP-vs-VCP.md)

---

*Last updated: 2026-10-26*
