1 description
--------------

### 1.1 Introduction

Remote maintenance refers to spatially separate access to IT systems and the applications running on them for configuration, maintenance, repair or control purposes. Remote maintenance can be done passively through an exclusive access to the IT system or applications, or actively through direct administrative intervention in the operating system or running applications. In the case of passive remote maintenance, a user on site must perform the actual actions under the guidance of an administrator. In the case of active remote maintenance, on the other hand, an operating system is intervened and operated directly by an administrator. Among other things, the signals of a mouse and keyboard commands, as well as screen contents and console outputs are transmitted. Even if effective mechanisms for securing remote access access are implemented, there is direct access from outside to the internal network and data processed therein. Through these interfaces, external parties can endanger the institution and thus cause economic and operational damage.

### 1.2 Objective

The aim of the module is to protect information stored, processed and transmitted based on remote maintenance. For this purpose, requirements are made for the remote maintenance, which relate to functions of active and passive remote maintenance.

### 1.3 Delimitation

This module looks at remote maintenance from the point of view of IT operation and provides advice for users on how remote maintenance can be used. The holistic guarantee of information security in all life cycle phases is important. The security aspects of the communication connections used, authentication mechanisms and the protection of the remote maintenance access are important components of the module. In the context of the component "remote monitoring", not all relevant aspects of the related business processes are covered. Therefore, especially aspects of the blocks * OPS.1.1.3 Patch and Change Management *, * ORP.3 Sensitization and Training, CON.1 Crypto Concept * and CON.3 * Data Backup Concept * must be guaranteed separately. Likewise, the specifications of the component layers NET (networks and communication), DER (detection & reaction), the components of the layer * OPS.2 IT operation of third parties * and the components of the layer * OPS.3 IT operation for third parties * have been implemented which are directly related to remote administration. For cloud-based products, the building block * OPS.2.2 cloud usage * must be taken into account. Likewise, the Remote Procedure Calls of Windows 2010 are not part of this document.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the field of remote maintenance:

### 2 1 Inadequate knowledge of remote maintenance regulations

If the parties know insufficiently about important regulations and therefore do not apply them, the protection of the information in the context of a remote maintenance is endangered. Therefore, there are dangers for the IT operation, if current regulations are not made public. In particular, administrators who set up and use remote maintenance, are on regulations, eg. As to configurations, instructed, otherwise with the remote maintenance additional operational risks, but also security gaps to the internal network arise and attacks on the remote maintenance can not be detected or fended off.

### 2 2 Missing or inadequate planning and control of remote maintenance
If remote maintenance is not carefully planned, set up and regulated, not only the security of an IT system but of all IT systems of an institution can be impaired if security gaps are exploited. Vulnerabilities can arise in many places and affect communication protocols, patching processes, encryption algorithms and authentication mechanisms. Inadequately secured remote maintenance interfaces can also compromise a linked network of a third party.

### 2 3 Unauthorized exercise of rights in remote maintenance

Access, access and access permissions tailored to each task are used to protect information, business processes and IT systems from unauthorized access. If such authorizations are granted to unauthorized persons during remote maintenance, or if rights are exercised unauthorized remotely, a large number of threats to the confidentiality and integrity of data and the availability of such data may arise. B. of computing power. Possible damage scenarios include, for example, the introduction of malicious software, the manipulation of data and information, and the unauthorized gathering of information. Impact can z. For example, financial and knowledge losses, physical destruction of physical assets and compromises of IT systems and networks.

### 2 4 Unsuitable use of authentication for remote maintenance

In the remote maintenance authentication mechanisms are used, which are based on a user management with stored authentication data. If unauthorized third parties gain administrative authorizations on remote maintenance computers or for remote maintenance tools, the institution may incur far-reaching damage. These include z. These include unauthorized configurations of IT systems and applications, compromises, and information and data loss.

### 2 5 Insecure and uncontrolled establishment of communication links

For remote maintenance, access to communication interfaces of the administered computer is generally required. This always includes a potential hazard.

