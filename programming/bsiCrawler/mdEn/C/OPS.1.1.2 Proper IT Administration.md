1 description
--------------

### 1.1 Introduction

The ongoing administration of IT systems and components is fundamental to IT operations. The system administrators set up IT systems and applications, observe the operation and react with measures that preserve the function and performance of the systems, or adapt the systems to the changing needs. They also perform a number of security tasks: not only do they keep the systems available, they also implement security measures and verify their effectiveness. For this they have very extensive authorizations, so it is also very important for the security of the information network to protect the system administration against unauthorized access.

### 1.2 Objective

The goal of this module is to demonstrate how proper IT administration meets the security requirements of IT applications, systems, and networks.

On the one hand, with the implementation of this module, the institution ensures that the activities required in the system administration for the security of the information network are carried out properly and systematically. On the other hand, the institution also reacts to the special threats that inevitably arise from dealing with administration privileges and from access to areas worthy of protection of the institution.

### 1.3 Delimitation

The module describes general security requirements for proper IT administration. It considers ongoing administrative activities carried out by designated personnel at the institution's sites. It must be distinguished from remote administration of IT systems via external interfaces as well as remote maintenance of devices and components by the respective manufacturer or supplier, which is considered in the module * OPS.2.4 Remote maintenance *.

The subject of the module are general requirements for the administration process as such. Specific requirements for the management of individual IT systems and components are dealt with in the module * OPS.1.1.2 Network and System Management *. There are corresponding requirements, such as systems installed and put into operation, such as changes and maintenance performed or systems are discarded.

The other building blocks of the area * OPS.1.1 core IT operation * describe aspects of IT operation that are relevant in addition to the present building block. They should therefore additionally be considered and modeled in addition to this module.

A particular security relevance in an institution is the proper administration of users and rights. Therefore, this topic is also covered in a separate building block * * (see * ORP.4 Identity and Permission Management) *.

The requirements described in this module must also be applied if administrative tasks are performed by third parties. Special requirements for such cases are additionally described in the modules * OPS.2.1 Outsourcing for Customers and OPS.3.1 Outsourcing for Service Providers *.

Furthermore, the module Proper IT Administration refers to the regular operation. In exceptional situations, especially in the case of a possible IT attack and the compromising of systems, deviating requirements must be observed, which are described in the relevant building blocks from the area * DER.2 Security Incident Management *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​proper IT administration:

### 2 1 Failures due to unregulated responsibilities
If the IT organization has the administrative responsibilities, eg. If, for example, planning, installation, documentation, patch management and monitoring are not clearly regulated or the regulations are not known and understood to the involved employees, this may mean that security-relevant tasks from these areas are not or not systematically carried out , Typical examples are an unclear definition of the responsibilities between IT and telecommunications technology, between office IT and production facilities or between application and platform operation.

### 2 2 Staff shortages of core competencies

Even administrators can be unplanned or long-term. Without trained representatives, there is no guarantee that the systems and applications they are looking after will continue to operate properly and safely. Administrators sometimes build up a great deal of detailed knowledge of the systems and applications they are looking after, which includes the products and solutions used on the one hand, and the specifics of the deployment environment and the specific configuration on the other hand. With this knowledge, they can quickly recognize error situations and implement requirements more easily, which often leads to the administration of individual persons, especially in complex systems. If this person fails, the knowledge for the institution is no longer available.

### 2 3 Abuse of administrative permissions

Administrative permissions allow extensive access to documents, communication content and databases. Administrators can use these far-reaching permissions not only to perform the tasks assigned to them, but also for their own purposes or in the sense of third parties. So they could z. B. View personnel records or read communications from colleagues. Third, pressure or other incentives could also be used by administrators to misappropriately access data or systems.

### 2 4 Relief from attacks

The privileged system access of the administrators is often the focus of attackers. If administrative tasks are not properly performed, attacks on the information network can be made considerably easier. Negligence may result in errors in the configuration, protective measures provided may not or only insufficiently implemented or suspicions that arise can not be tracked. Causes are z. For example, a lack of security awareness, high time pressure or lack of processes and procedures. This can lead to vulnerabilities that could be exploited by attackers.

