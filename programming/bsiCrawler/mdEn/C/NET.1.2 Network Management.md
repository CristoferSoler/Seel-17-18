1 description
--------------

### 1.1 Introduction

Reliable network management is a prerequisite for the secure and efficient operation of modern networks. This requires network management to fully integrate all network components and implement appropriate measures to protect management communications and infrastructure.

Network management includes many important functions, such as: For example, network monitoring, component configuration, event handling, and logging. Another important function is reporting, which can be created as a common platform for the network and IT systems. Alternatively, it can be implemented as a single platform or as part of the individual management components.

The network management infrastructure consists of central management systems (eg SNMP servers), administration terminals with software for management access, decentralized management agents, dedicated management tools (eg probes or specific measuring instruments) , Management protocols (such as SNMP or SSH), and management interfaces (such as dedicated Ethernet ports or console ports).

### 1.2 Objective

The aim of this module is to establish information security as an integral part of network management.

### 1.3 Delimitation

This module considers the necessary components and conceptual tasks for network management. The counterpart in the system management for networked clients and servers is described in the block SYS.5 * System Management *.

The present module specifies the basic requirements of the module NET.1.1 * Network architecture and design. * It also discusses how to build and secure network management and how to protect its communications. However, details regarding the protection of network components, in particular their management interfaces, are dealt with in the component groups NET.2 and NET.3.

The management of the passive network infrastructure is dealt with in the building blocks of the infrastructure (building block layer INF) or industrial IT (building block layer IND). Therefore, these topics are not included in this module.

The logging addressed in this module should be integrated into a comprehensive logging and archiving concept. (see OPS.1.1.5 * Logging *).

The subject of outsourcing is not dealt with in detail in this module. Further requirements are described in the module OPS.2.1 * Outsourcing *.

General considerations for the safe, efficient and orderly operation of network management are described in this module only if it goes beyond the general requirements of the module OPS.1.1.1 * General IT Operations *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in network management:

### 2 1 Unauthorized access to central network management components

If attackers succeed in accessing network management solutions, eg. For example, by unpatched security holes or insufficient network separation, they can control and reconfigure all network components connected there. So you can z. B. to access sensitive information, redirect network traffic or disrupt the entire network sustainable.

### 2 2 Unauthorized access to individual network components

If attackers succeed in accessing individual network components, they can control and manipulate the respective component. Any traffic routed via the network component can thus be compromised. In addition, further attacks can be prepared to penetrate deeper into the institution's network.

### 2 3 Unauthorized interference with network management communication
If the management communication is intercepted and manipulated, active network components can be misconfigured or controlled in this way. This can violate network integrity and limit the availability of the network infrastructure. In addition, the transmitted data can be recorded and viewed.

### 2 4 Inadequate time synchronization of network management components

If the system time of the network management components is insufficiently synchronized, the logging data may not be correlated with each other, or the correlation may lead to incorrect statements, since the different timestamps of events have no common basis. This can not properly govern events that have occurred and problems can not be resolved. As a result, for example, security incidents and data outflows can go undetected.

3 requirements
---------------

The following are specific requirements for network management. Basically, the IT operation is responsible for meeting the requirements. In addition, the Information Security Officer (ISB) should always be involved in strategic decisions. He is also responsible for ensuring that all requirements are met and regularly reviewed in accordance with established security policies. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These roles are listed in square brackets in the heading of each requirement.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### NET.1.2.A1 Planning the network management

The network management infrastructure MUST be planned appropriately. All points addressed in the security guideline and requirements specification as well as the role and authorization concept SHOULD be considered. At least MUST consider the following topics:

* management areas to be separated,
* Access to the management server,
* Communication for management access,
* used protocols, eg. Eg IPv4 and IPv6,
* Requirements for management tools,
* Interfaces to forward detected event or alarm messages
* Logging, including necessary interfaces to a central logging solution,
* Reporting and interfaces to comprehensive solutions,
* corresponding requirements for the network components to be integrated.
#### NET.1.2.A2 Requirements Specification for Network Management [IT Leader]

Based on NET.1.2A1 * Network Management Planning * Requirements for network management infrastructure and processes MUST be specified. All essential elements for network management MUST be considered. Also, the policy for network management SHOULD be respected.

#### NET.1.2.A3 Role and authorization concept for network management

A role and authorization concept for network management MUST be created, implemented and maintained. The concept MUST map the specific activities and associated access to information in network management.

#### NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]

For management access to network components and management information, appropriate authentication MUST be used. For this, the specifications of the institution for the authentication quality and the handling of the authentication information MUST be implemented. Also, all default passwords on the network components MUST be changed. The new passwords MUST be strong enough and regularly changed.

