---
title: Moving Forward, Together
---
# Moving Forward, Together

## Last updated: 2026-XX-XX

For more than the last decade, community members have tirelessly worked together to make the Internet a safer place. However, there’s still more work to be done. While we don’t know exactly what the future looks like, we remain focused on promoting changes that increase speed, security, stability, and simplicity throughout the ecosystem.

With those goals in mind, the Chrome Root Program continues to explore introducing future requirements related to the following themes:

*   Encouraging modern infrastructures and agility
*   Focusing on simplicity
*   Promoting automation
*   Reducing misissuance
*   Increasing accountability and ecosystem integrity
*   Streamlining and improving domain control validation practices
*   Preparing for a post-quantum world

## Understanding "Moving Forward, Together" initiatives

The initiatives described on this page are distinct from the requirements detailed in the [Chrome Root Program Policy](index). These initiatives are proposals for exploration. They are not requirements.

Some proposals may change during our review process, after considering community feedback, or studying the ecosystem impacts and tradeoffs of adoption. Others may not be adopted at all.

As an example, community feedback shaped the adoption of a previous "Moving Forward, Together" initiative promoting Certification Authority (CA) agility. This proposal  placed a limit on the duration of a root CA certificate’s inclusion in the Chrome Root Store (i.e., root "term-limit"). Based on feedback from the CA Owners included in the Chrome Root Store and as a result of studying data from publicly-available sources related to certificate ubiquity, we extended the duration of the initially proposed term-limit from 7 to 15 years and landed these changes in Version 1.5 of the Chrome Root Program Policy.

### Why communicate these initiatives?

Our program prioritizes transparency and recognizes that significant change takes time, careful planning, and collaboration. Many initiatives in "Moving Forward, Together" represent significant shifts within the ecosystem, and we want to minimize adverse ecosystem impacts when appropriate and possible. By sharing our initiatives early, we aim to understand the challenges stakeholders may face, collaboratively develop solutions to meet stated goals, and ultimately amplify the positive impact of these changes while reducing the negative.

### When might these initiatives take effect?

