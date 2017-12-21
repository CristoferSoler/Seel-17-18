1 description
--------------

### 1.1 Introduction

* Samba * is a freely available and fully-featured Active Directory Domain Controller (ADDC) that can provide authentication, file and print services, enabling interoperability between the Windows and Unix worlds. * Samba * brings together many different protocols and techniques. These include, for example, the * Server Message Block (SMB) * protocol, also known by the newer name * Common Internet File System * (CIFS). * Samba * servers are servers on which * Samba * is operated. In general, these are the Linux server.

* Samba * has been properly designed and neatly configured, the application interacts with a Windows client or server as if it were a Windows system itself.

### 1.2 Objective

The goal of the module is to show how * Samba * can be used safely in institutions and how the information provided by Samba can be protected.

### 1.3 Delimitation

This module considers * Samba * as an authentication, file and print service. Since * Samba * is generally used on Linux servers and represents services known from the Windows server world, the security aspects of the blocks SYS.1.1 * General Server * and SYS.2.1 * Server under Linux * must be taken into account. Security requirements for printers, file servers or directory services, on the other hand, are not part of this module but are described in the blocks SYS.4.1 * Printers, Copiers and Multifunction Devices *, APP.2.1 * General Directory Service * and APP.3.6 * DNS Server * and APP.2.3 * OpenLDAP *, even if the * Samba * internal DNS and LDAP services are used. Furthermore, due to the * Samba * functions, the components APP.3.3 * Fileserver * and APP.2.2 * Active Directory * have to be considered.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in * Samba *:

### 2 1 Listening to unprotected communications from Samba

When attackers hear unprotected * Samba * communication links, information can be intercepted and abused. When transferring files between Linux servers, Windows servers and clients, protocols are often used without extensive security features, so that both authentication and user data are accessible to third parties and could be misused by unauthorized persons. This can lead to valuable information flowing from the institution.

### 2 2 Incorrect logging in Samba

Improperly designed or missing logging in * Samba * can lead to security problems. Without proper logging, errors or attacks go undetected and preventive measures and early warning system indicators can not be defined.

### 2 3 Incorrect emergency preparedness in Samba

Also deficits in the emergency preparedness can lead to longer downtime of * Samba *. For example, after a successful attack, a necessary reinstallation may be delayed if installation packages are not available. Existing installation packages, in turn, can produce undesirable results if you have not used versioning of the configuration files or if the * Samba * server compilation and installation options are not kept.

### 2 4 Missing adaptation of Samba
To show some capabilities of the * Samba * server and to give administrators a quick start, the configuration file * smb.conf * is created with default settings during the installation of the * Samba * server. With the options preset in this file, the * Samba * server can be started afterwards. If this file is thoughtlessly used without further settings, this can lead to considerable security gaps. However, even if the file is modified, errors may occur that may result in the disclosure of sensitive information or compromise the security, availability, and performance of * Samba * server services.

### 2 5 Software vulnerabilities or errors in Samba

* Samba * is free software that is created and developed within a community. A consistent quality of the source code can not be guaranteed. This can lead to software vulnerabilities or failures and thus to serious security vulnerabilities in the application or all connected IT systems. Attackers can use such vulnerabilities for various attacks. For example, to infiltrate malicious software and thus possibly gain unauthorized access to sensitive information, such as confidential data or documents and access data. Furthermore, attackers can manipulate IT systems via security vulnerabilities, which can cause them to be inoperable or malfunctioning.

### 2 6 Unauthorized use or administration of Samba

Unauthorized persons may gain access to confidential information, manipulate it or cause malfunctions through the use of applications or systems, so that they * can administer * Samba * without authorization. It is particularly critical if configuration tools such. For example, the * Samba Web Administration Tool * (SWAT) can be used. SWAT was an integral part of * Samba * until version 4, but was prioritized little by * Samba * developers. Therefore, weaker or no security mechanisms were implemented, for example, HTTPS was not supported.

### 2 7 Incorrect administration of Samba

If administrators are not familiar enough with * Samba *'s extensive features, components, options, and configuration settings, it can lead to far-reaching complications. For example, misconfiguration of DNS or of user and rights management can lead to unauthorized access to resources. Furthermore, this can lead to business interruptions or protect information can be disclosed.

### 2 8 Malicious programs around Samba services

