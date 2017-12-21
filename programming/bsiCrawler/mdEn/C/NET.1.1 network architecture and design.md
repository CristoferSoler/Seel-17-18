1 description
--------------

### 1.1 Introduction

Most institutions today require computer networks for their business operations. B. information and data exchanged and distributed applications can be realized. Not only are traditional networks, partner institutions and the Internet integrated into such networks, but they are increasingly integrating mobile devices and elements that are assigned to the Internet of Things (IoT). In addition, cloud networks and services for Unified Communication and Collaboration (UCC) are increasingly being used over computer networks. The benefits of doing so are undeniable. But the many terminals and services are also increasing the risks. That's why it's important to protect your own network with a secure network architecture. To do this, for example, it is necessary to plan how a local area network (LAN) or a wide area network (WAN) can be set up safely. Similarly, only limited trusted external networks, eg. As the Internet or customer networks are properly connected.

In order to ensure a high level of security, additional safety-relevant aspects must be taken into consideration. For example, different clients and device groups are securely separated at the network level and their communication is controlled by firewall techniques. Another important security element especially in the client area is the network access control (see NET.1.3 * Network Access Control *).

### 1.2 Objective

The aim of this module is to establish information security as an integral part of the network architecture and the network design.

### 1.3 Delimitation

The module contains basic requirements that must be observed and fulfilled when networks are planned, constructed and operated. Requirements for the safe operation of the corresponding network components, including safety components such. As Firewalls and Intrusion Detection Systems / Intrusion Prevention Systems (IDS / IPS), are not the subject of this module. These are handled in the block group NET.3 * Network Components *.

The focus of this module is on wired networks and data communication. However, general architectural and design requirements, e.g. For example, separate security zones and segments for all network technologies. Further specific requirements for network areas such as wireless LAN (WLAN) or storage area networks (SAN) are dealt with in the block groups NET.2 * wireless networks * or in the block SYS.1.8 * storage systems *. In addition, the topics UCC and Voice over IP (VoIP) as well as the underlying security infrastructure are not discussed in this module, but are treated in the respective modules NET.4.2 * VoIP * and NET.4.5 * Unified Communications *.

Specific security requirements for Virtual Private Clouds and Hybrid Clouds are not the focus of this module (see OPS.3.2 * Cloud Providers * and OPS.3.4 * Managed Security Services *).

The network management is considered in the context of zoning and segmentation, all further topics of network management are dealt with in the module NET.1.2 * Network Management *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​*** *** network architecture and design:

### 2 1 Failure or inadequate performance of communication links
If the communication links are insufficiently sized or if their performance is no longer sufficient due to technical failures or due to a denial-of-service (DoS) attack, eg B. Clients communicate only limited with servers. As a result, the access times to internal and external services (eg cloud services) increase, which are sometimes only limited or even unusable. Also, any business-related information is no longer available. As a result, production downtime can occur, for example, or essential business processes fail.

### 2 2 Insufficiently secured network access

Is the internal network connected to the Internet and the transition not sufficiently protected, z. For example, because no firewall is used or it is misconfigured, attackers can access and copy or manipulate the institution's sensitive information.

### 2 3 Improper construction of networks

If a network is improperly constructed or improperly extended, unsafe network topologies and network configurations can arise. This makes it easier for attackers to find security holes, penetrate the institution's internal network and extract information, manipulate data or disrupt entire production systems. Also, attackers in a faulty network, which the security systems can only monitor to a limited extent, remain unrecognized for longer.

3 requirements
---------------

The following are specific requirements for network architecture and design. Basically, the head of networks is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]

Based on the institution's general security policy, a specific security policy for the network MUST be established, which comprehensibly describes requirements and requirements for how networks are designed and constructed securely. The directive MUST include:

* in which cases the security zones are to be segmented and in which cases user groups or clients are to be logically or even physically separated,
* which communication relationships and which network and application protocols are allowed,
* how the data traffic for administration and monitoring is to be separated by the network,
* which internal, inter-site communication (WAN, wireless networks) is allowed and which encryption is required in WAN, LAN or on radio links,
* which inter-institutional communication is allowed.
The policy MUST be known to all network design professionals and be fundamental to their work. If the policy is changed or deviated from the requirements, this MUST be documented and agreed with the responsible ISB. It MUST be checked on a regular basis to see if the directive is still correctly implemented. The results MUST be documented in a meaningful way.

