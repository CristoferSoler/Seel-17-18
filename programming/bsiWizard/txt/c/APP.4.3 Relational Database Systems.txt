Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Database systems (DBS) are a widely-used tool for organizing, creating, modifying, and managing large collections of data. A DBS consists of the so-called database management system (DBMS) and one or more databases. A database is a collection of data together with their description (metadata), which are stored persistently in the database system. Since database systems are of central importance in an IT infrastructure, they result in essential security requirements. In most cases, the core processes of an institution depend on the information from the databases, resulting in corresponding availability requirements. In addition, there are often high demands on the confidentiality and integrity of the information stored in the databases.

### 1.2 Objective

The goal of the module is to be able to operate relational database systems safely and to adequately protect the information that is processed and stored in databases. For this purpose, requirements are described with which database systems can be safely planned, implemented and operated, and which can reduce specific hazards.

### 1.3 Delimitation

This module describes requirements for relational database systems. Security requirements for non-relational database systems are not the subject of this module, but are listed in the module APP.4.5 * Non-relational database systems *.

In order to consistently protect the information in the databases, security requirements should already be taken into account in the development of the database tables and access to the database. However, requirements for this are not listed in this module, but can be found z. In CON.3 * software development *, APP.3.1 * web applications * and APP.3.5 * web services *.

Similarly, the module does not address hazards and requirements that affect the operating system and hardware underlying the database system. Aspects can be found in the corresponding operating system-specific building blocks of the layer IT systems, eg. SYS.1.3 * Unix server * or SYS.1.2.2 * Windows Server 2012 *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in relational database systems:

### 2 1 Insufficient sizing of system resources

If the hardware of a database system does not have enough system resources, there is a risk that the database will fail or malfunction. As a result, for example, data can not be saved. At peak times, resources can also be used to a great extent, thereby impairing performance. This, in turn, may result in applications not running or not performing properly.

### 2 2 Enabled standard user accounts

During the initial installation or in the delivery state of a database management system, user and administration accounts are often not secured or only with passwords that are publicly known. There is a risk that these accounts will be misused. For example, an attacker with the publicly known credentials can log in to the database management system as a user or even as an administrator. Then he can read, manipulate or delete the configuration or the stored data.

### 2 3 Insufficient allocation of authorizations
If authorizations are assigned or managed incorrectly, persons in charge or users of the database management system can receive authorizations that go beyond what is absolutely necessary. Thus, it is possible that the overly entitled persons or users carry out unauthorized actions on the database management system that have far-reaching consequences, as the following example shows:

An incorrect SQL statement (for example, in an installation script) unintentionally deletes a large number of records in the database. Afterwards it is determined that the user actually only needed read-only rights for these data records, but also unnecessarily had delete rights.

### 2 4 Unencrypted database connection

In the default configuration, many database management systems connect to the applications unencrypted. If communication between applications and the database management system is unencrypted, transmitted data and access information can be read or manipulated in transit.

### 2 5 Data loss in the database

Hardware or software failure as well as human error may cause data loss in the database. Since databases usually store important information for applications, services can fail or entire production processes can be shut down.

### 2 6 Loss of integrity of stored data

Incorrectly configured databases, software errors, or manipulated data may violate the integrity of the information in the database. If this is not noticed or noticed late, core processes of the institution can be severely impaired. For example, if the integrity relationships (referential integrity) between the tables are not defined correctly, it may cause the data in the database to be in a bad state. If this error is only noticed during productive operation or not at all, not only the inconsistent data must be laboriously cleaned up and reconstructed. Over time, the extent of damage can also have occurred, for example if critical data (tax-relevant data, billing data or even control data for entire production systems) is concerned.

### 2 7 SQL injections

