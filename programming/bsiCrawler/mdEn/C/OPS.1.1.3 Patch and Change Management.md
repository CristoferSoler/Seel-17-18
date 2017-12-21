1 description
--------------

### 1.1 Introduction

The ever faster IT development and the increasing demands of the users require many authorities and companies to update the components of their information technology correctly and in a timely manner. It also shows in practice that security holes or malfunctions are often due to incorrect or missing patches and changes. A missing or neglected patch and change management thus quickly leads to gaps in the security of the individual components and thus possible attack points.

The task of patch and change management is generally to design and control controllable changes in applications, infrastructure, documentation, processes and processes.

### 1.2 Objective

This module shows how a functioning patch and change management can be set up in an institution and how the corresponding process can be controlled and optimized.

### 1.3 Delimitation

The descriptions in this module focus on the IT operation, but can also be implemented analogously in other business processes. Change management is the task of planning and controlling changes. Since this process is very time-consuming, the standard requirements of the module are aimed primarily at larger information networks. For smaller institutions the fulfillment of the standard requirements has to be checked, but the effort should not be put above the benefit. Patch management represents a part or specific process within the change management, which aims at the updating of software and is to be applied in each case. The individual building blocks of the SYS and APP layers have additional patch management requirements where necessary.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in patch and change management:

### 2 1 Undefined responsibilities

For example, poorly defined, overlapping, or unclarified responsibilities can slow down the categorization and prioritization of change requests, thereby delaying the distribution of patches and changes. Even if patches and changes are released prematurely without test run and consideration of all (technical) aspects, this can have a serious impact on safety.

In the extreme case, poorly defined responsibilities can affect the entire institution completely or to a large extent. Faults in the operation affect the availability. Confidentiality and integrity may be affected if security-related patches are not or are distributed late.

### 2 2 Defective communication in change management

If the patch and change management within the institution is poorly accepted or the people involved communicate poorly, it may cause change requests to be delayed, or incorrectly decided on by a change request.

This can reduce overall security levels and seriously disrupt IT operations. In any case, the lack of communication makes the change process inefficient, as it often requires too much time and resources to be invested. This has a negative impact on the institution's responsiveness and, in extreme cases, can lead to security vulnerabilities or important business goals being missed.

### 2 3 Poor consideration of business processes
Incorrect changes can, among other things, affect the smooth running of business processes or even lead to the IT systems involved completely failing. Even a comprehensive test procedure can not completely rule out that a change in subsequent productive operation proves to be faulty.

If the impact, category or priority of a submitted business process change request is misjudged in the change process, the desired level of security may decrease. Such misjudgments occur predominantly when the IT managers and the responsible specialist departments do not adequately coordinate.

### 2 4 Insufficient resources for patch and change management

Effective patch and change management requires adequate human, time and financial resources. If these are not available, for example, the necessary roles can be filled with unsuitable persons. Also, interfaces for certain information, for example, between IT and the corresponding contact persons in the departments, can not be created, or the required capacities for the infrastructure of the test and distribution environments are not provided. If the staffing, time and financial shortcomings in regular operations can often be compensated, they will prove to be more time-consuming, for example when emergency patches need to be recorded.

### 2 5 Problems with automated distribution of patches and changes

Frequently, patches and changes are not distributed manually, but centrally software-supported. If such software is used, erroneous patches and changes in the entire information network can be deployed, which can result in mass security problems. It is especially serious when many systems simultaneously install software that contains security holes.

If only a few mistakes occur, they can often be remedied by hand. However, it will be problematic if IT systems can not be permanently accessed on the LAN. One example is sales representatives who rarely and irregularly connect their IT systems to the LAN. If the tool is configured to distribute the updates only within a certain period of time and then not all IT systems can be reached, these systems can not be updated.

### 2 6 Poor recovery options for patch and change management

If patches or changes are distributed without a recovery option, or if the recovery routines of the software in use are not or not adequately effective, incorrectly updated software can not be corrected in a timely manner. This can cause important IT systems to fail and high consequential damage. In addition to the integrity of data, especially the availability is at risk here.

### 2 7 Poor consideration of mobile devices

