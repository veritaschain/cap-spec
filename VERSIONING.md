# Versioning Policy

## Overview

CAP follows [Semantic Versioning 2.0.0](https://semver.org/) (SemVer) with domain-specific adaptations for specification documents.

## Version Format

```
MAJOR.MINOR.PATCH
```

| Component | Increment When |
|-----------|----------------|
| **MAJOR** | Breaking changes to normative requirements |
| **MINOR** | Backward-compatible additions or clarifications |
| **PATCH** | Editorial fixes, typos, non-normative updates |

---

## Breaking Changes (MAJOR)

A **breaking change** modifies the specification in a way that makes previously conformant implementations non-conformant.

### Examples of Breaking Changes

| Change | Impact |
|--------|--------|
| Removing a REQUIRED field | Existing events become invalid |
| Changing field semantics | Interpretation changes |
| Removing an event type | Existing chains may reference removed types |
| Changing hash algorithm defaults | Hash verification fails |
| Modifying the Completeness Invariant | SRP verification logic changes |

### Breaking Change Process

1. **Proposal**: Open issue with `breaking-change` label
2. **Review Period**: Minimum 30 days
3. **Migration Guide**: Required before merge
4. **Deprecation**: Previous version supported for 12 months minimum
5. **Announcement**: Published to veritaschain.org and mailing lists

---

## Backward-Compatible Changes (MINOR)

A **minor change** adds new capabilities without invalidating existing implementations.

### Examples of Minor Changes

| Change | Impact |
|--------|--------|
| Adding OPTIONAL fields | Existing events remain valid |
| Adding new event types | Existing processing continues |
| Adding new enum values | Unknown values handled gracefully |
| Clarifying ambiguous requirements | Intent unchanged |
| Adding new schemas | Existing schemas unaffected |

### Minor Change Process

1. **Proposal**: Open issue or pull request
2. **Review Period**: Minimum 14 days
3. **Documentation**: Update CHANGELOG and affected sections
4. **Merge**: After consensus

---

## Editorial Changes (PATCH)

An **editorial change** corrects errors or improves clarity without changing meaning.

### Examples of Editorial Changes

| Change | Impact |
|--------|--------|
| Fixing typos | No semantic change |
| Correcting grammar | No semantic change |
| Reformatting tables | No semantic change |
| Updating links | No semantic change |
| Adding examples | Clarification only |

### Editorial Change Process

1. **Pull Request**: Direct submission
2. **Review**: Single maintainer approval sufficient
3. **Merge**: Immediate upon approval

---

## Pre-Release Versions

Before v1.0.0, the specification is considered unstable:

```
0.MINOR.PATCH
```

- **MINOR** increments may include breaking changes
- Implementations should expect instability
- Feedback is especially valuable during this phase

### Current Status

CAP is currently at **v0.2.0** (pre-release).

---

## Version Compatibility Matrix

| Producer Version | Consumer Version | Compatibility |
|------------------|------------------|---------------|
| 0.2.x | 0.2.x | ✓ Full |
| 0.2.x | 0.1.x | ✗ Not guaranteed |
| 1.0.x | 1.0.x | ✓ Full |
| 1.1.x | 1.0.x | ✓ Backward compatible |
| 2.0.x | 1.x.x | ✗ Migration required |

---

## Schema Versioning

JSON schemas include version identifiers:

```json
{
  "$id": "https://veritaschain.org/schemas/cap/v0.2/core-event.json",
  ...
}
```

Schema versions align with specification versions.

---

## Deprecation Policy

### Deprecation Process

1. **Announce**: Feature marked as DEPRECATED in specification
2. **Document**: Migration path provided
3. **Support**: Feature remains functional for deprecation period
4. **Remove**: Feature removed in next MAJOR version

### Deprecation Periods

| Change Type | Minimum Deprecation Period |
|-------------|---------------------------|
| Event types | 12 months |
| Required fields | 12 months |
| Algorithms | 24 months |
| Major features | 24 months |

---

## Version History

See [CHANGELOG.md](docs/CHANGELOG.md) for detailed version history.

| Version | Date | Status |
|---------|------|--------|
| 0.2.0 | 2026-01-10 | Current |
| 0.1.0 | 2025-12-27 | Deprecated |

---

## Implementation Guidance

### Version Detection

Implementations SHOULD:
- Check `capVersion` in Evidence Pack manifests
- Support graceful handling of unknown versions
- Log warnings for version mismatches

### Forward Compatibility

Implementations SHOULD:
- Ignore unknown fields (preserve but don't process)
- Ignore unknown event types (log warning)
- Ignore unknown enum values (use default handling)

### Backward Compatibility

Implementations SHOULD:
- Support previous MINOR versions within the same MAJOR
- Provide migration tools for MAJOR version upgrades
- Document minimum supported version

---

## Contact

Questions about versioning policy: standards@veritaschain.org

---

*Last updated: 2026-01-13*