If * Samba * is used as a file server on Linux systems, then the server itself is not directly susceptible to Windows malware. These can however be contained in infected files that are stored on them. Through the * Samba * system these infected files are then provided to all connected Windows clients and thus actively disseminated.

### 2 9 Data loss at Samba

Data loss has a significant impact on IT use. If business-relevant information is destroyed or falsified, business processes and specialist tasks can be delayed or even stopped. For example, * Samba * notes that the file system properties of Windows and Unix are significantly different. Therefore, it is not always guaranteed that access rights will be maintained under Windows. It can also cause information on * Alternate Data Streams * (ADS) and DOS attributes to be lost.

### 2 10 Integrity loss of sensitive information at Samba
If information is no longer integer, it can lead to many problems. In the simplest case, information can then no longer be read, so it can no longer be further processed. * Samba * itself stores important operating data in * Trivial Database * (TDB) format databases. If these databases are not adequately and consistently handled by the operating system, they can cause problems when * Samba * services are used.

3 requirements
---------------

The following are specific requirements for the * Samba * area. Basically, IT operations are responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### APP.3.4.A1 Planning the use of a Samba server [Head IT]

The introduction of a * Samba * server MUST be carefully planned and regulated. Depending on the application scenario, it is necessary to define which tasks the * Samba * server should fulfill in the future, in which operating mode it is operated and which components of * Samba * and which other components are required for this.

If the cluster solution CTDB (Cluster Trivia Data Base) is used, the introduction of Samba MUST be carefully conceptualized. If * Samba * is also to provide the Active Directory (AD) services for Linux and Unix systems, the deployment MUST be carefully planned and the installation tested. Furthermore, the authentication process for the AD MUST be carefully designed and implemented. The introduction and the order in which the Stackable Virtual File System (VFS) modules are executed MUST be carefully designed and the implementation documented.

If IPv6 is used with Samba, this too MUST be carefully planned and also checked for error-free integration in a close-to-operational test environment.

#### APP.3.4.A2 Secure basic configuration of a Samba server

Once the * Samba * server has been installed, the service MUST be securely configured. For this purpose, settings for the access controls, but also settings affecting the performance of the server MUST be adapted. It MUST be ensured that the access permissions for each user are determined individually.

In general, it MUST be ensured that only selected users and user groups are allowed to connect to the * Samba * service and that users can only access the information within their shares.

* Samba * MUST be configured to receive connections only from secure hosts and networks and connect only to secure network addresses. Changes to the configuration SHOULD be carefully documented so that it can be understood at any time who changed what for what reason. It must be checked after each change, if the syntax is still correct.

Additional software modules, such as SWAT, MUST NOT be installed.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of Samba. They SHOULD be implemented in principle.

#### APP.3.4.A3 Secure configuration of the operating system for a Samba server

Databases in Trivial Database (TDB) format SHOULD NOT be stored on a partition that uses ReiserFS as the file system. If a * netlogon * share is configured, unauthorized users SHOULD NOT be able to modify files in this share.
The operating system of the * Samba * server SHOULD support Access Control Lists (ACLs) in conjunction with the file system used. In addition, it should be ensured that the file system is integrated with the appropriate parameters.

The default settings of * SMB * * Message Signing * SHOULD be retained, provided that they do not contradict the existing security guidelines in the information network. Using a local packet filter SHOULD block ports over which the * Samba * server should be unreachable.

It SHOULD * Kerberos * be used to avoid the shortcomings of NT LAN Manager (NTLM) or NTLMv2 as well as an excessive network load. If authenticated with * Kerberos *, the central time server SHOULD be installed locally on the domain controller. The NTP service SHOULD be hardened so that only authorized clients can query the time.

#### APP.3.4.A4 Securing the NTFS properties on a Samba server

If a version of * Samba * is used that can not map so-called * Alternate Data Streams * (ADS) in the * New Technology File System * (NTFS), it should be ensured that file system objects do not contain ADS with important information before they reach beyond system boundaries copied or moved away.

#### APP.3.4.A5 Secure configuration of access control for a Samba server

The default parameters used by * Samba * to map DOS attributes to the Linux file system SHOULD NOT be used. Instead, * Samba * SHOULD be configured to store DOS attributes and the status indicators for inheritance (flag) in * Extended Attributes *. The shares SHOULD only be managed via the registry.

