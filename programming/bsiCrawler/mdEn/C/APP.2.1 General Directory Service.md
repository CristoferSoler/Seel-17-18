1 description
--------------

### 1.1 Introduction

A directory service provides information on any objects in a defined manner in a data network. With an object related attributes can be stored, for example, to a user ID name and first name of the user, the personnel number and the computer name. These data can then be used equally by different applications. The directory service and its data are usually managed from a central location.

Some typical uses of directory services are:

* Administration of address books, eg. For example, for phone numbers, e-mail addresses, certificates for electronic signatures
* Resource management, eg. For computers, printers, scanners and other peripherals
* User administration, eg. For example, to manage user accounts and user permissions
* Authentication, eg For example, to log on to operating systems or applications
Directory services are optimized for read access because data is typically retrieved from the directory service. Write accesses, such as creating, changing or deleting entries, are less often necessary.

### 1.2 Objective

The aim of the module is to operate general directory services securely and to adequately protect the information processed with them.

### 1.3 Delimitation

This module considers general security aspects of directory services regardless of the product used. For product-specific security aspects, the IT-Grundschutz Compendium contains further components that must also be applied to the respective directory service.

An example of this is Microsoft Active Directory (see APP.2.2 * Active Directory *). Other directory services are based on the freely available OpenLDAP (see APP.2.3 * OpenLDAP *), which is used in many Unix-based systems and, for example, also used by Apple's macOS. Components for server systems on which directory services are usually operated are listed in the SYS.1 * Server * layer of the IT Baseline Protection Compendium.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​general directory service:

### 2 1 Lack of or insufficient planning of the use of directory services

The security of directory services relies heavily on the security of the base operating system, and especially on file system security. Directory services can be installed and operated on a variety of operating systems, which can result in a wide variety of security settings to be made. This diversity increases the planning requirements and requires appropriate knowledge of the underlying operating system. If the resulting overall solution is very heterogeneous or complex, an insufficiently planned use of the directory service in active operation can lead to security gaps. Since directory services also make use of role-based administration of the directory database and individual administration tasks can be delegated, incorrect administration of the administration tasks runs the risk of insecure or inadequate administration of the system.

### 2 2 Incorrect or inadequate planning of partitioning and replication in the directory service
Partitioning is a division of the directory data of a directory service into individual subareas (partitions). The replication of partitions of the directory service is usually used for load balancing. Furthermore, the redundancy in the data storage improves the reliability and thus increases the availability. Therefore, a suitable planning is of crucial importance here, since subsequent changes to the partition and replication settings are possible, but can sometimes cause problems. Planning the partitioning and replication of the directory service incorrectly or inadequately may result in data loss, inconsistencies in data management, poor directory service availability, overall poor system performance, and even outages.

### 2 3 Incorrect or inadequate planning of access to the directory service

Managing access and access rights in the context of a directory service is an extremely labor-intensive task, which in extreme cases requires many manual steps that can lead to errors and shortcomings in the overview of work performed. Inadequate planning of whether and what data may be transmitted in clear text may cause inconsistencies or contradictions with organizational security policies. Also, improper planning of directory security security measures and techniques can lead to incompatibilities or even encryption failure to protect confidential data, which can have a direct impact on confidentiality and integrity.

### 2 4 Incorrect administration of access and access rights

Access rights to an IT system and access rights to stored data and IT applications may only be granted to the extent necessary for the tasks to be performed. The same applies to the permissions granted to users and groups managed by a directory service. If these rights are administered incorrectly, this will lead to malfunctions if necessary rights have not been assigned. On the other hand, there may be security vulnerabilities if more than necessary rights are granted. If the access rights in the directory service are assigned incorrectly or inconsistently, the security of the entire system is considerably jeopardized. A particularly critical point is also the administration rights. If these rights are assigned incorrectly, the entire administration concept can be called into question or even the administration of the directory system itself may be blocked.

### 2 5 Incorrect configuration of access to directory services

In many usage scenarios, other applications, such as Internet or intranet applications, must access the directory service. A misconfiguration can lead to incorrect access to access rights or unauthorized access to the directory service, or to the fact that data for authentication can be transmitted in plain text and thus unencrypted information can be spied out.

### 2 6 Directory Services Failure and Encryption Failure

Technical failures due to hardware or software problems may cause directory services or parts thereof to fail. As a result, the data held in the directory are temporarily inaccessible. In extreme cases, data can be lost. This can hinder business processes and internal work processes. If functional copies of the failed system parts are available, access is still possible, but depending on the selected network topology, this may only be limited.

### 2 7 Compromise of directory services due to unauthorized access
If an attacker has managed to successfully bypass a necessary authentication against the directory service, he can generally access a variety of data for which he should not be authorized. Thus, the entire directory service can be compromised. In addition, unauthorized persons could gain access to network resources or services through extended permissions. This can lead to an attacker bypassing all directory service defenses. This could affect or even destroy the affected system. The security of a directory service can also be compromised if anonymous users are allowed. By not checking their identity, anonymous users can first direct arbitrary queries to the directory service, through which they obtain at least partial information about its structure and content. In addition, when anonymous access is allowed, DoS attacks on the directory service are easier to implement because attackers have more accessibility that is difficult to control.

3 requirements
---------------

The following are specific requirements for the General Directory Service area. Basically, the IT operation is responsible for meeting the requirements. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### APP.2.1.A1 Creating a directory services security policy

A security policy for the directory service MUST be created. This SHOULD be coordinated with the overarching security concept of the entire institution.

#### APP.2.1.A2 Planning the Use of Directory Services [Data Protection Officer, Specialist Responsible]

