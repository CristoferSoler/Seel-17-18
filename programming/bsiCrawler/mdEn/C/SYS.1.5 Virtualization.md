1 description
--------------

### 1.1 Introduction

Virtualization of IT systems involves running one or more virtual IT systems on a physical IT system. Such a physical IT system is called a virtualization server. Multiple virtualization servers can be grouped together to form a virtual infrastructure. In it, the virtualization servers themselves and the virtual IT systems running on them can be jointly managed.

The virtualization of IT systems offers many advantages for IT operation in an information network. Costs for hardware procurement, power and air conditioning can be saved by using the resources of the physical IT systems more efficiently. However, virtualization is also a challenge for the operation of the information network. Since the virtualization technology used touches on different areas and fields of work in the information network, knowledge and experience from a wide variety of areas must be brought together.

### 1.2 Objective

The module describes how virtualized IT systems in the information network can be safely introduced and operated.

### 1.3 Delimitation

In this module, only the virtualization of complete IT systems is discussed, other techniques, which are also partly associated with the word virtualization (application virtualization using terminal servers, storage virtualization, containers, etc.), are not the subject of this module.

In the field of software development, the terms * virtual machine * and * virtual machine monitor * are also used for runtime environments. Java, Microsoft .NET. Such runtime environments are also not considered in this building block.

Virtual infrastructures are typically managed with special management systems. Since these can be extensively accessed by the virtualization infrastructure, it is important to sufficiently secure them. This affects both the server (physical or virtual) on which the management software is running and the product itself. Details are described in the module NET.1.2 * Network Management *.

Virtualization environments are most commonly used with mass storage (NAS or SAN). Connection and protection of these systems are also not considered in this block (see block SYS.1.8 * Memory Solutions *).

Through virtualization, the networks of the institution must be structured differently. This topic is not covered comprehensively in this module. For this, the building block NET.1.1 * network architecture and design * must be implemented. Network virtualization is also touched on in this module. Security aspects of virtual network components are dealt with in the module NET.1.4 * Network Virtualization *.

In order to secure virtual IT systems, the respective components of the layer * SYS (IT systems) * must be used.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​virtualization:

### 2 1 Faulty virtualization planning

A virtualization server enables the operation of virtual IT systems, integrates the systems in the data center and controls their connection to other infrastructure elements, eg. B. networks and storage networks. Failure to plan how to integrate the virtualization servers technically and organizationally into the existing infrastructure can result in responsibilities for different areas not being clearly defined, such as: For applications, operating systems and network components. Furthermore, the responsibilities of different areas may overlap, or there may be no appropriate rights structure to separate administrative accesses for the different areas.
### 2 2 Incorrect virtualization configuration

Virtualization changes the way servers are provisioned. Resources such as CPU, RAM, network connectivity, and storage are typically configured centrally through a management system and are no longer dictated by hardware and cabling. This can lead to faster configuration errors. If, for example, a highly vulnerable virtual IT system is mistakenly placed in an external DMZ, it can be reached from the Internet and thus be exposed to an increased risk.

### 2 3 Insufficient resources for virtual IT systems

Virtualization servers require storage for the operation of the virtual IT systems, either locally in the virtualization server itself or in a storage network. If the required storage capacities are not sufficiently planned, there are far-reaching risks for the availability of the virtual IT systems and the integrity of the information processed in them. This is especially true when using special virtualization features such as snapshots or overbooking storage space.

Bottlenecks can not only affect the storage space on hard disks or in storage networks, but also the main memory (RAM) or the network connection. Also, with insufficient resources on the virtualization server, the virtual machines could interfere with each other's operations and eventually stop working or failing.

### 2 4 Information outflow or resource bottleneck through snapshots

A snapshot can be used to freeze and secure the state of a virtual machine. If such a snapshot is restored at a later time, any changes made in the meantime will be lost. As a result, already patched security vulnerabilities can be open again. In addition, open files, file transfers, or database transactions can result in inconsistent data at the time of the snapshot.

In addition, attackers can use snapshots to gain unauthorized access to the data of a virtual IT system. Because if the snapshot was taken on the fly, the contents of main memory are also backed up to disk and can be recovered and analyzed in a virtual environment outside the original IT infrastructure. Likewise, snapshots can become very large and thus the storage capacity can be scarce.

