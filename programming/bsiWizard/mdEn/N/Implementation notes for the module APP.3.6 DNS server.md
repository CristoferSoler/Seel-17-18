Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

These implementation notes cover the basic security features of the Domain Name System (DNS) and the servers required for this purpose. DNS is a network service that is used to transform host names of IT systems into IP addresses. Normally, a hostname is searched for the corresponding IP address (forward resolution). If, however, the IP address is known and the host name is searched, this is called backward resolution. The term DNS server stands for the software used in the actual sense, but is usually also used as a synonym for the computer on which this software is operated.

DNS servers can be distinguished according to their tasks, there are basically two different types: Advertising DNS server and Resolving DNS server. Advertising DNS servers are usually responsible for processing requests from the Internet. Resolving DNS servers, on the other hand, process requests from the internal network.

A failure of a DNS server can seriously affect the operation of an IT infrastructure. It is not directly the failed DNS system problematic, but the resulting restriction of DNS-based services. Under certain circumstances, web servers, e-mail servers are no longer available and the remote maintenance does not work anymore. As DNS is required by many networking applications, the specification (RFC 1034) requires at least two Authoritative DNS servers to operate on each zone.

Since a well-functioning name resolution is a prerequisite for many applications and thus for a smooth operation, DNS servers should be carefully planned, implemented and operated properly. Therefore, the focus of these implementation notes is on the availability of DNS servers and the integrity of the information being transmitted, as well as problems that may arise during DNS server operation.

### 1.2 Life cycle

** planning and conception **

Before a DNS server is selected and the infrastructure is planned, it should be checked whether the desired domain name is still owned by the institution or still available (see APP.3.6.M8 * Domain Name Management) *. If DNS Security Extensions (DNSSEC) are to be used, the measure APP.3.6.M17 * Use of DNSSEC * should be implemented. Planning determines how the DNS servers are integrated into the network infrastructure of the information network (see APP.3.6.M1 * DNS Use Planning *). It should also be decided what the performance capacity of a DNS server must be. On the one hand, this affects the IT system itself and, on the other hand, the transmission capacity of the network connection (see APP.3.6.M11 * Sufficient dimensioning of the DNS server *).

**Procurement**

There are different software products in the field of DNS servers. In order to make an appropriate choice, it must be checked whether the potential products have all the required functions and that all security requirements can be met with them (see APP.3.6.M10 * Selection of a suitable DNS server product *).

**Implementation**

After planning is complete and the software is installed on the server's operating system, the DNS server must be securely set up and configured (see APP.3.6.M4 * Secure Basic Configuration of a DNS Server *, APP.3.6.M6 * Dynamic Backup DNS updates * and APP.3.6.M13 * Limitation of visibility of domain information *). In addition, responsible personnel should be trained to be sufficiently familiar with the security measures that are relevant to them (see APP.3.6.M12 * Training of Responsible Persons *).

**Business**
During operation, it is important to be aware of current security vulnerabilities in order to install any existing software updates or implement other security measures (see APP.3.6.M5 * Timely Import of Security-Related Patches and Updates *). Furthermore, packet filter rules should minimize communication between the DNS server and other DNS servers and clients (see APP.3.6.M16 * Integration of a DNS server into a "P-A-P" structure *). In order to ensure a smooth operation and to detect possible malfunctions or anomalies, it is necessary to continuously monitor the DNS server and to analyze its log data regularly (see APP.3.6.M7 * Monitoring of DNS servers * and APP.3.6.M15 * Evaluation the log data *).

If a DNS server is configured or the DNS information is changed manually, the domain information should be backed up beforehand so that it can be restored if necessary.

** ** segregation

If DNS servers are taken out of service, these should be disposed of in a regulated manner (see APP.3.6.M19 * Separation of DNS servers *).

** Emergency Preparedness **

As part of emergency preparedness, contingency plans should be prepared for the relevant vulnerabilities (see APP.3.6.M9 * Creating a DNS server contingency plan *). In addition, Advertising DNS servers must be configured redundantly (see APP.3.6.M2 * Deployment of redundant DNS servers *).

2 measures
-----------

The following are specific implementation notes in the "DNS Server" section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### APP.3.6.M1 Planning the DNS deployment

In order to securely implement DNS servers, adequate planning must take place in advance. First of all, a concept has to be developed that describes, among other things, how DNS should be set up and which domain information is worth protecting. The responsible persons should also determine how DNS should be integrated into the network of the information network. However, not only aspects that are directly linked to the term security must be planned, but also normal business aspects that can lead to safety requirements.

