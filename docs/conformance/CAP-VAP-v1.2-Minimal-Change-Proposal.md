# CAP alignment with VAP v1.2 Draft 3 — minimal change proposal

**Status:** Unadopted proposal for review. No conformance or certification claim.  
**Prepared:** 2026-10-08 JST; baseline as of 2026-10-07 JST.  
**Suggested path:** `docs/conformance/CAP-VAP-v1.2-Minimal-Change-Proposal.md`  
**Sources and findings:** [Pinned clause-by-clause mapping](CAP-v1.0-VAP-v1.2-Draft3-Conformance-Mapping.md).

Normative keywords in the proposed passages below describe **proposed future obligations only**. They do not amend CAP v1.0 or create an approved VSO decision. M01–M13 are local review identifiers, not allocated VSO change numbers.

## A. Adoption and release boundary

Publish the descriptive mapping independently of this proposal. Preserve `docs/CAP-Specification-v1.0.md`, tag `v1.0`, existing event bytes, and historical proofs unchanged.

The default adoption route is a new **CAP 2.0.0 candidate**, because anchoring at Bronze and numeric-string encoding would invalidate implementations conforming to CAP v1.0. CAP VERSIONING.md defines that as a MAJOR change. The final version number is a maintainer decision; do not label these changes a patch or a backward-compatible CAP 1.1 by assumption. The alternative is a separately identified opt-in alignment extension with its own scope, not a blanket v1.0 conformance declaration.

The new profile would target the exact VAP Draft 3 digest in the mapping. Before publication for conformance use, reviewers must approve the concrete serialization bindings in M05–M06 and resolve the mapping's U rows. Draft targets and example policy values are not evidence of achieved conformance. No new formal document ID is assigned here.

| Package | Changes | Why it is necessary |
| --- | --- | --- |
| Unconditional integrity / declaration baseline | M01–M06, relevant parts of M11–M13 | All-tier anchoring, signed scoped batches, continuity, reproducible verification, explicit version/policy and data rules. |
| Existing privacy capability | M07 | CAP already supports shredding; perform it only with VAP ERASURE evidence and retention handling. |
| Optional features | M08–M09 | Explicit non-use initially is the smallest option; full contracts required before enabling sequence recovery, XREF or capabilities. |
| Higher-layer evidence | M06, M10 | Define the records needed for Standard/Full assessment rather than inferring them from tier names. |

## M01 — All-tier mechanism and anchoring matrix

**Affected CAP clauses:** §§2.1–2.4, 4.2, 6.3, 9.3–9.4; Appendix D.1–D.3.  
**Class:** Normative breaking for Bronze; consolidation/clarification for inherited obligations.

Proposed replacement rules:

> All conformance tiers MUST compute event hashes, retain the per-event PrevHash chain, produce RFC 6962 Merkle batches, and externally anchor signed batch commitments. A deployment MUST NOT declare VAP conformance for an unanchored interval. Every tier MUST support full Merkle inclusion paths to the externally committed root, authenticated anchor proofs, and batch-scope verification. Selective proofs MUST NOT be represented as a full-batch completeness result.

| Proposed tier | PrevHash | Merkle + signed external anchor | Normal-operation maximum interval / event anchoring delay | Required target class | Detection / completeness limit |
| --- | --- | --- | --- | --- | --- |
| Bronze | MUST | MUST | 24 hours | RFC 3161 TSA, public transparency log, or delegated/aggregated public timestamp service with independently verifiable proof | Chain alteration checked whenever a verifier has adjacent records; independently committed completeness only at batch closure/anchor, normally within 24 h. |
| Silver | MUST | MUST | 24 hours | RFC 3161 TSA | Same batch limit, with SRP required. |
| Gold | MUST | MUST | 1 hour | RFC 3161 TSA **and** SCITT transparency service; preserve cumulative CAP §2.4 requirements | Same property with a normally ≤1 h external commitment window; HSM and audit API retained. |

> The interval is an upper bound from first unanchored event to verifiable external commitment in normal operation, not merely a once-per-calendar-day schedule. A batch MUST NOT mix verification policies or CAP tiers. Each event's policy MUST declare the matrix row in force. Failure to meet a deadline MUST be reported; later anchoring MUST NOT be reported as timely anchoring. Continuity procedures do not waive the normal deadline. Evidence presented to authorities MUST disclose batch windows, actual anchor times, outages, delays and the limitation that events never recorded or implied by other retained records cannot be detected.