Furthermore, the effective access permissions to the shares of the * Samba * server, as well as the log files, SHOULD be checked regularly.

#### APP.3.4.A6 Secure configuration of Winbind under Samba

The use of * Winbind * SHOULD be carefully planned and regulated. For each Windows domain user, a user account with all group memberships SHOULD exist in the server's operating system. If this is not possible, * Winbind * SHOULD be used. In doing so, * Winbind * SHOULD implement domain usernames into unique Linux usernames. It should be noted that collisions between local Linux users and domain users are prevented.

Furthermore, the PAM (* Pluggable Authentication Modules *) SHOULD be integrated.

#### APP.3.4.A7 Secure configuration of DNS under Samba

If * Samba * is used as a DNS server, the introduction should be carefully planned and the implementation tested in advance.

Since * Samba * supports various AD integration modes, the DNS settings SHOULD be made according to the usage scenario of * Samba *. If * Samba * is used as the primary AD DC, the DNS service SHOULD be installed on the * Samba * server and carefully configured.

#### APP.3.4.A8 Secure configuration of LDAP under Samba

If the users are managed under * Samba * with LDAP, this should be carefully planned and documented. The access permissions to the LDAP SHOULD be governed by ACLs.

#### APP.3.4.A9 Secure configuration of Kerberos on Samba

For authentication, the Heimdal Kerberos Key Distribution Center * (KDC) implemented by * Samba * SHOULD be used. Care should be taken to use the * Samba * default Kerberos configuration file. Only enough secure encryption methods for Kerberos tickets should be used.

#### APP.3.4.A10 Secure use of external programs on a Samba server

Because external programs provide attack gates for attackers, * Samba * should only call audited and trusted external programs.

#### APP.3.4.A11 Secure use of communication protocols when using a Samba server
For a reliable network, only really needed protocols SHOULD be used on the Windows clients. If * Netware * systems need access to the * Samba * server, SHOULD consider that * Internetwork Packet Exchange * (IPX) is required. If IPv6 is used, special features should be considered.

#### APP.3.4.A12 Training the administrators of a Samba server

Administrators SHOULD address the specific areas of * Samba * used, such as: As user authentication, Windows and Unix rights models, but also to NTFS ACLs and NTFS ADS trained.

#### APP.3.4.A13 Regular backup of important system components of a Samba server

SHOULD include all system components required to restore a * Samba * server into the institution-wide backup concept. Also the account information from all used backends SHOULD be considered. Likewise, all TDB files SHOULD be backed up. Furthermore, the registry SHOULD be secured if it was used for shares.

The configuration data, status information and system files SHOULD be compatible with each other.

#### APP.3.4.A14 Create an Samba server outage disaster recovery plan

In order to be able to quickly reinstall the * Samba * server in an emergency, the necessary installation packages and information SHOULD be deposited at a specified location. It SHOULD be guaranteed that they are available at all times. The documentation of the * Samba * configuration SHOULD always be up to date and comprehensible.

For the * Samba * server SHOULD be tested depending on the server role and the availability requirements, whether it can be recovered and how long that takes. Based on the results, the emergency plan SHOULD be improved.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.3.4.A15 Encryption of data packets under Samba (CI)

To ensure the integrity and confidentiality of the data packets in the transport path, the data packets SHOULD be encrypted with the encryption methods integrated in SBM3.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and safety measures in the area of ​​"Samba" can be found in the following publications, among others:

* #### [SAMBA] Samba

  

 Opening Windows to a Wider World, SAMBA, (last accessed on 29.09.2017)
 <Https://www.samba.org/>

 
* #### [UBUNTU] ubuntuuser

  

 Wiki Samba, (last accessed on 29.09.2017)
 <Https://wiki.ubuntuusers.de/Samba>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Samba" building block.

* G 0.15 Listening
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.28 Software vulnerabilities or errors
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
* G 0.15 Listening
  * APP.3.4.A7 Secure configuration of DNS under Samba
  * APP.3.4.A9 Secure configuration of Kerberos on Samba
  * APP.3.4.A13 Regular backup of important system components of a Samba server
  * APP.3.4.A15 Encryption of data packets under Samba (CI)