Mobile devices are a particular challenge for change management, as they are not always involved in the automated distribution of patches and changes due to their changing locations and their connection to wireless networks. Also, bandwidth and stable data transmission in mobile devices are not always guaranteed. If such devices are not considered separately in patch and change management, patches and changes may be incomplete, take longer to complete, and always present a security risk.

### 2 8 Inadequate emergency preparedness plan for patch and change management
Patch and change management contributes to the technical implementation of information security in an institution. The IT systems used by this process are critical for IT operations. These include, for example, the central servers that distribute patches and changes, the databases with the current configurations of the IT systems and the backup servers for the recovery points. If, for example, the server that distributes the changes fails, any new critical updates may no longer be recorded promptly. Furthermore, missing backups of the current configurations of IT systems can mean that in an emergency it is no longer possible to ensure that important IT components can be restored to their original state as quickly as possible.

### 2 9 Misjudgment of the relevance of patches and changes

If changes are prioritized incorrectly, for example, unimportant patches could be installed first. On the other hand, important patches will be installed too late and vulnerabilities will persist for longer. Patch and change management is often supported by software-based tools. These tools can also contain software errors, making insufficient or incorrect information about a change. If the information that such a tool makes about a change is not checked and tested for plausibility, there may be differences between the actual and assumed implementation of changes.

### 2 10 Manipulation of data and tools in change management

Patch and change management often operates from a central point. Due to its exposed position, it is particularly vulnerable: If attackers succeed in taking over the servers involved, they could simultaneously distribute manipulated software versions to a variety of IT systems via this central point. Often further points of attack arise from the fact that these systems are operated by external partners (outsourcing). Maintenance accesses could also be set up to allow attackers to access the central server for distribution of changes.

3 requirements
---------------

The following are specific requirements for patch and change management. Basically, the * IT operation * is responsible for fulfilling the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### OPS.1.1.3.A1 Concept for Patch and Change Management [Administrator, Specialist]

If changes to IT components, software or configuration data are to be implemented, there must be guidelines for them that also take security aspects into account. All patches and changes MUST be planned, tested, approved and documented. If patches and changes are made, fallback solutions MUST be present. Major changes MUST also involve information security management. Overall, it MUST be ensured that the desired level of safety is maintained during and after the changes.

#### OPS.1.1.3.A2 Definition of responsibilities [Head IT]
For all organizational areas, the persons responsible for patch and change management MUST be defined. The defined responsibilities MUST also be reflected in the authorization concept. In addition, a dedicated change manager SHOULD be named. All parties involved MUST be familiar with the concepts of patch and change management, information security, and cryptographic techniques.

#### OPS.1.1.3.A3 Configuration of Auto Update Mechanisms [Administrator]

It is MUST be defined within the patch and change management strategy how to handle integrated update mechanisms (auto update) of the software used. In particular, it MUST be determined how these mechanisms are secured and appropriately configured. In addition, new components SHOULD be checked to see if and which update mechanisms they have.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state-of-the-art in patch and change management. They SHOULD be implemented in principle.

#### OPS.1.1.3.A4 Planning the Change Management Process [Change Manager]

A change management process SHOULD be defined, with institutions able to adapt to the change management process of the IT Infrastructure Library (ITIL). All changes to hardware and software versions as well as configurations SHOULD be controlled and controlled through the change management process.

#### OPS.1.1.3.A5 Dealing with Change Requests [Change Manager]

Requests for changes SHOULD be submitted and processed according to a specified procedure. All change requests (Request for Changes, RfCs) SHOULD be recorded, documented, and then reviewed by the Change Manager. Once a change request has been accepted, it SHOULD be prioritized and categorized. It should be ensured that the required resources are available for the respective priorities.

#### OPS.1.1.3.A6 Change Request Reconciliation [Change Manager]

When a change is implemented, the associated reconciliation process SHOULD consider all relevant audiences. The target groups affected by the change SHOULD have demonstrably been able to comment. Also, there SHOULD be a set procedure that can speed up important change requests.

#### OPS.1.1.3.A7 Integration of Change Management in the Business Processes [Change Manager]

