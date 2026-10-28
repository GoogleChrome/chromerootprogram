---
title: Chrome Quantum-resistant Root Program Policy, Version 0.4.0
---
# [DRAFT] Chrome Quantum-resistant Root Program Policy, Version 0.4.0

## Last updated: 2026-10-28

## Table of Contents

- [Introduction](#introduction)
  - [Preparing and Applying for Inclusion](#preparing-and-applying-for-inclusion)
  - [Chrome's Ongoing Commitment to Transport Security](#chromes-ongoing-commitment-to-transport-security)
- [Change History](#change-history)
- [Definitions](#definitions)
- [1. Participation in the Root Store](#1-participation-in-the-root-store)
  - [1.1. Eligibility](#11-eligibility)
  - [1.2. Beneficial Ownership](#12-beneficial-ownership)
  - [1.3. Operator Independence](#13-operator-independence)
  - [1.4. Facilities and Geographic Diversity](#14-facilities-and-geographic-diversity)
- [2. Minimum Requirements for MTC CA Operators](#2-minimum-requirements-for-mtc-ca-operators)
  - [2.1. Public General Availability](#21-public-general-availability)
    - [2.1.1. Disclosures Manifest](#211-disclosures-manifest)
  - [2.2. Service Uptime and Maintenance Notifications](#22-service-uptime-and-maintenance-notifications)
  - [2.3. PKI Policy Governance](#23-pki-policy-governance)
    - [2.3.1. CA/Browser Forum TLS Server Authentication Baseline Requirements](#231-cabrowser-forum-tls-server-authentication-baseline-requirements)
    - [2.3.2. MTC CA Operator Policies](#232-mtc-ca-operator-policies)
  - [2.4. Certificate Issuance Lifecycle and Profiles](#24-certificate-issuance-lifecycle-and-profiles)
    - [2.4.1. Domain Control Validation](#241-domain-control-validation)
    - [2.4.2. Automation Support](#242-automation-support)
    - [2.4.3. Certificate and CRL Profiles](#243-certificate-and-crl-profiles)
      - [2.4.3.1. MTC CA Cosigner Certificate Profile](#2431-mtc-ca-cosigner-certificate-profile)
      - [2.4.3.2. Subscriber TLS Server Authentication Certificate Profile](#2432-subscriber-tls-server-authentication-certificate-profile)
      - [2.4.3.3. CRL Profile](#2433-crl-profile)
    - [2.4.4. Linting](#244-linting)
    - [2.4.5. Criteria for Chrome Usability](#245-criteria-for-chrome-usability)
  - [2.5. MTC CA Issuance Log](#25-mtc-ca-issuance-log)
    - [2.5.1. Issuance Log Operations](#251-issuance-log-operations)
      - [2.5.1.1. Technical Specifications](#2511-technical-specifications)
      - [2.5.1.2. Issuance Log Mirroring and Continuity](#2512-issuance-log-mirroring-and-continuity)
      - [2.5.1.3. Data Retention and Log Pruning](#2513-data-retention-and-log-pruning)
      - [2.5.1.4. Service Availability and Reporting](#2514-service-availability-and-reporting)
    - [2.5.2. Issuance Log Cryptographic Integrity](#252-issuance-log-cryptographic-integrity)
  - [2.6. CA Cosigners](#26-ca-cosigners)
    - [2.6.1. CA Cosigner Key Generation](#261-ca-cosigner-key-generation)
    - [2.6.2. CA Cosigner Key Use](#262-ca-cosigner-key-use)
    - [2.6.3. CA Cosigner Key Lifecycle and Rotation](#263-ca-cosigner-key-lifecycle-and-rotation)
  - [2.7. Oversight and Incident Reporting](#27-oversight-and-incident-reporting)
    - [2.7.1. Annual Third Party Audits](#271-annual-third-party-audits)
    - [2.7.2. Timely and Transparent Communications](#272-timely-and-transparent-communications)
    - [2.7.3. Publicly Reporting on Incidents](#273-publicly-reporting-on-incidents)
      - [2.7.3.1. Incident Reports](#2731-incident-reports)
      - [2.7.3.2. Communicating with Chrome During Incidents](#2732-communicating-with-chrome-during-incidents)
- [3. Minimum Requirements for Mirroring Operators](#3-minimum-requirements-for-mirroring-operators)
  - [3.1. Mirroring Cosigner Key Generation and Use](#31-mirroring-cosigner-key-generation-and-use)
  - [3.2. Mirroring Cosigner Operations](#32-mirroring-cosigner-operations)
    - [3.2.1. Technical Specifications](#321-technical-specifications)
    - [3.2.2. Log Discovery and Synchronization](#322-log-discovery-and-synchronization)
    - [3.2.3. Cosigning Timeliness](#323-cosigning-timeliness)
    - [3.2.4. Data Retention and Log Pruning](#324-data-retention-and-log-pruning)
    - [3.2.5. Service Availability and Reporting](#325-service-availability-and-reporting)
    - [3.2.6. Log Consistency](#326-log-consistency)
  - [3.3. Mirroring Cosigner States](#33-mirroring-cosigner-states)
  - [3.4. Mirroring Cosigner Lifecycle and Rotation](#34-mirroring-cosigner-lifecycle-and-rotation)
- [References](#references)

## **Introduction**

The Chrome Quantum-resistant Root Program (CQRP) establishes the minimum requirements for [Merkle Tree Certificate](https://datatracker.ietf.org/doc/html/draft-ietf-plants-merkle-tree-certs-07) Certification Authorities (referred to as "MTC CAs") to be trusted by default in Chrome.

As [announced](https://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html) in February 2026, Chrome will not add traditional X.509 certificates containing post-quantum cryptography to the Chrome Root Store. Instead, the Chrome Quantum-resistant Root Store (CQRS) relies entirely on MTC CAs to decouple connection security strength from TLS handshake payload size while integrating transparency directly into the issuance process.

This policy does not apply to or impact CAs that are not trusted by default in Chrome and only issue certificates to an enterprise organization (sometimes called "enterprise," "private," or "locally trusted" CAs used for internal resources like corporate intranet sites or applications that do not directly interact with external users of the public Internet). For private PKI use cases, Chrome [supports](https://chromestatus.com/feature/5174590524489728) traditional X.509 certificates and trust anchors using ML-DSA in TLS 1.3 as of Chrome 150.

Unlike a traditional root store consisting of X.509 certificates acting as trust anchors for certificate chain validation and accompanying metadata, the CQRS encompasses both MTC CAs (i.e., TLS server authentication certificate issuers responsible for domain control validation and Merkle Tree generation) and Mirrors (i.e., entities responsible for replicating and cosigning log views to guarantee transparency and split-view resistance). The complete list of MTC CAs and Mirroring Cosigners included in the CQRS is published in [https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json), with keys provided in [https://www.gstatic.com/mtcs/cosigners/v1/cosigners.pem](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.pem).

> [!NOTE]
> `cosigners.json` and `cosigners.pem` are published solely for Chrome, CQRS operators, and monitors, and may contain keys that are not unconditionally trusted by Chrome. They MUST NOT be used for MTC validation in non-Chrome TLS clients, as unauthorized reliance endangers third-party users, Chrome users, and the broader ecosystem. Google provides no SLA or stability guarantees for unauthorized users and may modify these files in any way without notice; permitted consumers should cache recent versions locally.

The CQRS and corresponding policy are distinct from the existing:

* [Chrome Root Store](https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/root_store.md),  
* Chrome Root Program [Policy](https://googlechrome.github.io/chromerootprogram/crp/policy/),  
* Chrome Certificate Transparency (CT) [Policy](https://googlechrome.github.io/CertificateTransparency/ct_policy.html),  
* Chrome CT Log [Policy](https://googlechrome.github.io/CertificateTransparency/log_policy.html), and  
* Chrome CT Log List Usage [Policy](https://googlechrome.github.io/CertificateTransparency/log_lists.html).

Inclusion in the Chrome Root Store does not guarantee admission into the CQRS, nor is inclusion in the Chrome Root Store a prerequisite for inclusion in the CQRS.

Because this area is evolving rapidly, this policy will change over time. Stakeholders can expect an emphasis on **security, simplicity, predictability, transparency,** and **resilience.** To respond effectively to emerging security risks and standards, Google reserves the right to modify this policy as necessary. Although Google intends to provide reasonable notice for policy updates, advance notice is not guaranteed. Participants in the CQRS are expected to maintain the operational agility and technical capabilities required to implement policy changes without disrupting ecosystem availability. Any questions regarding this policy can be directed to chrome-quantum-resistant-root-program [at] google [dot] com.

### **Preparing and Applying for Inclusion**

Organizations are welcome to apply for inclusion in the CQRS as an MTC CA Operator if they meet the minimum requirements detailed in this policy and follow the submission guidelines detailed in [Preparing and Applying for Inclusion](https://googlechrome.github.io/chromerootprogram/cqrp/apply/).

### **Chrome's Ongoing Commitment to Transport Security**

The CQRP is purpose-driven and designed to serve Chrome users' security needs. Its existence and this corresponding policy represent Google's [ongoing commitment](https://transparencyreport.google.com/https/overview?hl=en) to upholding secure and reliable network connections in Chrome.

In support of this commitment, Google, as it deems appropriate and at its sole discretion, includes or removes MTC CA and Mirroring Cosigners in the CQRS. The selection and ongoing inclusion of these operators is done to enhance the security of Chrome. Inclusion in the root store, both initially and sustained, is not guaranteed to any CQRS Applicant or MTC CA Operator.

## **Change History**

| Version | Date | Note |
| :---- | :---- | :---- |
| 0.4.0 (RC 1.0.0) | 2026.10.28 | Fourth draft release with additional feedback considered and updated to align with draft-ietf-plants-merkle-tree-certs-07. This draft is considered Release Candidate (RC) Version 1.0.0. |
| 0.3.0 | 2026.08.14 | Third draft release with additional feedback considered, a reorganization of sections, and new subsection headers. |
| 0.2.0 | 2026.06.17 | Second draft release with feedback considered. |
| 0.1.0 | 2026.05.14 | Initial draft release for feedback. |

## **Definitions**

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) when, and only when, they appear in all capitals, as shown here.

**Note:** This policy applies BCP 14 keywords as defined above. Separately, and as a matter of program intent, the CQRP often uses SHOULD in part to phase in requirements whose immediate mandate would outpace available tooling or ecosystem maturity.

**CQRS Applicant**: A legal entity that has an open inclusion request submitted to Google Chrome in the [Chromium Issues Tracker](https://issues.chromium.org/issues/new?component=2114629&template=2386551).

**Inconsistent Merkle Tree View (or Split-View)**: A state where an MTC CA's issuance log or a Mirroring Cosigner's view of an issuance log presents different, conflicting versions of its log history to various parties (e.g., cosigners, relying parties, or monitors).

**Key Sunset**: The process by which Chrome deprecates and phases out default trust in an MTC CA Cosigner Key. To safely sunset a key and prevent retroactive issuance, Chrome establishes a Key Sunset Date technically enforced in client configurations through bounded minimum and maximum certificate serial numbers and log instances. Certificates linked to inclusion proofs outside this explicitly bounded window will not be accepted by Chrome clients. This is analogous to the SCTNotAfter feature used by the Chrome Root Store to gradually phase out trust in CA key material.

**Mirroring Operator**: A legal entity included in the CQRS that maintains a synchronized copy of MTC CA issuance logs (i.e., a mirror) and possesses or controls the private key(s) capable of cosigning views of those issuance logs.

**MTC CA Operator**: A legal entity included in the CQRS that possesses or controls the private key(s) capable of issuing Subscriber certificates and generating checkpoints for the associated issuance log. All MTC CA Operators are also Mirroring Operators.

**Planned Maintenance**: A service interruption announced on the operator's public status page no less than 48 hours before it begins, and limited to the duration announced. Any other service interruption, including any portion of a maintenance window extending beyond its announced end time, is considered "unplanned."

## **1. Participation in the Root Store**

### **1.1. Eligibility**

Initial eligibility to [apply for inclusion](https://googlechrome.github.io/chromerootprogram/cqrp/apply/) in the CQRS is restricted to [organizations](https://certificate.transparency.dev/logs/) responsible for operating a "[usable](https://googlechrome.github.io/CertificateTransparency/log_states.html)" Certificate Transparency (CT) Log prior to February 1, 2026. These organizations have already demonstrated the operational excellence and high-availability infrastructure required to run global security services that underpin default TLS connections in Chrome. Since MTC technology shares significant architectural similarities with CT, these operators are uniquely qualified to ensure MTCs are able to get off the ground quickly and successfully.

> [!NOTE]
> A future update to this policy is expected to establish requirements and open applications for additional MTC CA Operators (i.e., organizations that do not satisfy the above initial eligibility restrictions). Once eligible to apply, these prospective MTC CA Operators will be required to minimally first apply as a Mirroring Operator and demonstrate operational capability and high-availability infrastructure reliability by successfully operating a trusted Mirroring Cosigner in the CQRS, as defined by this policy, for a specified period before their CA Cosigners will be considered for inclusion in the CQRS.

### **1.2. Beneficial Ownership**

MTC Operators and CQRS Applicants MUST provide comprehensive ownership disclosures so the CQRP can fully evaluate the entity's ultimate beneficial corporate ownership, parent entities, and corporate control structure. In its public Repository (as defined within the CA/Browser Forum "[Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates](https://cabforum.org/baseline-requirements-documents/)" (Baseline Requirements)), the operator MUST disclose:

* Legal Entity Identification: Full legal name, entity type, jurisdiction of incorporation, official corporate registration number, and registered principal business address.
* Corporate Hierarchy: Full legal name, jurisdiction, and corporate registration number of the ultimate parent entity, along with a complete listing of all intermediate parent and subsidiary entities connecting the operator to its ultimate parent.
* Beneficial Ownership: Legal name, jurisdiction of incorporation, and exact percentage of equity or voting interest for any legal entity directly or indirectly holding a 25% or greater ownership or voting control interest in the operator.

Operators MUST continuously maintain transparent ownership records and update their disclosure for any material changes in legal structure, ultimate corporate control, or beneficial ownership.

When an operator intends to transfer ownership, trust in the new operator is not automatically transferred. To provide sufficient time to evaluate the security, operational, and trustworthiness implications of the new controlling entity prior to the transfer of trust, MTC CA Operators MUST, where permissible by law, notify mtcs [at] chromium [dot] org at least 30 calendar days before any impending:

* changes in ownership resulting in a transfer of effective control, or changes in operating control,
* cessations of operations, or  
* other change control events involving components that would materially affect the ongoing operations or perceived trustworthiness of CA Cosigner or Mirroring Cosigner Keys included in the CQRS (e.g., changes to operational location(s), etc.).

Not limited to the circumstances above, the CQRP reserves the right to require re-application to the CQRS.

### **1.3. Operator Independence**

To prevent single points of failure, every entity participating in the CQRS MUST be completely distinct from all other operators in the CQRS. Organizational independence is maintained through transparency, continuous monitoring, and ongoing re-evaluation processes.

For the purposes of this policy, an entity is "distinct" from another operator if and only if they are separate legal, corporate, and operational entities that share no common ownership, ultimate corporate control, parent companies, administrative access, or control over cosigner key material.

### **1.4. Facilities and Geographic Diversity**

To provide baseline assurance of physical, environmental, and operational security, all MTC CA Operator infrastructure MUST (and Mirroring Operator infrastructure SHOULD) be hosted in facilities that maintain an active ISO/IEC 27001 certification, AICPA SOC 2 Type II / SOC 3 attestation, or an equivalent security framework audited at least annually by an independent third party. Operators MAY satisfy this requirement through the inherited facility certifications of their underlying cloud or colocation provider.

When an operator deploys infrastructure across multiple physical locations, those locations SHOULD be distributed across diverse geographic regions (e.g., North America, Europe, Asia-Pacific) to prevent regional single points of failure.

Specific only to MTC CA Operator infrastructure:

* Components responsible for Subscriber certificate issuance and landmark generation, as detailed in Section 2. ("Minimum Requirements for MTC CA Operators"), SHOULD be distributed across at least 2 distinct Regional Internet Registries.  
* Because this policy strictly bounds the total number of Active CA Cosigner Keys an MTC CA Operator can maintain at any given time, as detailed in Section 2.6.2. ("CA Cosigner Key Use"), MTC CA Operators MUST strategically manage their key allowance to accommodate any current or future regional deployment needs. Additional CA Cosigner Key allowances will not be granted solely to support regional deployments or bypass key limits in Chrome.

Inclusion or usability standards will not be reduced solely to satisfy geographic diversity preferences.

## **2. Minimum Requirements for MTC CA Operators**

### **2.1. Public General Availability**

To ensure the CQRS supports the diverse needs of the web, MTC CA Operators MUST offer Subscriber certificate issuance as a service generally available to the public. An issuance service is considered generally available if it is open to any qualifying Subscriber under publicly documented criteria, and is not restricted to an operator's internal infrastructure or corporate affiliates. This requirement does not prohibit the MTC CA Operator from also offering other certificate issuance services that are not generally available to the public, provided those services do not negatively impact the availability of the CA Cosigner(s) trusted by default in Chrome. To manage risk and ensure system stability during initial deployment, upon initial inclusion in the CQRS, an MTC CA Operator MAY conduct a phased rollout for up to 60 calendar days, during which certificate issuance MAY be restricted to a controlled set of Subscribers. Following the conclusion of this period, the MTC CA Operator MUST transition the service to full public general availability.

To ensure that inclusion in the CQRS provides equitable public value, MTC CA Operators MUST NOT condition the acceptance of a certificate request or the issuance of a certificate on the Subscriber’s use of other services, products, or platforms offered by the MTC CA Operator or its affiliates (e.g., hosting or CDN services). This requirement does not prohibit the MTC CA Operator from requiring the use of its own platform or account management services for the purpose of authentication, quota management, or abuse prevention, provided these access mechanisms are made generally available to the public.

#### **2.1.1. Disclosures Manifest**

MTC CA Operators MUST create, publish, and continuously maintain an [mtc-disclosures.json](https://github.com/GoogleChrome/chromerootprogram/blob/main/content/cqrp/disclosures/mtc-disclosures.schema.json) ([example](https://github.com/GoogleChrome/chromerootprogram/blob/main/content/cqrp/disclosures/mtc-disclosures.json)). The manifest MUST:

* be hosted at a publicly accessible URL within the operator’s public Repository;
* conform to the latest version of the MTC Disclosures schema within 14 days of the publication thereof;
* accurately specify all mandatory global disclosure URLs (including the operator’s public Repository, legal entity and beneficial ownership disclosures, operational status page, and facility security certifications);
* accurately specify all key-specific disclosure URLs for each CA Cosigner Key included in the CQRS; and
* be updated within 14 calendar days of any material change to any contained URL or disclosure metadata.

### **2.2. Service Uptime and Maintenance Notifications**

The MTC CA Operator SHOULD maintain continuous availability of its Subscriber certificate issuance services. As the ecosystem relies on automated renewal of certificates, and prolonged downtime risks widespread TLS breakage for website operators, the MTC CA Operator MUST NOT experience any single, unplanned service outage exceeding 24 consecutive hours, during which certificate issuance and management is unavailable to Subscribers through any of the operator’s endpoints. All Planned Maintenance MUST be publicly announced, minimally on the MTC CA Operator's public status page (described below).

MTC CA Operators MUST maintain a freely accessible, public status page that reports the current operational health and availability for all MTC services. The status page SHOULD:

* be hosted on infrastructure operationally independent of the CA’s primary issuance endpoints to ensure availability during primary system outages;
* display the current operational status (e.g., normal/within SLA, degraded performance, service disruption, scheduled maintenance) for each primary service component - including Subscriber certificate issuance endpoints (i.e., ACME API), Domain Control Validation (DCV) services, ACME Renewal Information (ARI) endpoints, issuance log operations, landmark generation services, CRL distribution endpoints (if applicable), and Mirroring Cosigner endpoints - updated promptly upon detecting any change in service availability or performance;
* provide timely status updates throughout active service degradations or disruptions, detailing affected components, operational impact, and estimated resolution timelines as substantive information becomes available, followed by a post-incident root-cause summary (or a direct link to the corresponding public incident report required under Section 2.7.3.1. ("Incident Reports")); and  
* maintain a publicly viewable archive of all past service incidents and maintenance events for a minimum of 365 days.

### **2.3. PKI Policy Governance**

#### **2.3.1. CA/Browser Forum TLS Server Authentication Baseline Requirements**

MTC CA Operators that issue TLS server authentication Subscriber certificates trusted in Chrome by default MUST adhere to the latest version of the Baseline Requirements, except as described in the remainder of this policy. Because MTCs fundamentally differ from traditional X.509 certificates, this policy modifies, strengthens, limits, or exempts MTC CAs from certain Baseline Requirements. In the event of any conflict or incompatibility between the Baseline Requirements and this policy, the requirements of this policy SHALL take precedence.

#### **2.3.2. MTC CA Operator Policies**

MTC CA Operators MUST accurately describe the policies and practices of their MTC CA(s) within a combined CP/CPS that is:

* freely publicly available for examination;
* available in an authoritative English language version;
* available in Markdown (i.e., .md) or AsciiDoc (i.e., .adoc) and hosted in a public Repository where all historical versions are maintained and accessible (e.g., preserved as discrete versioned documents, or accessible via immutable release tags corresponding to each version identified in the document's change history);
* authoritative for all CA Cosigner Keys included in the CQRS;
* focused only on the specific PKI use case of issuing TLS server authentication MTCs to websites;
* sufficiently detailed to assess the operations of the CA(s) and compliance with these expectations and the Baseline Requirements, and MUST NOT conflict with either of these requirements, except for the Baseline Requirements modifications permitted by this CQRP Policy.

In Section 1.1 of the combined CP/CPS, the MTC CA Operator MUST explicitly state adherence to the latest published version of this policy, as well as adherence to the Baseline Requirements as modified, limited, or exempted by this policy. The MTC CA Operator is exempt from the requirement in Baseline Requirements Section 2.2 to state that the Baseline Requirements take precedence over the CP/CPS; the statement MUST instead confirm that the in-force CQRP policy takes precedence over the Baseline Requirements in the event of any conflict or inconsistency. The MTC CA Operator MAY fulfill this requirement by using a clause such as the following:

\[!NOTE] "[Name of MTC CA Operator] conforms to the current version of the Chrome Quantum-resistant Root Program (CQRP) Policy and the CA/Browser Forum Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates as modified by the CQRP Policy. In the event of any inconsistency between the Baseline Requirements and the CQRP Policy, the CQRP Policy takes precedence."

The combined CP/CPS SHOULD be structured in accordance with [RFC 3647](https://www.rfc-editor.org/info/rfc3647). For every applicable requirement in the CQRP Policy and Baseline Requirements, the combined CP/CPS MUST:

* Contain sufficient CA-specific detail to allow a technically competent reviewer to understand how the operator implements applicable controls. To satisfy this requirement, where underlying specifications (such as the Baseline Requirements) permit operational variation or optionality, the combined CP/CPS MUST explicitly state the chosen method, parameter, constraint, or implementation mechanism used by the CA (e.g., detailing the exact Domain Control Validation sub-methods utilized, rather than citing the section generally).  
* Describe the operator's current implementation commitments, including relevant operational parameters, constraints, and design choices. These SHOULD be explicit, bounded, and testable, particularly where applicable requirements permit discretion or variation.  
* Be self-contained, ensuring that any referenced external documents or specifications are publicly accessible and directly hyperlinked so that conformance can be evaluated without requiring excessive interpretive reconstruction across unlinked or undisclosed secondary documents.

MTC CA Operators MUST include in Section 1.1 of their combined CP/CPS a structured table chronologically disclosing all CA Cosigner Keys and corresponding certificate subjects governed by the policy. For each key, the disclosure MUST specify:

* The full Certificate Subject Distinguished Name (if a corresponding certificate exists);  
* The SHA-256 fingerprint of the SubjectPublicKeyInfo (Key ID);  
* The cryptographic algorithm and parameter set (e.g., ML-DSA-44); and  
* The key generation date and reference to the corresponding Key Generation Ceremony Report.

MTC CA Operators MUST publish exhaustive certificate profiles adhering to the profiles specified in Section 2.4.3. ("Certificate and CRL Profiles") of this policy. Specifically:

* The MTC CA Operator MUST publish in its Repository a separate certificate profile corresponding to each Reserved Certificate Policy Identifier (as defined within the Baseline Requirements) that might appear in Subscriber Certificates issued by MTC CAs it operates. The MTC CA Operator SHOULD generate and maintain these profiles via automated export or continuous synchronization from the active configuration of its issuance systems.  
* Each profile MUST exhaustively enumerate every field and extension the MTC CA is capable of including in a Subscriber certificate issued under that Reserved Certificate Policy Identifier. For each field and extension, the profile MUST explicitly specify presence (always, never, or optional), criticality, permitted values, permitted encodings, and, where applicable, permitted ordering and cardinality.  
* Any field or extension not explicitly enumerated and specified in the applicable certificate profile MUST NOT be present in Subscriber certificates issued under that profile.  
* The effective date of a certificate profile MUST NOT precede the date on which it was published in the MTC CA Operator’s Repository.  
* The MTC CA Operator MUST retain and continue to publish each superseded profile, together with its effective date range, until all remaining Subscriber certificates relying upon it have expired. Superseded profiles MUST remain directly retrievable as discrete artifacts or endpoints in the Repository (relying solely on Git commit history is not sufficient).

> [!NOTE]
> To prevent drift between documented and enforced configurations, a future update to this policy is expected to require structured certificate profiles exported directly from the MTC CA's issuance system.

Because a CP/CPS is considered a binding operational commitment, it needs to provide meaningful transparency into how the CA practically operates, rather than just acknowledging the rules it must follow. A CP/CPS MUST NOT simply copy, paraphrase, or restate the requirements as a substitute for describing the CA's actual implementation.

The requirements in this section do not prohibit MTC CA Operators from maintaining additional policy documents, which may also be considered authoritative by other stakeholders. However, the consolidated policy document made available to the CQRP MUST NOT conflict with any additional policy documents that might exist for the corresponding PKI.

### **2.4. Certificate Issuance Lifecycle and Profiles**

For the purpose of this policy and the expectations of the Baseline Requirements, MTC Subscriber certificate issuance (including the "certificate signing operation") occurs when the CA Cosigner private key is first applied to sign an issuance log checkpoint that incorporates the corresponding `TBSCertificateLogEntry` into the Merkle Tree.

MTC CA Operators MUST provide both Standalone and Landmark-relative certificates.

#### **2.4.1. Domain Control Validation**

MTC CA Operators MUST validate domain control in accordance with Section 3.2.2.4 ("Validation of Domain Authorization or Control") and Section 3.2.2.5 ("Authentication for an IP Address") of the Baseline Requirements, subject to the following modifications:

The following domain control validation methods are being deprecated in the Baseline Requirements and MUST NOT ever be relied upon:

* 3.2.2.4.4 Constructed Email to Domain Contact  
* 3.2.2.4.12 Validating Applicant as a Domain Contact  
* 3.2.2.4.13 Email to DNS CAA Contact  
* 3.2.2.4.14 Email to DNS TXT Contact  
* 3.2.2.4.16 Phone Contact with DNS TXT Record Phone Contact  
* 3.2.2.4.17 Phone Contact with DNS CAA Phone Contact  
* 3.2.2.5.2 Email, Fax, SMS, or Postal Mail to IP Address Contact  
* 3.2.2.5.3 Reverse Address Lookup  
* 3.2.2.5.5 Phone Contact with IP Address Contact

Domain control validation data reuse MUST be limited to a maximum of 10 days.

#### **2.4.2. Automation Support**

To enable reliable, rapid issuance and renewal without manual intervention, Subscriber certificates MUST be able to be issued and retrieved using an ACME-based service. The ACME service SHOULD conform to [RFC 8555](https://www.rfc-editor.org/info/rfc8555) and interoperate with standard ACME clients without requiring custom client-side software modifications for account registration, domain authorization, order processing, certificate issuance and management, and retrieval workflows. Any divergences from RFC 8555 MUST be documented in Section 4.1.2 of the combined CP/CPS.

The MTC CA MUST support ACME Renewal Information (ARI) ([RFC 9773](https://www.rfc-editor.org/info/rfc9773)) and use it as a mechanism by which Subscribers can be signaled to renew certificates in advance of scheduled expiry or in response to a revocation event. ARI adoption and client responsiveness are essential to ecosystem resilience and agility.

To evaluate whether Subscriber ACME clients reliably poll and act upon ARI signals, MTC CAs issuing Subscriber certificates with validity periods exceeding 7 days SHOULD conduct operational ARI testing.

When conducting operational ARI testing:

* No less than quarterly, the MTC CA Operator SHOULD randomly select a sample of no fewer than the lesser of (1) 3.0% of its time-valid Subscriber certificates with validity periods exceeding 7 days, or (2) 100,000 such certificates.
* For each sampled certificate, the MTC CA Operator SHOULD publish a modified ARI renewal window recommending an accelerated renewal timeline that begins within 24 hours of sample selection and spans no more than 72 hours in total duration.
* Within 14 calendar days of completing each operational ARI test cycle, the MTC CA Operator SHOULD publish [{test_cycle_id}-ari-operational-test-report.json](https://github.com/GoogleChrome/chromerootprogram/blob/main/content/cqrp/disclosures/ari-operational-test-report.schema.json) ([example](https://github.com/GoogleChrome/chromerootprogram/blob/main/content/cqrp/disclosures/ari-operational-test-report.json)) in a publicly disclosed location.
* Public reports SHOULD contain aggregated summary metrics (such as total certificates sampled, overall renewal pass rates within the window, and aggregated renewal latency percentiles).
* MTC CA Operators SHOULD contact Subscribers whose ACME clients failed to renew sampled certificates to identify technical or operational obstacles to ARI adoption.
* MTC CA Operators SHOULD aggregate identified adoption challenges and communicate them to mtcs [at] chromium [dot] org.
* All historical ARI testing reports SHOULD be preserved and made publicly accessible at that publicly disclosed location.
* It is NOT RECOMMENDED that MTC CA Operators revoke sampled certificates unless explicitly requested by the Subscriber.

> [!NOTE]
> A future update to this policy is expected to require periodic operational ARI testing and public reporting.

The MTC CA SHOULD also support the ACME Profiles Extension ([draft-ietf-acme-profiles](https://datatracker.ietf.org/doc/draft-ietf-acme-profiles/)) and use it as a mechanism to allow ACME clients to dynamically discover and select among different certificate profiles offered by the CA.

#### **2.4.3. Certificate and CRL Profiles**

The subsections below detail the profile requirements for MTC CA Cosigner Certificates, Subscriber TLS Certificates, and CRLs.

##### **2.4.3.1. MTC CA Cosigner Certificate Profile**

MTC CA Cosigner Certificates MUST conform to the MTC CA Certificate Profile defined in the MTC [specification](https://datatracker.ietf.org/doc/html/draft-ietf-plants-merkle-tree-certs-07) and the mtc-tlog [specification](https://c2sp.org/mtc-tlog@v0.1.0). MTC CA Operators are exempt from the signature algorithm and key size restrictions specified in Section 6.1.5 ("Key Sizes and Algorithms") and Section 7.1.3 ("Algorithm Identifiers") of the Baseline Requirements when using the ML-DSA ([RFC 9881](https://www.rfc-editor.org/info/rfc9881)) keys permitted by this policy.

In addition to the above listed specifications, these certificates MUST adhere to the following cryptographic constraints:

<table>
  <thead>
    <tr>
      <th align="left">Field</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>subjectPublicKeyInfo</code></td>
      <td>
        <p>The MTC CA MUST indicate an ML-DSA key using the following algorithm identifier:</p>
        <ul>
          <li>ML-DSA-44 (OID: <code>2.16.840.1.101.3.4.3.17</code>)</li>
        </ul>
        <p>The parameters for ML-DSA keys MUST be absent. To reduce complexity, minimize the attack surface, and ensure a single, consistent signature verification implementation is required across all Chrome clients, the MTC CA MUST NOT use HashML-DSA; only "pure" ML-DSA is permitted.</p>
        <p>When encoded, the <code>AlgorithmIdentifier</code> for ML-DSA keys MUST be byte-for-byte identical with the following hex-encoded bytes:</p>
        <ul>
          <li>For ML-DSA-44: <code>300b0609608648016503040311</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

| Extension | Presence | Critical | Description |
| :---- | :---- | :---- | :---- |
| `keyUsage` | MUST | YES | MUST be defined in accordance with the MTC [specification](https://datatracker.ietf.org/doc/html/draft-ietf-plants-merkle-tree-certs-07). `cRLSign` MUST also be present. |

##### **2.4.3.2. Subscriber TLS Server Authentication Certificate Profile**

MTC CA Operators MUST provide Subscriber certificates in the Standalone and Landmark-relative formats, both derived from the same underlying `TBSCertificateLogEntry` and defined in the MTC [specification](https://datatracker.ietf.org/doc/html/draft-ietf-plants-merkle-tree-certs-07).

For the purposes of this profile, MTC CA Operators are exempt from the serial number CSPRNG entropy requirements specified in Section 7.1.2.1 ("Serial Number") of the Baseline Requirements.

Except as modified above or where specified in the tables below, Subscriber certificates MUST comply with all requirements of the "Subscriber (Server) Certificate Profile" defined in the Baseline Requirements:

<table>
  <thead>
    <tr>
      <th align="left">Field</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>serialNumber</code></td>
      <td rowspan="4">
        <p>MUST be defined in accordance with the MTC <a href="https://datatracker.ietf.org/doc/html/draft-ietf-plants-merkle-tree-certs-07">specification</a>.</p>
        <p>In addition to the algorithms and key sizes permitted by the Baseline Requirements, MTC CA Operators MAY issue Subscriber certificates using ML-DSA keys. When an ML-DSA key is used, the CA MUST indicate the algorithm using one of the following identifiers:</p>
        <ul>
          <li>ML-DSA-44 (OID: <code>2.16.840.1.101.3.4.3.17</code>), or</li>
          <li>ML-DSA-65 (OID: <code>2.16.840.1.101.3.4.3.18</code>), or</li>
          <li>ML-DSA-87 (OID: <code>2.16.840.1.101.3.4.3.19</code>).</li>
        </ul>
        <p>Consistent with Section 2.4.3.1. (“MTC CA Cosigner Certificate Profile”), the parameters for ML-DSA keys MUST be absent, and HashML-DSA MUST NOT be used.</p>
        <p>When encoded, the <code>AlgorithmIdentifier</code> for these keys MUST be byte-for-byte identical with the hex-encoded bytes defined in Section 2.4.3.1. (“MTC CA Cosigner Certificate Profile”) of this policy:</p>
        <ul>
          <li>For ML-DSA-44: <code>300b0609608648016503040311</code></li>
          <li>For ML-DSA-65: <code>300b0609608648016503040312</code></li>
          <li>For ML-DSA-87: <code>300b0609608648016503040313</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><code>issuer</code></td>
    </tr>
    <tr>
      <td><code>signatureAlgorithm</code></td>
    </tr>
    <tr>
      <td><code>subjectPublicKeyInfo</code></td>
    </tr>
    <tr>
      <td><code>subject</code></td>
      <td>MUST be empty if <code>certificatePolicies</code> asserts <code>{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) domain-validated(1)} (2.23.140.1.2.1)</code> as defined in the Baseline Requirements.</td>
    </tr>
    <tr>
      <td><code>validity</code></td>
      <td>
        <p><code>notBefore</code>: MUST be a time no more than 24 hours prior to, and no later than, the CA Cosigner signing operation that first incorporates the corresponding <code>TBSCertificateLogEntry</code> into an issuance log checkpoint.</p>
        <p><code>notAfter</code>: When evaluated against the <code>notBefore</code> date as defined in RFC 5280, the difference between <code>notBefore</code> and <code>notAfter</code> MUST be equal to or less than the maximum validity period authorized for the issuing CA Cosigner (i.e., either 7 days or 47 days depending on the key constraints in Section 2.6.2. (“CA Cosigner Key Use”)).</p>
      </td>
    </tr>
  </tbody>
</table>

| Extension | Presence | Critical | Description |
| :---- | :---- | :---- | :---- |
| `certificatePolicies` | MUST | NO | MUST include the `policyIdentifier` field and SHOULD only assert `{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) domain-validated(1)} (2.23.140.1.2.1)` as defined in the Baseline Requirements. Other Reserved Certificate Policy Identifiers from the Baseline Requirements MAY be asserted instead. |
| `keyUsage` | MUST | YES | MUST only assert `digitalSignature`. |
| `extKeyUsage` | MUST | NO | MUST only include `id-kp-serverAuth` (OID: `1.3.6.1.5.5.7.3.1`). |
| `issuerAlternativeName` | MAY | NO | MAY include an arbitrary cosmetic name (e.g., for the commercial entity the Subscriber engaged to cause the issuance of the certificate). If included, this cosmetic name MUST be encoded as a `directoryName` within the `GeneralNames` structure, and SHOULD be represented using the `organizationName` (O) and/or `commonName` (CN) attributes. Other `GeneralName` types MUST NOT be used for this cosmetic purpose. |
| Signed Certificate Timestamp List | MUST NOT | - | - |

##### **2.4.3.3. CRL Profile**

MTC CA Operators are exempt from the signature algorithm and encoding restrictions specified in Section 7.1.3.2 ("Signature AlgorithmIdentifier") of the Baseline Requirements when signing CRLs. Instead, CRLs MUST be signed using an Active CA Cosigner Key in accordance with Section 2.6.2. ("CA Cosigner Key Use") of this policy.

#### **2.4.4. Linting**

For the purposes of Section 4.3.1.2 ("Pre-Issuance Linting") of the Baseline Requirements, MTC CA Operators SHOULD perform pre-issuance linting on `TBSCertificateLogEntry` structures prior to issuance log entry inclusion. This pre-issuance linting SHOULD block Subscriber certificate issuance (i.e., prevent a `TBSCertificateLogEntry` from being added to the MTC CA’s issuance log) for any certificate that does not conform to the applicable certificate profile in effect at the time of issuance.

MTC CA Operators SHOULD perform post-issuance linting on Standalone certificates prior to Subscriber delivery.

MTC CA Operators SHOULD publish a public mapping in their Repository that identifies, for each requirement expressed in a certificate profile defined in their CP/CPS (see Section 2.3.2. ("MTC CA Operator Policies")), the corresponding checks performed by their pre-issuance linting workflow(s) or issuance system controls. Where a profile requirement is not evaluated by linting, the CA SHOULD explicitly identify whether the requirement is enforced by construction within its underlying issuance system architecture, or identify it as unenforced.

As open-source and industry linting tools add support for MTC formats, MTC CA Operators SHOULD integrate newly released MTC linter rules into their pre-issuance pipelines within 60 calendar days of their public release.

> [!NOTE]
> A future update to this policy is expected to require automated pre-issuance linting against the MTC CA Operator's published certificate profiles.

When an MTC CA Operator becomes aware of a flawed private key generation method, or a demonstrated method or vulnerability that exposes a Subscriber's Private Key to compromise, the operator SHOULD update its pre-issuance validation systems to prevent future certificate issuance using keys generated by that method. MTC CA Operators are exempt from the requirement in Section 4.9.1.1 of the Baseline Requirements to scan extant public keys or revoke extant Subscriber certificates as a result of that discovery, and MAY rely on pre-issuance blocking and the natural expiration of extant certificates.

#### **2.4.5. Criteria for Chrome Usability**

To guarantee that a certificate's inclusion in an issuance log has been independently witnessed and to protect Chrome clients against log tampering or split-views created by an MTC CA, Subscriber certificates MUST meet the following criteria to be trusted by Chrome:

* Standalone certificates MUST include an MTCProof containing at least 2 valid subtree signatures over the covering subtree. One of these MUST be from the MTC CA Operator's CA Cosigner, and one MUST be from a Mirroring Cosigner recognized by Chrome as `Usable` (or `Frozen`, if the cosignature was generated prior to the freeze point) and not operated by or affiliated with the MTC CA Operator.  
* Landmark-relative certificates are only trusted by Chrome if the corresponding landmark is verified and its subtrees are published as trusted subtrees by Chrome’s Landmark Service. Chrome’s Landmark Service will only publish trusted subtrees for a landmark when the MTC CA has published a valid signed checkpoint for the corresponding issuance log at a tree size equal to or greater than that of the landmark; and at least one Mirroring Cosigner recognized by Chrome and not operated by or affiliated with the MTC CA Operator has published or cosigned a valid signed checkpoint for the corresponding issuance log at a tree size equal to or greater than that of the landmark.

MTC CAs are not required to delay the publication of their own signed checkpoints at the issuance log's primary checkpoint endpoint while awaiting Mirror cosignatures.

### **2.5. MTC CA Issuance Log**

#### **2.5.1. Issuance Log Operations**

##### **2.5.1.1. Technical Specifications**

The MTC CA Operator MUST operate an issuance log that cryptographically binds all issued Subscriber certificates into a verifiable Merkle Tree and that MUST be made publicly available in accordance with the mtc-tlog [specification](https://c2sp.org/mtc-tlog@v0.1.0).

To guarantee interoperability between MTC CAs, mirrors, monitors, and ACME clients across the ecosystem, the issuance log MUST strictly implement the API endpoints, cryptographic formats, and Merkle Tree structures defined in the MTC [specification](https://datatracker.ietf.org/doc/html/draft-ietf-plants-merkle-tree-certs-07) and the tlog-tiles [specification](https://c2sp.org/tlog-tiles@v1.0.0).

##### **2.5.1.2. Issuance Log Mirroring and Continuity**

To ensure Subscriber certificate information is widely available, MTC CA Operators MUST attempt to submit all issuance log updates to all Chrome-recognized Mirroring Cosigners in `Candidate`, `Qualified`, and `Usable` states described in Section 3.3. ("Mirroring Cosigner States"). Chrome will monitor to ensure that cosigned mirror checkpoints and supporting log tiles are made available on mirror endpoints in accordance with the timeliness SLA defined in Section 3.2.3. ("Cosigning Timeliness").

To prevent log fragmentation and ensure consistent oversight, MTC CA Operators MUST issue Subscriber certificates to only one issuance log at a time per Active CA Cosigner Key. If an issuance log becomes inoperable, the MTC CA Operator MAY rotate to a new issuance log to maintain issuance availability. Every rotation to a new issuance log for the same Active CA Cosigner Key MUST be publicly reported as an incident, as specified in Section 2.7.3. ("Publicly Reporting on Incidents"). Rotation to a new issuance log or the subsequent retirement of a CA Cosigner Key does not invalidate Subscriber certificates previously issued to the inoperable issuance log. If the CA chooses to retire the associated CA Cosigner Key as a result of the issuance log failure, Chrome may apply a Key Sunset Date, as described in Section 2.6.3. ("CA Cosigner Key Lifecycle & Rotation") to allow previously issued certificates to remain trusted by Chrome clients until their natural expiry.

##### **2.5.1.3. Data Retention and Log Pruning**

MTC CA Operators MUST NOT prune any log entry with a serial number greater than or equal to the `safe_to_prune_before` value published by Chrome in [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json). For capacity planning, operators SHOULD retain entries for at least 35 days after the end of the certificate's validity period (Chrome updates `safe_to_prune_before` to reflect entries that have been revoked or expired for at least 35 days).

To further prevent fragmented or hidden issuance logs and ensure monitors can predictably track all active issuance, Chrome enforces a strict upper bound on the number of issuance logs associated with a single CA Cosigner Key. For any given CA Cosigner Key, Chrome will only trust issuance log numbers 1 through 5. When transitioning to a new issuance log, the MTC CA Operator MUST use the next sequential issuance log number. Subscriber certificates issued to an issuance log number of 6 or greater will not be trusted by Chrome clients.

##### **2.5.1.4. Service Availability and Reporting**

The MTC CA issuance log MUST maintain high availability for read operations:

* Each log endpoint MUST maintain a request success rate (where a successful response is returned for a well-formed request) of at least 99.9% evaluated over any 72-hour period. This ensures sustained, low-grade request failures (e.g., due to rate limiting) are addressed independently of the 30-day overall requirement below.  
* Each log endpoint MUST maintain a request success rate of at least 99.0% evaluated over any rolling 30-calendar-day period. This bounds cumulative downtime over a month and ensures that a single, large disruption, or a series of severe, non-consecutive outages, is addressed even if the system recovers in under 72 hours.

Any Planned Maintenance that will interrupt these services MUST be publicly announced in advance in accordance with the definition of Planned Maintenance in this policy (note that Planned Maintenance does not exempt endpoints from the availability requirements above).

Upon becoming aware of any event that results in a failure to meet either availability requirement, the MTC CA Operator MUST submit a public incident report following the guidance in Section 2.7.3.1. ("Incident Reports"). The availability SLAs for a specific CA Cosigner Key's issuance log apply only until its final retention (Key Sunset Date + maximum permitted certificate lifetime + 35 days) has elapsed, after which Chrome no longer monitors the endpoint.

#### **2.5.2. Issuance Log Cryptographic Integrity**

The foundational security guarantee of the CQRS is the immutability of the MTC CA issuance log. If an MTC CA issuance log presents a split-view or cannot serve its data in a cryptographically verifiable way, it is considered a catastrophic failure. Any non-cryptographically verifiable issuance log MUST automatically discontinue Subscriber certificate issuance and the MTC CA Operator MUST issue a public incident report. Such failures MAY result in the CA Cosigner’s removal from the CQRS.

### **2.6. CA Cosigners**

Each CA Cosigner MUST operate in full conformance with this policy throughout its entire operational lifecycle, beginning at the time of key generation and continuing until the key is removed from the CQRS.

#### **2.6.1. CA Cosigner Key Generation**

To protect key material from unauthorized extraction, duplication, or misuse, CA Cosigner private keys MUST be generated, maintained, and perform all cryptographic operations within a Hardware Security Module (HSM) that is formally validated to FIPS 140-3 Level 3 or Common Criteria (CC) EAL 4+ (or higher). This requirement does not preclude the creation of secure, encrypted key backups or wrapped key transfers for disaster recovery or HSM migration, provided that the plaintext key material never exists outside of a validated HSM boundary and that all backup or transfer operations are performed under multi-person control by individuals in authorized Trusted Roles (as defined in the Network and Certificate System Security Requirements).

For the purposes of Section 6.1.1.1 ("CA Key Pair Generation") of the Baseline Requirements, MTC CA Cosigner Keys are considered to be CA Key Pairs for a Root Certificate.

For the purposes of Section 1.2.1 of the Network and Certificate System Security Requirements (incorporated by reference in the Baseline Requirements), MTC CA Cosigner Keys and Mirroring Cosigner Keys are not considered Root CA Systems.

If the HSM employed to generate and store the required CA Cosigner key pair has not yet achieved full Cryptographic Module Validation Program (CMVP) certification for ML-DSA ([RFC 9881](https://www.rfc-editor.org/rfc/rfc9881.html)) and ML-KEM ([RFC 9935](https://datatracker.ietf.org/doc/rfc9935/)) in an Approved Mode of operation, the generation and use of the key is permitted provided that:

* The underlying hardware module holds a valid FIPS 140-3 Level 3 (or Common Criteria EAL 4+ or higher) certification covering its physical security boundary, key management architecture, and classical cryptographic operations.  
* The specific implementation of ML-DSA and ML-KEM executing within the hardware boundary has successfully achieved Cryptographic Algorithm Validation Program (CAVP) certification from NIST.

Effective January 1, 2029, the HSM storing CA Cosigner Keys not already trusted by Chrome MUST possess a CMVP certification explicitly covering ML-DSA and ML-KEM. This intends to allow sufficient time for hardware vendors and testing laboratories to fully implement and execute the new post-quantum validation programs.

> [!NOTE]
> A future update to this policy is expected to allow the use of a single-tenant Cloud HSM to fulfill the requirements of this section. Additionally, a future update may require publicly verifiable cryptographic key attestation from the HSM to cryptographically prove that each CA Cosigner Key was natively generated within (i.e., not imported into), is non-exportable in plaintext from, and remains protected by a compliant HSM.

MTC CA Operators MUST collect written evidence from a Qualified Auditor (as defined within the Baseline Requirements) using their approved format for key generation ceremonies, that identifies the date(s) and approximate location(s) of the key generation ceremony and attests to the operator's adherence to the requirements defined in Section 6.1.1.1 ("CA Key Pair Generation") and 6.2 ("Private Key Protection and Cryptographic Module Engineering Controls") of the Baseline Requirements. These audit attestations MUST be hosted in the MTC CA Operator’s Repository.

#### **2.6.2. CA Cosigner Key Use**

CA Cosigner Keys MUST only be used in support of the MTC CA and its ancillary functions. To maintain a flat trust hierarchy, MTC CAs MUST NOT issue Subordinate CA certificates of any kind.

To encourage ecosystem agility, ensure rotation mechanisms are routinely exercised, and bound the operational impact of a potential undetected key compromise, a CA Cosigner Key will be trusted for a maximum of 2280 days (approximately 6 years) once included in the CQRS.

To ensure resilience against operational disruption and support disaster recovery, an MTC CA Operator MUST maintain in good standing a minimum of 3 and a maximum of 6 CA Cosigner Keys included in the CQRS, which MUST be composed as follows:

| Cosigner Key | Algorithm | Maximum Subscriber Validity | Additional Requirements |
| :---- | :---: | :---- | :---- |
| Active CA Cosigner #1 (Required) | ML-DSA-44 | 7 days | MUST be online and used for ongoing Subscriber certificate issuance. SHOULD generate landmarks approximately every hour, and MUST NOT exceed a total of 220 landmarks over any 7-day period. |
| Reserve CA Cosigner #1 (Required) This key is reserved for use in a planned key rotation or disaster recovery event. | ML-DSA-44 | N/A | MUST be maintained in a secure offline state by the MTC CA Operator, meaning the private key is physically air-gapped or logically disabled, and bringing the key into an active state requires interactive, multi-person authorization. |
| Reserve CA Cosigner #2 (Required) This key is reserved for use in a planned key rotation or disaster recovery event. | ML-DSA-44 | N/A | MUST be maintained in a secure offline state by the MTC CA Operator, meaning the private key is physically air-gapped or logically disabled, and bringing the key into an active state requires interactive, multi-person authorization. |
| Active CA Cosigner #2 (Optional) Active CA Cosigner #3 (Optional) Active CA Cosigner #4 (Optional) | ML-DSA-44* | 47 days* | MUST be online and used for ongoing Subscriber certificate issuance. Landmark generation MUST correspond to the maximum certificate validity issued by the CA Cosigner: Up to 7-day validity: SHOULD generate landmarks approximately every hour, and MUST NOT exceed a total of 220 landmarks over any 7-day period. Exceeding 7-day validity (up to 47 days): SHOULD generate landmarks approximately every 4 hours, and MUST NOT exceed a total of 370 landmarks over any 47-day period. |

> [!NOTE]
> (*) While ML-DSA-44 keys and a 7-day Subscriber certificate validity are RECOMMENDED, a future update to this policy is expected to allow the use of up to 3 ML-DSA-87 Active CA Cosigner Keys (which will be restricted to a maximum Subscriber certificate validity of 7 days).

#### **2.6.3. CA Cosigner Key Lifecycle and Rotation**

MTC CA Operators are responsible for managing the lifecycle of their CA Cosigner Keys in coordination with the CQRP and the ecosystem to ensure a seamless transition during planned rotations. To facilitate this transition and safely stage the update across Chrome clients, MTC CA Operators MUST submit requests to add or remove CA Cosigner Keys from the CQRS at least 30 calendar days in advance of a quarterly scheduled update, utilizing key material that was generated no more than 4 years prior to the request submission date. Key additions and removals will only be targeted for processing on the 15th day of January, April, July, and October.

To facilitate a key rotation schedule, an individual CA Cosigner Key SHOULD NOT be used for Subscriber certificate issuance for more than 1550 days (approximately 4 years). MTC CA Operators SHOULD establish a regular key ceremony schedule to refresh Active CA Cosigner Keys, utilizing designated Reserve CA Cosigner Keys to facilitate planned rotations. While operators MUST maintain 2 offline Reserve CA Cosigner Keys in the CQRS at all times, operators MAY transition both Reserve keys to Active during a single CQRS update to rotate multiple Active keys at once, provided that replacement Reserve keys are simultaneously introduced in the same batch to maintain ongoing disaster recovery readiness.

MTC CA Operators MAY issue Subscriber certificates concurrently from multiple Active CA Cosigner Keys; however, issuance MUST be limited to Active CA Cosigner Keys defined in Section 2.6.2. ("CA Cosigner Key Use"). When an MTC CA Operator is ready to retire an Active CA Cosigner Key from the CQRS, they MUST notify mtcs [at] chromium [dot] org. Following this notification, Chrome will establish and apply a Key Sunset Date for that specific key. Chrome clients will not trust any Subscriber certificates issued by that key after the established sunset date.

A key rotation schedule might look something akin to:

<pre><code>         | Y1  | Y2  | Y3  | Y4  | Y5  | Y6  | Y7  | Y8  | Y9  | Y10 | Y11 | Y12 | Y13 | Y14 | Y15 |
---------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
Key 1    | [A] | [-] |     |     |     |     |     |     |     |     |     |     |     |     |     |
Key 2    | [A] | [A] | [-] |     |     |     |     |     |     |     |     |     |     |     |     |
Key 3    | [A] | [A] | [A] | [-] |     |     |     |     |     |     |     |     |     |     |     |
Key 4    | [A] | [A] | [A] | [A] | [-] |     |     |     |     |     |     |     |     |     |     |
Key 5    | [+] | [A] | [A] | [A] | [A] | [-] |     |     |     |     |     |     |     |     |     |
Key 6    | [+] | [+] | [A] | [A] | [A] | [A] | [-] |     |     |     |     |     |     |     |     |
Key 7    |     | [+] | [+] | [A] | [A] | [A] | [A] | [-] |     |     |     |     |     |     |     |
Key 8    |     |     | [+] | [+] | [A] | [A] | [A] | [A] | [-] |     |     |     |     |     |     |
Key 9    |     |     |     | [+] | [+] | [A] | [A] | [A] | [A] | [-] |     |     |     |     |     |
Key 10   |     |     |     |     | [+] | [+] | [A] | [A] | [A] | [A] | [-] |     |     |     |     |
Key 11   |     |     |     |     |     | [+] | [+] | [A] | [A] | [A] | [A] | [-] |     |     |     |
Key 12   |     |     |     |     |     |     | [+] | [+] | [A] | [A] | [A] | [A] | [-] |     |     |
Key 13   |     |     |     |     |     |     |     | [+] | [+] | [A] | [A] | [A] | [A] | [-] |     |
Key 14   |     |     |     |     |     |     |     |     | [+] | [+] | [A] | [A] | [A] | [A] | [-] |
Key 15   |     |     |     |     |     |     |     |     |     | [+] | [+] | [A] | [A] | [A] | [A] |
 
Legend:
 [ + ] = Reserve (Offline / Inactive)
 [ A ] = Active (Online, issuing Subscriber certificates)
 [ - ] = Retired & Removed (Key Sunset Date applied to bound trust to previously issued certificates; removed from CQRS after those certificates expire)</code></pre>

The maximum limits of 4 Active CA Cosigner Keys and 2 Reserve CA Cosigner Keys are evaluated against the net effective state of the MTC CA Operator’s keys after a batch of updates is processed (e.g., on the 15th of the month), rather than the queueing state. A processed retirement of a key immediately frees up a slot in its respective category (Active or Reserve). An MTC CA Operator with the maximum number of keys (i.e., 4 Active and 2 Reserve) MAY submit an addition/activation request, provided they simultaneously submit a retirement request in the same processing batch. Because both actions are processed together, the net resulting state will not exceed the limit.

A valid rotation and invalid addition might look something like:

* An operator currently has 4 Active keys and 2 Reserve keys. They submit a request to retire and remove 1 Active key, transition 1 Reserve key to Active, and add 1 new Reserve key. Upon processing, the net result is 4 Active and 2 Reserve keys. This is valid.  
* An operator currently has 4 Active keys. They submit a request to transition 1 Reserve key to Active, but do not submit a retirement for an existing Active key. Because the processed result would be 5 Active keys, the update request will be rejected. This is invalid.

### **2.7. Oversight and Incident Reporting**

#### **2.7.1. Annual Third Party Audits**

At this time, MTC CAs are exempt from the annual, contiguous audit requirements detailed in Section 8 ("Compliance Audit and Other Assessments") of the Baseline Requirements. This exemption exists because current compliance evaluation criteria are bound to traditional X.509 architectures and may not accurately apply to MTC operations, especially while the underlying standards remain in active development.

In lieu of annual third-party audits, the CQRP may at any time require an MTC CA Operator to provide operational and system artifacts or execute directed compliance exercises to independently verify conformance with this policy. These exercises will be scoped to avoid disrupting Subscriber operations and may include, for example, timed certificate issuances for designated test domains under the control of the MTC CA Operator or the CQRP using standard validation and issuance workflows to evaluate issuance logging and mirroring. If such a request is made, the CQRP will work with the MTC CA Operator to identify reasonable timelines and disclosure methodologies, and the MTC CA Operator would need to complete the exercise and provide the requested data within the established timeframe.

> [!NOTE]
> To promote issuance transparency and increase accountability, a future update to this policy is expected to require MTC CA Operators to publish privacy-preserving validation data describing the domain control validation relied upon for each issuance, bound to the corresponding issuance log entry.

#### **2.7.2. Timely and Transparent Communications**

The CQRP may request additional information from an MTC CA Operator to verify that the commitments and obligations outlined in this policy are being met, or when updates to policy requirements are being considered. To ensure timely resolution of compliance questions and swift evaluation of potential ecosystem risks, MTC CA Operators MUST provide the requested information within 14 calendar days unless specified otherwise.

#### **2.7.3. Publicly Reporting on Incidents**

If an MTC CA Operator fails to meet this policy's commitments (excluding the requirements detailed in Section 3. ("Minimum Requirements for Mirroring Operators"), which have their own notification process), it is considered a publicly reportable incident. A reportable incident includes, but is not limited to:

* a known or suspected compromise of any CA Cosigner Key.  
* presenting conflicting Merkle Tree views or signing inconsistent checkpoints.  
* the issuance of any certificate that fails to comply with the authorized certificate profiles or validated domain control procedures mandated by this policy.  
* failure to meet the availability requirements from this policy.  
* any other situation that may impact the MTC CA's integrity, trustworthiness, or compatibility.

##### **2.7.3.1. Incident Reports**

To maintain transparency and enable the CQRP and the broader community to independently evaluate the severity and systemic risks of an event, rather than relying solely on the operator's internal assessment, MTC CA Operators MUST publicly disclose and/or respond to incident reports, regardless of perceived impact. Reports MUST be submitted in accordance with the current version of the [CCADB Incident Reporting Guidelines](https://www.ccadb.org/cas/incident-report) format and timelines. The CQRP uses the information in the public disclosure as the basis for evaluating incidents.

To ensure the CQRP is immediately alerted to severe vulnerabilities or active compromises while a safe public disclosure plan is actively coordinated, if the MTC CA Operator has not yet publicly disclosed an incident, they MUST notify chrome-quantum-resistant-root-program [at] google [dot] com and include an initial timeline for public disclosure.

MTC CA Operators MUST be detailed, candid, timely, and transparent in describing their architecture, implementation, operations, and external dependencies as necessary for the CQRP and the public to evaluate the nature of the incident and the operator's response. When evaluating an incident response, the CQRP's primary concern is ensuring that browsers, other MTC CA Operators, users, and website operators have the necessary information to identify improvements, and that the operator is responsive to addressing identified issues.

Factors that are significant to the CQRP when evaluating incidents include, but are not limited to:

* a demonstration of understanding of the root causes of an incident,
* a substantive commitment and timeline to changes that clearly and persuasively address the root cause,
* past history by the MTC CA Operator in its incident handling and its follow-through on commitments, and,
* the severity of the security impact of the incident.

##### **2.7.3.2. Communicating with Chrome During Incidents**

The CQRP prioritizes and remains committed to promoting public disclosure and discussion of incidents, as they can affect the entire Internet, not just Chrome and its users. The CQRP’s sole responsibility when responding to incidents is upholding the safety and security of Chrome's users.

As standard practice, the CQRP does not:

* discuss ongoing public incident reports privately with the MTC CA Operator. We believe using information disclosed to the public as the basis for our response is the most transparent and effective way of upholding the security expectations of Chrome's users, while also ensuring the factors that are significant to Chrome are adequately addressed;  
* advise on or approve an operator’s proposed or planned response to an incident; or  
* offer guarantees of specific outcomes in response to the course of action deemed most appropriate by the operator.

## **3. Minimum Requirements for Mirroring Operators**

To ensure the availability of Subscriber certificate information, MTC CA Operators MUST operate a Mirroring Cosigner usable by all other CA Cosigners included in Chrome’s [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json). This operational requirement contributes to a decentralized, highly available web of transparency.

While reference implementations may distinguish between a "witness" (consistency verification) and a "mirror" (durable storage), a Chrome-recognized Mirroring Cosigner MUST perform both roles. It MUST verify log consistency prior to cosigning and MUST maintain public availability of the mirrored log data.

### **3.1. Mirroring Cosigner Key Generation and Use**

Even during a planned key rotation coordinated under Section 3.4. ("Mirroring Cosigner Lifecycle and Rotation"), the CQRP will designate at most one Mirroring Cosigner Key per Mirroring Operator as `Usable` in [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json) at any given time. To ensure consistent interoperability, minimize bandwidth overhead, and optimize signature verification performance across all Chrome clients, Mirroring Cosigner Keys MUST be ML-DSA-44 (OID: 2.16.840.1.101.3.4.3.17) ([RFC 9881](https://www.rfc-editor.org/info/rfc9881)). Cosignatures MUST be generated and formatted in accordance with the tlog-cosignature [specification](https://c2sp.org/tlog-cosignature@v1.1.0).

While the use of an HSM for generating and storing Mirroring Cosigner Keys is OPTIONAL, operators MUST ensure these keys are protected against misuse, and MUST promptly notify mtcs [at] chromium [dot] org in the event of any known or suspected Mirroring Cosigner Key compromise.

Mirroring Cosigner Keys MUST be dedicated exclusively to cosigning issuance log checkpoints and views as defined in this policy. Mirroring Operators MUST NOT utilize Mirroring Cosigner Keys for any other cryptographic function or external purpose.

To facilitate a key rotation schedule, an individual Mirroring Cosigner Key SHOULD NOT be used for more than 1550 days (approximately 4 years).

### **3.2. Mirroring Cosigner Operations**

#### **3.2.1. Technical Specifications**

Mirroring Cosigners MUST strictly implement the API endpoints, cryptographic formats, and validation logic defined in the MTC [specification](https://datatracker.ietf.org/doc/html/draft-ietf-plants-merkle-tree-certs-07), the mtc-tlog [specification](https://c2sp.org/mtc-tlog@v0.1.0), the tlog-mirror [specification](https://c2sp.org/tlog-mirror@v0.1.0), and the tlog-cosignature [specification](https://c2sp.org/tlog-cosignature@v1.1.0).&nbsp;

#### **3.2.2. Log Discovery and Synchronization**

Mirroring Cosigners MUST consume Chrome’s [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json) at least every 24 hours to ensure newly added CA Cosigners are promptly recognized and incorporated into their active mirroring configurations. Upon a CA Cosigner Key no longer being included in [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json), Mirroring Cosigners MAY stop mirroring the corresponding issuance log(s).

#### **3.2.3. Cosigning Timeliness**

To ensure clients and monitors receive timely cryptographic proofs and to prevent the issuance of unobservable cosignatures, Mirroring Cosigners:

* SHOULD ensure that the newly cosigned checkpoint, along with all supporting log tiles and entries necessary to cryptographically verify it, is available on their public endpoints immediately after cosignature issuance.  
* MUST ensure that the cosigned checkpoint and all supporting log tiles and entries are available on their public endpoints within 10 minutes of cosignature issuance, and SHOULD consistently achieve availability within 5 minutes under normal operating conditions.

#### **3.2.4. Data Retention and Log Pruning**

Mirroring Cosigners MUST NOT prune any log entry with a serial number greater than or equal to the `safe_to_prune_before` value published by Chrome in [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json). For capacity planning, operators SHOULD retain entries for at least 35 days after the end of the certificate's validity period. To guarantee that mirrors function as complete, highly available backups of the transparency ecosystem and do not create premature data unavailability, Mirroring Cosigners SHOULD NOT prune entries until the corresponding entries have been pruned from the corresponding issuance log, except that Mirroring Cosigners MAY independently prune any entry below `safe_to_prune_before` once 90 days have elapsed since the end of the certificate's validity period.

#### **3.2.5. Service Availability and Reporting**

Mirroring Cosigners MUST maintain high availability for both read and write operations:

* Each mirror endpoint MUST maintain a request success rate (where a successful response is returned for a well-formed request) of at least 99.9% evaluated over any 72-hour period. This ensures sustained, low-grade request failures (e.g., due to rate limiting) are addressed independently of the 30-day overall requirement below.  
* Each mirror endpoint MUST maintain a request success rate of at least 99.0% evaluated over any rolling 30-calendar-day period. This bounds cumulative downtime over a month and ensures that a single, large disruption, or a series of severe, non-consecutive outages, is addressed even if the system recovers in under 3 days. 

Any Planned Maintenance that will interrupt these services MUST be publicly announced in advance in accordance with the definition of Planned Maintenance in this policy (note that Planned Maintenance only exempts write operations from the 72-hour availability requirement above; write operations MUST still meet the 30-calendar-day requirement, and read operations are not exempt from either requirement).

Upon becoming aware of any event that results in a failure to meet either availability requirement, the Mirroring Operator MUST notify mtcs [at] chromium [dot] org within 1 calendar day. This initial notification SHOULD include a high-level description of the incident and an estimated timeline for service restoration. Following the resolution of such an incident, the Mirroring Operator MUST submit a post-mortem report to mtcs [at] chromium [dot] org within 14 calendar days of service being sufficiently restored. This report SHOULD outline the technical and procedural safeguards that failed and the mitigations enacted to prevent recurrence.

#### **3.2.6. Log Consistency**

Mirroring Cosigners MUST strictly enforce append-only consistency for every mirrored issuance log. Generating a valid cosignature over an MTC CA log state that is cryptographically inconsistent with the Mirroring Cosigner's prior view of that log constitutes a critical operational failure by the Mirroring Cosigner. This failure to enforce append-only consistency will result in the mirror's transition to the `Frozen` state, and may result in the removal of the operator from Chrome's [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json).

If a Mirroring Operator has credible evidence that an MTC CA Cosigner Key is compromised, is presenting a split-view, or is causing severe operational degradation (e.g., denial-of-service), the Mirroring Cosigner MAY temporarily suspend cosigning new checkpoints for that specific issuance log prior to the key's removal from [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json), provided the Mirroring Operator immediately notifies mtcs [at] chromium [dot] org with the supporting evidence and continues to serve read requests for previously mirrored data.

### **3.3. Mirroring Cosigner States**

To safely introduce and retire Mirroring Cosigners without disrupting the broader ecosystem, Chrome recognizes the following distinct operational states. Only cosignatures from `Usable` or `Frozen` (if the cosignature was generated prior to the freeze point) Mirroring Cosigners count toward the minimum Chrome client trust requirements defined in Section 2.4.5. ("Criteria for Chrome Usability").

* `Candidate`: The initial state of a Mirroring Cosigner that is under consideration to be included in the CQRS. To facilitate ecosystem discovery and compliance monitoring, `Candidate` Mirroring Cosigners are published in [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json) and [`cosigners.pem`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.pem), but are not yet distributed to Chrome clients. During this time, Mirroring Cosigners MUST be fully capable of cosigning and mirroring all MTC CAs included in the CQRS. `Candidate` cosignatures, whether embedded within a Standalone certificate or attached to a published landmark, do not contribute to Chrome client validation.
* `Qualified`: The state of a Mirroring Cosigner that has successfully completed its minimum 30-calendar-day monitoring period and demonstrated adherence to all availability requirements. The Mirroring Cosigner’s state is updated in [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json) and its key and metadata have begun distribution to Chrome clients, but cannot yet be guaranteed to have propagated to all Chrome clients.
* `Usable`: The state of a Mirroring Cosigner that has been `Qualified` for at least 70 calendar days. Cosignatures from a `Usable` cosigner may be relied upon to satisfy the client validation requirements for both Standalone and Landmark-relative certificates.
* `Frozen`: The state of a Mirroring Cosigner that is no longer actively generating new cosignatures or observing new MTC CAs, but continues to provide high-availability read access to mirrored logs. Cosignatures generated prior to the freeze point remain valid for Chrome client validation.
* `Removed`: The terminal state for a Mirroring Cosigner that is no longer trusted by Chrome. This may be due to the Mirroring Cosigner being shut down by the operator, violating this policy, suffering a catastrophic compromise, or other critical failure. Cosignatures from a `Removed` cosigner are immediately invalid and do not contribute to Chrome client validation, even if embedded within an otherwise valid Standalone certificate.

### **3.4. Mirroring Cosigner Lifecycle and Rotation**

To ensure a seamless transition during planned retirement or replacement of Mirroring Cosigners and to minimize disruption to the ecosystem, Mirroring Operators MUST manage the lifecycle of their Mirroring Cosigner Keys in coordination with the CQRP.

Mirroring Operators MUST notify mtcs [at] chromium [dot] org at least 30 calendar days in advance of any planned cessation of operations for a Mirroring Cosigner or its intended transition to the `Frozen` and/or `Removed` states. This notification SHOULD include:

* The unique identifier of the Mirroring Cosigner.  
* The planned date for the Mirroring Cosigner to transition to the `Frozen` state.  
* The planned date for the Mirroring Cosigner to be `Removed` from Chrome's [`cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json).  
* A clear rationale for the planned transition (e.g., replacement with a new mirror, operational changes, etc.).

During a planned key rotation, a Mirroring Operator MAY concurrently operate a retiring key and a designated replacement key:

* The retiring key MUST remain in the `Usable` state until the replacement key has completed its qualification period and transitioned from `Qualified` to `Usable`.  
* Upon the replacement key transitioning to `Usable`, the retiring key MUST transition to the `Frozen` state and cease generating new cosignatures.  
* The retiring key MUST remain in the `Frozen` state, maintaining high-availability read access to mirrored log data, until all certificates relying upon its past cosignatures have expired or until it is transitioned to `Removed` in coordination with the CQRP.

The CQRP reserves the right to request adjustments to proposed state transition or key rotation timelines, or require additional information, to ensure the continued security, transparency, and operational stability of the ecosystem. New Mirroring Cosigners can be submitted to the CQRP by following Section 2. ("Submission Process") of [Preparing and Applying for Inclusion](https://googlechrome.github.io/chromerootprogram/cqrp/apply/).

## **References**

Unless a specific revision or version tag is specified below, references to external specifications, standards, and requirements documents in this policy refer to the most recent published version, or any subsequent superseding release. Where a specific version of a specification is cited below, any transitive specifications it normatively references apply at the versions specified therein.

[BCP 14](https://www.rfc-editor.org/info/bcp14), Best Current Practice 14 (RFC 2119, RFC 8174): Key words for use in RFCs to Indicate Requirement Levels. S. Bradner, B. Leiba.

[RFC 3647](https://www.rfc-editor.org/info/rfc3647), Request for Comments: 3647, Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework. S. Chokhani, W. Ford, R. Sabett, C. Merrill, S. Wu.

[RFC 5280](https://www.rfc-editor.org/info/rfc5280), Request for Comments: 5280, Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile. D. Cooper, S. Santesson, S. Farrell, S. Boeyen, R. Housley, W. Polk.

[RFC 8555](https://www.rfc-editor.org/info/rfc8555), Request for Comments: 8555, Automatic Certificate Management Environment (ACME). R. Barnes, J. Hoffman-Andrews, D. McCarney, J. Kasten.

[RFC 9773](https://www.rfc-editor.org/info/rfc9773), Request for Comments: 9773, ACME Renewal Information (ARI) Extension. A. Gable.

[RFC 9881](https://www.rfc-editor.org/info/rfc9881), Request for Comments: 9881, Internet X.509 Public Key Infrastructure Algorithm Identifiers for the Module-Lattice-Based Digital Signature Algorithm (ML-DSA). J. Massimo, P. Kampanakis, S. Turner, B. E. Westerbaan.

[RFC 9935](https://www.rfc-editor.org/info/rfc9935), Request for Comments: 9935, Internet X.509 Public Key Infrastructure Algorithm Identifiers for the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM). S. Turner, P. Kampanakis, J. Massimo, B. E. Westerbaan.

[ACME Profiles Extension](https://datatracker.ietf.org/doc/draft-ietf-acme-profiles/), Internet-Draft: draft-ietf-acme-profiles. A. Gable.

[Merkle Tree Certificates](https://datatracker.ietf.org/doc/html/draft-ietf-plants-merkle-tree-certs-07), Internet-Draft: draft-ietf-plants-merkle-tree-certs-07. D. Benjamin, D. O'Brien, B. E. Westerbaan.

[Merkle Tree Certificates With Tiled Transparency Logs](https://c2sp.org/mtc-tlog@v0.1.0), Community Cryptography Specification Project: mtc-tlog@v0.1.0. A. Gable, D. Benjamin, J. DeBlasio, M. McPherrin.

[Transparency Log Mirrors](https://c2sp.org/tlog-mirror@v0.1.0), Community Cryptography Specification Project: tlog-mirror@v0.1.0. A. Cutter, D. Benjamin, L. Valenta.

[Tiled Transparency Logs](https://c2sp.org/tlog-tiles@v1.0.0), Community Cryptography Specification Project: tlog-tiles@v1.0.0. R. Cox, F. Valsorda.

[Transparency Log Cosignatures](https://c2sp.org/tlog-cosignature@v1.1.0), Community Cryptography Specification Project: tlog-cosignature@v1.1.0. A. Cutter, F. Valsorda, R. Dahlberg.

[Baseline Requirements](https://cabforum.org/baseline-requirements-documents/), CA/Browser Forum Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates. CA/Browser Forum.

[Network and Certificate System Security Requirements](https://cabforum.org/working-groups/netsec/requirements/), CA/Browser Forum Network and Certificate System Security Requirements. CA/Browser Forum.