#### APP.3.6.M2 Use of redundant DNS servers

In order to guarantee high reliability, sufficient hardware redundancy must be ensured. That's why there should always be at least two separate Advertising DNS servers. Resiliency can be further increased if the servers are physically separated.

#### APP.3.6.M3 Use of separate DNS servers for internal and external requests

Advertising and Resolving DNS servers perform different tasks and should therefore be disconnected. It is therefore advisable to use your own physical servers for advertising and for resolving DNS servers. The Advertising DNS server manages the externally available domain information and supports only iterative requests, the resolving DNS server manages the inward visible information and supports both iterative and recursive requests.

Client applications need a resolver to use DNS. This is standard integrated in the common operating systems. However, it must be ensured that the resolvers of the internal IT systems use the internal resolving DNS servers for name resolution. Under no circumstances should you consult external DNS servers by default. In addition, the DNS suffixes used by the resolvers should also be specified, for example * bsi.bund.de *. This automatically adds the rest of the domain name to the Fully Qualified Domain Name (FQDN) * hostx.bsi.bund.de * when * * name * resolves the name.

#### APP.3.6.M4 Secure basic configuration of a DNS server
Servers are attractive targets for attackers. If they manage to manipulate those servers, they can affect all services that use DNS, such as web servers, email servers, or remote administration applications. Therefore, a thorough basic configuration of DNS servers is essential.

** DNS server version **

The version of the DNS server product used can provide valuable information to an attacker. Therefore, the version number should be hidden, for example by replacing it with * unknown *. Although this measure does not directly increase the security level of a DNS server, it makes it more difficult for an attacker to obtain information.

**Requests**

An increased risk of cache poisoning attacks exists when DNS servers unconditionally accept requests. Therefore, it is important to limit which requests are accepted.

Resolving DNS servers are responsible for requesting resolvers from the institution's network, typically recursive requests. This means that Resolving DNS servers must accept recursive requests from the internal network. Requests from the Internet may not be accepted, as this is the responsibility of the Advertising DNS server.

Inquiries originating from the Internet must always be iteratively handled, thus the Advertising DNS server only provides information about its managed zones and can not send forged replies.

To increase the security level of resolving DNS servers, another mechanism must be used. As already mentioned, Resolving DNS servers have to accept recursive requests from intra-institutional IT systems. Resolving DNS servers will inevitably have to resolve names for which they are not authoritative. An attacker could introduce fake answers here. The assignment of responses to requests is done via:

* IP address
* ID of the request (random number)
* Source Port of the request
Since the IP address and ID offer too little protection, additional random source ports should be used when sending requests. At the moment we are also going to configure several IP addresses for resolving DNS servers and to randomize them.

** zone transfers **

The purpose of zone transfers is to synchronize primary DNS servers with secondary DNS servers. The Primary DNS server reads the domain information from the zone files, via a zone transfer they reach the Secondary DNS server (s) and are kept synchronized. It must be ensured that the zone transfer between the Primary and the Secondary DNS server really works.

In order to prevent unauthorized persons from starting a zone transfer and thus receiving the entire domain information of a zone, zone transfers must be configured so that they are only possible between Primary and Secondary DNS servers. This must be done at least via the restriction to the IP addresses of the DNS servers, even more secure is to use Transaction Signatures (see APP.3.6.M18 * Extended coverage of zone transfers *).

The restrictions on IP addresses are as follows: The Primary DNS server must be configured for each zone that is the associated Secondary DNS server. This is done by specifying one or more IP addresses. One or more Secondary DNS servers for a zone must be configured to be the primary DNS server responsible.
To ensure zone transfer works, it should be checked for correct operation after each change to the zone transfer settings. For this example, a zone transfer can be performed. Thereafter, it is checked in the log files, if errors have occurred. For non-extensive zones, it is possible to manually compare the domain information managed by the primary DNS server with that of the secondary DNS server.

** Exclude certain DNS servers **

If DNS servers that provide incorrect domain information are known, the institution's resolving DNS servers must be prevented from sending requests to these DNS servers. If private IP networks such as * 10/8, 172.16 / 12 * and * 192.168 / 16 * are not used in the institution, requests from these networks should be ignored for security reasons.

#### APP.3.6.M5 Timely import of security-relevant patches and updates

Those responsible must inform themselves about current security vulnerabilities in the software used at an early stage. Ideally, at least two different sources of information, including a vendor-independent one, should be used. Below, for example, all previously published vulnerabilities in the DNS server product BIND can be read.

