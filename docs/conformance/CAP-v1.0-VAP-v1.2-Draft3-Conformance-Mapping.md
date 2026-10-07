# CAP v1.0 → VAP v1.2 Draft 3: conformance mapping

**Status:** Review draft; descriptive gap assessment, not an approved conformance declaration.  
**Assessment baseline:** 2026-10-07 (Asia/Tokyo). Prepared 2026-10-08 (Asia/Tokyo).  
**Scope:** The released CAP v1.0 specification against the pinned VAP v1.2.0 Draft 3 requirement set, including its 2026-10-06 editorial folds.  
**Suggested repository path:** `docs/conformance/CAP-v1.0-VAP-v1.2-Draft3-Conformance-Mapping.md`  
**Companion:** [Minimal change proposal](CAP-VAP-v1.2-Minimal-Change-Proposal.md).

## 1. Disposition

**CAP v1.0 conformance to VAP v1.2 has not been established.** Publishing this mapping would satisfy a documentation step, not remove the technical divergences. CAP v1.0 remains Released in its own right; VAP v1.2 remains Draft 3. Neither status is a finding of implementation conformance or certification.

CAP has substantial reusable infrastructure: UUIDv7 identifiers, RFC 8785 canonicalization, SHA-256/Ed25519, mandatory hash chaining, an anchor-record structure, SRP causal references, and Evidence Packs. The absence of the literal word `AnchorRecord` does **not** mean anchor records are absent: CAP §9.5 already defines them. Conversely, similar names do not establish equivalent assurance: CAP SRP outcome completeness is not VAP INT-008 anchored-batch completeness; CAP content-safety `PolicyID` is not automatically VAP verification-policy identification.

Unconditional blockers include Bronze anchoring, signed and policy-bound batch records, anchor continuity, mandatory verification-policy/version declarations, and conflicting numeric encodings. Hash-input and Merkle-proof inconsistencies require resolution before interoperable verification can be asserted. Provenance, trace grouping and accountability need additional rules for stronger VAP claims. ERASURE, RECOVERY, XREF and SCITT have different applicability triggers and are assessed separately below.

| CAP v1.0 tier | VAP-Core finding | VAP-Standard / VAP-Full finding |
| --- | --- | --- |
| Bronze | Not established; CAP explicitly permits no external anchor, contradicting INT-006. Shared gaps remain even if a Bronze implementation voluntarily anchors. | Not established; satisfying more layers cannot cure the integrity blockers. |
| Silver | Not established; daily TSA anchoring exists, but signed-record/policy/completeness/continuity and data-model requirements are not fully specified. | Not established; additional provenance/traceability/accountability coverage is not established. |
| Gold | Not established; hourly anchoring and HSM do not close the shared gaps. SCITT alignment has additional conditional obligations. | Not established; no automatic Gold → VAP-Full equivalence. |

These are specification-level findings. An implementation might provide extra functionality, but CAP tier membership alone does not prove it. No implementation, production log, reference implementation, certificate, or third-party audit was tested in this review.

## 2. Reproducible sources and precedence

