1 description
--------------

### 1.1 Introduction

A firewall is a system of software and hardware components that is used to securely couple IP-based data networks. For this purpose, the technically possible is restricted to the communication defined as secure in a security policy by means of a firewall structure. Security here means that only the desired accesses or data streams between different networks are allowed.

In order to secure gateways, it is often not just a single component that is used, but a whole range of IT systems that perform different tasks, such as: For example, you can only filter packets or strictly disconnect network connections using proxy functions. The term Application Level Gateway (ALG) used in this module refers to a firewall component that regulates data streams based on security proxies.

A firewall is used at the central junction between trusted networks. Differently trusted networks do not necessarily represent only the combination of Internet / Intranet. Rather, two institution-internal networks can also have different levels of protection requirements, eg. For example, the network of office communication usually has a different need for protection than the network of the personnel department, in which particularly sensitive personal data is transmitted.

### 1.2 Objective

The goal of the module is to be able to use a firewall or a firewall structure securely in order to securely connect networks with different protection requirements.

### 1.3 Delimitation

The building block builds on the building block NET.1.1 * Network Architecture and Design * and contains concrete requirements that must be observed and fulfilled when network-based firewalls are procured, constructed, configured and operated.

In order to secure networks, more network components are usually required, eg. For example, routers and switches. Requirements for this are not listed in this module, but can be found in NET.3.1 * Routers and Switches *. If a firewall takes on the role of a router or switch, it also has to meet the requirements of the NET.3.1 * Router and Switches * block.

In addition, it does not cover products such as Next Generation Firewalls (NGFW) or Unified Threat Management firewalls, which also contain functional enhancements, such as: VPN, Intrusion Detection and Intrusion Prevention (IDS / IPS) systems, virus scanners or spam filters. Safety aspects of these functional extensions are not the subject of the present module, but z. This is, for example, covered in the blocks NET.3.3 * VPN *, NET.3.4 * IDS / IPS *, OPS1.1.4 * Protection against malicious programs *.

Likewise, no application recognition or filtering is discussed. It is a common feature of Next Generation Firewalls and IDS / IPS. Since the implementations differ between the products, it is recommended that they be viewed individually depending on the application scenario. In this module is also not discussed on the individual protection options for externally offered server services, z. For example, through a reverse proxy or for web services using a Web Application Firewall (WAF). In addition, aspects of infrastructural safety (eg suitable installation or power supply) are not listed in this module, but can be found in the respective building blocks of the INF layer.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the firewall area:

### 2 1 Distributed Denial of Service (DDoS)
In a DDoS attack on a protected network (eg TCP-SYN-Flooding, UDP Packet Storm) the firewall may fail due to the many network connections that need to be processed. This can result in certain services in the Local Area Network (LAN) becoming unavailable or the entire LAN failing.

### 2 2 Manipulation

If an attacker succeeds in gaining unauthorized access to a firewall system or a corresponding administration interface, he can arbitrarily manipulate files there. For example, he can change the configuration, start additional services or install malicious software. Likewise, he can record the communication connections on the manipulated system. For example, the firewall rules can be changed to access the firewall and intranet of the institution from the Internet. Furthermore, an attacker can initiate a denial of service (DoS) attack by blocking access to individual server services in the policy.

### 2 3 Software vulnerabilities or errors

Firewalls are complex systems and are subject to numerous attacks, especially at the transition from the intranet to the Internet. Therefore, firewall manufacturers regularly release updates and patches to address software bugs and known vulnerabilities in their products. However, if these are not recorded or played too late, the firewall system can be successfully attacked. This makes it possible for attackers to manipulate the systems to drain business-critical data, disrupt services or shut down entire production processes.

### 2 4 Bypassing the firewall rules

 Attackers can bypass firewall rules (for example, by fragmentation attacks) by using basic mechanisms in network protocols to penetrate a firewall-protected area. In the protected area, they can then cause further damage (eg read out, manipulate or delete sensitive data).

