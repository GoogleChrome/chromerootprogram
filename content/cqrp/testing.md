---
title: Chrome Quantum-resistant Root Program - Testing Instructions
---
# Testing Instructions

## Last updated: July 17, 2026

As [announced](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/) in February 2026, Chrome will not add traditional X.509 certificates containing post-quantum cryptography to its root store. Instead, Chrome will rely on Merkle Tree Certificates (MTCs) to mitigate the impact of post-quantum key and signature size increases while integrating transparency directly into the issuance process.

To support development and interoperability with Chrome, we are providing a mechanism to submit non-production cosigners for inclusion in Chrome to be used for general testing and validation. Applications will begin in July 2026, and will be open to any organization currently operating either traditional root CAs or CT logs included in Chrome.

This FAQ aims to provide clarity on the test and validation trust store.

## Frequently Asked Questions (FAQ)

[TOC]

### Does Chrome support use of ML-DSA certificates?
Yes. Beginning in [Chrome 150](https://chromestatus.com/feature/5174590524489728), Chrome supports ML-DSA in private PKI hierarchies, making it possible to test non-MTC post-quantum X.509 certificates locally or within enterprise environments.

### What is Chrome providing for testing?
We are offering a dedicated MTC root store explicitly for the purposes of end-to-end testing and validation. This test root store will be delivered to Chrome clients, but not trusted for production use. Instead, Chrome clients can be individually configured to enable trust of MTCs from these specific test issuers. Chrome M152 is expected to have support for testing Standalone and Landmark-relative MTCs.

Additionally, Chrome may monitor the logs included in this testing phase for availability and correctness, similar to how it currently monitors CT logs.

### How can I request access to include my organization's cosigners in the testing root store and when will that access be provided?
Organizations currently operating either traditional root CAs or CT logs included in Chrome can request the inclusion of testing cosigners by creating a new issue in the [Chromium Issue Tracker](https://issues.chromium.org/) (use the *New Test MTC CA Operator* template).

Chrome will begin processing requests starting July 31, 2026, and aim to include these cosigner keys in the test root store within two weeks of reviewing the request. We will follow up on the issue tracker once the root store has been updated.

### How do I enable the testing root store in Chrome?
The testing root store is only supported in Chrome 152 or later (currently Chrome Canary).

You can enable the experimental features using `chrome://flags`:

1. Open Chrome Canary and navigate to `chrome://flags`.
2. Search for and enable the following two flags:
   - **`verify-mtcs`**
   - **`test-root-store`**
3. Click **Relaunch** at the bottom of the page.

MTC test root store anchors and cosigner metadata are updated dynamically via Chrome’s Component Updater:

1. Navigate to `chrome://components`.
2. Locate the **PKI Metadata Fastpush** component.
3. Click **Check for update**.
4. Wait until the status displays **Component updated** or **Up-to-date**.
5. Relaunch Chrome to ensure the newly downloaded test anchors are loaded.

### How can I verify that my connection is using an MTC?
To verify that your site successfully established a connection using MTCs:

1. Open DevTools (`F12` or `Cmd` + `Option` + `I`).
2. Go to the **Security** tab and refresh the page.
3. Under **Connection Details**, confirm the negotiated algorithms:
   - **Signature / Cosignature Algorithm**: `ML-DSA-44` (or different)
   - **Key Exchange**: `X25519MLKEM768` (ML-KEM)

### What can I expect `cosigners.json` to include?
The JSON can be found at: [https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json).

- This file respects the schema provided at: [https://www.gstatic.com/mtcs/cosigners/v1/cosigners_schema.json](https://www.gstatic.com/mtcs/cosigners/v1/cosigners_schema.json).
- Keys referenced in the JSON are available at: [https://www.gstatic.com/mtcs/cosigners/v1/cosigners.pem](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.pem).

### Are constraints such as certificate lifetimes and algorithms strictly enforced in testing?
Yes. Testing certificates will be subject to the same validation logic as production certificates. This includes restrictions to 7-day or 47-day maximum validity. For both Mirroring and CA Cosigners, we will accept only **ML-DSA-44** (OID: `2.16.840.1.101.3.4.3.17`, RFC 9881) cosigning keys. There is no equivalent key restriction on the test Subscriber certificates.

Though not technically enforced by the client, practices such as the use of strict domain control validation or the use of Hardware Security Modules are encouraged to maximize the value of this testing infrastructure.

### Am I required to run a mirror during the testing phase?
Yes. As Chrome will be enforcing realistic cosigner requirements (e.g., requiring mirroring cosignatures on Standalone certificates), we ask that participants in the testing phase contribute a Mirroring Cosigner usable by all CA Cosigners to ensure adequate and realistic mirroring capacity is available.

The CA Cosigner issuance log should implement the API endpoints, cryptographic formats, and Merkle Tree structures defined in the MTC [specification](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) (specifically `draft-ietf-plants-merkle-tree-certs-05`) and the `tlog-tiles` [specification](https://github.com/C2SP/C2SP/blob/main/tlog-tiles.md). The Mirroring Cosigner should implement the API endpoints, cryptographic formats, and validation logic defined in the MTC specification and the `tlog-mirror` [specification](https://github.com/C2SP/C2SP/blob/main/tlog-mirror.md).

### How many cosignatures are required for Chrome to validate my test certificate?
Chrome clients will enforce the same cosignature requirements to validate a certificate in the testing phase as with production certificates. Standalone certificates must have at least two cosignatures. One must be from the MTC CA Operator, and one must be from a Mirroring Cosigner recognized by the Chrome test root store. Chrome's servers will similarly ensure that issuer logs are mirrored before trusting subtrees for Landmark-relative certificates.

### What exactly might Chrome monitor for "availability and correctness"?
Chrome’s compliance monitoring infrastructure may continuously query both the test MTC CA issuance logs and Mirroring Cosigner endpoints throughout their lifetime. The monitoring would focus on uptime metrics, cryptographic integrity, and adherence to technical specifications, intending to be a feedback loop for MTC CA Operators from Chrome.

Development on Chrome's monitoring infrastructure is ongoing, but Operators can expect that Chrome would monitor for availability and uptime by looking for:

1. Endpoints (both issuance logs and mirrors) maintaining at least 99% uptime over a 30-day rolling window (no more than 7.2 hours of downtime per month).
2. Endpoints not experiencing a daily uptime below 99.9% for more than 3 consecutive days.
3. A majority of mirror checkpoints remaining within a few minutes of the current issuer checkpoint.

Operators should also expect that Chrome monitors would verify that:

1. API endpoints, cryptographic formats, and validation logic all match the definitions in the MTC [specification](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/), as well as the [tlog-tiles](https://github.com/C2SP/C2SP/blob/main/tlog-tiles.md) (for CAs) and [tlog-mirror](https://github.com/C2SP/C2SP/blob/main/tlog-mirror.md) (for mirrors) specifications.
2. Merkle trees served cryptographically validate.
3. Mirrors provide consistent, append-only views of mirrored logs.
4. Log entries remain available for at least 35 days after the corresponding certificate's validity period ends.

Chrome may send notifications to the Operator when availability and correctness failures are observed. During the testing phase, these notifications are purely to support Operators in developing robust implementations, and we encourage (but do not require) sharing postmortems and development challenges or milestones to [mtcs@chromium.org](mailto:mtcs@chromium.org) so that everyone can benefit from lessons learned.

### Where should I share my findings and feedback?
Please share your implementation experiences and challenges on [mtcs@chromium.org](mailto:mtcs@chromium.org)! The hope is that everyone in the ecosystem can benefit from these learnings.

### What happens to my test setup when Phase 2 (production inclusion in the default Chrome Quantum-resistant Root Store) launches in 2027?
The test setup can persist at the MTC CA Operators' discretion. We will maintain Chrome's testing infrastructure until Chrome accepts the first Phase 3 eligible MTC CA Operators.

Notably, cosigner keys accepted as part of the testing trust store will not be accepted for production use in Chrome. MTC CA Operators will need to generate new cosigner keys and fully adhere to the CQRP Policy to be included in Phase 2 or later launches.

### How are approved test CAs and mirrors designated in `cosigners.json`?
All cosigners approved for the testing phase are included in [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json) with a `realm` property of `"UNTRUSTED_VALIDATION_ONLY"`. This explicitly distinguishes test cosigners from production CAs (`"PUBLICLY_TRUSTED"`), ensuring Chrome clients restrict test keys to validation testing only and never trust them for production certificate validation.