Bronze's 24-hour value and proposed target subset are **new profile choices**, not requirements inferred from VAP. Gold's “and” preserves its inherited TSA requirement; changing that to “or” would be a separate relaxation requiring review. Local hash chaining is not promised to discover producer-wide re-signing before an independently held commitment exists.

## M02 — Signed AnchorRecord and cryptographic binding

**Affected CAP clauses:** §§9.2, 9.5, 15, 17.  
**Class:** Normative addition; schema change.

> Each batch closure MUST create a signed AnchorRecord that binds the root, count, ordered first and last event IDs, verification policy ID, and declared scope. Implementations MUST retain an authenticated mapping from each event's batch attachment to that AnchorRecord. A pack signature or a TSA token over an unbound bare root MUST NOT substitute for the signed batch commitment.

Use V §7.5's structure for new records, with these profile refinements:

| Field | Proposed rule |
| --- | --- |
| anchor_record_id | UUIDv7, unique per target receipt record. |
| batch.merkle_root | SHA-256 root under M05. |
| batch.event_count | Non-negative decimal integer **string**; nonempty batches required for this initial binding. |
| batch.first_event_id / last_event_id | Exact endpoint IDs in the committed sequence. |
| batch.policy_id | Same reverse-domain verification policy as every event in that batch. |
| batch.scope | Signed profile extension: ChainID, batch ID, sequence start/end, scope policy URI and digest, closure time, and ordered event-ID manifest digest. Integer values are strings. |
| anchor_target.type / identifier | Accepted target class and unambiguous service identity, including verifiable key/certificate identity where applicable. Endpoint alone is insufficient authentication. |
| anchor_target.proof | Verifiable target-specific proof of the exact signed commitment below; include necessary certificates/receipts/inclusion or transaction evidence for the selected target. |
| security.signature / sign_algo / signer_id | Producer signature and authenticated key identity; Ed25519 baseline. Gold signing uses its required HSM. |
| timestamp_int | UTC Unix microseconds as decimal integer string, profile-defined. |

**Proposed signed/external target binding (requires recorded acceptance):**

1. Let `B` be the AnchorRecord excluding `anchor_target.proof` and `security.signature` (and excluding an optional secondary `pqc_signature`), retaining all other fields including signer ID, algorithm and batch scope.
2. Produce `security.signature = Ed25519(SHA256(UTF8(JCS(B))))`. Signature bytes use an explicit Base64 encoding in the wire schema.
3. Let `S` be the resulting record excluding only `anchor_target.proof`; submit `SHA256(UTF8(JCS(S)))` as the external commitment or register `S` as a signed statement whose receipt authenticates those exact bytes. The target adapter MUST specify which operation is used and how its proof is verified.
4. Add the target proof without modifying `B` or `S`. Verification MUST reproduce `B` and `S`, verify the producer signature, and verify that the external proof binds `S`. This prevents the target proof from being self-referential while binding the producer signature and batch metadata externally.

For Gold, issue target-specific records for the same batch ID/root/scope; verify both the required TSA and SCITT records. An optional additional target never substitutes for a required target. No arbitrary assertion that a service is “SCITT-compatible” closes the M11 verification requirements.

## M03 — Separate batch completeness from SRP outcome completeness

**Affected CAP clauses:** §§5.1, 9, 13, 15.3, 17.  
**Class:** Normative clarification/addition; SRP window correction is breaking under CAP's policy.

> Batch completeness MUST be evaluated over the complete ordered event-ID manifest committed by M02, with each unique member included exactly once. Batches in this initial binding MUST contain a contiguous portion of one chain under one verification policy. A policy change MUST close the current batch. All in-scope event classes, including INGEST, TRAIN, GEN, EXPORT, SRP and applicable operational/ERASURE/RECOVERY events, MUST be eligible for batching without selective filtering.
>
> Full-batch verification MUST compare actual count, first/last identifiers, policy, unique membership and ordered scope to the signed record, recompute the Merkle root, and verify the external commitment. Event-subset disclosures MUST be marked PARTIAL_DISCLOSURE; the verifier MUST NOT report full-batch completeness solely from their inclusion proofs. Evidence of inconsistent externally committed scope/root presentations MUST be surfaced, not silently reconciled away.
>
> Where SRP applies, every recorded GEN_ATTEMPT MUST have exactly one linked terminal outcome after its permitted outcome interval. Outcomes MUST be matched by AttemptID, not by equality of aggregate counts alone. Unfinished attempts at a batch boundary MUST be carried forward with references to their anchored attempt records; a report covering an open cohort MUST report PENDING separately. An elapsed 60-second limit remains a CAP timing failure and MUST NOT be hidden as indefinitely pending. Anchored later outcomes remain later outcomes and MUST NOT be inserted into a closed batch.