Likewise, communication interfaces of IT systems are not always obvious to the user, which is additionally transmitted in addition to user and protocol information. A manipulated or even activated communication interface may under some circumstances be established without initiation by a user to connect to a remote station or be addressed by a third party to a function not known to the user.

### 2 6 Faulty remote maintenance

Ensuring the security and viability of remote-access IT systems and applications requires professional and ongoing remote maintenance. If these IT systems and applications are not properly configured, maintained, repaired, and monitored remotely, they can not be used at worst. If errors occur within the remote maintenance processes, malfunctions of individual operating system functions can result directly from this. In addition, late or faulty IT system maintenance can cause security vulnerabilities.

### 2 7 Use of unsafe protocols in remote maintenance

Communication via public and internal networks via insecure protocols poses a potential danger. For example, if legacy versions of IPSec, SSH, or SSL / TLS are used to establish a tunnel between two endpoints or networks, the security of these tunnels can not be adequately ensured. Attackers can exploit vulnerabilities in these protocols to inject their own content into protected connections. Generally considered to be unsecure protocols, where information is transmitted in plain text.

### 2 8 Inappropriate handling of authentication procedures for remote maintenance
The security of an authentication process is directly dependent on the careful handling of it. The disclosure of user-supplied authentication data and the insecure storage of this information pose a potential danger. There may be security vulnerabilities for unauthorized access to the rights and role profiles of administrators as well as IT systems and applications.

### 2 9 Unsafe cryptographic algorithms for remote maintenance

There is a loss of security within the remote maintenance, if insecure cryptographic methods used or secret keys are not sufficiently protected. Negligence in the field of cryptographic algorithms can lead to compromises of cryptographic keys. In addition, attackers can more easily penetrate if they can analyze or break the cryptographic process with reasonable time and technical resources and then penetrate into the communication.

### 2 10 Insecure and uncontrolled external use of remote maintenance access

Unauthorized persons or third parties are allowed to use the components of the remote maintenance without a contractual basis, eg. If authorization concepts of the institution are bypassed or not carefully implemented, the security of remote maintenance, IT systems and applications is no longer guaranteed.

### 2 11 Use of online services for remote maintenance

In addition to remote maintenance, in which an administrator establishes a direct data connection to the institution to be administered, so-called online services can also be used. In this case, the IT systems to be administrated connect to the servers of a third-party provider and the administrators can access the IT systems to be administered via a web browser or similar.

Since the communication is not encrypted end-to-end and access takes place via a third party, the data exchange could be read directly. In addition, the IT systems could also be administered by unauthorized persons by changing the data connection. If the IT systems automatically establish a data connection to the online service at system startup and the access data are known, the IT system could be accessed directly.

In order to establish a connection to the online service, often no administrative rights are required on the IT systems to be administrated, the administrator then only needs one browser. Users without administrative rights can thus initiate remote access unauthorized.

3 requirements
---------------

The following are specific requirements for remote maintenance. Basically, the IT manager is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### OPS.2.4.A1 Planning the use of remote maintenance [IT operation]

The use of remote maintenance MUST be adapted to the institution and planned as needed in terms of technical and organizational aspects. It MUST be clarified whether in-band and / or out-band administration is used, which IT system interfaces and protocols are used. It MUST be clarified how the remote maintenance is secured and how it is audited.

#### OPS.2.4.A2 Secure connection setup for remote maintenance [user]
The initiation of the remote maintenance access MUST be done out of the institution. The user of the remote-managed IT system MUST explicitly consent to the remote access.

#### OPS.2.4.A3 Hedging communication links for remote maintenance [IT operation]

The possible accesses and communication interfaces for external connection MUST be limited to the necessary extent. Likewise, all communication connections MUST be disconnected after the remote access has been completed (deactivation). For remote maintenance, necessary ports MUST be constantly provided. It MUST be used, taking into account the required protection requirements of the IT system or the application of secure authentication mechanisms for the administrators.