| Key | Document and pinned revision | SHA-256 of exact specification bytes |
| --- | --- | --- |
| C | [CAP v1.0, `docs/CAP-Specification-v1.0.md`](https://github.com/veritaschain/cap-spec/blob/d1ffc493c5389189bcea2ed45e645682c9517708/docs/CAP-Specification-v1.0.md), repo commit `d1ffc493c5389189bcea2ed45e645682c9517708` | `6510ef93b9a00e400964da8235b1790d2fb16f8a45ae5c254edfb84e581c18f4` |
| V | [VAP v1.2.0 Draft 3, `spec/v1.2/VAP_Framework_Specification.md`](https://github.com/veritaschain/vap-spec/blob/1771fdb2fc6dbd0ae92718e4fc44acc73dc395b3/spec/v1.2/VAP_Framework_Specification.md), repo commit `1771fdb2fc6dbd0ae92718e4fc44acc73dc395b3` | `67e9b2c20f7adecf00ef6df8f2f245673cd66bb91455eb8336142f1f8f9c7e0d` |

Additional read-only sources:

- [CAP README at the same CAP commit](https://github.com/veritaschain/cap-spec/blob/d1ffc493c5389189bcea2ed45e645682c9517708/README.md): Released status, outstanding mapping, Bronze divergence, and non-guarantee disclosure.
- [CAP VERSIONING.md at the same CAP commit](https://github.com/veritaschain/cap-spec/blob/d1ffc493c5389189bcea2ed45e645682c9517708/VERSIONING.md): changes that invalidate previously conformant implementations require a MAJOR increment. Its separate current-version/history text is stale (still v0.2); that inconsistency does not authorize bypassing the breaking-change process.
- [VSO-VAP-CHANGE-001 at the same VAP commit](https://github.com/veritaschain/vap-spec/blob/1771fdb2fc6dbd0ae92718e4fc44acc73dc395b3/spec/v1.2/VSO-VAP-CHANGE-001.md): CH-01–CH-12 and migration context. V §1.7 makes the framework text prevail where details differ.
- [VAP v1.2 README](https://github.com/veritaschain/vap-spec/blob/1771fdb2fc6dbd0ae92718e4fc44acc73dc395b3/spec/v1.2/README.md) confirms the current and earlier Draft 3 digests.

The latest commits returned for these repositories predate the assessment cutoff; both downloaded main-branch specification texts were byte-compared with the pinned revisions. CAP open issue and open PR searches returned empty at retrieval on 2026-10-08 JST. This corroborates the supplied observation but is not an archived proof of counts at every instant on October 7, and issue counts have no bearing on conformance.

Only C and V are used to decide technical requirements. README text is contextual and cannot silently amend released C. Repository schemas outside Appendix A, SDKs, test vectors, the separately linked research paper, and external legal accuracy are outside this assessment. RFC numbers below identify the requirements **as cited by V**; this is not a separate standards-status or legal review.

## 3. Reading the matrix

| Result | Meaning |
| --- | --- |
| **S — Supported** | Existing text provides the assessed requirement or an identified semantic equivalent. This is clause-level support, not a product PASS. |
| **P — Partial / not established** | Some machinery exists, but the whole obligation is not guaranteed by C. Additional implementation evidence alone cannot fix a missing profile-level obligation. |
| **C — Conflict** | C explicitly allows or requires behavior incompatible with the assessed V requirement. |
| **U — Unresolved interpretation** | Wording, serialization, or scope needs an authoritative decision; no PASS is inferred. |
| **N — Not applicable under stated condition** | The optional feature is not invoked. Conditional requirements become applicable immediately upon use or claim. Silence alone is not proof of non-use. |

Routes: **I** = interpretation/mapping only; **E** = clarification or editorial correction consistent with existing obligations; **R** = CAP normative amendment; **F** = framework/profile interpretation to be recorded by maintainers. `M01` etc. refer to the companion proposal. A SHOULD gap is reported as a recommendation gap, not promoted to a MUST failure. A conditional MUST is not postponed to VAP-Full merely because V §8.1 summarizes conditional capabilities in that row.

## 4. Integrity and Shared Assurance Core

| ID | V clause / force | CAP evidence | Result and exact disposition | Route |
| --- | --- | --- | --- | --- |
| I01 | §1.2, independent verification, MUST | §§1.2, 9, 15–17 | P overall. Third-party verification is an explicit design goal; anchorless Bronze and missing verification materials prevent a universal claim. | R M01–M05, M11 |
| I02 | INT-001; §7.3, JCS before hashing, MUST | §8.2; normative RFC 8785 reference | S for canonicalization choice. Hash-input exclusion is a distinct problem in I04. | I |
| I03 | INT-002, unique event ID, MUST; UUIDv7 recommended | §§6.3, 7.1; Appendix A.1 | S for specified UUIDv7 identity. Schema `format: uuid` alone does not enforce version 7 or global uniqueness; a validator must check the prose obligation too. | I / E M12 |
| I04 | INT-003, canonical event hash, MUST | §§7.1, 8.2–8.4; Appendix A.1 | P/U. SHA-256 and EventHash exist, but §8.2 excludes only Signature: verification includes the populated EventHash in its own hash input. A freshly hashed then populated event is generally not reproducible by §8.4. Exclude EventHash as well and publish vectors; verify the selected V serialization mapping. | E/R/F M05, M06 |
| I05 | INT-004, verifiable ordering/membership, MUST | §§2.2–2.4, 6.3, 8.1–8.4, 9 | P. Mandatory PrevHash provides an appropriate mechanism in principle. UUID time ordering alone is not cryptographic sequence verification. Hash defect and Merkle defect remain; mechanism/latency declarations are incomplete. | I for mechanism; E/R M01, M05 |
| I06 | INT-004, per-level mandatory mechanism and detection latency, MUST; §8.2 | §§2, 9.3, 17 | P. Requirements can be collected into a matrix, but no complete normative matrix, explicit proof depth, or completeness/detection disclosure exists. | E for consolidation; R M01 |
| I07 | INT-004a, PrevHash OPTIONAL at V level, profile MAY require | §§2.2, 6.3, 8 | S. CAP's stronger MUST is permitted. V §5.2's expectation that CAP might make PrevHash optional is not a requirement to weaken CAP. | I; preserve MUST |
| I08 | INT-005, signatures SHOULD | §§2.2, 8.3 | S. CAP mandates Ed25519 on all events, exceeding the recommendation. Does not substitute for a signed batch root/record. | I |
| I09 | INT-006, Merkle + external signed-root anchoring at all levels, MUST | §§4.2, 9.3: Bronze Optional; §§2.3–2.4: Silver daily TSA, Gold hourly and SCITT | C at Bronze; P at Silver/Gold because signed-root/record obligations and exact proof rules remain incomplete. An event signature or TSA signature over a bare root is not automatically a signature covering the batch metadata. | R M01–M03 |
| I10 | INT-006; §4.1.4, acceptable target classes / frequency / proof depth | §§2.3–2.4, 9.3–9.4 | P. TSA/SCITT/public-blockchain concepts map. Silver specifically requires TSA; Gold inherits it and adds SCITT. A generic services list cannot be interpreted as removing the tier MUSTs. | I for classes; R M01, M02 |
| I11 | INT-007(a), designated acceptable fallback, MUST | §9.4 lists services; no continuity procedure | P. Listing alternatives is not designating a fallback in a plan. | R M04 |
| I12 | INT-007(b), bounded migration/failover window, MUST | No counterpart in §§9–10 | P. V recommends 30 days; it is not already a CAP limit, and it does not suspend ordinary interval obligations. | R M04 |
| I13 | INT-007(c); §7.5, local historical AnchorRecord copies, MUST | §10.1: anchor retention S=5 years, G=10 years; B=N/A | P. Retention periods exist for S/G, but locality and offline historical-verification sufficiency are unspecified. B needs a requirement. V states no numeric retention lifetime; CAP must specify its retention scope explicitly. | R M04, M11 |
| I14 | INT-007, outage queue and retry, MUST | No counterpart | P. No normative retry/queue behavior. | R M04 |
| I15 | INT-007, error event when gap >2× interval, MUST | GEN_ERROR concerns a generation attempt (§12.1) | P. Reusing GEN_ERROR without a type distinction would contaminate SRP outcome accounting. Define a dedicated operational error event or rigorously separated equivalent. | R M04, M12 |
| I16 | INT-008, bound count / first / last / policy, MUST | §9.5 EventCount, FirstEventID, LastEventID; §15.3 pack counts | P. Three batch fields exist, so not a wholesale absence. Anchor PolicyID, signed binding of the metadata, and an unambiguous declared batch scope are missing. Pack counts are not an anchored batch commitment. | I for three fields; R M02, M03 |
| I17 | INT-008, post-anchor omission/split-view detection | §§13.1–13.3 SRP invariant | P. Attempt/outcome correspondence complements but cannot replace commitment to all in-scope events, including INGEST/TRAIN/EXPORT and operational events. No pre-measurement completeness claim is justified. | R M03 |
| I18 | §4.1.2 scope note, completeness window and disclosure to authorities, MUST | §§9.3, 13, 15, 17 | P. Daily/hourly intervals are known, but required disclosure of limitations is absent. Bronze has no bounded external verification window. | R M01, M03, M11 |
| I19 | INT-009, recovery bounded per type and tier, MUST when used | No RECOVERY or equivalent sequence-altering recovery contract | N only if no operation changes the effective sequence; otherwise P. A pipeline retry is not necessarily sequence recovery. SKIP/REBUILD/MERGE/CHECKPOINT cannot be silently enabled under unspecified bounds. | I applicability; R M08 if supported |
| I20 | INT-009, chained/anchored recovery record with break point and evidence | No counterpart | N under I19 non-use condition; otherwise P. A generic GEN_ERROR does not supply this evidence. | R M08 if supported |
| I21 | INT-009, human-approved Emergency Override beyond bounds and reporting | Context.Role, HumanOverride do not specify this protocol | N under I19; otherwise P. A Boolean is not an identified approval, and approval cannot erase evidence of a gap. | R M08 if supported |
| I22 | INT-009, recovery events not filtered from batches, MUST | Appendix A.1 closes event-type enum without RECOVERY | N under I19; otherwise C for encoding a new literal RECOVERY under existing schema. Must extend schema or specify an approved equivalent; no equivalent exists in C. | R M08, M12 |
| I23 | §4.1.3 Mechanism A, normative when PrevHash used | C §8.2 hashes a flat object; V hashes canonical Header, Payload and previous hash | U. Similar chaining semantics do not prove byte-equivalent hash inputs. C genesis `null` also needs a documented correspondence to V GENESIS_HASH. Do not relabel hashes through a case conversion. | F + E/R M05, M06 |
| I24 | §4.1.3 Mechanism B, inclusion + anchor signature + external proof + completeness | §§16.2, 17.2 | P. CAP has high-level verification stages but no complete signed-record/count-range-policy verification. | R M02, M03, M05 |
| I25 | §4.1.3, both mechanisms SHOULD be checked when PrevHash present; failure of either fails | §§8.4, 17.2 | P. Chain and anchor verification are listed; the combined failure rule and precise implementation are incomplete. Recommendation plus explicit failure semantics should be retained. | E/R M05 |
| I26 | §4.1.4, RFC 6962 tree and 0x00/0x01 domain separation, REQUIRED | §3.3 cites RFC 6962; §9.2 schematic; §16.2 fold starts with EventHash and hashes sibling concatenations without prefixes | U/C in verification example. The inherited RFC points the right way; the pseudocode conflicts and must not be treated as a valid implementation. Define leaf bytes, index/tree size, split rules and domain-separated hashing. | E/R M05 |
| I27 | §4.1.4; §7.5, signed AnchorRecord per batch close, MUST | §9.5 anchor has no producer signature, signer ID, signature algorithm or policy ID | P. AnchorProof may contain target authentication but does not by itself bind all record fields. | R M02 |
| I28 | §§4.1.5, 6.1, approved algorithms and strength | SHA-256 / Ed25519 in §§2.2, 7.1, 8.3 | S for the mandatory classical baseline. Other algorithms listed in Appendix A are not a complete migration protocol. No RSA-2048 deployment is required. | I; M05 for migration |
| I29 | §4.1.5, algorithm identifiers and future migration, MUST | HashAlgo/SignAlgo; §3.3 crypto agility; Appendix A.1 enums | S for identifier presence; P for usable migration. SHA384/SHA512 enums coexist with a sha256-only EventHash pattern; ML-DSA enum coexists with an ed25519-only Signature pattern and Ed25519 MUST. | R M05, M12 |
| I30 | §6.2.2, hybrid RECOMMENDED; classical authoritative until profile changes | Ed25519 MUST, ML-DSA planned; no dual-signature contract | N for optional PQC fields when unused; recommendation not implemented. If hybrid is enabled, classical verification remains authoritative; ML-DSA enum alone must not be advertised as conformance. | I non-use; R if enabled |

## 5. Provenance, traceability and accountability

| ID | V clause / force | CAP evidence | Result and exact disposition | Route |
| --- | --- | --- | --- | --- |
| P01 | §4.2.2–4.2.3, actor | §§7.4–7.5 Context / ModelContext; §14 ActorHash, ModelVersion | P. Creator/model semantics map naturally; model parameter hash and uniform event coverage are not guaranteed. A pseudonym is not automatically a resolved responsible operator. | I semantic mapping; R M06, M10 |
| P02 | §4.2.2–4.2.3, input | §7.2 Asset; §14.1 PromptHash, ReferenceImageHash | P. Source commitments exist for specified events; general input source list/time/hash bindings need a declared mapping. No plaintext disclosure is required merely to perform mapping. | I/R M06 |
| P03 | §4.2.2–4.2.3, context | §§7.3–7.5 Rights, ModelContext, content PolicyVersion | P. License/model/environment fields cover part of the abstract model, not all parameters/constraints on every event class. | I/R M06 |
| P04 | §4.2.2–4.2.3, action/outcome/explainability | §§6, 12–14 EventType, ModelDecision, RefusalReason, RiskScore | P. SRP result meanings map; RiskScore is risk, not necessarily confidence. Explanatory factors/method, status and time need event-specific mapping; do not fabricate model internals. | I/R M06 |
| P05 | TRC-001, causal relationships, MUST | §13.2 AttemptID; §14.2; Appendix A.3 | S for expressing SRP attempt→outcome causality. P for complete ingestion→training→generation→export lineage: chronological PrevHash and same ChainID do not establish causation. | I for capability; R M06 if broader coverage required |
| P06 | TRC-002, grouping via trace_id, MUST | ChainID (§7.1), optional SessionID (§7.4, A.2) | U/P. A logging chain can contain many workflows; SessionID is not uniformly required. A conditional ChainID→trace_id mapping works only if chain scope actually equals a trace; CAP does not require that invariant. | F/R M06 |
| P07 | TRC-003, point-in-time state reconstruction, SHOULD | ModelVersion, ordered events, rights/context | P recommendation. No guaranteed state/snapshot reconstruction contract. Do not count as an unconditional MUST blocker. | E/R for claimed coverage |
| P08 | TRC-004, RCA query capability, SHOULD | §§16–17 selective query; §§2.4, 4.2 audit API | S conceptually for described queries; P for mandatory uniform support in lower tiers. Record an exception or extend query contract if claiming full recommendation coverage. | I/E |
| P09 | TRC-005, XREF optional | §22.3 C2PA reference; §24.3 Cloud Audit Log reference | N when no VAP XREF is invoked. These references are not independent dual logging. Absence of XREF is not itself nonconformance, even at VAP-Full. | I |
| P10 | TRC-005, IDs, shared event key/tolerance, independent anchors, roles, reconciliation/severity; >2-party ordering | No such contract | P if XREF is claimed or used. Must specify all conditions, not just introduce cross_reference_id. | R M09 if enabled |
| P11 | §§4.4.2–4.4.3, accountability model | Context.UserID/Role, ModelProvider, RightsHolder, HumanOverride | P. Domain actors are partially represented; operator attribution, last approver/time, delegation scope/validity, override actor/reason/actions/time are not fully defined. | I/R M10 |
| P12 | §4.4.4, oversight record guidance | HumanOverride (§14.2, A.3); EscalationID | P for evidence richness. This V subsection contains no RFC 2119 requirement; do not invent a mandatory HALT event or require CAP to provide intervention capability. Binding fields in §7.1 and INT-009 remain separately assessed. | I scope; R M10 for actual records |

## 6. Versioning, policy, data model, privacy and composition

| ID | V clause / force | CAP evidence | Result and exact disposition | Route |
| --- | --- | --- | --- | --- |
| D01 | §§4.5.3, 10.4, profile minimum VAP version | C references VAP v1.1; §3 inheritance statement; no min_vap_version | P. A parent citation is not a minimum-version/conformance declaration. Do not insert 1.2 into released CAP 1.0 as though the analysis had passed. | R M06; explicit target only in proposal |
| D02 | §7.1, event vap_version and profile id/version | §7.1 flat common fields; §15.3 PackVersion | P. PackVersion is an Evidence Pack format version, not per-event profile/VAP version. Open JSON properties permit adding data but do not make it required. | R M06 |
| D03 | §7.1, policy_id reverse-domain syntax | §§14.1–14.2 `cap.safety.v1.0`; Appendix A.2/A.3 | C for treating the example as a VAP PolicyID; it lacks `<reverse_domain>:<local_id>` and represents content safety. P for overall policy coverage. Keep content policy and verification policy separate. | R M06 |
| D04 | §7.1, per-event tier, VAP level, registration issuer | §2.5 published conformance statement; §15.3 ConformanceLevel | P. Organization/pack declarations are not per-event bound policy. Bronze/Silver/Gold do not imply Core/Standard/Full. | R M06 |
| D05 | §7.1, verification_depth and both required booleans true | No counterpart | P. Mechanisms can be inferred for some tiers but the event's self-declaration is absent. Bronze's optional anchoring cannot be reconciled by setting a Boolean true. | R M01, M06 |
| D06 | §7.1, common envelope/header/security structure | C flat CamelCase object; ISO Timestamp only; no uniform signer_id/anchor linkage | U/P. Semantic correspondences exist, but the V text says all events MUST have the structure. No blanket alternate-wire exemption is established by C. Timestamp integer units/precision, event codes and byte mapping need a binding. | F/R M06 |
| D07 | §7.2, all numeric values strings, MUST | A.3 RiskScore REQUIRED number; §7.2 AssetSize; §9.5 EventCount; §15.3 numeric counts | C. Stringifying existing signed records changes canonical bytes/hashes. A view generated for reporting does not repair original wire-level conformance. V int64/int32 annotations describe logical types; they do not explicitly exempt fields from §7.2. | R M06, M12; request F clarification if exemption desired |
| D08 | §6.3.1–6.3.2, per-subject DEK and preserved evidence | §10.3 per-user encryption/key deletion/chain preservation | S at mechanism-description level; P for complete protection of Merkle/anchor verification. Ciphertext/committed bytes must remain stable, and key-destruction evidence is absent. | I for mechanism; R M07 |
| D09 | §6.3.3; §7.4, append-only anchored ERASURE when shredding | §10.3 supports shredding; Gold D.3 checklist; A.1 enum excludes ERASURE | N only if no crypto-shredding occurs; P/C when used. Gold's documented support makes a blanket profile-wide N/A particularly inappropriate. Must retain prior events, hashes and proofs. | R M07, M12 |
| D10 | §6.3.3, targets / reason / destruction proof / authorizing operator | No ERASURE payload | P when triggered; all four must be specified and protected by sequencing/anchoring. Key absence alone is not a destruction proof. | R M07 |
| D11 | §6.3.4, domain retention tension and retention_exemption when retention overrides erasure, MUST | §§7.3, 10.2–10.3 | P. Rights/retention exist but no required exception record. Copyright/license disputes and preservation holds versus creator-data erasure/opt-out need explicit treatment. The profile must surface this tension even if a particular deployment never shreds. | R M07 |
| D12 | §1.6 non-guarantee; verbatim adoption SHOULD | C §1.3, Part III and §10.3; README later adopts disclaimer | P in released text; S for README adoption only. C's compliance-oriented wording cannot establish legal compliance. Do not silently replace frozen historical text with README corrections. | E M13; no independent legal determination |
| D13 | §4.5.2, registry/status ceiling, MUST NOT overstate | Released CAP v1.0; V registry same; README explicitly outstanding | S for current stated status. Released ≠ VAP v1.2-conformant; new documents must stay review drafts until adopted. | I; M13 |
| D14 | §4.5.3, optional capabilities; unknown capability IDs ignored gracefully, MUST | No capability declaration/processing rules | N for omitted capabilities (default empty); P for a verifier claiming V compatibility when it encounters unknown IDs. No requirement to implement DAP/SMP simply because they exist. | I non-use; R M06/M12 for verifier contract |
| D15 | §4.6.3, invoked capabilities declared with exactly one domain profile | No DAP/SMP invocation in C | N for baseline CAP alone; P if composition is claimed. Declare ID/version and apply stricter shared constraints without replacing Core. | R M09 if composed |
| D16 | §4.6.3, no framework event redefinition, ERASURE inherited, stricter constraints, no tier-name collision, independent versioning | No invoked capability contract | N for baseline; requirements apply on composition. Must not invent CAP_ERASURE as a substitute with weaker semantics. | R M09 if composed |
| D17 | §4.6.4, expected compositions SHOULD be stated | No statement | P recommendation. Minimal revision may explicitly expect no capability composition initially; illustrative future DAP/SMP use is not a present claim. | E M09 |
| D18 | §10.4, accept v1.1 data; ignore unknown newer constructs gracefully | C event enum closed; no VAP compatibility verifier rules | P/U. A legacy CAP schema validator is not necessarily a VAP verifier. Distinguish accepting data for legacy processing from validating it as new-conformant. Preserve unknown data for hashing; never silently grant conformance to unverified features. | F/R M06, M12 |

## 7. Evidence packaging, interoperability and governance

| ID | V clause / force | CAP evidence | Result and exact disposition | Route |
| --- | --- | --- | --- | --- |
| E01 | §9.3, Evidence Pack SHOULD, profile-defined container | §§2.3, 2.5, 15–17 | S for defining a portable bundle; P for full V offline content. CAP already requires structured packs at Silver/Gold and availability on legitimate request at all tiers. Do not turn V's SHOULD into an invented all-tier V MUST. | I format; R/E M11 for completeness |
| E02 | §9.3, events, paths, records/proofs, public keys, policy documents | §15.2 events/anchors/merkle/signatures | P. Most components exist; public-key material, verification policies, full signed records and explicit offline verification sufficiency are not specified. Keys must be authenticated against verifier trust policy, not trusted solely because producer included them. | R/E M11 |
| E03 | §11.3, SCITT optional, normative on claim | §§2.4, 9.4, 23 | N for Bronze/Silver deployments that do not use or claim SCITT; P at Gold because CAP requires SCITT-compatible service. A mandatory CAP feature can trigger an optional framework feature's MUSTs. | R M02, M11 |
| E04 | §11.3, RFC 9942 receipt; service identity/type; native verification independent of service | §9.5 AnchorType=SCITT/ServiceEndpoint; §23.2 receipts | P. Naming and endpoint map conceptually; exact receipt conformance and an offline V-native path are not established. Follow pinned V's RFC references rather than older CHANGE-001 draft names. | I mapping; R M11 |
| E05 | §8.1, VAP conformance layers; §8.2 matrix | C §2 Bronze/Silver/Gold | P. Orthogonal level systems; no rule establishes Bronze=Core, Silver=Standard, Gold=Full. Conditional MUSTs remain triggered at any level where their feature is used. | R M01, M06 |
| E06 | §§8.3, 10.1, test/audit/certification roles | §2.5 self-assessment/third-party audit; D.3 annual audit | P for certification eligibility. A CAP self-assessment is not a VAP test-suite pass or independent CAB-issued certificate. No certification conclusion follows from this paper review. | I scope; release gate |
| E07 | §10.4, outstanding mapping and independent versions | README and V §10.4 both outstanding | S for honest current disclosure; mapping still a draft. Even after publication, unresolved rows must remain visible; do not edit compatibility cell to Full. | E M13 |
| E08 | §10.3; CHANGE-001 §5 and B.1, governance/migration | CAP VERSIONING.md | P process action, not proof of technical conformance. Map changes to CAP change control and publish migration before adoption; no retroactive reclassification of CAP v1.0. | M13 |

## 8. High-level requirements and excluded material

V §2.4 provides a summary rather than eight independent implementation algorithms. Coverage is:

| V summary | Detailed mapping |
| --- | --- |
| HR-001 cryptographic integrity | I02–I10, I23–I29 |
| HR-002 decision lineage | P01–P04 |
| HR-003 causal tracing | P05–P10 |
| HR-004 accountability | P11–P12 |
| HR-005 explainability | P04; no claim that refusal records prove decision correctness |
| HR-006 privacy | D08–D12 |
| HR-007 completeness | I16–I18; CAP SRP supplementary |
| HR-008 independent verification | I01, I09–I15, E01–E04 |

V §§3.1–3.3 and §4.5.1 organize the assessed layers; they are not a waiver of them. V §5.2's CAP alignment notes are addressed in I07, D09–D11 and P09–P10. Other domain profiles in §§2/5 are not CAP requirements. §§9.1–9.2 integration patterns are recommendations, not a requirement to adopt a sidecar. Informative standards/regulatory tables, roadmap, glossary and history do not add CAP MUSTs. Appendix D is nevertheless material to interpretation: fold H-5 expressly limits INT-008 to post-anchor batch completeness, and H-3 says §4.4.4 introduces no new HALT requirement. The main specification prevails over older annex wording.

## 9. What can be resolved without changing CAP obligations?

| Existing material | Defensible interpretation-only conclusion | Boundary |
| --- | --- | --- |
| JCS, UUIDv7, SHA-256, Ed25519 | Appropriate canonicalization/ID/classical algorithm choices; event signatures exceed INT-005's SHOULD. | Does not cure EventHash self-inclusion or algorithm migration. |
| Mandatory PrevHash | Valid profile choice under INT-004a; retain it. | Chain input/verification details still need resolution; chain is not external anchoring. |
| §9.5 AnchorID/MerkleRoot/EventCount/FirstEventID/LastEventID | Direct semantic counterparts to several V §7.5 fields exist. | Cannot invent policy binding or issuer signature from absent fields. |
| Daily Silver/hourly Gold; TSA/SCITT/public blockchain classes | Existing frequency/classes are reusable. | Cannot weaken Gold's inherited TSA requirement or silently add Bronze MUST. |
| AttemptID and EventType | SRP causal link and action/outcome semantics exist. | ChainID is not automatically trace_id; risk is not confidence. |
| Per-user key destruction | Same broad crypto-shredding mechanism. | ERASURE, retention-exception rules and preservation of committed bytes remain missing. |
| Evidence Pack directory layout | Reuse a CAP-specific format; no common VAP container is required by v1.2. | Offline keys/policies/signed batch records still need specification. |
| No use of XREF/sequence-changing recovery/PQC/capabilities | Conditional non-applicability can be declared and evidenced. | Do not apply this to Gold's required SCITT or to actual crypto-shredding. |

A descriptive mechanism matrix may be published immediately, but it must describe Bronze anchoring as optional **in CAP v1.0**, and show the VAP conflict. It cannot make an existing MAY into a MUST by calling the change “mapping.”

## 10. Findings needing explicit review

### 10.1 Hashes and proof verification

C §8.2 removes Signature, then hashes every remaining field. C §8.3 adds EventHash after computing the hash; C §8.4 recomputes it with EventHash now present. This is a reproducibility defect, not merely a naming difference. Its correction needs fixed hash-input rules and test vectors. Existing records must never be silently rehashed and passed off as their original signed evidence.

C §3.3 cites RFC 6962, but §16.2's proof example omits domain separation and starts with EventHash rather than the prescribed leaf calculation. A generic “Merkle tree” claim is insufficient. The revised profile must specify leaf bytes and decoding, not concatenate textual hexadecimal strings by accident.

V's own Mechanism A abstract Header/Payload hash, §7.1 lower-case envelope, and Mechanism B `canonical(E)` need a concrete CAP binding. Batch-finalized security fields (root/index/anchor reference) must not enter the leaf they depend on. This review identifies the issue; it does not silently decide that flat CAP bytes and V envelopes are interchangeable. Proposed binding in M05/M06 remains subject to recorded review.

### 10.2 Two different completeness properties

SRP asks whether each recorded attempt has exactly one corresponding recorded outcome. V INT-008 asks whether an anchored batch is later presented with in-scope omissions. Dropping an attempt **and** its matching outcome can preserve SRP counts; changing unbound batch metadata can defeat a claimed scope. Both checks are needed where SRP applies.

C §13.1's equality for *any* timestamp window is also too broad: an attempt just before a boundary can finish just after it while obeying §12.3's 60-second bound. Group outcomes by AttemptID, define closed attempt cohorts, and carry pending references across batches. An inclusion proof for a selectively disclosed event is not a proof of the complete event set. Neither mechanism discovers an event that was never measured or implied by another retained record.

### 10.3 Data-model and tier interpretation

An open JSON object permits extra fields but is not a normative promise to produce them. Likewise, re-serializing CAP into a VAP-shaped report cannot retroactively bind missing policy metadata to old events. V §10.4's legacy data acceptance is different from entitlement to make new v1.2 conformance claims. No CAP v1.1 conformance is inferred merely from the older normative reference.

The profile must choose and publish a wire binding, numeric lexical form, timestamp unit, event-code assignment, signed-field set and batch attachment rules. Because V §7.1 and §8.1 leave tension between an all-event structure and layered conformance, any claimed Core-level relaxation needs an explicit framework interpretation, not an assumption in this mapping.

### 10.4 Migration timing and version discipline

CHANGE-001 §5 uses P+3 months for mechanism matrices/policy and P+6 months for anchoring/continuity; ERASURE/RECOVERY rules apply on first use. If P is the recorded 2026-09-28 publication, those dates would be 2026-12-28 and 2027-03-28. V §10.4 nonetheless expressly calls the CAP mapping due and outstanding. The documents do not justify inventing a single earlier numeric CAP deadline or treating a grace window as affirmative conformance. Record the deadline interpretation with maintainers.

CAP's own version policy, not VAP's version number, controls the CAP release number. Making anchorless Bronze implementations nonconformant and changing required RiskScore encoding are breaking under that policy. A CAP **2.0.0 candidate** is therefore the default recommendation if these changes replace the existing CAP requirements. A separately named, additive alignment extension could preserve legacy CAP tiers, but would need its own reviewed conformance scope; plain “CAP v1.0 is VAP v1.2 conformant” would remain false as a blanket statement.

## 11. Closure gates

1. Adopt a CAP version/scope decision through change control; retain released v1.0 bytes.
2. Approve the profile/VAP field and hashing bindings, including resolution of U rows; publish schemas and cryptographic vectors for that binding.
3. Close unconditional conflicts and incomplete profile obligations. Confirm conditional N/A claims against deployment behavior; enabling a feature reopens its rows.
4. Verify anchored batches, policy binding, continuity/failover, erasure preservation and any enabled recovery/XREF/SCITT path using positive and adversarial fixtures described in the proposal.
5. Publish the updated mapping with evidence references and remaining limitations. A reviewer must separately assess implementation evidence and each requested VAP level.
6. Update the compatibility matrix only after the recorded assessment supports the specific claim; certification additionally requires the applicable tests/audit/CAB process. This draft authorizes none of those status changes.

## Attribution and change notice

Derived from the CAP and VAP specifications by VeritasChain Standards Organization, linked and pinned in §2, licensed CC BY 4.0 International. This mapping and its assessments are new review material, not an official VSO decision. Proposed changes are identified as such. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