#### NET.1.2.A5 Importing Updates and Patches
The responsible employees MUST regularly inform themselves about known vulnerabilities in the network management solutions used and import security-related updates and patches as quickly as possible. Non-security updates MAY NOT compromise the security and stability of the network management solution.

#### NET.1.2.A6 Regular backup

All network management solutions MUST be integrated into the institution's data protection concept (see CON.3 * data backup concept *). All specific data for network management MUST be considered. At least the system data for the integration of the components or objects to be managed, event messages, statistical data as well as data retained for the configuration management MUST be saved.

#### NET.1.2.A7 Basic logging of events

The network management solution MUST be integrated into the institution's logging concept (see OPS.1.1.5 * Logging *). In addition, at least the following events MUST be logged: unauthorized access attempts, power or availability fluctuations of the network, errors in automatic processes (eg during configuration distribution) as well as limited accessibility of network components.

#### NET.1.2.A8 time synchronization

All network management components, including the integrated network components, MUST use a synchronous time. The time MUST be synchronized at each location within the local network using NTP service. If a separate management network is set up, an NTP instance MUST be positioned in this management network.

#### NET.1.2.A9 Securing network management communication

If network management communication is via the productive infrastructure, then secure protocols MUST be used in accordance with the state of the art. If this is not possible, a dedicated administration network (out-of-band management) MUST be used (see NET.1.1 * network architecture and design *)

#### NET.1.2.A10 Limitation of SNMP communication

Network management MUST NOT use unsafe versions of the Simple Network Management Protocol (SNMP). However, if this is not possible, the SNMP communication MUST be either through a separate management network or MUST use SNMPv3 with authentication and encryption. Basically, SNMP should only be used with the minimum required access rights. The access authorization SHOULD be restricted to dedicated management servers.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of network management. They SHOULD be implemented in principle.

#### NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]

For network management, a security policy SHOULD be created and maintained sustainably. The policy SHOULD be known to all people involved in network management and fundamental to their work. It SHOULD be checked regularly and comprehensibly that the contents required by the directive are implemented. The results MUST be documented in a meaningful way.

The security policy SHOULD define which areas of network management are implemented through centralized management tools and services. It SHOULD also define to what extent tasks should be automated in the network management of the institution.

In addition, framework conditions and requirements for network separation, access control, logging and communication protection, the network management tool used and the operational rules for network management SHOULD be specified.

#### NET.1.2.A12 Actual recording and documentation of network management
A documentation describing how the management infrastructure of the network is constructed SHOULD be made. This should include the initial actual recording and all changes made to the network management. In particular, it should be documented which network components are managed with which management tools. In addition, all IT workstations and terminals used for network management, as well as all information inventories, management data and network management operation information, should be recorded. Ultimately, all interfaces to applications and services outside the network management SHOULD be documented.

The documented as-is state of the management infrastructure SHOULD be compared with the documentation of the network infrastructure (see building block NET.1.1 * Network Architecture and Design). *

The documentation SHOULD be complete and always up-to-date.

#### NET.1.2.A13 Creation of a network management concept [Head IT]

Based on the security policy (see NET.1.2.A11 * Defining a security policy for network management *), a network management concept SHOULD be created and sustainably maintained. At least the following aspects should be taken into account as needed:

* Methods, techniques and tools for network management,
* Security of access and communication,
* Network separation, in particular allocation of network management components to security zones,
* Scope of monitoring and alerting per network component,
* Logging,
* Automation, especially central distribution of configuration files on switches,
* Message chains in case of faults and security incidents,
* Provide network management information for other operating areas and
* Integration of network management in emergency planning.
#### NET.1.2.A14 fine- and implementation planning

It SHOULD create a detailed and implementation planning for the network management infrastructure. All points addressed in the security policy and in the network management concept SHOULD be considered.

#### NET.1.2.A15 Concept for the secure operation of the network management infrastructure

Based on the security guidelines and the network management concept, a concept for the secure operation of the network management infrastructure SHOULD be created. In it the application and system operation for the network management tools SHOULD be considered. It should also be examined how the services of other operational units can be integrated and controlled.

#### NET.1.2.A16 Setup and configuration of network management solutions

Network Management Solutions SHOULD be built on the Security Policy (see NET.1.2.A11 * Defining a Security Policy for Network Management *), the Specified Requirements (see NET1.2.A2 * Network Management Requirements Specification *), and the Detailed and Implementation Planning; safely configured and put into operation. After that, the specific processes for network management SHOULD be set up.

#### NET.1.2.A17 Regular target / actual comparison