#### NET.1.1.A2 Documentation of the network [IT operation]

It MUST be a complete documentation of the network (including network) created and maintained sustainably. This MUST include the initial initial recording (including network performance) and any changes made to the network. Also, the logical structure of the network MUST be documented, in particular how the subnets are mapped and how the network is zoned and segmented.

#### NET.1.1.A3 requirements specification for the network
Based on the security policy (see NET.1.1.A1 * Network Security Policy *), a requirements specification for the network MUST be created and sustainably maintained. The requirements MUST be used to derive all the essential elements for network architecture and design.

#### NET.1.1.A4 Network separation in security zones

The overall network MUST be physically separated into at least the following three security zones: internal network, demilitarized zone (DMZ) and external connections (including Internet connectivity and connection to other untrusted networks). Zone transitions MUST be protected by a firewall. This control MUST follow the principle of local communication, so that firewalls forward exclusively allowed communication (whitelisting).

Untrusted networks (eg Internet) and trusted networks (eg Intranet) MUST be separated by a two-tier firewall structure consisting of stateful packet filters (firewalls). To separate Internet and external DMZ network technically, at least one stateful packet filter (firewall) MUST be used.

In the two-stage firewall architecture, every incoming and outgoing data traffic MUST be controlled and filtered by the external packet filter (firewall) or the internal packet filter (firewall).

A P-A-P structure consisting of packet filters, application layer gateways or security proxies and packet filters MUST always be implemented if required by the security policy or requirement specification.

#### NET.1.1.A5 client-server segmentation

Clients and servers MUST be placed in different security segments. The communication between these segments MUST be controlled at least by a stateful packet filter (firewall).

It should be noted that any exceptions that allow clients and servers to be placed in a common security segment are governed by the appropriate application and system-specific building blocks.

For guest access and for network areas where there is insufficient internal control over the terminals, dedicated security segments MUST be set up.

#### NET.1.1.A6 Terminal Segmentation in the Internal Network

Only terminals in a security segment that meet a similar level of security may be positioned.

#### NET.1.1.A7 Protection of sensitive information

Protective information MUST be transmitted over state-of-the-art secure protocols if it is not communicated over trusted dedicated network segments (eg, within the management network). If such protocols can not be used, they MUST be adequately encrypted and authenticated according to the state of the art (see NET.3.3 * VPN). *

#### NET.1.1.A8 Basic protection of Internet access

Internet access MUST be designed according to NET.1.1.A4 * Network separation in security zones *. Internet traffic MUST be routed through the firewall structure. The data flows MUST be restricted by the firewall structure to the required protocols and communication relationships.

#### NET.1.1.A9 Basic security of communication with untrusted networks

For each network it MUST be determined to what extent it is trustworthy. Networks that are not trusted at all MUST be treated as the Internet and secured accordingly.

#### NET.1.1.A10 DMZ segmentation for traffic from the Internet
The firewall structure MUST be supplemented by a so-called external DMZ for all services or applications that can be reached from the Internet. A DMZ segmentation concept SHOULD be created that comprehensibly implements the security policy and the requirements specification. Depending on the security level of the IT systems, the DMZ segments MUST be subdivided further. An external DMZ MUST be connected to the outer packet filter.

#### NET.1.1.A11 Securing incoming communication from the Internet to the internal network

IP-based access to the internal network MUST be via a secure communication channel and restricted to trusted IT systems and users (see NET.3.3 * VPN *). Such VPN gateways SHOULD be realized in an external DMZ. It should be noted that sufficiently hardened VPN gateways can be directly accessible from the Internet. The network accesses to the internal network authenticated via the VPN gateway MUST pass through at least the internal firewall (to protect the internal network).

IT systems MUST NOT access the internal network via the Internet or external DMZ. It SHOULD be noted that any exceptions to this requirement are governed by the appropriate application and system-specific building blocks (eg APP.5.1 * E-mail / Groupware *, NET.4.2 * VoIP) *.