For products for which no security patches are (yet) available from the manufacturer, it must be checked in good time whether it is still responsible to use them. It will then also be necessary to examine which additional measures can be implemented in order to nevertheless protect the affected systems.

Before any updates or patches are installed, always back up the system so that it can recover to its original state if problems occur. In advance, it must be checked on a test system whether the security updates are compatible and do not cause any errors.

It should be documented when, by whom and for what reason patches and updates were recorded. From the documentation, the current patch level of the system must be quickly determined at any time. In this way, those responsible can quickly become aware of whether a new vulnerability also endangers their own systems.

#### APP.3.6.M6 Secure Dynamic DNS Updates

To be able to use dynamic updates securely, it must be ensured that only legitimate IT systems can make changes to domain information. Furthermore, it must be determined which domain information the individual IT systems are allowed to change. To ensure that domain information is not manipulated by unauthorized IT systems using dynamic updates, there are two options:

* Restriction of authorized hosts using IP addresses,
* Restriction of authorized hosts using TSIG (see APP.3.6.M18 Extended coverage of zone transfers).
When limiting by IP address, the IP address identifies the source of the dynamic update. TSIG uses symmetric encryption to identify the source of the dynamic update.

Besides the vulnerability to IP spoofing, there is another problem with using IP addresses. Secondary DNS servers can be set up as dynamic update forwarders, and the primary DNS server can be configured to accept only updates from Secondary DNS servers. Because only Secondary DNS servers configure which IT systems accept updates, the Primary DNS server will not know where the updates come from. Thus, it is not possible to limit which hosts are allowed to perform dynamic DNS updates based on the original source.
In addition to the identification of the source must be configured, which domain information may be changed. The rules must be configured so that dynamic updates can be used smoothly. For example, a DHCP server might need permission to change the mapping of domain names and IP addresses, but there is no reason to allow a DHCP server to change the DNS server responsible for a zone.

#### APP.3.6.M7 Monitoring of DNS servers

In order to maintain the security of a DNS server in operation, it is not enough to rely only on careful planning and initial configuration. A number of measures have to be taken to identify any problems and safety-critical loopholes.

The capacity requirements should already be specified in the planning. Due to the fact that the capacity requirements of the

* Size of the zone (s),
* Number of requests,
* Number of recursive requests,
* Number of zone transfers,
* Number of dynamic updates etc.
it is difficult to plan the required capacities. Therefore, it must be regularly monitored how busy a DNS server is to adjust the power capacity of the hardware if necessary. Furthermore, an increased load can be an indicator of an ongoing attack. The communication of the DNS server is therefore suitable for logging. Logging should include, for example, the number of requests, zone transfers, dynamic updates, etc. (see OPS.1.1.7 * Logging *).

#### APP.3.6.M8 Domain Name Management [IT Leader]

Internet domain names (in short: domains) must be registered with registrars. A registry can give names to one or more so-called top-level domains, e.g. For example, the classic domains * .com, .org, .gov * and the various country domains such as * .de * for Germany, * .at * for Austria and * .ch * for Switzerland. Domains are registered for a specific period of time. If this period has expired, the registration must be renewed for a fee. Forgetting to extend a registration can have unpleasant consequences. It must therefore be ensured that registrations for all domains used by an institution are renewed on a regular and timely basis. For this purpose, a body should be defined in each institution, which coordinates the administration of the domain names at the various registration authorities.

Several top-level domains (such as * .com * and * .org *) have different registries. A change of registrar is possible at any time, but usually with costs. It is important to have an overview of the registration period and the renewal price for all registered domains in order to ensure a timely renewal of the registration.

** Preventing Domain Grabbing **

If an institution does not self-register and manage its domains, but handles it through an Internet service provider, it must be careful when designing the contract to retain control of its domains. This can be important, for example, in the case of a possible change of registrar or in the resolution of name disputes.

In the event of errors and omissions of the service provider in the administration of domain names, appropriate provisions must be made, since in such cases, considerable damage may occur.

If the name servers are not hosted in the institution itself but are hosted by a service provider, the service level agreements should in particular define requirements for the availability of the name servers and the processing times for changes in the DNS of the institution.

#### APP.3.6.M9 Create an emergency plan for DNS servers
If the network service DNS fails in an information network, this seriously affects the operation of the IT infrastructure. It is not directly the failed DNS system problematic, but the resulting restriction of DNS-based services. Under certain circumstances, web servers are no longer available and remote maintenance is no longer working.

