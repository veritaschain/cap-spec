# Completeness Test Vectors

Test vectors for verifying the SRP Completeness Invariant.

## Overview

The SRP (Safe Refusal Provenance) attempt–outcome invariant of CAP v1.0 (§13) requires:

> **count(GEN_ATTEMPT) == count(GEN) + count(GEN_DENY) + count(GEN_ERROR)**

Every recorded generation attempt MUST have exactly one corresponding outcome. The check covers recorded events only: a request that was never recorded as GEN_ATTEMPT leaves nothing to detect. This profile-level invariant is distinct from the VAP v1.2 Completeness Invariant (INT-008).

In CAP v0.2, WARN, ESCALATE and QUARANTINE were separate outcome event types; in CAP v1.0 they are `ModelDecision` values on GEN_DENY. These vectors were updated on 2026-10-25 to the v1.0 outcome set. They are invariant-only fixtures: their hashes and some fields (for example `HashAlgo`) are placeholders or omitted.

## Verification Logic

```python
def verify_completeness(events: list[dict]) -> dict:
    """Verify the SRP Completeness Invariant."""
    
    attempts = {}  # AttemptID -> GEN_ATTEMPT event
    outcomes = {}  # AttemptID -> outcome event
    
    outcome_types = {'GEN', 'GEN_DENY', 'GEN_ERROR'}
    
    for event in events:
        event_type = event['EventType']
        
        if event_type == 'GEN_ATTEMPT':
            attempt_id = event['EventID']
            if attempt_id in attempts:
                return {'valid': False, 'error': f'Duplicate GEN_ATTEMPT: {attempt_id}'}
            attempts[attempt_id] = event
            
        elif event_type in outcome_types:
            attempt_id = event.get('AttemptID')
            if not attempt_id:
                return {'valid': False, 'error': f'Missing AttemptID in {event_type}'}
            if attempt_id in outcomes:
                return {'valid': False, 'error': f'Multiple outcomes for: {attempt_id}'}
            outcomes[attempt_id] = event
    
    # Check completeness
    attempt_ids = set(attempts.keys())
    outcome_ids = set(outcomes.keys())
    
    missing_outcomes = attempt_ids - outcome_ids
    orphan_outcomes = outcome_ids - attempt_ids
    
    if missing_outcomes:
        return {
            'valid': False,
            'error': 'Missing outcomes for attempts',
            'missingOutcomes': list(missing_outcomes)
        }
    
    if orphan_outcomes:
        return {
            'valid': False,
            'error': 'Outcomes without attempts',
            'orphanOutcomes': list(orphan_outcomes)
        }
    
    return {
        'valid': True,
        'attemptCount': len(attempts),
        'outcomeBreakdown': {
            'GEN': sum(1 for e in outcomes.values() if e['EventType'] == 'GEN'),
            'GEN_DENY': sum(1 for e in outcomes.values() if e['EventType'] == 'GEN_DENY'),
            'GEN_ERROR': sum(1 for e in outcomes.values() if e['EventType'] == 'GEN_ERROR')
        }
    }
```

## Test Cases

### test-001-valid-chain.json

Valid chain with matching attempts and outcomes.

### test-002-missing-outcome.json

Invalid chain - GEN_ATTEMPT without corresponding outcome.

### test-003-orphan-outcome.json

Invalid chain - GEN_DENY without corresponding GEN_ATTEMPT.

### test-004-duplicate-outcome.json

Invalid chain - Multiple outcomes for same AttemptID.

### test-005-gen-error-outcome.json

Valid chain - one attempt ends in GEN_ERROR, which counts as an outcome.

## Detection Scenarios

| Scenario | Detection | Error |
|----------|-----------|-------|
| Normal operation | ✓ Valid | None |
| Omitted outcome of a recorded attempt | Missing outcome | Attempt has no outcome |
| Fabricated refusal | Orphan outcome | Outcome has no attempt |
| Double-logging | Duplicate outcome | Multiple outcomes per attempt |
| Log tampering | Chain break | Hash verification fails |

## References

- [CAP Specification v1.0 §13](../../docs/CAP-Specification-v1.0.md#13-completeness-invariant) - Completeness Invariant
