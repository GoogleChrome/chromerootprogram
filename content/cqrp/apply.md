---
title: Chrome Quantum-resistant Root Program - Preparing and Applying for Inclusion
---

# [DRAFT] Preparing and Applying for Inclusion

## Last updated: 2026-08-14

The Chrome Quantum-resistant Root Program's (CQRP) primary commitment is to the security of Chrome's users. Chrome continuously works to improve the baseline of security on the web, and its policies, procedures, and initiatives reflect that goal. Every [Merkle Tree Certificate](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) Certification Authority (MTC CA) and Mirroring Cosigner in the Chrome Quantum-resistant Root Store (CQRS) is a critical link in the chain of trust relied upon by Chrome’s billions of users. Any compromise or misoperation by a single operator can have cascading, detrimental effects, with harm not limited to Subscribers of the corresponding operator.

Ultimately, in order for an operator’s inclusion request to be accepted, it must clearly and unequivocally demonstrate how their organization meets the high standards defined in the [CQRP Policy](draft-policy.md). The burden of proof rests entirely on the entity applying to proactively and unquestionably demonstrate this commitment, thereby clearly offsetting the inherent and significant security risks of inclusion. 

Google includes or removes operators in the CQRS as it deems appropriate at its sole discretion. Google selects and continues to include Cosigner keys to enhance Chrome's security. Operators included in the CQRS must provide value to Chrome end users that clearly exceeds the risk of their continued inclusion. To that end, the CQRP Policy defines the minimum requirements that MTC CA Operators and Mirroring Operators must meet for both initial and continued inclusion in the CQRS. The policy is periodically updated to further promote the CQRP’s goals: **security, simplicity, predictability, transparency,** and **resilience**.

