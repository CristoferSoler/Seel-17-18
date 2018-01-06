1 description
--------------

### 1.1 Introduction

Advanced Persistent Threats (APT) are targeted cyber attacks on selected institutions and facilities where an attacker gains permanent access to a network and subsequently broadens it to other IT systems. The attacks are characterized by a very high use of resources and considerable technical capabilities on the part of the attackers and are usually difficult to detect.

### 1.2 Life cycle

To be able to successfully clean up an APT incident requires strategic planning and then consistent action. This means first switching off IT systems in a targeted manner in order to lock out the attacker, then to purge them as planned and finally to bring the adjusted environment back into a productive state.

The steps that should be taken and the actions to follow in each step are listed below:

** planning and conception **

An APT incident can not be cleared until it has been detected and correctly classified as APT. This is done as part of the detection (see DER.1 * Detection of security-relevant events *), an initial forensic investigation (see DER.2.2 * Provisioning for IT forensics * and classic incident management (see building block DER.2.1 * Incident Management *) The measures in this module therefore need to be implemented only after the other components have been completed.

The cleanup of an APT incident is a large-scale, labor-intensive project. Therefore, successful management requires a steering committee that is responsible for planning, designing and tracking the necessary actions (see DER.2.3.M1 * Establishment of a governing body * ). An APT incident always represents an emergency, which is why it should be integrated with emergency management and the application of the measures defined there (see DER.4 * BCM, Emergency Management *). If it turns out that the incident has company-threatening dimensions, those responsible must coordinate with crisis management.

Typically, the cleanup of an APT incident, once discovered and classified, is preceded by a phase of observation of the attacker. This phase is designed to gather enough information to effectively lock out the attacker and eliminate any access channels he has established. As part of a clean-up strategy, the governing body determines whether an observation period is being carried out, how long it lasts and what action is being taken to monitor the aggressor (see DER.2.3.M2 * Decision on a clean-up strategy *). Furthermore, this strategy will determine the exact course of action that will be taken to clean up IT systems. This can range from the targeted elimination of individual infections to the re-establishment of IT systems to the replacement of affected IT systems (see DER.2.3.M9 * Hardware Replacement of Affected IT Systems *).

Since the attacker can potentially fully access and actively monitor the existing communication infrastructure of the institution concerned, it is necessary to coordinate the observation phase and the preparation of the cleanup via secure, independent communication channels (see DER.2.3.M8 * Establishment of secure, independent communication channels * ).

**Procurement**
Typically, various hardware and software components must be procured at short notice to clean up an APT incident. For example, secure communication mechanisms may need to be established (see DER.2.3.M8 * Establishment of secure, independent communication channels *), hardware for forensic investigations needs to be procured, and hardware may need to be replaced by high-security IT systems (see DER. 2.3.M9 * Hardware replacement of affected IT systems *). As procurements must be made on a very short-term basis, it may be necessary to bypass the institution's usual procurement channels. Furthermore, it should possibly be avoided that the incident prematurely in the institution or even beyond known. This may also play a role in procurement. The above requirements may cause conflicts with the usual requirements and processes for procurement. The governing body must therefore have far-reaching decision-making powers.

**Implementation**

The implementation of the cleanup begins with deliberately locking out the attacker. This process is often referred to as cut-off. The cut-off is usually realized by isolating the affected network areas (see DER.2.3.M3 * Isolation of affected network sections *).

Subsequently, the previously planned and decided strategy to clean up the affected IT systems can be implemented (see DER.2.3.M2 * Decision on a clean-up strategy *). In addition to the actual cleansing of the IT systems, the initial break-in path must also be closed (see DER.2.3.M5 * Closing the initial break-in path *) and all potentially compromised access data and key materials must be changed (see DER.2.3.M4 * Blocking and changing Credentials and cryptographic keys *).

Before the environment goes back into productive operation, measures should be taken to make it more difficult to compromise again, or to increase the likelihood of timely detection. Targeted hardening measures should be carried out for this purpose (DER.2.3.M7 * Targeted IT system hardening *). In addition, re-attacks by the same attacker should be made more difficult (see DER.2.3.M10 * Conversions to hinder a re-attack by the same attacker *).

Only when the environment has been completely cleaned up can it be put back into productive operation (DER.2.3.M6 * Return to productive operation *).

** ** segregation

While the cleanup strategy is being developed and forensic investigations are in progress, additional detection and logging mechanisms are usually created. These are often ad-hoc solutions that do not always meet the requirements of long-term productive operation. In most cases, the measures taken by data protection officers, works councils or company management are also only approved on a temporary basis, since, for example, data protection aspects can not be sufficiently taken into account. For these reasons, these IT systems often have to be discarded again. However, after cleansing, a phase of intensive observation of the affected area should be scheduled. If possible, the temporarily created infrastructure should continue to be used in this phase. A partial transfer of ad hoc monitoring infrastructure into productive operation to supplement already existing detection mechanisms (see also DER.1 * Detection of safety-relevant events *) should be examined.
When screening out IT systems used to monitor the attacker or for forensic analysis, it is important to ensure the secure deletion or destruction of all storage media, as they usually contain sensitive data. In addition, it may be necessary to examine whether forensic data must be securely archived in order to allow for further follow-up investigations or to secure evidence as evidence.

2 measures
-----------

The following is a list of specific implementation notes in the section "Cleaning Up Major Security Incidents."

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### DER.2.3.M1 Establishment of a governing body [Information Security Officer (ISB)]

Cleaning up an information network after an APT attack is a complex and extensive project. Usually, different parties have to be coordinated in the clarification and clarification, tactical and strategic decisions are made on a partly unclear information base and at the same time the clean-up activities are kept secret, at least for the short to medium term. To ensure these requirements, competent contact persons must control the clean-up activities. For this purpose, a governing body should be convened which has the following competences:

* ** Decision-making powers: ** Those responsible must make numerous decisions about how to proceed with the clean-up process. Often, the usual processes and specifications must be bypassed so that the process remains secret and time-critical processes can be performed immediately. Therefore, senior management staff of the institution should be included in the panel. The information security officer must also be a member of the governing body due to its interface function between technology and management and its fundamental responsibility.
* ** Competency: ** APT attacks are mostly technically very complex. Analyzing the incidents, devising an effective clean-up strategy, and developing measures to avoid being compromised require a lot of technical expertise and information security expertise. Therefore, on the one hand, experienced administrators should be involved in the committee, with as much cross-departmental knowledge as possible. On the other hand, internal or external forensic experts should be involved in the body at least in an advisory capacity.
* ** Administrative skills: ** Cleaning up an APT incident requires complex project management. Different parties must be coordinated and many tasks must be coordinated and implemented under great time pressure. During the observation phase, the facts are often still unclear. Therefore, due to the ever-changing information base and the actions to be derived from it, iterative action should be taken. Thus it is necessary to involve employees with a lot of competence in project management in the committee. These are responsible for creating schedules, assigning and tracking tasks, and coordinating committee members with the executing staff.
The governing body takes over the entire project management for the cleanup. All decisions, eg. Eg the duration of the observation phase, the IT systems to be analyzed, the time of the cut-off, are met by the governing body. In general, the panel is responsible for designing the cleanup strategy and planning and tracking its implementation.
To accomplish these tasks, the governing body should meet regularly. In addition, all panel members should only communicate with one another via secure communication channels (see DER.2.3.A7 * Establishment of secure, independent communication channels *).

If the IT is too compromised or if the necessary clean-up measures are very extensive, it may be that the institution concerned sets up a crisis staff. In this case, the governing body must monitor the clean-up activities. The governing body must then report to the crisis staff.

#### DER.2.3.M2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]

Before the cleanup is technically implemented, some strategic decisions need to be made. In most cases, the cleansing strategy is not completely defined, but constantly supplemented and adjusted by the steering committee based on new findings. Decisions on the cornerstones of the cleanup strategy should be documented by the performance committee. It is also helpful for practical work if the current status of the overall strategy is recorded and made available to the members of the executive committee and in excerpts to the implementing employees.

In the following, the most important decisions for a cleanup strategy are described in their order of application. The decisions are partly conditional, so that later decisions have to be taken very early.

* Before the actual cleanup are the observation phase and the cut-off. How long and detailed the observation phase should be is already the first part of the cleanup strategy. It should be determined what knowledge is needed for the cut-off and the cleanup. If a complete rebuilding of the infrastructure is already assumed in this phase, detailed knowledge can be dispensed with. However, if it is not ruled out that malware should later be intentionally deleted, so the IT systems may not need to be reinstalled, a great deal of information is needed on how the attack spread and how it worked. In addition, indicators for affected IT systems (Indicators of Compromise, IoC) will be required. The result of the observation phase should be an overview of the assets to be adjusted. If there are still investigations, the affected assets should also be documented with their status and the overviews should be updated regularly. The overviews are the basis for the cleanup later.
* The cut-off (see also DER.2.3.A3 * Isolation of affected network sections * and DER2.3.A4 * Blocking and modification of access data and cryptographic keys *) should always be planned without regard to later recommissioning. The cut-off partially or completely shuts down affected IT systems, network sections, and network devices, rendering them inaccessible. As a rule, cut-off and technical cleansing are planned together. How to implement a cut-off is described in DER.2.3.M3 * Isolation of affected network sections *. Before the cut-off, it should be examined how it affects the institution. Damage caused by the cleanup can significantly exceed the damage of the actual attack and be life-threatening. The governing body, together with the crisis management team, should, as appropriate, review appropriate temporary evasive solutions and prioritize the applications to be re-deployed. In this case, the building block DER.4 * BCM, Notfallmanagement * can be used.
* During the observation phase, an APT incident can still be treated confidentially. After a cut-off and during technical cleansing, the incident or impact is typically visible to employees, customers and business partners. It should therefore be timely defined how long the APT incident must be kept secret to ensure effective technical cleansing. For the period after the observation phase, a communication strategy should be drafted, including, for example, a legend for the visible failures, ready answers to possible inquiries or an accompanying press release. The strategy has to be announced to all directly involved employees. It can also be created with the help of PR staff or external PR agencies.
* During the cleanup there will probably be more requests to the help desk. The governing body should ensure that there is sufficient and adequately skilled staff at all stages to implement the clean-up actions and support the users. Even if the clean-up measures lead to major business interruptions, the helpdesk must remain able to work.
* Beyond the observation phase, appropriate monitoring measures must be established to assess whether the cut-off has been successful and to identify whether there are new attacking activities during or after the cleanup. It is important to ensure that this monitoring option is maintained throughout, even if system components are changed or replaced in the course of the cleanup. To ensure this, the monitoring measures should be documented in the clean-up strategy.
* Immediately after the cut-off, further forensic investigations can be made that were previously not possible without warning the attacker. This may result in further insights for the adjustment.
* Based on the overview of the affected IT systems and the analysis results, it is decided how the cleanup will be carried out. It must be decided and documented for each IT system whether it is completely reinstalled (possibly together with new hardware, see DER.2.3.A9 * hardware replacement of affected IT systems *), whether the malicious software and other changes made by the attacker are targeted removed or cleaned up, or if no cleanup is necessary. Basically, it is better to reinstall the IT systems than just purposely clean them up, as otherwise artifacts of the attacker could remain on the IT system. The measures can vary from IT system to IT system and therefore have to be coordinated for each IT system or for smaller groups.
* The governing body must prepare and agree on a timetable for the cleanup. In this case, the responsible z. For example, make sure that the institution remains functional or that the failures are as short as possible.
* The governing body should establish guidelines on whether and how backup data can be used. Backups that were created before the APT attack can usually be used. If the point of attack can not be determined with certainty or if only newer backups are available, the data to be backed up must be determined in a targeted manner. Installations and configurations should be rebuilt manually.
* If the analysis reveals that the attacker exploited operational or application software errors, it should be agreed with the manufacturer or internal developers when and how to correct them. If it is not possible to remedy the vulnerabilities in a timely manner and there are no other safeguards, the application should be discontinued for the time being.
* If subnets are cleared, the governing body decides when and how to reopen the accesses to these networks.
* After IT systems and networks have been put back into service, functional tests should be performed to verify that all applications are ready for use. The management committee then decides which temporary alternative solutions are to be dissolved or taken over permanently.
#### DER.2.3.M3 Isolation of affected network sections

The cleanup activities begin with the affected network areas being isolated. The goal is to completely deprive the attacker of access to the IT environment. This should be done in one go if possible so that the attacker does not notice prematurely that he has been discovered and may be able to take countermeasures. Therefore, the network sections must be isolated in a concerted action, the so-called cut-off.

In particular, those responsible should switch off all Internet access at one go in order to prevent the attacker from communicating with compromised IT systems. For this purpose, all access routes must be identified (see DER.2.3.M2 * Decision on a clean-up strategy *). These include, for example, central access, possibly existing Internet breakouts, eg. B. DSL connections at individual sites, redundant connections and emergency connections, z. Eg via UMTS / LTE. However, it is important to avoid accidentally reconnecting the IT environment to the Internet before cleanup is complete.

In order to isolate IT systems and networks, the connection should be physically separated as far as possible, for example by pulling out the corresponding power cable. This approach is safer than configuring firewall rules, access control lists, or VLANs to isolate the network. If there is any suspicion that network devices have been compromised, either the connections must be physically disconnected or the devices switched off.

If the forensic investigation has proven sufficiently certain that only individual network areas are compromised, for example a single Windows domain, then the cleanup can be limited to these segments. In this case, however, it must be ensured that the areas are reliably isolated from other network segments.

Especially mobile clients are difficult to isolate because IT may not be able to access all devices at the time of isolation. If mobile devices are to be cleaned up, it must first be ensured that all accesses (VPN, e-mail, etc.) of these devices to the internal network are disconnected. It must also be ensured that the accesses remain separate until the cleanup measures have been completed. Subsequently, users must be prompted to submit or return their terminal for cleanup.

#### DER.2.3.M4 Blocking and modification of credentials and cryptographic keys

The main goal of cleaning up a far-reaching security incident is to stop the attacker's access to the affected environment and prevent it in the future. For this, it is not enough to exclusively close the vulnerability that the attacker exploited for initial compromise. Rather, it must be assumed that he knows all the access data that existed on the compromised computers. Therefore, all access data must be changed after the network has been isolated.
Access data are locally stored IT system and application passwords as well as passwords of users who have logged on to the IT system in the affected period, as their passwords or access data derived from them may have been extracted from the main memory of the IT system , Furthermore, centrally managed access data must be reset, for. In Active Directory environments or when using Lightweight Directory Access Protocol (LDAP). If one of the central authentication servers (domain controller or LDAP server) has been compromised, all accesses existing there must be blocked and their passwords exchanged.

When a central authentication server is reset, special care must be taken. These are infrequently performed administration processes, which also often have technical pitfalls. For example, to protect yourself from so-called Golden Tickets, it is necessary to reset the password of the KRBTGT account twice. A Golden Ticket is a fake Kerberos ticket that can be used to issue new access tickets for a period of ten years. If the associated password is not reset or reset only once, then an attacker with a previously created Golden Ticket can continue to issue access tickets and access the IT system. Therefore, only experienced administrators with the assistance of internal or external forensics experts should take appropriate action.

Usually, in such a situation, large parts of the existing access data must be reset. Often this occurs at a time when most users know little or nothing about the security incident. A prior information of the user is often difficult to realize because the IT infrastructure is compromised and the attacker should not be informed ahead of time of the pending cleanup. For this reason, increased inquiries to the help or service desk can be expected. If possible, additional staff should be provided for the expected password requests. If possible, they should have a script containing the procedure and answers to the questions they are expecting. This script should be drafted as part of crisis management, possibly with the help of PR staff or external PR agencies. In particular, employees should be advised that no old passwords should be reused and they should not choose passwords that can be derived simply from old passwords.

If necessary, not only user accounts and their passwords must be reset on the affected IT systems, but also service accounts. These changes must be made by the administrators of the respective IT systems.
Care must also be taken to replace all cryptographic key material stored on compromised IT systems. These include, for example, TLS or SSH keys. If central keystores, such. For example, if a Certification Authority (CA) server of a self-managed Public Key Infrastructure (PKI) has been compromised, they must be rebuilt. This also implies that existing keys are locked there and eventually all derived key material has to be re-rolled. The certificates are to be blocked by a corresponding entry in a Certificate Revocation List (CRL) or on an OCSP server. Depending on the application of the compromised key, a global blocking by an external validation service may be necessary. In this case, it must be kept in mind that publishing cRL entries to an external validation service publicizes that the key may be compromised. Therefore, the timing of this action must be carefully chosen. Eventually, a corresponding accompanying communication strategy should also be developed.

#### DER.2.3.M5 Closing the initial break-in path

In order to prevent an attacker from accessing a compromised environment again, the initial break-in path of the APT attack must be closed. However, this must happen only after the affected network environments have been isolated. This prevents the attacker from being warned prematurely and possibly even sabotaging IT systems, obscuring traces or creating additional backdoors.

The initial attack path must be identified as part of the forensic analysis. If several vulnerabilities have been exploited for the compromise, then a prioritized removal of the vulnerabilities can take place if necessary.

The possible burglary paths can basically be divided into two classes: technical weaknesses and attacks on employees. For all technical vulnerabilities, the root cause must be identified and resolved. Typical examples are:

* The attacker used a known vulnerability in outdated software to access the IT system. In this case, it must be checked if there is an updated version of the software that is no longer vulnerable. The break-in path is usually closed when the software is updated.
* The attacker used a vulnerability that has no patches or is completely unknown (zero-day exploit). If the vulnerability is not publicly known, contact the software manufacturer or the internal developers to contact them to develop a patch or other countermeasure. Developing a patch may take longer. In the meantime, other immediate measures must be implemented. The affected IT system can, for. B. taken from the network or made unreachable by firewall rules. Consideration can also be given to protection by upstream IT systems specifically developed for the observed vulnerability, for example by using tailor-made rules in a web application firewall or an intrusion prevention system. However, special expertise is required for this.
* The attacker exploited a misconfigured IT system. Examples include the accidental publication of sensitive information on the Internet, the use of standard or easily guessable passwords on externally accessible IT systems or an unprotected service over the Internet. Here the basic problem has to be eliminated by a configuration change.
When attacks on employees, it is not easy to eliminate the original vulnerability, as such attacks can not be completely prevented by technical measures. Examples of such attacks include:

* The attackers send extremely credible phishing e-mails that either contain malicious software or force employees to enter sensitive information on untrusted pages.
* The attackers use so-called water-hole attacks, in which malicious software or phishing links are targeted to pages that are interesting for individual employees, so they are more likely to access.
Prior to such attacks, the institution may protect itself through awareness-raising (see ORP.3 * Information and Information Security Education *). Sensitized employees will also be more likely to detect and report attempts to attack, thus helping to detect attacks early. Awareness measures are useful after a successful APT incident, but should be done after cleanup.

However, technical measures can also be taken to ward off attacks on employees. For example, the IT systems should be specifically hardened (see DER.2.3.A7 * Targeted IT system hardening *) and measures implemented to monitor the IT environment (monitoring). Further technical measures are:

* Extend the antivirus infrastructure through additional checks on emails, outbound Internet traffic or client devices,
* the decoupling of the terminals from the Internet (for example by ReCoBS systems) or
* the introduction of two-factor authentication for particularly vulnerable accesses.
However, it should be avoided to punish successfully attacked employees. The quality of the APT attacks is very high and the e-mails or websites used are often extremely credible, making the attacks difficult to detect. In such a case, disciplinary measures would not only be unfair but would also lead to a loss of confidence, so that future attacks will no longer be reported and recognized early.

#### DER.2.3.M6 Return to productive operation

After the cleanup work is completed, the decoupled IT environment should be returned to production. So that the cleansing restricts the availability as little as possible, this step can be done step by step for individual network segments. In this case, however, it must be absolutely certain that uncleaned network sections will in no case be connected to already cleared ones.

It is often only possible to distribute new passwords and access data to end users at this stage. Increased support requests are expected (see DER.2.3.M4 * Blocking and changing access data and cryptographic keys *). Again, a gradual restart can reduce the requests or distribute them over time. If possible, functional tests should be performed before restarting productive operation to avoid support requests or error symptoms misinterpreted as attack symptoms.

The returned IT systems should be accompanied by increased monitoring. In this way, it is possible to identify renewed access attempts by the attacker and any previously overlooked backdoors. For this purpose, the monitoring systems set up during the observation phase can continue to be used. The temporarily set up monitoring and analysis systems should therefore continue to be operated for a period of time defined as part of the clean-up strategy and coordinated with data protection and staff representation. For this period, an increased effort for the monitoring is planned.
After this monitoring period has been completed, the monitoring and analysis systems should be disposed of or put into productive operation. When discarded, it must be decided whether and, if so, what evidence will be archived for further use (such as in-depth analysis, for evidence purposes or, if applicable, disclosure to law enforcement or investigative authorities). If the IT systems are to be archived, this may only be done in a sufficiently secure environment that meets the protection requirements of the evidence. Unnecessary evidence and IT systems that are discarded must be securely deleted or destroyed (see DER.2.3.M9 * Hardware Replacement of Affected IT Systems *). Even temporarily established communication and collaboration solutions should be dismantled.

If the monitoring and analysis systems go into productive operation, it must be checked whether they are also suitable for the intended application. Often, in the reconnaissance phase of APT incidents, ad hoc installations are performed that do not meet the requirements for medium or long-term productive operation. It may therefore be necessary to set up projects to revise the IT systems.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the area of ​​clearing up far-reaching security incidents.

#### DER.2.3.M7 Targeted system hardening

Often, an attacker does not exploit a single vulnerability, but uses different gaps over the course of an APT attack. In particular, attackers often combine and use various vulnerabilities, lack of IT system hardening, and inadequate detection mechanisms to move around the internal network and extend their privileges (privilege escalation). In addition to eliminating the initial break-in path (see DER.2.3.A5 * Closing the Initial Break-in Path *), IT systems should be hardened to hinder or prevent the techniques used by the attacker to spread across the internal network. Measures that can be implemented with little effort should, if possible, be carried out during the cleanup. Elaborate and far-reaching measures can be implemented after the adjustment as medium and long-term projects.

Basically, there are many different ways to harden individual IT systems and entire network environments. The choice of concrete measures depends on the techniques used by the attacker. As part of forensic analysis, its tools and approaches for extending rights and movement within the network should be identified and concrete measures should be developed to make APT attacks more difficult and more detectable in the future. For this purpose, the ISB, together with the forensic experts and the administrators responsible for the respective IT systems, should evaluate the results of the forensic analyzes and develop countermeasures.

Meaningful hardening measures can be identified, for example, on the basis of the IT-Grundschutz Compendium. It was to be examined whether IT-Grundschutz requirements previously unfulfilled for the IT environment would have prevented or at least made the attacks more difficult. The implementation of the respective measures should be re-examined.

Curing measures are very specific to the individual environment and should also be adapted as individually as possible to this environment, eg. B .:
* ** Network segmentation: ** If the attacker used a flat or roughly segmented environment to gain access to multiple IT systems, it would be better to divide the network into smaller segments with clearly defined and monitored transitions. This reduces the number of IT systems that can be reached (and therefore vulnerable) from a single segment. It is also often easier to monitor the transitions between smaller, well-defined segments. A very fine-grained network segmentation requires detailed knowledge of the network and in particular the operationally necessary transitions. This is often not available in institutions, which is why a fine granular segmentation can only be implemented in the medium to long term. However, a rough segmentation can already be implemented in the course of the clean-up measures and already makes the movement of an attacker within the network considerably more difficult.
* ** Separation of administration systems: ** A special case of the above-mentioned segmentation is the partitioning of administrative IT systems. Because of their high privileges and their mostly extensive access within a network environment, administrators are often an interim target for APT attacks. Therefore, administration systems should be closed off and administrative activities monitored for abnormal patterns of behavior. B. by a suitable monitoring. This can be done, for example, through a special admin network from which all accesses via (hardened and monitored) jumphosts or terminal servers take place. Administrative accesses (for example via RDP or SSH) may only be made from these IT systems. Deviations from this should lead to an alarm. A very far-reaching architecture for foreclosing privileged users is Microsoft's Red Forest and ESAE architectures. The concepts of these architectures can be adapted for a target environment, whereby many of the measures described there can only be implemented in the medium to long term.
* ** Restriction of service accounts: ** If service accounts were abused in an APT attack, these accounts should be hardened. Common examples of such measures include the operation of services with minimal privileges. If possible, services should not be run as * root * or * SYSTEM *, but only with the privileges that are actually needed for the specific purpose. For example, the account for operating a database should not be allowed to be written to the root directory of the web server if both services are running on the same server. These principles can be implemented using different techniques. For example, services may be isolated by containers or special techniques may be used to control service rights, such as * managed service accounts * or * group managed service accounts * on Windows or MAC systems such as SELinux or AppArmor on Linux.
* ** Additional protection of external accesses: ** If the attacker could use legitimate external access, for example the VPN access of employees, these accesses should be hardened. Possible measures could be the introduction of two-factor authentication, monitoring for the transfer of larger amounts of data or the limitation of access times.
Frequently, clean-up measures need to be implemented under high time pressure in order to minimize the period of isolation and thus the lack of or very limited availability of the environment. As a result, ad hoc solutions are often first implemented without the usual quality assurance processes and measures. It is therefore important to review the measures implemented after regular operations have resumed and to set up projects for the revision and quality assurance of the corresponding measures. It should also be planned how to implement measures for which there was no time during the cleanup.

#### DER.2.3.M8 Establishment of secure, independent communication channels

In an APT attack, the communication infrastructure may be compromised. Especially in the observation phase, when the exact extent of the attack is unknown, the existing communication channels should therefore not be used. Otherwise, the attacker can be warned at an early stage or is informed about the planned countermeasures and can respond to it.

Potentially affected communication channels can be:

* Telephony (especially with VoIP or integration with IT),
* E-mail (if an e-mail gateway for encryption is used, also encrypted mail servers),
* Chat and collaboration tools.
However, even if the attacker does not know the content of the communication, he can derive, for example, from communication patterns that he has been discovered. Likewise, the attacker can learn about it through side channels, such as stored call notes or calendar entries of communication relationships.

The governing body and all staff responsible for the clean-up should therefore have independent communication channels and, where appropriate, independent collaboration tools. In addition, it should be regulated when it should be possible to communicate via the established channels and when it is mandatory to use the independent channels.

It is not necessary to replace all lost communication channels. An easy way is to have face-to-face meetings and close collaboration between the governing body and direct supporters.

Usually it is not possible to build a parallel communication infrastructure in addition to the ongoing investigation and cleanup activities. Therefore, communication services of third parties are often used in such a situation. When selecting a suitable communication channel, care must be taken to ensure that the confidentiality and integrity of the communication is as well protected as possible.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### DER.2.3.M9 hardware replacement of affected IT systems (CIA)

In an APT attack, attackers can also manipulate the IT systems beyond the usual channels (operating system, applications). This includes:

* hardware-related software (eg UEFI),
* Firmware of system components (eg CPU, GPU, additional hardware),
* not directly affected additional components (eg remote maintenance solutions such as ILO)
* Firmware of power supplies and embedded devices (eg UPS),
* safety-critical settings of the software mentioned (eg undocumented options and options not available in maintenance programs).
Since there are often only limited access to these components via the firmware itself, an attacker can easily disguise his manipulations.
However, this kind of attack is time consuming, technically and organizationally complex for the attacker. In addition, he must have extensive access to the IT system and adapt the attack strongly to the respective target platform. Such an attack vector is unlikely, but can not be ruled out in an APT attack.

Such manipulations can only be detected by an institution with great effort and special knowledge. Since the self-assessment of the components can not be trusted, the settings and firmware files must be extracted and analyzed independently of the running component.

When deciding on the cleanup strategy (see DER.2.3.A2 * Decision on a cleanup strategy *), at least for devices with high protection needs and those used in high protection networks, consider replacing the potentially compromised hardware. There are basically three possible treatment strategies:

* ** No special treatment: ** The forensic analysis has shown that manipulation is ruled out because the attacker did not have the necessary access, the component was reliably secured against manipulation, and no extraction of the firmware gave any indication of manipulation Has. Only if all these points are given, the component can be used for the reinstallation.
* ** Reset software and settings: ** According to forensic analysis, it is possible to clean up the IT systems by resetting them to the factory settings or by re-importing the firmware. The component is designed so that a reset to the delivery state or the re-import of the firmware is possible independently of the potentially manipulated software itself (eg on a separate data carrier or via a bootloader in the ROM). In this case, the component can also be cleaned up and then used for the new installation.
* ** Exchange hardware: ** Since a reliable detection is uneconomical, it should be assumed in case of doubt of a manipulation. In this case, the entire system, or at least the affected component, must be replaced with a new device.
Each potentially affected IT system should be classified in one of the three groups. If there are sufficient reasons to refrain from a hardware exchange, the decision must be documented as part of the cleanup strategy.

If new or reset IT systems are set up again, existing recovery plans can be used. If component backups can be used for this, they should only be used if they have been created without doubt before the compromise. Since these backups are often created in an undocumented format, it is very expensive to check them. In case of doubt, it should therefore be reconfigured and the backup should not be used.

Separate devices must be disposed of properly. If possible, they should not be returned to leasing partners or sold as used equipment.

#### DER.2.3.M10 Conversions to hinder a renewed attack by the same attacker (CI)
During an APT attack, an attacker typically acquires detailed knowledge of how the target environment is built and configured. As part of the network reconnaissance, he learns how network sections and naming schemes are built for IT systems. He also knows user and service accounts, used software and services as well as methods for administration and maintenance. This detailed knowledge makes it easier for him to attack the same environment again. After the cleanup, the attacker succeeds in gaining access to the IT environment again, eg. For example, by exploiting a new vulnerability or an overlooked backdoor, he can use his knowledge to regain widespread control over the target environment within a short space of time.

To make it even more difficult for an APT attacker to compromise an environment, the IT environment can be purposefully rebuilt so that the attacker's knowledge of the internal structure is useless. Examples of such measures are:

* Use of other IP address ranges for network segments and / or other IP addresses for individual IT systems,
* Change of naming schemes for computers and / or change of names of individual IT systems
* Changing user and service account naming schemes and / or changing names for individual accounts
* Change URL paths for web applications and / or web services.
If the measures are implemented, the relevant documentation must be updated and the users must be notified and accompanied by administrators.

The measures described are not safety measures in the strict sense. On the contrary, they are concealment measures, but they can provide some protection. On the one hand, a renewed compromise is more time-consuming for the attacker because he can not reuse previously gained knowledge. On the other hand, the measures described can be supplemented by targeted detection. Establishing detection mechanisms that target the use of the old attacker's knowledge increases the chance of identifying a recurring attacker. If, for example, he uses a previously used IP address or an old account name, the IT operation is alerted. Such alarms often lead to many false alarms in the initial phase following a change, since not all configurations have been adapted by neighboring IT systems or users and administrators have not yet adapted to the changed circumstances. However, these false alarms can typically be sorted out with manageable effort and decrease with time, so that ultimately a high-quality alarming criterion can be established.

Targeted monitoring should also be used if the * KRBTGT * password has been reset twice to avoid Golden Ticket attacks (see also DER.2.3.A4 * Blocking and changing access data and cryptographic keys *). Then it should be monitored whether invalid Kerberos tickets are used. The use of corresponding tickets can be recognized by entries with the Event-ID * 4769 * in the security event log of the domain controller. If the error code is set to the value * 0x1f * here, this indicates * Golden Tickets * and should lead to an immediate alert.

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Further information on hazards and safety measures in the area "Clean-up of far-reaching security incidents" can be found in the following publications, among others:
* #### [CS072] First aid with an APT attack

  

 Federal Office for Security in Information Technology, Version 3.0, 01.2016
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_072\_TLP-White.pdf](https://www.allianz-fuer-cybersicherheit.de /ACS/DE/_/downloads/BSI-CS_072_TLP-White.pdf)

 
* #### [DRP] Data Breach Response Guide

  

 Experian Data Breach Resolution, 2013
 <Https://www.experian.com/assets/data-breach/brochures/response-guide.pdf>

 
* #### [GMSA] Windows Server 2012: Group Managed Service Accounts

  

 Microsoft, (last viewed 05.10.2017)
 <Https://blogs.technet.microsoft.com/askpfeplat/2012/12/16/windows-server-2012-group-managed-service-accounts/>

 
* #### [KGT] Protection from Kerberos Golden Ticket

  

 CERT-EU, 06.2014
 [https://cert.europa.eu/static/WhitePapers/CERT-EU-SWP\_14\_07\_PassTheGolden\_Ticket\_v1\_1.pdf](https://cert.europa.eu/static/WhitePapers/ CERT-EU SWP_14_07_PassTheGolden_Ticket_v1_1.pdf)

 
* #### [MSMSA] Managed Service Accounts

  

 Understanding, Implementing, Best Practices and Troubleshooting Microsoft (last viewed 05.10.2017)
 <Https://blogs.technet.microsoft.com/askds/2009/09/10/managed-service-accounts-understanding-implementing-best-practices-and-troubleshooting/>

 
* #### [PARM] Securing Privileged Access Reference Material

  

 Microsoft TechNet, (last accessed 05.10.2017)
 <Https://technet.microsoft.com/en-us/windows-server-docs/security/security-privileged-access/securing-privileged-access-reference-material>

 
* #### [ReCoBS] Common Criteria Protection Profile for Remote Controlled Browsers System (ReCoBS)

  

 BSI, BSI-PP-0040; Version 1.0, 2008
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/recobslanginfo\_pdf.pdf?\_blob=publicationBundesamt](https://www.bsi.bund.de/SharedDocs/Downloads /DE/BSI/Internetsicherheit/recobslanginfo_pdf.pdf?_blob=publicationBundesamt)

 
* #### [SANS1] When Breaches Happen: Top Five Questions to Prepare For

  

 SANS Institute, 2000
 <Https://www.sans.org/reading-room/whitepapers/analyst/breaches-happen-top-questions-prepare-35220>

 
* #### [SANS2] Detection and Recovery from a Major Security Breach

  

 SANS Institute, 2000
 <Https://giac.org/paper/gcux/50/detection-recovery-major-security-breach/100810>