Replace the “any timestamp window” equality with a **closed attempt cohort** check: select attempts by attempt time, then include their corresponding outcomes even when outcome timestamps lie outside the selection window. Include duplicate/orphan detection. Independent batch verification and SRP verification have separate report fields.

The batch scope/manifest binding proposed here is a CAP implementation choice for making VAP's declared scope concrete. It does **not** reinterpret VAP H-5 as requiring an advance commitment to all events that will ever occur, and it does not prove absence of pre-measurement drops or prevent all collusion.

## M04 — Anchor continuity and operational errors

**Affected CAP clauses:** §§6.1, 9, 10.1, 17.3; Appendix A.1.  
**Class:** Normative addition.

> Every deployment MUST publish and version an anchor continuity plan naming at least one acceptable fallback for each required target class. The plan MUST define failure detection, queue persistence, retry and operator escalation, and a migration procedure with a maximum window of 30 days. This migration limit MUST NOT be interpreted as an anchor-interval waiver.
>
> Failed submissions MUST be retained in a durable queue and retried without dropping or rewriting the original batch. If the gap since the last successful required anchor exceeds twice the tier interval, an ANCHOR_ERROR event MUST be appended immediately when the condition is detected, with last-success time, failed batch IDs, required target class, failure reason, observed gap and responsible operator. Bronze/Silver thresholds are >48 h; Gold is >2 h. The first missed interval is already a timeliness failure; the error-event threshold is not a grace period. Errors and eventual resolution MUST themselves be included in subsequent anchored batches.
>
> Local AnchorRecords, scope manifests, keys/certificates and verification proofs sufficient for historical verification MUST be retained for the entire supported evidence-verification period, at least as long as any retained event or Evidence Pack relying on them. Minimum anchor retention is Bronze six months, Silver five years, Gold ten years. Longer event/pack retention extends dependent proof retention. A later dependency MUST NOT be left unverifiable because a nominal minimum elapsed. Relevant evidence-preservation holds MUST be honored as recorded under M07.

Define `ANCHOR_ERROR` as an operational event with error class, not GEN_ERROR. GEN_ERROR remains an SRP terminal outcome linked to an attempt. Do not create a fictitious generation attempt to make anchor errors fit the old event enum. Fallback tests must show verification of historical anchors while the primary endpoint is unavailable, using retained evidence and independently configured trust material.

## M05 — Deterministic event hashes and Merkle proofs

**Affected CAP clauses:** §§7.1, 8.2–8.4, 9.2, 16.2; Appendix A.  
**Class:** Correctness repair plus normative serialization binding; no silent retrofit to old evidence.

For the existing flat CAP format, the minimal correction to §8.2's example is to exclude **both** EventHash and Signature from the hash input. That is a proposed repair, not evidence that historical implementations already used it. A verifier must select an explicitly identified legacy hash recipe and preserve the recorded original bytes.

For new-envelope events in M06, the following binding is proposed to instantiate V §4.1.3 Mechanism A without self-inclusion:

> Define `Header` as all top-level event fields other than `provenance`, `accountability`, `domain_payload` and `security`, plus a `security_context` object containing the immutable algorithm and signer-identification fields of `security`. Define `Payload` as the object containing `provenance`, `accountability` and `domain_payload`. No unknown extension field may be discarded from these committed inputs merely because the verifier does not understand its semantics.
>
> The event hash MUST be SHA256 over `UTF8(JCS(Header)) || UTF8(JCS(Payload)) || DecodePrevHash(prev_hash)`. Here `||` is byte concatenation, not hexadecimal-text concatenation. PrevHash decodes to 32 bytes; the genesis value is 32 zero bytes. This is the proposed concrete binding of V's abstract Header/Payload/GENESIS_HASH. `event_hash`, `signature`, optional secondary signature and batch-finalized attachment fields MUST NOT occur inside Header or Payload. Ed25519 MUST sign the 32 event-hash bytes. Each subsequent event MUST commit the previous event's recorded hash.

`security_context` includes `hash_algo`, `sign_algo`, `signer_id` and, if hybrid is later enabled, `pqc_sign_algo`; all other security extensions require an explicit signed-field disposition. Reject an unsupported algorithm for a claimed new-format PASS; do not reinterpret it as the default. Verify UUIDv7 format/uniqueness and exact genesis/continuity rules, including out-of-order presentation. The signed verification policy identifies this binding version.

