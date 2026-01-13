# Changelog

All notable changes to the CAP specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- CAP v0.3.0 alignment with VCP v1.1
- Enhanced external anchoring tiers (L1/L2/L3)
- Crypto agility improvements
- Policy identification extensions

---

## [0.2.0] - 2026-01-10

### Added
- **SRP Extension (Safe Refusal Provenance)**: Complete Part II added
  - `GEN_ATTEMPT` event type for recording generation requests
  - `GEN_DENY` event type for recording refusals
  - `GEN_WARN`, `GEN_ESCALATE`, `GEN_QUARANTINE` event types
  - Completeness Invariant definition
  - Evidence Pack structure specification
  - Privacy-preserving design (prompt hashing, actor anonymization)
- **Risk Category taxonomy**: CSAM_RISK, NCII_RISK, MINOR_SEXUALIZATION, etc.
- **Regulatory alignment sections**: EU AI Act, DSA, TAKE IT DOWN Act mappings
- **Third-party verification procedures**: Step-by-step verification guide
- **JSON Schema appendices**: Machine-readable schemas for all event types

### Changed
- Document structure reorganized into Part I (Core) and Part II (SRP Extension)
- Enhanced threat model with actor analysis
- Expanded implementation guidelines with L1/L2/L3 levels
- English translation and international formatting

### Fixed
- Clarified relationship between GEN and GEN_ATTEMPT events
- Corrected AUDIT_ANCHOR event type code

---

## [0.1.0] - 2025-12-27

### Added
- Initial draft specification (Japanese)
- CAP Core Event Model (INGEST, TRAIN, GEN, EXPORT)
- Data Model definitions (CAP-CORE, CAP-RIGHTS, CAP-PERMISSIONS, CAP-CONFIDENTIALITY, CAP-CONTEXT)
- Integrity Layer specification (Hash Chain, Digital Signature, Merkle Anchoring)
- Target industry classification (Games, Film, Publishing, Music)
- Threat model overview (IP Dilution, Reverse Flow, Confidential Leakage, Deepfake, Brand Mimicry)
- Position within VAP Framework
- Non-goals definition

---

## Version Numbering

| Version | Meaning |
|---------|---------|
| 0.x.x | Pre-release, expect breaking changes |
| 1.0.0 | First stable release (planned) |

---

## Migration Guides

### 0.1.0 → 0.2.0

**Breaking Changes:**
- None (additive changes only)

**Recommended Updates:**
1. Implement SRP events if using content moderation
2. Update schema references to v0.2
3. Review new regulatory alignment documentation

---

[Unreleased]: https://github.com/veritaschain/cap-spec/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/veritaschain/cap-spec/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/veritaschain/cap-spec/releases/tag/v0.1.0