> [!NOTE]
> A future update to this process may require the use of the Common CA Database ([CCADB](https://www.ccadb.org/)) for inclusion submissions, rather than using the [Chromium Issues Tracker](https://issues.chromium.org/u/0/issues/new?component=2114629&pli=1&authuser=0&template=0).

## 1. Roles and Prerequisites for Inclusion Requests

Entities interested in applying for inclusion to the CQRS can do so under one of 2 operational roles:

1. **Mirroring Operator:** Responsible for operating a Mirroring Cosigner service to cosign issuance log views, guaranteeing ecosystem transparency and split-view resistance. A Mirroring Operator that is not also an MTC CA Operator is referred to as an “Independent Mirroring Operator.”  
2. **MTC CA Operator:** Responsible for Subscriber certificate issuance and issuance log operation. All MTC CA Operators need to also fulfill the duties of a Mirroring Operator.

Except for CT Log [operators](https://certificate.transparency.dev/logs/) with at least one “[usable](https://googlechrome.github.io/CertificateTransparency/log_states.html)” log in Chrome before February 1, 2026, demonstrating the high-availability infrastructure and operational maturity required for global certificate issuance, a CQRS Applicant applying to become an MTC CA Operator need to first be an Independent Mirroring Operator in good standing for at least 90 consecutive calendar days before submitting an MTC CA Operator inclusion request.

## 2. Submission Process

### 2.1. Initial Submission

CQRS inclusion requests are submitted using the Operator template [TODO: create and link to template] in the Chromium Issues Tracker. Depending on the intended role of the operator, specific information is required and described by the template. By creating a new issue in the Chromium Issue Tracker the entity is asserting they are organizationally distinct from all existing operators present in [cosigners.json](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json).

All application artifacts need to be hosted from a publicly-accessible Repository (as defined within the Baseline Requirements). At any point during its review, the CQRP may contact the operator seeking additional or clarifying information. Operators are expected to provide the requested information promptly, and no later than 14 days unless specified otherwise.

### 2.2. Updating Submissions

Inclusion request submissions are expected to remain up-to-date as operational representations change. This includes updating the issue in the Chromium Issues Tracker as planned key lifecycle events become known, as detailed in the subsections below.

If an Independent Mirroring Operator intends to apply for inclusion as an MTC CA Operator, they are expected to use their preexisting issue and provide the additional template details required for MTC CA Operators.

#### 2.2.1. Submitting new Mirroring Cosigner Keys

Existing Mirroring Operators can apply to have a new Mirroring Cosigner Key included in the CQRS by updating their existing issue on the Chromium Issue Tracker.

#### 2.2.2. Submitting new CA Cosigner Keys

Existing MTC CA Operators can apply to have CA Cosigner Keys rotated in the CQRS, which will be processed according to a quarterly schedule (targeted for processing on the 15th day of January, April, July, and October). This includes:

1. At least 30 days prior to the target quarterly update date, the existing MTC CA Operator will publish the new MTC CA Cosigner Certificates (i.e., Reserve CA Cosigner Keys) on its Repository, update their existing issue in the Chromium Issues Tracker with the new key information, and announce the planned addition to mtcs [at] chromium [dot] org. The announcement needs to include the URL to the MTC CA Operators [mtc-disclosures.json](disclosures/mtc-disclosures.schema.json) ([example](disclosures/mtc-disclosures.json)).   
2. After the CQRP reviews the issue and the key is added to the CQRS, the MTC CA Operator needs to update the issue explicitly stating when the Reserve CA Cosigner Key(s) are expected to transition to an Active state, which is when the MTC CA Operator can expect landmarks for the newly Active CA Cosigner Key(s) to be distributed to Chrome clients. 

## 3. Evaluation Process

Chrome evaluates inclusion requests through a structured review pipeline, generally adhering to the following high-level milestones:

1. Completeness Triage  
2. Beneficial Ownership and Due Diligence Review  
3. Public Discussion Period  
4. Technical Compliance and Audit Verification  
5. Inclusion Decision

Once an inclusion request has all required artifacts, ongoing monitoring will occur as the review progresses through the high-level milestones. 

All Mirroring Cosigners need to pass a minimum 30-day compliance monitoring period before becoming `Qualified`. Once `Qualified`, a Mirroring Cosigner that maintains ongoing compliance with the CQRP policy will automatically transition to `Usable` after a 70-day propagation period, at which point its cosignatures will be relied upon for Chrome client validation. During this time, the CQRP will actively monitor the Mirroring Cosigner to ensure conformance to the technical specifications and availability requirements included in the CQRP Policy. In the event that the Mirroring Cosigner does not maintain ongoing compliance with the CQRP Policy, it will not be promoted `Usable`.

All operators should expect ongoing querying of their cosigners from Google’s compliance monitoring infrastructure throughout the lifetime of the mirror and/or issuance log.

## 4. Potential Outcomes

Inclusion requests may conclude with one of the following outcomes:

* **Accepted**: An inclusion application is classified as “Accepted” when an entity proactively and unequivocally demonstrates full compliance with all technical, operational, procedural, and audit requirements defined within the CQRP Policy, and clearly establishes that the value of its inclusion for Chrome end users exceeds the associated security, privacy, and operational risks.  
    
  Upon receiving an Accepted determination, the entity's key material, endpoints, and associated trust metadata will be scheduled for inclusion in the CQRS and distributed to Chrome clients on approximately, but not limited to, a targeted quarterly release cycle. However, the CQRP makes no guarantees on the timeliness of distribution. 

  Acceptance does not constitute a permanent, irrevocable, or unconditional guarantee of trust. Included operators need to continuously maintain adherence to all ongoing policy obligations - including compliance monitoring metrics (uptime, cryptographic correctness, and mirror consistency) and prompt incident reporting. The CQRP reserves the right to modify, suspend, or revoke inclusion at its sole discretion if an operator fails to sustain these standards or if the risk of continued inclusion outweighs the benefit to Chrome users.

* **Rejected**: An inclusion application is classified as “Rejected” when an entity fails to unequivocally demonstrate that the value of its inclusion to Chrome end users clearly exceeds the associated security, privacy, or operational risks. Rejection typically results from unaddressed technical, audit, or procedural deficiencies, incomplete or inaccurate disclosures, an incident reporting history that fails to reliably demonstrate the factors that are significant to the CQRP, or a failure to satisfy the minimum requirements defined within the CQRP Policy.  
    
  An organization whose application is Rejected is typically subject to a standard 6 month cooling-off period, beginning on the date of the formal rejection determination. During this period, the organization is ineligible to submit new or revised inclusion requests to the CQRP. This cooling-off period provides the organization sufficient time to remediate identified deficiencies, demonstrate sustained operational stability, and obtain updated, compliant audit attestations prior to re-applying.  
    
* **Disqualified**: An entity is classified as “Disqualified” when the CQRP determines that they present an unacceptable or unmitigable risk to Chrome end users or the integrity of the web. Disqualification is reserved for, but not limited to:  
  * Being the subject of multiple application Rejections without demonstrating meaningful and measurable remediation;  
  * Intentional misrepresentation, falsification, or material omission of facts in public disclosures, audit attestations, or program communications;  
  * Willful non-compliance with the CQRP Policy; or  
  * Critical failures, key compromises, or operational practices that demonstrate an inability or unwillingness to maintain a robust "security-first" culture.  
    

  An entity designated as Disqualified is permanently barred from applying for or receiving inclusion in the CQRS across all current and future PKI hierarchies operated, owned, or controlled by the organization, its subsidiaries, or its affiliates.
