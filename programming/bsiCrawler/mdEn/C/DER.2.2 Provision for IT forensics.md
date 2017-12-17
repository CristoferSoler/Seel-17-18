1 description
--------------

### 1.1 Introduction

IT forensics is the strictly methodical data analysis on data carriers and in computer networks for the clarification of incidents, taking into account the possibilities of strategic preparation, especially from the point of view of the plant operator of an IT system.

Forensically investigating IT security incidents is always necessary if damage is to be determined, attacks should be averted and avoided in the future, and attackers identified. Whether an IT security incident is investigated forensically is decided on during the incident. An IT forensic investigation in the sense of this module consists of the following phases:

* Strategic Preparation: In this phase, processes are planned and built to ensure that an institution can forensically analyze IT security incidents. It is also necessary if the institution does not have its own forensic experts.
* Initialization: After the responsible employees have decided to forensically investigate an IT security incident, the previously planned processes are triggered. Furthermore, the scope of the investigation will be determined and initial measures will be carried out.
* Forensics: Here, the evidence to be backed up is selected and the data forensically secured. A distinction is made between live forensics and post-mortem forensics: live forensics ensures that volatile data (eg network connections, RAM) is backed up by a running IT system. In the case of post-mortem forensics, however, forensic copies of data carriers are created.
* Analysis: The collected data is analyzed forensically. The data are considered both individually and in the overall context.
* Presentation of results: The relevant test results are prepared and taught according to the target group.
### 1.2 Objective

The module shows what precautionary measures are necessary to enable IT forensic investigations. The focus will be on how forensics can be prepared and carried out. If forensic service providers carry out forensics in whole or in part, the requirements also apply to the service providers. Through contractual agreements and examinations, it can be ensured that the service provider adheres to the same.

### 1.3 Delimitation

The module does not describe any requirements to ensure that attacks are detected. These are contained in the module DER.1 * Detection of safety-relevant events * and are assumed in the present block. Also, no criteria and processes are explained, by means of which the responsible persons can decide, whether an IT security incident must be examined forensisch or not. The decision is made while the incident is being handled (see DER.2.1 * Incident Management *).

Furthermore, the module deals only with precautionary measures, which are fundamental for later IT forensic investigations. How the actual forensic analysis is performed is therefore not the subject of this module.

Ultimately, the building block also does not address how IT infrastructures can be cleaned up after they have been attacked (see DER.2.3 * Clean Up Major Security Incidents *). However, the activities described there can be significantly supported by the results of IT forensic investigations.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance for provisioning for IT forensics:

### 2 1 Infringement of legal framework
For IT forensic investigations, all data deemed necessary are often copied, secured and evaluated. This usually includes personal data of employees or partners. Is it z. Unfounded and without the Privacy Commissioner is involved, accessed, the institution violates legal regulations, such. For example, if the earmarking is disregarded. It is also possible that, for example, it can be deduced from the collected data how employees behave, or a relationship to them can be established. As a result, there is a risk that internal regulations will also be violated.

### 2 2 Loss of evidence through incorrect or incomplete preservation of evidence

If evidence is backed up incorrectly or not fast enough, it can cause important data to be lost that can not later be recovered. At worst, this leads to a fruitless forensic investigation. At least, however, the probative value is limited.

The risk of losing important evidence increases when employees misuse forensic tools, back up data too slowly or practice too little. Often, evidence is lost if those responsible do not recognize and secure transient data as relevant.

3 requirements
---------------

The following are specific requirements for the provision of IT forensics. Basically, the information security officer is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### DER.2.2.A1 Examination of the legal and regulatory framework for recording and evaluability [Head of Institution, Data Protection Officer]

If forensic data is collected and evaluated, all legal and regulatory frameworks MUST be identified and adhered to (see ORP.5 * Requirements Management *). Also, DO NOT violate internal regulations and employee agreements. In individual cases, however, it may be necessary to weigh the interest of the institution against that of the employees. The company or staff council and the data protection officer MUST be involved.

#### DER.2.2.A2 Creation of a guideline for initial measures during an IT security incident

It MUST be created a guide that describes for the IT systems used, which initial measures must be performed in an IT security incident in order to destroy as few traces. It also MUST be described by what actions potential traces can be destroyed and how to avoid them.

#### DER.2.2.A3 Preselection of forensic service providers

If an institution does not have its own forensic team, it is necessary to identify possible suitable forensics service providers in the preparatory phase. Which forensic service providers are eligible MUST be documented.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the provision of IT forensics. They SHOULD be implemented in principle.

#### DER.2.2.A4 Definition of interfaces for crisis and emergency management
The interfaces between IT forensic investigations and crisis and emergency management SHOULD be defined and documented. For this purpose, it should be determined which employees are responsible for what and how to communicate with them. In addition, it should be ensured that contact persons are available.

#### DER.2.2.A5 Creation of a guideline for the safeguarding of evidence of IT security incidents

A guideline SHOULD be created describing how to secure evidence. It should include procedures, technical tools, legal frameworks and documentation requirements.

#### DER.2.2.A6 Training of forensic security implementation personnel

All responsible employees SHOULD know how to properly track and use forensic tools properly. For this, suitable training courses SHOULD be offered.

#### DER.2.2.A7 Selection of forensic tools

