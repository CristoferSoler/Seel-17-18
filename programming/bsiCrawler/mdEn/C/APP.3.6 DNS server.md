1 description
--------------

### 1.1 Introduction

This module considers the basic security features of the Domain Name System (DNS) and the servers required for this purpose. DNS is a network service that is used to transform host names of IT systems into IP addresses. Normally, a hostname is searched for the corresponding IP address (forward resolution). If, however, the IP address is known and the host name is searched, this is called backward resolution. DNS can be compared to a phonebook that resolves names not into phone numbers but into IP addresses. Which names belong to which IP addresses is managed in the domain namespace. This is hierarchical and is provided by DNS servers. DNS servers manage the domain name space on the Internet, but they are also often used in the institution's internal network. By default, so-called resolvers are installed on users' computers, which are used to make requests to DNS servers and return information about the domain namespace in response. The term DNS server literally stands for the software used, but is usually also used as a synonym for the computer on which this software is operated.

DNS servers can be distinguished according to their tasks, there are basically two different types: Advertising DNS server and Resolving DNS server. Advertising DNS servers are usually responsible for processing requests from the Internet. Resolving DNS servers, on the other hand, process requests from the internal network.

A failure of a DNS server can seriously affect the operation of an IT infrastructure. It is not directly the failed DNS system problematic, but the resulting restriction of DNS-based services. Under certain circumstances, web servers, e-mail servers are no longer available and the remote maintenance does not work anymore. As DNS is required by many networking applications, the specification (RFC 1034) requires at least two Authoritative DNS servers to operate on each zone.

### 1.2 Objective

This module describes the specific threats for a DNS server and the resulting requirements for safe operation.

### 1.3 Delimitation

This module contains basic requirements that must be observed and fulfilled when an institution operates DNS servers. The focus here is on the availability of DNS servers, the integrity of the information transmitted, and the problems that can arise when operating DNS servers. However, general and operating system-specific aspects of a server are not the subject of this module, but are described in the SYS1.1. * General server * and handled in the appropriate OS-specific building blocks of the IT systems layer, eg. SYS.1.3 * Unix server * or SYS.1.2.2 * Windows Server 2012 *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to DNS servers:

### 2 1 DNS server failure

If a DNS server fails, the entire IT operation can be affected. Since clients and other servers of the institution are then no longer able to resolve internal and external addresses, data connections can no longer be established. Also external IT systems, eg. Mobile workers, customers, and business partners, for example, can not access the institution's servers, which typically disruptes critical business processes.

### 2 2 Insufficient line capacity
If the line capacities for a DNS server are insufficient, access times to internal and external services may increase. As a result, these may only be limited or no longer usable. Also, attackers can more easily overload the DNS server with a denial-of-service (DoS) attack.

### 2 3 Lack of or inadequate planning of DNS use

Planning errors often turn out to be particularly serious, since it is easy to create comprehensive security gaps. If the use of DNS is not or only insufficiently planned, this can lead to problems and security gaps during operation. For example, if the firewall rules are too liberally defined to allow DNS traffic on the network, it may allow an attack. However, if the rules are too restrictive, legitimate clients will not be able to make requests to the DNS servers and will be affected if they use services such as e-mail, FTP, or the like.

### 2 4 Bad domain information

Even if the DNS deployment has been carefully planned and thus all safety-relevant points have been considered, this is not sufficient if semantically and / or syntactically incorrect domain information is created. For example, if a hostname is assigned an incorrect IP address, data is missing, or unauthorized characters are used, or the forward and reverse resolutions are inconsistent. If domain information contains errors, services that use this information will be restricted due to misinformation.

### 2 5 Incorrect configuration of a DNS server

Security-critical defaults, self-configured security-critical settings, or bad configurations can cause a DNS server to malfunction. For example, if a Resolving DNS server is configured to accept recursive requests unrestricted, both from the internal LAN and the Internet, the server's availability may be severely affected by the increased load. In addition, it could make it vulnerable to DNS reflection attacks.

