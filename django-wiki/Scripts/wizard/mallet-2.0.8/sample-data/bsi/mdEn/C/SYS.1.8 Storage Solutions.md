1 description
--------------

### 1.1 Introduction

The steady growth of digital information and the increasing amount of unstructured information are leading to the use of centralized storage solutions within institutions. The requirements for such storage solutions are subject to constant change, which can be observed, for example, in the following aspects:

* The data of an institution should be available anytime, anywhere and for different application scenarios. As a result, modern storage solutions often have increased availability requirements.
* The increasing digitization of all information in an institution makes it necessary to comply with and comply with far-reaching legal requirements (compliance requirements).
* Storage solutions should be dynamically adaptable to ever-changing requirements and provide storage space centrally.
In the past, storage solutions were often implemented by connecting storage media directly to a server. However, these so-called direct-attached storage (DAS) systems often can not meet current and future requirements. Therefore, today's widely used central storage solutions and their components are necessary, which can be differentiated as follows:

* Storage solutions: A storage solution consists of one or more storage networks and at least one storage system.
* Storage networks: Storage networks allow access to the storage systems on the one hand and replication of data between storage systems on the other.
* Storage systems: A storage system is the central instance that provides space for other IT systems. A storage system also allows the simultaneous access of several IT systems to the available storage space.
### 1.2 Objective

The aim of this module is to show how centralized storage solutions can be planned, operated and rejected safely.

### 1.3 Delimitation

In this module storage systems are considered together with the associated storage networks. Backup devices that are connected to the storage system or to the storage network are not considered here, but are treated in block OPS.1.2.2 * Archiving *. Conceptual aspects of data backup are explained in the module CON.3 * Data backup concept *. In addition, no requirements for file servers are described. These can be found in the module APP.3.3 * Fileserver *.

If external service providers are used to run a storage solution, the requirements of the module OPS.2.1 * Outsourcing for Customers * must be considered separately.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​*** *** storage solutions:

### 2 1 Lack or insufficient delineation of storage solutions

Central storage solutions increase the requirements for administration. If the responsibilities for different areas are not clearly defined, this can lead to misconfiguration. For example, if a traditional network administrator administers FC (Fiber Channel, FC) switches, he may be able to access components that he is not responsible for and not trained for. Such an operation may result in FC switches not being properly configured. This could cause important services to fail because all servers attached to the FC switches can no longer access the storage systems.

### 2 2 Unsafe default settings for memory componentsFrequently, memory components are shipped with a default configuration to allow the devices to get up and running quickly with as much functionality as possible. Thus, in many devices not required functions are activated, such. HTTP, Telnet and insecure SNMP versions. If storage components with insecure factory settings are used productively, they can be accessed more easily without authorization. This can lead to z. B. Services are no longer available or unauthorized access to confidential information of the institution.

### 2 3 Manipulation of data via the storage system

An inadequately configured storage area network (SAN) can unintentionally connect networks. If, for example, a server with a SAN connection can be reached from the Internet and thus compromised from the outside, this can be used as an entry point for attackers to unauthorized access to sensitive information stored on the SAN. Since all security and surveillance measures such as firewalls or IDS (intrusion detection systems) can be bypassed in the IT networks of an institution in this way, the potential for damage is great.

### 2 4 Loss of confidentiality through storage-based replication methods

Storage-based replication methods have the purpose of duplicating stored or archived data in real-time over a storage network and thus additionally storing them redundantly. This is to avoid data loss. However, the automated replication of unencrypted data entails risks both in its own network and in the use of public networks: unauthorized access to legitimate replication traffic, for example by means of FC analyzers (FC replication) or sniffers (IP replication).

### 2 5 Access to information from other clients through WWN spoofing