#### NET.1.1.A12 Securing outgoing internal communication to the Internet

Outgoing communication from the internal network to the Internet MUST be decoupled at a security proxy. The decoupling MUST take place outside the internal network. If a P-A-P structure is used, the outgoing communication should always be decoupled by the security proxies of the P-A-P structure.

#### NET.1.1.A13 network planning

Each network implementation MUST be designed to be fully and comprehensibly planned. The security policy as well as the requirement specification MUST be observed. In addition, at least the following points MUST be considered in the planning as needed:

* Internet connection and, if available, location network and extranet,
* Topology of the whole network and network areas, d. H. Security zones and segments,
* Dimensioning and redundancy of network and safety components, transmission links and external connections,
* protocols to be used and their basic configuration and addressing, in particular IPv4 / IPv6 subnets of terminal groups,
* Administration and Monitoring (see NET.1.2 * Network Management *).
The network planning MUST be checked regularly.

#### NET.1.1.A14 Implementation of network planning

The planned network MUST be implemented professionally. This MUST be checked during acceptance.

#### NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]

It MUST be checked regularly whether the existing network corresponds to the target state. It must at least be checked to what extent it meets the security guideline and requirements specification and to what extent the implemented network structure corresponds to the current state of network planning. For this, competent persons and test criteria or specifications MUST be defined.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of network architecture and design. They SHOULD be implemented in principle.

#### NET.1.1.A16 Network Architecture Specification

On the basis of the security guideline and the requirement specification, an architecture for the security zones including internal network, DMZ area and external connections SHOULD be developed and sustainably maintained. Depending on the specific situation of the institution, all relevant architectural elements SHOULD be considered, but at least:
* Network architecture of the internal network with definitions of how to use network virtualization techniques, Layer 2 and Layer 3 communication, and redundancy techniques,
* Network architecture for external connections, including firewall architectures, as well as DMZ and extranet design and site coupling requirements,
* Determine at which points of the network which security components such as firewalls or IDS / IPS are to be placed and what security functions they must implement,
* Specifications for the network connection of the various IT systems,
* Network architecture in virtualization hosts, taking into account Network Virtualization Overlay (NVO) and Vertical Integrated Systems (ViS) architecture,
* Definitions of the basic architecture elements for a private cloud as well as securing the connections to Virtual Private Cloud, Hybrid Cloud and Public Cloud (see OPS.3.2 * Cloud Providers * and OPS.3.4 * Managed Security Services *),
* Architecture for secure administration and monitoring of the IT infrastructure.
#### NET.1.1.A17 Specification of the network design

Based on the network architecture, the network design for the security zones including the internal network, DMZ area and external connections SHOULD be developed and sustainably maintained. The relevant architecture elements SHOULD be detailed, but at least:

* permissible forms of network components including virtualized network components,
* Specifications on how to secure WAN and radio links
* Connection of terminals to switching components, connections between network elements and use of communication protocols,
* Redundancy mechanisms for all network elements,
* Address concept for IPv4 and IPv6 as well as associated routing and switching concepts,
* virtualized networks in virtualization hosts including NVO,
* Setting up, connecting and securing private clouds as well as secure connection of virtual private clouds, hybrid clouds and public clouds,
* Network design specifications for secure administration and monitoring of the IT infrastructure.
#### NET.1.1.A18 P-A-P structure for the Internet connection

Between the two firewall levels (see NET.1.1.A4 * Network separation in security zones *), a proxy-based application layer gateway (ALG) MUST be implemented or appropriate security proxies MUST be implemented. These MUST be connected via a dual-homed transfer network to the outer firewall and the internal firewall. In these transfer networks, only the proxy-based ALG or ONLY appropriate security proxies MUST be integrated. All data traffic MUST be decoupled via the ALG or corresponding security proxies. A transport network that connects both firewall levels directly together MUST NOT be configured. The internal firewall MUST also reduce the attack surface of the ALG or the security proxies against intruders or IT systems in the internal network.

Authenticated and trusted network accesses from the VPN gateway to the internal network SHOULD NOT pass through the ALG or security proxies of the P-A-P structure.