The change management process SHOULD be integrated into the business processes. Thus, in the case of planned changes, the current situation of the affected business processes SHOULD be taken into account. All relevant departments SHOULD be informed about upcoming changes. Also, there SHOULD be an escalation level, whose members belong to the management level of the institution and which decides in case of doubt about the priority and scheduling of a hardware or software change.

#### OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]

It SHOULD define requirements and frameworks for selecting patch and change management tools. In addition, a specific security policy for the tools used SHOULD be created.

#### OPS.1.1.3.A9 Testing and acceptance procedure for new hardware and software [IT Manager]

New hardware and software SHOULD BE tested before it is used. For this purpose only isolated test systems should be used. Also, there SHOULD be an acceptance procedure and release statement for software. The responsible person SHOULD file the release declaration in a suitable place in writing. In the event that errors are detected in the software despite the acceptance and release procedures during operation, there should be a troubleshooting procedure.
#### OPS.1.1.3.A10 Ensuring the integrity and authenticity of software packages [Administrator]

Throughout the patching and modification process, the authenticity and integrity of software packages SHOULD be ensured. For this purpose, it should be checked whether checksums or digital signatures are available for the software packages used. Likewise, care should be taken to ensure that the necessary programs are available for review.

#### OPS.1.1.3.A11 Continuous Documentation of Information Processing [IT Manager, Change Manager]

Changes SHOULD be documented in all phases, all applications and all systems. For this purpose, appropriate regulations should be developed.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### OPS.1.1.3.A12 Scalability in Change Management (A)

If a change management tool is used, the implementation speed should be carefully checked before startup. It should be possible to define break points at which the distribution of a faulty change is stopped.

#### OPS.1.1.3.A13 Measuring Change Requirement Success (IA)

To check if a change was successful, the change manager SHOULD perform so-called post-tests. For this he SHOULD select suitable reference systems as quality assurance systems. The results of the night tests SHOULD be documented as part of the change process.

#### OPS.1.1.3.A14 Synchronization within Change Management [Change Manager] (CIA)

As institutions make changes to the IT infrastructure, the change management process SHOULD respond. Temporarily or permanently unavailable devices SHOULD be considered in the change management process through appropriate mechanisms.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the area of ​​"patch and change management" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Patch and Change Management" block.

* G 0.9 Failure or malfunction of communication networks
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.27 Resource shortage
* G 0.28 Software vulnerabilities or errors
* G 0.33 Personnel loss
* G 0.37 denying actions
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
  * OPS.1.1.3.A3 Configuration of Auto Update Mechanisms [Administrator]
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
  * OPS.1.1.3.A9 Testing and acceptance procedure for new hardware and software [IT Manager]
* G 0.18 Missing planning or missing adjustment
  * OPS.1.1.3.A1 Concept for Patch and Change Management [Administrator, Specialist]
  * OPS.1.1.3.A10 Ensuring the integrity and authenticity of software packages [Administrator]
  * OPS.1.1.3.A11 Continuous Documentation of Information Processing [IT Manager, Change Manager]
  * OPS.1.1.3.A12 Scalability in Change Management (A)
  * OPS.1.1.3.A13 Measuring Change Requirement Success (IA)
  * OPS.1.1.3.A14 Synchronization within Change Management [Change Manager] (CIA)
  * OPS.1.1.3.A2 Definition of responsibilities [Head IT]
  * OPS.1.1.3.A4 Planning the Change Management Process [Change Manager]
  * OPS.1.1.3.A5 Dealing with Change Requests [Change Manager]
  * OPS.1.1.3.A6 Change Request Reconciliation [Change Manager]
  * OPS.1.1.3.A7 Integration of Change Management in the Business Processes [Change Manager]
  * OPS.1.1.3.A11 Continuous Documentation of Information Processing [IT Manager, Change Manager]
  * OPS.1.1.3.A12 Scalability in Change Management (A)
  * OPS.1.1.3.A13 Measuring Change Requirement Success (IA)
  * OPS.1.1.3.A14 Synchronization within Change Management [Change Manager] (CIA)
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.1.3.A3 Configuration of Auto Update Mechanisms [Administrator]
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
  * OPS.1.1.3.A10 Ensuring the integrity and authenticity of software packages [Administrator]
