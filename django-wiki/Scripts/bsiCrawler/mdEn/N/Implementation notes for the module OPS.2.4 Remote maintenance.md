[toc]
 
1 description
--------------

### 1.1 Introduction

Remote maintenance describes spatially separate access to IT systems and the applications running on them for configuration, maintenance, repair or control purposes. Remote maintenance can be done passively through an exclusive access to the IT system or applications, or actively through direct administrative intervention in the operating system or running applications. In the case of passive remote maintenance, a local user must initiate the actual actions. In the case of active remote maintenance, on the other hand, an operating system is intervened and operated directly by an administrator. Among other things, the signals of a mouse and keyboard commands, as well as screen contents and console outputs are transmitted.

Even if effective mechanisms to secure access to remote maintenance are implemented, there is direct access from outside to the internal network and all data processed therein. Through these interfaces, external parties can endanger the institution and thus cause economic and operational damage. It is therefore necessary to safeguard the entire information security lifecycle for remote maintenance.

### 1.2 Life cycle

** planning and conception **

If the decision for a remote maintenance has been made, the safe use must be planned and designed. The aspects to be taken into account are summarized in * OPS.2.4.M1 Planning the use of remote maintenance * and * OPS.2.4.M5 Creating a guideline for remote maintenance *. The security of remote maintenance can already be decisively influenced in the planning and conception phase by considering safety-relevant aspects.

Also important is * OPS.2.4.M6 documentation for remote maintenance * for the continuous documentation of processes of remote maintenance and * OPS.2.4.M22 planning of safe use in a secure network segment * for security in Internet and Intranet scenarios.

Irrespective of the following measures, the requirements of the * module ORP.4 Identity and Authorization Management * should be observed, evaluated and implemented.

**Procurement**

In the next step, the procurement of suitable tools for remote maintenance and possibly additionally required hardware must be carried out. Based on application scenarios, the requirements for products to be procured must be formulated and, based on this, the selection of suitable products must be made. Therefore, at this point * OPS.2.4.M8 Selection of suitable remote maintenance tools * must be considered.

**Implementation**

After the organizational preparatory work has been carried out, the implementation of the remote maintenance can take place. In particular, the measures * OPS.2.4.M9 Management of remote maintenance tools *, * OPS.2.4.M10 Use of cryptographic processes for remote maintenance * and * OPS.2.4.M11 Patch and change management for remote maintenance * must be observed.

Only secure authentication mechanisms should be used for remote maintenance (see * OPS.2.4.M16 Authentication Mechanisms for Remote Maintenance *).

All users and administrators should be adequately trained in the processes of remote maintenance (see * OPS.2.4.M15 Remote Maintenance Training *).

Since the pure implementation of the remote maintenance has many interfaces to the internal and external network, suitable measures for the protection of networks, IT systems and applications must be taken (see * OPS.2.4.M7 Secure protocols for remote maintenance *, * OPS.2.4 .M3 Regulations for communication connections *, * OPS.2.4.M17 Password security for remote maintenance * and * OPS.2.4.M14 Securing remote maintenance *).

If third parties are involved in the implementation of remote maintenance, the recommendations of the measure * OPS.2.4.M18 remote maintenance by third parties * should be observed.
In order to ensure high availability of remote maintenance, the measures from * OPS.2.4.M21 Redundant use of communication networks * should be taken into account.

**Business**

After the implementation of the requirements for remote maintenance, the normal operation is started. In order to detect security breaches, a corresponding attack defense and monitoring of all IT systems and applications, which are managed by the remote maintenance, must take place.

Since the remote maintenance is always subject to changes, which are usually derived from changed requirements or application scenarios, it must be ensured that the desired level of security is maintained (see * OPS.2.4.M19 Operation of the remote maintenance and OPS.2.4.M11 patch and change management for remote maintenance *).

** Emergency Preparedness **

Recommendations for emergency provision for remote maintenance can be found in the measures * OPS.2.4.M12 Data backup for remote maintenance * and * OPS.2.4.M20 Creation of an emergency plan for the failure of remote maintenance. *

2 measures
-----------

The following are specific implementation instructions in the "Remote maintenance" area.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### OPS.2.4.M1 Planning the use of remote maintenance [IT operation]

The use of remote maintenance must be adapted to the institution and planned as required in terms of technical and organizational aspects. At least the following aspects should be considered in resource planning:

