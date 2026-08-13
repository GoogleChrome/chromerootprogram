---
title: Google Chrome Root Programs
---
# Google Chrome Root Programs

Google Chrome uses certificates issued by Certification Authorities (CAs) to secure connections across the web. When Chrome connects to a website, it verifies the site's certificate against a list of trusted CAs, known as a Root Store, to ensure the connection is private and safe.

To secure the web today and prepare for the post-quantum future, Chrome operates two distinct root programs:

* **[The Chrome Root Program](crp/policy.md)**: [Launched in 2022](https://blog.chromium.org/2022/09/announcing-launch-of-chrome-root-program.html), this program determines which website certificates Chrome trusts by default, providing consistent and reliable security for HTTPS connections.

* **[The Chrome Quantum-resistant Root Program](cqrp/draft-policy.md)**: Designed for the post-quantum era, this program uses Merkle Tree Certificates (MTCs) to deliver quantum-safe security without slowing down page connections. Learn more about Google's planned adoption of MTCs on the [Google Security Blog](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/).