Depending on which DNS servers fail, the name resolution within the institution and / or from outside no longer works. If the name resolution from outside does not work anymore, this will usually become public quickly, which can result in damage to the image in the event of regular or long-lasting failures.

It is therefore a concept to design how a failure can minimize the resulting consequences. The following aspects should be considered:

* The contingency planning for DNS servers must be integrated into the existing contingency plan.
* A system failure can lead to data loss. Therefore, a data protection concept for the zone files has to be created. This must be integrated into the existing data protection concept.
* In addition to the disaster recovery plan for the DNS server, an emergency plan must also exist for the underlying operating system.
* A functioning internet connection is required for the operation of a DNS server for requests from the Internet.
* The system configuration must be documented. Important tasks must be described so that in the event of an emergency, the entire system can be restored by IT staff without prior knowledge of this system configuration.
* If the failure was the result of an attack, the vulnerability must be resolved and documented.
* A recovery plan must be created so that the IT system (s) can be booted up again in a regulated manner.
### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "DNS servers".

#### APP.3.6.M10 Selection of a suitable DNS server product

DNS server products vary in performance and ease of use. When procuring such a product, the following aspects should be considered:

* The DNS server product should have already proven itself in practice.
* If enough trained personnel already exist for a given product and all functionality requirements are met, this DNS server product should be used.
* There are DNS server products whose implementation differs from the standards to DNS (RFC 1034, 1035 etc.). It is planned to use different DNS server products to For example, to avoid software monocultures, this should only be done after a compatibility check.
* In case DNSSEC is used, care must be taken to ensure that this is supported by the DNS server product.
* If the master files are edited manually, it should be tool-supported to check whether the zone file is syntactically correct.
#### APP.3.6.M11 Sufficient size of DNS servers

The hardware on which a DNS server is to be operated decisively influences the overall performance of the resulting system. It should also be considered how many requests a DNS server must serve on average, whether it is a Resolving DNS server accepting recursive requests, or whether it is an Advertising DNS server that accepts only iterative requests and whether DNSSEC should be used.
For DNS servers, sufficient main memory is important, which prevents the server from having to swap out memory contents to the hard disk, thus increasing response times. When using DNSSEC, it is important to ensure that processor performance is increased accordingly to maintain adequate throughput for cryptographic operations. The selected capacities for main memory and processor performance must be checked in regular operation, since the actual required capacities can only be accurately determined here.

In order to avoid external processes influencing the DNS server, only the DNS server should be operated on the hardware used. To ward off distributed denial-of-service attacks, DNS servers should have broadband and robust network connectivity.

#### APP.3.6.M12 Training of the persons responsible [Supervisor, Head IT]

In order to administrate a DNS server correctly and securely, the responsible employees must be trained accordingly. Even small configuration errors can lead to safety-critical vulnerabilities. Particularly solid expertise is required when scheduling the use of DNS servers and restricting communication to legitimate subscribers.

In addition to the aspects of general operating system security, the following points are important:

* Installing a DNS server
* Possibilities to integrate DNS servers into the boot process of the operating system
* Introduction to possible hazards
* Development of a rights concept, both for the configuration rights by administrators and for the rights of the DNS server process
* Difference between Advertising and Resolving DNS server
* Configuration of the DNS server
* Mechanisms for securing requests
* Mechanisms to secure zone transfers
* Mechanisms to secure dynamic updates
* Uses and configuration of DNSSEC
* Mechanisms to ensure the availability of DNS servers
* Mechanisms to secure the zone information
For training and further education the institution should plan a sufficient budget.

#### APP.3.6.M13 Limiting the visibility of domain information

The main function of DNS is to resolve names and IP addresses. In order to meet these requirements, DNS servers store, among other things, the assignment of names and IP addresses of all computers and network components. Part of this information needs to be published, eg. DNS server, web server, mail server, file server, VPN connection points. If this domain information were not publicly available, it would not be possible to establish a connection with domain names via the Internet to these servers.

Domain information about internal computers and network components, however, are usually not intended for the public and should therefore remain within the institution. Because domain information often tells you something about the function or location of the IT component in question, DNS Information Leakage is used when this information is published. The publication itself does not represent any direct damage to the information network. However, the domain information obtained can be used to prepare an attack on the information network. An attacker can gain an overview of the network, the security-related components and the worthwhile goals.