The use of directory services MUST be carefully planned. In addition to determining the use of the directory service, a model of object classes and attribute types MUST be developed that meets the requirements of the intended use. During the planning of the directory service, staff representatives and data protection officers MUST be involved. A needs-based authorization concept for directory service MUST be designed. In general, the planned directory service structure SHOULD be fully documented. Actions SHOULD be planned to prevent the unauthorized collection of data from the directory service.

#### APP.2.1.A3 Establishment of Access Permissions on Directory Services [Specialists]

The administrative tasks for the administration of the directory service itself as well as for the actual management of the data MUST be strictly separated. The administrative activities SHOULD be delegated in such a way as to avoid any overlap. All administrative tasks and permissions SHOULD be sufficiently documented.

The access rights of the user and administrator groups MUST be configured and implemented based on the created security policy. When merging multiple directory service trees, the resulting effective rights MUST be controlled.

#### APP.2.1.A4 Secure installation of directory services

A MUST be created for the installation, after which administration and access permissions are already configured during the installation of the directory service.

#### APP.2.1.A5 Secure configuration and configuration changes of directory services
The directory service MUST be securely configured. For the secure configuration of a directory service infrastructure, the clients (computers and programs) MUST be included in addition to the server.

Administrative access to the directory service MUST be protected. When making configuration changes to the networked IT systems, users SHOULD be informed about maintenance in a timely manner. Before the configuration changes, backups of all affected files and directories SHOULD be made.

#### APP.2.1.A6 Secure operation of directory services

The security of the directory service MUST be permanently maintained during operation. All policies, regulations and processes concerning the operation of a directory service system SHOULD be documented. Access to all administration tools MUST be prevented for normal users.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state of the art in the area of ​​general directory service. They SHOULD be implemented in principle.

#### APP.2.1.A7 Creation of a security concept for the use of directory services

The security concept for directory services SHOULD regulate all security-related topics of a directory service. The resulting security guidelines SHOULD be recorded in writing and communicated to the extent necessary to the users of the directory service.

#### APP.2.1.A8 Planning partitioning and replication in the directory service

When partitioning, the availability and protection needs of the directory service SHOULD be taken into account. The partitioning of the directory service SHOULD be documented in writing, so that it can be reconstructed manually. In order to be able to perform the replications on time, a sufficient bandwidth should be ensured.

#### APP.2.1.A9 Appropriate Selection of Directory Services Components [Specialists]

For the use of a directory service, suitable components SHOULD be identified. A list of criteria SHOULD be created to select and procure the components for the directory service. As part of the planning and design of the directory service requirements for its security should be formulated depending on the purpose.

#### APP.2.1.A10 Training on administration and operation of directory services

Administrators SHOULD be familiar with all security mechanisms and aspects of directory services in their field of activity. You SHOULD be trained before setting up and then regularly.

#### APP.2.1.A11 Setting up access to directory services

Access to the directory service SHOULD be configured according to the security policy. If the directory service is used as a server on the Internet, then it SHOULD be protected accordingly by a security gateway. If anonymous users are to be granted further access to individual subareas of the directory tree, a separate user account, a so-called proxy user, SHOULD be set up for anonymous access. Furthermore, the access rights for this proxy user SHOULD be granted sufficiently restrictive. They SHOULD be completely withdrawn again when the account is no longer needed. In order to prevent the unnecessary release of security-sensitive information, the search function of the directory service should be suitably limited to the intended purpose.

#### APP.2.1.A12 Directory Services Monitoring

To monitor directory services, a surveillance concept SHOULD be designed and implemented. Directory service specific events and events of the operating system SHOULD be observed, logged and evaluated.
#### APP.2.1.A13 Securing Communication with Directory Services

The data exchange between client and directory service server SHOULD be secured, this applies in particular to external connections. It SHOULD be defined to which data may be accessed. In the case of a service-oriented architecture (SOA), to protect service entries in a service registry, all requests to the registry should be checked for validity of the user.

#### APP.2.1.A14 Regulated decommissioning of a directory service [specialist responsible]

When decommissioning the directory service SHOULD be made sure that further required rights or information are sufficiently available, but all others are deleted. In addition, users SHOULD be notified when a directory service is taken out of service. When decommissioning individual partitions of a directory service, care should be taken not to affect other partitions.

#### APP.2.1.A15 Migration of directory services

For a planned migration of directory services, a migration concept SHOULD be created in advance. The schema changes made to the directory service SHOULD be documented. Extensive permissions used to perform the directory service migration SHOULD be reset. The access rights for directory service objects on systems that were upgraded from previous versions or adopted by other directory systems SHOULD be updated.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.2.1.A16 Creation of a directory service failure plan (CIA)

As part of emergency preparedness, needs-based contingency planning for directory services SHOULD be carried out. SHOULD have contingency plans in place for the failure of major directory service systems. All emergency procedures for the entire system configuration of directory service components SHOULD be documented.

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the area of ​​the "general directory service" can be found in the following publications, among others:

* #### [ISFTM12] The Standard of Good Practice - Area 1.2 Security Event Logging

  

 especially Area TM 1.2 Security Event Logging, Information Security Forum (ISF), 06.2016

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008
 <Https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf>

 
* #### [TKOM1] Telekom - Privacy and Security Assessment Procedure

  

 Proxy server, Deutsche Telekom, 10.2016
 <Https://www.telekom.com/de/verantwortung/datenschutz-und-datensicherheit/sicherheit/sicherheit/privacy-and-security-assessment-verfahren-342724>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the module "General directory service".

* G 0.11 Failure or disruption of service providers
* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.27 Resource shortage
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.33 Personnel loss
* G 0.36 Identity theft
* G 0.37 denying actions
* G 0.38 Abuse of personal data
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.42 Social engineering
* G 0.43 Importing messages
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
