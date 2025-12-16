---
title: Chrome Root Program Policy, Version 1.8
---

# Chrome Root Program Policy, Version 1.8

## Last updated: 2026-XX-XX

Bookmark this page as [https://g.co/chrome/root-policy](https://g.co/chrome/root-policy)

## Table of Contents

- [Introduction](#introduction)
  - [Apply for Inclusion](#apply-for-inclusion)
  - [Chrome's Ongoing Commitment to Transport Security](#chromes-ongoing-commitment-to-transport-security)
  - [Moving Forward, Together](#moving-forward-together)
  - [Additional Information](#additional-information)
- [Change History](#change-history)
- [Definitions](#definitions)
- [1. Minimum Requirements for CAs Included in the Chrome Root Store](#1-minimum-requirements-for-cas-included-in-the-chrome-root-store)
  - [1.1. PKI Policy Governance and Requirements](#11-pki-policy-governance-and-requirements)
    - [1.1.1. Baseline Requirements](#111-baseline-requirements)
    - [1.1.2. Common CA Database](#112-common-ca-database)
    - [1.1.3. Chrome Root Program Participant Policies](#113-chrome-root-program-participant-policies)
  - [1.2. Reducing Attack Surface of the Chrome Root Store](#12-reducing-attack-surface-of-the-chrome-root-store)
    - [1.2.1. Maximum Number of CAs per CA Owner](#121-maximum-number-of-cas-per-ca-owner)
  - [1.3. Modern Infrastructures](#13-modern-infrastructures)
    - [1.3.1. Promote use of Modern PKI Hierarchies](#131-promote-use-of-modern-pki-hierarchies)
      - [1.3.1.1. Root CA Succession Planning](#1311-root-ca-succession-planning)
      - [1.3.1.2. Root CA Term-Limit](#1312-root-ca-term-limit)
      - [1.3.1.3. Subordinate CA Certificate Lifecycle Management](#1313-subordinate-ca-certificate-lifecycle-management)
    - [1.3.2. Promote use of Dedicated TLS Server Authentication PKI Hierarchies](#132-promote-use-of-dedicated-tls-server-authentication-pki-hierarchies)
    - [1.3.3. Promote Cryptographic Agility and Resilience](#133-promote-cryptographic-agility-and-resilience)
      - [1.3.3.1. Automation Support](#1331-automation-support)
        - [1.3.3.1.1. ACME Solutions](#13311-acme-solutions)
        - [1.3.3.1.2. Non-ACME Solutions](#13312-non-acme-solutions)
    - [1.3.4. Promote Increased Transparency](#134-promote-increased-transparency)
        - [1.3.4.1. Logging Precertificates ](#1341-logging-precertificates)
        - [1.3.4.2. Logging Final Certificates ](#1341-logging-final-certificates)
        - [1.3.4.2. Contributing to a healthy CT ecosystem](#1342-contributing-to-a-healthy-ct-ecosystem)
  - [1.4. Audits](#14-audits)
    - [1.4.1. Annual Audits](#141-annual-audits)
    - [1.4.2. Ad-Hoc Audits](#142-ad-hoc-audits)
  - [1.5. Reporting and Responding to Incidents](#15-reporting-and-responding-to-incidents)
    - [1.5.1. Incident Reports](#151-incident-reports)
    - [1.5.2. Communicating with Chrome During Incidents](#152-communicating-with-chrome-during-incidents)
  - [1.6 Timely and Transparent Communications](#16-timely-and-transparent-communications)
    - [1.6.1. Notification of CA Certificate Issuance](#161-notification-of-ca-certificate-issuance)
    - [1.6.2. Notification of Procurement, Sale, or other Change Control Events](#162-notification-of-procurement-sale-or-other-change-control-events)
    - [1.6.3. Industry and Community Forum Engagement](#163-industry-and-community-forum-engagement)
- [2. Minimum Requirements for Applicant CAs Requesting Inclusion into the Chrome Root Store](#2-minimum-requirements-for-applicant-cas-requesting-inclusion-into-the-chrome-root-store)
  - [2.1. PKI Policy Governance and Requirements](#21-pki-policy-governance-and-requirements)
  - [2.2. Root CA Key Material Freshness](#22-root-ca-key-material-freshness)
  - [2.3. Dedicated TLS Server Authentication PKI Hierarchies](#23-dedicated-tls-server-authentication-pki-hierarchies)
  - [2.4. Promote Cryptographic Agility and Resilience](#24-promote-cryptographic-agility-and-resilience)
  - [2.5. Annual Audits](#25-annual-audits)

## Introduction

Google Chrome relies on Certification Authority systems (herein referred to as "CAs") to issue certificates to websites. Chrome uses these certificates to help ensure the connections it makes on behalf of its users are properly secured. Chrome accomplishes this by verifying that a website's certificate was issued by a recognized CA, while also performing additional evaluations of the HTTPS connection's security properties. Certificates not issued by a CA trusted by Chrome or a user's local settings can cause users to see warnings and error pages.

When making HTTPS connections, Chrome refers to a list of self-signed root certificates from CAs that have demonstrated why continued trust in them is justified. This list is known as a "Root Store." CA certificates included in the [Chrome Root Store](https://g.co/chrome/root-store) are selected on the basis of publicly available and verified information, such as that within the Common CA Database ([CCADB](https://ccadb.org/)), and ongoing reviews by the Chrome Root Program.

The Chrome Root Program Policy below establishes the minimum requirements for CA certificates to be included as trusted in a default installation of Chrome. 

The Chrome Root Program continuously evolves this policy to enhance the security and resilience of the Internet ecosystem, consistent with Google's ongoing [commitment](#chromes-ongoing-commitment-to-transport-security) to secure and reliable network connections in Chrome. This involves establishing and periodically strengthening minimum requirements for CAs. New requirements, sometimes only for Applicants, are introduced to progressively raise the baseline of trust and drive the adoption of modern, agile, and secure Public Key Infrastructure (PKI) practices. This phased approach allows the program to integrate advancements and best practices, ensuring that certificates included in the Chrome Root Store consistently provide value to Chrome end users that exceeds the risk of their continued inclusion, while accounting for the practicalities of protecting users at scale. Aspects of value are principally demonstrated through the real-world use of the corresponding root CA certificate. This includes active TLS server authentication certificate issuance, observability of time-valid and unrevoked TLS server authentication certificates across the Internet, and direct reliance on those certificates by the Chrome Certificate Verifier when securing Chrome user connections.

Except in the case of CA Owners applying for inclusion, this policy makes no stipulation on the characteristics or PKI use cases served by CAs not included in the current version of the Chrome Root Store.

Any questions regarding this policy can be directed to chrome-root-program [at] google [dot] com.

### Apply for Inclusion

CA Owners that satisfy the requirements defined in the policy below may apply for self-signed root CA certificate inclusion in the Chrome Root Store using [these](apply-for-inclusion.md) instructions.

Applicants are expected to continuously adhere to the policies outlined herein, irrespective of their inclusion request submission date. All Applicants are expected to satisfy the requirements set forth in both the ["Minimum Requirements for CAs included in the Chrome Root Store"](#1-minimum-requirements-for-cas-included-in-the-chrome-root-store) and ["Minimum Requirements for Applicant CAs Requesting Inclusion into the Chrome Root Store"](#2-minimum-requirements-for-applicant-cas-requesting-inclusion-into-the-chrome-root-store) Sections. Where requirements in these sections differ, the Applicant-specific requirements take precedence.

If an Applicant's Root Inclusion Request is currently in the CCADB with a status of 'Verification By Root Store' and has not yet received a final determination, and this policy is updated to a new version, the Chrome Root Program will change the request's status to 'CA Providing Data.' Applicants must review and ensure compliance with the updated policy expectations before resubmitting their Root Inclusion Request for review by the Chrome Root Program.

### Chrome's Ongoing Commitment to Transport Security

The Chrome Root Program and corresponding policy represent Google's [ongoing commitment](https://transparencyreport.google.com/https/overview?hl=en) to upholding secure and reliable network connections in Chrome.

In support of this commitment, Google, as it deems appropriate and at its sole discretion:

- includes or removes certificates in the Chrome Root Store. The selection and ongoing inclusion of certificates is done to enhance the security of Chrome. Certificates included in the Chrome Root Store must provide value to Chrome end users that exceeds the risk of their continued inclusion. Certificates that do not provide a broad service to all browser users will not be added to, or may be removed from the Chrome Root Store. Initial and sustained inclusion in the Chrome Root Store is not guaranteed to any CA Owner.
- applies metadata-based [name constraints](https://source.chromium.org/chromium/chromium/src/+/main:net/cert/root_store.proto;drc=7c2b25f6a19cfeeea67f0f43ed33617840bab33d;l=39) to certificates in the Chrome Root Store. These constraints, which may go beyond those in the CA certificates themselves, restrict the use of corresponding TLS server authentication certificates to specific Top-Level Domains (TLDs) and/or Second-Level Domains (SLDs).

Chrome maintains a variety of mechanisms to protect its users from certificates that put their safety and privacy at risk, and is prepared to use them as necessary. A Chrome Root Program Participant's failure to follow the minimum requirements defined in this policy may result in the corresponding certificate's removal from the Chrome Root Store, limitations on Chrome's acceptance of the certificates they issue, or other technical or policy restrictions. Before taking such action, the Chrome Root Program always evaluates the broader context of an individual incident and considers it against the [factors](#151-incident-reports) significant to the Chrome Root Program.

### Moving Forward, Together

The "Moving Forward, Together" initiative envisions a future Internet ecosystem that includes modern, reliable, highly agile, purpose-driven PKIs with an emphasis on automation, simplicity, and security.

Learn more about priorities and initiatives that may influence future versions of this policy [here](moving-forward-together.md). Please note "Moving Forward, Together" is future looking and does not describe normative requirements.

### Additional Information

If you're a Chrome user experiencing a certificate error and need help, please see [this support article](https://support.google.com/chrome/answer/6098869?hl=en).

If you're a website operator, you can learn more about [why HTTPS matters](https://web.dev/why-https-matters/) and how to [secure your site with HTTPS](https://support.google.com/webmasters/answer/6073543). If you've got a question about a certificate you've been issued, please contact the CA that issued it.

If you're responsible for a CA that is not trusted by default in Chrome and only issues certificates to your enterprise organization, sometimes called an "enterprise", "private" or "locally trusted" CA, the Chrome Root Program Policy does not apply to or impact your CA's PKI use cases. Enterprise CAs are used for issuing certificates to internal resources like intranet sites or applications that do not directly interact with external users of the public Internet (e.g., a TLS server authentication certificate issued to a corporate intranet site).

Though uncommon, websites can also use certificates to identify clients (e.g., users) connecting to them. Besides ensuring it is well-formed, Chrome passes this type of certificate to the server, which then evaluates and enforces its chosen policy. The policies on this page do not apply to client authentication certificates.

Learn more about the Chrome Root Store and Chrome Certificate Verifier [here](https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/faq.md).

This policy, along with archived versions, is available in Markdown [here](https://github.com/GoogleChrome/chromerootprogram).

## Change History

| Version | Date | Note |
|-------- |----- |----- |
| 1.8 | 2026-XX-XX | Updates include, but are not limited to: TBD
| 1.7 | 2025-07-15 | Updates include, but are not limited to: *(1)* add the ARI RFC numerical identifier, *(2)* remove requirements redundant with CCADB Policy Version 2.0
| 1.6 | 2025-02-15 | Updates include, but are not limited to: *(1)* the future phase-out of non-TLS server authentication dedicated hierarchies from the Chrome Root Store, *(2)* requirements for future Applicants related to automation support, promoting simplicity of policy documents, and the definition of a dedicated TLS server authentication PKI hierarchy, *(3)* improved alignment with the TLS Baseline Requirements following Ballot SC-077, *(4)* addition of subsection numbers and major reorganization of normative and non-normative requirements|
| 1.5 | 2024-01-16 | Updates include, but are not limited to: *(1)* incorporated CA Owner feedback in response to policy Version 1.4 (clean-ups and clarifications throughout the policy), *(2)* added new subsections for Root CA Key Material Freshness, Automation Support, and the Root CA Term-Limit, *(3)* aligned incident reporting format and timelines with CCADB.org |
| 1.4 | 2023-03-03 | Updates include, but are not limited to: *(1)* alignment with CCADB Policy Version 1.2 and the Baseline Requirements, *(2)* clarify requirements related to the submission of annual self-assessments, *(3)* clarify requirements to better align with program intent (e.g., CA Owner policy document freshness), *(4)* updated audit and incident reporting requirements to promote increased transparency, *(5)* require subordinate CA disclosures in CCADB, *(6)* clarify CA certificate issuance notification requirements |
| 1.3 | 2023-01-06 | Updated to include the CCADB Self-Assessment |
| 1.2 | 2022-09-01 | Updated to reflect the launch of the Chrome Root Program. Updates include, but are not limited to: *(1)* removal of pre-launch discussion, *(2)* clarifications resulting from the June 2022 Chrome CCADB survey, *(3)* minor reorganization of normative and non-normative requirements |
| 1.1 | 2022-06-01 | Updated in anticipation of the future Chrome Root Program launch. Updates include, but are not limited to: *(1)*  future-dated Applicant requirements for dedicated TLS-hierarchies and key-pair freshness, *(2)*  clarification of audit expectations, *(3)*  requirements for cross-certificate issuance notification, *(4)*  description of and requirements related to an annual self-assessment process, *(5)*  an outline of priority Chrome Root Program initiatives |
| 1.0 | 2020-12-20 | Initial release |

## Definitions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this policy are to be interpreted as described in [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119).

This policy considers a "CA Owner" to be the organization or legal entity that is either:

- represented in the subject DN of the CA certificate; or
- in possession or control of the corresponding private key capable of issuing new certificates, if not the same organization or legal entity directly represented in the subject DN of the certificate.

This policy considers an "Applicant" to be an organization or legal entity that has an open "Root Inclusion Request" submitted to Google Chrome in the [CCADB](https://ccadb.org/).

This policy uses the term "Chrome Root Program Participants" to describe:

- Applicants; and
- CA Owners with either (a) a certificate included in the Chrome Root Store or (b) a CA certificate that validates to a certificate included in the Chrome Root Store.

This policy uses the term "Externally-operated CA" to describe a subordinate CA certificate issued where the organization or legal entity in possession or control of the corresponding private key capable of issuing new certificates is not under the sole control of the CA Owner whose certificate is included in the Chrome Root Store.

This policy considers a PKI hierarchy as "dedicated" if it is intended to serve one specific use case, for example, the issuance of TLS server authentication certificates.

To continually raise the baseline of trust and drive the adoption of modern, agile, and secure PKIs, this policy sometimes "phases out" practices (sometimes referred to as a "phase-out"). Unless otherwise specified, phase-outs are accomplished using an [SCTNotAfter constraint](https://source.chromium.org/chromium/chromium/src/+/main:net/cert/root_store.proto;drc=a783c3bab474ff68e675e2753f91c92ca817e072;l=15?q=f:root_store.proto&ss=chromium) on a corresponding root CA’s certificate included in the Chrome Root Store. TLS server authentication certificates issued on or before a practice’s or PKI hierarchy’s specified phase-out date and time will be trusted in Chrome until expiry, whereas certificates issued after will not be trusted by default. The corresponding root CA’s certificate included in the Chrome Root Store will be removed upon the absence of unexpired and unrevoked TLS server authentication certificates issued prior to the phase-out date.

## 1. Minimum Requirements for CAs Included in the Chrome Root Store

The following requirements are effective immediately, unless explicitly stated as otherwise.

### 1.1. PKI Policy Governance and Requirements

Chrome Root Program Participants MUST satisfy the requirements defined in this policy, including taking responsibility for ensuring the continued compliance of all corresponding subordinate CAs and delegated third parties participating in the PKI.

#### 1.1.1. Baseline Requirements

Chrome Root Program Participants that issue TLS server authentication certificates trusted by Chrome MUST adhere to the latest version of the ["Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates"](https://cabforum.org/baseline-requirements-documents/) ("Baseline Requirements"). The Baseline Requirements are consensus-driven requirements owned by a community of participants represented in the [CA/Browser Forum](https://cabforum.org/) [Server Certificate Working Group](https://cabforum.org/working-groups/server/). No single organization, including Google, has the authority to grant exceptions to the Baseline Requirements.

In some cases, this policy strengthens requirements described in the Baseline Requirements.

#### 1.1.2. Common CA Database

The Chrome Root Program relies on the [CCADB](https://ccadb.org/) to identify and maintain up-to-date information for Chrome Root Program Participants and the corresponding PKI hierarchies.

Chrome Root Program Participants MUST adhere to the latest version of the [CCADB Policy](https://www.ccadb.org/policy).

In some cases, this policy strengthens requirements described in the CCADB Policy.

#### 1.1.3. Chrome Root Program Participant Policies

**Effective June 15, 2026**, a Chrome Root Program Participant's CP or combined CP/CPS MUST explicitly state adherence to the latest published version of this policy and the CCADB Policy. This attestation SHOULD be made in Section 1.1 ("Overview").

### 1.2. Reducing Attack Surface of the Chrome Root Store

#### 1.2.1. Maximum Number of CAs per CA Owner

If a CA Owner already has two (2) or more self-signed root CA certificates included in the Chrome Root Store, the Chrome Root Program will only accept a new CCADB Root Inclusion Request to replace an existing certificate (i.e., 'one in, one out').

**Before June 15, 2026**, CA Owners with more than two (2) self-signed root CA certificates in the Chrome Root Store MUST submit a written consolidation plan to the Chrome Root Program. This plan MUST:
1. Identify the two (2) root CA certificates that will remain in the Chrome Root Store, and 
2. Provide a phase-out date for all of their other root CA certificates. The phase-out date MUST be **before September 15, 2027, (00:00 UTC)**.

**Effective September 15, 2027**, the Chrome Root Store will only include a maximum of two (2) self-signed root CA certificates per CA Owner. PKI hierarchies being phased-out are not counted toward this limit.

To further reduce negative impact to the ecosystem, the Chrome Root Store may temporarily continue to include more than two (2) self-signed root CA certificates past the specified consolidation timeline on a case-by-case basis.

### 1.3. Modern Infrastructures

#### 1.3.1. Promote use of Modern PKI Hierarchies

##### 1.3.1.1. Root CA Succession Planning

CA Owners SHOULD request for the replacement of a certificate included in the Chrome Root Store no later than five (5) years after the release date of the Chrome Root Store's initial inclusion of the certificate.

Before a CA Owner submits a Root Inclusion Request to the CCADB, it MUST have issued a cross-certificate from the CA being replaced to the replacement CA. Due to the existence of the cross-certificate, TLS server authentication certificates issued by the replacement PKI hierarchy will be trusted by default in versions of Chrome relying on the Chrome Root Store, regardless of whether they are capable of receiving updates to the Chrome Root Store.

Within no more than 90 calendar days after a replacement CA certificate being first distributed by the Chrome Root Store and as disclosed in the CCADB, the CA Owner MUST have transitioned all TLS server authentication certificate issuance intended to be trusted by default in Chrome from the cross-signing PKI hierarchy to the replacement PKI hierarchy. To technically enforce this transition, the CA being replaced will have a phase-out date set to 90 calendar days after the Applicant CA certificate being first distributed by the Chrome Root Store. While the CA Owner is not prohibited from continuing to issue certificates from the PKI hierarchy being replaced after this phase-out date, such certificates will not be trusted by default in Chrome. The CA certificate being replaced will be removed from the Chrome Root Store upon the absence of unexpired and unrevoked TLS server authentication certificates (excluding test certificates like those disclosed to the CCADB) disclosed to Certificate Transparency (CT) before this phase-out date.

##### 1.3.1.2. Root CA Term-Limit

Any root CA certificate with corresponding key material generated more than 15 years ago will be removed from the Chrome Root Store on an ongoing basis.

The age of the key material will be determined by the earliest of either:

- a key generation report issued by a Qualified Auditor that distinctly represents the corresponding key; or
- the validity date of the earliest appearing certificate that contains the corresponding public key.

To phase-in these requirements in a manner that reduces negative impact to the ecosystem, affected root CA certificates included in the Chrome Root Store will be removed according to the schedule in the table below.

| Key Material Created | Approximate Removal Date |
|--------------------- |------------------------- |
| Between January 1, 2006 and December 31, 2007 (inclusive) | April 15, 2026 |
| Between January 1, 2008 and December 31, 2009 (inclusive) | April 15, 2027 |
| Between January 1, 2010 and December 31, 2011 (inclusive) | April 15, 2028 |
| Between January 1, 2012 and April 14, 2014 (inclusive) | April 15, 2029 |
| After April 15, 2014 | 15 years from generation |

To further reduce negative impact to the ecosystem, the Chrome Root Store may temporarily continue to include a root CA certificate past its defined term-limit on a case-by-case basis, if the corresponding CA Owner has submitted a Root Inclusion Request to the CCADB for a replacement root CA certificate at least one (1) year in advance of the approximate removal date.

Other circumstances may lead to the removal of a root CA certificate included in the Chrome Root Store before the completion of its term.

##### 1.3.1.3. Subordinate CA Certificate Lifecycle Management

The lifecycle management of subordinate CA certificates plays a crucial role in promoting agility and resilience within the ecosystem. By setting clear expectations for their validity and renewal, the Chrome Root Program aims to align certificate profiles with modern best practices, reduce reliance on specific subordinate CA certificates that could be single points of failure, and discourage potentially harmful practices. This approach allows the ecosystem to benefit from continuous improvement efforts.

To achieve these goals, it's encouraged that all subordinate CA certificates that validate to a certificate included in the Chrome Root Store align with the following practices:

- Subordinate CA certificates SHOULD have a maximum validity period of three (3) years.
- CA Owners SHOULD create and deploy new subordinate CA certificates at least once every year. CA Owners SHOULD actively transition subscriber certificate issuance to these newly deployed CAs.

#### 1.3.2. Promote use of Dedicated TLS Server Authentication PKI Hierarchies

The Chrome Root Store is solely relied upon for TLS server authentication in Chrome; it is not used for any other PKI use case (e.g., TLS client authentication, secure email, code-signing, etc.).

To align all PKI hierarchies included in the Chrome Root Store on the principle of serving only TLS server authentication use cases, the Chrome Root Program will phase-out multi-purpose roots from the Chrome Root Store.

**Beginning June 15, 2026**, the Chrome Root Program will phase-out PKI hierarchies found in violation of the below requirements. In these cases, the phase-out date will be set to 90 calendar days following the violation’s detection.

1. All corresponding unexpired and unrevoked subordinate CA certificates operated beneath an existing root included in the Chrome Root Store MUST:
    -  if disclosed to the CCADB **before June 15, 2026**: include the extendedKeyUsage extension and (a) only assert an extendedKeyUsage purpose of id-kp-serverAuth OR (b) only assert extendedKeyUsage purposes of id-kp-serverAuth and id-kp-clientAuth.
    -  if disclosed to the CCADB **on or after June 15, 2026**: include the extendedKeyUsage extension and only assert an extendedKeyUsage purpose of id-kp-serverAuth.
    -  NOT contain a public key corresponding to any other unexpired or unrevoked certificate that asserts different extendedKeyUsage values.
2. All corresponding subscriber certificates issued **on or after March 15, 2027**, MUST include the extendedKeyUsage extension and only assert an extendedKeyUsage purpose of id-kp-serverAuth.
       
#### 1.3.3. Promote Cryptographic Agility and Resilience

##### 1.3.3.1. Automation Support

Certificate lifecycle management automation solutions ("automation solutions") increase agility and improve the [security](https://zanema.com/papers/imc23_stale_certs.pdf) and resilience of the Internet ecosystem. Automation solutions minimize "hands-on" input required from humans during certificate issuance and renewal. Routine certificate issuance and renewal SHOULD NOT involve human input except as needed for identity or business document verification related to IV, OV, or EV certificate issuance.

**Effective March 15, 2027**, all unexpired and unrevoked subordinate CA certificates signed by a root CA certificate included in the Chrome Root Store MUST be integrated with an automation solution, minimally compliant with either [Section 1.3.3.1.1 ("ACME Solutions")](#13311-acme-solutions) or [Section 1.3.3.1.2 ("Non-ACME Solutions")](#13312-non-acme-solutions). Functionally, this means that every TLS server authentication certificate profile offered by a subordinate CA trusted in Chrome MUST be capable of being issued and renewed using an automation solution. CA Owners MUST attest that this requirement is met for each Baseline Requirements certificate policy OID the corresponding PKI hierarchy issues through a disclosure in the CCADB on the root certificate record of each CA included in the Chrome Root Store.

Additionally, **effective March 15, 2027**, for each CCADB root record corresponding to a root included in the Chrome Root Store, CA Owners MUST disclose at least one (1) automation solution for each Baseline Requirements reserved certificate policy OID appearing in unexpired and unrevoked subscriber certificates. For each such OID, the CA Owner MUST use a disclosed automation solution to issue "Automation Test Certificates" to demonstrate its automation capabilities. Automation Test Certificates MUST be renewed at least once every 30 calendar days; however, at any point, the Chrome Root Program may request more frequent renewal. At least one valid (1) Automation Test Certificate corresponding to each Baseline Requirements reserved certificate policy OID MUST be served by a publicly accessible website whose URL is disclosed to the CCADB on the corresponding intermediate certificate record. CA Owners are encouraged to issue "Short-lived Subscriber Certificates," as [introduced](https://cabforum.org/2023/07/14/ballot-sc-063-v4make-ocsp-optional-require-crls-and-incentivize-automation/) in Version 2.0.1 of the Baseline Requirements, for the Automation Test Certificates.

The above requirements do not:
- Prohibit PKI hierarchies from also supporting other "non-automated" methods of certificate issuance and renewal.
- Require website operators to rely on the automation solution(s) for certificate issuance and renewal.

**Beginning March 15, 2027**, the Chrome Root Program will phase-out PKI hierarchies found issuing new certificates containing a Baseline Requirements certificate policy OID lacking an automation solution attestation disclosure in the CCADB. In these cases, the phase-out date will be set to 90 calendar days following the violation’s detection.

###### 1.3.3.1.1. ACME Solutions

PKI hierarchies SHOULD support the Automatic Certificate Management Environment (ACME) protocol. If ACME is supported:

- The CA Owner MUST disclose to the CCADB an ACME endpoint (i.e., directory URL) accessible to the Chrome Root Program for each Baseline Requirements certificate policy OID the corresponding CA issues (i.e., IV, DV, OV, EV).
- Each endpoint MUST support the following capabilities, as specified in [RFC 8555](https://www.rfc-editor.org/rfc/rfc8555):
    - keyChange,
    - newAccount,
    - newNonce,
    - newOrder, and
    - revokeCert.
- Each endpoint's corresponding issuing CA(s) MUST support Certification Authority Authorization (CAA) Record Extensions for Account URI and ACME Method Binding, as specified in [RFC 8657](https://www.rfc-editor.org/rfc/rfc8657).
- PKI hierarchies supporting the ACME protocol MUST support ACME Renewal Information (ARI, [RFC 9773](https://datatracker.ietf.org/doc/rfc9773/)).
- ACME endpoints SHOULD support the Profiles extension ([RFC TBD]((https://datatracker.ietf.org/doc/draft-ietf-acme-profiles/)).
- ACME endpoints SHOULD be publicly accessible.
- Each endpoint SHOULD be hosted using an appropriate and readily accessible online means that is available on a 24x7 basis.

###### 1.3.3.1.2. Non-ACME Solutions

While ACME support is encouraged, PKI hierarchies MAY support other automation solutions so long as the following characteristics are verifiably demonstrated to the Chrome Root Program. If the requirements in [Section 1.3.3.1.1 ("ACME Solutions")](#13311-acme-solutions) are not met, the CA Owner MUST disclose to the CCADB publicly available information that describes the other automation solution capability for each Baseline Requirements certificate policy OID that the corresponding CA issues and how a subscriber can leverage its benefits. For the purposes of this section, an "automation solution" is defined as the combination of the CA’s issuance interface (e.g., API) and compatible client software provided and maintained directly by the CA Owner that is ultimately operated by the TLS server authentication certificate requestor. This client software SHOULD be comparable in function and operation to an ACME client, and MAY be incorporated into Certificate Lifecycle Management tooling.

- The automation solution MUST:
    - generate a new key pair for each certificate request by default.
    - generate and submit a Certificate Signing Request (CSR).
    - support automated domain control validation (i.e., the automated solution automatically places the Request Token or Random Value in the appropriate location without "hands-on" input from humans, comparable to how ACME clients function), using at least one (1) of the following methods from the Baseline Requirements:
        - DNS Change (Section 3.2.2.4.7)
        - Agreed‑Upon Change to Website v2 (Section 3.2.2.4.18)
    - support automated retrieval of the issued certificate (i.e., the automated solution downloads a copy of the certificate to a well-known location without "hands-on" input from humans, comparable to how ACME clients function).
    - be sufficiently detailed in a completed "Automation Solution Assessment" form by requesting a copy from chrome-root-program [at] google [dot] com.
    - support comparable features as described in [RFC 8657](https://www.rfc-editor.org/rfc/rfc8657) to restrict issuance capabilities to a specific CA account(s) using the "accounturi" CAA parameter and to restrict permitted domain validation methods using the "validationmethods" CAA parameter.
    - support and/or request certificate revocation.
    - support comparable features as described by ACME Renewal Information (ARI, [RFC 9773](https://datatracker.ietf.org/doc/rfc9773/)).

- The automation solution SHOULD:
    - support automated deployment (i.e., installation and configuration) of the issued certificate without "hands-on" input from humans (comparable to how ACME clients function).
    - support comparable features as described by the ACME Profiles extension ([RFC TBD]((https://datatracker.ietf.org/doc/draft-ietf-acme-profiles/)).

#### 1.3.4. Promote Increased Transparency

##### 1.3.4.1. Logging Precertificates 

Within 24 hours of issuance, Chrome Root Program Participants SHOULD log precertificates to at least one (1) CT log [usable or qualified](https://www.gstatic.com/ct/log_list/v3/log_list.json) in Chrome at the time of issuance.

**Effective June 15, 2026**, within 24 hours of issuance, Chrome Root Program Participants MUST log precertificates to at least one (1) CT log [usable or qualified](https://www.gstatic.com/ct/log_list/v3/log_list.json) in Chrome at the time of issuance.

##### 1.3.4.2. Logging Final Certificates 

Within 24 hours of issuance, Chrome Root Program Participants SHOULD log final certificates to at least one (1) CT log [usable or qualified](https://www.gstatic.com/ct/log_list/v3/log_list.json) in Chrome at the time of issuance.

##### 1.3.4.3. Contributing to a healthy CT ecosystem

Chrome Root Program Participants SHOULD contribute to the health and diversity of the CT ecosystem. Such contributions may include, but are not limited to:

- reliably operating CT logs [Usable](https://googlechrome.github.io/CertificateTransparency/log_states.html#usable) in Chrome.
- providing engineering resources or expertise to assist CT log operators or related projects.
- developing and open-sourcing CT-related tools (e.g., for log operations, monitoring, auditing, or client-side integration).
- sponsoring research and development focused on improving CT scalability, security, privacy, or new log designs.
- hosting or mirroring CT logs for redundancy and geographical diversity.
- actively participating in CT standardization and policy development efforts.

### 1.4. Audits

Chrome Root Program Participant CAs MUST be audited in accordance with the table below.

Audits MUST NOT rely on a version of the accepted audit criteria below if it has been superseded by more than 30 calendar days before the start of the corresponding audit period.

| CA Type | EKU Characteristics** | Audit Criteria |
|-------- |---------------------- |--------------- |
| Root CA | N/A | **If WebTrust scheme**…<br><br> (1) "WebTrust Principles and Criteria for Certification Authorities"; and either… <br><br>- (A) "WebTrust Principles and Criteria for Certification Authorities – SSL Baseline with Network Security" or<br>- (B)  "WebTrust Principles and Criteria for Certification Authorities – SSL Baseline"  and "WebTrust Principles and Criteria for Certification Authorities – Network Security"<br><br>and<br><br>(2) "WebTrust for CA - Extended Validation - SSL" (if issuing EV) <br><br>**If ETSI scheme*****...<br><br>(1) ETSI EN 319 411-1 LCP and [DVCP or OVCP];<br><br>or<br><br>(2) ETSI EN 319 411-1 [NCP or NCP+] and EVCP (if issuing EV)<br>
| Cross-Certified Subordinate CA | Either: (1) Certificate does not include an EKU; or (2) EKU is present and includes id-kp-serverAuth or anyExtendedKeyUsage |  Same as above. |
| TLS Subordinate CA or Technically Constrained TLS Subordinate CA | Same as above.  | Same as above. |
| Technically Constrained Non-TLS Subordinate CA | EKU is present and does not include id-kp-serverAuth or anyExtendedKeyUsage. | Minimally expected to be audited as defined in Section 8.7 of the BRs (self-audit). |
| All others | N/A | Minimally expected to be audited as defined in Section 8.7 of the BRs (self-audit). |

\*\* while existing CA certificates trusted by Chrome MAY have EKU values as described in this table, Applicant PKI hierarchies MUST remain [dedicated to only TLS server authentication use cases](#42-promote-use-of-dedicated-tls-server-authentication-pki-hierarchies)

\*\*\* accepted on a discretionary basis

#### 1.4.1. Annual Audits
All Chrome Root Program Participant CAs MUST retain an unbroken, contiguous audit coverage.

Recurring "complete" (i.e., "full", "full system", or "full re-assessment") audits MUST occur at least once every 365 calendar days (or 366 calendar days in a leap year). These audits MUST begin once a CA's key material has been generated and MUST continue until the corresponding root CA's key material has been destroyed or is no longer included in the Chrome Root Store.

#### 1.4.2. Ad-Hoc Audits

The Chrome Root Program may require Chrome Root Program Participants undergo additional ad-hoc audits, including, but not limited to, instances of CA private key destruction or verification of incident remediation.

### 1.5. Reporting and Responding to Incidents

The failure of a Chrome Root Program Participant to meet the commitments of this policy is considered an incident, as is any other situation that may impact the CA's integrity, trustworthiness, or compatibility.

#### 1.5.1. Incident Reports

Chrome Root Program Participants MUST publicly disclose and/or respond to incident reports in [Bugzilla](https://bugzilla.mozilla.org/enter_bug.cgi?product=CA%20Program&component=CA%20Certificate%20Compliance), regardless of perceived impact. Reports MUST be submitted in accordance with the current version of [this](https://www.ccadb.org/cas/incident-report) CCADB incident report format and timelines.

While all Chrome Root Program Participants MAY participate in the incident reporting process, the CA Owner whose corresponding certificate is included in the Chrome Root Store is encouraged to disclose and/or respond to incidents on behalf of the Chrome Root Program Participants included in its PKI hierarchy.

If the Chrome Root Program Participant has not yet publicly disclosed an incident, they MUST notify chrome-root-program [at] google [dot] com and include an initial timeline for public disclosure. Chrome uses the information in the public disclosure as the basis for evaluating incidents.

The Chrome Root Program will evaluate every incident on a case-by-case basis, and will work with the CA Owner to identify ecosystem-wide risks or potential improvements to be made that can help prevent future incidents.

Chrome Root Program Participants MUST be detailed, candid, timely, and transparent in describing their architecture, implementation, operations, and external dependencies as necessary for the Chrome Root Program and the public to evaluate the nature of the incident and the CA Owner's response. When evaluating an incident response, the Chrome Root Program's primary concern is ensuring that browsers, other CA Owners, users, and website developers have the necessary information to identify improvements, and that the Chrome Root Program Participant is responsive to addressing identified issues.

Factors that are significant to the Chrome Root Program when evaluating incidents include (but are not limited to):

- a demonstration of understanding of the [root causes](https://sre.google/sre-book/postmortem-culture/) of an incident,
- a substantive commitment and timeline to changes that clearly and persuasively address the root cause,
- past history by the Chrome Root Program Participant in its incident handling and its follow through on commitments, and,
- the severity of the security impact of the incident.

Due to the incorporation of the Baseline Requirements into CA policy documents, incidents may include a prescribed follow-up action, such as revoking impacted certificates within a certain timeframe. If the Chrome Root Program Participant does not perform the required follow-up actions, or does not perform them in the expected timeframe, the Chrome Root Program Participant MUST file a secondary incident report describing any certificates involved, the expected timeline to complete any follow-up actions, and what changes they are making to ensure they can meet these requirements consistently in the future.

#### 1.5.2. Communicating with Chrome During Incidents

The Chrome Root Program prioritizes and remains committed to promoting public disclosure and discussion of incidents, as they can affect the whole Internet ecosystem, not just Chrome and its users. The Chrome Root Program's sole responsibility when responding to incidents is upholding the safety and security of Chrome's users.

As standard practice, the Chrome Root Program does not:

- discuss ongoing public incident reports privately. We believe using information disclosed to the public as the basis for our response is the most transparent and effective way of upholding the security expectations of Chrome's users, while also ensuring the [factors](#51-incident-reports) that are significant to Chrome are adequately addressed;
- advise on or approve a CA Owner's proposed or planned response to an incident; or
- offer guarantees of specific outcomes in response to the course of action deemed most appropriate by the CA Owner.

### 1.6. Timely and Transparent Communications

At any time, the Chrome Root Program may request additional information from a Chrome Root Program Participant using email or CCADB communications to verify the commitments and obligations outlined in this policy are being met, or as updates to policy requirements are being considered. Chrome Root Program Participants MUST provide the requested information within 14 calendar days unless specified otherwise.

#### 1.6.1. Notification of CA Certificate Issuance

CA Owners included in the Chrome Root Store MUST complete the "Chrome Root Program Notification of CA Certificate Issuance" form, made available by emailing chrome-root-program [at] google [dot] com, at least three (3) weeks before a CA in the corresponding hierarchy issues a CA certificate that:

- extends the Chrome Root Store's trust boundary (i.e., the third-party subject CA Owner is either (a) not explicitly included in the Chrome Root Store at the time of issuance, or (b) is constrained (i.e., SCTNotAfter) and planned for removal), or
- replaces an unrevoked and unexpired CA certificate whose subject certificate CA Owner is not explicitly included in the Chrome Root Store.

Examples of the above use cases include cross-certificates issued to CA Owners not represented in the Chrome Root Store and Externally-operated CA certificates.

Such CA certificates MUST NOT be issued without the expressed approval of the Chrome Root Program.

No other notification or approval is required.

#### 1.6.2. Notification of Procurement, Sale, or other Change Control Events

Chrome Root Program Participants MUST NOT assume trust is transferable.

Where permissible by law, Chrome Root Program Participants MUST notify chrome-root-program [at] google [dot] com at least 30 calendar days before any impending:

- procurements,
- sales,
- changes of ownership or operating control,
- cessations of operations, or
- other change control events involving PKI components that would materially affect the ongoing operations or perceived trustworthiness of a CA certificate included in the Chrome Root Store (e.g., changes to operational location(s), changes to delegated third parties involved in the PKI, etc.) or any Externally-operated CA.

Not limited to the circumstances above, the Chrome Root Program reserves the right to require re-application to the Chrome Root Store.

#### 1.6.3. Industry and Community Forum Engagement

Chrome Root Program Participants are expected to maintain awareness of, and where relevant, actively engage in public discussions concerning CA practices, policy developments, and incidents, within minimally the following public forums:
- [CCADB Public](https://groups.google.com/a/ccadb.org/g/public),
- the CA/Browser Forum [Server Certificate Working Group](https://groups.google.com/a/groups.cabforum.org/g/servercert-wg), [Validation Subcommittee](https://groups.google.com/a/groups.cabforum.org/g/validation), and [Network Security Working Group](https://lists.cabforum.org/mailman/listinfo/netsec) mailing lists, 
- the Bugzilla [CA Certificate Compliance](https://bugzilla.mozilla.org/buglist.cgi?product=CA%20Program&component=CA%20Certificate%20Compliance&bug_status=__open__&list_id=17629668) component, and
- the [Certificate Transparency Policy](https://groups.google.com/a/chromium.org/g/ct-policy) mailing list.
  
Awareness of, and participation in, other key industry and community forums is encouraged.

## 2. Minimum Requirements for Applicant CAs Requesting Inclusion into the Chrome Root Store

The following requirements are effective immediately, unless explicitly stated as otherwise.

### 2.1. PKI Policy Governance and Requirements

Applicants MUST accurately describe the policies and practices of their CA(s) within a single CA policy document that is:

- in the form of a combined CP/CPS.
- freely publicly available for examination.
- available in an authoritative English language version.
- available in either Markdown or AsciiDoc at a location disclosed to the CCADB ([GitHub-Flavored Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github) is preferred).
- except for Externally-operated CAs, authoritative for all CAs included in the corresponding PKI hierarchy.
- focused only on the specific PKI use case of issuing TLS server authentication certificates to websites.
- sufficiently detailed to assess the operations of the CA(s) and the compliance with these expectations and those of the Baseline Requirements, and MUST NOT conflict with either of these requirements.

The immediately above requirements do not prohibit Applicants from maintaining additional policy documents, which may also be considered authoritative by other stakeholders. However, the consolidated policy document made available to the Chrome Root Program MUST NOT conflict with any additional policy documents that might exist for the corresponding PKI hierarchy.

### 2.2. Root CA Key Material Freshness

The Chrome Root Program only accepts CCADB Root Inclusion Requests from Applicant PKI hierarchies with corresponding root CA key material generated within five (5) years of application to the Chrome Root Store.

Applicants MUST submit written evidence to the CCADB identifying the date(s) of the key generation ceremony and an attestation to the Applicant's adherence to the requirements defined in Sections 6.1.1.1 ("CA Key Pair Generation") and 6.2 ("Private Key Protection and Cryptographic Module Engineering Controls") of the Baseline Requirements from a Qualified Auditor using an approved format, in accordance with the table below.

| Audit Scheme | Qualified Auditor Criteria | Report Format Criteria |
|------------- |--------------------------- |----------------------- |
| WebTrust | an [enrolled](https://www.cpacanada.ca/en/business-and-accounting-resources/audit-and-assurance/overview-of-webtrust-services/licensed-webtrust-practitioners-international) WebTrust practitioner | WebTrust "Reporting on Root Key Generation" report |
| ETSI | a [member](https://www.acab-c.com/members/) of the Accredited Conformity Assessment Bodies' Council (ACAB'c) | ACAB'c Key and Certificate Ceremony Audit Attestation Letter |

If key material is not used to issue a self-signed root CA certificate on the same date it was generated, Applicants MUST present written evidence from a Qualified Auditor, attesting that keys were minimally protected in a manner consistent with the requirements defined in Section 6.2 ("Private Key Protection and Cryptographic Module Engineering Controls") of the Baseline Requirements from the time of generation to the time the self-signed certificate was issued. Publicly-accessible links for these documents MUST be disclosed to the CCADB.

### 2.3. Dedicated TLS Server Authentication PKI Hierarchies

The Chrome Root Program will only accept CCADB Root Inclusion Requests from Applicant PKI hierarchies that are dedicated to TLS server authentication certificate issuance.

To qualify as a dedicated TLS server authentication PKI hierarchy under this policy:

1. All corresponding unexpired and unrevoked subordinate CA certificates operated beneath an Applicant root CA certificate MUST:
    -  if disclosed to the CCADB **before June 15, 2025**: include the extendedKeyUsage extension and (a) only assert an extendedKeyUsage purpose of id-kp-serverAuth OR (b) only assert extendedKeyUsage purposes of id-kp-serverAuth and id-kp-clientAuth.
    -  if disclosed to the CCADB **on or after June 15, 2025**: include the extendedKeyUsage extension and only assert an extendedKeyUsage purpose of id-kp-serverAuth.
    -  NOT contain a public key corresponding to any other unexpired or unrevoked certificate that asserts different extendedKeyUsage values.
2. All corresponding unexpired and unrevoked subscriber (i.e., TLS server authentication) certificates MUST include the extendedKeyUsage extension and only assert an extendedKeyUsage purpose of id-kp-serverAuth.

### 2.4. Promote Cryptographic Agility and Resilience

All unexpired and unrevoked subordinate CA certificates included in an Applicant PKI hierarchy MUST be integrated with an automation solution, minimally compliant with either [Section 1.3.3.1.1 ("ACME Solutions")](#13311-acme-solutions) or [Section 1.3.3.1.2 ("Non-ACME Solutions")](#13312-non-acme-solutions). Functionally, this means that every TLS server authentication certificate profile offered by the PKI hierarchy MUST be capable of being issued and renewed using an automation solution. CA Owners MUST attest that this requirement is met for each Baseline Requirements certificate policy OID the corresponding Applicant PKI hierarchy issues through a disclosure in the CCADB on the root certificate record of each CA certificate intending to be included in the Chrome Root Store.

For each Baseline Requirements reserved certificate policy OID an Applicant intends to issue, the Applicant MUST disclose at least one (1) automation solution to the CCADB. For each such OID, the Applicant MUST use a disclosed automation solution to issue "Automation Test Certificates" to demonstrate its automation capabilities. Automation Test Certificates MUST be renewed at least once every 30 calendar days; however, at any point, the Chrome Root Program may request more frequent renewal. At least one (1) valid Automation Test Certificate corresponding to each Baseline Requirements reserved certificate policy OID MUST be served by a publicly accessible website whose URL is disclosed to the CCADB on the corresponding intermediate certificate record. Applicants are encouraged to issue "Short-lived Subscriber Certificates," as [introduced](https://cabforum.org/2023/07/14/ballot-sc-063-v4make-ocsp-optional-require-crls-and-incentivize-automation/) in Version 2.0.1 of the Baseline Requirements, for the Automation Test Certificates.

### 2.5. Annual Audits

Applicant PKI hierarchies MUST provide evidence of at least one (1) complete audit by disclosing the applicable ETSI Audit Attestation Letter(s) or WebTrust Assurance Report(s) to the CCADB before submitting a CCADB Root Inclusion Request to Google Chrome. The initial complete audit SHOULD cover a period of at least 180 calendar days.

For Applicant PKI hierarchies subject of a CCADB Root Inclusion Request submitted to Google Chrome:

-  Except for Externally-operated CAs, when CAs in the hierarchy are assessed against:
    -  **only a single audit scheme** (e.g., all CAs in the hierarchy are only assessed against the WebTrust scheme), they MUST fall under a single audit scope (i.e., represented in a single WebTrust Assurance Report) for the assessed criteria (e.g., (a) WebTrust Principles and Criteria for Certification Authorities, (b) WebTrust Principles and Criteria for Certification Authorities - Network Security, (c) WebTrust Principles and Criteria for Certification Authorities - SSL Baseline, or (d) WebTrust for CA - Extended Validation - SSL).
    -  **multiple audit schemes** (e.g., some CAs are assessed against the WebTrust scheme and others are assessed against the ETSI scheme), all CAs assessed against each respective scheme MUST fall under a single audit scope for that scheme (i.e., all ETSI-assessed CAs are represented in a single ETSI Audit Attestation Letter, and all WebTrust CAs are represented in a single WebTrust Assurance Report) for the assessed criteria.
 
If accepted into the Chrome Root Store, Applicant PKI hierarchies MUST continue this practice for the duration of its inclusion.