One common attack on database systems is SQL injection. If an application accesses the data in a SQL database, commands are sent to the DBMS in the form of SQL statements. If input data within the application is insufficiently validated, an attacker can inject their own SQL commands into the application, which are then processed with the authorization of the service account of the application. An attacker could read, manipulate, delete, add new data, or invoke system commands. Although SQL injections primarily affect the applications in the frontend, they have a significant impact on the database system itself and the associated infrastructure.

### 2 8 Insufficient patch management

Due to the extensive range of functions of the database management systems, errors or weaknesses occur relatively frequently, which are remedied by patches and updates by the manufacturer. However, if these are not brought in or are recorded too late, weak points can be exploited and the database management system successfully attacked. This makes it possible for attackers to manipulate the systems to drain business-critical data, shut down services or shut down entire production processes.

### 2 9 Insecure configuration of the database management system
Often, in the default configuration of the database management system, unneeded features are enabled that make it easier for a potential attacker to read or manipulate information from the database. For example, an attacker can connect to an unused programming interface by an unmodified default installation to administer the DBMS without having to authenticate. This allows him to access the databases of the institution without authorization.

### 2 10 malware and insecure database scripts

In many database management systems, it is possible to automate certain actions via scripts executed in the context of the database, e.g. Using the Procedural Language / Structured Query Language (PL / SQL). These include, among others, so-called database triggers. However, if these are used unchecked by those responsible, there is a risk that the database scripts will not meet the requirements of the institution's software development.

Also, an attacker could manipulate core functions (such as Data Dictionary Tables) of a database, such as by using malicious programs or database scripts. This type of attack is difficult to detect. Quality deficiencies in these scripts and malware can compromise the confidentiality as well as the integrity and availability of the data stored in the databases.

3 requirements
---------------

The following are specific requirements for the Database Systems area. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### APP.4.3.A1 Creating a Security Policy for Database Systems [Information Security Officer (ISB)]

Based on the institution's general security policy, a specific security policy for database systems MUST be established, which comprehensibly describes requirements and requirements for how database systems can be operated safely. The policy MUST be known to all staff responsible for database systems and fundamental to their work. If the policy is changed or deviated from the requirements, this MUST be agreed and documented with the ISB. It MUST be checked on a regular basis to see if the directive is still correctly implemented. The results MUST be documented in a meaningful way.

#### APP.4.3.A2 Installation of the database management system

It MUST be ensured that the database management system installation packages come from secure sources. Already published patches MUST be recorded before the DBMS is run.

#### APP.4.3.A3 Basic hardening of the database management system

The database management system MUST be hardened. For this, a checklist with the steps to be performed MUST be compiled and processed. Also, all passwords MUST be changed according to the internal requirements of the institution. All passwords MUST be stored encrypted. Base hardening MUST be periodically reviewed and adjusted if necessary.

#### APP.4.3.A4 Regulated creation of new databases

New databases MUST be created according to a defined process. When a new database is created, basic information about the database MUST be documented in a traceable way.
#### APP.4.3.A5 user and authorization concept

The user and authorization concept (see ORP.4 * Identity and Authorization Management *) of the institution MUST be extended by the authorizations for roles, profiles and user groups required for database management systems.

A process MUST be established that governs how database users and their privileges are created, approved, set up, modified and revoked or deleted. In this case, ONLY as many access rights must be granted as are necessary for the respective tasks (need-to-know principle). All changes SHOULD be documented. The configured users and their associated permissions MUST be periodically reviewed and adjusted as necessary.

#### APP.4.3.A6 Change of password [responsible person]

All database user passwords MUST conform to the institution's password policy (see ORP.4 * Identity and Permissions Management *). It MUST be ensured that the passwords are changed at the slightest suspicion of a security incident. Especially with privileged database accounts and service accounts, a password change SHOULD be carefully planned and, if necessary, coordinated with the users responsible for the application.

#### APP.4.3.A7 Timely import of security updates

Existing security updates for the database management system and operating system MUST be installed in a timely manner. First, it must be checked on a test system, whether the security updates are compatible and do not cause any errors. Before a patch is imported, the database system MUST be backed up (see APP.4.3.A9 * Data backup of a database system *).