### 2 5 Disturbance of operation

Administrative activities directly influence the operation of IT systems and applications. For example, ongoing user sessions can be aborted when IT systems are restarted or legitimate access is prevented when a firewall policy is customized. If such operations are performed without considering how they affect the users and without coordinating them with the affected areas, the operation can be significantly disrupted.

### 2 6 Lack of information on incidents
Deficiencies in the documentation of the IT operation or missing records can lead to the fact that IT security incidents can not be clarified or tracked. Since security incidents are often not easily recognizable, such. If the attack has expired, what extent it has had or how it has been manipulated, this must first be determined by means of suitable investigations. However, this assumes, for example, that the target state of systems prior to the incident is documented and verifiable, or that proper unauthorized changes to systems can be distinguished on the basis of appropriate records. If such information is lacking, incidents are difficult or impossible to resolve. Even a judicial proof against the perpetrators is no longer possible in such cases.

3 requirements
---------------

The following are specific requirements for proper IT administration. Basically, the IT manager is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### OPS.1.1.2.A1 Personnel Selection for Administrative Activities [Head of Personnel]

If employees are to perform administrative tasks within the IT environment, they MUST meet the following criteria, taking into account the security requirements of the systems and applications they are managing:

* Employees MUST have the necessary professional qualifications to properly handle the tasks assigned to them. You must continue to have sufficient knowledge of the IT systems, applications, and platforms that you are managing. Employees MUST master the language used in the institution for documentation and have sufficient command of English to understand typical IT documentation.
* Employees MUST be able to perform the tasks assigned to them reliably and carefully.
* Role separation of administrative and controlling roles (e.g., revision) MUST be made.
The administrators and their representatives MUST have sufficient time to perform their duties diligently. All administrators and their representatives MUST receive sufficient training opportunities

These requirements MUST also be met when administrative tasks are delegated to third parties.

#### OPS.1.1.2.A2 Representation arrangements and emergency preparedness

For all administrative tasks and responsibilities, substitution arrangements MUST be made.

It MUST be ensured that designated representatives have access to the IT systems to be managed. In order to be able to administratively access systems and applications in emergency situations, corresponding emergency users with administration rights SHOULD be set up.

#### OPS.1.1.2.A3 Regulated recruitment of IT administrators [Head of Human Resources]

As employees assume administrative responsibilities within the IT environment, they MUST be trained in their work, particularly in the existing IT architecture and the IT systems and applications they are responsible for. The security regulations valid in the institution and relevant for their activities MUST be made known to the IT administrators. Also, they MUST be required to comply with relevant data protection laws and other legal and operational regulations.
These requirements MUST also be met when administrative tasks are delegated to third parties.

#### OPS.1.1.2.A4 Termination as IT Administrator [Head of Human Resources]

When IT administrators are relieved of their responsibilities, all personal administration identifiers assigned to them MUST be revoked. It MUST be checked, which passwords the departing employees in addition still know, z. B. Superuser access, emergency users, Wi-Fi passwords. Such passwords MUST be changed. Equipment, storage media and means of access (eg tokens, chip cards) given to employees MUST be returned in full.

Furthermore, it MUST be checked whether the departing employees were named as contact person vis-à-vis third parties. z. In contracts or as an Admin-C entry in Internet domains. In this case, the affected parties MUST be informed and new contact persons must be defined. The users of the affected IT systems and applications MUST be informed that the previous IT administrator has left.

These requirements MUST also be fulfilled if administrative tasks have been entrusted to third parties and the employees who work there retire from their duties.

#### OPS.1.1.2.A5 Administration IDs

Each administrator and every administrator representative MUST have their own unique administrator ID. The assigned administration rights MUST be derived from the requirements of the respective IT administration tasks.

Administrators MAY only perform administrative work under these identifiers. They MUST NOT be used for routine activities that do not require extended privileges, such as: B. e-mail communication, information research on the Internet. For such tasks, IT administrators MUST additionally set up personal, non-privileged accounts.