### 2 5 Incorrect configuration and operating error of a firewall

An improperly configured or incorrectly operated firewall can seriously affect the availability of services. If, for example, firewall rules are set incorrectly, network access can be blocked. Furthermore, faulty configurations can lead to IT systems being no longer completely protected or even no longer protected. In the worst case, internal services for attackers can be reached.

3 requirements
---------------

The following are specific firewall requirements. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### NET.3.2.A1 Creating a Security Policy [Information Security Officer (ISB)]

On the basis of the institution's general security policy, a specific security policy MUST be drawn up in which comprehensible requirements and specifications are described on how firewalls can be operated safely. The policy MUST be known and fundamental to all employees responsible for firewalls. If the policy is changed or deviated from the requirements, this MUST be agreed and documented with the ISB. It MUST be checked on a regular basis to see if the directive is still correctly implemented. The results MUST be documented in a meaningful way.
#### NET.3.2.A2 Setting firewall rules

All communications between the participating networks MUST be routed through the firewall. It MUST be ensured that no unauthorized connections to the protected network can be established from outside. Likewise, NO unauthorized connections MUST be built out of the protected network.

The firewall MUST have unique rules defining which communication links and data streams are allowed. All other connections MUST be blocked by the firewall (whitelist approach). The communication relationships with connected service servers (eg e-mail servers, web servers) that are routed through the firewall MUST be considered in the rules.

NO IT systems MUST access the internal network from the outside via the firewall (see specifications from the NET.1.1 module * Network architecture and design) *. Any exceptions to this requirement are governed by the appropriate application and system-specific building blocks.

It is MUST designate responsible persons who design, implement and test the filter rules. In addition MUST be clarified, who may change filter rules. The decisions taken as well as the relevant information and reasons for the decision MUST be documented.

#### NET.3.2.A3 Set up appropriate filter rules on the packet filter

Based on the firewall rules from NET.3.2.A2 * Setting the firewall rules * MUST be defined and set up appropriate filter rules for the packet filter.

A packet filter MUST be set to discard all invalid TCP flag combinations. Basically MUST always conditional filtered. Stateful filter rules should also be configured for the connectionless protocols UDP and ICMP. The firewall MUST filter the ICMP and ICMPv6 protocols restrictively.

#### NET.3.2.A4 Secure configuration of the firewall

Before a firewall is used, it MUST be configured securely.

A firewall may ONLY be installed and configured ONLY by authorized persons, eg. B. Persons responsible for their own IT operations or contracted service providers.

All configuration changes MUST be traceable documented (see NET.3.2.A14 * operating documentation *). The integrity of the configuration files SHOULD be properly protected. Access passwords MUST be stored encrypted.

A firewall MUST be configured so that only mandatory services are available. If functional enhancements are used, the institution's security policies MUST continue to be met. It also MUST be justified and documented why such extensions are used. Unnecessary (information) services and unneeded functional enhancements MUST be disabled or completely uninstalled.

Information about the internal configuration and operating state MUST be hidden to the outside as best as possible.

#### NET.3.2.A5 Restrictive rights assignment

It must be regulated, who may access the firewall, z. To configure or monitor them. In this case, ONLY as many access rights must be granted as are necessary for the respective tasks (need-to-know principle). Unauthorized user accounts MUST be removed. It MUST be ensured that administrator rights (or root rights) are only used when necessary.

#### NET.3.2.A6 Protection of the administration interfaces

All administration and management accesses of the firewall MUST be restricted to individual source IP addresses or address ranges. It MUST be ensured that the administration interfaces can not be accessed from untrusted networks.
In order to administer or monitor the firewall, only secure protocols must be used or a dedicated administration network (out-of-band management) MUST be used (see specifications from the module NET.1.1 * Network architecture and -). design and NET.1.2 network management). * Suitable time limits MUST be specified for the user interfaces.

#### NET.3.2.A7 Emergency access to the firewall

It must always be possible to access the firewall directly so that you can continue to work locally, even if the entire network fails.