> The committed Merkle leaf event `E` MUST be the immutable signed event, including its event hash and event signature, excluding only the batch-finalized `security.merkle_root`, `security.merkle_index` and `security.anchor_reference` attachments. Those attachments are supplied with the proof and authenticated by matching the signed AnchorRecord and inclusion path. An attachment MUST NOT change the originally hashed/signed event.
>
> Compute `Leaf(E) = SHA256(0x00 || UTF8(JCS(E)))` and `Node(L,R) = SHA256(0x01 || L || R)` using raw 32-byte child hashes. Use RFC 6962 tree construction, ordering and audit-path rules, including non-power-of-two tree sizes; do not duplicate odd leaves as an undocumented alternative. Proofs MUST include tree size and leaf index, and reject impossible indices, missing/surplus path elements and incorrect direction. Empty heartbeat batches are outside this initial binding, not represented by fabricated endpoint IDs.
>
> Verification MUST recompute event hashes and chain continuity, verify event and AnchorRecord signatures, validate inclusion/root and external proof, and check M03 completeness for a full-batch claim. A failure in either sequence mechanism MUST result in verification failure; unavailable required evidence MUST be reported as INDETERMINATE, never PASS.

This binding requires review against V's abstract algorithms and §7.1. It is not asserted to be byte-equivalent to released CAP 1.0 or to an existing VAP implementation. Once adopted, publish vectors with exact canonical bytes, hash preimages, hashes, signatures, root, proof and target commitment. Do not mark I04/I23/I26 closed merely because this proposal exists.

Keep SHA-256/Ed25519 mandatory initially. Remove misleading unsupported alternate-algorithm choices from the new baseline schema until their complete hash/signature encoding is defined. A versioned signed policy and separately identified schema MUST permit future approved-algorithm migration without rewriting past events; retain historical verifiers and key identifiers. This is crypto agility, not a claim that optional PQC is required now.

## M06 — Version, verification policy, wire model and numeric encoding

**Affected CAP clauses:** §§3.3, 7, 14, 15.3; Appendix A.  
**Class:** Normative breaking; framework/profile binding decision required.

Proposed route: use the V §7.1 common envelope for newly generated events in the revised profile. Existing CAP domain fields are retained in `domain_payload` after moving common fields into their mapped envelope positions. Do not maintain two unsynchronized copies of EventID/EventHash/Signature.

| CAP v1.0 concept | Proposed new location / constraint |
| --- | --- |
| EventID | header.event_id; UUIDv7. |
| ChainID | domain_payload.ChainID; cryptographic chain identity, distinct from trace. |
| SessionID | Domain/session context; use as trace_id only when its scope is demonstrably the whole intended trace. Otherwise allocate a stable workflow UUIDv7. |
| Timestamp | header.timestamp_iso plus timestamp_int as UTC Unix microseconds string; declare timestamp_precision. Both represent the same recorded time. Microsecond storage does not claim microsecond clock accuracy. |
| EventType | header.event_type; maintain existing domain vocabulary plus approved framework/operational additions. |
| PrevHash / EventHash / HashAlgo / Signature / SignAlgo | Corresponding security members, using the approved M05 serialization and explicit encoding. |
| Context / ModelContext / Rights | Mapped into provenance and accountability as described below; retain remaining domain-specific fields in domain_payload. |
| PromptHash / input assets / AttemptID | Provenance input commitments and causal references; keep auditable domain-specific identifiers. |
| PolicyID / PolicyVersion for content safety | domain_payload.ContentPolicyID / ContentPolicyVersion; not the VAP verification policy. |
| AnchorID and proofs | security.anchor_reference plus batch attachments resolved to the signed M02 record. |

> Newly produced events MUST declare `vap_version`, `profile.id`, `profile.version` and the full §7.1 verification policy, including reverse-domain `policy_id`, profile tier, separately assessed VAP level, registration issuer and `verification_depth`. For this binding, mechanisms are PREV_HASH, MERKLE and EXTERNAL_ANCHOR; both required-proof booleans MUST be true. A policy MUST be immutable under its identifier or content-digest-bound; changing verification semantics MUST create a new version/identifier and close the old batch. Policy documents MUST be available with the evidence.
>
> The profile descriptor MUST declare its profile ID/version, `min_vap_version`, mechanism matrix, target/interval policy, recovery support/bounds and invoked capabilities. Draft descriptors identify these as targets, not achieved conformance. Events MUST NOT claim a VAP level merely because their CAP tier has the same ordinal position.

