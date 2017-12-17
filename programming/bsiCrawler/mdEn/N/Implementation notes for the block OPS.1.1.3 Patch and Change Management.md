1 description
--------------

### 1.1 Introduction

The task of change management is to make changes in applications, infrastructure, documentation, processes and procedures controllable and controllable. A missing or neglected patch and change management quickly leads to security gaps in the individual components and thus to possible attack points.

Especially in the field of information technology, many authorities and companies are faced with the challenge of correctly and promptly adopting the necessary changes to the components of their system landscape due to the ever-accelerating development and increasing demands of users. Experience in government agencies and companies shows that security holes or malfunctions are often the result of incorrect or missing changes.

This document demonstrates how to build a well-functioning patch and change management in an institution. It also describes how the process can be controlled and optimized so that disruptions in operation can be avoided and security gaps can be minimized and eliminated in a timely manner. The descriptions focus on the IT operation, but can also be implemented analogously in other business processes. The term change management in this module refers to the task of planning and controlling changes. Patch management is a part of change management that aims at updating software and should always be applied.

### 1.2 Life cycle

To set up an effective system that can handle changes, there are a number of steps to take.

** planning and conception **

Patch and change management should control and control all hardware and software changes and their configurations. To record and evaluate all changes, all IT systems recorded within the patch and change management system should be subordinated to this (see OPS.1.1.3.M2 * Definition of Responsibilities for Change Management *). Changes to the configuration and the state of the systems are therefore only possible via change management. This requires the management of the institution to delegate the appropriate responsibility. The organizational implementation of patch and change management represents a cross-sectional function by different departments of an institution. In particular, the IT operation, information security management and the specialist departments must be involved.

A single change process begins with a change request. This should first be recorded and controlled by the change manager. Relevance, urgency, planned execution (deadline, process) and possible risks and problems should be compiled and recorded for this change (see OPS.1.1.3.M4 * Change Management Process Planning * and OPS.1.1.3.M5 * Dealing with Change Requests) *).

Patch and change management can be meaningfully supported by technical aids, for example for the automatic distribution of software. If special tools are used to implement patch and change management, it must be ensured that a concept for their use is created (see OPS.1.1.3.M8 * Safe Use of Change Management Tools *).

**Procurement**

There are different products that support the patch and change management process. In order to make an appropriate choice from these products, the requirements for these tools, such as which platforms to support, must be determined prior to procurement (see OPS.1.1.3.M8 * Safe Use of Change Management Tools *).

**Implementation**
During implementation, all IT systems managed by Patch and Change Management should be subordinated individually or in groups. Furthermore, changes to these systems must be documented in a central location (see OPS.1.1.3.M11 * Continuous Documentation of Information Processing *).

**Business**

Depending on the size and complexity of a patch or change, it is recommended that an execution plan define tests, control and breakpoints, and distribution priorities. It must be ensured that the desired level of safety is maintained during and after the change. The approval and implementation of changes should be coordinated, taking into account resources and interests of departments and IT operations (see OPS.1.1.3.M7 * Integration of change management in business processes * and OPS.1.1.3.M6 * Reconciliation of change requests *).

For quality assurance purposes and to detect errors or to prevent future errors, every patch and every change should be evaluated after it has been loaded (see OPS.1.1.3.M13 * Measuring the success of change requests *).

Changes, especially software updates, can be made manually, or with the help of suitable tools. When using these tools, it must be ensured that they are particularly secured against misuse and do not endanger the overall security since they often work with system administrator authorizations. The tools provide the ability to make changes to many systems at the same time. It also multiplies the effects of errors, so it should be tested very carefully before the change is made (see OPS.1.1.3.M12 * Scalability in Change Management *). It should also be taken into account that systems to be converted might be switched off temporarily or permanently or may not be reachable. This mainly affects mobile devices such as laptops and smartphones (see OPS.1.1.3.M14 * Synchronization within change management *). In addition, the integrity and authenticity of the software used must be technically ensured during the entire patch and change management process (OPS.1.1.3.M10 * Ensuring the integrity and authenticity of software packages *).

The software update mechanisms used in the software update must be considered, regardless of their operational level within the patching and modification process (see OPS.1.1.3.M3 * Configuring Autoupdate Mechanisms *).

** Emergency Preparedness **

For contingency planning, the individual contingency plans of the applications and IT systems managed by Patch and Change Management must be considered (see DER.4 * Emergency Management *). As patch and change management contributes to the technical implementation of security in the institution, appropriate technical redundancy and backup systems should be provided to counteract a non-compensable failure. Furthermore, representative rules are of particular importance in order to maintain the decision-making and approval process.

2 measures
-----------

The following are specific implementation notes in the patch and change management section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### OPS.1.1.3.M1 Concept for Patch and Change Management [Administrator, Specialist]

With the complexity of today's IT systems, even minor changes to running systems can lead to security issues, such as: Due to unexpected system behavior or system failures.
In terms of information security, change management is responsible for identifying new security requirements that result from changes to IT systems. If significant hardware or software changes are planned on an IT system, then how are they affecting the security of the overall system? Changes to an IT system must not lead to individual security measures becoming inefficient and endangering overall security.

Therefore, there should be guidelines for making changes to IT components, software or configuration data. Any changes to IT components, software or configuration data should be planned, tested, approved and documented. It must be ensured that all security-relevant changes are appropriately addressed. These include, for example:

* Changes to IT systems (new applications, new hardware, new network connections, modifications to the software used, installation of security patches, hardware upgrade, etc.),
* Changes in the task or in the importance of the task for the institution,
* Changes in user structure (new, external or anonymous, user groups),
* spatial changes, eg. B. after a move.
Before changes are approved and implemented, it is necessary to check and test whether the level of security is maintained during and after the change. If risks, especially for availability, can not be ruled out, a relapse solution must be planned, which also specifies criteria for when it should be used.

All changes and the corresponding decision-making principles must be documented. This applies both in the operating and in a test environment.

Important for patch and change management is also an authorization concept:

* Only those who are allowed to make changes should have access privileges to the relevant system areas.
* There should be mechanisms to ensure that all significant changes have been agreed in advance.
** Note: ** When making changes, always pay attention to changes in an IT system or its operating conditions

* Changes in the implementation of individual security measures,
* the creation of a new security concept or even
* the revision of the organization-wide information security guideline
may require. For major changes, therefore, information security management should be included.

#### OPS.1.1.3.M2 Definition of responsibilities [Head of IT]

When setting up patch and change management, a number of responsibilities need to be addressed. It must be ensured that there is a precise definition of each task and organization area, which responsibilities an employee has in the patch and change process, and how the coordination between the individual areas has to proceed.

It is sometimes the case that employees in different areas of an institution have different responsibilities for making changes. For example, one section may be responsible for operating systems, and another section may be responsible for the services installed on it (eg, e-mail server, application, etc.). This can then lead to different areas being responsible, for example, for patching an entire system. In such cases, it is particularly important to specify the responsibilities.

The responsibilities thus divided should also be reflected in the authorization concept.
For the efficient and effective coordination and evaluation of the changes, a dedicated change manager should be named in the institution. It filters, accepts and classifies all change requests. He is also responsible for authorizing the necessary changes as well as planning, coordinating and executing them.

It is imperative that changes take place in a coordinated manner. No employee may make changes on their own. All employees of the IT organization must also agree to relevant changes with the change management. This ensures that any changes do not interfere with each other or even lead to a system failure.

For an institution of at least medium size or with complex IT infrastructures, the change manager should be supported in its work by a Change Advisory Board (CAB). It has been proven that, in addition to the persons entrusted with the technical implementation of change tasks, one person from each department should also be appointed as a member of the CAB. The CAB is convened regularly at scheduled times to assess changes and help the change manager assess, prioritize and authorize them. As a rule, the CAB will only be subject to serious changes. For this purpose, the CAB may be composed differently in terms of its members. For example, the complete CAB could come together every three months to discuss critical change requests.

For uncritical regular changes, the agreements can be made directly between the change manager and the responsible administrators or the test team.

In order for the CAB to perform its tasks properly, its members must be able to assess how changes can impact both technically and in terms of business goals and processes.

#### OPS.1.1.3.M3 Configuring Auto Update Mechanisms [Administrator]

Many products have automatic update mechanisms (autoupdate) that inform users when there are patches or updates. Often, these also offer the option of downloading and installing the updates immediately via the Internet. As a rule, today all operating systems and available standard software packages contain such mechanisms. The functionality of the update mechanism varies depending on the version, installation mode and manufacturer.

Usually, auto-update IT products look for new versions or software packages each time the system or software is started or timed on a public update server. The products provide several ways to configure the auto-update mechanism. When new IT components are put into operation, it should always be checked whether and which update mechanisms they have and how they can be configured. It should also be checked which data is transferred from the auto-update mechanism to the manufacturer. It should first be clarified in principle how these mechanisms are handled. Then it should be determined how the update functions are concretely configured in the different products. The following sections give an overview of the different variants of these mechanisms.

Not every software can completely deactivate the update function. If the institution wants to prevent the uncontrolled communication of IT components with the outside world, then packet filters must be used.

If no query of a public update server is desired, many software products can be redirected to Internet addresses other than those of the manufacturer, such as internal ones.
Some manufacturers offer software for own operation of update servers or update mirror servers, whereby the update server in the institution is installed locally (eg Windows Server Update Services WSUS). The update server then communicates directly with the manufacturer and loads the desired updates. The advantage of this solution is that the IT systems of an institution affected by the update do not have to communicate themselves with the manufacturer's update server, but only with the locally installed system. As a result, data traffic to the outside can be reduced to a minimum. With many products for update servers, the desired settings can be conveniently made via a graphical user interface (GUI). However, there are also products in which the necessary settings to use local update servers or to prevent the query from a public update server are hidden or can only be prevented by packet filters or firewalls.

If public update servers are to be used, the authenticity of the update server must first be checked (see OPS.1.1.3.M10 * Ensuring the Integrity and Authenticity of Software Packages *). In addition, it should be investigated whether update query actions can be set using time intervals or events. The settings must then be made according to the defined change strategy.

It should be examined how the communication with update servers can be limited to the lowest possible level. It must also be decided whether direct communication with the manufacturer should be the only alternative or parallel to internal communication (parallel configuration).

A parallel configuration is often useful for mobile users who do not always communicate within the government or enterprise network. For mobile IT systems, for example, it can be more important to load a current patch when it closes a dangerous security gap than to wait for release from change management. Instead, the change manager can also specify that all software changes occur only through the internal shared software distribution.

With auto-update mechanisms, it is also important to note whether the changes are only downloaded to an internal IT system by the manufacturer and then the installation is left to the user, or if they are automatically installed immediately after they have been downloaded.