It SHOULD be made sure that tools used to forensically secure and analyze traces are also suitable for this purpose. Before a forensics tool is used, it should also be checked if it works properly. Also SHOULD be checked and documented that it was not manipulated.

#### DER.2.2.A8 Selection and order of evidence to be secured [Investigator]

A forensic investigation SHOULD always begin by defining the goals or work assignment. The goals SHOULD be formulated as concrete as possible. Thereafter, all necessary data sources SHOULD be identified. It should also be determined in which order the data is to be saved and how exactly this should be done. The order SHOULD be based on how volatile the data to be backed up is. So fast volatile data SHOULD be secured promptly. Only then should, for example, fixed memory contents and finally backups follow.

#### DER.2.2.A9 Preliminary selection of forensically relevant data [Investigator]

It SHOULD be determined which secondary data (eg log data or traffic recordings) are kept in the way and for how long within the legal framework for possible forensic evidence.

#### DER.2.2.A10 IT forensic security of evidence [investigator, investigator]

In order to secure evidence, if possible, the entire volume should be forensically duplicated. If that is not possible, for. For example, in the case of volatile data in RAM or in SAN partitions, a method should be chosen that changes as little data as possible.

In order to prove that the data is integer, the original data carriers SHOULD be kept sealed. If cryptographic checksums of forensic copies or originals exist, integrity can also be proven. To do this, the written documented cryptographic checksums SHOULD be separated from the data carriers and kept in multiple copies. In addition, it should be ensured that the checksums documented in this way can not be changed. In order for the data to be judicially usable, a witness SHOULD confirm how it was done and authenticate the checksums that were created.

It SHOULD use only trained personnel (see DER.2.2.A6 * Training of personnel for the implementation of forensic protection *) or a forensic service provider (see DER.2.2.A3 * Preselection of forensic service providers *) to forensic evidence to secure.

#### DER.2.2.A11 Documentation of the evidence [investigator, investigator]

If evidence is forensically secured, all steps taken should be documented. The documentation SHOULD provide complete proof of how the secured original evidence was handled. Also SHOULD be documented, which methods were used and why the responsible people have decided.
#### DER.2.2.A12 Secure storage of original data and evidence [investigator, investigator]

All seized original data carriers SHOULD be physically stored in such a way that only investigative and named employees can access them. If original media and evidence are to be stored, SHOULD set how long they should be stored. After the deadline has expired, it should be checked whether the media and evidence must be kept even further. After the retention period, evidence should be securely erased or destroyed and original data carriers returned.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### DER.2.2.A13 Framework contracts with external service providers (CIA)

To enable IT security incidents to be investigated forensically more quickly, the institution SHOULD conclude retrieval agreements or framework agreements with forensic service providers.

#### DER.2.2.A14 Establishment of standard procedures for the preservation of evidence (CIA)

For applications, IT systems or IT system groups with high protection requirements as well as for widespread system configurations, standard procedures SHOULD be created, which make it possible to secure volatile and non-volatile data as completely as possible forensically.

The respective system-specific standard procedures SHOULD be implemented by proven and possibly automated processes. They SHOULD also be supported by checklists and technical aids, such as: Through software, software tools on mobile devices, and IT forensic hardware such as write-blockers.

#### DER.2.2.A15 Performing evidence-gathering exercises (CIA)

All employees involved in forensic analysis SHOULD regularly practice how to secure evidence in an IT security incident.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the area of ​​"Provisioning for IT forensics" can be found in the following publications, among others:

* #### [BSIFor] BSI IT Forensics Guide

  

 BSI, Version 1.0.1, 03.2011
 [https://www.bsi.bund.de/DE/Themen/Cyber-Sicherheit/Dienstleistungen/IT-Forensik/forensik\_node.html](https://www.bsi.bund.de/DE/Themen/ Cyber ​​security / services / IT forensics / forensik_node.html)

 
* #### [ISFTM24] Information Security Forum (ISF), specifically Area TM 2.4 Forensic Investigations

  

 ISF, in particular Area TM 2.4 Forensic Investigations, 06.2016

 
* #### [ISO27042] ISO / IEC 27042: 2015

  

 Information technology- Security techniques- Guidelines for the analysis and interpretation of digital evidence, ISO, 06.2015
 <Https://www.iso.org/standard/44406.html>

 
* #### [ISO27043] DIN EN ISO / IEC 27043

  

 Information technology- IT security procedures- Principles and processes for the investigation of incidents (ISO / IEC 27043: 2015); German version EN ISO / IEC27043: 2016

 
* #### [NIST80086] NIST Special Publication 800-86

  

 NIST, Guide to Integrating Forensic Techniques Into Incident Response, 08.2006
 <Https://csrc.nist.gov/publications/detail/sp/800-86/final>

 
* #### [RFC3227] Guidelines for Evidence Collection and Archiving

  

 RFC, 02.2002
 <Https://tools.ietf.org/html/rcf3227>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the module "Provision for IT Forensics".

* G 0.17 Loss of equipment, data carriers or documents
* G 0.20 Information or products from unreliable sources
* G 0.22 Manipulation of information
* G 0.25 Failure of devices or systems
* G 0.27 Resource shortage
* G 0.29 Violation of laws or regulations
* G 0.31 Incorrect use or administration of devices and systems
* G 0.37 denying actions
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