Devices in an FC SAN are managed and assigned internally via World Wide Names (WWNs). They are somewhat the same as the MAC addresses of Ethernet network adapters. Using programs provided by the manufacturer of the Host Bus Adapter (HBA), the WWN of an HBA can be changed. This allows an attacker to access data for which he has no authorization. The manipulation of WWNs, also known as WWN spoofing, poses a considerable potential for danger for an institution. Particularly in connection with multi-tenant storage systems, unauthorized persons can access the information of other clients.

### 2 6 Overcoming the logical network separation

If the network structures of different clients are separated by virtual storage area networks (VSANs) rather than physically separate networks, this can endanger the information security of the institution. If an attacker succeeds in penetrating the network of another client, he can access both the virtual SAN of this client and the transmitted user data.

### 2 7 Failure of components of a storage solution

Complex, network-based storage solutions often consist of many components (such as FC switches, storage controllers, virtualization appliances). If components of a storage solution fail, this can lead to important applications becoming inoperable and data loss threatening.

### 2 8 Obtaining Physical Access to SAN Switches

If an institution has inadequate access and access controls to the components of a storage system or if these are completely lacking, an attacker can gain physical access to existing switches or connect additional FC SAN switches to the network. The target of the attacker could be to access the distributed zoning database to change it so that it can access the storage systems.

3 requirements
---------------The following are specific requirements for storage solutions. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. He is also responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.1.8.A1 Appropriate installation of storage systems [Building Services, IT Manager]

The IT components MUST be installed in secured rooms. These rooms must ONLY have authorized access. In addition, a safe power supply and according to the manufacturer's specifications recommended ambient temperature and humidity must be ensured.

#### SYS.1.8.A2 Secure basic configuration of storage solutions

Before a storage solution is used productively, it MUST be ensured that all software and firmware components used are up-to-date. After that, a secure basic configuration MUST be made.

Unused user accounts MUST be disabled. Also, you MUST change default passwords in accordance with the password policy or create new accounts.

Unused interfaces of the storage system MUST be deactivated. The default configuration, the basic configuration made and the current configuration SHOULD be kept redundant and protected.

#### SYS.1.8.A3 Restrictive rights assignment

For storage solutions, a rights and roles concept MUST be created. All user accounts created on each solution MUST conform to this concept. All user accounts MUST be set up according to the principle of minimum permissions.

#### SYS.1.8.A4 Protection of the administration interfaces

All administration and management accesses of the storage systems MUST be restricted. It MUST be ensured that the administration interfaces can not be accessed from untrusted networks.

Sufficient encrypted protocols SHOULD be used. However, if unencrypted and therefore unsecure protocols are used, a separate administration network MUST be used for the administration.

#### SYS.1.8.A5 Logging on storage systems

The internal logging of the storage systems MUST be configured to log information used to detect problems early.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of storage solutions. They SHOULD be implemented in principle.

#### SYS.1.8.A6 Creating a Security Policy for Storage Solutions [Information Security Officer (ISB)]

Based on the institution's general security policy, a specific security policy for storage solutions SHOULD be created. It should describe in a comprehensible way requirements and specifications how storage solutions can be safely planned, administered, installed, configured and operated.

The policy SHOULD tell all administrators responsible for storage solutions and be fundamental to their work. If the policy is changed or deviated from the requirements, this should be agreed and documented with the ISB. It SHOULD be checked regularly to see if the directive is still correctly implemented. The results SHOULD be sensibly documented.

#### SYS.1.8.A7 Planning Storage Solutions [Information Security Officer (ISB), IT Leader]A REQUIREMENT analysis should be carried out, which among other things considers the topics performance and capacity. Based on the identified requirements, SHOULD then create a detailed planning for storage solutions. The following points should be considered:

* Selection of suitable hardware,
* Selection of manufacturers and suppliers,
* Decision for or against central management systems,
* Planning the grid connection,
* Planning the infrastructure as well
* Integration into existing processes.
#### SYS.1.8.A8 Selecting a suitable storage solution [Information Security Officer (ISB), IT Leader]