* Should the remote maintenance take place in-band (ie within the normal IT network) or out-band (ie via a dedicated administration network)? In the case of increased protection requirements, it is advisable to carry out the remote maintenance from a dedicated administration network.
* Which interfaces and protocols should be used?
* What protection is required? Which protection goals have to be met?
* Which auditing requirements have to be considered?
* Which legal and internal regulations have to be considered?
* Is remote maintenance carried out by service providers? Then OPS.2.4.M18 is to implement remote maintenance by third parties.
* May online services be used for remote maintenance?
* What is the task distribution within the institution when using the remote maintenance?
* Which requirements from the network separation are to be considered?
The more precisely the general conditions are known and the more precisely the specifications are formulated, the easier will be the next conceptualization and implementation steps of the remote maintenance.

#### OPS.2.4.M2 Secure connection setup for remote maintenance [user]

The initiation of a remote maintenance access must always be done out of the institution. This can be realized by calling the IT system to be serviced at the remote maintenance center or using an automatic callback. The external maintenance personnel must authenticate themselves at the beginning of the maintenance. If the connection to the remote maintenance center is interrupted in any way, the access to the system must be terminated by a "forced logout".

The user of the remotely-administered IT system must explicitly agree to remote access. B. via an appropriate confirmation on the system.

#### OPS.2.4.M3 Hedging communication links for remote maintenance [IT operation]

The communication interfaces and possible accesses for establishing a connection from the outside are to be limited to the necessary degree, according to the operating systems used and other related hardware and software components. Similarly, all communication connections must be disconnected after complete remote access (deactivation). For remote maintenance, necessary ports must be constantly provided. For example, the available ports can be opened with the help of a firewall portal and stored firewall rule after successful authentication of an authorized administrator.
Secure authentication mechanisms must be used taking into account the protection requirements of the respective IT system, the application or the associated network separation. If no separate administration network is used for the communication, an alternative with identical security features should be used. The permitted group of persons for establishing a connection should be restricted according to the minimum principle.

It is important that the following points are taken into account for the communication connections and the connection setup for remote maintenance:

* Ensuring the confidentiality of the transferred data: Ensuring the confidentiality of the transmitted data must be achieved by sufficient secure encryption.
* Ensuring the integrity of transmitted data: The transmission protocols used must detect and correct a random change in transmitted data.
* Ensuring the availability of remote maintenance: If time delays in remote maintenance are difficult to tolerate, redundant transmission paths should be made available.
* Ensuring the traceability of the data transfer: To make a communication traceable, logging functions can be used, which can subsequently determine which data was transferred when and to whom.
* Ensuring data reception: If it is important for remote maintenance whether data has been received correctly, acknowledgment mechanisms can be used that show whether the recipient has received the data correctly.
#### OPS.2.4.M4 Regulations for communication connections [IT operation]

With consideration of the module * NET.3.2 Firewall *, the remote maintenance must be integrated into the firewall rules of the institution. Care must be taken to ensure that existing firewall infrastructures and their regulations are not circumvented.

In accordance with the minimum principle (whitelist strategy), the protocols required for remote maintenance should be supplemented.

When checking network connectivity using ICMP, the rules for local and remote checks must be followed. Locally it is recommended to allow a ping of localhost in the local firewall to verify the correct functioning of the network card. To check the basic network connectivity, a remote check by means of ping to the required remote station should be allowed.

In terms of firewall security, it must be checked whether remote procedure calls (RPCs) can be analyzed and filtered by the established security architecture. If filtering is not possible, appropriate protective measures against abusive RPC calls must be made.

Together with the basic measures, the following measures correspond to the state of the art in the field of remote maintenance.

#### OPS.2.4.M5 Use of Online Services [IT Operations, Users]

Often an established software for the remote maintenance is charged and must be installed on each client. In exceptional situations, however, it may be helpful to administer IT systems remotely over the short term. The solution seems pragmatic that the clients connect to an online service and the administrator accesses the clients via a web server via the online service.