We understand the enthusiasm within the community regarding some of the proposals described on this page. However, we want to emphasize that there are currently **no planned implementation timelines** for these initiatives, unless explicitly stated below, in the Chrome Root Program Policy, or in [CA/Browser Forum Server Certificate Working Group Ballots.](https://cabforum.org/working-groups/server/ballots/) Again, not all proposals and initiatives may be ultimately adopted by the Chrome Root Program Policy.

### How might these initiatives take effect?

Some of the proposals described on this page might be achieved through collaborations within the CA/Browser Forum. In other cases, it might be most appropriate for corresponding changes to land only in the Chrome Root Program Policy, as not all CA Owners who adhere to the CA/Browser Forum TLS Baseline Requirements intend to serve Chrome’s focused PKI use case of server (i.e., website) authentication, or wish to be trusted by default in Chrome. Regardless of how these proposals might eventually be implemented, we are committed to collaborating with community members and deeply value their feedback.

### What informs our approach?

To explore and understand the broader ecosystem impacts of these proposals, we:

*   study ecosystem data from publicly available tools like [crt.sh](http://crt.sh) and [Censys](https://censys.com/),
*   interpret data resulting from Chrome tools, experiments, and usage data,
*   evaluate peer-reviewed research,
*   collect direct feedback through surveys shared with the CA Owners included in the Chrome Root Store,
*   communicate with members of the community using the Common CA Database [discussion forums](https://groups.google.com/a/ccadb.org/g/public), and
*   monitor indirect feedback from ecosystem stakeholders across a number of communications channels.

This helps ensure our decisions are informed by real-world data, observed Chrome user behavior, expert research, and the many voices of the community.

## Areas under exploration:

### Experiment and evolve the ecosystem through Photosynthesis

**Themes:** (1) "Encouraging modern infrastructures and agility", (2) "Focusing on simplicity", and (3) "Preparing for a post-quantum world"

**Understanding the Post-Quantum challenge:** The rise of quantum computing poses two significant threats to HTTPS. 

The first is the threat to traffic generated today. An adversary could store encrypted traffic now, wait for a [cryptographically-relevant quantum computer ("CRQC")](https://media.defense.gov/2021/Aug/04/2002821837/-1/-1/1/Quantum_FAQs_20210804.PDF) to become practical, and then use it to decrypt the traffic after the fact. This is commonly known as a ["store-now-decrypt-later"](https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later) attack. Chrome has mitigated this risk through the [deployment of post-quantum key exchange](https://blog.chromium.org/2024/05/advancing-our-amazing-bet-on-asymmetric.html).

The second threat is that future traffic is vulnerable to impersonation by a quantum computer. Once a CRQC exists, it could break the asymmetric cryptography used for authentication in HTTPS. To defend against impersonation from a CRQC, we need to migrate all of the asymmetric cryptography used for authentication to post-quantum variants. Unfortunately, post-quantum keys and signatures have a fundamental problem: their size. A single post-quantum signature can be over 20 times larger than the classical cryptography signatures commonly used today (e.g., ECDSA). Considering that secure connections in Chrome often rely on more than 5 signatures and 2 public keys, attempting to use post-quantum cryptography as a "drop-in" replacement within the existing ecosystem would drastically [degrade internet performance](https://blog.cloudflare.com/another-look-at-pq-signatures/). **For this reason Chrome has no immediate plan to add traditional X.509 certificates containing post-quantum cryptography to the Chrome Root Store and will only do so as a last resort.**

Instead, Chrome, in collaboration with other partners, is exploring a fundamental [evolution](https://drive.google.com/file/d/1KQXAGBHXR4S_prwFrZlyfA6DrpvfJwuJ/view) of the ecosystem based on [Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-davidben-tls-merkle-tree-certs/) (MTCs), a concept often referred to as "Photosynthesis". MTCs replace the heavy, serialized chain of signatures found in traditional PKI with compact Merkle Tree proofs. In this model, a CA signs a single "Tree Head" representing potentially millions of certificates, and the "certificate" sent to the browser is merely a lightweight proof of inclusion in that tree.

**Why it matters:**
*   **Enables feasible Post-Quantum security:** MTCs allow the ecosystem to adopt robust post-quantum algorithms without incurring the massive bandwidth penalty of legacy certificate chains. It decouples the security strength of the algorithm from the size of the data transmitted to the user.
*   **Improves performance:** By shrinking the authentication data in a TLS handshake to the absolute minimum, MTCs prevent the latency and fragmentation issues that would otherwise plague a post-quantum web.
*   **Bakes in transparency:** In the current ecosystem, Certificate Transparency (CT) is an "add-on" that adds extra overhead to the TLS handshake. With MTCs, transparency is a fundamental property of issuance; a certificate cannot be trusted by a client unless it is included in the public tree.

### Modernizing issuing CA infrastructure

**Themes:** (1) "Encouraging modern infrastructures and agility" and (2) "Focusing on simplicity"

**Understanding modern issuance practices:** Today, the "intermediate" or "issuing" CAs that sit between the Root and the leaf certificate presented by a server are traditionally treated as static, long-lived infrastructure. Often valid for a decade or more, these intermediates can become single points of failure. If an intermediate CA is compromised or needs replacement due to an unforeseen circumstance, for example a cryptographic vulnerability, the "blast radius" can be massive, potentially requiring the revocation of tens or hundreds of millions of certificates.

To address this, the Chrome Root Program is exploring policies that encourage a shift toward more ephemeral and dynamic CA infrastructure. This includes:
*   **Reducing maximum validity**: Limiting the currently unbounded lifetime of Subordinate CA certificates to ensure they naturally expire and cycle out of the ecosystem faster.
*   **Faster issuer rotation**: Encouraging CAs to frequently rotate the active issuing key(s). This ensures that any single key is responsible for a smaller "shard" of the total certificate volume.
*   **Issuance randomization**: Promoting the use of dynamic or randomized intermediates. By issuing certificates from a changing pool of intermediates, rather than a single static issuer, reliance on specific issuer identities is reduced.

**Why it matters:**
*   **Reduces blast radius:** Frequent rotation and randomization mean that if an issuing key is compromised or needs decommissioning, it only impacts a small slice of valid certificates (those issued from that specific CA during that specific window), rather than the CA's full certificate corpus.
*   **Prevents rigid dependencies:** Dynamic issuance discourages "pinning" (where software hard-codes trust in a specific CA). This improves compatibility and uptime when CAs need to replace infrastructure, and decreases the likelihood of operational footguns.
*   **Increases resilience:** Shorter-lived, agile intermediates allow the ecosystem to adopt new practices and cryptographic standards (like Post-Quantum Cryptography) much faster, as there is less "legacy debt" tied to old certificates or keys.

### Further sunsetting legacy practices

**Themes:** (1) "Focusing on simplicity", (2) "Encouraging modern infrastructures and agility", and (3) "Increasing accountability and ecosystem integrity"

**Understanding legacy practices:** As the ecosystem evolves, standards bodies like the CA/Browser Forum frequently prohibit creating new artifacts using outdated standards or practices (such as prohibiting the issuance of new certificates signed with SHA-1). However, these changes sometimes create significant gaps by exempting existing infrastructure from the scope of improved requirements, allowing legacy CAs and practices to remain valid and trusted simply because they were created before a certain date.

This creates a fragmented security model where "legacy" infrastructure operates under outdated rules, effectively indefinitely. While SHA-1, which still appears in time-valid CA certificates and CRLs trusted by Chrome, is the most prominent example, this issue extends to other legacy practices that should no longer be considered relevant or acceptable in 2025 and beyond. The Chrome Root Program is exploring steps to close these gaps by removing exceptions for legacy systems and practices, ensuring that all trusted PKI artifacts, regardless of their creation date or inclusion in the Chrome Root Store, adhere to modern security standards.

**Why it matters:**
*   **Ensures uniform security:** Vulnerabilities do not respect historical exemptions. A cryptographically broken artifact poses a risk to the ecosystem regardless of when it was issued.
*   **Reduces ecosystem complexity:** Maintaining special-case logic to support deprecated artifacts or practices forces browsers and relying parties to carry technical debt and compatibility code, which complicates validation logic.
*   **Retires unmanaged infrastructure:** Legacy CAs that have existed for decades are often less agile and may not adhere to contemporary operational best practices. Forcing their retirement ensures the ecosystem runs on modern, actively managed infrastructure that closely aligns with modern security expectations. Doing so also reduces risk associated with lingering but unknown vulnerabilities, while also creating opportunities for process improvement and ensuring capability retention. 

## Areas of future exploration:

The following initiatives are planned for future exploration by the Chrome Root Program Team. As observed with several areas of past exploration, for example "[Multi-Perspective Issuance Corroboration](#require-multi-perspective-issuance-corroboration)," the Chrome Root Program Team looks forward to pursuing these security-enhancing initiatives within the CA/Browser Forum Server Certificate Working Group, when appropriate.

### Verifiable and Reproducible Domain Control Validation
**Themes:** (1) "Increasing accountability and ecosystem integrity" and (2) "Streamlining and improving domain control validation practices"

**Understanding reproducible validation:** Currently, Domain Control Validation (DCV) is often an opaque process: a CA generates a random challenge, communicates it to the certificate requestor, performs a check (like querying a DNS record) from its own internal perspective, logs success, and issues the certificate. This process can take less than a second yet can have long-lasting security implications. If a bug or vulnerability is later discovered in the CA's validation logic, there is no way to verify if the validation actually succeeded at that time, often necessitating mass revocations to protect the ecosystem.

"Reproducible" Domain Control Validation proposes a model where the proof of domain control is made publicly and persistently available, allowing any party, not just the issuing CA, to independently and retroactively verify the validation's legitimacy. Defining this model's practical implementation is a key objective we look forward to pursuing with the broader community.

**Why it matters:**
*   **Prevents mass revocations:** If a CA has a software flaw, certificates corroborated by external monitors may not need to be revoked, as the "receipts" prove the domain control was valid despite the CA's internal bug.
*   **Increases integrity:** Shifts trust from a single CA's internal logs to a validation model that is observable and verifiable by the broader ecosystem.
*   **Bakes in validation from multiple perspectives:** Corroboration from diverse network vantage points ensures that a CA isn't tricked by localized network attacks (like BGP hijacking) that might otherwise pass a single-point check. This complements existing [Multi-Perspective Issuance Corroboration](#require-multi-perspective-issuance-corroboration) implementations.

### Further promoting adoption of ARI and ARI-like capabilities

**Themes:** (1) "Promoting automation" and (2) "Encouraging modern infrastructures and agility"

**Understanding ARI:** ACME Renewal Information (ARI) is a [standard](https://datatracker.ietf.org/doc/rfc9773/) that transforms certificate renewal from a static, client-driven guess into a dynamic, server-driven signal. Instead of clients hard-coding renewal logic (e.g., "renew 30 days before expiration"), ARI allows the CA to explicitly signal when a certificate should be renewed.

While simple in concept, this capability is critical for ecosystem resilience. It creates a direct communication channel for CAs to prioritize specific renewals, whether to smooth out infrastructure load or to urgently replace certificates in response to security incidents.

**Why it matters:**
*   **Automates incident response:** In the event of a mass revocation (e.g., due to a CA compliance incident or a cryptographic vulnerability like Heartbleed), ARI allows CAs to signal clients to renew immediately, potentially automating the replacement of millions of certificates without human intervention.
*   **Facilitates agility:** As certificate lifetimes shorten (e.g., to 45 days or less), ARI prevents clients from misconfiguring renewal windows, ensuring they adapt automatically to new validity periods.
*   **Improves stability:** CAs can use ARI to spread renewal traffic over time, preventing dangerous load spikes that could cause issuance outages.

## Past accomplishments:

### Sunset less secure DCV methods

**Themes:** (1) "Encouraging modern infrastructures and agility", (2) "Focusing on simplicity", (3) "Promoting automation", (4) "Reducing misissuance", (5) "Increasing accountability and ecosystem integrity", and (6) "Streamlining and improving domain control validation practices"

**Understanding DCV sunsets:** DCV is a security-critical process designed to ensure that certificates are only issued to a legitimate domain operator. This prevents unauthorized entities from obtaining a certificate for a domain they do not control. Without this check, an attacker could obtain a valid certificate for a legitimate website and use it to impersonate that site or intercept web traffic.

Historically, the ecosystem permitted validation methods that relied on "indirect" communication channels like email or phone calls. These methods, some of which were [proven](https://labs.watchtowr.com/we-spent-20-to-achieve-rce-and-accidentally-became-the-admins-of-mobi/) vulnerable, represent a "weak link" in the security chain because they only demonstrate that an applicant can interact with a contact associated with the domain, rather than proving direct administrative control over the domain's infrastructure. Furthermore, these methods inherit the vulnerabilities of their underlying channels, such as BGP hijacking, SIM swapping, and opportunistic TLS downgrades, and expand the attack surface by involving third-party service providers.

To address this, the Chrome Root Program collaborated with members of the ecosystem in the CA/Browser Forum to pass Ballots [SC-080](https://cabforum.org/2024/11/14/ballot-sc080v3-sunset-the-use-of-whois-to-identify-domain-contacts-and-relying-dcv-methods/), [SC-090](https://cabforum.org/2025/11/20/ballot-sc-090-gradually-sunset-all-remaining-email-based-phone-based-and-crossover-validation-methods-from-sections-3.2.2.4-and-3.2.2.5/), and [SC-091](https://www.google.com/search?q=https://cabforum.org/2025/11/12/ballot-sc-091-sunset-3-2-2-5-3-reverse-address-lookup-validation-proposal-of-new-dns-based-validation-using-persistent-dcv-txt-record-for-ip-addresses/). These ballots sunset these legacy methods in favor of automated, cryptographically verifiable alternatives (like ACME-based DNS or HTTP challenges) that confine the attack surface to the validated domain itself.

**Why it matters:**
*   **Enhances security:** These changes make it harder for attackers to trick a CA into issuing a certificate for a domain they don’t control. This reduces the risk that stale or indirect signals, (like outdated WHOIS data, complex phone and email ecosystems, or inherited infrastructure) can be abused.
*   **Encourages automation:** The shift toward standardized validation methods pushes the ecosystem toward modern, auditable practices and away from complex, manual workflows.

### Phase out "multi-purpose roots" from the Chrome Root Store

**Themes:** (1) "Encouraging modern infrastructures and agility" and (2) "Focusing on simplicity"

**Understanding dedicated hierarchies:** Certificates issued by publicly-trusted CA Owners (i.e., those included in various product and operating system trust stores) serve various use cases including TLS server authentication, TLS client authentication, secure email (e.g., signed and encrypted email), document signing, code signing, and others. Up until about 2018, it was common to see some or all of these use cases served from a single PKI hierarchy. While this approach offered flexibility to some stakeholders, balancing multiple, sometimes competing use cases and requirements presents inherent complexity, especially as the CA/Browser Forum created additional standards focused on use cases beyond TLS.

Beginning in September 2022, the Chrome Root Program [codified](policy-archive/policy-version-1-1#4-dedicated-tls-pki-hierarchies) its commitment to simplicity by requiring applicant PKI hierarchies submitted for inclusion in the Chrome Root Store focus only on serving TLS use cases. However, while that approach promoted future simplicity, not all CA certificates included in the Chrome Root Store aligned with this principle. To address this, and to completely realize the benefits of the transition to TLS-dedicated hierarchies, Chrome Root Program Policy Version 1.6 established a future phase-out of existing "multi-purpose" root CA certificates, or those CA certificates not dedicated to TLS server authentication use cases, from the Chrome Root Store. The adoption process is ongoing, but is expected to complete by the end of 2027.

**Why it matters:**
*   **Improves security by reducing attack surface:** Today, Chrome transitively trusts over 2,300 CA certificates, however, only about half of these CAs issue TLS server authentication certificates, the only PKI use case applicable for Chrome when authenticating websites. Removing out-of-scope CAs from Chrome’s security boundary results in fewer potential points of vulnerability, reducing risk for Chrome users.
*   **Promotes simplicity:** Dedicated-use hierarchies reduce complexity, clarify priorities, and improve maintainability for the use cases they serve. This simplicity can lead to more effective policies, practices, and operations compared to multi-use hierarchies that try to address multiple disparate requirements and standards at once.
*   **Focuses innovation:** By focusing on purpose-built hierarchies, the community can work together to more directly satisfy the specific needs of TLS certificate subscriber use cases (e.g., improve support for automation) and allow unencumbered innovation and iteration, rather than being obligated to satisfy the lowest common denominator of many different subscriber-type use cases or corresponding certificate issuance and management requirements.
*   **Decouples public and private PKI use cases:** Client authentication represents a private PKI use case that web browsers do not rely upon for website authentication. Issuing certificates intended for client authentication by CAs that validate to certificates included in public root stores, like the Chrome Root Store, means CAs and sometimes by extension, subscribers, are obligated to adhere to the CA/Browser Forum TLS Baseline Requirements and root program policies. In some cases, this approach actively harms both subscribers and CA Owners. Serving client authentication use cases from private PKI hierarchies (i.e., those not trusted by public root stores) may promote enhanced security and control, offer improved scalability and flexibility, and advance the CA Owner’s ability to satisfy their subscribers' unique use cases while promoting meaningful security improvements to TLS server authentication.

### Reduced certificate lifetimes and validation reuse

**Themes:** (1) "Encouraging modern infrastructures and agility", (2) "Promoting automation", and (3) "Streamlining and improving domain control validation practices"

**Understanding certificate lifetimes and validation reuse:** Certificates represent a "point-in-time" state of reality; the more time passes from the moment of issuance, the more likely it becomes that the data represented in the certificate diverges from reality. For years, the Chrome Root Program advocated for shorter certificate lifespans to address this divergence and improve ecosystem agility. This effort, with collaboration from other members of the ecosystem, culminated in Ballot [SC-081v3](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/), which was passed by the CA/Browser Forum in 2025.

This ballot establishes a roadmap to reduce the maximum validity of publicly-trusted TLS certificates from 398 days down to 47 days. It also introduces a significant reduction in DCV reuse periods, eventually bringing the limit for reusing validation data down to just 10 days. Previously, a single validation check could be used for over two years, creating a risk that certificates were issued based on [stale ownership information](https://insecure.design/). These changes are scheduled to phase in starting March 2026 and concluding in March 2029.

**Why it matters:**
*   **Increases agility and cryptographic safety:** Deprecating ecosystem practices (e.g., use of a specific cryptographic algorithm) is a complex process; a reduced maximum validity period provides substantial support for smoothly, and when necessary, swiftly transitioning between practices when weaknesses are identified.
*   **Reduces risk of stale data:** Because certificates represent a verification performed at a specific moment, reducing lifetimes [minimizes](https://zanema.com/papers/imc23_stale_certs.pdf) the period in which a certificate remains valid after the information it contains is no longer accurate.
*   **Reduces reliance on revocation checks:** Certificate status services (like CRLs and OCSP) often struggle with privacy, performance, and timeliness; shorter certificate lifetimes provide firm protection to users independent of these services.
*   **Drives automation:** Frequent renewal necessitates automation, which improves the consistency, quality, and stability of certificate lifecycle management across the ecosystem.

### Require "Multi-Perspective Issuance Corroboration"

**Themes:** (1) "Increasing accountability and ecosystem integrity" and (2) "Streamlining and improving domain control validation practices"

**Understanding Multi-Perspective Issuance Corroboration:**

Despite the then existing domain control validation requirements defined by the CA/Browser Forum, peer-reviewed research authored by the Center for Information Technology Policy of Princeton University ([1](https://www.usenix.org/conference/usenixsecurity18/presentation/birge-lee) and [2](https://www.usenix.org/conference/usenixsecurity21/presentation/birge-lee)) and others (e.g., [3](https://dl.acm.org/doi/10.1145/3243734.3243790)) highlights the risk of equally-specific prefix Border Gateway Protocol (BGP) attacks or hijacks resulting in fraudulently issued certificates. This risk is not merely theoretical, as it has been demonstrated that attackers have successfully exploited this ongoing vulnerability on numerous occasions, with just [one](https://freedom-to-tinker.com/2022/03/09/attackers-exploit-fundamental-flaw-in-the-webs-security-to-steal-2-million-in-cryptocurrency/) of these attacks resulting in approximately $2 million dollars of direct losses.

Multi-Perspective Issuance Corroboration (referred to as "MPIC"), sometimes referred to as "Multi-Perspective Domain Validation" ("MPDV") or "Multi-VA", enhances existing domain control validation methods by reducing the likelihood that routing attacks can result in fraudulently issued certificates. Rather than performing domain control validation and authorization from a single geographic or routing vantage point, which an adversary could influence as demonstrated by security researchers, MPIC implementations perform the same validation from multiple geographic locations and/or Internet Service Providers and have been [observed](https://drive.google.com/file/d/15e4Z9InYbThwJsDuH0oS7vfXKvdSBzi9/view) as an effective countermeasure against ethically conducted, real-world BGP hijacks ([4](https://arxiv.org/abs/2302.08000)).

The Chrome Root Program [led](https://drive.google.com/file/d/1LTwtAwHXcSaPVSsqKQztNJrV2ozHJ7ZL/view?usp=sharing) a work team of ecosystem participants which culminated in a CA/Browser Forum Ballot to require adoption of MPIC via [Ballot SC-067](https://cabforum.org/2024/08/05/ballot-sc067v3-require-domain-validation-and-caa-checks-to-be-performed-from-multiple-network-perspectives-corroboration/). The ballot received unanimous support from organizations who participated in voting, and the adoption process is ongoing.

**Why it matters:**

*   **Enhances security:** MPIC improves protection against equally-specific prefix BGP attacks or hijacks. Unless all publicly-trusted CA Owners adopt MPIC, it will be possible for attackers to target those who do not to obtain fraudulently issued certificates.

### Establishing minimum expectations for linting

**Themes:** (1) "Encouraging modern infrastructures and agility" and (2) "Reducing misissuance"

**Understanding linting:**

Linting refers to the automated process of analyzing X.509 certificates for errors, inconsistencies, and adherence to best practices and industry standards. Linting ensures certificates are well-formatted and include the necessary data for their intended use, such as website authentication. There are numerous open-source linting projects in existence (e.g., [certlint](https://github.com/certlint/certlint), [pkilint](https://github.com/digicert/pkilint), [pkimetal](https://github.com/pkimetal/pkimetal), [x509lint](https://github.com/kroeckx/x509lint), and [zlint](https://github.com/zmap/zlint)), in addition to numerous custom linting projects maintained by members of the Web PKI ecosystem.

The Chrome Root Program participated in drafting CA/Browser Forum [Ballot SC-075](https://cabforum.org/2024/08/05/ballot-sc-075-pre-sign-linting/) to require adoption of certificate linting. The ballot received unanimous support from organizations who participated in voting, and the adoption process is ongoing.

**Why it matters:**

*   **Enhances security:** Linting can expose the use of weak or obsolete cryptographic algorithms and other known insecure practices, improving overall security.
*   **Reduces misissuance:** Linting helps CA Owners reduce the risk of non-compliance with industry standards (e.g., CA/Browser Forum TLS Baseline Requirements). Non-compliance can result in certificates being "mis-issued". By detecting these issues before certificate distribution to Subscribers, the likelihood and negative impact associated with having to correct the mis-issued certificate(s) can be reduced.

### Root CA term-limit

**Theme:** "Encouraging modern infrastructures and agility"

In Chrome Root Program Policy 1.5, we [landed](policy-archive/policy-version-1-5#root-ca-term-limit) changes that set a maximum "term-limit" (i.e., period of inclusion) for root CA certificates included in the Chrome Root Store to 15 years.

While we still prefer a more agile approach, and may again explore this in the future, we encourage CA Owners to explore how they can adopt more frequent root rotation.

**Why it matters:**

*   **Helps realize the value of continuous improvement:** The Baseline Requirements, the audit schemes permitted therein, and the ecosystem’s processes and practices have been in a state of continuous improvement since their inception. Aligning ongoing practices with modern requirements, audit frameworks, and best practices is the best way of benefiting from that improvement - and the lessons we’ve learned along the way.
*   **Promotes agility:** Reducing over reliance on a specific root or set of roots eliminate single points of failure, while also helping to discourage potentially dangerous practices like key pinning.
*   **Helps reduce risk:** Particularly, they help re-establish a known good baseline that otherwise may have been unknowingly lost over what is now sometimes a 35 year period of time. Reducing the functional lifetime that a Root CA is relied upon reduces the maximum window of potential abuse.

### Improve automation support

**Themes:** (1) "Encouraging modern infrastructures and agility", (2) "Focusing on simplicity" and (3) "Promoting automation"

In Chrome Root Program Policy 1.5, we landed changes that require Applicant hierarchies to support automated certificate issuance and management. For more information on automation, refer to our blog post: "[Unlocking the power of automation for a safer and more reliable Internet.](https://blog.chromium.org/2023/10/unlocking-power-of-tls-certificate.html)"

**Why it matters:**

*   **Promotes agility:** Automation increases the speed at which the benefits of new security capabilities are realized.
*   **Increases resilience and reliability:** Automation eliminates human error and can help scale the certificate management process across complex environments. Innovations like ACME Renewal Information (ARI) present opportunities to seamlessly protect site-owners and organizations from outages related to unforeseen events.
*   **Increases efficiency:** Automation reduces the time and resources required to manually manage certificates. Team members are instead free to focus on more strategic, value-adding activities.

### Make OCSP optional and incentivize automation

**Themes:** (1) "Encouraging modern infrastructures and agility", (2) "Focusing on simplicity", and (3) "Promoting automation"

We proposed and collaborated with members of the CA/Browser Forum Server Certificate Working Group to pass [Ballot SC-063](https://cabforum.org/2023/07/14/ballot-sc-063-v4-make-ocsp-optional-require-crls-and-incentivize-automation/) which transitioned support for the Online Certificate Status Protocol (OCSP) from mandatory to optional within the TLS Baseline Requirements. The ballot also incentivized adoption of automation solutions by standardizing the definition of a "short-lived certificate" which is exempt from certificate revocation requirements defined in [Section 4.9.1](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#4911-reasons-for-revoking-a-subscriber-certificate) of the TLS Baseline Requirements. Ballot SC-063 became effective on March 15, 2024.

**Why it matters:**

*   **Improves privacy:** OCSP requests reveal details of individuals’ browsing history to the operator of the OCSP responder. These can be exposed accidentally (e.g., via data breach of logs) or intentionally (e.g., via subpoena). Due to privacy concerns, several certificate consumer products like Chrome **do not** perform online OCSP checks by default, while others have signaled interest in transitioning to privacy-preserving methods of communicating revocation status.
*   **Enhances security:** Subscriber certificate expiration is broadly and reliably enforced across major certificate consumers, while the same is not true for certificate revocation. From a security perspective, short-lived certificates may reduce the aperture of an attack where subscriber private keys are compromised - limiting the maximum attack window to just a few days. Short-lived certificates also present an opportunity to further reduce the size of Certificate Revocation Lists, which are relied upon by many certificate consumers.

### Clarify certificate profiles

**Themes:** (1) "Focusing on simplicity" and (2) "Reducing misissuance"

We proposed and collaborated with members of the CA/Browser Forum Server Certificate Working Group to pass [Ballot SC-062](https://cabforum.org/2023/03/17/ballot-sc62v2-certificate-profiles-update/) which clarified and improved upon the existing certificate profiles included within Section 7 of the TLS Baseline Requirements. The ballot received unanimous support from organizations who participated in voting and became effective on September 15, 2023.

**Why it matters:**

*   **Promotes simplicity:** The ballot better aligned TLS Baseline Requirements certificate content expectations across certificate issuers and consumers, reduced the opportunity for confusion resulting from the absence of a more precise certificate profile specification, and promoted more consistent and reliable implementations across the ecosystem.