For an eventual approved target, `vap_version` uses V's `1.2` convention, while the descriptor states minimum version `1.2.0` and pins the reviewed Draft 3 digest in the assessment. No concrete conformance-bearing sample event is issued by this proposal. A producer claiming a level needs a corresponding supported assessment; during development, test fixtures must be plainly marked as synthetic candidate-format data outside production claims.

> All numeric wire values MUST be JSON strings, including RiskScore, asset sizes, batch counts, sequence positions, timestamps and event codes. Booleans remain JSON booleans. Integer strings use canonical base-10 notation without leading plus signs or unnecessary leading zeros. RiskScore strings MUST represent a finite value in [0,1]; a semantic range check is required in addition to a string schema. No preexisting signed event may be transformed in place to satisfy this rule.

Proposed profile-local uint8 event-code assignments, represented on wire as strings, are: INGEST `1`, TRAIN `2`, GEN `3`, GEN_ATTEMPT `4`, GEN_DENY `5`, GEN_ERROR `6`, EXPORT `7`, ERASURE `128`, ANCHOR_ERROR `129`, RETENTION_DECISION `130`. These numbers are candidate CAP assignments, **not framework-reserved code points**. Maintainers must check collision/registration policy before adoption. Optional RECOVERY/XREF extensions must allocate and document their own approved codes before use, not borrow GEN_ERROR.

Provenance rules:

- Each event MUST identify the acting model/human/system, relevant input commitments, execution context, recorded action and observed outcome. Where the V abstract model requests unavailable information, the profile must define a truthful absence/unknown representation; no invented model hash, explanation, confidence, approval or operator is permitted.
- Model events MUST identify model ID/version and, where available, parameter/artifact hash. Unknown hash and why it is unavailable must be disclosed for assessment; this is not automatically deemed equivalent to a populated V field.
- `trace_id` MUST group the workflow across its relevant events. Add explicit causal parent IDs for non-SRP lineage; AttemptID remains authoritative for SRP causality. Chain ordering is not a substitute for causal parents.
- VAP-Standard/Full assessment must evaluate this concrete provenance/trace mapping, not merely the presence of empty objects. The interpretation of unavailable fields and any claimed Core-level relaxation of the common envelope remain release-review decisions.

Legacy handling:

> Preserve CAP 1.0 events and proofs byte-for-byte. A VAP-compatible verifier MUST accept legacy data for its applicable legacy verification path; acceptance does not establish new v1.2 conformance. Report data validity, cryptographic verification and conformance separately. Unknown optional fields/capabilities MUST be preserved for canonicalization and ignored gracefully at the semantic layer when required by V §10.4. A verifier MUST NOT report verification of an unknown capability's guarantees. Unknown mandatory verification algorithms cannot yield PASS.

No assumed CAP v1.1 conformance or undocumented legacy algorithm is created by this migration rule. At cutover, close and retain the final old batch, start the new chain, and publish a signed migration record referencing both histories and the actual cutover/anchor time. A new anchor can attest evidence present now; it cannot prove old evidence was externally anchored earlier.

## M07 — ERASURE and retention decisions

**Affected CAP clauses:** §§6.1, 10.3, 14, 17; Appendix A and Gold checklist.  
**Class:** Conditional normative addition plus mandatory profile privacy clarification.

> When protected plaintext is rendered irrecoverable by per-subject DEK destruction, the implementation MUST append the framework ERASURE event, fully sequenced and anchored. The event MUST contain target event IDs, an allowed erasure reason, independently assessable destruction evidence or an authenticated reference to it, and the authorizing operator. The reason vocabulary is SUBJECT_REQUEST, RETENTION_EXPIRED or LEGAL_ORDER unless a reviewed profile extension adds one.
>
> Erasure MUST NOT delete, rewrite or rehash prior committed event bytes. Prior event hashes, Merkle paths and anchors MUST remain verifiable. Encryption must therefore commit stable ciphertext or stable references before shredding; deletion of a DEK must not mutate the canonical committed record. Key-destruction proof MUST account for managed backup/replica copies under the key lifecycle policy; do not claim destruction merely because a key lookup fails.
>
> The profile MUST document the tension between creator-data erasure/opt-out and copyright/licensing disputes, preservation holds and applicable retention duties. If a retention duty overrides an erasure request, a RETENTION_DECISION event MUST record `retention_exemption`, identified decision-maker, affected records, stated basis, scope and review/expiry information. Partial erasure uses ERASURE with the retained scope and exemption recorded. A wholly denied erasure request MUST NOT falsely assert that shredding occurred.

