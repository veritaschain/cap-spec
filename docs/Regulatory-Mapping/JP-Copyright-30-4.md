# CAP Alignment: Japan Copyright Act Article 30-4

## Overview

**Japan Copyright Act Article 30-4** (著作権法第30条の4) establishes a statutory exception allowing AI training on copyrighted works under certain conditions. This document explains how CAP provides evidentiary support for demonstrating compliance with Article 30-4 requirements.

---

## Article 30-4 Summary

### Legal Text (Translated)

> It is permissible to exploit a work, to the extent deemed necessary, in any of the following cases, or in other cases in which it is not a person's purpose to personally enjoy or cause another person to enjoy the thoughts or sentiments expressed in that work:
>
> (iii) Using a work in the course of information analysis (meaning the extraction, comparison, classification, or other statistical analysis of the elements of language, sounds, images, or other information constituting a large number of works or other such large volume of information...)

### Key Conditions

| Condition | Description | CAP Evidence |
|-----------|-------------|--------------|
| Non-enjoyment purpose | Not for experiencing the work itself | Purpose documentation |
| Information analysis | Statistical/analytical processing | TRAIN event context |
| Necessary extent | Only what's needed for analysis | AssetID scope |
| No undue prejudice | Does not harm rights holder interests | RightsBasis documentation |

---

## CAP Support for Article 30-4 Compliance

### INGEST Event Documentation

When ingesting copyrighted materials for AI training:

```json
{
  "EventType": "INGEST",
  "AssetID": "urn:cap:asset:studio:training-data-001",
  "AssetHash": "sha256:...",
  "AssetType": "IMAGE",
  "Rights": {
    "RightsBasis": "STATUTORY_EXCEPTION",
    "StatutoryBasis": {
      "jurisdiction": "JP",
      "article": "Copyright Act Article 30-4",
      "clause": "iii",
      "justification": "Information analysis for model training"
    },
    "ConsentBasis": "NOT_REQUIRED"
  },
  "Confidentiality": {
    "ConfidentialityLevel": "INTERNAL"
  }
}
```

### RightsBasis: STATUTORY_EXCEPTION

When claiming Article 30-4:

| Field | Value | Purpose |
|-------|-------|---------|
| RightsBasis | "STATUTORY_EXCEPTION" | Indicates statutory basis |
| StatutoryBasis.jurisdiction | "JP" | Japan law |
| StatutoryBasis.article | "Copyright Act Article 30-4" | Specific provision |
| StatutoryBasis.justification | Free text | Purpose documentation |

### TRAIN Event Documentation

Training activities should record:

```json
{
  "EventType": "TRAIN",
  "TrainingType": "PRETRAIN",
  "InputAssetIDs": ["urn:cap:asset:studio:training-data-001", "..."],
  "OutputModelID": "urn:cap:model:studio:image-gen-v1",
  "TrainingContext": {
    "purpose": "Information analysis for image generation model",
    "article30_4_compliance": {
      "non_enjoyment_purpose": true,
      "information_analysis": true,
      "necessary_extent": "Dataset limited to style features extraction",
      "no_undue_prejudice": "Training data not redistributed or exposed"
    }
  }
}
```

---

## Evidential Value

### What CAP Proves

| Question | CAP Evidence |
|----------|--------------|
| What materials were used? | AssetID, AssetHash in INGEST |
| When were they used? | Timestamp |
| What was the stated purpose? | StatutoryBasis.justification |
| What processing occurred? | TRAIN event details |
| Was output different from input? | OutputAssetHash ≠ InputAssetHash |

### What CAP Does NOT Prove

| Legal Question | Reason |
|----------------|--------|
| Is use actually "necessary extent"? | Legal determination |
| Does it cause "undue prejudice"? | Requires market analysis |
| Is it truly "information analysis"? | Purpose is subjective |

**CAP provides evidence; courts make legal determinations.**

---

## "Undue Prejudice" Considerations

Article 30-4 requires that use does not "unduly prejudice the interests of the copyright holder."

### CAP Fields Supporting Non-Prejudice Claims

| Field | Evidence Value |
|-------|---------------|
| ConfidentialityLevel | Shows materials protected from leakage |
| PermittedUse.Distribution: false | Training data not redistributed |
| OutputAssetHash | Generated content differs from training data |
| ModelContext.Environment: LOCAL | Model isolated from external access |

### Evidence Pack for Dispute Resolution

If a rights holder challenges Article 30-4 applicability:

```
evidence-pack/
├── manifest.json
├── events/
│   ├── ingest-events/          ← What was used
│   └── train-events/           ← How it was used
├── article30_4_documentation/
│   ├── purpose_statement.md    ← Non-enjoyment purpose
│   ├── necessity_scope.md      ← Necessary extent
│   └── no_prejudice_measures.md ← Safeguards
└── verification/
    └── instructions.md
```

---

## Opt-Out Compliance

The 2024 Agency for Cultural Affairs guidance addresses opt-out:

### Recording Opt-Out Status

```json
{
  "EventType": "INGEST",
  "AssetID": "urn:cap:asset:external:opt-out-001",
  "Rights": {
    "RightsBasis": "UNKNOWN",
    "ConsentBasis": "OPTED_OUT",
    "OptOutReference": {
      "source": "robots.txt",
      "detected": "2026-01-10T00:00:00Z",
      "action": "EXCLUDED_FROM_TRAINING"
    }
  }
}
```

### Opt-Out Event Types

| ConsentBasis | Action |
|--------------|--------|
| OPTED_OUT | Exclude from training |
| UNKNOWN | Apply precautionary measures |
| EXPLICIT_WRITTEN | Include with documentation |

---

## Industry-Specific Considerations

### Games Industry

| Concern | CAP Mitigation |
|---------|---------------|
| Character design leakage | ConfidentialityLevel: PRE_RELEASE |
| Style extraction | RightsBasis documentation |
| Unreleased content | Timestamp + classification |

### Publishing Industry

| Concern | CAP Mitigation |
|---------|---------------|
| Manuscript protection | ConfidentialityLevel tracking |
| Translation rights | PermittedUse documentation |
| Derivative works | RightsBasis chain |

### Film/Animation

| Concern | CAP Mitigation |
|---------|---------------|
| Actor likeness | ConsentBasis documentation |
| Voice cloning | AssetType: AUDIO tracking |
| Production committee rights | Multi-party RightsHolder |

---

## Recommendations

### For AI Developers

1. Use STATUTORY_EXCEPTION with full justification
2. Document non-enjoyment purpose explicitly
3. Record scope limitations (necessary extent)
4. Implement safeguards against distribution

### For Rights Holders

1. Review INGEST events for your assets
2. Verify ConsentBasis accuracy
3. Check for opt-out compliance
4. Request Evidence Packs for disputes

---

## Related Japanese Regulations

| Regulation | CAP Relevance |
|------------|---------------|
| Act on Protection of Personal Information | ActorHash anonymization |
| Unfair Competition Prevention Act | Trade secret classification |
| Act Against Unjustifiable Premiums | Marketing claim evidence |

---

## Disclaimer

This document provides technical capability mapping only. Article 30-4 interpretation requires legal analysis. The scope and limits of the statutory exception are subject to ongoing judicial and administrative clarification.

---

## References

- [Japan Copyright Act (English)](https://www.cric.or.jp/english/)
- [Agency for Cultural Affairs AI Guidelines](https://www.bunka.go.jp/)
- [CAP Specification](../CAP-Specification-v0.2.md)

---

*Last updated: 2026-01-13*