It should be checked regularly and comprehensibly to what extent the network management solution meets the target state. It should be checked whether the existing solution still meets the security policy and requirements specification. It should also be examined to what extent the implemented management structure and the processes used are up-to-date. Next SHOULD be compared, whether the management infrastructure is state-of-the-art.

#### NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
Training and training measures SHOULD be designed and implemented for the network management solutions used. The measures SHOULD cover the individual circumstances in the configuration, availability and capacity management as well as typical situations in error management. Training and training SHOULD be repeated on a regular basis, but at least if major technical or organizational changes occur within the network management solution.

#### NET.1.2.A19 Strong authentication of management access

For administrative access to network components, a state of the art authentication method SHOULD be used. The administrative approaches SHOULD be authenticated via a central authentication server using personalized accounts using correspondingly secure protocols.

#### NET.1.2.A20 Securing Access to Network Management Solutions

The access to central network management solutions and management information SHOULD be protected by a state of the art authentication method. The receipts SHOULD be authenticated via a central authentication server using personalized accounts.

The prior art authentication and encryption methods MUST be implemented if network management tools are accessed from a network outside the management networks, particularly from a productive network or an insufficiently secure network.

#### NET.1.2.A21 Decoupling of network management communication

Direct management access by an administrator from an IT system outside the management networks to a network component SHOULD be avoided. If such access is required without a central management tool, the communication SHOULD be decoupled. Such jump servers SHOULD be integrated into the management network and positioned in a separate access segment.

#### NET.1.2.A22 Limitation of management functions

Only the required management functions SHOULD be activated.

#### NET.1.2.A23 Logging of administrative access

As part of network management, the session data of all administrative accesses SHOULD be logged and stored. In doing so, the data protection regulations SHOULD be respected.

The logging data SHOULD be sufficiently protected in the data protection according to the law. In addition, it should be determined whether and to what extent session data for forensic analysis should be archived. When archiving data, care should be taken to ensure that it complies with the law and is auditable.

#### NET.1.2.A24 Central configuration management for network components

Software or firmware and configuration data for network components SHOULD be automatically distributed over the network and installed and activated without interruption. The information required for this purpose SHOULD be securely available at a central location and incorporated into the version management and data backup. The central configuration management SHOULD be sustainably maintained and regularly audited.

#### NET.1.2.A25 Status monitoring of the network components

The basic performance and availability parameters of the central network components SHOULD be continuously monitored. For this, the respective threshold values ​​SHOULD be determined beforehand (baselining).

#### NET.1.2.A26 Comprehensive logging, alarming and logging of events

Important events or error conditions SHOULD be automatically transmitted to a central management system and logged there. This applies to events on network components as well as events on the network management tools. The responsible IT staff SHOULD additionally be notified automatically. The alarming and logging SHOULD include at least the following points:
* Failure or unavailability of network or management components
* Hardware malfunction
* incorrect login attempts
* Critical states or congestion of IT systems
Event messages or logging data SHOULD be transmitted continuously or cumulatively to a central management system. Alarm messages SHOULD be transmitted directly when they occur.

#### NET.1.2.A27 Integration of network management in emergency planning

The network management solutions SHOULD be integrated into the emergency planning of the institution. For this, the network management tools and the configurations of the network components SHOULD be saved and integrated into the recovery plans.

#### NET.1.2.A28 Placement of management clients for in-band management

Dedicated management clients SHOULD be used to administer both internal and external IT systems. For this purpose, at least one management client should be placed on the external network area (for the administration of the IT systems connected to the Internet) and another in the internal area (for the administration of internal IT systems).

#### NET.1.2.A29 Use of VLANs in the Management Zone

If management networks are separated by VLANs, care should be taken that the external packet filter and the devices connected to it are in their own subnetwork. In addition, it should be ensured that the ALG is not bypassed.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### NET.1.2.A30 Highly available realization of the management solution (A)

Central management solutions SHOULD be operated at high availability. For this purpose, the servers or tools including the network connections SHOULD be configured redundantly. Also, the individual components SHOULD be provided highly available.

#### NET.1.2.A31 Basic Use of Secure Protocols (CIA)

For network management only secure protocols SHOULD be used. All security features of these protocols SHOULD be used.

#### NET.1.2.A32 Physical separation of the management network (CIA)

The management network SHOULD be physically separated.

#### NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)

The management network SHOULD be divided into physically separate security zones. At a minimum, physically separated security zones should be set up to manage LAN components, security components, and outdoor connectivity components.

#### NET.1.2.A34 Logging Content of Administrative Sessions (CI)