The technical basics of different storage solutions SHOULD be examined in detail and their effects on the possible use in the institution should be examined. The possibilities and limits of the different types of storage systems SHOULD be presented transparently to the responsible persons of the institution. The decision criteria for a storage solution SHOULD be documented comprehensibly. Similarly, the decision for the selection of a storage solution should be documented comprehensible.

#### SYS.1.8.A9 Selection of vendors for a storage solution [Information Security Officer (ISB), IT Leader]

Based on the specified requirements for a storage solution, a suitable supplier SHOULD be selected. The selection criteria and the decision for a supplier SHOULD be traceable documented. In addition, aspects of maintenance and servicing SHOULD be written down in Service Level Agreements (SLAs). The SLAs SHOULD be clear and quantifiable. It SHOULD be precisely regulated when the contract with the supplier ends.

#### SYS.1.8.A10 Creation and Maintenance of Operations Manual [Information Security Officer (ISB), IT Leader]

It SHOULD be created an operating manual. It SHOULD document all the necessary rules, requirements and settings required to operate storage solutions. The operation manual SHOULD be updated regularly.

#### SYS.1.8.A11 Safe operation of a storage solution

The storage system SHOULD be monitored for availability of internal applications, system load, and critical events (see also SYS.1.8.A13 * Monitoring and Management of Storage Solutions *). Furthermore, for storage solutions, fixed maintenance windows should be defined in which changes can be made. In particular, firmware or operating system updates of storage systems or the network components of a storage solution SHOULD only be performed within such a maintenance window. All changes SHOULD also be activated via the change management and coordinated with all involved specialists.

#### SYS.1.8.A12 Administrator Training [Supervisor, IT Leader]

The administrators responsible for the storage solutions SHOULD be sufficiently trained. The training SHOULD impart knowledge with which procedures, techniques and tools storage systems and their components can be set up and operated safely. In addition, manufacturer-specific aspects of individual products and components SHOULD be addressed. If an institution uses new products, administrators SHOULD be trained to do so.

#### SYS.1.8.A13 Monitoring and management of storage solutions

To detect and resolve error situations and security issues, you should monitor storage solutions. All collected data SHOULD be checked as to whether the requirements of the operating manual are adhered to (see also SYS.1.8.A10 * Creation and maintenance of an operating manual *).Individual components of the storage solution and the overall system SHOULD be managed centrally. In addition, the essential messages SHOULD be filtered out to better represent them.

If a storage solution is operated by an external service provider, SHOULD define and document how the contracted SLAs are monitored.

#### SYS.1.8.A14 Securing a SAN by segmentation

A SAN SHOULD be segmented. A concept SHOULD be developed that maps the SAN resources to the respective servers. For this purpose it should be decided based on the security requirements and the administrative effort which segmentation should be used in which application scenario. The current resource allocation SHOULD be easily and clearly visible using management tools. Furthermore, the current zoning configuration SHOULD be documented. The documentation SHOULD also be available in emergencies.

#### SYS.1.8.A15 Secure separation of clients in storage solutions

It SHOULD be documented and comprehensibly documented, which requirements the institution places on the multi-client capability of a storage solution. The storage solutions used SHOULD meet these documented requirements.

In the block storage environment, * LUN Masking * SHOULD be used to separate clients. In file service environments SHOULD it be possible to act with virtual file servers. In this case, each client SHOULD be assigned a separate file service.

When using IP or iSCSI, the clients SHOULD be separated by segmentation in the network. If Fiber Channel is used, SHOULD be separated using VSANs and soft zoning.

#### SYS.1.8.A16 Secure deletion in SAN environments

For the storage system SHOULD be determined which information is to be deleted with which method. In multi-tenant storage systems, it should be ensured that logical unit numbers (LUNs) assigned to a specific client are deleted.

#### SYS.1.8.A17 Documentation of the system settings of storage systems

All system settings of storage systems SHOULD be documented. The documentation SHOULD include the technical and organizational requirements as well as all specific configurations of the storage systems of the institution.