#### NET.3.2.A8 Prevention of dynamic routing

In the settings of the firewall, the dynamic routing MUST be deactivated, unless the packet filter is used as a perimeter router according to the building block NET.3.1 * Router and Switches *.

#### NET.3.2.A9 logging

The firewall MUST be configured to log at least the following events:

* denied network connections (source and destination IP addresses, source and destination ports or ICMP / ICMPv6 type, date, time),
* Failed access to system resources due to incorrect authentication, lack of authority or lack of resources,
* Error messages of the firewall services and
* general system error messages.
If security proxies are used, security violations and access control list violations (ACLs or short access lists) MUST be appropriately logged: at least the type of protocol violation or violation, source and destination IP address, source and destination IP addresses Destination port, service, date and time, and connection duration (if required).

If a user authenticates to the security proxy, authentication data or only information about a failed authentication MUST also be logged.

The persons responsible MUST take care that the logging complies with all legal framework conditions.

#### NET.3.2.A10 Defense against fragmentation attacks on the packet filter

Protective mechanisms MUST be enabled on the packet filter to fend off both IPv4 and IPv6 fragmentation attacks.

#### NET.3.2.A11 Importing Updates and Patches

Those responsible MUST inform themselves about known vulnerabilities. Updates and patches MUST be loaded as soon as possible. First, it should be checked on a test system, whether the security updates are compatible and do not cause any errors. Unless patches are available for known vulnerabilities, other appropriate measures MUST be taken to protect the firewall.

It MUST be taken care that patches and updates are obtained only from trustworthy sources. This MUST be respected in related services within the firewall system.

#### NET.3.2.A12 Procedure for security incidents

It MUST be determined how to respond to a detected attack. The tasks and competencies for the employees involved MUST be clearly defined. For more information see DER.2.1 * Incident Management *.

#### NET.3.2.A13 Regular backup

Firewall system backups MUST be created periodically. Even before a firewall is reinstalled or otherwise configured, the system MUST be secured. If backed-up databases are restored, the security-relevant files such as access lists, password files and filter rules MUST be located on the security-required configuration status.

#### NET.3.2.A14 Operation documentation
The operational tasks of a firewall MUST be comprehensibly documented. All configuration changes and security-related tasks MUST be documented, in particular changes to the system services and the rules of the firewall. The documentation MUST be protected against unauthorized access. Changes to the configuration MUST also be logged as automatically as possible.

#### NET.3.2.A15 Obtaining a firewall

Before a firewall is procured, a list of requirements MUST be created to evaluate the products available on the market. It MUST be ensured that the security level sought by the institution is achievable with the firewall. The basis for procurement MUST therefore be the requirements of the safety guideline.

If IPv6 is used, the packet filter MUST check the IPv6 extension headers. In addition, IPv6 MUST be able to be configured adequately to IPv4.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​firewalls. They SHOULD be implemented in principle.

#### NET.3.2.A16 Structure of a "P-A-P" structure

The structure of a "Packet Filter - Application Level Gateway Packet Filter" (P-A-P) structure SHOULD consist of several components each with dedicated hardware and software. For the most important protocols used, security proxies SHOULD be present at application layer and for other services at least generic security proxies for TCP and UDP. The security proxies SHOULD also run within a secure runtime environment of the operating system.

#### NET.3.2.A17 Disabling IPv4 or IPv6

If the IPv4 or IPv6 protocol is not needed in a network segment, it SHOULD be disabled at the respective firewall network access point (eg at the corresponding firewall interface). If the IPv4 or IPv6 protocol is not needed or used at all, it SHOULD be completely disabled on the firewall.

#### NET.3.2.A18 Administration via a separate management network

Firewalls SHOULD only be administered via a separate management network (out-of-band management). Any existing administration interface via the actual data network (in-band) MUST be deactivated. Communication in the management network SHOULD be limited to a few management protocols with well-defined origins and goals via management firewalls (see NET.1.1 * network architecture and design *). The available security mechanisms of the used management protocols for authentication, integrity assurance and encryption SHOULD be activated and all insecure management protocols deactivated (see NET.1.2 * Network Management *).