The namespace of an information network should be divided into a public and an institution-internal area. The public part should only contain domain information (typically IP address and hostname) to make services that should be accessible from outside work well.
Within the institution, the visibility of the information usually does not have to be limited. Which domain information is visible to the outside and which is not, should be taken into account when planning the DNS deployment.

#### APP.3.6.M14 Placement of the name servers

To ensure sufficient availability for line faults, external DNS servers should be redundantly connected and connected in different network segments. In addition, they should not be connected to the same network coupling element. Thus, the availability of name resolution is not affected by failure of an IP subnet or a network element.

Where a DNS server is placed ultimately depends on the network infrastructure of the respective institution. However, there are some basic rules that should be followed:

* Primary and Secondary DNS servers should be placed in different IP subnets. Furthermore, they should not be connected to the same network coupling element. This ensures name resolution, even if an IP subnet or a network switch fails.
* Advertising DNS servers should be placed in the demilitarized zone (DMZ). Further information can be found in the module NET.1.1 Network architecture and design.
* Resolving DNS servers are responsible for inquiries from institution-internal IT systems. They should therefore be placed as close as possible to the requesting IT systems within the trusted network of the institution in order to avoid long response times and unnecessary network load. In addition, Resolving DNS servers must not be accessible from external IT systems.
* If the visibility of the information is restricted, the public part of the domain information should be managed by the Advertising DNS server in the DMZ.
* If a forwarder is used for the internal name server for the resolution of the Internet domain name space, it should not be placed in the internal network.
* If caching-only DNS servers are used in the corporate network, the resolvers on the clients should not cache domain information. The caching is handled by the caching-only DNS server. The central memory minimizes the number of requests. Furthermore, in the case of a successful cache poisoning attack, the central cache of the caching-only DNS server can simply be deleted to remove the spoofed data.
* In order to accept DNS network traffic, rules must be set up on the firewall (see APP.3.6.M16 Integration of a DNS server into a "P-A-P" structure). When planning, care should be taken that as few routes and ports as possible have to be opened.
#### APP.3.6.M15 Evaluation of log data

The log files of the DNS server and the underlying operating system should be regularly checked and evaluated. Irregularities in the log files, which may be indications of potential problems, include:

* frequent inquiries from certain sources,
* frequent (failed) zone transfers,
* frequent requests for specific domain names,
* frequent requests for domain names that do not exist,
* frequent unauthorized recursive requests.
Irregularities do not necessarily mean that the server is compromised. Often they also occur due to incorrect settings.

#### APP.3.6.M16 Integration of a DNS server into a "P-A-P" structure

Especially DNS server products are always a source of security problems. Due to the special importance of domain information and the increased susceptibility of the DNS software to attacks, a special setup is required to securely deploy and use domain information.

** Minimize communication through packet filters **

DNS servers require the following communication channels:
* Resolving DNS server allowed on port 53 of the Advertising DNS server UDP
* Advertising DNS server is allowed on all ports of Resolving DNS server UDP (only for stateless firewall necessary)
* Resolving DNS server allowed on port 53 of its forwarder UDP
* Forwarder is allowed on all ports of Resolving DNS server UDP (only for stateless firewall necessary)
* External network allowed on port 53 of the Advertising DNS server UDP
* Advertising DNS server is allowed on all ports of external DNS servers UDP and TCP (only necessary with stateless firewall)
* Internal network allowed on port 53 of Resolving DNS server UDP
* Resolving DNS server is allowed on all ports of internal network UDP (only for stateless firewall necessary)
* Primary DNS server is allowed on port 53 of its Secondary DNS servers UDP and TCP
* Secondary DNS server is allowed on port 53 of its Primary DNS server UDP and TCP
If only these rules are implemented, only limited communication from the Internet to the shared services is possible. If the communication partners can be further restricted, an attacker can not establish a direct connection to the Internet server.

** Note: ** The above rules can cause the DNS server not to be reached from any machine because ICMP is not allowed through. Therefore, it is recommended to pass the ICMP subtype * icmp unreachable * from the Internet to the Internet server.

** DNS server ** in a "P-A-P" structure

In order to integrate DNS securely into a "P-A-P" structure, the structure shown in Figure 1, in which there is no direct connection between a client in the trusted network and a DNS server in the untrusted network (and vice versa), can be used. Two separate DNS servers are used.

The Advertising DNS server, which contains the externally available information, is located in a DMZ of the outer packet filter. It is set up as a primary DNS server for the domain of the trusted network and contains only the essential information, for example:

* Name and IP address of the external mail server (MX record)
* Names and addresses of information servers that provide information to the public. In this case, a distinction must be made between the servers that are located in front of the Application Level Gateway (ALG) and those that are located behind the ALG. For the former, the address of the server itself must be entered, for the latter the address of the ALG.
The Resolving DNS server is placed in a DMZ of the inner packet filter. It contains the information about the computers of the internal network. For computers of the internal network, the Resolving DNS server is entered as DNS server: All clients of the trusted network use only the Resolving DNS server, for Unix computers, for example, by means of entries in the file * / etc / resolv.conf. * Required a client in the trusted network domain information from the untrusted network, he makes the request to the Resolving DNS server. As a forwarder, this server uses a public DNS server (or an extra forwarder) for queries that involve external names. Direct access to the Resolving DNS server from the untrusted network should be prevented by packet filtering rules so that the domain information of the trusted network is only visible in the trusted network.

The packet filter used must be configured in such a way that only the DNS service is permitted between the DNS servers. H. Port 53 as (depending on the direction in question) source or destination port. The Advertising DNS server should not allow any connections to the internal network. The server should only be administered via appropriately secured connections (eg SSH-2).
Table 1 describes a possible access policy configuration that can be implemented using appropriate packet filter rules. It is assumed that the servers are administered via an SSH connection from the internal network and that UDP is used for DNS as the carrier protocol. Log data is transmitted via syslog to a log server.

Table 1: Access rule configuration

** Domain registration with external service provider **

In this alternative, important domain information is stored at an external service provider and not provided by its own DNS server. The difference to the scenarios just described consists essentially in the omission of the Advertising DNS server. DNS queries from the external network to domain information from the internal network are not sent to the internal DNS DNS server, but to the DNS server of the external service provider and answered by this. When resolving requests for external DNS names or IP addresses, the resolving DNS server accesses a DNS server in the external network, usually operated by the Internet provider, directly across the firewall.

Even with this integration variant, only the absolutely necessary domain information should be offered externally, such as the name and IP address of the mail server and the ALG. For particularly harmless institutions internal users, the Resolving DNS server can also be operated in the internal network, rather than in a DMZ of the inner packet filter, which facilitates the administration of the packet filter something.

Advantages of this variant are the low investment costs and the low complexity of integration into a P-A-P structure.

#### APP.3.6.M17 Use of DNSSEC

DNSSEC is designed to protect DNS against attacks, including cache poisoning attacks. This is realized by asymmetric cryptography. At DNSSEC, all zone information is signed with a private key. These signatures can be verified using the associated public key. The key pair is called a zone signing key (ZSK). If a DNSSEC-supporting resolver makes a request to a DNS server that has DNSSEC configured, the server will respond by returning the domain information containing the signatures. The resolver can use the signature and public key to verify that the domain information is correct.

To ensure the authenticity of the ZSK, it is signed using key-signing keys (KSK). A hash value of the public part of the KSK is transmitted to the parent domain. The parent domain uses its keys to sign the hash value and confirm the authenticity of the hash value. This creates a chain of trust. If the parent domain does not use DNSSEC, it has no keys and can not create a signature to verify the authenticity of the KSK. However, you can tell your DNS servers to trust their own keys, thus creating islands of trust. As DNSSEC becomes more prevalent, these trusted islands become larger, and thus the security level higher. DNSSEC offers the following security mechanisms:

* The source of DNS information is authenticated.
* The integrity of the domain information is ensured, so domain information can no longer be manipulated because the signature makes this manipulation visible. For example, customers can be sure to communicate with the right web server or mail server.
* If a domain name does not exist, an authenticated error message will be sent.
The keys ZSK and KSK must be carefully managed and regularly exchanged. Since more data is being signed with the ZSK, they have to be exchanged more often. Depending on the size of the signed zones, a change in the timeframe of one to three months constitutes a suitable level of security. A change should be made to the KSK after one year at the latest. If the KSK and ZSK reach the public, the keys must be exchanged immediately.

With DNSSEC and the cryptographic operations it requires, it may be necessary to adjust the performance capacity of DNS servers, and it may be necessary to increase computational power. It must be ensured that the response time is kept acceptable even at peak loads.

#### APP.3.6.M18 Extended coverage of zone transfers