If online services are used, but safety risks arise. This should therefore be prohibited in principle. Remote maintenance via online services should be prevented by technical measures. If a general prohibition is not possible in individual cases, the use should be limited to a minimum and only for clearly defined areas of application with strict regulations.
For online services for remote maintenance, the IT systems of the remote maintenance administrator and the administrator each connect to a service provider on the Internet. It is not recognizable by the remote maintainer what happens with this information to the service provider or what intervention options exist there. Content could be recorded or manipulated. This applies z. As well as for keystrokes (eg passwords).

Often, the remote attendant's clients automatically start the service and connect to the online service. If this is the case, anyone who knows the access data (often only an ID and PIN) unobserved and unnoticed access to the Clients.It should be forbidden that clients can automatically connect to online services, this should also be technically prevented become.

The advantage of online services is that z. B. remote maintenance can be initiated quickly in an emergency, because the participants no special infrastructure is necessary. In this case, however, it is necessary to specify in advance exactly in which cases and under what conditions online services are permitted for remote access. These must be documented and agreed in advance with the ISB and the data protection officer of the institution.

The regulations should z. B. include the following items:

* It should be specified in which cases a remote maintenance via online services is allowed. For example, in the case of defined emergencies or to avert immediate danger to service operation, it may be necessary to resort to remote maintenance via online services.
* It must be regulated how and by whom the use of online services is authorized. In doing so, the existing reporting channels should be observed for the individual case.
* Automatic connection establishment should be prohibited. The connection must be released in individual cases by the IT system to be monitored.
* For each connection new access data must be generated (eg new PIN).
* The access data must not be transmitted in clear text (eg only verbally, encrypted).
* In a connection via an online service, passwords or other confidential information may not be displayed or entered locally. A "whitelist" can be used to describe which information may be transmitted.
### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "remote maintenance".

#### OPS.2.4.M6 Creation of a guideline for remote maintenance [IT operation]

It must be decided whether the aspects of remote maintenance are to be supplemented in existing directives or whether a separate guideline is to be drawn up. If a separate guideline is to be created, the existing guidelines of the institution should refer to the guideline for remote maintenance. Based on the general security policy of the institution, the essential core aspects for remote maintenance should be specified. The directive must be known to all those involved in the design, construction, operation and disposal, and be the basis for their work. The implementation of the content required in the directive should be reviewed regularly and the results should then be meaningfully documented. The guidelines within the guideline should be stringent in order to carry out later risk assessments or risk assumptions. If cryptographic communication is required for remote maintenance, the requirements of the block * CON.1 crypto concept * must be taken into account.

#### OPS.2.4.M7 Documentation for remote maintenance [IT operation]
There must be current documentation of remote maintenance. Existing deputies must be able to take over the tasks and processes at any time with the help of the remote maintenance documentation. For this reason, it is advisable to use a uniform naming concept for the IT systems of the institution for larger infrastructures in order to increase transparency and optimize work processes through targeted access.

Since the documents, z. If, for example, work instructions for the initiation of a remote access, usually contain confidential information and data, they must be stored securely in suitable locations and also be available in the context of emergency management. Likewise, they must be protected against unauthorized access. All remote access options must be recorded and documented, unless they are standard procedures according to the operating system standard. In the asset management of the institution, the systems and their interfaces should be stored for remote administration. For the emergency management and the recovery plan, the internal and external contact persons of the systems should be deposited.

The general documentation of the administrative processes for the various IT components should take the form of operating manuals. The operating manual for the respective system, which is to be administered remotely, must contain an indication of which system is allowed to access it, which rights and which organizational unit it can access.

Within the remote maintenance processes, the following documented information is accessed:

* The current documentation of all existing IT systems and their configuration and, if applicable, the name concept of the IT systems,
* The documentation of the users set up on the respective IT systems and their rights profiles,
* The newly added hardware and software components in the system documentation,
* The documentation of all security-related processes such as data backup or the destruction of data carriers,
* Descriptions of all found and fixed bugs.
#### OPS.2.4.M8 Secure protocols for remote maintenance [IT operation]

Only current and safe communication protocols should be used for remote maintenance. The communication should be encrypted. The recommendations of the BSI from the technical guideline (TR-02102) "Cryptographic methods: Recommendations and key lengths" should be taken into account when selecting the protocols and algorithms. To ensure that the protocols used are managed appropriately and the security requirements are taken into account, information on vulnerabilities from the trade press or relevant sources must be observed and continuously updated.

