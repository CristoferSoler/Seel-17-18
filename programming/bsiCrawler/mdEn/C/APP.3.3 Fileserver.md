1 description
--------------

### 1.1 Introduction

A file server (or file server) is a server in a network that centrally provides files for all authorized users or clients. The data can be used by authorized users at the same time, without this z. B. to removable media or to distribute by e-mail. By keeping the data central, the data can be structured and provided in different file versions. For file servers, rights can be assigned centrally and data backup can be done centrally.

A file server usually manages mass storage devices that are connected to it via interfaces such as SCSI (Small Computer System Interface) or SAS (Serial Attached SCSI). The memories are located either directly in the housing of the file server or are connected externally. The latter is often referred to as Directly Attached Storage (DAS). A file server can work on conventional server hardware or a dedicated appliance, such as a server. As a Network Attached Storage (NAS) operated. In the case of large volumes of data, central storage area networks (SANs) can often be connected via HBA (Host Bus Adapter) in the server and SAN switches.

### 1.2 Objective

This module describes the specific threats for a file server and the resulting requirements for safe operation.

### 1.3 Delimitation

This module contains basic requirements that must be observed and fulfilled when operating file servers. General and operating system-specific aspects of a server are not the subject of the present module, but are dealt with in the SYS1.1 General Server module and in the corresponding operating system-specific components of the IT systems layer. For example, SYS.1.3 Unix Server or SYS.1.2.2 Windows Server 2012. Furthermore, no requirements for storage systems or storage networks are described; these can be found in the SYS.1.8 Storage Systems block. Also, it does not deal with dedicated services that can be used to run a file server, e.g. B. samba.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to file servers:

### 2 1 Failure of a file server

If a file server fails, the entire information network can be affected and thus also important business processes of the institution. In addition to users, applications may rely on data from the file server to function properly. If the availability of data and services is not given, z. Deadlines are not met or essential business processes fail. If no emergency management concept has been implemented, recovery times can increase further. In many cases this will lead to financial losses of the institution or it will affect other institutions.

### 2 2 Inadequate dimensioning of the file server

If the line connection or storage capacity of the file server is insufficiently dimensioned, access times may increase or memory bottlenecks occur. For example, there is a risk that employees will be frustrated by the lengthy wait times and begin storing data locally. This means that it is no longer possible to understand where data is stored and who owns the data.

### 2 3 Inadequate review of dropped files
If a file server is insufficiently included in the concept of protection against malicious programs of the institution, there is a risk that attackers unnoticed place malicious software on the file server. As a result, the data on the file server can be viewed unauthorized or manipulated. But there are also security risks for all devices and applications that access the file server's data. For example, malware can quickly spread throughout the institution.

### 2 4 Missing or insufficient access authorization concept

If access authorizations and approvals are not properly designed and assigned, third parties may be able to access data without authorization. This allows attackers to modify, delete or copy data.

### 2 5 Unstructured data management

If the storage structure is not specified or the employees do not stick to it, data can be stored in a confusing and uncoordinated manner on the file server. This leads to various problems, such as space wastage due to redundancy, unauthorized access when z. For example, files reside in directories or file systems that are made accessible to third parties, or that are not consistent versions.

### 2 6 Unsuitable installation of the file server

If file servers are set up in easily accessible locations, attackers can directly access their components and thus the stored data, eg. B. by removing drives or remove and take away. Smaller NAS systems can also be easily stolen completely. It is also possible that an attacker directly leverages the access restrictions on the file server and thus can view sensitive data. Once he has access, he can also import malicious programs and thus jeopardize the security of the entire network.

### 2 7 Lack of or insufficient data protection concept

If a file server fails completely, individual components are defective or an employee unintentionally deletes files, important data can be lost without a functioning backup. In addition, if no RAID (Redundant Array of Independent Disks) are used, the failure of a single disk has a direct effect on the current operation, since the files are no longer available.

3 requirements
---------------

The following are specific requirements for the Fileserver area. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### APP.3.3.A1 Suitable installation [Building services]

File servers MUST NOT be operated in offices or as workstations. They MUST be placed in locations to which only authorized persons have access. In addition, attention must be paid to a vibration-free or vibration-free environment of the file server. Even file servers with additional functions, such as NAS systems combined with a WLAN access point or with direct connections for memory cards, MUST be set up suitably. Furthermore, a safe power supply and according to the manufacturer's recommended ambient temperature and humidity MUST be ensured.

#### APP.3.3.A2 Use of RAID systems

It MUST be planned whether a RAID system is used in the file server. A decision against such a system MUST be documented comprehensible. If a RAID system is to be used, it MUST be decided:
* which RAID level should be used to logically group the volumes
* how long the period of time for a RAID Rebuild process may be and
* whether a software or a hardware RAID should be used.
The RAID levels MUST conform to the state of the art. For a hardware RAID, the RAID controller SHOULD be redundant. In a RAID, hot spare disks SHOULD be kept.

#### APP.3.3.A3 Use of antivirus programs