Similarly, in the case of incorrectly configured DNS servers, there is a risk that the zone transfers will not be restricted to authorized DNS servers. This allows any host who has the opportunity to submit a request to the DNS servers to read out the entire domain information of these servers. The data thus obtained can facilitate later attacks.

### 2 6 DNS manipulation

With a DNS cache poisoning attack, the target is tracked that the compromised machine stores incorrect mappings of IP addresses and names. It exploits the fact that DNS servers cached received domain information for a certain period of time in the cache. Fake data can spread that far. If corresponding queries are made to the manipulated DNS server, it will provide the counterfeit data as an answer. The recipient of the response stores this between and his cache is thus also "poisoned". The stored data has a defined shelf life (Time-To-Live, TTL). If the resolving DNS server is asked for a manipulated address, it will not ask another DNS server until its expiration date. So it is possible that manipulated DNS information last long, even though they are already corrected on the originally attacked DNS server. If, for example, an attacker succeeds in taking over the name resolution for a domain by manipulating the entries in such a way that his DNS servers are interrogated, all subdomains are automatically affected. DNS cache poisoning attacks are often conducted with the goal of redirecting requests to malicious servers.

### 2 7 DNS hijacking
DNS hijacking is an attacking technique used to direct communication between Advertising DNS servers and resolvers through an attacker's IT system. The attacker can use this man-in-the-middle attack to intercept and record communication between servers. The far greater danger, however, is that a successful attacker can arbitrarily change any traffic between the two communication partners. For example, if a request is sent to a DNS server by the resolver of a client IT system after a successful DNS hijacking attack, the attacker can change the name and IP address mapping. DNS hijacking can also be combined with other attacks, especially phishing in this case.

### 2 8 DNS-DoS

In a DoS attack on a DNS server, so many requests are sent to it that the network connection to the DNS server or the DNS server itself is overloaded. As a rule, the requests are sent via botnets in order to achieve the necessary data rate. A DNS server overloaded in this way can no longer answer legitimate requests.

### 2 9 DNS Reflection

A DNS Reflection attack is a DoS attack that does not target the DNS server to which the requests are made, but the recipient of the replies. It is exploited that certain requests generate a relatively large amount of response data. It is possible to achieve a gain of 100 or more. This means that the response, measured in bytes, is at least 100 times larger than the request. Due to the number and size of the answers, the network bandwidth or the computer itself is overloaded beyond the power capacity. Thus, any technical IT component can be the target (see 2.8 * DNS-DoS *). DNS reflection attacks are favored by open resolvers.

3 requirements
---------------

The following are specific requirements for DNS servers. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### APP.3.6.A1 Planning the DNS deployment

Because well-functioning name resolution is a prerequisite for many applications and thus for smooth operation, DNS servers MUST be carefully planned. It must first be determined how the network service DNS should be established and which domain information is worth protecting. It also MUST be planned how DNS servers should be integrated into the network of the information network. The decisions made MUST be documented.

#### APP.3.6.A2 Use of redundant DNS servers

Advertising DNS servers (external requests) MUST be designed redundantly. Therefore, there must be at least one additional Secondary DNS server for each Advertising DNS server.

#### APP.3.6.A3 Use of separate DNS servers for internal and external requests

Advertising DNS servers (external requests) and resolving DNS servers (internal requests) MUST be separate on the server side. Resolvers of internal IT systems MUST use internal Resolving DNS servers to resolve names.

#### APP.3.6.A4 Secure basic configuration of a DNS server
A Resolving DNS server MUST be configured to accept requests from the internal network only. When sending requests, it MUST use random source ports. If DNS servers that provide incorrect domain information are known, the Resolving DNS server MUST be prevented from sending requests to it. An Advertising DNS server MUST be configured to iteratively handle requests from the Internet.

It MUST be ensured that DNS zone transfers between Primary and Secondary DNS servers work. In addition, zone transfers MUST be configured to only be possible between Primary and Secondary DNS servers. To secure zone transfers, they MUST be limited to specific IP addresses. The version of the used DNS server product MUST be hidden.