Tunnel administration can be secured by an SSH tunnel, SSL tunnel or IPSec tunnel. An adequate tunneling method should be selected based on the institution's protection needs. Of course, this must also be supported by the IT systems used.

To use the following protocols, we recommend using the respective versions:

* Use of SSH version 2
* Use of TLS 1.2
* Using SNMP from version 3
* Using IPsec with IKEv2 and ideally certificates
In the case of increased protection requirements, an independent user account should be set up for read, write and send access for SNMP Version 3.

All occurring syslog and event messages in the context of remote maintenance must be processed according to the logging and monitoring specifications of the institution.

#### OPS.2.4.M9 Selection of suitable remote maintenance tools [IT operation]
The selection of suitable remote maintenance tools is based on the operational, safety and data protection requirements of the institution. The selection and evaluation of the remote maintenance tools in question should be determined by means of a requirement analysis and subsequent risk assessment. All procurement decisions should be coordinated with the purchasing department, the system and application manager and the security management. Here also the staff representation should be involved.

The remote maintenance tools should meet the security requirements of the institution, taking into account the protection needs to be met. This results in particular demands on the cryptographic mechanisms. Likewise, data transmission should take into account connection quality and system utilization. For all other functions, the aspects from * OPS.2.4.M1 Planning the use of remote maintenance * should always be taken into account.

After considering the functions of the remote maintenance tools, the assistance and support services should finally be checked. It should be possible to ask questions and problems to the manufacturer or publisher. This should have support with multi-level escalation and prioritization.

#### OPS.2.4.M10 Management of remote maintenance tools [IT operation, users]

Since remote maintenance tools enable a variety of different functions, organizational management processes for dealing with the selected tools must be established. There must be an operating manual for the suitable handling of the remote maintenance tools for the IT operation. Sample procedures for passive and active remote maintenance must be created and communicated for use within the institution. In order to minimize possible security gaps resulting from misconfiguration and operating problems, IT operations must be sensitized and trained in the use of remote maintenance tools. An application manager must be named who serves as the point of contact for all technical questions about the remote maintenance tools.

** Administration requirements **

* The permissions of the administrators should be assigned according to the minimum principle. If administrators change their responsibilities and responsibilities, the permissions must be adjusted in a timely manner.
* The existing processes of authorization assignment and authorization withdrawal of the institution must be adapted accordingly for remote maintenance.
* The instructions for remote maintenance should specify what exact purposes are foreseen and which available resources should and may be used.
The required authorizations and identities for the remote maintenance of systems and applications should be integrated into the established identity and authorization management.

** Specifications for the processes of remote maintenance **

* For the operation of remote maintenance tools, specifications and procedures must be specified. For example, it should be determined who may access the tools and where changes may be made. This should be documented in the form of a process diagram.
* The remote maintenance tools must be included in the process of remote maintenance itself and in patch and change management, if they are not already part of the operating system.
#### OPS.2.4.M11 Use of cryptographic processes for remote maintenance [IT operation]
For remote maintenance, cryptographic methods (signatures and encryption methods) must be used in order to secure communication on the one hand and secure authentication on the other hand. Sufficiently strong cryptographic methods for encryption or signature within the remote maintenance must be used. The strength of the cryptographic methods and keys used must be checked regularly in the context of remote maintenance and adjusted if necessary. The used cryptographic procedures are to be kept up to date on the basis of the internal specifications and the recommendations of the BSI. The general requirements and measures are covered by the recommendations of the module * CON.1 crypto concept * and also apply to the use of remote maintenance procedures.

#### OPS.2.4.M12 Patch and Change Management for Remote Maintenance [IT Operations]

All updates, patches, and other changes to IT systems and applications running on them remotely are subject to the organization's patch management and change management policies.

In addition, the requirements of the module OPS.1.1.3 Patch and Change Management should be observed.

#### OPS.2.4.M13 Data backup for remote maintenance [IT operation]

To avoid data loss within the infrastructure for remote maintenance, backups must be carried out regularly for them. It is necessary to make specifications for the remote maintenance backup * * based on the amount and importance of the newly stored data and possible damage to the institution if this data is lost. The requirements must correspond to the patch and change management of the institution.

A person responsible for the execution and monitoring of the data backups as well as for the recovery exercises must be named. This must handle error messages related to backups and manage disk space resources.

