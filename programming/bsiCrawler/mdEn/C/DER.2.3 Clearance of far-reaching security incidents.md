1 description
--------------

### 1.1 Introduction

Advanced Persistent Threats (APT) are targeted cyber attacks on selected institutions and facilities where an attacker gains permanent access to a network and subsequently broadens it to other IT systems. The attacks are characterized by a very high use of resources and considerable technical capabilities on the part of the attackers and are usually difficult to detect.

After an APT attack is discovered, those in charge in the affected institutions face the challenge of having to clean up beyond the usual IT incident handling procedures. Because it can be assumed that the discovered attackers have been able to access the affected IT infrastructure for some time and use complex attack tools to bypass the standard security mechanisms and to establish various backdoors. In addition, there is a danger that the attackers will closely monitor the infected environment and respond to cleanup attempts by blurring their tracks and sabotaging the investigation.

In general, the building block assumes a high threat situation through a targeted, motivated attacker with above-average resources. In principle, a (certified) forensic service provider should always be involved in such an incident if the institution itself does not have its own forensic experts. Forensic service providers should already be consulted during the forensic analysis phase, but the service provider should also be consulted at least in an advisory capacity

### 1.2 Objective

This module describes how an institution should proceed to clean up the IT systems after an APT attack and restore the regular and secure operating state of the information network.

### 1.3 Delimitation

An information network can only be purged if the APT incident was previously successfully detected and forensically analyzed. Detection and forensics, however, are not the subject of this module, but are dealt with in DER.1 * Detection of security-relevant events * and DER.2.2 * Precaution for IT forensics *.

In this module, only the cleanup of APT incidents is considered. Common incidents are dealt with in module DER.2.1 * Incident Management *. Also, the building block does not describe how so-called "Indicators of Compromise" (IOCs), ie burglary traces, are derived and how they can be used to detect recurring attackers. Likewise, it does not discuss how any backdoors overlooked during analysis and cleanup can be found. Furthermore, the building block has to be demarcated from the higher-level incident management process (see DER.2.1 * Incident Management *), in which the cleanup is embedded.

It also eliminates attacks that give attackers physical access to an IT environment. This is how attack forms break down in computer centers, bribe administrators, intercept and manipulate newly procured hardware or do not listen to electromagnetic radiation. Only cyber attacks are considered.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​remediation of far-reaching security incidents:

### 2 1 Incomplete cleanup
APT attackers usually want to permanently infiltrate an information network. They have the resources they need and are able to launch long-term offensive campaigns. For this they use tools and methods that are attuned to an attack target. Even if an APT incident is detected, it can not be assumed that all access routes were found, all malware infections and communication channels were eliminated, and all backdoors were removed. However, with an incomplete cleanup, it is highly probable that an attacker would later, e.g. B. after a long period of rest, accesses the IT systems again and expanded its access again. He can, for example, by placing backdoors not only in operating systems and application software, but also manipulating hardware-related components, such as firmware. Such modifications are very difficult to identify, and the knowledge needed to extract and analyze them is poorly understood. Try the responsible z. For example, to clean up the IT components by overwriting or updating the firmware, it can still happen that the attacker has also modified the update routines and thus re-enters the system in this way.

### 2 2 Destruction of tracks

After an APT incident, IT systems are often reinstalled or completely retired. However, if no forensic copy was previously made by the IT systems, traces could be destroyed that would be necessary for further investigation of the incident or even for legal proceedings.

### 2 3 Early warning of the attacker

Usually, prior to clearing an APT incident, the attack is monitored over time and forensically analyzed to identify all access paths and tools and methods used. If the attacker notices that he has been discovered during this phase, he may resort to countermeasures. For example, he can try to cover his tracks or quickly sabotage other IT systems. He could also stop or set up more backdoors just to continue the attack later.

Since an APT attack must generally assume that the entire IT infrastructure of the institution has been compromised, there is a high risk that the attacker will detect the cleanup activity. This is especially true when the compromised IT infrastructure is used to plan and coordinate the cleanup. If the essential cleanup steps are not performed in the correct order, or critical actions are not performed concurrently and concertedly, the risk of alerting the attacker increases. For example, if those responsible isolate the network step-by-step rather than all at once, the attacker may be warned before their access is effectively terminated.