#### OPS.2.4.A4 Regulations for communication connections [IT operation]

In compliance with the institution's firewall requirements, the remote maintenance MUST be integrated into the firewall rules. It MUST be ensured that existing firewall infrastructures and their regulations are not bypassed.

When checking network connectivity using ICMP, the regulations for local and remote testing MUST be followed.

#### OPS.2.4.A5 Use of online services [IT operation, users]

It MUST be decided if remote maintenance via online services is allowed. The use of online services for remote maintenance SHOULD be prohibited. Technical and organizational measures SHOULD be taken to enforce the ban.

If the use is unavoidable, it should be limited to as few cases as possible. The conditions under which remote maintenance via online services is allowed should be specified. The clients SHOULD NOT automatically connect to the online service.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of remote maintenance. They SHOULD be implemented in principle.

#### OPS.2.4.A6 Creation of a guideline for remote maintenance [IT operation]

The regulations for remote maintenance SHOULD be documented in a guideline. If a stand-alone policy is to be created, the institution's existing policies SHOULD refer to the Remote Maintenance Policy. The guideline SHOULD be known to all responsible persons, who are involved in the conception, the construction and the operation as well as the separation, and can form the basis for their work.

#### OPS.2.4.A7 Documentation for remote maintenance [IT operation]

There must be a current documentation of the remote maintenance. Existing representatives SHOULD be able to take over the tasks and processes at any time. Since the documents usually contain confidential information and data, they SHOULD be stored securely in suitable locations and also be available as part of emergency management. Likewise, the protection against unauthorized access to the documentation SHOULD be ensured. All remote access options SHOULD be recorded and documented.

#### OPS.2.4.A8 Secure protocols for remote maintenance [IT operation]

It SHOULD use current and considered secure communication protocols. The communication SHOULD be encrypted. Based on the protection needs of the institution, suitable cryptographic procedures for the realization of a tunnel SHOULD be used. In order to properly manage the protocols used and to take into account the security requirements, information on vulnerabilities in the specialized press or relevant sources SHOULD be observed and continuously updated.

#### OPS.2.4.A9 Selection of suitable remote maintenance tools [IT operation]
The selection of suitable remote maintenance tools SHOULD be based on the operational, safety and data protection requirements of the institution. All procurement decisions SHOULD be agreed with the person in charge of purchasing, the system and application manager and the security management.

#### OPS.2.4.A10 Management of remote maintenance tools [IT operation, users]

Organizational administrative processes for dealing with the selected tools SHOULD be established. There SHOULD be an instruction manual for handling the remote maintenance tool. Sample procedures for passive and active remote maintenance SHOULD be created and communicated. IT operations SHOULD be sensitized and trained in the use of remote maintenance tools. It SHOULD name a contact person for all technical questions about the remote maintenance tools.

#### OPS.2.4.A11 Use of cryptographic procedures for remote maintenance [IT operation]

Remote maintenance SHOULD use sufficiently strong cryptographic procedures to secure communications and authenticate administrators. The strength of the cryptographic methods and keys used SHOULD be regularly checked in the context of remote maintenance and adjusted if necessary.

#### OPS.2.4.A12 Patch and Change Management for Remote Maintenance [IT Operations]

The general requirements for patch and change management of the institution for remote maintenance SHOULD be implemented. The IT systems and administration tools SHOULD all be considered in patch and change management.

The remote maintenance accesses SHOULD be suitably activated and deactivated. All activations and deactivations of the remote maintenance access SHOULD also be documented. For security reasons, all IT systems and applications serviced by remote maintenance SHOULD be patched in a timely manner. Before patches and changes are imported into a production system by remote maintenance, they SHOULD be checked in advance in a suitably equipped test environment.

#### OPS.2.4.A13 Data backup for remote maintenance [IT operation]

To avoid data loss within the infrastructure for remote maintenance, regular backups SHOULD be made. The specifications of the remote backup data SHOULD be made based on the amount and importance of the newly stored data and the potential harm to the institution should this data be lost.

