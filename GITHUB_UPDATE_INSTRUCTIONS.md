# CAP v1.0 GitHub Update Instructions

## Overview

This document provides step-by-step instructions for updating the `veritaschain/cap-spec` repository from v0.2.0 to v1.0.

---

## Files to Update/Add

### 1. UPDATE: `README.md` (root)

Replace the existing README.md with the new version that includes:
- v1.0 release announcement banner
- Updated spec badge (v0.2.0 → v1.0)
- VAP v1.2 badge
- Conformance Levels section (Bronze/Silver/Gold)
- Updated Completeness Invariant formula
- Academic paper DOI reference
- Updated regulatory alignment table

### 2. UPDATE: `docs/CHANGELOG.md`

Replace with new version containing:
- v1.0 release notes
- Migration guide from v0.2.0 → v1.0
- Updated version links

### 3. ADD: `docs/CAP-Specification-v1.0.md`

New file - the complete CAP v1.0 specification (~1,600 lines).

**Do NOT delete** `docs/CAP-Specification-v0.2.md` - keep for historical reference.

### 4. ADD: `docs/Regulatory-Mapping/US-AI-Laws.md`

New file covering:
- TAKE IT DOWN Act mapping
- Colorado AI Act (SB24-205) mapping
- Federal AI requirements (OMB M-25-21/22)
- NIST AI RMF integration

---

## Git Commands

```bash
# 1. Clone repository
git clone https://github.com/veritaschain/cap-spec.git
cd cap-spec

# 2. Create release branch (optional)
git checkout -b release/v1.0

# 3. Copy updated files
# (Copy files from this package)

# 4. Stage changes
git add README.md
git add docs/CHANGELOG.md
git add docs/CAP-Specification-v1.0.md
git add docs/Regulatory-Mapping/US-AI-Laws.md

# 5. Commit
git commit -m "Release CAP v1.0 - Official Release

## What's New in v1.0

### Added
- Conformance Levels (Bronze/Silver/Gold) aligned with VAP v1.2
- External Anchoring Specification
- C2PA/SCITT Integration
- Comprehensive Regulatory Mapping (EU AI Act, DSA, Colorado AI Act)
- Implementation Checklist

### Changed
- Status: Draft → Official Release
- VAP reference: v1.1 → v1.2
- SRP now REQUIRED for Silver/Gold conformance

### Documentation
- Full specification: docs/CAP-Specification-v1.0.md
- US regulatory mapping: docs/Regulatory-Mapping/US-AI-Laws.md
- Updated changelog with migration guide"

# 6. Push to main
git checkout main
git merge release/v1.0
git push origin main

# 7. Create tag
git tag -a v1.0 -m "CAP v1.0 - Official Release

The first official release of Content / Creative AI Profile (CAP).

Key Features:
- Safe Refusal Provenance (SRP) for proving AI content refusals
- Completeness Invariant: ∑ GEN_ATTEMPT = ∑ GEN + ∑ GEN_DENY + ∑ GEN_ERROR
- Three Conformance Levels: Bronze / Silver / Gold
- External Anchoring (RFC 3161, SCITT, Blockchain)
- C2PA/SCITT Interoperability
- Regulatory Alignment: EU AI Act, DSA, Colorado AI Act, TAKE IT DOWN Act

Documentation:
- Specification: docs/CAP-Specification-v1.0.md
- Academic Paper: https://doi.org/10.5281/zenodo.18213616

License: CC BY 4.0 International"

git push origin v1.0
```

---

## GitHub Release Notes

When creating the GitHub Release, use the following content:

### Title
```
CAP v1.0 — Official Release
```

### Body
```markdown
# CAP v1.0 - Official Release

The first official release of **Content / Creative AI Profile (CAP)**, the world's first open specification for cryptographic AI content refusal logging.

## Highlights

🔐 **Safe Refusal Provenance (SRP)**
- Cryptographic proof of what AI refused to generate
- GEN_ATTEMPT → GEN_DENY event chain

📊 **Completeness Invariant**
```
∑ GEN_ATTEMPT = ∑ GEN + ∑ GEN_DENY + ∑ GEN_ERROR
```

🏅 **Three Conformance Levels**
| Level | Requirements |
|-------|-------------|
| Bronze | Hash chain, basic logging, 6-month retention |
| Silver | + SRP, external anchoring, 2-year retention |
| Gold | + Real-time verification, HSM, 5-year retention |

⚓ **External Anchoring**
- RFC 3161 TSA
- SCITT Transparency Services
- Blockchain anchoring

📋 **Regulatory Alignment**
- EU AI Act Article 12
- Digital Services Act Article 37
- Colorado AI Act (SB24-205)
- TAKE IT DOWN Act

## Documentation

- 📄 [Full Specification](docs/CAP-Specification-v1.0.md)
- 📚 [Academic Paper](https://doi.org/10.5281/zenodo.18213616)
- 🔬 [World-First Verification Report](docs/CAP_WorldFirst_Final_Consolidated_Report.md)

## Related

- [VAP Framework v1.2](https://github.com/veritaschain/vap-framework) - Parent framework
- [VCP v1.1](https://github.com/veritaschain/vcp-spec) - Finance profile
- [Reference Implementation](https://github.com/veritaschain/cap-safe-refusal-provenance)

## License

CC BY 4.0 International
```

---

## Post-Release Checklist

- [ ] README.md updated
- [ ] CHANGELOG.md updated
- [ ] CAP-Specification-v1.0.md added
- [ ] US-AI-Laws.md added
- [ ] Tag v1.0 created
- [ ] GitHub Release published
- [ ] Repository "About" description updated (if needed)
- [ ] Spec badge shows v1.0

---

## Repository "About" Section Update

If updating the repository description:

**Description:**
```
CAP (Content / Creative AI Profile) specification: a verifiable audit framework for AI content workflows, including Safe Refusal Provenance (SRP) to cryptographically prove non-generation and policy enforcement.
```

**Website:**
```
veritaschain.org/vap/cap/
```

**Topics (tags):**
```
regtech, content-ai, audit-trails, algorithmic-accountability, ai-governance, eu-ai-act, ai-provenance, ai-audit, cryptographic-logging, veritaschain, non-generation-proof, verifiable-logging, safe-refusal
```

---

**Document Created:** 2026-01-13  
**For:** veritaschain/cap-spec v1.0 Release