In addition, it must be determined how to deal with any necessary reboots of IT systems after the installation of changes, ie whether they are made directly or z. For example, when the system shuts down the next time.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "patch and change management".

#### OPS.1.1.3.M4 Planning the Change Management Process [Change Manager]

Each institution should set up a clearly defined process for change management and regulate responsibilities for the different tasks (see OPS.1.1.3.M2 * Definition of responsibilities *). All hardware and software changes and configurations should be controlled and controlled through the patch and change management process. To record and evaluate all changes, all IT systems managed by Change Management should report to the change manager. Changes to the configuration and status of the systems should therefore only be possible via change management.

The change management process can be modeled as follows, based on the IT Infrastructure Library (ITIL):

**Coordination**
When a Request for Change (RfC) request (see OPS.1.1.3.M5 * Dealing with Change Requests *) has been submitted and accepted, it must first be classified, categorized and prioritized, before the actual implementation planning and coordination begins becomes. Afterwards, the following points should be considered before the change is recorded.

* Procurement or development of changes
 Many manufacturers offer to receive the necessary information about new hardware or software or about errors that have occurred and their rectification in the subscription by e-mail.
 Updates and patches are typically available for download on Internet servers. In part, these sources are only accessible in conjunction with valid registration or support contracts. Often, the installed software or operating system provides the user with the ability to load software changes directly from the particular application or system.
 Some manufacturers provide their customers with special applications to manage and update the products. In addition, there are also more and more applications that, if the user and the security settings allow it, automatically seek updates from their manufacturers via the Internet and inform the user. From a security point of view, however, there are also disadvantages if changes are automatically recorded. This means that faulty updates that are automatically imported can lead to failures and malfunctions. Therefore, it should be carefully considered whether such mechanisms should be used.
 Internal software development could be another way to make software changes if any security vulnerabilities or other requirements make it necessary. However, not only the necessary expertise must be available. The interfaces or the source code must also be open.
* Testing
 After a change has been recorded, the functionality of the systems must be determined by a test. Whenever possible, a representative selection of typical application scenarios with the specialist department must be defined and tested. The results should be documented and compared with the expected results in order to identify any problems. In addition, all log files created during the test must be examined for evidence of malfunction.
* Integration into the software distribution, test of integration
 Often, specific package or file formats in which manufacturers provide their updates must be adapted for use in an automatic software distribution system. This is especially true if active components, such as shell scripts, have to be executed during or after the installation. These adjustments need to be tested on a test system for effectiveness before the changes are distributed.
**Implementation**

The employees designated by the change manager are assigned to implement the change. Change Management monitors this. In the case of changes that can not be adequately tested, it makes sense in some cases to only initialize them for a small group of users. Then the results are evaluated before the change is implemented on all systems. If this is not possible or expedient due to the circumstances, for example because comparable changes have often already been carried out without problems, or because mutually incompatible software versions make a partial distribution impossible, a complete distribution can also be carried out.

** Evaluation **
Changes made should then be evaluated. Then the result is evaluated by Change Management or by the Change Advisory Board (CAB) based on the following aspects:

* Has the change or patch achieved the desired goal?
* Are the clients and the users satisfied with the result?
* Have side effects (for example, problems with non-change applications) occurred?
* Were the estimated costs, the planned effort and the timetable met?
If the change was successful, the change request (Request for Change) or the change record can be closed. If the change fails, it must be decided whether the changes made need to be adjusted. In some cases, it is recommended that you undo the change and create a new or modified change request. In the case of a failed change, it may also be useful to investigate the causes and, based on this, adapt IT systems or processes. So similar problems can be avoided in the future.

Depending on the nature and extent, it may be useful to evaluate the change immediately. On the other hand, it may also be beneficial to wait a few days or weeks to see what effect the change will have and whether the goal has been achieved. Changes made are only successfully completed once they have been positively evaluated and documented. To make sure that this is not forgotten, the change manager should be reminded of this by an automated resubmission.

** Withdrawal of changes **

Whether it is necessary to withdraw hardware or software changes, results directly from the evaluation. If the changes were unsuccessful or the situation even deteriorated, they should be withdrawn if technically feasible and economically viable.

This can often be technically supported by the patch and change management software used. If not, the changes must be manually undone.

** degree and documentation **

It is recommended that all change requests, hardware and software changes, test procedures and results be documented in a database, regardless of whether they were successful or not (see OPS.1.1.3.M11 * Continuous documentation of information processing *) ,

In many institutions, it is now routine to regularly provide operating systems and applications with available software updates to address vulnerabilities and protect against malware. Often, however, it is forgotten that this procedure is also necessary for hardware. Many IT devices use compact operating systems that are often tailored to their hardware. These include, for example, routers, switches, network printers and smartphones. Therefore, it must be ensured that even such devices are included in patch and change management and supplied with safety-relevant updates.

#### OPS.1.1.3.M5 Handling Change Requests [Change Manager]

Requests for changes should be submitted and processed according to a set schedule.

** Submit and capture change requests **

First, all change requests (Requests for Change, RfCs) must be recorded. So that all the necessary information is available, it is recommended to provide the applicants with a form (see the sample of a change request from the IT Baseline Protection Tools).

This application also serves to coordinate the change (see also OPS.1.1.3.M6 Reconciliation of Change Requests). For example, if a change was requested to solve an existing problem, a corresponding reference to the problem, usually an entry number in a database, should also be documented.
Not every amendment is treated as a normal change within the change process. Some routine changes, which are clearly circumscribed, standardized, and nonetheless subject to change, can be treated as a service request. A service request would be, for example, to reset a password and, in terms of change management, to change a login banner of a service (the text that the service uses when connecting via the network interface).