#### NET.1.1.A19 Separation of infrastructure services

Servers that provide basic services to the IT infrastructure SHOULD be positioned in a dedicated security segment. Communication with them SHOULD be controlled by a stateful packet filter (firewall).

#### NET.1.1.A20 Assignment of Dedicated Subnets for IPv4 / IPv6 Terminal Groups

Different IPv4 / IPv6 terminals SHOULD be assigned to dedicated subnets depending on the protocol used (IPv4 / IPv6 or IPv4 / IPv6 DualStack).

#### NET.1.1.A21 Separation of the management area
It should be used throughout an out-of-band management to manage the infrastructure. All devices that are needed for the management of the IT infrastructure SHOULD be positioned in dedicated segments. Communication with these terminals SHOULD be controlled by a stateful packet filter (firewall). Communication from and to these management segments SHOULD be limited to the necessary management protocols with defined communication endpoints.

The management area SHOULD include at least the following security segments, which SHOULD be further sub-divided depending on the security policy and the requirements specification:

Segment (s) for IT systems responsible for the authentication and authorization of administrative communications,
* Segment (s) for the administration of IT systems,
* Segment (s) for monitoring and monitoring,
* Segment (s) containing central logging including syslog server and SIEM server
* Segment (s) for IT systems needed for basic management services
* Segment (s) for the management interface of the IT systems to be administered.
The various management interfaces of the IT systems MUST be separated according to their purpose and their network placement via a stateful packet filter (firewall). The IT systems (management interface) in addition to the following affiliation SHOULD be separated via dedicated firewalls:

* IT systems that are accessible from the Internet,
* IT systems in the internal network,
* Security components that are located between the IT systems accessible from the Internet and the internal network.
It MUST be ensured that the segmentation can not be undermined by the management communication, i. H. a bridging of segments MUST be excluded.

#### NET.1.1.A22 Specification of the segmentation concept

Based on the specifications of network architecture and network design, a comprehensive segmentation concept for the internal network, including possibly existing virtualized networks in virtualization hosts, should be planned, implemented, operated and sustainably maintained. The concept SHOULD include at least the following items, as far as they are intended in the target environment:

* Safety segments to be created initially and specifications on how to create new safety segments and how to position terminals in the safety segments.
* Definition for the segmentation of development and test systems (staging)
* Network access control for security segments with clients
* Connection of network areas that are connected to the safety segments via wireless technology or leased line
* Connecting the virtualization hosts and virtual machines on the hosts to the security segments
* Data center automation
* Determination of how to integrate terminals that serve multiple security segments, eg. Load balancers, and storage and backup solutions
Depending on the security policy and the requirement specification, SHOULD be designed for each security segment, as it should be implemented in terms of network technology. In addition, it should be determined which security functions the coupling elements must provide between the security segments (eg firewall as a stateful packet filter or IDS / IPS).

#### NET.1.1.A23 Separation of security segments

IT systems with different protection requirements SHOULD be placed in different security segments. If this is not possible, the protection requirement is based on the highest protection requirement occurring in the security segment. In addition, the security segments SHOULD be further subdivided depending on their size and the requirements of the segmentation concept. It MUST be ensured that bridging of segments or even zones is not possible.
If the VLANs on a switch belong to different institutions, the separation should be either physical or encryption SHOULD be used to protect the transmitted information from unauthorized access.

#### NET.1.1.A24 Secure logical separation via VLAN

A Virtual LAN (VLAN) MAY NOT establish a connection between a zone in front of the ALG or the security proxies of a P-A-P structure and the underlying internal network.

In general, it MUST be ensured that bridging zones is not possible when using VLANs.

#### NET.1.1.A25 Fine and implementation planning of network architecture and design

A detailed and implementation planning for the network architecture and the network design SHOULD be carried out, documented, checked and sustainably maintained.

#### NET.1.1.A26 Specification of operating processes for the network

For a safe and effective network operation SHOULD business processes be generated or adapted and documented as required (see the block group Core IT Operations, in particular OPS.1.1.3 * Patch and Change Management *). In particular, it should be considered how the zoning as well as the segmentation concept affect IT operations.

