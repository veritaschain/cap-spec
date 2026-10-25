#!/usr/bin/env python3
"""Run illustrative CAP hash vectors, not full CAP conformance checks."""

import hashlib
import json
from pathlib import Path

try:
    import rfc8785
except ImportError as exc:
    raise SystemExit("Install the test dependency: python -m pip install rfc8785") from exc


def canonical_event(event: dict) -> bytes:
    """Apply the draft exclusion rule, then return RFC 8785 UTF-8 bytes."""
    if not isinstance(event, dict):
        raise TypeError("event must be a JSON object")
    payload = {key: value for key, value in event.items()
               if key not in ("EventHash", "Signature")}
    # Propagate canonicalization errors; do not round, stringify or fall back.
    return rfc8785.dumps(payload)


def compute_event_hash(event: dict) -> str:
    return "sha256:" + hashlib.sha256(canonical_event(event)).hexdigest()


def main() -> int:
    directory = Path(__file__).resolve().parent
    filenames = ("test-001-simple-event.json", "test-002-jcs-regressions.json")
    count = 0
    for filename in filenames:
        document = json.loads((directory / filename).read_text(encoding="utf-8"))
        cases = document.get("cases", [document])
        for case in cases:
            name = case.get("id", filename)
            actual_bytes = canonical_event(case["input"])
            if actual_bytes != case["canonicalJson"].encode("utf-8"):
                raise ValueError(f"{name}: canonical byte mismatch: {actual_bytes!r}")
            actual_hash = compute_event_hash(case["input"])
            if actual_hash != case["expectedHash"]:
                raise ValueError(f"{name}: hash mismatch: {actual_hash}")
            print(f"PASS {name}")
            count += 1
    if count == 0:
        raise ValueError("No test cases executed")
    print(f"{count} hash vectors passed (not a CAP conformance claim)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