** filter and accept change requests **

After a change request has been captured, it is controlled by the change manager. It should identify non-feasible, unnecessary or duplicate change requests. Such requests should be rejected on justification. So it is possible for the applicant to reconsider and reformulate his change request.

If a change request has been accepted, the information is included in a change record to make the change. The data record can be recorded in a software tool, on paper or in a self-created database. Later, the following information will be added to the change record:

* determined priority and category,
* Assessing the impact and required resources,
* Recommendations of the Change Manager or the Change Advisory Board (CAB),
* Date and time of authorization,
* planned date for the implementation of the amendment,
* current date and time of change, date of evaluation,
Justification for a possible rejection of the proposal or application and
* Schedule and evaluation data.
* Test results and problems encountered,
** Classify change requests (priority and category) **

Once a change request has been accepted, it must be prioritized and categorized:

* The priority describes the importance of a change and derives from the urgency and impact. If an error is to be corrected that has already been classified as part of change management, the priority may already be transferred. However, it should always be checked once again by the change manager and corrected if necessary. The same applies to security patches or updates requested by information security. However, the final priority is set within change management, taking into account other pending change requests.
* The category is determined by the change manager. The basis for this are the expected effects and the required resources. highest priority:
* normal priority:
 A change with normal priority has no urgency or major impact, but should not be postponed to a later date. In the CAB, this change in the allocation of resources is given a normal priority.
* low priority:
 A low priority change is desired, but has time until a suitable opportunity arises (eg, a follow-up version or scheduled maintenance).
The classification, which is composed of priority and category, determines how the change request is processed further and thus describes how significant the planned change is.

Priorities are assigned by the change manager for a change and are divided into different levels, whereby the security management should be given a right of objection against too low or wrong prioritization. For example, the following priority levels can be assigned by change management:

* high priority:
This priority describes z. A change due to a serious malfunction or is related to other urgent activities. This change will be given top priority in the allocation of resources for testing and execution at the next session of the CAB.
Categories are usually assigned by change management, whereby security management should also be given a right of appeal against too low a categorization. Categories are used to assess how the change will work and how the institution will be impacted by the change process. For example, the following categories can be awarded:

* minor consequences:
 Changing this category requires little effort. The change manager can approve these types of changes without having to submit them to the CAB.
* serious consequences:
 This category includes changes that require significant effort and have a significant impact on IT services. Such changes are discussed in the CAB in order to define the required effort and to minimize the risk. In the run-up to the meeting, the necessary documentation is first sent to the members of the CAB and, if necessary, to some IT specialists and developers.
* far-reaching consequences:
 Changing this category requires a lot of effort. For such a change, the change manager first requires authorization from the security management team. Subsequently, the change must be submitted to the CAB for assessment and further planning.
**Planning**

The employees involved in the change management process plan the implementation for all accepted changes. If necessary, this is done together with the CAB. At this stage of the change management process, it is important to consider the required technical and human resources and to estimate how the change will affect the operation. The following aspects should be considered at least:

* Required technical and human resources and their cost emergency plans for responding to adverse effects caused by the change, reliability and recoverability of affected IT services;

 
+ technical approvals, for example because additional IT systems need to be procured.
+ business approvals because, for example, the upgrade has implications for suppliers.


 
* Number and availability of required IT specialists,
* desired temporal implementation of a change,
* Consequences for the use of IT services and resulting adjustments to service level agreements,
* possible conflicts with other changes.
#### OPS.1.1.3.M6 Reconciliation of Change Requests [Change Manager]

Whether a change management process succeeds depends on effective communication, as the individual process steps, as defined in OPS.1.1.3.M4 * Change Management Process Planning * and OPS.1.1.3.M5 * Dealing with Change Requests *, are common can only be continued after the responsible roles have responded.

In addition to the Change Advisory Board (CAB), additional target groups may be included in the voting process for a hardware or software change. Which these are depends on the size and structure of the institution. Typically, the applicant should be involved in a hardware or software change, the IT help desk, and the end-user affected by the change, or a representative of the department.
Business Process Owners must be aware of the application process for hardware or software changes. They also need to know what process the application is undergoing and what information will be provided during the application process. An essential aspect is the quality of the content of the Amendment Request (RfCs). The necessary information is often recorded as a form or via an input mask in a special application. Which information is needed and how the form is developed should therefore be carefully coordinated and determined with the possible target groups.

In addition, the change management process must ensure that, in the event of serious changes, all subject-matter managers can comment on the content of the application in order to prevent a change that is undesirable from the point of view of a target group.

On the other hand, the application process must not take too long. It must also be possible to speed up important changes. Under certain circumstances, it must be allowed to abbreviate the regular change management process.

#### OPS.1.1.3.M7 Integration of Change Management into Business Processes [Change Manager]

Depending on the nature of the changes made, it may be necessary for an application or IT system to be restarted, and thus fail for a short period of time. In addition, even carefully conducted tests can not always avoid difficulties with the affected application, or a system can fail entirely by distributing hardware or software changes.

For this reason, irrespective of the tests carried out, the current situation of the affected business processes must also be taken into account. It can, for. For example, it may be useful to make a hardware or software change a few days later, even though the affected system is currently considered critical to security. The system may provide important services to which the institution relies. Management might value the risk of disruption to business processes through patch and change management as greater than the risk of a pending vulnerability.