#### APP.3.6.A5 Timely import of security-relevant patches and updates

The responsible employees MUST inform themselves regularly at various sources about newly discovered vulnerabilities in the used DNS server product and import security-relevant updates in a timely manner. However, in advance, a test system MUST check to see if the security updates are compatible and do not cause errors. Unless patches are available for known vulnerabilities, other appropriate measures MUST be taken to protect the DNS servers. Before a patch is imported, the zone and configuration files MUST be backed up.

#### APP.3.6.A6 Secure Dynamic DNS Updates

In order to be able to use dynamic updates securely, only legitimate IT systems MAY change domain information. It also MUST be determined which domain information the IT systems may change.

#### APP.3.6.A7 Monitoring of DNS servers

In order to operate DNS servers smoothly and to detect possible malfunctions or anomalies, they MUST be constantly monitored. It also MUST be monitored how busy the DNS servers are to be able to adjust the power capacity of the hardware in time. In addition, all security-related events at DNS servers MUST be properly logged.

#### APP.3.6.A8 Domain Name Management [IT Leader]

It MUST be ensured that registrations for all domains used by an institution are renewed on a regular and timely basis. It MUST be determined by an employee who is responsible for managing the Internet domain names. If an Internet service provider is commissioned with the domain administration, MUST be taken to ensure that the institution retains control of the domains.

#### APP.3.6.A9 Create an emergency plan for DNS servers

An emergency plan for DNS servers MUST be created. It MUST be integrated into the institution's existing emergency plans. It also MUST describe a data protection concept for the zone and configuration files, which MUST be integrated into the existing data protection concept of the institution. The contingency plan MUST also include a recovery plan for DNS servers.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of DNS servers. They SHOULD be implemented in principle.

#### APP.3.6.A10 Selection of a suitable DNS server product

If a DNS server product is procured, care should be taken to ensure that all security requirements of the institution are properly implemented. The product SHOULD have proven its worth in practice and support the current RFC standards. It SHOULD help those responsible to create syntactically correct master files. In addition, there should be enough trained personnel for the selected DNS server product.

#### APP.3.6.A11 Sufficient size of DNS servers
Since the hardware of a DNS server affects the performance of the entire system, it SHOULD be sufficiently sized. Also, the hardware SHOULD only be used to operate a DNS server. Likewise, the network connection of the DNS server SHOULD be sufficiently dimensioned.

#### APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]

It SHOULD be ensured through training that the persons in charge are familiar with the individual configuration options and security-relevant aspects of the DNS server.

#### APP.3.6.A13 Limiting the visibility of domain information

The namespace of an information network SHOULD be divided into a public and an institution-internal area. The public part SHOULD only contain domain information that is required by services that should be accessible externally. IT systems in the internal network SHOULD NOT receive an externally resolvable DNS name even if they have a public IP address.

#### APP.3.6.A14 Placement of the name servers

Primary and Secondary Advertising DNS servers SHOULD be placed in different network segments.

#### APP.3.6.A15 Evaluation of log data

The log files of the DNS server and the underlying operating system SHOULD be checked and evaluated regularly.

#### APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure

The DNS servers SHOULD be integrated into a "Packet Filter - Application Level Gateway Packet Filter" (PAP) structure (see also NET.3.2 * Firewall *): The Advertising DNS server SHOULD be located in a demilitarized zone (DMZ) of the outer packet filter. The resolving DNS server SHOULD be placed in a DMZ of the inner packet filter.

#### APP.3.6.A17 Use of DNSSEC

The DNS protocol extension DNSSEC SHOULD be activated on Resolving DNS servers as well as on Advertising DNS servers. The keys used Key-Signing-Keys (KSK) and Zone-Signing-Key (ZSK) SHOULD be changed regularly.

#### APP.3.6.A18 Extended protection of zone transfers