#### NET.3.2.A19 Protection against TCP SYN Flooding, UDP Packet Storm and Sequence Number Guessing on Packet Filter

The packet filter, which protects server services reachable from untrusted networks, SHOULD set a limit for half open and open connections.

At the packet filter, which protects server services reachable from less or untrusted networks, the so-called rate limits for UDP data streams SHOULD be set.

At the outer packet filter, a random generation of initial sequence numbers (ISN) SHOULD be activated for outgoing connections for TCP, if this is not already implemented by security proxies.

#### NET.3.2.A20 Securing basic internet protocols

To communicate to the Internet, the HTTP, SMTP, and DNS protocols, including their encrypted versions, SHOULD be routed through protocol-specific security proxies.

#### NET.3.2.A21 Temporary decryption of traffic
Encrypted connections to untrusted networks SHOULD be decrypted temporarily to verify the protocol and check the data for malicious software. Here, the legal framework MUST be observed.

The component that decrypts traffic temporarily SHOULD prevent outdated encryption options (such as SSL) and cryptographic algorithms (such as DES, MD5, SHA1) from being used.

Also, the TLS proxy SHOULD use to verify that certificates are trusted. If a certificate is untrusted, SHOULD it be possible to reject the connection. Own certificates SHOULD be retrofittable in order to configure and check "internal" root certificates. Preconfigured certificates SHOULD be checked and removed if they are not needed.

#### NET.3.2.A22 Secure time synchronization

There SHOULD be a secure time synchronization with a Network Time Protocol (NTP) server. The firewall SHOULD NOT allow external time synchronization. Further requirements can be found in the module NET.1.2 * Network Management *.

#### NET.3.2.A23 System Monitoring and Evaluation

Firewalls SHOULD be integrated into a suitable system monitoring or monitoring concept. Furthermore, a process SHOULD be defined that regulates how log data should be evaluated and which logs should be evaluated regularly, sporadically or only on an ad hoc basis. It SHOULD constantly be monitored to see if the firewall itself and the services running on it are working properly. In case of errors or if limit values ​​are exceeded, the operating personnel SHOULD be alerted. In addition, ALARMS SHOULD automatically be generated, which are triggered by defined events. Protocol data or status messages SHOULD only be transmitted via secure communication channels.

#### NET.3.2.A24 Revision and Penetration Tests

The firewall structure SHOULD regularly be checked for known security issues. There should be regular penetration tests and revisions.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### NET.3.2.A25 Extended integrity protection for configuration files (CI)

If a system crashes, SHOULD ensure that no old or faulty configurations (including access lists) are used. This should also apply if an attacker succeeds in restarting the firewall.

#### NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)

To further minimize the potential for attack, an organization SHOULD outsource its firewall functionality to dedicated hardware and software.

#### NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)

In a multi-tier firewall architecture, different operating systems and products for the outer and inner firewalls SHOULD be used to reduce the potential for a vulnerability in an operating system or product.

#### NET.3.2.A28 Central filtering of active content (CI)

Active content SHOULD be centrally filtered according to the security objectives of the institution. The encrypted traffic SHOULD also be decrypted. The required security proxies SHOULD support filtering active content.

#### NET.3.2.A29 Use of High Availability Solutions (A)
Packet filters and Application Level Gateway SHOULD be designed to be highly available. In addition, two independent access to the external network SHOULD exist, eg. B. two Internet access from different providers. Internal and external routers, as well as any other active components involved (eg, switches) that may cause loss of availability, SHOULD also be designed to be highly available.

Even after an automatic failover, the firewall structure SHOULD meet the security requirements of the security policy (fail-safe or fail-secure).

Function monitoring SHOULD be done on the basis of numerous parameters and not rely on a single criterion. Log files and alerts for the high availability solution SHOULD be regularly audited.