If the documentation of the system settings contains confidential information, these should be protected against unauthorized access. The documentation SHOULD be regularly reviewed and always up to date, especially with regard to the assignment of rights. Also SHOULD be made sure that it is available in all emergency scenarios.

#### SYS.1.8.A18 Security audits and reporting on storage systems [Information Security Officer (ISB)]

All used storage systems SHOULD be audited regularly. For this, a corresponding process SHOULD be set up. It SHOULD be regulated, which security reports with which contents are to be created regularly. In addition, it should also be regulated how deviations from specifications are handled and how often and to what extent audits are carried out.

#### SYS.1.8.A19 Disposal of storage solutions

If entire storage solutions or individual components of a storage solution are no longer needed, all existing data SHOULD be transferred to other storage solutions. A transitional phase should be planned for this. Subsequently, all user data and configuration data SHOULD be securely deleted. From all relevant documents, all references to the decommissioned storage solution SHOULD be removed.

#### SYS.1.8.A20 Emergency Preparedness and Emergency Reaction for Storage Solutions [IT Leader]It SHOULD create an emergency plan for the storage solution used. The plan SHOULD describe exactly how to handle certain emergency situations. Also SHOULD include instructions in the form of actions and commands that support error analysis and error correction. To correct errors, suitable tools should be used.

It should be done regular exercises and tests of the emergency plan. After the exercises and tests as well as after an emergency, the generated data SHOULD be safely erased.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.1.8.A21 Use of Client Separation Storage Pools (CI)

Clients SHOULD be allocated storage resources from different storage pools. In this case, a storage medium should always be assigned to only one pool. The logical disks (LUNs) that are generated from such a pool SHOULD only be assigned to a single tenant.

#### SYS.1.8.A22 Deploying a Highly Available SAN Solution [Information Security Officer (ISB)] (A)

It SHOULD use a high-availability SAN solution. The replication mechanisms used SHOULD meet the institution's availability requirements for the storage solution. The configuration of the storage solution SHOULD meet the availability requirements. In addition, a test and consolidation system SHOULD be in place.

#### SYS.1.8.A23 Using Encryption for Storage Solutions [Information Security Officer (ISB)] (CI)

All data stored in storage solutions SHOULD be encrypted. It SHOULD be determined on which levels (data-in-motion and data-in-rest) is encrypted. It should be noted that encryption on the transport path is also relevant for replication and backup traffic.

#### SYS.1.8.A24 Ensuring SAN Fabric Integrity (I)

To ensure the integrity of the SAN fabric, protocols with additional security features SHOULD be used. The following protocols SHOULD consider their security properties and use appropriate configurations:

* Diffie Hellman Challenge Handshake Authentication Protocol (DH-CHAP)
* Fiber Channel Authentication Protocol (FCAP) and
* Fiber Channel Password Authentication Protocol (FCPAP).
#### SYS.1.8.A25 Multiple overwriting of the data of a LUN (C)

In SAN environments, data SHOULD be deleted by overwriting the associated memory segments of a LUN multiple times.

#### SYS.1.8.A26 Securing a SAN through hard zoning

To segment SANs, hard zoning should be used.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the area of ​​"storage solutions" can be found in the following publications, among others:

* #### [27040] ISO / IEC 27040: 2015

  

 Information technology - Security techniques - Storage security, 01.2015
 <Https://www.iso.org/standard/44404.html>

 
* #### [ISFSY14] Information Security Forum (ISF)

  

 The Standard of Good Practice - especially Area SY1.4 Network Storage Systems, 06.2016

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the "memory solutions" block.

* G 0.8 Failure or malfunction of the power supply
* G 0.11 Failure or disruption of service providers* G 0.15 Listening
* G 0.16 Theft of devices, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.24 Destruction of equipment or data media
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.27 Resource shortage
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.40 Denial of Service
* G 0.44 Unauthorized intrusion into premises
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.