The retention-decision event is a proposed CAP extension to surface V's required field in a non-erasure situation; it does not redefine ERASURE. Crypto-shredding may support erasure duties but is not itself a legal-compliance determination. Conditional N/A is acceptable only for a deployment that performs no shredding; it does not erase CAP Gold's own support requirement or the profile's obligation to state retention tensions.

## M08 — Smallest honest RECOVERY contract

**Affected CAP clauses:** new recovery subsection; profile descriptor.  
**Class:** Optional extension or explicit non-support.

The smallest initial revision does **not** add sequence-altering recovery:

> This revision does not authorize SKIP, REBUILD, MERGE, CHECKPOINT or equivalent operations that alter the effective committed sequence. Deployments under this non-recovery scope MUST preserve gaps and original evidence and MUST NOT conceal them by renumbering, rehashing or filtering. Byte-identical backup restoration and retry of an already identified external submission are not sequence-altering recovery. New workflow attempts are new events and do not replace failed attempts.

This is a non-use boundary, not an assertion that arbitrary recovery is permitted with a zero bound. An Emergency Override cannot be used to enable an unreviewed extension.

If operations that alter the sequence are required, approval of the following contract is mandatory **before use**:

| Operation | Quantitative limits the extension must specify separately for Bronze/Silver/Gold | Required evidence |
| --- | --- | --- |
| SKIP | Maximum skipped events and elapsed gap duration | Original IDs/range, reason, before/after break references; never erase the gap. |
| REBUILD | Maximum event count and time horizon | Source snapshot/hash, validation results, original and reconstructed references. |
| MERGE | Maximum number of branches/events and divergence age | All branch roots, deterministic ordering/conflict rules and provenance. |
| CHECKPOINT | Maximum covered interval/event count | Prior root/break reference, checkpoint commitment and validation evidence. |

Every supported operation MUST be an anchored/chained RECOVERY event with break point, scope, validation evidence and operator. Beyond-limit operations MUST require explicit recorded approval by an identified human, flagged Emergency Override in the conformance report; recovery events MUST never be filtered from batches. The table deliberately does not invent operationally unvalidated limits: support remains disabled until numeric limits, schema and tests are adopted.

## M09 — XREF and capability non-use / enablement

**Affected CAP clauses:** §§3, 22–24; profile descriptor.  
**Class:** Interpretation-only non-use initially; conditional normative extension if enabled.

> This initial revision does not claim XREF conformance from C2PA references, cloud-log pointers or CAP event IDs alone. No cross-cutting capability is invoked by default (`capabilities = []`). CAP continues to be the single domain profile. Possible later creator↔platform XREF or DAP/SMP compositions are future extensions, not present functionality.

Before enabling XREF, define shared UUID v4/v7, shared event key, explicit matching tolerance, independently anchored records at each party, INITIATOR/COUNTERPARTY/OBSERVER roles, PENDING/MATCHED/DISCREPANCY/TIMEOUT status, INFO/WARNING/CRITICAL severity and, for >2 parties, ordering/reference rules. Include timeout and missing-counterparty evidence. A single operator signing twice is not evidence of independent parties/anchors.

Before invoking DAP/SMP or another capability, declare ID/version, preserve all Shared Assurance Core requirements, apply the stricter overlapping constraints, retain framework ERASURE semantics, and avoid competing profile tier names. Verifiers must tolerate unknown capability IDs without claiming to verify them. No new capability implementation is needed merely to publish this mapping.

## M10 — Accountability and oversight evidence

**Affected CAP clauses:** §§7.4–7.5, 14.2, 18.2; V §4.4/§7.1 mapping.  
**Class:** Normative schema/coverage addition for the claimed scope.

> Events MUST identify the accountable operator using a stable identifier with an auditable authorized resolution mechanism; publishing personal identity is not required. Where an approval, delegation or override occurs, retain approver identity/time; delegator, delegatee, scope and validity interval; or original/replacement action, actor, reason and time, respectively. HumanOverride alone is insufficient. The absence of a human approval MUST NOT be replaced by a fabricated approver; its schema representation and effect on the requested VAP assessment must be explicit.

Define mappings from CREATOR/REVIEWER/ADMIN/SYSTEM and model provider/developer/data vendor to actual responsibilities. Distinguish the model acting on a request from the human or organization responsible for operation. Capture oversight actions that occurred; this profile does not add a runtime intervention system and does not invent a mandatory HALT event. VAP-Full remains unestablished until the complete accountability binding has been reviewed and demonstrated.

