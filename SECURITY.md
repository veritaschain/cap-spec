# Security Policy

## Reporting Security Vulnerabilities

The VeritasChain Standards Organization (VSO) takes security seriously. If you discover a security vulnerability in the CAP specification or related implementations, please report it responsibly.

### How to Report

**Email:** security@veritaschain.org

Please include:
- Description of the vulnerability
- Steps to reproduce (if applicable)
- Potential impact assessment
- Any suggested mitigations

### Response Timeline

| Phase | Timeline |
|-------|----------|
| Acknowledgment | Within 48 hours |
| Initial assessment | Within 7 days |
| Status update | Within 14 days |
| Resolution target | Within 90 days |

### Scope

This security policy covers:
- CAP specification documents
- JSON schemas
- Reference implementations in this repository
- Test vectors and examples

### Out of Scope

- Third-party implementations of CAP
- Vulnerabilities in dependencies (report to upstream maintainers)
- Social engineering attacks
- Physical security issues

## Security Considerations in CAP

### Cryptographic Components

CAP relies on the following cryptographic primitives:

| Component | Algorithm | Standard | Security Level |
|-----------|-----------|----------|----------------|
| Event Hash | SHA-256 | FIPS 180-4 | 128-bit |
| Digital Signature | Ed25519 | RFC 8032 | 128-bit |
| Canonicalization | JCS | RFC 8785 | N/A |
| UUID Generation | UUID v7 | RFC 9562 | N/A |

### Crypto Agility

CAP is designed with crypto agility in mind. The `HashAlgo` and `SignAlgo` fields allow future migration to post-quantum algorithms (e.g., CRYSTALS-Dilithium) without breaking backward compatibility.

Implementers SHOULD:
- Support algorithm negotiation
- Plan for algorithm deprecation
- Monitor NIST PQC standardization

### Known Security Considerations

#### 1. Hash Chain Integrity

The hash chain provides tamper detection but not prevention. Implementers MUST:
- Store events in append-only storage where possible
- Implement external anchoring (Merkle roots) for high-assurance deployments
- Verify chain integrity on every access

#### 2. Time Source Security

CAP timestamps require reliable time sources. Implementers SHOULD:
- Use NTP with authenticated time sources
- Consider PTP (IEEE 1588) for high-precision requirements
- Log time source synchronization status

#### 3. Key Management

Ed25519 keys for signing require proper management:
- Generate keys using cryptographically secure random number generators
- Store private keys in HSMs or secure enclaves for production use
- Implement key rotation procedures
- Maintain key revocation lists

#### 4. Privacy Protection

CAP uses hashing for privacy protection. However:
- `PromptHash` may be vulnerable to rainbow table attacks for common prompts
- Consider salting for high-sensitivity deployments
- Actor anonymization (k-anonymity) may be insufficient for unique users

### Threat Model Reference

For detailed threat analysis, see [docs/Threat-Model.md](docs/Threat-Model.md).

## Coordinated Disclosure

VSO practices coordinated disclosure:

1. Reporter notifies VSO
2. VSO acknowledges and investigates
3. VSO develops fix/mitigation
4. VSO notifies affected parties (if applicable)
5. Public disclosure after fix is available

We request a 90-day disclosure window for critical vulnerabilities.

## Security Advisories

Security advisories will be published:
- In this repository's Security tab
- On https://veritaschain.org/security
- Via the security@veritaschain.org mailing list

## Acknowledgments

We thank security researchers who responsibly disclose vulnerabilities. Contributors will be acknowledged (with permission) in our security advisories.

---

**Contact:** security@veritaschain.org  
**PGP Key:** Available upon request

---

*Last updated: 2026-01-13*