The backup requirements of the remote maintenance must correspond to the general specifications of the institution for data backup and should consider the following criteria:

* Time intervals (eg daily, weekly, monthly),
* Times (eg at night, on Fridays in the evening),
* the number of generations to be preserved,
* the volume of data to be backed up,
* the storage media (depending on the amount of data),
* the previous deletion of the data carriers before reuse (eg for tapes or cassettes),
* the responsibility for the execution of the data backup,
* the responsibility for monitoring the backup, especially in the case of automatic execution (eg error messages, remaining space on the storage media),
* the documentation of the created backups (date, type of execution of the backup as well as selected parameters, labeling of the data carriers)
#### OPS.2.4.M14 Dedicated systems for remote maintenance [IT operation]

Within the remote maintenance components should be used, which serve exclusively for this purpose. All other features and services should be disabled. Implementing the minimal principle automatically reduces the potential attack surface that attackers could use to compromise. The dedicated IT systems thus provide their performance and resources (eg RAM, CPU capacity, hard disk space) only for the necessary purpose. The remote maintenance components should be securely configured and operated with the latest operating system and application software versions.

#### OPS.2.4.M15 Securing remote maintenance [IT operation]
Direct administrative access to IT systems and applications over public networks should, in principle, be prohibited and prevented. The remote maintenance should only take place from the internal network (eg institution location) via a coupling server. A docking server (also known as a Jump Server) is a dedicated hardened IT system that is used to manage devices in separate security zones. In the case of access via the public network, this system should be located in a so-called demilitarized zone (DMZ) of the firewall. So that the transferred information can not be intercepted or even manipulated, the administration may only take place via secure protocols (for example, via SSH and HTTPS).

When accessing via the public network, the remote maintainer only has the option of establishing an SSH or VPN tunnel (see NET.3.3 VPN) for the dedicated system. Only after successful authentication does an administrator from the internal network open a corresponding tunnel between the maintenance object and the coupling server, thus establishing a continuous connection between the remote maintenance person and the maintenance object (Rendezvous principle). The protocols and algorithms used should comply with the recommendations of the BSI and the internal cryptographic specifications of the institution.

Further requirements for the use of VPN are described in the block * NET.3.3 VPN *.

#### OPS.2.4.M16 Training for remote maintenance [IT-Betrieb]

The administrators should be given sufficient knowledge in dealing with the remote maintenance components. These training measures should be integrated into the already established procedures of the institution.

Within the awareness-raising and training activities, the basics, concepts and peculiarities of remote maintenance as well as knowledge of relevant commands for setting up, changing and deleting settings within the tools should be trained. The training should be regular, z. B. once a year, or take place if necessary. All awareness-raising and training should be documented.

Important aspects in the planning of the sensitization and training of administrators of the remote maintenance are:

* Analysis of target groups for awareness-raising and training programs
* the planning of training content (eg requirements for remote maintenance on the basis of this implementation note, laws, internal regulations)
* Measurement and evaluation of learning success
* Announcement of contacts on security issues
The topics of the training must be adapted according to the purpose of the tool. The following or a combination of several subject fields can be content of the training:

* Use as part of problem and incident management
* Use in the context of emergency management
* Use in security incident treatment
* Awareness of employees:

 
+ in dealing with passwords
+ in dealing with the remote maintenance tool
+ in the implementation of the requirements regarding the use of cryptographic methods
+ the use of secure protocols
+ the rights and roles concept
+ in the procedure and operation of the remote maintenance infrastructure and its tools
+ regarding the dependent procedural interfaces as well as application interfaces
+ the execution of data backups


 
The employees must be informed about what they have to consider in the remote maintenance. When IT systems are remotely administered by employees, they must explicitly agree to remote maintenance, such as: B. via an appropriate confirmation on the system. In addition, they must observe all activities during remote maintenance.

#### OPS.2.4.M17 Authentication mechanisms for remote maintenance [IT operation]

Remote maintenance requires mechanisms for identification and authentication that meet the protection requirements. It should be used two-factor authentication.
The selection of the authentication method and the reasons that led to the selection should be documented. Existing authentication mechanisms of the institution may not be circumvented by remote maintenance. To facilitate the registration for remote maintenance, it is advisable to integrate this into an identity and authorization management system and its infrastructure.

#### OPS.2.4.M18 Password security for remote maintenance [IT operation]