#### OPS.1.1.2.A6 Protection of administrative identifiers

Administration IDs MUST be appropriately protected by appropriate authentication mechanisms. If passwords are used, DO NOT use similar passwords for IT systems in other protection zones.

For administrative access, secure protocols MUST be used if this is not done through a local console. These MUST ensure that state-of-the-art communication is encrypted.

Each login process via an administration ID (LOG) MUST be logged so that it is understandable when, in what way and under which user ID the system was accessed.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in terms of proper IT administration. They SHOULD be implemented in principle.

#### OPS.1.1.2.A7 IT administration regulation [Head of Human Resources]

The powers, duties and responsibilities of IT administrators SHOULD be made mandatory in a work instruction or policy. The distribution of tasks between the individual administrators SHOULD be done in such a way that on the one hand overlaps in the responsibilities are avoided and on the other hand no administration gaps arise. The regulations SHOULD be updated regularly. The specifications SHOULD in particular exclude unauthorized changes of the IT administrators in the information network, as far as these go beyond the explicitly assigned tasks and are not necessary to avert a security incident or incident.

#### OPS.1.1.2.A8 Administration of Specialist Applications [IT Operations]
The basic requirements listed in this module SHOULD also be consistently implemented for employees with administrative tasks for individual specialist applications. The division of tasks between application and system administration SHOULD be clearly defined and recorded in writing. Interfaces SHOULD have defined interfaces between the persons responsible for system and specialist application administration (eg contact person, communication channels, regular exchange).

If there is administrative intervention in the operation of the application (eg version change, maintenance window), this SHOULD be coordinated in advance with the department and take into account the needs of the department.

#### OPS.1.1.2.A9 Sufficient resources for IT operations

Sufficient human and material resources SHOULD be provided to properly handle the administrative tasks involved. It SHOULD be taken into account that appropriate capacities must also be available for unpredictable activities, in particular to handle and clarify safety-relevant events.

Resource planning SHOULD be done in regular cycles, such as B. annually, tested and adapted to the current requirements.

#### OPS.1.1.2.A10 Training and Information [Head of Staff]

For the IT administrators deployed, suitable further education measures SHOULD be taken to ensure that they are always state-of-the-art. It should also take into account technical developments that have not yet begun, but which may become relevant to the institution in the foreseeable future. The training measures SHOULD be supported by a training plan and take into account the entire team, so that all required qualifications in the team are multiple.

Administrators SHOULD regularly check the security of the systems, services and protocols they are looking after, especially current threats and security measures.

#### OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]

System changes SHOULD be comprehensibly documented in an appropriate form. From the documentation SHOULD emerge,

* which changes have been made,
* when the changes have been made,
* who made the changes,
* on what basis or for what occasion the changes have been made.
#### OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]

IT systems SHOULD be maintained regularly. It should be regulated which safety aspects are to be observed during maintenance and repair work and who is responsible for the maintenance or repair of equipment. Employees SHOULD know that maintenance personnel must be supervised while working in the house. Performed maintenance work SHOULD be documented.

#### OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]

Remote maintenance SHOULD only be performed if adequate security measures have been taken. It SHOULD be ensured that remote maintenance access can only ever be initiated by the local IT system. The execution of the remote maintenance SHOULD be sufficiently recorded.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### OPS.1.1.2.A14 Administrators Security Check (CIA)

In the high-security area, an additional security check SHOULD be carried out to confirm the trustworthiness of employees.
#### OPS.1.1.2.A15 Distribution of administrative activities (CI)

There SHOULD be set up different administration roles for subtasks. When defining the tasks, the type of data and the existing system architecture SHOULD be taken into account.

#### OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)

In the case of increased protection requirements, access to administrative interfaces or interfaces with filtering and separating measures SHOULD be technically restricted, ie. H. they SHOULD NOT be accessible to persons outside the relevant IT administration teams. Administrative access to IT systems in other protection zones SHOULD always be done indirectly via a jump server in the respective security zone. Access from other systems or from other security zones SHOULD be denied.

#### OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)