### 2 4 Data loss and failure of IT systems

When cleaning up an APT incident, various IT systems are reinstalled and networks are also temporarily isolated. As a result, compulsory fall out of IT systems and services are thus z. B. only limited or no longer available. If the cleanup takes a long time, it can lead to significant productivity losses. This, in turn, can result in significant economic losses that can even threaten corporate existence. This is especially the case if no or insufficient documentation is available for rebuilding.

### 2 5 Lack of retransformation after an APT attack
In an APT attack, the attacker gains detailed knowledge of how the target environment is built and configured. For example, he knows the existing network segments, naming schemes for IT systems, user and service accounts, software and services used. This knowledge may allow the same attacker to regain access to the target environment after a cleanup. Thus, he can move very targeted, efficient and unobtrusive within the network and reach again in a short time a high degree of infection.

3 requirements
---------------

The following are specific requirements for the Clean Up of Long Range Security Incidents (APT Responder). Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### DER.2.3.A1 Establishment of a governing body [Information Security Officer (ISB)]

In order to remedy an APT incident, a governing body must be set up to plan, coordinate and monitor all necessary activities. The panel MUST be assigned all the necessary authority to carry out its duties.

If such a governing body has already been set up when the APT incident was detected and classified, the same body should also plan and direct the cleanup. If a specialized forensics service provider has been called in to analyze the APT incident, then it should also be included in the incident resolution.

If the IT is over-compromised or if the necessary clean-up measures are very extensive, SHOULD it be checked whether a crisis staff should be set up. In this case, the governing body MUST monitor the clean-up actions. The governing body MUST then report to the crisis staff.

#### DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]

Before an APT incident is actually remediated, the governing body MUST define a cleanup strategy. In particular, it must be decided whether the malware can be removed from compromised IT systems, whether IT systems need to be reinstalled, or whether IT systems, including the hardware, should be completely replaced. Furthermore, it MUST be determined which IT systems are cleaned up. The basis for these decisions MUST be the results of a previous forensic investigation.

All affected IT systems SHOULD be reinstalled. Thereafter, the institution's recovery plans MUST be used. However, before backups are restored, forensic investigations MUST ensure that no manipulated data or programs are transferred to the newly installed IT system.

On the other hand, if an institution chooses to reinstall all its IT systems, a targeted APT cleanup MUST be implemented. To minimize the risk of missed backdoors, after the cleanup, the IT systems MUST be monitored to see if they are still communicating with the attacker.

#### DER.2.3.A3 Isolation of affected network sections

The network sections affected by an APT incident MUST be completely isolated (cut-off). In particular, the affected network sections MAY NOT be connected to the Internet. To effectively block the attacker and prevent him from blurring his tracks or even sabotaging IT systems, the network sections MUST be isolated in one fell swoop.
Which sections of the network need to be isolated MUST first be determined by a forensic analysis. All affected sections MUST be identified. If this can not be ensured, all suspicious and all theoretically infected network sections MUST be isolated.

In order to effectively isolate network sections, all local Internet connections, e.g. B. additional DSL connections in individual subnets, as completely as possible and taken into account.

#### DER.2.3.A4 Blocking and modification of credentials and cryptographic keys

Since it must be assumed that the attacker has acquired all the access data available on the compromised IT systems, all access data MUST be changed after the network has been isolated. Furthermore, centrally managed access data MUST be reset, z. In Active Directory environments or when using the Lightweight Directory Access Protocol (LDAP).

If the central authentication server (domain controller or LDAP server) is compromised, all accesses existing there MUST be blocked and their passwords exchanged. This MUST be performed by experienced administrators, if necessary with the help of internal or external forensics experts.

If TLS keys or an internal Certification Authority (CA) have been compromised by the APT attack, the corresponding keys and infrastructures MUST be recreated and redistributed. Also, the compromised keys MUST be locked reliably.

#### DER.2.3.A5 Closing the initial break-in path