In order to distribute hardware and software changes, it is therefore necessary to notify all stakeholders of upcoming changes and expected downtime. The individual parties include all departments that need the system. In particular, departments whose tasks depend on the applications and IT systems concerned must be involved in prioritizing changes and scheduling.

There must be at least one escalation level above the change manager and the CAB, which decides if necessary via prioritization (see OPS.1.1.3.M5 * Dealing with Change Requests *). This escalation level must be chosen from the management level of the institution.

#### OPS.1.1.3.M8 Secure Use of Patch and Change Management Tools [IT Leader]

A patch and change management tool plays a vital role as the central entity to implement the change management process and software distribution for the safe and proper operation of the institution.

** Appropriate selection of tools **

The change management process can be supported with different products or product combinations. There can be many reasons for implementing changes using a suitable tool. Frequently, heterogeneous IT infrastructures and the more effective use of resources are decisive.
Before acquiring a patch and change management tool, the requirements and constraints should be determined to find a product that is appropriate for the particular institution. The procedure for the evaluation of a tool is always similar and is based on the valid change strategy of the institution, regardless of whether change management is needed as a tool for an operating system, for a manufacturer's product range or for a large heterogeneous IT scenario.

The following are the main features that should be considered when choosing a product.

* Platform support:
 On the one hand, this term refers to which platforms are supported with regard to the implementation of the patch and change process and, on the other hand, on which platform the tool itself is executable. Especially the first aspect should be considered in great detail, since in the server-client area, for example, most tool manufacturers support patches and changes to Microsoft products. However, this does not mean that the entire range of IT products available in the institution is covered, from desktop and server operating systems to application servers and individual products.
* Change analysis:
 Some manufacturers are focusing on the amount of updates associated with the distribution process and their rapid distribution, as well as reporting the "delivery status". Some provide more information on the background or cause of a patch, partly with lists of affected files, more detailed description of the vulnerabilities and their own test reports. Especially for security patches, which should normally be distributed quickly, the detailed information provides an indispensable indication for the internal classification of the hardware or software change.
* Change verification:
 Most manufacturers provide hash sums, fingerprints or signatures with the changes to verify their authenticity and integrity. However, only a few tools check this evidence. Therefore, there is a risk that unwanted software is distributed in bulk in the institution and thus a considerable damage occurs. For security reasons, therefore, you should not use any change tools that do not have this function.
* Change strategy:
 The tool must allow flexible configuration to automate as many steps as possible in the chosen change strategy. This can vary greatly due to different platforms. The processed steps of the change process should be documented comprehensibly by the tool and, if necessary, audit-proof. Later changes in the process must be able to flow into the tool.
* Distribution:
 Not every change should be applied to every system. The tool should be the grouping of systems and applications according to freely definable attributes such. Protection, location and organizational unit. These attributes can become IT system profiles according to the standardized system types in the institution.
* Rollback:
 No software is perfect. Therefore, despite all the tests, it may be necessary to reverse a change process. Being able to automate this process saves time and money in the event of an error. If erroneous changes can not be canceled promptly and with little effort, this can cause considerable damage to the institution.
* Status evaluation: It must be possible to automatically and correctly distribute the changed hardware or software on all systems. As with software distribution, there might be problems with the connection or availability of a system. For example, a system may reject a patch due to other system states. It is therefore important that the change tool records the patch status of all systems. Depending on the strategy, if problems occur, the tool should continue the technical change process on the remaining IT systems or skip certain system groups or terminate the process.
** Security Policy for Using Change Management Tools **

The patch and change management must be operated with a reasonable organizational and technical effort. Among other things, the protection requirements of the business processes and thus the protection requirements of the data and systems must be taken into account. A specific security policy for change management should be created for this. This must be aligned with the security concept of the institution and the security guidelines derived from it.

Aspects for which guidelines must be formulated in this security policy are:

** Specifications for the planning: **

* The tool must have scalable server applications. For this purpose, requirements must already be formulated in advance as to how replication and load distribution should be used and how technical redundancies can be used.
* For a secure network connection to external sources of patches or changes, eg. As with manufacturers, appropriate regulations must be established. For example, the direct connection of the clients to the manufacturers of the software used could be redirected to a proxy by appropriate rules on the security gateway.
* To ensure that the integrity and authenticity of changes can be reliably verified, appropriate concepts and components must be specified.
* Documentation requirements for operation, emergency and recovery of the change management tool must be formulated. This includes, among other things, that the documentation must always be up to date. Furthermore, it should be defined where the documentation must be stored and how many copies of the documentation must be present.
** Administration requirements: **

* It is necessary to create a rights concept for change management personnel and also for the services used by the patch and change management software.
* Administrators must specify how rights are granted, what rights they are entitled to, or which they are allowed to distribute.Specifications for the installation:
* The tools for patch and change management must be configured securely. The specific settings depend heavily on the existing applications and IT systems of the institution.
* It must be determined how the IT resources relevant to the Patch and Change Management tool are configured with security considerations in mind.
* The patch and change management tool should be adequately separated in the LAN. New changes and patches should not be tested in the production network, but in a separate test network.
** Requirements for safe operation **

* To operate a patch and change management tool, you must set policies and procedures, such as who can access them and where changes can be made.
* Patches and changes are often obtained over the Internet. Connections to public or less trusted networks must always be secured via security gateways.
* The patch and change management tool itself must be included in the process of patch and change management. It is necessary to define how to handle hardware and software changes for the patch and change management tool itself.
** Specifications for logging and monitoring **