All data protection requirements of the remote maintenance SHOULD correspond with the general specifications of the institution for data backup.

#### OPS.2.4.A14 Dedicated systems for remote maintenance [IT operation]

Within the remote maintenance components should be used, which serve exclusively for this purpose. All other functions / services SHOULD be disabled. The components of the remote maintenance SHOULD be securely configured and set.

#### OPS.2.4.A15 Securing remote maintenance [IT operation]

Remote maintenance SHOULD only be done from the internal network.

However, if it is necessary to access internal IT systems from a public data network, a secure Virtual Private Network (VPN) SHOULD be used. For remote maintenance via VPN, a protected data connection to the VPN endpoint SHOULD be generated. In addition to these external remote access accesses, the internal remote maintenance access points SHOULD also be protected. The use of internal remote maintenance access SHOULD be restricted as much as possible. Furthermore, all activities SHOULD be logged during an administration session.

#### OPS.2.4.A16 Training for remote maintenance [IT operation]

The administrators SHOULD be provided with sufficient knowledge in dealing with the remote maintenance components. These training courses SHOULD be integrated into the already established procedures of the institution.
Likewise, the employees SHOULD be informed about what they have to consider in the remote maintenance.

#### OPS.2.4.A17 Authentication mechanisms for remote maintenance [IT operation]

For remote maintenance, two-factor authentication methods SHOULD be used.

The selection of the authentication method and the reasons that led to the selection SHOULD be documented. To facilitate the registration in the remote maintenance SHOULD be integrated into an identity and authorization management and their infrastructures.

#### OPS.2.4.A18 Password security for remote maintenance [IT operation]

If password-based authentication is used during remote maintenance, password rules SHOULD be defined, documented and made known to the administrators. For remote maintenance these password rules SHOULD be enforced technically.

#### OPS.2.4.A19 Remote maintenance by third parties [IT operation]

If it is not possible to dispense with external remote maintenance, all activities within this framework SHOULD be monitored by Internal. All remote maintenance operations by third parties SHOULD be recorded. With external maintenance personnel contractual arrangements MUST be made, above all about the security of the affected IT systems and information. The duties and responsibilities of the external maintenance personnel SHOULD be contractually established.

#### OPS.2.4.A20 Remote maintenance operation [IT operation]

A reporting process for support and remote maintenance issues should be established (eg ticket system). All access by the remote maintenance SHOULD only be permitted after successful authentication.

The security infrastructure releases required to establish remote maintenance accesses SHOULD be integrated into the established firewall rule processes. It should be implemented mechanisms for detection and defense against high-volume attacks, TCP state exhaustion attacks and attacks at the application level.

All remote maintenance operations SHOULD be recorded. The resulting log data SHOULD be evaluated regularly.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### OPS.2.4.A21 Create a contingency plan for remote maintenance (A)

In the context of emergency preparedness, a concept SHOULD be developed to minimize the consequences of failure of remote maintenance components and what activities should be carried out in the event of a failure. The emergency plan SHOULD ensure that faults, damage and consequential damage are minimized, and that timely restoration of normal operation takes place.

#### OPS.2.4.A22 Redundant use of mobile communication networks (A)

For the protection of the communication networks of the remote maintenance with high availability requirements, redundant connection or communication networks SHOULD be established.

#### OPS.2.4.A23 Planning the Safe Use in a Secure Network Segment [IT Operations]

For remote maintenance, a secured network segment SHOULD be used. This SHOULD be realized and operated in the manner of a Demilitarized Zone (DMZ). The remote maintenance accesses SHOULD NOT result in circumventing existing security infrastructures, thus merging trusted and untrusted networks.

4 Further Information
------------------------------

### 4.1 Literature
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

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "Remote maintenance".

* G 0.9 Failure or malfunction of communication networks
* G 0.14 Spying out information (spying)
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.43 Importing messages
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