### 2 5 Failure of the management server for virtualization systems

Since the management server controls and manages all the functions of a virtual infrastructure, a failure of this management system means that configuration changes to the virtual infrastructure can not be made. Administrators can not respond to issues such as resource bottlenecks or the failure of individual virtualization servers, integrate new virtualization servers into the infrastructure, or create new virtual IT systems. The * Live Migration * and thus the dynamic allocation of resources for individual guest systems is not possible without a management server.

### 2 6 Misuse of guest tools

Guest tools are often run with very high privileges. As a result, they can be misused for denial-of-service attacks, for example, or attackers take over the entire host system with them.

### 2 7 Compromising the virtualization software

The virtualization software (also: hypervisor) is the central component of a virtualization server, it controls all running virtual machines on this server and allocates them processor and memory resources. Successfully attacking this component also results in compromised server virtual IT systems.
3 requirements
---------------

The following are specific requirements for virtualization. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.1.5.A1 Importing Updates and Security Updates

Host operating system, management software and hardware firmware MUST be updated regularly. Existing security updates MUST be imported in a timely manner. First, it must be checked on a test system, whether the security updates are compatible and do not cause any errors.

#### SYS.1.5.A2 Secure use of virtual IT systems

Any virtual IT systems administrator MUST know how virtualization affects the IT systems and applications they run. The access rights for administrators to virtual IT systems MUST be reduced to the actual necessary level.

It MUST be ensured that the network connections necessary for the virtual IT systems are available in the virtual infrastructure. It MUST also be examined whether the requirements for the isolation and encapsulation of the virtual IT systems and the applications operated thereon are sufficiently fulfilled. Furthermore, the virtual IT systems used MUST meet the requirements for availability and data throughput. During operation, the performance of the virtual IT systems MUST be monitored.

#### SYS.1.5.A3 Secure configuration of virtual IT systems

Guest systems MUST NOT access devices and interfaces of the virtualization server. However, if such a connection is necessary, it MUST be established exclusively and only for the necessary duration by the administrator of the host system. Binding regulations MUST be defined for this.

Virtual IT systems SHOULD be configured and protected according to the security guidelines of the institution (see the respective modules of the layer * SYS *).

#### SYS.1.5.A4 Secure configuration of a network for virtual infrastructures

It MUST be ensured that existing security mechanisms (eg firewalls) and monitoring systems can not be circumvented by virtual networks. It also MUST be ruled out that unwanted network connections can be established via virtual IT systems that are connected to multiple networks.

Network connections between virtual IT systems and physical IT systems, as well as virtual security gateways, SHOULD be configured according to the institution's security policies.

#### SYS.1.5.A5 Protection of administration interfaces

All administration and management access to the management system and to the host systems MUST be restricted. It MUST be ensured that the administration interfaces can not be accessed from untrusted networks.

To administer or monitor the virtualization servers or the management systems, sufficiently encrypted protocols should be used. However, if unencrypted and therefore unsecure protocols are used, a separate administration network MUST be used for the administration.

#### SYS.1.5.A6 Logging in the virtual infrastructure

Operating status, utilization and network connections of the virtual infrastructure MUST be logged continuously. If capacity limits are reached, virtual machines MUST be moved and eventually the hardware extended. The logging data SHOULD be evaluated regularly.
#### SYS.1.5.A7 Time synchronization in virtual IT systems

The system time of all productive IT systems MUST always be synchronous (see also OPS.1.1.5 * Logging *).

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state-of-the-art in the area of ​​virtualization. They SHOULD be implemented in principle.

#### SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]

The structure of the virtual infrastructure SHOULD be planned in detail. The current regulations and guidelines for the operation of IT systems, applications, networks and storage networks SHOULD be taken into account. When multiple virtual IT systems are operated on a virtualization server, there should be no conflict in the protection requirements of the IT systems.

Furthermore, the tasks of each group of administrators SHOULD be defined and clearly separated from each other. It should also be regulated which employee is responsible for the operation of which component. The administrators SHOULD be sufficiently qualified.

#### SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]

The structure of the network for virtual infrastructures SHOULD be planned in detail. For this the module NET.1.1 * network architecture and design * should be considered. It should also be checked whether a specific network needs to be set up and used for certain virtualization functions (such as * live migration *).