#### NET.3.2.A30 Bandwidth Management for Critical Applications and Services (A)

To ensure bandwidth management for critical applications and services, packet filters with appropriate bandwidth management capability should be deployed at gateways and at the transition between different security zones.

#### NET.3.2.A31 Use of Certified Products (CI)

Firewalls should be deployed with a Common Criteria security evaluation, at least EAL4 level.

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the "Firewall" area can be found in the following publications, among others:

* #### [BSICS112] Next Generation Firewalls - Cyber ​​Security Publications

  

 Recommendation of possible uses for the normal protection requirement, BSI, 04.2015
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/infos/20150407\_BSI\_Empfehlung\_NGFW.htm](https://www.allianz-fuer-cybersicherheit.de/ACS /DE/_/infos/20150407_BSI_Empfehlung_NGFW.htm)

 
* #### [ISILANA] BSI Internet Security Standard (Isi Series):

  

 Secure connection of local networks to the Internet (Isi-LANA), Federal Office for Information Security (BSI), 2014
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/ standard criteria / ISi series / ISi-LANA / lana_node.html)

 
* #### [NIST80041] NIST Special Publication 800-41

  

 Guidelines on Firewalls and Firewall Policy, 09.2009
 <Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r3.pdf>

 
* #### [TR21022] BSI Technical Guideline, Cryptographic Procedures

  

 Use of Transport Layer Security (TLS), Federal Office for Information Security (BSI), 2017
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Firewall" block.

* G 0.8 Failure or malfunction of the power supply
* G 0.9 Failure or malfunction of communication networks
* G 0.14 Spying out information (spying)
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
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.41 Sabotage
* G 0.43 Importing messages
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A29 Use of High Availability Solutions (A)
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A7 Emergency access to the firewall
  * NET.3.2.A18 Administration via a separate management network
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A29 Use of High Availability Solutions (A)
  * NET.3.2.A30 Bandwidth Management for Critical Applications and Services (A)
* G 0.14 Spying out information (spying)
  * NET.3.2.A2 Setting firewall rules
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A21 Temporary decryption of traffic
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
  * NET.3.2.A28 Central filtering of active content (CI)
  * NET.3.2.A29 Use of High Availability Solutions (A)
  * NET.3.2.A3 Set up appropriate filter rules on the packet filter
  * NET.3.2.A30 Bandwidth Management for Critical Applications and Services (A)
  * NET.3.2.A31 Use of Certified Products (CI)
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A16 Structure of a "P-A-P" structure
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
* G 0.18 Missing planning or missing adjustment
  * NET.3.2.A1 Creating a Security Policy [Information Security Officer (ISB)]
  * NET.3.2.A10 Defense against fragmentation attacks on the packet filter
  * NET.3.2.A11 Importing Updates and Patches
  * NET.3.2.A12 Procedure for security incidents
  * NET.3.2.A13 Regular backup
  * NET.3.2.A14 Operation documentation
  * NET.3.2.A15 Obtaining a firewall
  * NET.3.2.A16 Structure of a "P-A-P" structure
  * NET.3.2.A17 Disabling IPv4 or IPv6
  * NET.3.2.A18 Administration via a separate management network
  * NET.3.2.A19 Protection against TCP SYN Flooding, UDP Packet Storm and Sequence Number Guessing on Packet Filter
  * NET.3.2.A12 Procedure for security incidents
  * NET.3.2.A14 Operation documentation
  * NET.3.2.A15 Obtaining a firewall
  * NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)