To achieve a higher level of protection, zone transfers can be secured via transaction signatures (TSIG). TSIG defines symmetric keys on the primary DNS server and the secondary DNS server (s). When a zone transfer is started, TSIG generates a hash message authentication code (HMAC) from the binary data of the request using the symmetric key and a hash function. The HMAC will be attached to the request. The Secondary DNS server, which also knows the key, calculates the HMAC independently. If the number of received and calculated HMACs is the same, the zone transfer will be carried out, otherwise it will be rejected. This method also protects against IP spoofing, in contrast to IP address-based security. However, with TSIG, it should be noted that not every DNS server product has this feature. There may also be manufacturer-specific deviations in the respective implementation.

#### APP.3.6.M19 Disposal of DNS servers

If it is decided not to continue to operate a DNS server, for example because the domain is being dissolved, there are some points to consider when decommissioning it. Among other things, the rejection plan is intended to prevent references to defunct DNS servers from remaining in the domain namespace.

** Erase / Dispose of storage media **

The storage media of all affected computers should be safely deleted before reuse. If the hardware is disposed of, then this should also be done in a secure manner.

** Delete the DNS server from the domain namespace **

If the DNS server is not registered with the parent domain, no further action is required. However, if the DNS server is registered with the parent domain, the disassociation must be reported to the administrators of the parent domain so that they delete all zone entries from the remote DNS servers in the parent domain.

** Delete system from network connection **

All references at network and operating system level are to be deleted. If the segregated server is entered as the default DNS server in the institution's internal systems, these entries must be deleted. Zone transfers configured between the remote DNS server and existing DNS servers must also be deleted.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### APP.3.6.M20 Review of the contingency plan (A)
The contingency plan for DNS servers must be tested regularly on a regular basis. This is the only way to ensure that the measures described in the recovery plans are actually feasible. At the same time, the employees learn about the processes described in the exercises and train their implementation. Finally, the exercise provides insights on actual recovery and recovery times.

#### APP.3.6.M21 Hidden Master (CIA)

A so-called hidden master configuration ensures that the primary advertising DNS server is not accessible from the outside and is not visible in the DNS zone data. Requests will only be answered by at least two secondary Advertising DNS servers, which will retrieve their data via a secure line from the hidden primary advertising DNS server.

#### APP.3.6.M22 Connection of DNS servers via different providers [IT manager] (IA)

When registering a domain name, at least two DNS name servers (* Primary and Secondary Nameserver *) must be specified, which are responsible for assigning host names to IP addresses. A name server is often operated by the internet access provider, but can also be operated by the institution itself. To prevent DoS attacks, Primary and Secondary name servers should be located in different networks and connected via different providers.

3 Further information
------------------------------

### 3.1 Worth knowing

The Domain Name System (DNS) is a network service used to resolve host names of IT systems on computer networks. Forward resolution is when the IP address to a host name is detected. If, on the other hand, the host name is determined to be an IP address, this is referred to as backward resolution.

** domain name space **

DNS is a distributed database that manages the tree-shaped domain namespace (see Figure 2). The tree consists of nodes and leaves, which are called labels. The concatenation of the labels separated by dots results in a domain name. The domain namespace is divided into different domains. The topmost level, the root, is represented as a dot and named * root *. Below are the top-level domains such as. * Com *,. * Edu *,. * De *,. * At *, then the second-level domains like. * Bund * etc.

The domain name space stores information about the assignment of IP addresses to domain names. DNS can be referred to as a kind of directory in computer networks whose main task is to resolve names. It is sufficient, for example, to enter the domain name * www.bsi.bund.de * in the browser, DNS will find the corresponding IP address in the domain name space and the browser can connect to the result of the search to the corresponding web server.

Basically, a distinction must be made between domains and zones. A zone, as shown in Figure 3, is a management unit that reads a DNS server through a master file. A master file contains all the domain information of a zone and is managed by the responsible administrators. Examples of zones are * arpa *, * com *, * example, a, b * and * c, * where * com *, * example, a, b * and * c * each represent a separate zone. By contrast, a domain, for example, is understood to mean a domain such as * com * and all subdomains underneath, in this case * example *, * a *, * b *, * c *.

For each zone, at least two DNS servers are authoritative, meaning that these DNS servers manage the domain information for that zone. In addition, each DNS server knows the authoritative DNS servers for its subdomains. This means that, for example, the DNS server for * com * knows the DNS server for * example *, and can therefore refer to it with a name resolution.

** ** Resolver
Client applications need a resolver to participate in DNS. This is often part of the operating system. If a client application requires name resolution, it makes a request to the resolver. This packs the request into a DNS-compliant packet, sends it to a DNS server, interprets the response and transmits the data back to the appropriate application. To increase the performance of DNS, the resolver caches the response data for a specified time. As long as the data is in the cache, the DNS server will not be interrogated again in a repeated resolution.

