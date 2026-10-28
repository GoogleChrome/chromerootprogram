---
title: Chrome Quantum-resistant Root Program - Preparing and Applying for Inclusion
---

# [DRAFT] Preparing and Applying for Inclusion

## Last updated: 2026-10-28

The Chrome Quantum-resistant Root Program's (CQRP) primary commitment is to the security of Chrome's users. Chrome continuously works to improve the baseline of security on the web, and its policies, procedures, and initiatives reflect that goal. Every [Merkle Tree Certificate](https://datatracker.ietf.org/doc/html/draft-ietf-plants-merkle-tree-certs-07) Certification Authority (MTC CA) and Mirroring Cosigner in the Chrome Quantum-resistant Root Store (CQRS) is a critical link in the chain of trust relied upon by Chrome’s billions of users. Any compromise or misoperation by a single operator can have cascading, detrimental effects, with harm not limited to Subscribers of the corresponding operator.

Ultimately, in order for an operator’s inclusion request to be accepted, it must clearly and unequivocally demonstrate how its organization meets the high standards defined in the [CQRP Policy](https://googlechrome.github.io/chromerootprogram/cqrp/draft-policy/). The burden of proof rests entirely on the entity applying to proactively and unquestionably demonstrate this commitment, thereby clearly offsetting the inherent and significant security risks of inclusion.

Google includes or removes operators in the CQRS as it deems appropriate at its sole discretion. Google selects and continues to include Cosigner keys to enhance Chrome's security. Operators included in the CQRS must provide value to Chrome end users that clearly exceeds the risk of their continued inclusion. To that end, the CQRP Policy defines the minimum requirements that MTC CA Operators and Mirroring Operators must meet for both initial and continued inclusion in the CQRS. The policy is periodically updated to further promote the CQRP’s goals: **security**, **simplicity**, **predictability**, **transparency**, and **resilience**.

> [!NOTE]
> A future update to this process may require the use of the Common CA Database ([CCADB](https://www.ccadb.org/)) for inclusion submissions, rather than using the [Chromium Issues Tracker](https://issues.chromium.org/issues/new?component=2114629&template=2386551).

## **1. Roles and Prerequisites for Inclusion Requests**

As [described](https://googlechrome.github.io/chromerootprogram/cqrp/draft-policy/) in the CQRP Policy, all MTC CA Operators are also Mirroring Operators. Applying for inclusion in the CQRS represents a commitment to operate as both a Mirroring Operator and an MTC CA Operator.

As detailed in Section 1.1. ("Eligibility") of the CQRP Policy, initial eligibility to apply for inclusion in the CQRS is restricted to [CT Log operators](https://certificate.transparency.dev/logs/) with at least one "[usable](https://googlechrome.github.io/CertificateTransparency/log_states.html)" log in Chrome before February 1, 2026.

> [!NOTE]
> Beginning in 2027H2, a future update to the CQRP Policy is expected to allow organizations that do not meet the initial eligibility restrictions above to apply for inclusion. Those prospective operators will be required to demonstrate reliable, high-availability and consistent operation of their Mirroring Cosigner in the CQRS for a specified period before their CA Cosigners will be considered for inclusion as an MTC CA Operator.

Though eligible CQRS Applicants are preferred to submit a complete inclusion request covering both their Mirroring Cosigner and CA Cosigner operations simultaneously, the CQRP recognizes the technical and operational effort required to deploy a complete MTC infrastructure. To help bootstrap ecosystem mirroring availability and allow operators to gain operational experience incrementally, an eligible CQRS Applicant may initially submit an inclusion request populating only the required Operator and Mirroring Cosigner fields, deferring the CA Cosigner artifacts to a subsequent update. In this case, the CQRS Applicant may omit the `facility_certification_url` and all `ca_cosigner_keys` information from their `mtc-disclosures.json` until applying as an MTC CA Operator.

However, this staged onboarding path is time-bounded. An operator that initially enters the CQRS solely as a Mirroring Operator must submit a complete MTC CA Operator inclusion update within 3 years of its Mirroring Cosigner first being accepted into the CQRS. If the operator does not submit the required CA Cosigner materials within this 3-year window, or it fails to progress to MTC CA Operator inclusion, the operator should expect its Mirroring Cosigner to be phased out (transitioned to `Frozen` and subsequently `Removed`) from the CQRS.

## **2. Submission Process**

### **2.1. Initial Submission**

CQRS inclusion requests are submitted using the New MTC Operator template in the [Chromium Issues Tracker](https://issues.chromium.org/issues/new?component=2114629&template=2386551). By creating a new issue in the Chromium Issues Tracker, the entity is asserting it is organizationally distinct from all existing operators present in [cosigners.json](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json).

All application artifacts need to be hosted from a publicly accessible Repository (as defined within the Baseline Requirements). At any point during its review, the CQRP may contact the operator seeking additional or clarifying information. Operators are expected to provide the requested information promptly, and no later than 14 days unless specified otherwise.

### **2.2. Updating Submissions**

Inclusion request submissions are expected to remain up-to-date as operational representations change. This includes updating the issue in the Chromium Issues Tracker as planned key lifecycle events become known, as detailed in the subsections below.

#### **2.2.1. Submitting new Mirroring Cosigner Keys**

Existing Mirroring Operators can apply to have a new Mirroring Cosigner Key included in the CQRS by updating their existing issue on the Chromium Issues Tracker.

#### **2.2.2. Submitting new CA Cosigner Keys**

Existing MTC CA Operators can apply to have CA Cosigner Keys rotated in the CQRS, which will be processed according to a quarterly schedule (targeted for processing on the 15th day of January, April, July, and October). This includes:

1. At least 30 days prior to the target quarterly update date, the existing MTC CA Operator will publish the new MTC CA Cosigner Certificates (i.e., Reserve CA Cosigner Keys) on its Repository, update their existing issue in the Chromium Issues Tracker with the new key information, and announce the planned addition to mtcs [at] chromium [dot] org. The announcement needs to include the URL to the MTC CA Operator’s [mtc-disclosures.json](https://github.com/GoogleChrome/chromerootprogram/blob/main/content/cqrp/disclosures/mtc-disclosures.schema.json) ([example](https://github.com/GoogleChrome/chromerootprogram/blob/main/content/cqrp/disclosures/mtc-disclosures.json)). 
2. After the CQRP reviews the issue and the key is added to the CQRS, the MTC CA Operator needs to update the issue explicitly stating when the Reserve CA Cosigner Key(s) are expected to transition to an Active state, which is when the MTC CA Operator can expect landmarks for the newly Active CA Cosigner Key(s) to be distributed to Chrome clients.

## **3. Evaluation Process**

Chrome evaluates inclusion requests through a structured review pipeline, generally adhering to the following high-level milestones:

1. Completeness Triage  
2. Beneficial Ownership and Due Diligence Review  
3. Public Discussion Period  
4. Technical Compliance and Audit Verification  
5. Confirming Inclusion Provides Value to Chrome Users  
6. Inclusion Decision

Once an inclusion request has all required artifacts, ongoing monitoring will occur as the review progresses through the high-level milestones.

All Mirroring Cosigners need to pass a minimum 30-day compliance monitoring period before becoming `Qualified`. Once `Qualified`, a Mirroring Cosigner that maintains ongoing compliance with the CQRP policy will automatically transition to `Usable` after a 70-day propagation period, at which point its cosignatures will be relied upon for Chrome client validation. During this time, the CQRP will actively monitor the Mirroring Cosigner to ensure conformance to the technical specifications and availability requirements included in the CQRP Policy. In the event that the Mirroring Cosigner does not maintain ongoing compliance with the CQRP Policy, it will not be promoted to `Usable`.

All operators should expect ongoing querying of their cosigners from Google’s compliance monitoring infrastructure throughout the lifetime of the mirror and/or issuance log.

The duration, availability, incident history, and overall compliance record of an operator's Mirroring Operator service will be material to the evaluation of any subsequent MTC CA Operator inclusion request. Once eligibility is expanded in a future policy update (targeted for 2027H2), sustained, demonstrably reliable mirroring operations in good standing, beyond the minimum period ultimately specified, will be viewed favorably. Mirroring tenure alone does not establish eligibility, and does not entitle an operator to inclusion or to any particular order of request review by the CQRP.

## **4. Potential Outcomes**

Inclusion requests may conclude with one of the following outcomes:

* **Accepted**: An inclusion application is classified as "Accepted" when an entity proactively and unequivocally demonstrates full compliance with all technical, operational, procedural, and audit requirements defined within the CQRP Policy, and clearly establishes that the value of its inclusion for Chrome end users exceeds the associated security, privacy, and operational risks.

    Upon receiving an Accepted determination, the entity's key material, endpoints, and associated trust metadata will be scheduled for inclusion in the CQRS and distributed to Chrome clients on an approximately quarterly targeted release cycle (though distributions are not limited to quarterly releases). However, the CQRP makes no guarantees on the timeliness of distribution.

    Acceptance does not constitute a permanent, irrevocable, or unconditional guarantee of trust. Included operators need to continuously maintain adherence to all ongoing policy obligations - including compliance monitoring metrics (uptime, cryptographic correctness, and mirror consistency) and prompt incident reporting. The CQRP reserves the right to modify, suspend, or revoke inclusion at its sole discretion if an operator fails to sustain these standards or if the risk of continued inclusion outweighs the benefit to Chrome users.

* **Rejected**: An inclusion application is classified as "Rejected" when an entity fails to unequivocally demonstrate that the value of its inclusion to Chrome end users clearly exceeds the associated security, privacy, or operational risks. Rejection typically results from unaddressed technical, audit, or procedural deficiencies, incomplete or inaccurate disclosures, an incident reporting history that fails to reliably demonstrate the factors that are significant to the CQRP, or a failure to satisfy the minimum requirements defined within the CQRP Policy.

    An organization whose application is Rejected is typically subject to a standard 6-month cooling-off period, beginning on the date of the formal rejection determination. During this period, the organization is ineligible to submit new or revised inclusion requests to the CQRP. This cooling-off period provides the organization sufficient time to remediate identified deficiencies, demonstrate sustained operational stability, and obtain updated, compliant audit attestations prior to re-applying.

* **Disqualified**: An entity is classified as "Disqualified" when the CQRP determines that they present an unacceptable or unmitigable risk to Chrome end users or the integrity of the web. Disqualification is reserved for, but not limited to:

    * Being the subject of multiple application Rejections without demonstrating meaningful and measurable remediation;
    * Intentional misrepresentation, falsification, or material omission of facts in public disclosures, audit attestations, or program communications;
    * Willful non-compliance with the CQRP Policy; or
    * Critical failures, key compromises, or operational practices that demonstrate an inability or unwillingness to maintain a robust "security-first" culture.

    An entity designated as Disqualified is permanently barred from applying for or receiving inclusion in the CQRS across all current and future PKI hierarchies operated, owned, or controlled by the organization, its subsidiaries, or its affiliates.