* It must be specified how the data supplied by the tool should be monitored, logged and evaluated.
**Data backup**

* A suitable procedure for data backup must be defined. When backing up, at least the following components should be backed up at regular intervals:
 

 
+ The configuration or settings of the tools required for patch and change management.
+ The databases with the current configurations of the IT systems.
+ For self-translated software, the exact compiler settings.
+ The installed patches and changes.
+ The last recovery points of the IT systems.
+ Any existing older versions, for example because the latest version of a software has not yet been sufficiently tested or is not executable on all systems.
+ An overview of the comparison checksums of the software packages, which should possibly be saved on a Write Once Read Many - Medium (WORM).
+ An overview of the comparison checksums of the software packages, which should possibly be saved on a Write Once Read Many - Medium (WORM).


 
* Furthermore, the data protection concept for the patch and change management tool must be integrated into the overall data protection concept of the institution.
** Disruption and emergency care **

* For emergency preparedness, the individual contingency plans of the applications and IT systems managed by Patch and Change Management must be considered.
* Depending on the availability requirements for the Patch and Change Management tool, it should be considered to create a separate contingency plan for the tool in case of unwanted effects during and after installation of patches and changes.
#### OPS.1.1.3.M9 Testing and Acceptance Procedure for New Hardware and Software [Head IT]

Before new hardware components or new software are used in the production environment, they must be checked on special test systems. It must be checked whether the product is executable and whether it has a negative effect on the current IT systems. Since malfunctioning can not be excluded before successful tests and because errors are provoked during tests, test systems that are isolated from the production plant must always be used. General procedures for software acceptance and release, including testing, are described in APP.5.1 * Standard Software *. Only after passing the test may new components be installed on production systems.

** software acceptance process **

As part of a software acceptance process, it is checked whether the considered software reliably provides the required functionality and whether it also has no unwanted side effects. The subsequent release of the software by the competent authority grants permission to use the software. At the same time, this position also assumes responsibility for the IT process that is implemented by the software.

In the case of software acceptance, a distinction is made between software that was developed on its own or commissioned by the customer and standard software that is adapted only for the specific application.

** Acceptance of self-developed or commissioned software **

Before the order for software development is awarded internally or externally, the requirement definition for the software must be created, from which the rough and detailed concept for the realization is developed. On the basis of these documents, the responsible body draws up an inspection plan.
Usually, test cases and the expected results for the software are developed. The software is tested based on these test cases. The comparison between expected and actually calculated result is used as an indication of the correctness of the software.

To develop the test cases and to carry out the tests, the following should be noted:

* the test cases are developed by the competent authority,
* for test cases, no data of the active operation is used,
* Test data, in particular if data for this purpose are copied, must not contain any confidential information. Personal data must be anonymised or simulated,
* The test must not affect the current operation. If possible, a logically or physically isolated test computer should be used.
A decrease is to be refused if:

* serious errors are detected in the software
* Test cases occur where expected results do not match those calculated
* User manuals or manuals are not available or of inadequate quality and
* The software, including the source code and processes, is not or not sufficiently documented.
The results of the acceptance must be recorded in writing. The documentation of the acceptance result should include:

* Name and version number of the software and possibly the IT procedure,
* Description of the test environment,
* Test cases and test results and
* Declaration of acceptance.
** decrease of standard software **

If standard software is procured, it should also be accepted and released. In the decrease should be checked whether

* the software is free of computer viruses,
* the software is compatible with the other products used,
* the software is executable in the desired operating environment and which parameters are to be set,
* the software has been delivered complete including the required manuals and
* the required functionality is fulfilled.
** Release procedure **

If the software has been approved, it must then be released for use. To do this, first determine who is authorized to release software. The release of the software must be specified in writing and suitably filed.

The release statement should include:

* Name and version number of the software and if necessary the IT-procedure,
* Confirmation that the acceptance has been made properly,
* Restrictions on use (parameter setting, user group, ...),
* Release date, from when the software may be used and
* the actual release.
If IT is technically possible, it must be prevented that software can be changed or manipulated unnoticed after release, for example by means of suitable integrity protection methods. Otherwise, appropriate organizational rules must be established to prevent or promptly detect changes to the software.

Even after intensive acceptance tests, errors in the software may be detected during ongoing use. In this case, it is necessary to determine how to proceed in such an error case (contact person, troubleshooting process, involvement of the responsible authority, repetition of acceptance and release, version control).

#### OPS.1.1.3.M10 Ensuring the integrity and authenticity of software packages [Administrator]
In principle, software should only be installed from well-known sources, especially if it has not been delivered on data carriers but has been downloaded from the internet, for example. This is especially true for updates or patches. Most manufacturers and distributors offer checksums that can at least verify the integrity of a package. The checksums are usually published on the websites of manufacturers or sent by e-mail. To verify the integrity of a downloaded program or archive file, the published checksum is then compared to a locally generated checksum by a corresponding program.

If checksums are offered for a software package, they should be checked before the package is installed.

The authenticity can not be verified with checksums. Therefore, in many cases, digital signatures are offered for programs or packages. In turn, the public keys needed to verify the signature are usually available on the manufacturer's websites or from public-key servers. Often the checksums are generated with one of the programs PGP or GnuPG.

If the check reveals that this is a valid signature of the respective manufacturer, this results in a significantly higher degree of trustworthiness for the package than merely the presence of a checksum.