#### NET.1.1.A27 Integration of network architecture into contingency planning [Head IT]

Initially and at regular intervals, it should be comprehensibly analyzed how the network architecture and the derived concepts affect emergency planning.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### NET.1.1.A28 Fault-tolerant network and security components (A)

Central areas of the internal network as well as the security components SHOULD be realized with high availability. For this purpose, the components SHOULD be designed redundantly and implemented internally highly available.

#### NET.1.1.A29 Highly available realization of network connections (A)

The network connections (eg Internet connection and WAN connections) SHOULD be completely redundant. Depending on the availability requirement, redundant connections to one or several providers should be implemented as needed, with different technology and performance. Also, distance redundancy within and outside of one's own responsibility should be implemented as needed. Here, possible single points of failure (SPoF) and disturbing environmental conditions should be considered.

#### NET.1.1.A30 Distributed Denial-of-Service Protection (A)

To ward off DDoS attacks, Bandwidth Management SHOULD allocate available bandwidth between different communication partners and protocols.

In order to fend off DDoS attacks with very high data rates, mitigation services SHOULD be purchased through larger Internet Service Providers (ISPs) and their use SHOULD be regulated in contracts.

#### NET.1.1.A31 Physical separation of security segments (CIA)

Depending on security policy and requirement specification, security segments SHOULD be separated physically by separate switches.

#### NET.1.1.A32 Physical separation of management segments (CIA)

Depending on security policy and requirement specification, security segments of the management area SHOULD be physically separated.

#### NET.1.1.A33 Network microsegmentation (CIA)
To limit potential attacks on a small number of terminals, the network SHOULD be divided into small segments with a very similar requirement profile and protection needs. In particular, this should be taken into account for the DMZ segments.

#### NET.1.1.A34 Use of cryptographic procedures at network level (CI)

The security segments SHOULD be implemented on the internal network, on the extranet and in the DMZ area using cryptographic techniques already at the network level. For this, VPN techniques or IEEE 802.1AE should be used.

When communicating within the internal network, extranet or DMZ over links that are not sufficiently secure for increased protection needs, the communication SHOULD be adequately encrypted at the network level.

#### NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)

At the network level, data loss prevention (DLP) systems should be used to reduce the risk of data leakage.

#### NET.1.1.A36 Separation via VLAN with very high protection requirement

With very high protection requirements, NO VLANs SHOULD BE used.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and security measures in the area of ​​"network architecture and design" can be found in the following publications, among others:

* #### [27033-5] ISO / IEC 27033-5: 2013

  

 Information technology - Security techniques - Network Security - Part 5: Securing communications across networks using Virtual Private Networks (VPNs), ISO, 08.2013
 <Https://www.iso.org/standard/51584.html>

 