In addition, a responsible role MUST be defined to be responsible for regularly reporting known database management system vulnerabilities and available security updates. Furthermore, it MUST be checked whether the update intervals of the database management system can be adapted to the update cycles of the manufacturer. The result SHOULD be traceable documented.

#### APP.4.3.A8 Database logging

Security relevant events of the database system MUST be logged with a unique timestamp. The nature and extent of logging MUST be based on the protection requirements of the information to be processed. Additionally, it must be checked whether the logging of the specialized applications together with the logging of the database covers all required information in order to recognize operational and security-relevant changes to the database infrastructure and the applications. It SHOULD be logged so that the log files are not subsequently editable. More detailed information can be found in OPS.1.1.57 * Logging *.

#### APP.4.3.A9 Data backup of a database system

System backups of the DBMS and the data MUST be performed regularly. Even before a database is recreated, the database system MUST be backed up. For this, the allowable utilities SHOULD be used.

All transactions SHOULD be saved so that they can be recovered at any time. If the backup exceeds the available capacities, an advanced concept (such as incremental backup) SHOULD be created to secure the database. Depending on the protection requirements of the data, the recovery parameters SHOULD be specified (see OPS.1.1.5 * Data Backup) *.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of relational database systems. They SHOULD be implemented in principle.

#### APP.4.3.A10 Selection of suitable database management systems
Before database management systems are procured, requirements for the DBMS SHOULD be defined and documented in a requirements catalog. Thereafter, all eligible database management systems SHOULD be evaluated against the catalog. The results SHOULD be documented.

#### APP.4.3.A11 Sufficient dimensioning of the hardware [Head of IT, specialist responsible]

Database management systems SHOULD be installed on sufficiently sized hardware. The hardware SHOULD have enough reserves to meet any increasing demands. Nevertheless draw down resource bottlenecks during operation, SHOULD these be remedied early. If the hardware is dimensioned, the expected growth for the planned deployment period SHOULD be considered.

#### APP.4.3.A12 Unified Configuration Standard of Database Management Systems [Head of IT, Information Security Officer (ISB)]

For all used database management systems a uniform configuration standard SHOULD be defined. All database management systems SHOULD be configured and operated in accordance with this standard. If it is necessary to deviate from the configuration standard during an installation, all steps should be approved by the ISB and documented in a comprehensible manner. The configuration standard SHOULD be regularly reviewed and adjusted if necessary.

#### APP.4.3.A13 Restrictive handling of database links

It SHOULD be ensured that only those responsible are authorized to create database links (DB links). If such links are created, so-called private DB links MUST be created in preference to public DB links. All DB links created by the responsible persons SHOULD be documented and regularly checked. In addition, DB links SHOULD be taken into account when the database system is backed up (see APP.4.3.A9 * Data backup of a database system *).

#### APP.4.3.A14 Checking the backup of a database system

The data backups SHOULD be regularly checked to see if the integrity of the backup files is still guaranteed. The responsible staff SHOULD regularly practice how databases can be quickly recovered in an emergency.

#### APP.4.3.A15 Training Database Administrators [Supervisors, Head of IT]

It SHOULD be ensured that only adequately trained employees administer the database management system. A training plan SHOULD be created to ensure that database managers receive timely training on information security issues (see ORP.3 * Information Security Education & Training *) and performance, as well as on the features of new versions of the database management system.

#### APP.4.3.A16 Encryption of the database connection

The database management system SHOULD be configured to always encrypt database connections. The cryptographic procedures and protocols used for this purpose SHOULD comply with the internal requirements of the institution (see CON.1 * crypto concept *).

#### APP.4.3.A17 Data Transfer or Migration [Specialists]

If data is transferred to a database either initially or on a regular basis, it should be defined in advance how this data transfer should take place. After data has been acquired, SHOULD check if it is complete and unchanged.