## M11 — Offline evidence and SCITT

**Affected CAP clauses:** §§15–17, 23.  
**Class:** Evidence recommendation completion; normative where CAP tier or SCITT claim requires it.

Retain the CAP directory layout; no new universal VAP container is proposed. Add verification-policy documents and their hashes, authenticated public keys/certificates/key history, signed AnchorRecords and scope manifests, all required target proofs, exact hash-binding identifier, event/chain boundaries and actual timing/continuity information. Preserve sufficient evidence for verification without the producing system or live transparency endpoint; externally configured trust policy remains necessary.

> Reports MUST separate event/hash/signature validity, chain validity, Merkle inclusion, batch completeness, SRP outcome completeness, timeliness, continuity, enabled conditional features, and requested conformance scope. Missing evidence is INDETERMINATE; detected contradiction is FAIL; non-triggered optional feature is NOT_APPLICABLE with an explicit basis. Overall PASS MUST NOT hide a failing required subcheck or a still-open cohort. Each report MUST identify the specification and policy versions and its disclosed evidence scope.

> When SCITT alignment is claimed (including this proposal's Gold tier), receipts MUST satisfy RFC 9942 as required by the pinned V §11.3; identify the RFC 9943 transparency service in `anchor_target` with type TRANSPARENCY_SERVICE, retain its verifiable receipt and identity, and retain the VAP-native verification path. SCITT MUST remain additive and MUST NOT replace VAP's event/sequence/batch checks.

V §9.3 makes Evidence Packs a SHOULD; this proposal strengthens practical packaging within CAP's already defined export duties. The exact new CAP obligation must be adopted explicitly, not retrospectively attributed to VAP.

## M12 — Schemas, vectors and acceptance evidence

**Affected CAP clauses:** Appendix A, Appendix B, Appendix D; schemas/examples maintained for the next version.  
**Class:** Schema and normative implementation alignment, not merely documentation.

Required companion implementation work before a claim:

- New versioned common-event and AnchorRecord schemas matching M01–M11; do not overwrite v1.0 schema IDs. Require PrevHash explicitly on new chain events and validate genesis specially. Validate UUID version, duplicate IDs, hash/signature encodings, allowed event-type codes, numeric lexical forms and semantic ranges.
- Add ERASURE, ANCHOR_ERROR and RETENTION_DECISION; optional RECOVERY/XREF schemas remain disabled until approved. Regenerate examples with valid UUIDv7 variant bits, real signatures and fixed keys labelled test-only; the abbreviated historical examples are not cryptographic vectors.
- Ensure policy/metadata, public keys and batch attachments are genuinely authenticated, not merely adjacent JSON. Vectors must cover the exact byte encoding proposed in M02/M05/M06.
- Separate parser compatibility from conformance checks. Preserve unknown signed content; tolerate unknown optional constructs as V requires; never report success for an unsupported required verifier.

| Test | Fixture / mutation | Required observation |
| --- | --- | --- |
| T01 Hash round trip | Populate hash/signature then verify same immutable event | Exact reproducibility; self-including hash algorithm rejected. |
| T02 Tree correctness | 1, 2, 3, 5 leaves; wrong prefixes/index/size/path length | Correct RFC 6962 roots and rejection of mutated proofs. |
| T03 Bronze anchor | Valid chain and Merkle tree with no external proof | New VAP claim not established; no anchorless PASS. |
| T04 Metadata binding | Change count, endpoints, policy, scope or signer after commitment | Signature/external binding or scope check fails. |
| T05 Balanced deletion | Remove attempt+outcome, preserving SRP aggregate equality | Anchored-batch verification fails despite matching counts. |
| T06 Selective disclosure | Supply one event and valid path from a larger batch | Inclusion may pass; whole-batch completeness not claimed. |
| T07 SRP boundary | Attempt before cutoff, outcome after cutoff but within 60 s | Matched by AttemptID; no false missing-event result from window arithmetic. |
| T08 Outage | Miss interval; exceed 2× interval; restore with fallback | Delay reported, ANCHOR_ERROR present, queue retained, historical proofs still verifiable; late submission not relabelled timely. |
| T09 Erasure | Destroy DEK; independently verify old hashes/proofs and new ERASURE | Prior integrity remains valid; targets/reason/proof/operator present. Retention-only decision does not assert erasure. |
| T10 Recovery | Prohibited sequence rewrite; or enabled operation beyond its adopted bound | Reject unsupported rewrite; enabled extension requires recorded human Emergency Override and flags it. |
| T11 XREF (if enabled) | Missing counterparty, mismatched key/tolerance, >2 parties | Correct timeout/discrepancy and independent anchors/order rules. |
| T12 SCITT / offline | Gold receipts invalid or omitted; primary endpoint inaccessible | Reject missing/invalid required receipts; validate retained native evidence without online dependency. |
| T13 Legacy / numeric | Original numeric RiskScore versus new string score; unknown optional field | Legacy path preserves bytes; new schema enforces string and range; no retroactive v1.2 PASS. |
| T14 Policy downgrade | Set required-proof Boolean false, change tier/policy mid-batch | Reject policy/matrix mismatch or mixed batch. |
| T15 Trace / operator | Multiple workflows on one ChainID; override with only Boolean | No false trace equivalence; missing attribution/approval is exposed. |

These are acceptance criteria, **not a claim that an implementation has passed these tests**. Document-level checks performed for the deliverable are listed separately in the package README.

## M13 — Publication language and migration

**Affected repository material:** README, conformance mapping, CHANGELOG, VERSIONING current-state text; future specification and compatibility matrix.  
**Class:** Editorial status update separated from normative adoption.

Safe statement after the draft mapping is actually merged:

> CAP v1.0 is a released profile. A draft mapping against VAP v1.2 Draft 3 is published for review and identifies unresolved normative divergences, including Bronze external anchoring and shared data-model, batch-verification and continuity requirements. CAP v1.0 conformance to VAP v1.2 has not been established. Publication of the mapping or the accompanying change proposal is not a conformance declaration or certification.

Keep the current honest statement until that publication occurs. The accompanying README update links the mapping and proposal at their committed review-document paths. Do not change VAP §10.4 to “Full”; a later descriptive cell could read “Draft mapping published; conformance not established” after actual publication and maintainer review.

Migration checklist:

1. Open the appropriate breaking-change review and hold the required review period (CAP policy: at least 30 days); obtain the applicable governance decision. Opening this proposal for review does not adopt its normative changes or start a release.
2. Publish the selected new-version/extension scope, approved wire/hash binding, schemas, policy examples and vectors; resolve open framework interpretations. Update stale VERSIONING current-state text separately.
3. Publish a migration guide before merge/adoption, including original-byte retention, old/new chain cutover, key/algorithm history, and anchoring time disclosure. CAP policy requires at least 12 months of previous-version support for a breaking change; feature-specific longer deprecation periods must also be checked.
4. Run and publish implementation evidence for the applicable tests and all enabled conditional features; assess each VAP level independently.
5. Update mapping dispositions and compatibility status only after substantiated closure. Any certification needs its separate VAP test/audit/CAB process. Grace windows and a Draft 3 reference do not create a certificate.

Adopt V §1.6's non-guarantee statement in the new specification (the current CAP README already contains it); remove or qualify blanket compliance claims in the new text. Preserve the released historical text rather than silently rewriting its claims. No legal review or present regulatory-compliance assertion is part of this proposal.

## Open decisions that prevent adoption as-is

| Decision | Proposed default | Why still reviewable / open |
| --- | --- | --- |
| Release vehicle | CAP 2.0 candidate; preserve v1.0 | CAP change control must approve scope and version. |
| V abstract model → concrete byte binding | New envelope with M05 Header/Payload and immutable leaf projection | V's abstract algorithms and batch-finalized fields do not independently prescribe this exact CAP binding. Requires recorded acceptance and vectors. |
| Numeric types / timestamps / codes | String wire values; microseconds; proposed CAP-local codes | No implicit numeric exemption; confirm assigned units/codes and migration impact. |
| Provenance unknowns / Core envelope | Truthful absence indicators, no fabricated records | Their admissibility and level-specific semantics must be approved before a conformance result. |
| Sequence-changing recovery | Disabled initially | Enable only with approved per-tier quantitative limits; no placeholder limits count as a finished feature. |
| Bronze service subset and 24 h interval | Table in M01 | Delegated profile choice with cost/availability implications. |
| Anchor signed-body/receipt binding | M02 pre-proof commitment | Confirm adapters and receipts bind the exact signed bytes, especially Gold dual targets. |

None of these open items changes the descriptive finding that CAP v1.0 conformance is currently unestablished. They are visible release gates rather than hidden assumptions in a “compliant” draft.

## Attribution

Derived from the pinned CAP/VAP specifications by VeritasChain Standards Organization under CC BY 4.0. This is new proposed text, not an official adopted revision. See the companion mapping for exact sources and digests. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