* G 0.19 Disclosure of information worthy of protection
  * NET.3.2.A2 Setting firewall rules
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A21 Temporary decryption of traffic
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
  * NET.3.2.A28 Central filtering of active content (CI)
  * NET.3.2.A29 Use of High Availability Solutions (A)
  * NET.3.2.A3 Set up appropriate filter rules on the packet filter
  * NET.3.2.A30 Bandwidth Management for Critical Applications and Services (A)
  * NET.3.2.A31 Use of Certified Products (CI)
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A10 Defense against fragmentation attacks on the packet filter
  * NET.3.2.A16 Structure of a "P-A-P" structure
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
* G 0.20 Information or products from unreliable sources
  * NET.3.2.A11 Importing Updates and Patches
  * NET.3.2.A14 Operation documentation
  * NET.3.2.A15 Obtaining a firewall
  * NET.3.2.A31 Use of Certified Products (CI)
* G 0.21 Manipulation of hardware or software
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A9 logging
  * NET.3.2.A11 Importing Updates and Patches
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
* G 0.22 Manipulation of information
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A5 Restrictive rights assignment
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A8 Prevention of dynamic routing
  * NET.3.2.A9 logging
  * NET.3.2.A16 Structure of a "P-A-P" structure
  * NET.3.2.A21 Temporary decryption of traffic
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * NET.3.2.A2 Setting firewall rules
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A21 Temporary decryption of traffic
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
  * NET.3.2.A28 Central filtering of active content (CI)
  * NET.3.2.A29 Use of High Availability Solutions (A)
  * NET.3.2.A3 Set up appropriate filter rules on the packet filter
  * NET.3.2.A30 Bandwidth Management for Critical Applications and Services (A)
  * NET.3.2.A31 Use of Certified Products (CI)
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A16 Structure of a "P-A-P" structure
  * NET.3.2.A17 Disabling IPv4 or IPv6
  * NET.3.2.A18 Administration via a separate management network
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
* G 0.24 Destruction of equipment or data media
  * NET.3.2.A11 Importing Updates and Patches
* G 0.25 Failure of devices or systems
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A7 Emergency access to the firewall
  * NET.3.2.A8 Prevention of dynamic routing
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)
  * NET.3.2.A29 Use of High Availability Solutions (A)
* G 0.26 Malfunction of equipment or systems
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A5 Restrictive rights assignment
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
* G 0.27 Resource shortage
  * NET.3.2.A1 Creating a Security Policy [Information Security Officer (ISB)]
  * NET.3.2.A10 Defense against fragmentation attacks on the packet filter
  * NET.3.2.A11 Importing Updates and Patches
  * NET.3.2.A12 Procedure for security incidents
  * NET.3.2.A13 Regular backup
  * NET.3.2.A14 Operation documentation
  * NET.3.2.A15 Obtaining a firewall
  * NET.3.2.A16 Structure of a "P-A-P" structure
  * NET.3.2.A17 Disabling IPv4 or IPv6
  * NET.3.2.A18 Administration via a separate management network
  * NET.3.2.A19 Protection against TCP SYN Flooding, UDP Packet Storm and Sequence Number Guessing on Packet Filter
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)
* G 0.28 Software vulnerabilities or errors
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A11 Importing Updates and Patches
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
* G 0.29 Violation of laws or regulations
  * NET.3.2.A9 logging
  * NET.3.2.A22 Secure time synchronization
* G 0.30 Unauthorized use or administration of devices and systems
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A9 logging
  * NET.3.2.A18 Administration via a separate management network
  * NET.3.2.A22 Secure time synchronization
* G 0.31 Incorrect use or administration of devices and systems
  * NET.3.2.A9 logging
  * NET.3.2.A22 Secure time synchronization
* G 0.32 Abuse of permissions
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A9 logging
  * NET.3.2.A22 Secure time synchronization
* G 0.39 Malware
  * NET.3.2.A2 Setting firewall rules
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A21 Temporary decryption of traffic
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
  * NET.3.2.A28 Central filtering of active content (CI)
  * NET.3.2.A29 Use of High Availability Solutions (A)
  * NET.3.2.A3 Set up appropriate filter rules on the packet filter
  * NET.3.2.A30 Bandwidth Management for Critical Applications and Services (A)
  * NET.3.2.A31 Use of Certified Products (CI)
  * NET.3.2.A16 Structure of a "P-A-P" structure