It SHOULD be planned which network segments have to be set up (eg management network, storage network) and how they can be safely separated and protected from each other. It should be ensured that the productive network is disconnected from the management network (see SYS.1.5.A11 * Administration of the virtualization infrastructure via a separate management network *). The availability requirements for the network SHOULD also be observed and fulfilled.

#### SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]

For virtualization servers and virtual IT systems, processes for commissioning, inventorying, operation and decommissioning SHOULD be defined and established. The processes SHOULD be documented and regularly updated.

When the mission is planned, it should be determined which virtualization capabilities the virtual IT systems are allowed to use.

Before a virtual IT system is operated, it should be checked in a test and development environment whether it is suitable for productive use. Test and development environments SHOULD NOT operate on the same virtualization server as productive virtual IT systems.

#### SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network

The virtualization infrastructure SHOULD only be administered via a separate management network. The available security mechanisms of the used management protocols for authentication, integrity assurance and encryption SHOULD be activated and all insecure management protocols deactivated (see NET.1.2 * Network Management *).

#### SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure

Based on the tasks and roles defined in the planning (see SYS.1.5.A8 * Planning a Virtual Infrastructure *), a rights and roles concept SHOULD be created and implemented for the administration of virtual IT systems and networks, the virtualization server and the management environment , All components of the virtual infrastructure SHOULD be integrated into a central identity and authorization management.

Administrators of virtual machines and administrators of the virtualization environment SHOULD differentiate and be equipped with different access rights.
Furthermore, the management environment SHOULD be able to group virtual machines to introduce appropriate structuring associated with an appropriate administrator role assignment.

#### SYS.1.5.A13 Selection of suitable hardware for virtualization environments

The hardware used SHOULD be compatible with the virtualization solution used. It should be ensured that the manufacturer of the virtualization solution also offers support for the operated hardware over the planned period of use.

#### SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]

For the virtual IT systems used, uniform configuration standards SHOULD be defined. The virtual IT systems SHOULD be configured according to these standards. The configuration standards SHOULD be regularly reviewed and adjusted if necessary.

#### SYS.1.5.A15 Operation of guest operating systems with different protection requirements

If virtual IT systems with different protection requirements are operated together on a virtualization server, it should be ensured that the virtual IT systems are sufficiently encapsulated and isolated from each other. Also, the network separation in the virtualization solution used should be sufficiently secure. If this is not the case, further security measures should be identified and implemented.

#### SYS.1.5.A16 Encapsulation of virtual machines

The functions * Copy * and * Paste * of information between virtual machines SHOULD be disabled.

#### SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure

The operating state of the virtual infrastructure SHOULD be monitored. It SHOULD z. For example, you can check if there are enough resources left and if there might be conflicts with shared resources of a virtualization server.

Furthermore, the configuration files of the virtual IT systems SHOULD regularly be checked for unauthorized changes. It should also be monitored whether the virtual networks are correctly assigned to the respective virtual IT systems.

If configuration changes are made to the virtualization infrastructure, they SHOULD be tested or tested before they are implemented.

#### SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]

All administrators of the virtual environment SHOULD be adequately trained. The training course SOLLTE teaches how virtual infrastructures can be safely set up and operated.

#### SYS.1.5.A19 Regular audits of the virtualization infrastructure

It SHOULD be routinely audited whether the current state of the virtual infrastructure complies with the state defined in the planning and whether the configuration of the virtual components complies with the given default configuration. The audit results SHOULD be documented comprehensibly. Deviations SHOULD be corrected.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)

The virtual infrastructure SHOULD be designed to be highly available. All virtualization servers SHOULD be merged into clusters.

#### SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)

For virtual IT systems, overbooking features for resources SHOULD be disabled.
#### SYS.1.5.A22 Hardening of the Virtualization Server (CI)

The virtualization server SHOULD be hardened. Mandatory access controls SHOULD be used to isolate and encapsulate virtual IT systems in front of each other and over the virtualization server. Likewise, the IT system on which the management software is installed SHOULD be hardened.

#### SYS.1.5.A23 Rights limitation of virtual machines (CI)