For particularly safety-critical systems, access to identifiers with administrative authorizations SHOULD be implemented in such a way that two employees are required for this. One IT administrator SHOULD perform each of the upcoming administrative tasks while being controlled by another IT administrator.

#### OPS.1.1.2.A18 Consistent logging of administrative activities (CI)

Administrative activities SHOULD be logged if possible. For particularly security-critical systems, all administrative accesses SHOULD be thoroughly and completely logged. The executing IT administrators SHOULD NOT have permission to modify or delete the recorded log files themselves. The log files SHOULD be kept for a period of time that is appropriate to the need for protection and that allows subsequent intrusion into the system.

#### OPS.1.1.2.A19 Consideration of High Availability Requirements [Information Security Officer (ISB)] (A)

IT administrators SHOULD analyze which of the systems and networks they serve to meet high availability requirements. For these areas, they SHOULD make sure that the components and architectures used, as well as the associated operating processes, are suitable to meet these requirements. As a rule, this requires comprehensive high-availability planning.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on hazards and security measures in the area of ​​"Proper IT administration" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [HVK] High Availability Compendium

  

 BSI, (last accessed on 28.09.2017)
 [https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/HVKompendium/hvkompendium\_node.html](https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/ HVKompendium / hvkompendium_node.html)

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the module "Proper IT Administration".

* G 0.14 Spying out information (spying)
* G 0.16 Theft of devices, data carriers or documents
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.27 Resource shortage
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.33 Personnel loss
* G 0.35 coercion, blackmail or corruption
* G 0.37 denying actions
* G 0.42 Social engineering
The cross reference tables can be found in the download area due to their size.
* G 0.14 Spying out information (spying)
  * OPS.1.1.2.A1 Personnel Selection for Administrative Activities [Head of Personnel]
  * OPS.1.1.2.A10 Training and Information [Head of Staff]
  * OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
  * OPS.1.1.2.A19 Consideration of High Availability Requirements [Information Security Officer (ISB)] (A)
  * OPS.1.1.2.A3 Regulated recruitment of IT administrators [Head of Human Resources]
  * OPS.1.1.2.A4 Termination as IT Administrator [Head of Human Resources]
  * OPS.1.1.2.A5 Administration IDs
  * OPS.1.1.2.A6 Protection of administrative identifiers
  * OPS.1.1.2.A7 IT administration regulation [Head of Human Resources]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.1.2.A1 Personnel Selection for Administrative Activities [Head of Personnel]
  * OPS.1.1.2.A10 Training and Information [Head of Staff]
  * OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
  * OPS.1.1.2.A19 Consideration of High Availability Requirements [Information Security Officer (ISB)] (A)
  * OPS.1.1.2.A3 Regulated recruitment of IT administrators [Head of Human Resources]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
* G 0.21 Manipulation of hardware or software
  * OPS.1.1.2.A1 Personnel Selection for Administrative Activities [Head of Personnel]
  * OPS.1.1.2.A10 Training and Information [Head of Staff]
  * OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
  * OPS.1.1.2.A19 Consideration of High Availability Requirements [Information Security Officer (ISB)] (A)
  * OPS.1.1.2.A3 Regulated recruitment of IT administrators [Head of Human Resources]
  * OPS.1.1.2.A4 Termination as IT Administrator [Head of Human Resources]
  * OPS.1.1.2.A5 Administration IDs
  * OPS.1.1.2.A6 Protection of administrative identifiers
  * OPS.1.1.2.A7 IT administration regulation [Head of Human Resources]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
* G 0.22 Manipulation of information
  * OPS.1.1.2.A1 Personnel Selection for Administrative Activities [Head of Personnel]
  * OPS.1.1.2.A10 Training and Information [Head of Staff]
  * OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
  * OPS.1.1.2.A19 Consideration of High Availability Requirements [Information Security Officer (ISB)] (A)
  * OPS.1.1.2.A3 Regulated recruitment of IT administrators [Head of Human Resources]
  * OPS.1.1.2.A4 Termination as IT Administrator [Head of Human Resources]
  * OPS.1.1.2.A5 Administration IDs
  * OPS.1.1.2.A6 Protection of administrative identifiers
  * OPS.1.1.2.A7 IT administration regulation [Head of Human Resources]
  * OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