* G 0.18 Missing planning or missing adjustment
  * APP.3.4.A1 Planning the use of a Samba server [Head IT]
  * APP.3.4.A10 Secure use of external programs on a Samba server
  * APP.3.4.A11 Secure use of communication protocols when using a Samba server
  * APP.3.4.A12 Training the administrators of a Samba server
  * APP.3.4.A13 Regular backup of important system components of a Samba server
  * APP.3.4.A14 Create an Samba server outage disaster recovery plan
  * APP.3.4.A15 Encryption of data packets under Samba (CI)
  * APP.3.4.A2 Secure basic configuration of a Samba server
  * APP.3.4.A3 Secure configuration of the operating system for a Samba server
  * APP.3.4.A4 Securing the NTFS properties on a Samba server
  * APP.3.4.A5 Secure configuration of access control for a Samba server
  * APP.3.4.A6 Secure configuration of Winbind under Samba
  * APP.3.4.A8 Secure configuration of LDAP under Samba
  * APP.3.4.A9 Secure configuration of Kerberos on Samba
  * APP.3.4.A10 Secure use of external programs on a Samba server
  * APP.3.4.A11 Secure use of communication protocols when using a Samba server
  * APP.3.4.A12 Training the administrators of a Samba server
* G 0.19 Disclosure of information worthy of protection
  * APP.3.4.A5 Secure configuration of access control for a Samba server
  * APP.3.4.A9 Secure configuration of Kerberos on Samba
  * APP.3.4.A13 Regular backup of important system components of a Samba server
  * APP.3.4.A15 Encryption of data packets under Samba (CI)
* G 0.28 Software vulnerabilities or errors
  * APP.3.4.A8 Secure configuration of LDAP under Samba
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.4.A7 Secure configuration of DNS under Samba
* G 0.31 Incorrect use or administration of devices and systems
  * APP.3.4.A1 Planning the use of a Samba server [Head IT]
  * APP.3.4.A10 Secure use of external programs on a Samba server
  * APP.3.4.A11 Secure use of communication protocols when using a Samba server
  * APP.3.4.A12 Training the administrators of a Samba server
  * APP.3.4.A13 Regular backup of important system components of a Samba server
  * APP.3.4.A14 Create an Samba server outage disaster recovery plan
  * APP.3.4.A15 Encryption of data packets under Samba (CI)
  * APP.3.4.A2 Secure basic configuration of a Samba server
  * APP.3.4.A3 Secure configuration of the operating system for a Samba server
  * APP.3.4.A4 Securing the NTFS properties on a Samba server
  * APP.3.4.A5 Secure configuration of access control for a Samba server
  * APP.3.4.A6 Secure configuration of Winbind under Samba
  * APP.3.4.A8 Secure configuration of LDAP under Samba
  * APP.3.4.A9 Secure configuration of Kerberos on Samba
  * APP.3.4.A10 Secure use of external programs on a Samba server
* G 0.39 Malware
  * APP.3.4.A2 Secure basic configuration of a Samba server
  * APP.3.4.A10 Secure use of external programs on a Samba server
* G 0.40 Denial of Service
  * APP.3.4.A1 Planning the use of a Samba server [Head IT]
  * APP.3.4.A10 Secure use of external programs on a Samba server
  * APP.3.4.A11 Secure use of communication protocols when using a Samba server
  * APP.3.4.A12 Training the administrators of a Samba server
  * APP.3.4.A13 Regular backup of important system components of a Samba server
  * APP.3.4.A14 Create an Samba server outage disaster recovery plan
  * APP.3.4.A15 Encryption of data packets under Samba (CI)
  * APP.3.4.A2 Secure basic configuration of a Samba server
  * APP.3.4.A3 Secure configuration of the operating system for a Samba server
  * APP.3.4.A10 Secure use of external programs on a Samba server
  * APP.3.4.A14 Create an Samba server outage disaster recovery plan
* G 0.45 data loss
  * APP.3.4.A4 Securing the NTFS properties on a Samba server
  * APP.3.4.A10 Secure use of external programs on a Samba server
  * APP.3.4.A11 Secure use of communication protocols when using a Samba server
* G 0.46 Loss of integrity of sensitive information
  * APP.3.4.A5 Secure configuration of access control for a Samba server
  * APP.3.4.A12 Training the administrators of a Samba server
  * APP.3.4.A15 Encryption of data packets under Samba (CI)