Sometimes even the built-in software update mechanisms of the respective operating system or application software do not perform checksum comparisons. If possible, however, a checksum check should be performed on each software package.

Furthermore, not all checksum comparisons can be performed without the involvement of the users, since the checksums, signatures or certificates required for this purpose are not provided by the manufacturers in a uniform manner. This often requires manual verification on the manufacturer pages or customization of the URLs in the change software.

If digital signatures are available for a software package, they should always be checked before installing the package.

A fundamental problem with the use of digital signatures is the verification of the authenticity of the key used itself. If the public key carries no signature of a known trustworthy person or organization (such as a trust center), the signatures generated with the corresponding private key offer no real security in that the software package actually comes from the developer, manufacturer or distributor. Therefore, if not certified, the public keys should preferably be obtained from a different source than the software package itself, for example from another mirror server on which the package can also be downloaded, or from a public-key server.

In order to check checksums and digital signatures, the corresponding programs must be available locally. Administrators should be aware of the meaning and validity of checksums and digital signatures. In addition, the administrators must have enough time to use the test programs in their daily work and familiarize themselves with the operation.
Obtaining patches and email changes is not recommended for a variety of reasons. The origin of emails is difficult to determine without the use of additional security mechanisms and the recipient addresses in the institutions are often distribution lists, whose address is easy to guess. Patches and changes can also be very extensive. Many companies and government agencies have limited the size of email attachments and may also prohibit the adoption of executable attachments. Furthermore, the large amounts of data unnecessarily burden the e-mail systems. Therefore, a timely availability of the software changes, which can be critical especially for security patches, can not be adequately ensured via e-mail.

Furthermore, some manufacturers offer to send changes and patches to the customer directly on data carriers. In this case as well, the changes should be verified using checksums or digital signatures, as sender information on mailpieces and manufacturer logos on CDs and DVDs can easily be falsified.

Another means of checking the authenticity of the update may be messages published by the manufacturer on its website, newsletter or similar channels. Some manufacturers have established cycles and timepoints that typically release information about changes systematically.

#### OPS.1.1.3.M11 Continuous Documentation of Information Processing [IT Manager, Change Manager]

Information processing must be continuously documented in all phases, all applications and all systems to ensure proper IT operation. This includes:

* a current documentation of all existing IT systems and their configuration,
* the documentation of the users and their rights profiles set up on the respective IT systems, including a description and justification of all restrictions on the use of IT systems,
* the newly added hardware and software components must be listed in the system documentation,
* the documentation of all security-related processes such as data backup or the destruction of data carriers,
* the documentation of the maintenance measures,
* a description of all found and fixed bugs.
The naming of system owners should also be in writing and communicated to the users. For problem cases should be documented, who can help and where to find information.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### OPS.1.1.3.M12 Scalability in Change Management (A)

Obtaining a patch and change management tool often has different requirements than later. The IT landscape is growing and additional IT systems that need to be taken into account by patch and change management are added. Therefore, it is important that the patch and change management tool can be scaled. The scalability required to introduce the system must already be determined during the planning phase.

The main factors influencing scalability are the required implementation speed with which hardware or software changes are to be distributed in the existing IT infrastructure as well as the necessity to massively restore the IT systems in parallel in the event of a fault.
In the event that faulty hardware or software changes are distributed, break points must be defined. Since this possibility depends strongly on the speed of implementation, it must be determined where, how and at what time a deliberate interruption of the distribution is possible.

In order to determine whether an expected implementation speed actually exists, firstly operating values ​​of the IT infrastructure, such as network bandwidths and system utilization, can be used. However, the rate of implementation must be carefully tested before starting the system. Any bottlenecks that may occur in the IT infrastructure must be quickly addressed by extending or changing the configuration.

In addition to the determined values, a presumed growth of the IT infrastructure in the direct time after commissioning should be added in order not to immediately switch to a further scaling and rebuilding phase of the system. Further operational experience should be gathered and then used as additional clues for further development of the system.

In practice, it has been proven to implement scalability according to the physical and geographic IT structure of the institution. If the change strategy of the institution allows it, z. B. in the branches of the institution distribution systems are used, the receive and process the software changes only for the IT systems of each site.

On the other hand, if the institution's change strategy is strongly center-oriented, or if the patch and change management tools are outsourced, it is advisable to choose scaling so that dedicated systems are operated per branch.

When software tools are used to support patch and change management, care should be taken to meet scalability requirements.

#### OPS.1.1.3.M13 Measuring Change Requirement Success (IA)

Management processes such as patch and change management must be constantly improved, optimized and adapted to the changing conditions in the institution. The way in which the present measure is implemented in the institution also demonstrates the maturity of the patch and change management process.

The tests performed in the run-up to hardware, software, or configuration changes can be used primarily to verify that the changes in the expected field of application are basically working. Since changes are usually intended to remedy a fault, it is necessary for the requestors of the change request to subsequently obtain an evaluation of the success of the change.

For this it is inevitable to perform so-called post-tests. As a prerequisite, reference systems must be selected as quality assurance systems. In addition, it must be ensured that the post-tests are carried out by those business users who know the business processes of the institution and are able to assess any errors that may occur.

If the change was necessary from a security point of view, the backtest must be initiated by the change manager and carried out by specialist users.

The results of the post-tests and evaluations are documented as part of the patching and change process. The Change Manager, the Change Advisory Board, and Security Management have data available to help improve the process.

#### OPS.1.1.3.M14 Synchronization within Change Management [Change Manager] (CIA)