All interfaces and communication channels that allow a virtual IT system to read and query information about the host system SHOULD be disabled or disabled. Furthermore, only the virtualization server SHOULD have access to its resources. In addition, it should NOT be possible for virtual IT systems to share so-called * Pages * of memory.

#### SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)

For all virtual IT systems, the snapshot function SHOULD be disabled.

#### SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)

Direct access to the emulated consoles of virtual IT systems SHOULD be kept to a minimum. The virtual systems SHOULD be controlled via the network if possible.

#### SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)

Since the communication between the components of the IT infrastructure is often secured by means of certificates, a Public Key Infrastructure (PKI) SHOULD be used.

#### SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)

It SHOULD use certified EAL 4 or higher virtualization software.

#### SYS.1.5.A28 Encryption of virtual IT systems (CI)

All virtual IT systems SHOULD be encrypted.

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the area of ​​"virtualization" can be found in the following publications, among others:

* #### [CSE113] CSE-113: Server virtualization

  

 CSE-113: Server Virtualization, BSI Cyber ​​Security Release, 03.2015
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_113.htm](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_113.htm)

 
* #### [ISFSY13] Information Security Forum (ISF)

  

 especially Area SY1.3 - Virtual Servers, 06.2016

 
* #### [NIST800125] NIST Special Publication (SP) 800-125, Guide to Security for Full Virtualization Technologies, 01-2011

  

 <Http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-125.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "virtualization" building block.

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
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.40 Denial of Service
* G 0.43 Importing messages
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.15 Listening
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
* G 0.18 Missing planning or missing adjustment
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
* G 0.19 Disclosure of information worthy of protection
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
* G 0.20 Information or products from unreliable sources
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.21 Manipulation of hardware or software
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.22 Manipulation of information
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A4 Secure configuration of a network for virtual infrastructures
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
* G 0.25 Failure of devices or systems
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.26 Malfunction of equipment or systems
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A7 Time synchronization in virtual IT systems
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.27 Resource shortage
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
  * SYS.1.5.A3 Secure configuration of virtual IT systems
  * SYS.1.5.A6 Logging in the virtual infrastructure
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.1.5.A1 Importing Updates and Security Updates
  * SYS.1.5.A10 Implementing Administrative Processes for Virtual IT Systems [IT Leader]
  * SYS.1.5.A11 Administration of the virtualization infrastructure via a separate management network
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A13 Selection of suitable hardware for virtualization environments
  * SYS.1.5.A14 Uniform Configuration Standards for Virtual IT Systems [IT Leader]
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A17 Monitoring the health and configuration of the virtual infrastructure
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
  * SYS.1.5.A19 Regular audits of the virtualization infrastructure
* G 0.29 Violation of laws or regulations
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A5 Protection of administration interfaces
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A9 Network Planning for Virtual Infrastructures [Head of IT, Head of Networks]
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A16 Encapsulation of virtual machines
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.1.5.A8 Planning a Virtual Infrastructure [Head of IT, Head of Networks]
  * SYS.1.5.A18 Training Virtual Site Administrators [Supervisors, Head of IT, Heads of Networks]
* G 0.32 Abuse of permissions
  * SYS.1.5.A2 Secure use of virtual IT systems
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
  * SYS.1.5.A21 Secure configuration of virtual IT systems with increased protection requirements (IA)
  * SYS.1.5.A22 Hardening of the Virtualization Server (CI)
  * SYS.1.5.A23 Rights limitation of virtual machines (CI)
  * SYS.1.5.A24 Disabling Snapshots of Virtual IT Systems (CIA)
  * SYS.1.5.A25 Minimal use of console access to virtual IT systems (A)
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
  * SYS.1.5.A27 Use of Certified Virtualization Software [IT Leader] (CIA)
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
  * SYS.1.5.A12 Rights and Roles Concept for the Administration of a Virtual Infrastructure
* G 0.40 Denial of Service
  * SYS.1.5.A26 Use of a PKI [Head of IT, Head of Networks] (CIA)
* G 0.43 Importing messages
  * SYS.1.5.A15 Operation of guest operating systems with different protection requirements
  * SYS.1.5.A20 Use of Highly Available Architectures [Head of IT, Head of Networks] (A)
* G 0.46 Loss of integrity of sensitive information
  * SYS.1.5.A28 Encryption of virtual IT systems (CI)