** DNS server **

DNS servers are applications that manage information about a particular area of ​​the domain namespace. The information is stored in so-called zone files. If a DNS server manages several domains, for example, * bund.de * and the associated subdomain * bsi.bund.de *, these are stored in separate zones. The information about a zone is read by a DNS server from the master files.

DNS servers are differentiated according to their tasks, there are basically two different types:

* Advertising DNS server
* Resolving DNS server
Advertising DNS servers are usually responsible for processing requests for their own domains from the Internet. If you have saved the desired domain information, you will provide the appropriate answer. Otherwise, they will refer you to another DNS server. The main task of an Advertising DNS server is to provide its stored domain information.

Resolving DNS servers, on the other hand, usually process requests from within the institution's internal network. Once they have the domain information they need, they, like Advertising DNS servers, provide the answer. Otherwise, Resolving DNS servers will not direct to another DNS server, but will inherit the name resolution itself.

DNS servers that can answer requests using their own zone information are said to be authoritative. If a DNS server receives a request that is not related to its own zone (s) and does not have any information in the cache, a DNS server can respond in three ways:

* Delegation Delegation means that some of the domain name space information has been swapped out to a subdomain. For example, if the DNS server receives a request for bund.de, the DNS server will forward the request to the appropriate DNS server. Since a DNS server must know all the DNS servers responsible for the delegated zones, it can forward the request directly to the responsible DNS servers.
* Resolution via root name serversThere are a total of 13 root DNS servers. These root DNS servers have stored which DNS servers are authoritative for the top-level domains. If the data you want is outside the managed domain and there is no data in the cache, you must start a recursive resolution, starting with the root name servers. This behavior corresponds to a resolving DNS server.
* Forwarding If a DNS server can not deliver the requested information, it forwards the request to a previously configured DNS server.
**Communication**

As described earlier, applications communicate with DNS servers through the resolver interface, regardless of whether it is an Advertising or Resolving DNS server. Resolvers send requests to DNS servers for applications that require name resolution, and interpret the responses received to return them to the application. Basically, a distinction is made between two types of requests:
* iterative requests: iterative means that the polled DNS server, if it has not saved the required data, refers to the next responsible DNS server. The polled DNS server is thus an advertising DNS server. The requesting resolver must itself perform the entire name resolution. A name resolution to www.bsi.bund.de over the root DNS servers (root DNS servers answer only iterative inquiries and thus are advertising DNS servers) would look like follows. In the first step, the resolver queries the Root DNS servers for the Advertising DNS server, which is responsible for de. responsible is. In the second step, the resolver determines the DNS server responsible for the responsible advertising DNS server, which is responsible for bund.de. Thereafter, the advertising DNS server for bsi.bund.de is requested from this. Finally, the Advertising DNS server for bsi.bund.de can deliver the IP address to www.bsi.bund.de to the resolver.
* Recursive requests: The resolution works very similar for the recursive request. However, the DNS server responsible for the resolver takes over the complete name resolution as described above. So it's a resolving DNS server. The resolver of the client only has to make one request.
An Advertising DNS server accepts only iterative requests, while a Resolving DNS server accepts both iterative and recursive requests. Recursive queries mean more stress on the DNS server than iterative queries.

** zone transfers **

Because DNS is required by many networking applications, the specification (RFC 1034) requires at least two authoritative DNS servers to be operated for each zone. Since it is too time-consuming to manage separate master files for each DNS server, which must be consistent, synchronization is performed via zone transfer. The DNS server, which obtains the domain information directly from the master files, is called the Primary or Master DNS server. Each additional DNS server is referred to as Secondary or Slave DNS server and receives the data via a zone transfer from the Primary DNS server. A secondary DNS server periodically checks to see if its zone (s) domain information has changed or is notified of changes by its Primary DNS server. If so, the secondary DNS server initiates a zone transfer to update its domain information.

** Caching-Only DNS Server **

The caching-only DNS server is a special case of a resolving DNS server. Typically, a DNS server, whether advertising or resolving DNS server, is authoritative for one or more zones. This means that he has read out the domain information about these zones from the master files or received from his master DNS server via a zone transfer. Caching-only DNS servers, on the other hand, are not authoritative for any zone; they have no zones themselves. They are usually used to receive requests and perform name resolution. Caching-only DNS servers are often used as forwarders for intra-institution resolving DNS servers when they need to resolve domain information from the Internet.

### 3.2 Literature

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