#### APP.4.3.A18 Monitoring the database management system
It SHOULD define parameters, events and operating states of the database management system that are critical to safe operation. These SHOULD be monitored using a monitoring system. Thresholds SHOULD be set for all critical parameters and events. If these values ​​are exceeded, MUST be responded appropriately (eg the responsible staff must be alerted). Application-specific parameters, events and their threshold values ​​SHOULD be coordinated with those responsible for the specialized applications (see also APP.4.3.A11 * Sufficient hardware dimensioning *).

#### APP.4.3.A19 protection against malicious database scripts [developer]

If database scripts are developed, then mandatory quality criteria should be defined (see CON.3 * Software Development *). Database scripts SHOULD undergo detailed functional testing on separate test systems before being used productively. The results SHOULD be documented.

#### APP.4.3.A20 Regular audits

For all components of the database system SHOULD check regularly whether all defined security measures have been implemented and correctly configured. It should be checked whether the documented state corresponds to the actual state, whether the configuration of the database management system corresponds to the documented standard configuration, whether all database scripts are required and whether they meet the quality standard of the institution. In addition, the log files of the database system and the operating system SHOULD be examined for abnormalities (see DER.1 * Detection of security-relevant events *). The audit results SHOULD be traceable documented and compared with the target state. Deviations SHOULD be investigated.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.4.3.A21 Use of a database firewall (CI)

A database firewall SHOULD be used if the application side can not guarantee that the database is sufficiently protected, eg. For example, before SQL injections. Similarly, the database firewall SHOULD prevent unauthorized access to a database. Before a database firewall is used, possible side effects SHOULD be evaluated. When updating database applications, care should be taken to adapt the firewall as well.

#### APP.4.3.A22 Emergency Preparedness (CIA)

For the database management system, a contingency plan SHOULD be created that determines how an emergency operation can be implemented and what resources are required (see DER.4 * Emergency Management *). In addition, the contingency plan SHOULD define how normal operation can be restored from emergency operation. The contingency plan SHOULD set out the required reporting routes, reaction paths, resources and response times of the specialist responsible, allowing a potential emergency to quickly escalate. On the basis of a restart coordination plan, all IT systems dependent on the database SHOULD be determined in advance and taken into account.

#### APP.4.3.A23 Archiving (CIA)

If it is necessary to archive data of a database system, a corresponding archiving concept SHOULD be created. It SHOULD be ensured that the datasets are fully and consistently available again at a later date.
In the archiving concept, both the intervals of the archiving and the retention periods of the archived data SHOULD be specified. In addition, it should be documented with which technique the databases were archived. The archived data SHOULD regularly perform recovery tests. The results SHOULD be documented.

#### APP.4.3.A24 Data encryption in the database (C)

The data in the databases SHOULD be encrypted. The following factors SHOULD be considered beforehand, among others:

* Influence on the performance,
* Key management processes and procedures, including separate key storage and backup,
* Influence on backup recovery concepts,
* functional effects on the database, such as sorting options.
#### APP.4.3.A25 Database System Security Checks (CIA)

Database systems SHOULD be regularly audited using security audits. The security reviews SHOULD consider the systemic and vendor-specific aspects of the database infrastructure used (eg directory services) as well as the database management system used.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on hazards and security measures in the area of ​​"Relational Database Systems" can be found in the following publications, among others:

* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008
 <Https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf>

 
* #### [TELEKOM \ _DB] Security Requirements Database Systems

  

 Privacy and Security Assessment Procedures: Security Requirements Database Systems, Deutsche Telekom, 06.2014
 <Https://www.telekom.com/de/verantwortung/datenschutz-und-datensicherheit/sicherheit/sicherheit/privacy-and-security-assessment-verfahren-342724>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "Relational Database Systems".

* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.27 Resource shortage
* G 0.28 Software vulnerabilities or errors
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.36 Identity theft
* G 0.37 denying actions
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.43 Importing messages
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