* G 0.27 Resource shortage
  * OPS.1.1.2.A9 Sufficient resources for IT operations
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A19 Consideration of High Availability Requirements [Information Security Officer (ISB)] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.1.2.A3 Regulated recruitment of IT administrators [Head of Human Resources]
  * OPS.1.1.2.A7 IT administration regulation [Head of Human Resources]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.1.2.A3 Regulated recruitment of IT administrators [Head of Human Resources]
  * OPS.1.1.2.A4 Termination as IT Administrator [Head of Human Resources]
  * OPS.1.1.2.A5 Administration IDs
  * OPS.1.1.2.A6 Protection of administrative identifiers
  * OPS.1.1.2.A7 IT administration regulation [Head of Human Resources]
  * OPS.1.1.2.A8 Administration of Specialist Applications [IT Operations]
  * OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.1.2.A1 Personnel Selection for Administrative Activities [Head of Personnel]
  * OPS.1.1.2.A10 Training and Information [Head of Staff]
  * OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
  * OPS.1.1.2.A19 Consideration of High Availability Requirements [Information Security Officer (ISB)] (A)
  * OPS.1.1.2.A8 Administration of Specialist Applications [IT Operations]
  * OPS.1.1.2.A9 Sufficient resources for IT operations
  * OPS.1.1.2.A10 Training and Information [Head of Staff]
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
* G 0.32 Abuse of permissions
  * OPS.1.1.2.A1 Personnel Selection for Administrative Activities [Head of Personnel]
  * OPS.1.1.2.A10 Training and Information [Head of Staff]
  * OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
  * OPS.1.1.2.A19 Consideration of High Availability Requirements [Information Security Officer (ISB)] (A)
  * OPS.1.1.2.A3 Regulated recruitment of IT administrators [Head of Human Resources]
  * OPS.1.1.2.A4 Termination as IT Administrator [Head of Human Resources]
  * OPS.1.1.2.A7 IT administration regulation [Head of Human Resources]
  * OPS.1.1.2.A8 Administration of Specialist Applications [IT Operations]
  * OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
* G 0.33 Personnel loss
  * OPS.1.1.2.A2 Representation arrangements and emergency preparedness
  * OPS.1.1.2.A9 Sufficient resources for IT operations
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A19 Consideration of High Availability Requirements [Information Security Officer (ISB)] (A)
* G 0.35 coercion, blackmail or corruption
  * OPS.1.1.2.A1 Personnel Selection for Administrative Activities [Head of Personnel]
  * OPS.1.1.2.A10 Training and Information [Head of Staff]
  * OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A14 Administrators Security Check (CIA)
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A16 Access Restrictions for Administrative Access (CIA)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
  * OPS.1.1.2.A19 Consideration of High Availability Requirements [Information Security Officer (ISB)] (A)
  * OPS.1.1.2.A3 Regulated recruitment of IT administrators [Head of Human Resources]
  * OPS.1.1.2.A4 Termination as IT Administrator [Head of Human Resources]
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
* G 0.37 denying actions
  * OPS.1.1.2.A4 Termination as IT Administrator [Head of Human Resources]
  * OPS.1.1.2.A5 Administration IDs
  * OPS.1.1.2.A6 Protection of administrative identifiers
  * OPS.1.1.2.A11 Documentation of IT Administration Activities [IT Operations]
  * OPS.1.1.2.A13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
  * OPS.1.1.2.A18 Consistent logging of administrative activities (CI)
* G 0.42 Social engineering
  * OPS.1.1.2.A3 Regulated recruitment of IT administrators [Head of Human Resources]
  * OPS.1.1.2.A12 Regulations for maintenance and repair work [IT operation]
  * OPS.1.1.2.A15 Distribution of administrative activities (CI)
  * OPS.1.1.2.A17 IT Administration in the Four-Eyes Principle (CI)