Most government agencies and companies often make changes to the IT infrastructure. The change management process must react to these changes. It must be ensured that the respective patches and changes are promptly and if possible simultaneously applied to all affected IT systems.
With mobile devices or even if the network used is overloaded, it can happen that IT systems can not be reached when distributing hardware or software changes. For such cases, appropriate mechanisms must be established to ensure that systems can not re-connect to the network until they have been provided with appropriate updates. There are several tools that verify access to the production network, whether security programs and security patches are up-to-date, and deny access to the internal network if there are security issues. Typically, such tools are used to first determine the software status of the systems and then assemble the software for update. Depending on the type of change process, these can then be distributed and installed automatically or after prior approval for these systems. Changes that require a system restart should be installed last, or only when the IT system shuts down. Depending on the technical support and implementation of the process, the updates can also be installed and the necessary reboot afterwards can be released separately.

3 Further information
------------------------------

### 3.1 Worth knowing

** Basic concepts of change management **

The change management process provides, manages, and manages various updates and enhancements to the production environment. In this area, a variety of concepts have established themselves. These must be known to the persons involved in the process.

** Versionsbezeichnungen ** very different terms are common. This is because there is no single, binding, overarching standard for the definition of a term. During development, the products go through different stages. ** Due to not exactly defined terms, it is recommended to use a glossary within the institution to ensure a consistent understanding of all terms.

The first executable version of a product is often called ** alpha version **. The alpha version is mostly for internal use, eg. To demonstrate that a software project is feasible. It therefore usually already contains the most important basic functions.

A ** beta version ** is an unfinished product version that is often released by the developer for trial and presale purposes. The essential functions of the product are already available, but not yet sufficiently tested. Beta versions are distributed to so-called beta testers, which check the functionality and usability of the product and report errors to the developers. The software typically finds many programming errors.

For software development, ** Release Candidate ** (** RC **) or ** Release Candidate ** is a final trial. In this version, all functions that the final version of the software should contain are available. This version type is for a final system or product test. Only further RCs will be released if serious quality issues are identified.

The finished and published version of a software is called ** Release ** or ** Stable ** and usually additionally provided with a version number. Since media production also begins at this time, the term ** Ready to Manufacturing (RTM) ** is often used.

Many software developers have published mechanisms for handling software fixes. The following terms are not always consistently used consistently. Overall, however, they provide the necessary overview of the conceptual world in this subject area.
Software fixes are released to fix bugs in previously published software. A ** patch ** is a general ** software update **, which fixes malfunctions in a software. First, such ** update ** is not critical and not security relevant. If the update is relevant to the security of the software, so if a vulnerability is closed, it is often called ** security patch **. For a security patch, a ** severity ** is often specified. This usually refers to how seriously the manufacturer keeps the vulnerability that the security patch fixes. If the update corrects a major functionality of the software, which is not necessarily relevant to security, for example an incorrect calculation, it is often referred to as ** critical update **.

A different publication by the manufacturer, which however only refers to special customer situations and is often provided only with a valid support contract or is only created on the basis of support inquiries, has the designation ** Hotfix **. It can be a single package of one or more files to fix a problem in a product.

A ** service pack **, on the other hand, is a cumulative collection of hotfixes, security patches, critical updates, and updates that have been released since the product's launch and are made available to the general public.

The period until the release of service packs is often very long. A summary may also be useful for providing the amount of software fixes available in between. Therefore, some manufacturers publish in between so-called ** Update Roll-Ups **. This is a collection of security patches, critical updates, updates, and hotfixes that are offered cumulatively or for a single product component, such as a web server.

After the release of service packs, the available product series are often incremented by a number in the decimal point range. This should document that the software products already contain all the corrections available up to this point. Some manufacturers also refer to this as ** Integrated Service Pack **.

Due to the different requirements of customers, manufacturers are often forced to integrate new options (features) into their product. These feature enhancements are usually offered to all customers with valid contractual relationships with the manufacturer (support contract, update contract, software maintenance agreement, etc.) as a ** feature pack **. The new features are usually included in the next product version.

Two types of ** change ** to IT components are common in business practice. ** Standardized changes ** and ** changes ** that must go through the change management process.

Standard changes are changes to applications and IT systems for which detailed procedures exist and which were approved in advance by the ** Change Manager **.

The written procedure must ensure that the risk associated with the change can be neglected. The change can be made without having to contact the change manager again. This significantly reduces the amount of work required by the persons responsible for the process.

One of the reasons for hardware or software changes is interference. ** Incident ** is a departure from the standard operation of an IT service (** Service **) that actually or potentially reduces service quality or even interrupts service.
If the cause of a fault is not recognizable, then there is a problem to be investigated in detail. The term ** problem ** refers to one or more similar disorders of unknown cause in ITIL. When the underlying cause is identified and a way to resolve or work around the problem becomes known, a problem becomes a known error (Known Error). The solution is documented in a request for change (RfC) and implemented under the control of change management.

In addition to the specific terminology of change management (for example, from ITIL), those entrusted with it should be familiar with the terminology of information security.

### 3.2 Literature

Additional information on threats and security measures in the area of ​​"patch and change management" can be found in the following publications, among others:

*

 #### [GSKHM] Tools for using the IT-Grundschutz catalogs

  

 BSI, (last accessed on 05.10.2017)
 [https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Hilfsmittel/Bausteine/bausteine\_node.html](https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ ITGrundschutzKataloge / resources / blocks / bausteine_node.html)
