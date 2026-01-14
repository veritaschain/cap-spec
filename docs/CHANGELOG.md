# Changelog

All notable changes to the CAP specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-01-13

### 🎉 Official Release

CAP v1.0.0 is the first official release of the Content / Creative AI Profile specification.

### Added

- **Conformance Levels** (Bronze/Silver/Gold)
  - Bronze: Basic hash chain, signatures, 6-month retention
  - Silver: + SRP required, external anchoring (daily), 2-year retention
  - Gold: + Real-time verification, HSM, SCITT integration, 5-year retention

- **External Anchoring Specification** (Section 9)
  - RFC 3161 TSA integration
  - SCITT Transparency Services
  - Blockchain anchoring (optional)
  - Merkle tree construction for batch anchoring

- **Retention Framework** (Section 10)
  - Level-based retention requirements
  - Crypto-shredding support for GDPR compliance
  - Retention extension triggers

- **C2PA Integration** (Section 22)
  - Complementary positioning (CAP = system accountability, C2PA = content provenance)
  - Cross-reference format specification

- **SCITT Integration** (Section 23)
  - CAP as SCITT domain profile
  - Receipt format specification

- **Enterprise Platform Integration** (Section 24)
  - Azure OpenAI Service patterns
  - AWS Bedrock integration
  - Google Cloud Vertex AI integration

- **Implementation Checklist** (Appendix D)
  - Bronze/Silver/Gold checklists

- **Regulatory Mapping Tables** (Appendix C)
  - EU AI Act Article 12 detailed mapping
  - DSA compliance mapping
  - Colorado AI Act alignment
  - TAKE IT DOWN Act alignment

### Changed

- **Status**: Draft → **Official Release**
- **VAP Reference**: v1.1 → v1.2
- **SRP**: Now REQUIRED for Silver/Gold conformance
- **Evidence Pack**: Standardized per VAP v1.2 format
- **Completeness Invariant**: Now includes GEN_ERROR in formula

### Fixed

- JSON Schema corrections for GEN_DENY event
- Clarified RiskCategory enumeration values

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
| **1.0.0** | **First stable release** |
| 1.x.x | Backward-compatible additions |
| 2.0.0 | Breaking changes (if any) |

---

## Migration Guides

### 0.2.0 → 1.0.0

**Breaking Changes:**
- None (additive changes only)

**Required Updates for Silver/Gold Conformance:**
1. Implement SRP events (GEN_ATTEMPT, GEN_DENY) - now REQUIRED
2. Implement external anchoring (daily minimum for Silver)
3. Update Evidence Pack format to VAP v1.2 specification
4. Implement Completeness Invariant verification

**Recommended Updates:**
1. Update VAP reference from v1.1 to v1.2
2. Review new conformance level requirements
3. Implement C2PA cross-reference if applicable
4. Review updated regulatory mapping documentation

### 0.1.0 → 0.2.0

**Breaking Changes:**
- None (additive changes only)

**Recommended Updates:**
1. Implement SRP events if using content moderation
2. Update schema references to v0.2
3. Review new regulatory alignment documentation

---

[Unreleased]: https://github.com/veritaschain/cap-spec/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/veritaschain/cap-spec/compare/v0.2.0...v1.0.0
[0.2.0]: https://github.com/veritaschain/cap-spec/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/veritaschain/cap-spec/releases/tag/v0.1.0