* #### [ISILANA] BSI Internet Security Standard (Isi Series):

  

 Secure connection of local networks to the Internet (Isi-LANA), Federal Office for Information Security (BSI), 2014
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/ standard criteria / ISi series / ISi-LANA / lana_node.html)

 
* #### [TL2103] BSI TL-02103 - Version 2.0 "Technical Guideline for Organizational Telecommunication Systems with Increased Protection Needs"

  

 Federal Office for Security in Information Technology, 2014
 [https://www.bsi.bund.de/DE/Publikationen/TL-sichere-TK-Anlagen/TL02103\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TL- secure PBXs / TL02103_htm.html)

 
* #### [TR21022] BSI Technical Guideline, Cryptographic Procedures

  

 Use of Transport Layer Security (TLS), Federal Office for Information Security (BSI), 2017
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the building block "network architecture and design".

* G 0.9 Failure or malfunction of communication networks
* G 0.11 Failure or disruption of service providers
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.27 Resource shortage
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.43 Importing messages
The cross reference tables can be found in the download area due to their size.
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A3 requirements specification for the network
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
  * NET.1.1.A4 Network separation in security zones
  * NET.1.1.A5 client-server segmentation
  * NET.1.1.A6 Terminal Segmentation in the Internal Network
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A20 Assignment of Dedicated Subnets for IPv4 / IPv6 Terminal Groups
  * NET.1.1.A21 Separation of the management area
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A24 Secure logical separation via VLAN
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A26 Specification of operating processes for the network
  * NET.1.1.A27 Integration of network architecture into contingency planning [Head IT]
  * NET.1.1.A28 Fault-tolerant network and security components (A)
  * NET.1.1.A29 Highly available realization of network connections (A)
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
* G 0.11 Failure or disruption of service providers
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A3 requirements specification for the network
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A27 Integration of network architecture into contingency planning [Head IT]
  * NET.1.1.A28 Fault-tolerant network and security components (A)
  * NET.1.1.A29 Highly available realization of network connections (A)
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
* G 0.18 Missing planning or missing adjustment
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A2 Documentation of the network [IT operation]
  * NET.1.1.A20 Assignment of Dedicated Subnets for IPv4 / IPv6 Terminal Groups
  * NET.1.1.A21 Separation of the management area
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A24 Secure logical separation via VLAN
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A26 Specification of operating processes for the network
  * NET.1.1.A27 Integration of network architecture into contingency planning [Head IT]
  * NET.1.1.A28 Fault-tolerant network and security components (A)
  * NET.1.1.A29 Highly available realization of network connections (A)
  * NET.1.1.A3 requirements specification for the network
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
  * NET.1.1.A4 Network separation in security zones
  * NET.1.1.A8 Basic protection of Internet access
  * NET.1.1.A9 Basic security of communication with untrusted networks
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A20 Assignment of Dedicated Subnets for IPv4 / IPv6 Terminal Groups
  * NET.1.1.A21 Separation of the management area
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A24 Secure logical separation via VLAN
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A26 Specification of operating processes for the network
  * NET.1.1.A27 Integration of network architecture into contingency planning [Head IT]
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
* G 0.19 Disclosure of information worthy of protection
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A3 requirements specification for the network
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
  * NET.1.1.A4 Network separation in security zones
  * NET.1.1.A5 client-server segmentation
  * NET.1.1.A6 Terminal Segmentation in the Internal Network
  * NET.1.1.A7 Protection of sensitive information
  * NET.1.1.A8 Basic protection of Internet access
  * NET.1.1.A9 Basic security of communication with untrusted networks
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A24 Secure logical separation via VLAN
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
* G 0.22 Manipulation of information
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A3 requirements specification for the network
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
  * NET.1.1.A5 client-server segmentation
  * NET.1.1.A6 Terminal Segmentation in the Internal Network
  * NET.1.1.A7 Protection of sensitive information
  * NET.1.1.A8 Basic protection of Internet access
  * NET.1.1.A9 Basic security of communication with untrusted networks
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A21 Separation of the management area
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A24 Secure logical separation via VLAN
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
* G 0.23 Unauthorized intrusion into IT systems
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A3 requirements specification for the network
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
  * NET.1.1.A4 Network separation in security zones
  * NET.1.1.A5 client-server segmentation
  * NET.1.1.A6 Terminal Segmentation in the Internal Network
  * NET.1.1.A7 Protection of sensitive information
  * NET.1.1.A8 Basic protection of Internet access
  * NET.1.1.A9 Basic security of communication with untrusted networks
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A21 Separation of the management area
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A24 Secure logical separation via VLAN
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
* G 0.27 Resource shortage
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A2 Documentation of the network [IT operation]
  * NET.1.1.A20 Assignment of Dedicated Subnets for IPv4 / IPv6 Terminal Groups
  * NET.1.1.A21 Separation of the management area
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A24 Secure logical separation via VLAN
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A26 Specification of operating processes for the network
  * NET.1.1.A27 Integration of network architecture into contingency planning [Head IT]
  * NET.1.1.A28 Fault-tolerant network and security components (A)
  * NET.1.1.A29 Highly available realization of network connections (A)
  * NET.1.1.A3 requirements specification for the network
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A20 Assignment of Dedicated Subnets for IPv4 / IPv6 Terminal Groups
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A28 Fault-tolerant network and security components (A)
  * NET.1.1.A29 Highly available realization of network connections (A)
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
* G 0.29 Violation of laws or regulations
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A2 Documentation of the network [IT operation]
  * NET.1.1.A20 Assignment of Dedicated Subnets for IPv4 / IPv6 Terminal Groups
  * NET.1.1.A21 Separation of the management area
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A24 Secure logical separation via VLAN
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A26 Specification of operating processes for the network
  * NET.1.1.A27 Integration of network architecture into contingency planning [Head IT]
  * NET.1.1.A28 Fault-tolerant network and security components (A)
  * NET.1.1.A29 Highly available realization of network connections (A)
  * NET.1.1.A4 Network separation in security zones
  * NET.1.1.A5 client-server segmentation
  * NET.1.1.A6 Terminal Segmentation in the Internal Network
  * NET.1.1.A7 Protection of sensitive information
  * NET.1.1.A8 Basic protection of Internet access
  * NET.1.1.A9 Basic security of communication with untrusted networks
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A27 Integration of network architecture into contingency planning [Head IT]
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A3 requirements specification for the network
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
  * NET.1.1.A4 Network separation in security zones
  * NET.1.1.A5 client-server segmentation
  * NET.1.1.A6 Terminal Segmentation in the Internal Network
  * NET.1.1.A8 Basic protection of Internet access
  * NET.1.1.A9 Basic security of communication with untrusted networks
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A21 Separation of the management area
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A24 Secure logical separation via VLAN
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A26 Specification of operating processes for the network
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
* G 0.39 Malware
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A3 requirements specification for the network
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
  * NET.1.1.A4 Network separation in security zones
  * NET.1.1.A5 client-server segmentation
  * NET.1.1.A6 Terminal Segmentation in the Internal Network
  * NET.1.1.A8 Basic protection of Internet access
  * NET.1.1.A9 Basic security of communication with untrusted networks
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A21 Separation of the management area
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A27 Integration of network architecture into contingency planning [Head IT]
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
* G 0.40 Denial of Service
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A3 requirements specification for the network
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
  * NET.1.1.A4 Network separation in security zones
  * NET.1.1.A5 client-server segmentation
  * NET.1.1.A8 Basic protection of Internet access
  * NET.1.1.A9 Basic security of communication with untrusted networks
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A27 Integration of network architecture into contingency planning [Head IT]
  * NET.1.1.A28 Fault-tolerant network and security components (A)
  * NET.1.1.A29 Highly available realization of network connections (A)
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
* G 0.43 Importing messages
  * NET.1.1.A1 Network Security Policy [IT Director, Information Security Officer (ISB)]
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A12 Securing outgoing internal communication to the Internet
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A15 Regular Target / Act Comparison [Information Security Officer (ISB)]
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A3 requirements specification for the network
  * NET.1.1.A30 Distributed Denial-of-Service Protection (A)
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A32 Physical separation of management segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A35 Use of Net-based DLP [Information Security Officer (ISB)] (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
  * NET.1.1.A4 Network separation in security zones
  * NET.1.1.A5 client-server segmentation
  * NET.1.1.A6 Terminal Segmentation in the Internal Network
  * NET.1.1.A7 Protection of sensitive information
  * NET.1.1.A8 Basic protection of Internet access
  * NET.1.1.A9 Basic security of communication with untrusted networks
  * NET.1.1.A10 DMZ segmentation for traffic from the Internet
  * NET.1.1.A11 Securing incoming communication from the Internet to the internal network
  * NET.1.1.A13 network planning
  * NET.1.1.A14 Implementation of network planning
  * NET.1.1.A16 Network Architecture Specification
  * NET.1.1.A17 Specification of the network design
  * NET.1.1.A18 P-A-P structure for the Internet connection
  * NET.1.1.A19 Separation of infrastructure services
  * NET.1.1.A21 Separation of the management area
  * NET.1.1.A22 Specification of the segmentation concept
  * NET.1.1.A23 Separation of security segments
  * NET.1.1.A24 Secure logical separation via VLAN
  * NET.1.1.A25 Fine and implementation planning of network architecture and design
  * NET.1.1.A31 Physical separation of security segments (CIA)
  * NET.1.1.A33 Network microsegmentation (CIA)
  * NET.1.1.A34 Use of cryptographic procedures at network level (CI)
  * NET.1.1.A36 Separation via VLAN with very high protection requirement