* G 0.40 Denial of Service
  * NET.3.2.A2 Setting firewall rules
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A21 Temporary decryption of traffic
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
  * NET.3.2.A28 Central filtering of active content (CI)
  * NET.3.2.A29 Use of High Availability Solutions (A)
  * NET.3.2.A3 Set up appropriate filter rules on the packet filter
  * NET.3.2.A30 Bandwidth Management for Critical Applications and Services (A)
  * NET.3.2.A31 Use of Certified Products (CI)
  * NET.3.2.A16 Structure of a "P-A-P" structure
  * NET.3.2.A19 Protection against TCP SYN Flooding, UDP Packet Storm and Sequence Number Guessing on Packet Filter
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A30 Bandwidth Management for Critical Applications and Services (A)
* G 0.41 Sabotage
  * NET.3.2.A2 Setting firewall rules
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A21 Temporary decryption of traffic
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
  * NET.3.2.A28 Central filtering of active content (CI)
  * NET.3.2.A29 Use of High Availability Solutions (A)
  * NET.3.2.A3 Set up appropriate filter rules on the packet filter
  * NET.3.2.A30 Bandwidth Management for Critical Applications and Services (A)
  * NET.3.2.A31 Use of Certified Products (CI)
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A5 Restrictive rights assignment
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A8 Prevention of dynamic routing
  * NET.3.2.A9 logging
  * NET.3.2.A10 Defense against fragmentation attacks on the packet filter
  * NET.3.2.A11 Importing Updates and Patches
  * NET.3.2.A12 Procedure for security incidents
  * NET.3.2.A19 Protection against TCP SYN Flooding, UDP Packet Storm and Sequence Number Guessing on Packet Filter
  * NET.3.2.A21 Temporary decryption of traffic
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A28 Central filtering of active content (CI)
* G 0.43 Importing messages
  * NET.3.2.A2 Setting firewall rules
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A21 Temporary decryption of traffic
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
  * NET.3.2.A28 Central filtering of active content (CI)
  * NET.3.2.A29 Use of High Availability Solutions (A)
  * NET.3.2.A3 Set up appropriate filter rules on the packet filter
  * NET.3.2.A30 Bandwidth Management for Critical Applications and Services (A)
  * NET.3.2.A31 Use of Certified Products (CI)
  * NET.3.2.A8 Prevention of dynamic routing
  * NET.3.2.A9 logging
  * NET.3.2.A10 Defense against fragmentation attacks on the packet filter
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A21 Temporary decryption of traffic
  * NET.3.2.A22 Secure time synchronization
* G 0.45 data loss
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A9 logging
  * NET.3.2.A13 Regular backup
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
* G 0.46 Loss of integrity of sensitive information
  * NET.3.2.A2 Setting firewall rules
  * NET.3.2.A20 Securing basic internet protocols
  * NET.3.2.A21 Temporary decryption of traffic
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A23 System Monitoring and Evaluation
  * NET.3.2.A24 Revision and Penetration Tests
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A26 Outsourcing of functional extensions to dedicated hardware (CIA)
  * NET.3.2.A27 Use of different firewall operating systems and products in a multi-level firewall architecture (CI)
  * NET.3.2.A28 Central filtering of active content (CI)
  * NET.3.2.A29 Use of High Availability Solutions (A)
  * NET.3.2.A3 Set up appropriate filter rules on the packet filter
  * NET.3.2.A30 Bandwidth Management for Critical Applications and Services (A)
  * NET.3.2.A31 Use of Certified Products (CI)
  * NET.3.2.A4 Secure configuration of the firewall
  * NET.3.2.A5 Restrictive rights assignment
  * NET.3.2.A6 Protection of the administration interfaces
  * NET.3.2.A9 logging
  * NET.3.2.A22 Secure time synchronization
  * NET.3.2.A25 Extended integrity protection for configuration files (CI)
  * NET.3.2.A28 Central filtering of active content (CI)