If a forensic investigation has found that the attacker entered the institution's network through a technical vulnerability, this vulnerability MUST be closed. If the attackers were able to compromise the IT systems through human error, organizational, personnel and technical measures MUST be taken to prevent similar incidents in the future.

#### DER.2.3.A6 Return to productive operation

After the network has been successfully cleaned up, the IT systems MUST be returned to productive operation in an orderly manner. All previously purchased IT systems and installed programs used to monitor and analyze the attack MUST either be removed or put into production. The same MUST be done with communication and collaboration systems purchased for cleanup. Evidence and segregated IT systems MUST either be safely deleted or destroyed or archived properly.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​clearing up far-reaching security incidents. They SHOULD be implemented in principle.

#### DER.2.3.A7 Targeted system hardening

After an APT attack, all affected IT systems SHOULD be hardened. The basis for this should be the results of forensic investigations (see DER.2.X * IT Forensic Analysis *). In addition, it SHOULD be rechecked if the affected environment is still safe, e.g. B. with the results of the detailed forensic analyzes.

If possible, IT systems should already be hardened during cleanup. Measures that can not be implemented in the short term SHOULD be included in an action plan and implemented in the medium term. The ISB SHOULD be responsible for drawing up the plan and checking that it has been implemented correctly.

#### DER.2.3.A8 Establishment of secure, independent communication channels

It SHOULD establish secure communication channels for the governing body and staff responsible for the cleanup. It SHOULD be ensured that the most secure communication channel is selected.

### 3.3 Requirements for increased protection requirements
Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### DER.2.3.A9 hardware replacement of affected IT systems (CIA)

In IT systems with high protection requirements SHOULD be considered to completely replace the hardware after an APT incident. Even if a suspicious behavior is observed after a cleanup with individual IT systems, eg. For example, inexplicable network traffic SHOULD the affected IT system be replaced.

#### DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)

To prevent the same attacker from performing another APT attack on the institution's IT systems, the internal structure of the network environment SHOULD be modified. In addition, mechanisms should be established to quickly detect a recurring attacker.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and safety measures in the area "Clean-up of far-reaching security incidents" can be found in the following publications, among others:

* #### [CS072] First aid with an APT attack

  

 Federal Office for Security in Information Technology, Version 3.0, 01.2016
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_072\_TLP-White.pdf](https://www.allianz-fuer-cybersicherheit.de /ACS/DE/_/downloads/BSI-CS_072_TLP-White.pdf)

 
* #### [DRP] Data Breach Response Guide

  

 Experian Data Breach Resolution, 2013
 <Https://www.experian.com/assets/data-breach/brochures/response-guide.pdf>

 
* #### [KGT] Protection from Kerberos Golden Ticket

  

 CERT-EU, 06.2014
 [https://cert.europa.eu/static/WhitePapers/CERT-EU-SWP\_14\_07\_PassTheGolden\_Ticket\_v1\_1.pdf](https://cert.europa.eu/static/WhitePapers/ CERT-EU SWP_14_07_PassTheGolden_Ticket_v1_1.pdf)

 
* #### [ReCoBS] Common Criteria Protection Profile for Remote Controlled Browsers System (ReCoBS)

  

 BSI, BSI-PP-0040; Version 1.0, 2008
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/recobslanginfo\_pdf.pdf?\_blob=publicationBundesamt](https://www.bsi.bund.de/SharedDocs/Downloads /DE/BSI/Internetsicherheit/recobslanginfo_pdf.pdf?_blob=publicationBundesamt)

 
* #### [SANS1] When Breaches Happen: Top Five Questions to Prepare For

  

 SANS Institute, 2000
 <Https://www.sans.org/reading-room/whitepapers/analyst/breaches-happen-top-questions-prepare-35220>

 
* #### [SANS2] Detection and Recovery from a Major Security Breach

  

 SANS Institute, 2000
 <Https://giac.org/paper/gcux/50/detection-recovery-major-security-breach/100810>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "Cleaning up far-reaching security incidents".

* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.16 Theft of devices, data carriers or documents
* G 0.19 Disclosure of information worthy of protection
* G 0.18 Missing planning or missing adjustment
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.24 Destruction of equipment or data media
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.41 Sabotage
* G 0.42 Social engineering
* G 0.43 Importing messages
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
* G 0.14 Spying out information (spying)
  * DER.2.3.A1 Establishment of a governing body [Information Security Officer (ISB)]
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A3 Isolation of affected network sections
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A5 Closing the initial break-in path
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A8 Establishment of secure, independent communication channels
  * DER.2.3.A9 hardware replacement of affected IT systems (CIA)
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.15 Listening
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A5 Closing the initial break-in path
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A8 Establishment of secure, independent communication channels
  * DER.2.3.A9 hardware replacement of affected IT systems (CIA)
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.16 Theft of devices, data carriers or documents
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A8 Establishment of secure, independent communication channels
  * DER.2.3.A9 hardware replacement of affected IT systems (CIA)
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.18 Missing planning or missing adjustment
  * DER.2.3.A6 Return to productive operation
* G 0.19 Disclosure of information worthy of protection
  * DER.2.3.A1 Establishment of a governing body [Information Security Officer (ISB)]
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A3 Isolation of affected network sections
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A5 Closing the initial break-in path
  * DER.2.3.A6 Return to productive operation
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A8 Establishment of secure, independent communication channels
  * DER.2.3.A9 hardware replacement of affected IT systems (CIA)
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.20 Information or products from unreliable sources
  * DER.2.3.A7 Targeted system hardening
* G 0.21 Manipulation of hardware or software
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A9 hardware replacement of affected IT systems (CIA)
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.22 Manipulation of information
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A3 Isolation of affected network sections
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A8 Establishment of secure, independent communication channels
  * DER.2.3.A9 hardware replacement of affected IT systems (CIA)
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A3 Isolation of affected network sections
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A5 Closing the initial break-in path
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A9 hardware replacement of affected IT systems (CIA)
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.24 Destruction of equipment or data media
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.28 Software vulnerabilities or errors
  * DER.2.3.A5 Closing the initial break-in path
  * DER.2.3.A6 Return to productive operation
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.29 Violation of laws or regulations
  * DER.2.3.A6 Return to productive operation
* G 0.31 Incorrect use or administration of devices and systems
  * DER.2.3.A6 Return to productive operation
* G 0.32 Abuse of permissions
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A3 Isolation of affected network sections
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A5 Closing the initial break-in path
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.39 Malware
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A9 hardware replacement of affected IT systems (CIA)
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.40 Denial of Service
  * DER.2.3.A1 Establishment of a governing body [Information Security Officer (ISB)]
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A7 Targeted system hardening
* G 0.41 Sabotage
  * DER.2.3.A1 Establishment of a governing body [Information Security Officer (ISB)]
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A5 Closing the initial break-in path
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A9 hardware replacement of affected IT systems (CIA)
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.42 Social engineering
  * DER.2.3.A1 Establishment of a governing body [Information Security Officer (ISB)]
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
  * DER.2.3.A5 Closing the initial break-in path
* G 0.43 Importing messages
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A8 Establishment of secure, independent communication channels
  * DER.2.3.A9 hardware replacement of affected IT systems (CIA)
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
* G 0.45 data loss
  * DER.2.3.A1 Establishment of a governing body [Information Security Officer (ISB)]
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A3 Isolation of affected network sections
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A8 Establishment of secure, independent communication channels
* G 0.46 Loss of integrity of sensitive information
  * DER.2.3.A1 Establishment of a governing body [Information Security Officer (ISB)]
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
  * DER.2.3.A2 Decision for a clean-up strategy [Head IT, Information Security Officer (ISB)]
  * DER.2.3.A3 Isolation of affected network sections
  * DER.2.3.A4 Blocking and modification of credentials and cryptographic keys
  * DER.2.3.A7 Targeted system hardening
  * DER.2.3.A8 Establishment of secure, independent communication channels
  * DER.2.3.A9 hardware replacement of affected IT systems (CIA)
  * DER.2.3.A10 Conversions to hinder a renewed attack by the same attacker (CI)