* G 0.20 Information or products from unreliable sources
  * OPS.1.1.3.A3 Configuration of Auto Update Mechanisms [Administrator]
  * OPS.1.1.3.A5 Dealing with Change Requests [Change Manager]
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
  * OPS.1.1.3.A10 Ensuring the integrity and authenticity of software packages [Administrator]
* G 0.23 Unauthorized intrusion into IT systems
  * OPS.1.1.3.A3 Configuration of Auto Update Mechanisms [Administrator]
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
  * OPS.1.1.3.A10 Ensuring the integrity and authenticity of software packages [Administrator]
* G 0.25 Failure of devices or systems
  * OPS.1.1.3.A3 Configuration of Auto Update Mechanisms [Administrator]
  * OPS.1.1.3.A5 Dealing with Change Requests [Change Manager]
  * OPS.1.1.3.A6 Change Request Reconciliation [Change Manager]
  * OPS.1.1.3.A7 Integration of Change Management in the Business Processes [Change Manager]
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
  * OPS.1.1.3.A9 Testing and acceptance procedure for new hardware and software [IT Manager]
  * OPS.1.1.3.A12 Scalability in Change Management (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.1.3.A3 Configuration of Auto Update Mechanisms [Administrator]
  * OPS.1.1.3.A5 Dealing with Change Requests [Change Manager]
  * OPS.1.1.3.A6 Change Request Reconciliation [Change Manager]
  * OPS.1.1.3.A7 Integration of Change Management in the Business Processes [Change Manager]
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
  * OPS.1.1.3.A9 Testing and acceptance procedure for new hardware and software [IT Manager]
  * OPS.1.1.3.A12 Scalability in Change Management (A)
* G 0.27 Resource shortage
  * OPS.1.1.3.A2 Definition of responsibilities [Head IT]
  * OPS.1.1.3.A5 Dealing with Change Requests [Change Manager]
  * OPS.1.1.3.A6 Change Request Reconciliation [Change Manager]
  * OPS.1.1.3.A7 Integration of Change Management in the Business Processes [Change Manager]
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
  * OPS.1.1.3.A12 Scalability in Change Management (A)
  * OPS.1.1.3.A14 Synchronization within Change Management [Change Manager] (CIA)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.1.3.A3 Configuration of Auto Update Mechanisms [Administrator]
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
  * OPS.1.1.3.A9 Testing and acceptance procedure for new hardware and software [IT Manager]
  * OPS.1.1.3.A10 Ensuring the integrity and authenticity of software packages [Administrator]
* G 0.33 Personnel loss
  * OPS.1.1.3.A2 Definition of responsibilities [Head IT]
  * OPS.1.1.3.A6 Change Request Reconciliation [Change Manager]
  * OPS.1.1.3.A7 Integration of Change Management in the Business Processes [Change Manager]
  * OPS.1.1.3.A12 Scalability in Change Management (A)
* G 0.37 denying actions
  * OPS.1.1.3.A2 Definition of responsibilities [Head IT]
  * OPS.1.1.3.A5 Dealing with Change Requests [Change Manager]
  * OPS.1.1.3.A6 Change Request Reconciliation [Change Manager]
  * OPS.1.1.3.A7 Integration of Change Management in the Business Processes [Change Manager]
  * OPS.1.1.3.A11 Continuous Documentation of Information Processing [IT Manager, Change Manager]
* G 0.39 Malware
  * OPS.1.1.3.A3 Configuration of Auto Update Mechanisms [Administrator]
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
  * OPS.1.1.3.A10 Ensuring the integrity and authenticity of software packages [Administrator]
* G 0.40 Denial of Service
  * OPS.1.1.3.A3 Configuration of Auto Update Mechanisms [Administrator]
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
  * OPS.1.1.3.A10 Ensuring the integrity and authenticity of software packages [Administrator]
* G 0.45 data loss
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.1.3.A3 Configuration of Auto Update Mechanisms [Administrator]
  * OPS.1.1.3.A8 Secure Use of Patch and Change Management Tools [IT Leader]
  * OPS.1.1.3.A10 Ensuring the integrity and authenticity of software packages [Administrator]
