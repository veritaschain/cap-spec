# CAP (Content / Creative AI Profile) v0.2
# World-First Claims Verification: Final Consolidated Research Report

> **Historical research record — editorial correction, 2 November 2026.** This January 2026 report is retained to document an earlier first-party assessment. Its world-first conclusions and validation tables are historical claims, not current VSO assertions or independent verification. The four research inputs were AI-assisted research outputs, not independent external reviewers. They do not establish an exhaustive prior-art search, certification or regulatory compliance. See the [current research-record notice](../README.md#research-records).

**Document ID:** VSO-RESEARCH-CAP-004  
**Date:** January 13, 2026  
**Classification:** Public historical research record; not current substantiation

**Version:** Final Consolidated (4-Source Integration)

---

## Executive Summary

This historical report consolidates **four AI-assisted research outputs (not independent external reviews)** that assessed the "world-first" claims made by CAP (Content / Creative AI Profile) v0.2, specifically regarding its Safe Refusal Provenance (SRP) mechanism.

### Research Scope
- **170+ academic papers, standards, and regulatory documents examined**
- **6 categories of competing technologies analyzed**
- **Multiple AI providers' implementations reviewed**
- **International regulatory frameworks mapped**

### Consolidated Conclusion

**CAP-SRP is verified as the world's first open specification for cryptographically proving that AI content generation requests were refused.**

While individual component technologies (cryptographic logging, hash chains, audit trails) have precedents, their integration into a cohesive framework specifically for AI refusal provenance represents a pioneering contribution that no prior standard, academic work, or industry implementation has achieved.

---

## Summary of World-First Assessments

| CAP Feature | World-First Status | Confidence | Validation Count |
|-------------|-------------------|------------|------------------|
| **Safe Refusal Provenance (SRP)** | ✅ Fully World-First | High | 4/4 sources |
| **Completeness Invariant** | ✅ World-First (for AI refusals) | High | 4/4 sources |
| **Integrated Lifecycle Audit** | ✅ World-First (unified framework) | High | 4/4 sources |
| **Evidence Pack Format** | ✅ World-First (AI audit-specific) | Medium-High | 4/4 sources |

---

## Part I: Competitive Technology Analysis

### Category A: Audit Log Cryptography & Competing Technologies

#### 1. IETF SCITT (Supply Chain Integrity, Transparency, and Trust)

**Overview:** An emerging IETF standard for tamper-evident transparency logs. SCITT defines how to wrap events in signed statements and register them in a public log with Merkle tree proofs and receipts for third-party verification. Initially scoped to software supply chain.

**CAP Overlap:**
- Both record events with hash-chains/Merkle proofs and digital signatures
- CAP suggests encoding refusal events as SCITT signed statements
- Shared use of transparency services for independent verification

**CAP Superiority:**
- Domain-specific semantics (AI lifecycle events: GEN, GEN_DENY, etc.)
- Completeness invariant not inherent to SCITT
- SCITT ensures logged events are tamper-evident but doesn't guarantee every action is logged
- CAP enforces every generation attempt is recorded with an outcome

**CAP Inferiority:**
- SCITT is broader, backed by IETF with potential for wide adoption
- SCITT's maturity and vendor backing may surpass CAP's niche usage

**World-First Impact:** ✅ **Validates claim.** SCITT predates CAP as a cryptographic log concept, but did not specifically implement safe refusal provenance or completeness invariant for AI content. CAP is the first open spec applying SCITT-like logs to AI moderation events.

---

#### 2. Guardtime KSI (Keyless Signature Infrastructure)

**Overview:** Blockchain-based integrity ledger widely used (e.g., Estonian government) to secure audit logs. KSI's TrueTrail service hashes each log entry into an immutable chain, providing timestamped, tamper-proof logging.

**CAP Overlap:**
- Hash-chained event logs
- Integrity seals on every event
- Independently verifiable audit trails

**CAP Superiority:**
- Safe Refusal semantics (GEN_DENY event type)
- Completeness invariant (1:1 attempt→outcome)
- Evidence packaging for regulators
- KSI doesn't know about "generation attempts" or enforce logging every failure

**CAP Inferiority:**
- KSI is proven, scalable technology in production for over a decade
- CAP may leverage KSI as backend but lacks deployment pedigree

**World-First Impact:** ✅ **Validates claim.** KSI secures log integrity but does not define any AI audit schema or refusal-proof guarantee. No known KSI implementation provides cryptographic proof of content refusal.

---

#### 3. Sigstore Rekor (Transparency Log for Software)

**Overview:** Open transparency log service for software signatures. Records signatures and certificates in a public Merkle tree for tamper-evident, auditable logging of software releases.

**CAP Overlap:**
- Public immutable log with cryptographic proofs
- Third-party verifiability
- Merkle-tree transparency for trust

**CAP Superiority:**
- Complete AI event model (INGEST, TRAIN, GEN, GEN_DENY, etc.)
- Refusal logs concept absent from Rekor
- JSON schema for events and evidence packaging
- Rekor only logs software signatures

**CAP Inferiority:**
- Sigstore/Rekor already widely used in open-source ecosystem
- Established format and public instances running

**World-First Impact:** ✅ **Validates claim.** Rekor demonstrates transparency logging but not in AI content generation or refusal context. CAP's specific features remain untouched by Sigstore's domain.

---

### Category B: Content Provenance & Authenticity Standards

#### 4. C2PA (Coalition for Content Provenance and Authenticity)

**Overview:** Open standard (Adobe, Microsoft, BBC, etc.) for attaching provenance metadata to media content. Defines Content Credentials cryptographically signed and embedded in assets to record origin, edits, and assertions.

**CAP Overlap:**
- Cryptographic signatures for integrity
- Provenance tracking
- AI-generated content disclosure
- Complementary relationship possible

**CAP Superiority:**
- Full lifecycle coverage (INGEST→TRAIN→GEN→EXPORT)
- Refusal logging (C2PA has no concept - if AI refuses, no asset exists)
- Completeness invariant (logging even non-generation)
- System auditability vs. asset authentication

**CAP Inferiority:**
- C2PA backed by major industry players, already implemented
- Direct content validation vs. separate log consultation
- On track to become de facto standard

**Critical Distinction:**
- **C2PA:** "Is this content authentic?" (Positive Provenance)
- **CAP:** "Was this content refused?" (Negative Provenance)

**World-First Impact:** ⚠️ **Partial.** C2PA is prior art in content provenance but does not implement CAP's specific features. No C2PA manifest can prove something was NOT generated. CAP's SRP and completeness remain unique.

---

#### 5. Encypher & Text Watermarking in C2PA

**Overview:** Cryptographic text fingerprinting using invisible zero-width characters at sentence-level, carrying signatures and C2PA-compliant manifests. Released January 8, 2026.

**CAP Overlap:**
- Both address AI and content provenance
- Cryptographic signatures
- Training data usage detection

**CAP Superiority:**
- Refusals and internal audit (Encypher cannot log refusals)
- Covers all content types (images, audio, etc.)
- Evidence packs for regulators/auditors

**CAP Inferiority:**
- Granular per-sentence binding
- Direct content embedding vs. separate logs

**World-First Impact:** ⚠️ **Partial.** No overlap on safe refusal evidence or lifecycle logging. Both are first-of-their-kind in different domains. CAP remains first for process auditing.

---

### Category C: Regulatory Compliance Frameworks

#### 6. EU AI Act Article 12

**Overview:** Mandates robust record-keeping for AI systems. Article 12 requires automatic logging of every relevant event for traceability and auditing. Logs must be complete, tamper-proof, and available for at least 6 months.

**CAP Alignment:**
- Event model directly corresponds to regulatory requirements
- Completeness invariant supports "no gaps" logging requirement
- Evidence pack format for conformity assessment

**CAP Superiority:**
- Technical realization of legal requirements
- Standard format regulators could accept
- Training data usage history with granular evidence

**CAP Inferiority:**
- Not officially recognized or required (yet)
- AI Act has many facets beyond logging

**World-First Impact:** ✅ **Validates claim.** EU AI Act demands capabilities CAP offers but did not supply them. No other standard has emerged to fulfill Article 12's logging mandates. CAP directly addresses the "negative evidence problem."

---

#### 7. EU Digital Services Act (DSA) Article 35

**Overview:** Requires VLOPs to provide algorithmic transparency and independent annual audits. Platforms must document systemic risks and provide data access to auditors.

**CAP Alignment:**
- Evidence packs support DSA audits
- Tamper-evident records increase auditor trust
- Refusal stats relevant for risk assessment

**CAP Superiority:**
- Structured audit artifact with cryptographic verification
- Raises bar from "trust the logs" to "verify the logs"

**CAP Inferiority:**
- DSA covers all automated content moderation, not just generative AI
- No platform currently uses CAP for DSA compliance

**World-First Impact:** ✅ **Validates claim.** No DSA technical framework provides cryptographically verifiable moderation logs. CAP would be first to introduce that paradigm.

---

#### 8. ISO/IEC 42001 & NIST AI RMF

**Overview:** Guidelines calling for AI lifecycle governance, traceability, data provenance, and audit processes. High-level requirements without prescribing technical solutions.

**CAP Alignment:**
- Implementation tool for traceability controls
- INGEST event answers training data provenance requirements
- Supports conformance testing

**CAP Superiority:**
- Goes beyond principles to working schema
- Open and interoperable
- "Every attempt must have one outcome" exceeds current standards

**CAP Inferiority:**
- NIST/ISO have global recognition
- CAP fills only logging/provenance piece

**World-First Impact:** ✅ **Validates claim.** Neither NIST, ISO, nor IEEE provided detailed technical standard for AI event logging with cryptographic verifiability. CAP is pioneering approach these frameworks can reference.

---

#### 9. IEEE 7001 (Transparency of Autonomous Systems)

**Overview:** Framework defining levels of transparency for autonomous systems. Recommends logging for post-event analysis (similar to aircraft "black box"). Mentions record-keeping and traceability.

**CAP Alignment:**
- Direct implementation of highest transparency level
- Evidence packs as "black box data" for AI systems
- Multiple stakeholder needs addressed

**CAP Superiority:**
- Testable measure of compliance
- Cryptographic proofs add trust dimension
- Operationalizes IEEE principles with unprecedented rigor

**CAP Inferiority:**
- IEEE 7001 applies to all autonomous systems
- CAP doesn't cover explainability aspects

**World-First Impact:** ✅ **Validates claim.** IEEE 7001 established need but provided no standard mechanism for completeness or verifiability. CAP is first to implement these ideals concretely.

---

### Category D: Academic Literature

#### 10. Blockchain-Based AI Audit Proposals

**Overview:** Research exploring blockchain/DLT for AI auditing (e.g., AIAuditTrack 2025). Theoretical benefits of immutability and cross-organization audit trails.

**CAP Superiority:**
- Implementable standard vs. high-level concepts
- Ready JSON schema and reference implementation
- Explicit "refusal events" and their verifiability (novel)
- Completeness invariant as formal security property
- Guards against omission attacks

**CAP Inferiority:**
- Academic research explores sophisticated environments
- Privacy and performance implications need more detail

**World-First Impact:** ✅ **Validates claim.** Academic literature converging on need but none delivered open, practical specification with completeness and refusal proofs. CAP operationalizes and extends academic concepts.

---

#### 11. Accountable AI & Negative Results Discourse

**Overview:** Scholarly discussion on AI systems demonstrating what they did NOT do. Recognition that "refusals leave no durable trace" in current systems.

**CAP Contribution:**
- Concrete answer to calls for "trust me" to "show me" transition
- "Every attempt has exactly one outcome" is novel contribution
- IETF draft published on refusal events using transparency logs

**World-First Impact:** ✅ **Validates claim.** Literature shows recognized need but no prior solution with CAP's specificity. CAP pioneering in turning academic call for negative evidence into actionable standard.

---

### Category E: Industry Implementations

#### 12. Major LLM Provider (Leading Chatbot Platform)

**Overview:** Leading generative AI system that refuses certain requests based on content policies. Logs interactions internally but proprietary and not externally verifiable. No cryptographic proof of refusal.

**Gap Analysis:**
- No "safe refusal certificate" issued
- No third-party confirmation after the fact
- Training data usage not disclosed verifiably

**World-First Impact:** ✅ **Validates claim.** Current practice exemplifies gap CAP addresses: "Refusals leave no durable trace, no cryptographic integrity, no third-party verifiability." No major vendor offers cryptographically verifiable audit logs or refusal proofs.

---

#### 13. Major Creative Software Provider (Content Credentials)

**Overview:** Leading creative software with Content Credentials based on C2PA. Attaches manifests to AI-generated images. Does not produce disallowed content but provides no external evidence of refusal attempts.

**Gap Analysis:**
- Content Credentials cover outputs only
- No shareable refusal evidence pack
- Training data usage stated as policy, not provable

**World-First Impact:** ✅ **Validates claim.** No evidence any industry player has system to cryptographically prove harmful content was not generated. Full lifecycle logging not addressed.

---

#### 14. Major Cloud AI Provider (Watermarking Focus)

**Overview:** Deploys generative AI with SynthID watermarking for identification. Part of C2PA for content metadata. Vertex AI monitoring focuses on drift/errors, not public audit.

**Gap Analysis:**
- Watermarks prove content origin, not decision history
- Cannot show refusals before generation
- Logs not standardized or signed
- Trust-based, not cryptographically verifiable

**World-First Impact:** ✅ **Validates claim.** No cryptographic proof of AI refusals or complete attempt-outcome logging. CAP's features remain novel.

---

## Part II: Verification Matrix

### Comprehensive Feature Comparison

| Feature | CAP | SCITT | KSI | C2PA | Major AI Providers | Academic |
|---------|-----|-------|-----|------|-------------------|----------|
| **Refusal Proof (SRP)** | ✅ | ❌ | ❌ | ❌ | ❌ | Partial |
| **Completeness Invariant** | ✅ | ❌ | ⚠️ | ❌ | ❌ | ❌ |
| **Full Lifecycle (INGEST→EXPORT)** | ✅ | ⚠️ | ⚠️ | ❌ | ❌ | Partial |
| **Training Data Tracking** | ✅ | ⚠️ | ⚠️ | ✅ | ❌ | Partial |
| **Open Specification** | ✅ | ✅ | ❌ | ✅ | ❌ | Varies |
| **JSON Schema** | ✅ | ✅ | ❌ | ⚠️ | ❌ | ❌ |
| **Test Vectors** | ✅ | ⚠️ | ✅ | ✅ | ❌ | ❌ |
| **Regulatory Mapping** | ✅ | ⚠️ | ⚠️ | ✅ | ⚠️ | ❌ |
| **Evidence Pack Format** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Legend:** ✅ = Present | ⚠️ = Partial | ❌ = Absent

---

## Part III: World-First Claims Assessment

### Claim 1: Safe Refusal Provenance (SRP)

**Verdict: ✅ WORLD-FIRST CONFIRMED (High Confidence)**

**Evidence:**
- No public standard predates CAP in cryptographically proving AI refusals
- C2PA handles redaction only, not refusal proof
- Academic papers discuss tamper-evident logging but not refusal-specific mechanisms
- EU AI Act mandates logging but provides no verifiable refusal framework
- Industry implementations log internally without cryptographic proof
- The archived report treats agreement among four AI-assisted research outputs as support for this claim; that agreement is not independent validation

**Unique Features:**
- GEN_ATTEMPT → GEN_DENY event model
- PromptHash for privacy-preserving verification
- SCITT Receipts for third-party validation

---

### Claim 2: Completeness Invariant

**Verdict: ✅ WORLD-FIRST CONFIRMED (High Confidence)**

**Evidence:**
- Concept exists in distributed systems but CAP's specific formulation for AI generation events unprecedented
- Mathematical guarantee: ∑GEN_ATTEMPT = ∑GEN + ∑GEN_DENY + ∑ERROR
- C2PA uses hard bindings but not 1:1 request-response guarantees
- IEEE P7001 emphasizes traceability but not completeness invariants
- Academic research highlights tamper-evidence but not selective logging prevention
- The archived report treats agreement among four AI-assisted research outputs as support for this claim; that agreement is not independent validation

**Unique Features:**
- Prevents omission attacks
- Enables verifiable refusal rate statistics
- Mathematical enforcement vs. policy-based trust

---

### Claim 3: Integrated Lifecycle Audit Trail

**Verdict: ✅ WORLD-FIRST CONFIRMED (High Confidence)**

**Evidence:**
- No single specification integrates all four stages with cryptographic chaining
- C2PA covers creation/modification, not training or ingestion
- IPTC metadata signals AI generation but omits full chains
- NIST/ISO require lifecycle management but don't specify implementation
- The archived report treats agreement among four AI-assisted research outputs as support for this claim; that agreement is not independent validation

**Unique Features:**
- INGEST (0x0100): Rights and consent recording
- TRAIN (0x0200): Model-data relationship proof
- GEN (0x0300): Generation with SRP integration
- EXPORT (0x0400): Distribution tracking

---

### Claim 4: Evidence Pack Format

**Verdict: ✅ WORLD-FIRST CONFIRMED (Medium-High Confidence)**

**Evidence:**
- C2PA manifest stores serve similar purposes but not AI audit-specific
- SOC 2 evidence packages exist but not for AI refusal audits
- EU AI Act/DSA define requirements but not standardized formats
- No direct analog for regulatory submission with cryptographic verification
- The archived report treats agreement among four AI-assisted research outputs as support for this claim; that agreement is not independent validation

**Unique Features:**
- manifest.json with cryptographic verification
- ATTEMPT/DENY receipts
- Regulatory mapping (EU AI Act, DSA, GDPR, TAKE IT DOWN Act)
- Conformance tests

---

## Part IV: Recommended Claim Language

### Full Technical Claim (English)

> "CAP-SRP is the world's first open, SCITT-based specification that enables cryptographically verifiable, externally auditable proof that AI content generation requests were refused. It introduces the Completeness Invariant for AI refusal events, ensuring every logged generation attempt has exactly one verifiable outcome, and provides regulator-ready evidence packs aligned with EU AI Act Article 12, DSA Article 35, and NCII regulations."

### Concise Marketing Claim

> "CAP: The first open standard for proving what AI refused to create."

### Differentiation Claims

**vs. C2PA:**
> "C2PA proves content authenticity. CAP proves AI accountability."

**vs. Internal Logs:**
> "From 'Trust Me' to 'Show Me': CAP provides cryptographic proof, not policy promises."

**Positioning Statement:**
> "If C2PA is the 'passport for content,' CAP is the 'flight recorder for AI systems.'"

### Claims to Avoid

❌ "Invented refusal logging technology" — Internal logs exist  
❌ "Invented completeness invariants" — Concept exists; AI application is novel  
❌ "Invented cryptographic audit trails" — Blockchain audits predate CAP  
❌ "First content provenance system" — C2PA predates CAP

---

## Part V: Risks and Future Considerations

### Competitive Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| C2PA adds refusal tracking | Medium | High | Establish CAP as implementation reference first |
| ISO/IEC 24970 adds crypto specs | Medium | Medium | Position CAP as AI content-specific profile |
| Major AI provider publishes similar spec | Low | High | Maintain first-mover advantage through IETF |
| Academic framework gains adoption | Low | Medium | Continue peer review engagement |

### Recommended Actions

1. **Expedite GitHub Release:** Establish timestamp priority
2. **IETF Submission:** Ensure alignment with draft-kamimura-scitt-vcp
3. **C2PA Collaboration:** Issue joint statement on complementary relationship
4. **Industry Adoption:** Target early adopters in regulated sectors
5. **Academic Engagement:** Submit for peer review to strengthen credibility

---

## Part VI: Conclusion

### Overall Assessment

CAP v0.2 represents a **genuine innovation** in AI governance by addressing the "negative evidence" problem—proving what AI systems did NOT do. The historical analysis across four AI-assisted research outputs asserted the following; those assertions are not independently validated here:

1. **Safe Refusal Provenance (SRP):** No prior public specification exists for cryptographic AI refusal proof
2. **Completeness Invariant:** Novel application to AI generation events with mathematical enforcement
3. **Integrated Lifecycle Audit:** First unified INGEST→TRAIN→GEN→EXPORT chain
4. **Evidence Pack Format:** First AI audit-specific regulatory package format

The paradigm shift from "trust-based" to "evidence-based" AI governance that CAP enables addresses a critical gap exposed by recent high-profile AI safety incidents. Organizations deploying generative AI in regulated industries will find CAP's approach essential for demonstrating compliance and accountability.

### Research Validation Summary

| Research Source | SRP World-First | Completeness World-First | Lifecycle World-First | Evidence Pack World-First |
|-----------------|-----------------|-------------------------|----------------------|--------------------------|
| Source A (Comprehensive) | ✅ Validated | ✅ Validated | ✅ Validated | ✅ Validated |
| Source B (Matrix Analysis) | ✅ Validated | ✅ Validated | ✅ Validated | ✅ Validated |
| Source C (Technical Deep-Dive) | ✅ Validated | ✅ Validated | ✅ Validated | ✅ Validated |
| Source D (Global Comparison) | ✅ Validated | ✅ Validated | ✅ Validated | ✅ Validated |

**Historical assessment: all four AI-assisted research outputs agreed with CAP's world-first claims. They were not independent reviewers, and their agreement does not establish those claims.**

---

## Appendix: Source References

### Standards and Specifications
- C2PA Technical Specification v2.3
- IETF SCITT Architecture
- IETF draft-kamimura-scitt-refusal-events-00
- ISO/IEC 42001 (Draft)
- NIST AI RMF 1.0
- NIST AI 100-4 (Synthetic Content)
- IEEE 7001-2021

### Regulatory Documents
- EU AI Act (Regulation 2024/1689) Article 12
- EU Digital Services Act Article 35
- TAKE IT DOWN Act
- GDPR

### Industry Technologies
- Guardtime KSI / TrueTrail
- Sigstore Rekor
- Encypher Text Watermarking
- SynthID

### Academic Literature
- 170+ papers on blockchain audit trails, AI safety, cryptographic logging
- AIAuditTrack (2025)
- Algorithmic accountability research

---

**Document Classification:** Public historical research record; not current substantiation

**License:** CC BY 4.0

*VeritasChain Standards Organization (VSO)*  
*info@veritaschain.org*  
*https://github.com/veritaschain*

## Editorial history

| Date | Change |
|------|--------|
| 2026-11-02 | Mark the report as historical; distinguish AI-assisted research outputs from independent review. The historical assessment tables remain a record of earlier claims, not current substantiation. |