In addition to the logging of session data (see NET.1.2.A22 * Logging of Administrative Accesses *), the contents of administrative accesses SHOULD also be logged. Alternatively, proceed according to the four-eyes principle. The logged contents of the administrative sessions SHOULD be sufficiently protected in the data protection according to the law.

#### NET.1.2.A35 Preservation Requirements (CIA)

It was intended to establish and document procedures for the preservation of evidence and forensic investigations within the framework of network management. The collected logging data SHOULD be archived for forensic analyzes in compliance with the law and auditable.

#### NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
The logging of network management SHOULD be integrated into a security information and event management (SIEM) solution. For this, the requirement catalogs (see NET.1.2.A2) for the selection of network management solutions should be adapted with regard to the required support of interfaces and transfer formats.

#### NET.1.2.A37 Cross-Site Time Synchronization (CI)

The time synchronization SHOULD be ensured across all locations of the institution. For this a common reference time SHOULD be used, eg. B. via a parent NTP server.

#### NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)

In order to quickly restore the software or firmware setpoints and to configure the components in the network management infrastructure, it is important to establish adequate backup solutions that can be used to perform the administrative tasks in an emergency.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and security measures in the area of ​​"network management" can be found in the following publications, among others:

* #### [ISI] BSI Internet Security Standards (Isi Series)

  

 BSI, (last accessed on 28.09.2017)
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-Reihe\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ ISi series / ISi Reihe_node.html)

 
* #### [TR21022] BSI Technical Guideline, Cryptographic Procedures

  

 Use of Transport Layer Security (TLS), Federal Office for Information Security (BSI), 2017
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "Network Management".

* G 0.9 Failure or malfunction of communication networks
* G 0.11 Failure or disruption of service providers
* G 0.14 Spying out information (spying)
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.27 Resource shortage
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.43 Importing messages
The cross reference tables can be found in the download area due to their size.
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.11 Failure or disruption of service providers
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.14 Spying out information (spying)
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.19 Disclosure of information worthy of protection
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.22 Manipulation of information
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
* G 0.25 Failure of devices or systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A8 time synchronization
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.27 Resource shortage
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A32 Physical separation of the management network (CIA)
* G 0.29 Violation of laws or regulations
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.39 Malware
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
* G 0.40 Denial of Service
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A7 Basic logging of events
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
* G 0.43 Importing messages
  * NET.1.2.A1 Planning the network management
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A12 Actual recording and documentation of network management
  * NET.1.2.A13 Creation of a network management concept [Head IT]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A15 Concept for the secure operation of the network management infrastructure
  * NET.1.2.A16 Setup and configuration of network management solutions
  * NET.1.2.A17 Regular target / actual comparison
  * NET.1.2.A18 Training for Management Solutions [Head of IT, Supervisors]
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A2 Requirements Specification for Network Management [IT Leader]
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A22 Limitation of management functions
  * NET.1.2.A23 Logging of administrative access
  * NET.1.2.A24 Central configuration management for network components
  * NET.1.2.A25 Status monitoring of the network components
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A27 Integration of network management in emergency planning
  * NET.1.2.A28 Placement of management clients for in-band management
  * NET.1.2.A29 Use of VLANs in the Management Zone
  * NET.1.2.A3 Role and authorization concept for network management
  * NET.1.2.A30 Highly available realization of the management solution (A)
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
  * NET.1.2.A37 Cross-Site Time Synchronization (CI)
  * NET.1.2.A38 Definition of emergency forms of operation for the network management infrastructure (A)
  * NET.1.2.A4 Basic Authentication for Network Management Access [IT Leader, Information Security Officer (ISB)]
  * NET.1.2.A5 Importing Updates and Patches
  * NET.1.2.A6 Regular backup
  * NET.1.2.A9 Securing network management communication
  * NET.1.2.A10 Limitation of SNMP communication
  * NET.1.2.A11 Definition of a Security Policy for Network Management [Information Security Officer (ISB)]
  * NET.1.2.A14 fine- and implementation planning
  * NET.1.2.A19 Strong authentication of management access
  * NET.1.2.A20 Securing Access to Network Management Solutions
  * NET.1.2.A21 Decoupling of network management communication
  * NET.1.2.A26 Comprehensive logging, alarming and logging of events
  * NET.1.2.A31 Basic Use of Secure Protocols (CIA)
  * NET.1.2.A32 Physical separation of the management network (CIA)
  * NET.1.2.A33 Physical separation of management segments [Network Manager] (CIA)
  * NET.1.2.A34 Logging Content of Administrative Sessions (CI)
  * NET.1.2.A35 Preservation Requirements (CIA)
  * NET.1.2.A36 Integration of network management logging into a SIEM solution (CIA)