In order to secure zone transfers more strongly, additional Transaction Signatures (TSIG) SHOULD be used.

#### APP.3.6.A19 Disposal of DNS servers

If a DNS server is discarded, all server storage media SHOULD be securely deleted. In addition, the DNS server SHOULD be deleted from both the domain namespace and the network.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.3.6.A20 Assessment of the contingency plan (A)

It SHOULD be checked regularly if the emergency plan is feasible.

#### APP.3.6.A21 Hidden Master (CIA)

To complicate attacks on the primary advertising DNS server, a so-called hidden master arrangement SHOULD be made.

#### APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)

Externally accessible DNS servers SHOULD be connected via different providers.

4 Further Information
------------------------------

### 4.1 Literature

Further information about threats and security measures in the area of ​​"DNS servers" can be found in the following publications, among others:

* #### [BSICS055] Secure Deployment of DNS Services:

  

 Recommendations for Internet Service Providers (ISP) and large companies, BSI, 2013
[https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_055.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_055.pdf)

 
* #### [BSIDNSSEC] Implementation of DNSSEC

  

 Recommendations for setting up and operating Domain Name Security Extensions, BSI, 2015
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Cyber-Sicherheit/Themen/Umsetzung\_von\_DNSSEC.pdf](https://www.bsi.bund.de/SharedDocs/ Downloads / DE / BSI / cyber security / topics / Umsetzung_von_DNSSEC.pdf)

 
* #### [ISILANA] BSI Internet Security Standard (Isi Series):

  

 Secure connection of local networks to the Internet (Isi-LANA), Federal Office for Information Security (BSI), 2014
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/ standard criteria / ISi series / ISi-LANA / lana_node.html)

 
* #### [NIST800-81-2] NIST Special Publication 800-81-2:

  

 Secure Domain Name System (DNS) - Deployment Guide, NIST, 09.2013
 <Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-81-2.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "DNS server" building block.

* G 0.9 Failure or malfunction of communication networks
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
* G 0.40 Denial of Service
* G 0.43 Importing messages
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
* G 0.18 Missing planning or missing adjustment
  * APP.3.6.A1 Planning the DNS deployment
  * APP.3.6.A10 Selection of a suitable DNS server product
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A8 Domain Name Management [IT Leader]
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
* G 0.19 Disclosure of information worthy of protection
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A13 Limiting the visibility of domain information
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A19 Disposal of DNS servers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.20 Information or products from unreliable sources
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.21 Manipulation of hardware or software
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.22 Manipulation of information
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.25 Failure of devices or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.26 Malfunction of equipment or systems
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.27 Resource shortage
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A15 Evaluation of log data
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.28 Software vulnerabilities or errors
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A5 Timely import of security-relevant patches and updates
  * APP.3.6.A10 Selection of a suitable DNS server product
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
  * APP.3.6.A21 Hidden Master (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
* G 0.32 Abuse of permissions
  * APP.3.6.A12 Training of Responsible Persons [Supervisors, Head of IT]
  * APP.3.6.A15 Evaluation of log data
* G 0.40 Denial of Service
  * APP.3.6.A2 Use of redundant DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
  * APP.3.6.A21 Hidden Master (CIA)
  * APP.3.6.A22 Connection of DNS servers via different providers [Head IT] (IA)
  * APP.3.6.A3 Use of separate DNS servers for internal and external requests
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A7 Monitoring of DNS servers
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A11 Sufficient size of DNS servers
  * APP.3.6.A14 Placement of the name servers
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.43 Importing messages
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A16 Integration of a DNS server into a "P-A-P" structure
  * APP.3.6.A17 Use of DNSSEC
* G 0.45 data loss
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A9 Create an emergency plan for DNS servers
  * APP.3.6.A20 Assessment of the contingency plan (A)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.6.A4 Secure basic configuration of a DNS server
  * APP.3.6.A6 Secure Dynamic DNS Updates
  * APP.3.6.A17 Use of DNSSEC
  * APP.3.6.A18 Extended protection of zone transfers
