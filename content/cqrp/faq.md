---
title: Chrome Quantum-resistant Root Program - Frequently Asked Questions
---
# Frequently Asked Questions

[TOC]

### Does Chrome support use of ML-DSA certificates?
Yes. Beginning in [Chrome 150](https://chromestatus.com/feature/5174590524489728), Chrome supports ML-DSA in private PKI hierarchies, making it possible to test non-MTC post-quantum X.509 certificates locally or within enterprise environments.

### Why does Chrome not support ML-DSA in the Chrome Quantum-resistant Root Store?
Post-quantum cryptographic algorithms such as ML-DSA feature significantly larger key and signature sizes than classical algorithms (like RSA or ECDSA). In a traditional PKI model using X.509 certificates, sending heavy, serialized chains of post-quantum signatures and Certificate Transparency (CT) proofs during every TLS handshake creates severe bandwidth penalties and increases connection latency across the web.

Instead of traditional X.509 chains, Chrome uses **Merkle Tree Certificates (MTCs)** developed in the [IETF PLANTS working group](https://datatracker.ietf.org/group/plants/about/):

* **Lightweight Proofs**: CAs sign a single "Tree Head" representing millions of certificates. The server sends only a compact Merkle Tree proof of inclusion rather than full signature chains.
* **Decoupled Payload Size**: Cryptographic strength is decoupled from transmitted data size, preserving fast handshake speeds.
* **Built-in Transparency**: Transparency is an intrinsic property of MTC issuance, making it impossible to issue a certificate without including it in a public tree, eliminating the need for extra CT overhead in the TLS handshake.

### When will MTCs be usable in Chrome?
Chrome's rollout of Merkle Tree Certificates spans three distinct phases:

- **Phase 1 (Underway)**: Feasibility study conducted in collaboration with Cloudflare to evaluate real-world performance and security of MTC connections. Experimental MTC connections are dual-backed by traditional X.509 certificates for safe fallback.
- **Phase 2 (Target: Q1 2027)**: Initial public MTC bootstrapping. Qualified CT Log operators (operating usable CT logs in Chrome prior to February 1, 2026) will be invited to participate in running initial public MTC issuance logs and mirrors.
- **Phase 3 (Target: Q3 2027)**: Launch of the Chrome Quantum-resistant Root Store (CQRS) and onboarding of prospective MTC CA Operators under the Chrome Quantum-resistant Root Program Policy. This phase will also introduce optional downgrade protections for sites using quantum-resistant certificates.