Depending on the operating system and other existing protection mechanisms, the file server MUST be included in the concept of protection against malicious programs of the institution. The used anti-virus program MUST regularly check files released via the file server. In addition to real-time and on-demand scans, the solution MUST also be able to search compressed files for malicious programs. In addition, she SHOULD be able to check encrypted files.

All data MUST be scanned for malware by the antivirus solution before it is placed on the storage media. Both the virus signatures and the antivirus software itself MUST be updated on an ongoing basis. It MUST be ensured that users can not make any security-relevant changes to the settings of the antivirus solution.

#### APP.3.3.A4 Regular backup

All data stored on the file server MUST be backed up regularly. For this, a data backup concept MUST be created, which among other things defines in which intervals the backup should be carried out. In addition, a backup MUST be performed if something is installed or reconfigured on the file server. All secured data MUST be restored at any time. The maximum recovery time SHOULD be collected and taken into account in the data backup concept.

#### APP.3.3.A5 Restrictive allocation of rights

Access rights to the files managed by the file server MUST be granted restrictively. It MUST be ensured that each user can only access the data he needs to perform his tasks. System directories and files MUST NOT be shared with unauthorized users.

It MUST be checked on a regular basis to see if the access permissions are still up to date and comply with the security policy. In addition, there must be a defined process to re-establish, change, or revoke permissions. All access rights MUST be traceable documented.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​file servers. They SHOULD be implemented in principle.

#### APP.3.3.A6 Obtaining a file server

Before a file server is procured, a list of requirements SHOULD be created to evaluate the products available on the market. The performance, the storage capacity, the bandwidth and the number of users who should use the file server SHOULD be taken into account when purchasing the file server.

#### APP.3.3.A7 Selecting a file system

A REQUEST LIST SHOULD be created to evaluate the file systems. To ensure transaction security, the file system SHOULD provide a journaling feature. Also, it SHOULD have a protection mechanism that prevents two users or applications from writing to a file at the same time. A file system should be selected that does not exceed a defined overhead limit. For high availability solutions, distributed file systems SHOULD be used.

#### APP.3.3.A8 Structured Data Management [User]
It SHOULD be determined a structure, according to which data are to be stored. Users SHOULD be informed regularly about the required structured data management. It SHOULD be determined in writing which data may be stored locally and which on the file server. Program and work data SHOULD be stored separately. It SHOULD be checked regularly whether the specifications for structured data management are adhered to.

#### APP.3.3.A9 Secure storage management

All storage resources of the file server SHOULD be cataloged, eg. Hard disks, flash memory, tape drives. In addition, it should be checked regularly whether the memory is still working as intended. In order to be able to react quickly in the event of bottlenecks, replacement storage tanks SHOULD be reserved.

If a memory hierarchy (primary, secondary or tertiary memory) has been set up, (partially) automated memory management SHOULD be used. If data is distributed automatically, it should be checked manually on a regular basis to see if it works correctly.

Furthermore, the memories used SHOULD be included in the logging concept of the information network. The following events SHOULD at least be logged:

* Activities (modification, addition or deletion of data),
* unauthorized access to data and
* Changes to access rights.
#### APP.3.3.A10 Periodic tests of the backup or recovery concept

It SHOULD be tested regularly to see if backup and recovery works properly. For this, a schedule SHOULD be worked out. Sufficient resources SHOULD be provided to plan, design, and execute the tests.

The results SHOULD be sufficiently documented. Discovered shortcomings SHOULD cause the data protection concept to be revised.

#### APP.3.3.A11 Use of Quotas

It SHOULD be considered setting up Quotas. Alternatively, mechanisms of the file or operating system used should be used, which warn the user at a certain fill level of the hard disk or only give the system administrator write access.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.3.3.A12 Encryption of the data (CI)

All data on the file server SHOULD be encrypted. To do this, the volumes SHOULD be completely encrypted. It should be ensured that the virus protection can check the encrypted files for malware. Cryptographic pots SHOULD be safely generated and kept separate from the data (see also CON.1 Crypto Concept).

#### APP.3.3.A13 Replicating Between Sites (A)

For high-availability systems, adequate replication of data SHOULD take place on multiple volumes. Data SHOULD also be replicated between independent devices or standalone sites. For this, a suitable replication mechanism SHOULD be selected. For replication to work as intended, sufficiently accurate time services should be used and operated.

#### APP.3.3.A14 Use of Error Correction Codes (I)
In principle, error-detecting or error-correcting codes SHOULD be used to store data. The necessary redundant bits SHOULD be included in the planning. It should be noted that, depending on the method used, errors can only be detected with a certain degree of probability and can only be remedied to a limited extent.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the area of ​​"file servers" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [HVK] High Availability Compendium

  

 BSI, (last accessed on 28.09.2017)
 [https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/HVKompendium/hvkompendium\_node.html](https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/ HVKompendium / hvkompendium_node.html)

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008
 <Https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "file server" building block.

* G 0.14 Spying out information (spying)
* G 0.16 Theft of devices, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.27 Resource shortage
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.43 Importing messages
* G 0.44 Unauthorized intrusion into premises
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
