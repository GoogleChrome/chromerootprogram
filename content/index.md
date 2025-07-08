---
title: Chrome Root Program Policy, Version 1.7
---

# Chrome Root Program Policy, Version 1.7

## Last updated: 2025-07-14

Bookmark this page as [https://g.co/chrome/root-policy](https://g.co/chrome/root-policy)

## Table of Contents

- [Introduction](#introduction)
- [Change History](#change-history)
- [Definitions](#definitions)
- [Minimum Requirements for CAs](#minimum-requirements-for-cas)
  - [1. Baseline Requirements](#1-baseline-requirements)
  - [2. Common CA Database](#2-common-ca-database)
  - [3. Chrome Root Program Participant Policies](#3-chrome-root-program-participant-policies)
    - [3.1. Applicant PKI Hierarchies](#31-applicant-pki-hierarchies)
  - [4. Modern Infrastructures](#4-modern-infrastructures)
    - [4.1. Promote use of Modern PKI Hierarchies](#41-promote-use-of-modern-pki-hierarchies)
      - [4.1.1. Root CA Key Material Freshness](#411-root-ca-key-material-freshness)
      - [4.1.2. Root CA Succession Planning](#412-root-ca-succession-planning)
      - [4.1.3. Root CA Term-Limit](#413-root-ca-term-limit)
    - [4.2. Promote use of Dedicated TLS Server Authentication PKI Hierarchies](#42-promote-use-of-dedicated-tls-server-authentication-pki-hierarchies)
      - [4.2.1. Applicant PKI Hierarchies](#421-applicant-pki-hierarchies)
      - [4.2.2. PKI Hierarchies included in the Chrome Root Store](#422-pki-hierarchies-included-in-the-chrome-root-store)
    - [4.3. Promote Cryptographic Agility and Resilience](#43-promote-cryptographic-agility-and-resilience)
      - [4.3.1. Automation Support](#431-automation-support)
        - [4.3.1.1. ACME Solutions](#4311-acme-solutions)
        - [4.3.1.2. Non-ACME Solutions](#4312-non-acme-solutions)
      - [4.3.2. Encouraging use of Automation Solutions](#432-encouraging-use-of-automation-solutions)
    - [4.4. Promote Increased Transparency](#44-promote-increased-transparency)
  - [5. Audits](#5-audits)
    - [5.1. Annual Audits](#51-annual-audits)
    - [5.2. Ad-Hoc Audits](#52-ad-hoc-audits)
  - [6. Reporting and Responding to Incidents](#6-reporting-and-responding-to-incidents)
    - [6.1. Incident Reports](#61-incident-reports)
    - [6.2. Communicating with Chrome During Incidents](#62-communicating-with-chrome-during-incidents)
  - [7. Timely and Transparent Communications](#7-timely-and-transparent-communications)
    - [7.1. Notification of CA Certificate Issuance](#71-notification-of-ca-certificate-issuance)
    - [7.2. Notification of Procurement, Sale, or other Change Control Events](#72-notification-of-procurement-sale-or-other-change-control-events)

## Introduction

Google Chrome relies on Certification Authority systems (herein referred to as "CAs") to issue certificates to websites. Chrome uses these certificates to help ensure the connections it makes on behalf of its users are properly secured. Chrome accomplishes this by verifying that a website's certificate was issued by a recognized CA, while also performing additional evaluations of the HTTPS connection's security properties. Certificates not issued by a CA trusted by Chrome or a user's local settings can cause users to see warnings and error pages.

When making HTTPS connections, Chrome refers to a list of self-signed root certificates from CAs that have demonstrated why continued trust in them is justified. This list is known as a "Root Store." CA certificates included in the [Chrome Root Store](https://g.co/chrome/root-store) are selected on the basis of publicly available and verified information, such as that within the Common CA Database ([CCADB](https://ccadb.org/)), and ongoing reviews by the Chrome Root Program.

The Chrome Root Program Policy below establishes the minimum requirements for CA certificates to be included as trusted in a default installation of Chrome.

### Apply for Inclusion

CA Owners that satisfy the requirements defined in the policy below may apply for self-signed root CA certificate inclusion in the Chrome Root Store using [these](apply-for-inclusion.md) instructions.

### Chrome's Ongoing Commitment to Transport Security

The Chrome Root Program and corresponding policy represent Google's [ongoing commitment](https://transparencyreport.google.com/https/overview?hl=en) to upholding secure and reliable network connections in Chrome.

In support of this commitment, Google, as it deems appropriate and at its sole discretion:

- includes or removes certificates in the Chrome Root Store. The selection and ongoing inclusion of certificates is done to enhance the security of Chrome and promote interoperability. Certificates included in the Chrome Root Store must provide value to Chrome end users that exceeds the risk of their continued inclusion. Certificates that do not provide a broad service to all browser users will not be added to, or may be removed from the Chrome Root Store. Initial and sustained inclusion in the Chrome Root Store is not guaranteed to any CA Owner.
- applies metadata-based [name constraints](https://source.chromium.org/chromium/chromium/src/+/main:net/cert/root_store.proto;drc=7c2b25f6a19cfeeea67f0f43ed33617840bab33d;l=39) to certificates in the Chrome Root Store. These constraints, which may go beyond those in the CA certificates themselves, restrict the use of corresponding TLS server authentication certificates to specific Top-Level Domains (TLDs) and/or Second-Level Domains (SLDs).

Chrome maintains a variety of mechanisms to protect its users from certificates that put their safety and privacy at risk, and is prepared to use them as necessary. A Chrome Root Program Participant's failure to follow the minimum requirements defined in this policy may result in the corresponding certificate's removal from the Chrome Root Store, limitations on Chrome's acceptance of the certificates they issue, or other technical or policy restrictions. Before taking such action, the Chrome Root Program always evaluates the broader context of an individual incident and considers it against the [factors](#51-incident-reports) significant to the Chrome Root Program.

### Moving Forward, Together

The "Moving Forward, Together" initiative envisions a future Internet ecosystem that includes modern, reliable, highly agile, purpose-driven PKIs with an emphasis on automation, simplicity, and security.

Learn more about priorities and initiatives that may influence future versions of this policy [here](moving-forward-together.md). Please note "Moving Forward, Together" is future looking and does not describe normative requirements.

### Additional Information

If you're a Chrome user experiencing a certificate error and need help, please see [this support article](https://support.google.com/chrome/answer/6098869?hl=en).

If you're a website operator, you can learn more about [why HTTPS matters](https://web.dev/why-https-matters/) and how to [secure your site with HTTPS](https://support.google.com/webmasters/answer/6073543). If you've got a question about a certificate you've been issued, please contact the CA that issued it.

If you're responsible for a CA that only issues certificates to your enterprise organization, sometimes called a "private" or "locally trusted" CA, the Chrome Root Program Policy does not apply to or impact your organization's Public Key Infrastructure (PKI) use cases. Enterprise CAs are used for issuing certificates to internal resources like intranet sites or applications that do not directly interact with external users of the public Internet (e.g., a TLS server authentication certificate issued to a corporate intranet site).

Though uncommon, websites can also use certificates to identify clients (e.g., users) connecting to them. Besides ensuring it is well-formed, Chrome passes this type of certificate to the server, which then evaluates and enforces its chosen policy. The policies on this page do not apply to client authentication certificates.

Learn more about the Chrome Root Store and Chrome Certificate Verifier [here](https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/faq.md).

This policy, along with archived versions, is available in Markdown [here](https://github.com/GoogleChrome/chromerootprogram).

## Change History

| Version | Date | Note |
|-------- |----- |----- |
| 1.7 | 2025-07-14 | Updates include, but are not limited to: *(1)* add the ARI RFC numerical identifier, *(2)* remove requirements redundant with CCADB Policy Version 2.0
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
- CA Owners with either (1) a certificate included in the Chrome Root Store or (2) a CA certificate that validates to a certificate included in the Chrome Root Store.

This policy uses the term "Externally-operated CA" to describe a subordinate CA certificate issued where the organization or legal entity in possession or control of the corresponding private key capable of issuing new certificates is not under the sole control of the CA Owner whose certificate is included in the Chrome Root Store.

This policy considers a PKI hierarchy as "dedicated" if it is intended to serve one specific use case, for example, the issuance of TLS server authentication certificates.

## Minimum Requirements for CAs

Chrome Root Program Participants MUST satisfy the requirements defined in this policy, including taking responsibility for ensuring the continued compliance of all corresponding subordinate CAs and delegated third parties participating in the PKI.

The requirements included in this policy are effective immediately, unless explicitly stated as otherwise.

Any questions regarding this policy can be directed to chrome-root-program [at] google [dot] com.

### 1. Baseline Requirements

Chrome Root Program Participants that issue TLS server authentication certificates trusted by Chrome MUST adhere to the latest version of the ["Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates"](https://cabforum.org/baseline-requirements-documents/) ("Baseline Requirements"). The Baseline Requirements are consensus-driven requirements owned by a community of participants represented in the [CA/Browser Forum](https://cabforum.org/) [Server Certificate Working Group](https://cabforum.org/working-groups/server/). No single organization, including Google, has the authority to grant exceptions to the Baseline Requirements.

In some cases, this policy strengthens requirements described in the Baseline Requirements.

### 2. Common CA Database

The Chrome Root Program relies on the [CCADB](https://ccadb.org/) to identify and maintain up-to-date information for Chrome Root Program Participants and the corresponding PKI hierarchies.

Chrome Root Program Participants MUST adhere to the latest version of the [CCADB Policy](https://www.ccadb.org/policy).

In some cases, this policy strengthens requirements described in the CCADB Policy.

### 3. Chrome Root Program Participant Policies

#### 3.1 Applicant PKI Hierarchies

Applicants MUST accurately describe the policies and practices of their CA(s) within a single CA policy document that is:

- in the form of a combined CP/CPS.
- freely publicly available for examination.
- available in an authoritative English language version.
- available in either Markdown or AsciiDoc at a location disclosed to the CCADB ([GitHub-Flavored Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github) is preferred).
- except for Externally-operated CAs, authoritative for all CAs included in the corresponding PKI hierarchy.
- focused only on the specific PKI use case of issuing TLS server authentication certificates to websites.
- sufficiently detailed to assess the operations of the CA(s) and the compliance with these expectations and those of the Baseline Requirements, and MUST NOT conflict with either of these requirements.

The immediately above requirements do not prohibit Applicants from maintaining additional policy documents, which may also be considered authoritative by other stakeholders. However, the consolidated policy document made available to the Chrome Root Program MUST NOT conflict with any additional policy documents that might exist for the corresponding PKI hierarchy.

### 4. Modern Infrastructures

#### 4.1 Promote use of Modern PKI Hierarchies

##### 4.1.1 Root CA Key Material Freshness

The Chrome Root Program only accepts CCADB Root Inclusion Requests from Applicant PKI hierarchies with corresponding root CA key material generated within 5 years of application to the Chrome Root Store.

Applicants MUST submit written evidence to the CCADB identifying the date(s) of the key generation ceremony and an attestation to the Applicant's adherence to the requirements defined in Sections 6.1.1.1 ("CA Key Pair Generation") and 6.2 ("Private Key Protection and Cryptographic Module Engineering Controls") of the Baseline Requirements from a Qualified Auditor using an approved format, in accordance with the table below.

| Audit Scheme | Qualified Auditor Criteria | Report Format Criteria |
|------------- |--------------------------- |----------------------- |
| WebTrust | an [enrolled](https://www.cpacanada.ca/en/business-and-accounting-resources/audit-and-assurance/overview-of-webtrust-services/licensed-webtrust-practitioners-international) WebTrust practitioner | WebTrust "Reporting on Root Key Generation" report |
| ETSI | a [member](https://www.acab-c.com/members/) of the Accredited Conformity Assessment Bodies' Council (ACAB'c) | ACAB'c Key and Certificate Ceremony Audit Attestation Letter |

If key material is not used to issue a self-signed root CA certificate on the same date it was generated, Applicants MUST present written evidence from a Qualified Auditor, attesting that keys were minimally protected in a manner consistent with the requirements defined in Section 6.2 ("Private Key Protection and Cryptographic Module Engineering Controls") of the Baseline Requirements from the time of generation to the time the self-signed certificate was issued. Publicly-accessible links for these documents MUST be disclosed to the CCADB.

##### 4.1.2 Root CA Succession Planning

CA Owners SHOULD request for the replacement of a certificate included in the Chrome Root Store no later than 5 years after the release date of the Chrome Root Store's initial inclusion of the certificate.

Within no more than 90 calendar days after an Applicant CA (i.e., replacement) being first distributed by the Chrome Root Store and as disclosed in the CCADB, the CA Owner MUST have:

1. Issued a cross-certificate from the CA being replaced to the replacement CA; and
2. Transitioned all TLS server authentication certificate issuance from the cross-signing PKI hierarchy to the replacement PKI hierarchy.

The CA certificate being replaced will be removed from the Chrome Root Store upon the absence of unexpired and unrevoked TLS server authentication certificates (excluding test certificates like those disclosed to the CCADB) disclosed to Certificate Transparency (CT) before the date of the Applicant CA (i.e., replacement) being first distributed by the Chrome Root Store.

Due to the existence of the cross-certificate, TLS server authentication certificates issued by the replacement PKI hierarchy will be trusted by default in versions of Chrome relying on the Chrome Root Store, regardless of whether they are capable of receiving updates to the Chrome Root Store.

##### 4.1.3 Root CA Term-Limit

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

To further reduce negative impact to the ecosystem, the Chrome Root Store may temporarily continue to include a root CA certificate past its defined term-limit on a case-by-case basis, if the corresponding CA Owner has submitted a Root Inclusion Request to the CCADB for a replacement root CA certificate at least one year in advance of the approximate removal date.

Other circumstances may lead to the removal of a root CA certificate included in the Chrome Root Store before the completion of its term.

#### 4.2 Promote use of Dedicated TLS Server Authentication PKI Hierarchies

The Chrome Root Store is solely relied upon for TLS server authentication in Chrome; it is not used for any other PKI use case (e.g., TLS client authentication, secure email, code-signing, etc.).

##### 4.2.1 Applicant PKI Hierarchies

The Chrome Root Program will only accept CCADB Root Inclusion Requests from Applicant PKI hierarchies that are dedicated to TLS server authentication certificate issuance.

To qualify as a dedicated TLS server authentication PKI hierarchy under this policy:

1. All corresponding unexpired and unrevoked subordinate CA certificates operated beneath an applicant root CA MUST:
    - when disclosed to the CCADB…
        - **prior to June 15, 2025,** include the extendedKeyUsage extension and (1) only assert an extendedKeyUsage purpose of id-kp-serverAuth OR (2) only assert extendedKeyUsage purposes of id-kp-serverAuth and id-kp-clientAuth.
        -  **on or after June 15, 2025,** include the extendedKeyUsage extension and only assert an extendedKeyUsage purpose of id-kp-serverAuth.
    -  NOT contain a public key corresponding to any other unexpired or unrevoked certificate that asserts different extendedKeyUsage values.
2. All corresponding unexpired and unrevoked subscriber (i.e., TLS server authentication) certificates MUST include the extendedKeyUsage extension and only assert an extendedKeyUsage purpose of id-kp-serverAuth.

##### 4.2.2 PKI Hierarchies included in the Chrome Root Store

To align all PKI hierarchies included in the Chrome Root Store on the principle of serving only TLS server authentication use cases, the Chrome Root Program will "phase-out" multi-purpose roots from the Chrome Root Store.

**Beginning** **June 15, 2026**, the Chrome Root Program will set an [SCTNotAfter constraint](https://source.chromium.org/chromium/chromium/src/+/main:net/cert/root_store.proto;drc=a783c3bab474ff68e675e2753f91c92ca817e072;l=15?q=f:root_store.proto&ss=chromium) on root CA certificates included in the Chrome Root Store for any PKI hierarchy found in violation of the below requirements. Once the constraint is applied, Chrome will no longer trust any certificate chaining to the root by default if it is issued more than 90 calendar days following the violation's detection.

1. All corresponding unexpired and unrevoked subordinate CA certificates operated beneath an existing root included in the Chrome Root Store MUST:
    -  when disclosed to the CCADB…
        -  **prior to June 15, 2026,** include the extendedKeyUsage extension and (1) only assert an extendedKeyUsage purpose of id-kp-serverAuth OR (2) only assert extendedKeyUsage purposes of id-kp-serverAuth and id-kp-clientAuth.
        -  **on or after June 15, 2026,** include the extendedKeyUsage extension and only assert an extendedKeyUsage purpose of id-kp-serverAuth.
    -  NOT contain a public key corresponding to any other unexpired or unrevoked certificate that asserts different extendedKeyUsage values.
2. All corresponding unexpired and unrevoked subscriber certificates issued on or after **June 15, 2026** MUST include the extendedKeyUsage extension and only assert an extendedKeyUsage purpose of id-kp-serverAuth.

**Before** **June 15, 2026**, CA Owners with a CA included in the Chrome Root Store whose corresponding PKI hierarchy does not adhere to the above requirements MAY, at their own discretion:

1. Apply with a new dedicated TLS server authentication PKI hierarchy (recommended to be completed **before** **September 15, 2025**).
2. Convert a "multi-purpose" root included in the Chrome Root Store to be dedicated to TLS server authentication by either revoking and/or re-issuing certificates that do not satisfy the above requirements.
3. Request for the removal of non-TLS server authentication hierarchies from the Chrome Root Store.
4. Pursue other solutions as they deem appropriate and compliant with this policy.

The subsequently constrained multi-purpose root CA certificate(s) will be scheduled for removal from the Chrome Root Store upon the absence of unexpired and unrevoked TLS server authentication certificates (excluding test certificates like those disclosed to the CCADB) disclosed to CT **before** **June 15, 2026**.

To reduce negative impact to the ecosystem, the Chrome Root Store may temporarily continue to include a multi-purpose root CA certificate in the Chrome Root Store without an SCTNotAfter constraint on a case-by-case basis, but only if the corresponding CA Owner has submitted a Root Inclusion Request to the CCADB for a replacement root CA certificate **before June 15, 2026**.

#### 4.3 Promote Cryptographic Agility and Resilience

##### 4.3.1 Automation Support

The Chrome Root Program only accepts CCADB Root Inclusion Requests from Applicant PKI hierarchies that support at least one automated solution for certificate issuance and renewal for each Baseline Requirements certificate policy OID (i.e., IV, DV, OV, EV) the corresponding hierarchy issues.

This requirement does not:

- Prohibit Applicant PKI hierarchies from supporting "non-automated" methods of certificate issuance and renewal.
- Require website operators to rely on the automated solution(s) for certificate issuance and renewal.

The automated solution MUST minimize "hands-on" input required from humans during certificate issuance and renewal. Acceptable "hands-on" input from humans includes initial software installation and configuration, applying software updates, and updating subscriber account information as needed. Routine certificate issuance and renewal SHOULD NOT involve human input except as needed for identity or business document verification related to IV, OV, or EV certificate issuance.

For each Baseline Requirements certificate policy OID the corresponding hierarchy issues, the Applicant MUST use its automated solution to issue valid test TLS server authentication certificates (i.e., "Automation Test Certificates") intended to demonstrate its automation capabilities to the Chrome Root Program. Valid Automation Test Certificates MUST be renewed at least once every 30 calendar days, however, at any point, the Chrome Root Program may request more frequent renewal. Automation Test Certificates must be served by a publicly accessible website whose URL is disclosed to the CCADB in a Root Inclusion Request. CA Owners are encouraged to issue "Short-lived Subscriber Certificates," as [introduced](https://cabforum.org/2023/07/14/ballot-sc-063-v4make-ocsp-optional-require-crls-and-incentivize-automation/) in Version 2.0.1 of the Baseline Requirements, for the Automation Test Certificates.

If at any point a self-signed root CA certificate is accepted into the Chrome Root Store and the CA Owner intends to issue a Baseline Requirements certificate policy OID not previously disclosed to the Chrome Root Program, the requirements in this section MUST be satisfied before issuing certificates containing the OID to Subscribers from the corresponding hierarchy, with the exception of Automation Test Certificates.

###### 4.3.1.1 ACME Solutions

Applicant PKI hierarchies SHOULD support the Automatic Certificate Management Environment (ACME) protocol. If ACME is supported by the Applicant:

-  The CA Owner MUST disclose to the CCADB an ACME endpoint (i.e., directory URL) accessible to the Chrome Root Program for each Baseline Requirements certificate policy OID the corresponding hierarchy issues (i.e., IV, DV, OV, EV).
- Each endpoint MUST support the following capabilities, as specified in [RFC 8555](https://www.rfc-editor.org/rfc/rfc8555):
    - keyChange
    - newAccount
    - newNonce
    - newOrder
    - revokeCert
- Each Applicant PKI hierarchy's endpoint's corresponding issuing CA(s) MUST support Certification Authority Authorization (CAA) Record Extensions for Account URI and ACME Method Binding, as specified in [RFC 8657](https://www.rfc-editor.org/rfc/rfc8657).
- Applicant PKI hierarchies supporting the ACME protocol MUST support ACME Renewal Information (ARI, [RFC 9773](https://datatracker.ietf.org/doc/rfc9773/)).
- ACME endpoints SHOULD be publicly accessible.
- Each endpoint SHOULD be hosted using an appropriate and readily accessible online means that is available on a 24x7 basis.

###### 4.3.1.2 Non-ACME Solutions

While ACME support is encouraged, Applicant PKI hierarchies MAY support other automated solutions so long as the following characteristics are verifiably demonstrated to the Chrome Root Program. The CA Owner MUST disclose to the CCADB publicly available information that describes the other automated solution capability for each Baseline Requirements certificate policy OID that the corresponding hierarchy issues and how a Subscriber can leverage its benefits.

- The automated solution MUST:
    - generate a new key pair for each certificate request by default.
    - generate and submit a Certificate Signing Request (CSR).
    - support automated domain control validation (i.e., the automated solution automatically places the Request Token or Random Value in the appropriate location without "hands-on" input from humans, comparable to how ACME clients function), using at least one of the following methods from the Baseline Requirements:
        - DNS Change (Section 3.2.2.4.7)
        - Agreed‑Upon Change to Website v2 (Section 3.2.2.4.18)
    - support automated retrieval of the issued certificate (i.e., the automated solution downloads a copy of the certificate to a well-known location without "hands-on" input from humans, comparable to how ACME clients function).
    - be sufficiently detailed in a completed "Automated Solution Assessment" form by requesting a copy from chrome-root-program [at] google [dot] com.
    - support comparable features as described in [RFC 8657](https://www.rfc-editor.org/rfc/rfc8657) to restrict issuance capabilities to a specific CA account(s) using the "accounturi" CAA parameter and to restrict permitted domain validation methods using the "validationmethods" CAA parameter.
    - support and/or request certificate revocation.
    - support comparable features as described by ACME Renewal Information (ARI, [RFC 9773](https://datatracker.ietf.org/doc/rfc9773/)).
- The automated solution SHOULD:
    - support automated deployment (i.e., installation and configuration) of the issued certificate without "hands-on" input from humans (comparable to how ACME clients function).

##### 4.3.2 Encouraging use of Automation Solutions

The following requirements are intended to promote use of automation solutions to increase agility and improve the [security](https://zanema.com/papers/imc23_stale_certs.pdf) and resilience of the Internet ecosystem, while recognizing that at the moment, not all subscriber use cases can be addressed using automation.

For Applicant PKI hierarchies subject of a CCADB Root Inclusion Request submitted **on or after September 15, 2025**, the following requirements apply:

- TLS server authentication certificates SHOULD NOT exceed 90 calendar days.
- The period for domain control validation data reuse SHOULD NOT exceed 90 calendar days.
- Due to (1) limitations in offering support for automation and (2) these methods offering a weak binding between request authorization and the demonstrated control over the domain(s) appearing in the requested certificate, TLS server authentication certificates SHOULD NOT rely on the following domain validation methods as defined by the Baseline Requirements:
    - 3.2.2.4.4 Constructed Email to Domain Contact
    - 3.2.2.4.13 Email to DNS CAA Contact
    - 3.2.2.4.14 Email to DNS TXT Contact
    - 3.2.2.4.16 Phone Contact with DNS TXT Record Phone Contact
    - 3.2.2.4.17 Phone Contact with DNS CAA Phone Contact
    - 3.2.2.5.2 Email, Fax, SMS, or Postal Mail to IP Address Contact
    - 3.2.2.5.5 Phone Contact with IP Address Contact

In cases where the above requirements cannot be met, CA Owners are encouraged to collect and share the corresponding subscriber use cases and affected technologies with chrome-root-program [at] google [dot] com on a quarterly basis in a format of their choosing to support the Chrome Root Program in better understanding blockers and opportunities for ecosystem improvement.

#### 4.4 Promote Increased Transparency

Within 24 hours of issuance, Chrome Root Program Participants SHOULD log final certificates to at least one CT log [usable](https://googlechrome.github.io/CertificateTransparency/log_list.html) in Chrome at the time of issuance.

Applicants MUST log pre-certificates and final certificates to at least one "Test" CT log disclosed [here](https://www.gstatic.com/ct/log_list/v3/all_logs_list.json) (i.e., log type = "test") until eligible for logging in logs usable in Chrome at the time of issuance (e.g., due to being accepted by a publicly-trusted root store operator or due to the existence of a cross-certificate issued from a publicly-trusted root CA).

### 5. Audits

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

#### 5.1 Annual Audits
All Chrome Root Program Participant CAs MUST retain an unbroken, contiguous audit coverage.

Recurring "complete" (i.e., "full", "full system", or "full re-assessment") audits MUST occur at least once every 365 calendar days (or 366 calendar days in a leap year). These audits MUST begin once a CA's key material has been generated and MUST continue until the corresponding root CA's key material has been destroyed or is no longer included in the Chrome Root Store.

Applicant PKI hierarchies MUST provide evidence of at least one complete audit by disclosing the applicable ETSI Audit Attestation Letter(s) or WebTrust Assurance Report(s) to the CCADB prior to submitting a CCADB Root Inclusion Request to Google Chrome. The initial complete audit SHOULD cover a period of at least 180 calendar days.

For Applicant PKI hierarchies subject of a CCADB Root Inclusion Request submitted to Google Chrome **on or after September 15, 2025**:

-  Except for Externally-operated CAs, when CAs in the hierarchy are assessed against:
    -  **only a single audit scheme** (e.g., all CAs in the hierarchy are only assessed against the WebTrust scheme), they MUST fall under a single audit scope (i.e., represented in a single WebTrust Assurance Report) for the assessed criteria (e.g., (1) WebTrust Principles and Criteria for Certification Authorities, (2) WebTrust Principles and Criteria for Certification Authorities - Network Security, (3) WebTrust Principles and Criteria for Certification Authorities - SSL Baseline, or (4) WebTrust for CA - Extended Validation - SSL).
    -  **multiple audit schemes** (e.g., some CAs are assessed against the WebTrust scheme and others are assessed against the ETSI scheme), all CAs assessed against each respective scheme MUST fall under a single audit scope for that scheme (i.e., all ETSI-assessed CAs are represented in a single ETSI Audit Attestation Letter, and all WebTrust CAs are represented in a single WebTrust Assurance Report) for the assessed criteria.

#### 5.2 Ad-Hoc Audits

The Chrome Root Program may require Chrome Root Program Participants undergo additional ad-hoc audits, including, but not limited to, instances of CA private key destruction or verification of incident remediation.

### 6. Reporting and Responding to Incidents

The failure of a Chrome Root Program Participant to meet the commitments of this policy is considered an incident, as is any other situation that may impact the CA's integrity, trustworthiness, or compatibility.

#### 6.1 Incident Reports

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

#### 6.2 Communicating with Chrome During Incidents

The Chrome Root Program prioritizes and remains committed to promoting public disclosure and discussion of incidents, as they can affect the whole Internet ecosystem, not just Chrome and its users. The Chrome Root Program's sole responsibility when responding to incidents is upholding the safety and security of Chrome's users.

As standard practice, the Chrome Root Program does not:

- discuss ongoing public incident reports privately. We believe using information disclosed to the public as the basis for our response is the most transparent and effective way of upholding the security expectations of Chrome's users, while also ensuring the [factors](#51-incident-reports) that are significant to Chrome are adequately addressed;
- advise on or approve a CA Owner's proposed or planned response to an incident; or
- offer guarantees of specific outcomes in response to the course of action deemed most appropriate by the CA Owner.

### 7. Timely and Transparent Communications

At any time, the Chrome Root Program may request additional information from a Chrome Root Program Participant using email or CCADB communications to verify the commitments and obligations outlined in this policy are being met, or as updates to policy requirements are being considered. Chrome Root Program Participants MUST provide the requested information within 14 calendar days unless specified otherwise.

#### 7.1 Notification of CA Certificate Issuance

CA Owners included in the Chrome Root Store MUST complete the "Chrome Root Program Notification of CA Certificate Issuance" form, made available by emailing chrome-root-program [at] google [dot] com, at least 3 weeks before a CA in the corresponding hierarchy issues a CA certificate that:

- extends the Chrome Root Store's trust boundary (i.e., the third-party subject CA Owner is either (1) not explicitly included in the Chrome Root Store at the time of issuance, or (2) is constrained (i.e., SCTNotAfter) and planned for removal), or
- replaces an unrevoked and unexpired CA certificate whose subject certificate CA Owner is not explicitly included in the Chrome Root Store.

Examples of the above use cases include cross-certificates issued to CA Owners not represented in the Chrome Root Store and Externally-operated CA certificates.

Such CA certificates MUST NOT be issued without the expressed approval of the Chrome Root Program.

No other notification or approval is required.

#### 7.2 Notification of Procurement, Sale, or other Change Control Events

Chrome Root Program Participants MUST NOT assume trust is transferable.

Where permissible by law, Chrome Root Program Participants MUST notify chrome-root-program [at] google [dot] com at least 30 calendar days before any impending:

- procurements,
- sales,
- changes of ownership or operating control,
- cessations of operations, or
- other change control events involving PKI components that would materially affect the ongoing operations or perceived trustworthiness of a CA certificate included in the Chrome Root Store (e.g., changes to operational location(s), changes to delegated third parties involved in the PKI, etc.) or any Externally-operated CA.

Not limited to the circumstances above, the Chrome Root Program reserves the right to require re-application to the Chrome Root Store.