If password-based authentication is used in remote maintenance, password rules should be defined, documented, and made known to administrators to ensure a minimum level of password quality. For remote maintenance, these password rules should be enforced technically. Since two-factor authentication procedures should be used for remote maintenance, the password-based authentication procedure alone offers only basic protection.

For password security within the remote maintenance processes, a software solution should be used that facilitates the handling of many different passwords and the creation of secure passwords. Because there are many different password manager applications, the selection of the application should be based on the following criteria:

* Current state of the art
* Complexity of generated passwords
* Distinguish as needed between On and Offline Password Manager
* Password Manager with two-factor authentication
* Security options (eg automatic log-off)
#### OPS.2.4.M19 Remote maintenance by third parties [IT operation]

There can be various reasons why remote maintenance should be carried out by third parties. For example, remote maintenance may be part of the agreed services of device manufacturers. It may also lack the necessary resources or expertise internally.

Remote maintenance by third parties is particularly critical. Should it be necessary in individual cases, the following points should be noted:

* In principle, remote maintenance by third parties should only be passive, so considerate.
* All changes made (eg the configuration settings, within the source code) should be documented. This documentation must be submitted to the remote-controlled institution.
* If technically possible, all activities should be monitored by third-party IT experts during administration. For example, in remote administration of a client via a graphical user interface, often all inputs and outputs on the IT system to be maintained can be displayed and recorded. Even if remote maintenance is used by third parties, because internally the know-how or the capacity is not available, the external maintenance personnel can not be left unattended. In case of ambiguity about the operations, the connection should be interrupted immediately or switched to viewing mode. After that, the questions can be clarified.
* It must always be possible to cancel the remote maintenance locally.
* If data or programs are created on the local IT system during maintenance, this must be clearly recognizable and comprehensible. For example, this may only be done in specially marked directories or under certain user identifiers.
* All remote maintenance operations must be recorded. At least the beginning and the end of the remote maintenance as well as the participants are to be noted. If no one can observe the remote access on the maintained IT system, all activities involved in performing the remote maintenance must be recorded on the IT system to be maintained.
* For the external maintenance personnel contractual arrangements must have been made, above all about the secrecy of data (confidentiality agreements). In particular, it should be stipulated that data stored externally during maintenance should be carefully deleted after completion of the work. Likewise, the duties and responsibilities of the external maintenance personnel must be carefully defined.
If more protection is required, the following measures should also be taken:

Before selecting a remote maintenance partner, information about its reliability and further information should be obtained. As part of operational, safety, data protection and emergency cooperation arrangements, for example, the requirements for the service level agreements (SLAs) to be fulfilled should be transferred. In addition, voting should be taken regarding the network segmentation and separation requirements to be met, as well as the expected protection mechanisms for the clients and the underlying operating systems. The institution should establish contractually agreed control mechanisms of the agreed services with the service provider.

With regard to identity and authorization management, when selecting the remote maintenance service provider, the latter must never receive more rights than is absolutely necessary for the performance of his tasks and each service provider employee must authenticate himself via a unique, personalized user ID.

As the institution, as a service user, has no direct influence on the operation of the service provider and its staff, any potential negligence or unreliability may give rise to uncontrollable risks. In order to minimize these risks, contractual arrangements should be designated for at least the following topics:

* Joint risk management through the close integration of the service provider's remote maintenance systems with the institution's systems
* Security incident detection and handling
* joint emergency management including the naming of the Business Impact Analysis values ​​(BIA values)
* a confidentiality agreement,
* Definition of competences and duties
* Specifications regarding backup and archiving requirements
* a detailed description of how the service provider's IT systems are protected,
* Definitions around the possibility of auditing
* Determinations for the purpose of integration into the monitoring and logging infrastructure of the institutional sites
* Transfer or confirmed destruction (annihilation declaration) of the backup and archiving data in the context of remote maintenance after termination of the contract
Further information on the operation of remote maintenance by third parties is described in the modules OPS.2.1 Outsourcing Usage and OPS.3.1 Outsourcing Providers.

#### OPS.2.4.M20 Operation of remote maintenance [IT operation]

To ensure the operation of the IT systems and applications through remote maintenance, the initiative to set up a support or remote maintenance session should always be based on the users of the IT components being managed. Since these work directly with the IT systems and applications, a notification process for support and remote maintenance requests should be established (eg ticket system). All access by remote maintenance should only be permitted after successful authentication.

The security infrastructure releases required to establish the remote maintenance access should be integrated into the established firewall rule processes. The integration of remote maintenance into the security infrastructure should take into account all the information in the * NET.3.2 Firewall * block.
A remote maintenance service provider should not have access to IT systems and applications outside of those required for the respective remote maintenance. In order to ensure that only authorized accesses by administrators are possible, the communication between remote maintenance server and client should be verified by means of a stateful firewall, better a firewall NG.

In addition, it should be considered to implement further functionalities on the IT system to be maintained:

* If remote maintenance by third parties is not monitored: Disabling remote maintenance in normal operation and explicit release for a precisely defined period of time,
* Limitation of the rights of the administrators: The administrators should not have the full administrator rights. A graded rights administration should be realized. The administrators should only have access to the data and directories that are currently affected by the remote maintenance.
* If the session is interrupted without the intervention of the administrators, resumption of the connection should precede a re-authentication.
In addition, the following instructions should be observed.

All remote maintenance operations must be recorded. At least the beginning and the end of the remote maintenance as well as the participants are to be noted. If no one can observe the remote access on the maintained IT system, all activities involved in performing the remote maintenance must be recorded on the IT system to be maintained. The resulting log data should be evaluated regularly.

If Security Information and Event Management (SIEM) exists, the security incident verification log data should be sent to it.

After a defined number of failed attempts, a temporary lock on access to remote maintenance should be activated. In contrast to conventional IT, with regard to the special requirements of remote maintenance with regard to availability, such blocks must be made, for example, not after twenty, but already after three failed attempts.

A successful DoS or DDoS attack equates to an invitation to further attacks on the IT systems of the institution and participating service providers. For this reason, mechanisms for detection and defense against high-volume attacks, TCP state exhaustion attacks, and attacks at the application level should be implemented. Possible actions against this type of attack are not part of these implementation notes, but are described in the Implementation Considerations of the * NET.3.1 Router / Switches * and * NET.3.2 Firewall * blocks.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### OPS.2.4.M21 Creating a contingency plan for remote maintenance failure (A)

In the context of emergency preparedness, a concept should be developed to minimize the consequences of failure of remote maintenance components and what to do in case of failure. The emergency plan should ensure that malfunctions, damage and consequential damage are minimized, and that timely restoration of normal operation takes place. In the case of high availability, the infrastructure of the remote maintenance should be checked for criticality by means of a business impact analysis.

Further aspects of emergency planning are dealt with in the block in the module * DER.4 Emergency Management *.

#### OPS.2.4.M22 Redundant use of mobile communication networks (A)
For the protection of the communication networks of the remote maintenance with high availability requirements redundant connection or communication networks should be established. It should be regulated whether external telecommunication networks should be used for this, eg. B. via mobile.

In addition to the established productive channels, the internal IT systems of the institution should also be accessible via a non-productive fallback access network. The fallback access could be realized for example via a DSL or LTE connection or by a landline connection.

#### OPS.2.4.M23 Planning the Safe Use in a Secure Network Segment [IT Operations]

A secured network segment should be used for the remote maintenance, this should be implemented and operated in the manner of a * Demilitarized Zone * (* DMZ). *

In the area of ​​remote maintenance, all remote maintenance components should preferably be located in the secure network segment and not be located directly in the internal network. This can protect the spread from a non-intrusive network to the network with the remote maintenance system, with appropriate analysis tools and tools in between.

The remote maintenance access should not result in circumventing existing security infrastructures, thus merging trusted and untrusted networks.

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Additional information on hazards and safety measures in the area of ​​"remote maintenance" can be found in the following publications, among others:

* #### [CSE108] Remote maintenance in the industrial environment

  

 BSI Cyber ​​Security Publication - Alliance for Cyber ​​Security, CSE 108, BSI, Version 1.0, 01.2015
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_108.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_108.pdf)

 
* #### [CSE54] Basic rules for securing remote maintenance access

  

 BSI publication on cyber security alliances for cyber security, BSI, 06.2013
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_054.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_054.pdf)

 
* #### [TR02102] Cryptographic method recommendations and key lengths

  

 BSI, (last accessed on 27.09.2017)
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)
