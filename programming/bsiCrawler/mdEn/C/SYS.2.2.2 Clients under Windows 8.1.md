1 description
--------------

### 1.1 Introduction

With Windows 8, Microsoft has further developed its Windows client operating system and the functions and components it introduces. New to Windows 8 is the use of portable touchscreen devices. This brings a new operating concept for applications. In addition to the classic desktop applications, Microsoft has provided a class of mobile applications for use under Windows 8, the so-called "apps". These are consistently designed for control by touch. In addition, they can perceive display functions as "tiles" on the screen. Some applications, most notably the Windows 8-based Internet Explorer, are available in two variants for Windows 8. Since the release of Windows 8, Microsoft has made some improvements and integrated them into the operating system, which is now version 8.1.

### 1.2 Objective

The goal of this module is to protect information that will be processed by and on Windows 8.1 clients.

### 1.3 Delimitation

This block applies to all target objects on which the operating system Windows 8.1 is operated. Insofar as the described safety requirements and threats apply exclusively to Windows 8, this is explicitly stated in the texts. The requirements from the block [* SYS.2.1 General Client *] (DE / topics / IT Grundschutz / IT Grundschutz Compendium / modules / SYS / SYS_2_1_General_Client.html? Nn = 10137184 "SYS.2.1 General Client") must also be met in every case. This module clarifies and complements requirements that are specific to Windows 8.1. Application programs that are used on the Windows clients must meet the requirements of the corresponding blocks, for example APP.1.1 Office products or APP.1.6 Browser. When used in a Windows domain, the requirements of the corresponding components such as APP.2.2 Active Directory must be met.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​*** *** Windows 8.1:

### 2 1 Malware targeted to Windows

Malicious programs provide an attacker with extensive communication and control options and have a variety of functions. Among other things, malicious programs can specifically search passwords, remotely control systems, deactivate protection software and spy on data. A removable disk could be manipulated to run and install malware when the removable disk is inserted or connected. In particular, loss or falsification of information or applications is of paramount importance. But also a loss of image and financial damage, which can thus result from malicious programs, is of great importance. Windows is a prime target for malware attacks because of its widespread adoption, posing a major threat from numerous attackers and attack types.

### 2 2 Software vulnerabilities or errors

Windows 8.1, including its many included applications, is a very complex software product. If software errors are not detected in time, the crashes or errors that occur during the application can lead to far-reaching consequences (such as incorrect calculation results, incorrect management decisions, and delays in the course of business processes). Software vulnerabilities or errors can cause serious security vulnerabilities in individual applications, in the entire IT system, or even in all connected IT systems. Vulnerabilities in Windows can sometimes be exploited by attackers to inject malicious software, unauthorized read out or manipulate data.

### 2 3 Integrated cloud functionalities
Windows 8.1 includes many features that store and synchronize data in Microsoft's cloud services. There is a risk of unconsciously (or at least carelessly) using cloud services for possibly sensitive or personal data. At the same time, data protection laws may also be violated if data is stored by third parties, especially abroad. If a user with an already activated Microsoft account logs on to a new device, the Microsoft cloud services he uses are automatically set up there. Thus, data of the company can be unintentionally synchronized to the employees' private devices. As another example, Windows 8 provides the ability to back up the Bitlocker recovery key directly from the Microsoft account in the cloud. This puts critical cryptographic secrets in the hands of third parties.

### 2 4 Impairment of software functions due to compatibility issues

Software that was successfully run on previous versions of Windows does not have to work with a current version of the operating system. Possible causes are new security features or operating system features, as well as the omission of functionalities or services. As a result, the software can not be used or only with restrictions. For example, new versions of Windows can cause the activation of new security features to cause compatibility issues. Examples include User Account Control (UAC) or 64-bit versions of the Kernel Patch Guard operating system, and the need for signed drivers. For newer versions of Windows but also eliminated functionality. An example of this is the omission of the GINA login component in newer versions of Windows, the z. B. was used by some fingerprint readers.

### 2 5 Incorrect administration or use of devices and systems

Windows operating systems are complex systems whose security is essentially determined by the set parameters. In particular, misconfiguration of components can compromise security, causing malfunction or compromising the IT system. Basically, any interface to an IT system not only includes the ability to legitimately use certain services of the IT system, but also the risk of unauthorized access to the IT system. If, for example, user IDs and associated passwords can be spied out due to misconfiguration of the Windows own authentication mechanisms, then unauthorized use of the applications or IT systems protected by this is conceivable.

Improper or improper use of devices, systems, and applications can also affect security in Windows, especially if existing security measures are disregarded or circumvented. Too generously granted rights, easy-to-guess passwords, insufficiently protected data carriers with backup copies or jobs that are not locked in case of temporary absence can lead to security incidents. Another consequence of improper operation of Windows systems or applications may be the accidental deletion or modification of data. It is also possible for confidential information to reach the public, for example if access rights are set incorrectly.

3 requirements
---------------
The following are specific requirements for the Windows 8.1 area. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.2.2.2.A1 Appropriate selection of a Windows 8.1 version

The functional scope of a Windows version MUST be checked prior to procurement for operational capability and a suitable version must be selected. It is preferable to use 64-bit versions that include advanced security features.

#### SYS.2.2.2.A2 Definition of a registration procedure

Depending on the security requirements, it MUST be decided whether other mechanisms such as PIN should be allowed in addition to the traditional login procedure with password. This MUST be set accordingly on all clients.

#### SYS.2.2.2.A3 Use of virus protection programs

Unless equivalent or better measures have been taken to protect the IT system from malware infection, an anti-virus program MUST be used on Windows 8 clients.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​clients under Windows 8.1. They SHOULD be implemented in principle.

#### SYS.2.2.2.A4 Procurement of Windows 8.1

The requirements according to the Windows Hardware Certification Requirements SHOULD be taken into account when purchasing Windows 8.1 or the corresponding hardware for the Windows 8.1 system. Furthermore, the systems to be procured should have a firmware configuration interface for UEFI SecureBoot and for the TPM (if any) allowing for control by the owner. The Windows 8.1 procurement process SHOULD include the selection of a suitable license model.

#### SYS.2.2.2.A5 Local Security Policy

All security-relevant settings should be configured, tested and regularly checked via security guidelines. All unnecessary applications and components SHOULD be disabled using security policies. The distribution of security settings on multiple Windows 8.1 clients SHOULD be done according to the circumstances of the institution.

#### SYS.2.2.2.A6 file and share permissions

To allow unified restrictive rights assignment, there should be an authorization and access concept for Windows that defines appropriate file and directory permissions according to the need-to-know principle for content on the Windows 8.1 clients.

In addition to authorizations on the local file system, the authorization and access concept SHOULD observe the access rights for shared directories in network access. A check of the permissions of the files and directories SHOULD be done especially for computers upgraded from older operating system versions.

#### SYS.2.2.2.A7 Using the Windows User Account Control UAC

To support restrictive rights allocation, the user account control (UAC) SHOULD be enabled. For default users, SHOULD be set to automatically decline the password prompt for elevated privileges. For administrator accounts, the UAC setting SHOULD balance the usability and security level. The decision SHOULD be documented and the corresponding settings configured. It SHOULD be checked regularly if the need still exists and the rights are adjusted or withdrawn accordingly.
#### SYS.2.2.2.A8 Using the homegroup feature [User]

Clients SHOULD NOT offer services such as file or printer sharing. A security policy (GPO) with the setting "Prevent the computer from joining a homegroup" SHOULD apply to all clients. If the feature is used for operational reasons, users SHOULD be trained in handling homegroup permissions.

#### SYS.2.2.2.A9 Privacy and Data Saving on Windows 8.1 Clients [User]

If Microsoft accounts are created for the users, only absolutely necessary information about the persons should be deposited. The SmartScreen function SHOULD be reviewed and evaluated for compatibility with internal or external privacy policies. Before an application or app is released for use within the institution, SHOULD carefully examine which data applications and apps automatically submit to the Microsoft cloud. Applications SHOULD be configured so that no such data is transmitted. Apps with unwanted or unnecessarily extensive data transfer to third parties SHOULD NOT be used.

#### SYS.2.2.2.A10 Integration of online accounts in the operating system

The registration on the IT system and the domain SHOULD only be done with an account of a self-operated directory service, such Active Directory. A local login SHOULD be reserved for administrators. When using online accounts to log in, eg. For example, a Microsoft account or accounts from other providers of identity management services SHOULD be made aware of the security of the provider and privacy.

#### SYS.2.2.2.A11 Configuration of Synchronization Mechanisms in Windows 8.1

Syncing user data with Microsoft Cloud Services SHOULD be completely disabled.

#### SYS.2.2.2.A12 Central authentication in Windows networks

In pure Windows networks, only Kerberos SHOULD be used for centralized SSO authentication (Single Sign On). A group policy SHOULD prevent the use of older protocols. Storage of LAN Manager hash values ​​for password changes SHOULD be disabled by group policy. The monitoring settings together with the server components of DirectAccess SHOULD be carefully adjusted to the requirements of the information network. Client side logging SHOULD be ensured.

#### SYS.2.2.2.A13 Connection of Windows 8.1 to AppStores

The ability to install apps from the Microsoft AppStore SHOULD be disabled if not needed.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.2.2.2.A14 Application Control with Software Restriction Policies and AppLocker (CIA)

Applications in user-writable paths SHOULD be prevented from running by Software Restriction Policies (SRP) or AppLocker. The management of the AppLocker and SRP GPOs in a domain-based network SHOULD be centralized by means of GPOs per user / user group.

AppLocker SHOULD be used after the approach of a positive list. Everything should be forbidden, which is not explicitly allowed. AppLocker prefers to use rules based on application signatures of defined publishers. Attempted rule violations SHOULD be logged and suitably evaluated.
For clients with particularly high security requirements, AppLocker SHOULD prevent all unauthorized applications from running instead of logging them.

Implementation of the SRP and AppLocker rules SHOULD be tested on a test system or operating in monitor mode before being used on a productive system.

#### SYS.2.2.2.A15 Encrypting the file system with EFS (CI)

With increased protection requirements, the file system SHOULD be encrypted. When using the Encrypting File System (EFS), a complex password should be used to protect EFS encrypted data. In addition, EFS encrypted files SHOULD be protected by restrictive access rights. Instead of the administrator account, a dedicated account SHOULD be the recovery agent. The private key of this account SHOULD be swapped out to an external disk and kept safe and removed from the system. In doing so, backups of all private keys SHOULD be created. When using EFS with local user accounts, registry encryption using syskey SHOULD be used. When using EFS, users should be trained in using EFS correctly.

#### SYS.2.2.2.A16 Using Windows PowerShell (CIA)

If the Windows PowerShell (WPS) is not needed, it SHOULD be uninstalled. With Windows 8.1, however, the PowerShell scripting environment can only be removed if the .NET framework is also uninstalled. Therefore, alternatively, the execution of the WPS files SHOULD only be allowed to the groups of administrators, local and domain. The logging of read and write access to the Windows PowerShell profile SHOULD be enabled and periodic control of the logs should be ensured. The execution of Windows PowerShell scripts using the Set-Execution Policy AllSigned command SHOULD be restricted to prevent at least the accidental execution of unsigned scripts.

#### SYS.2.2.2.A17 Safe Use of the Maintenance Center (CIA)

The security policy SHOULD define the way the user interacts with the maintenance center. Changes to the default startup settings of the Windows 8 services DPS, WDiSvcHost, and WerSvc are required. Get the settings for "Get latest troubleshooting from Windows online troubleshooting service", "Send problem reports", "Send data to computer via Microsoft on a regular basis," "Windows Backup," "User Experience Utility," and "Troubleshooting Other Settings" below Windows 8.1 will be disabled.

#### SYS.2.2.2.A18 Activation of the last-access timestamp (A)

As part of the process of creating a security plan for an IT system running Windows 8.1, it should be checked whether the load-access timestamp is activated to facilitate the analysis of a system abuse. In particular, performance aspects should be taken into consideration during the test.

#### SYS.2.2.2.A19 Using Credential Management (C)

The permission or the prohibition of the storage of access data in the so-called "safe" SHOULD be defined in a guideline. A ban SHOULD be technically enforced.

#### SYS.2.2.2.A20 Remote access security via RDP (CIA)
The impact on the configuration of the local firewall SHOULD be taken into account when planning the remote support. The group of authorized users for remote desktop access SHOULD be set by assigning appropriate user rights and policy. Remote support SHOULD only be done after an explicit invitation via EasyConnect or on the basis of an invitation file. When saving an invitation to a file, the file SHOULD be password protected. The currently logged in user SHOULD always have to explicitly agree to the setup of a session. The maximum validity of the invitation SHOULD have an appropriate size. In addition, a strong encryption (128 bit, setting "Highest Level") SHOULD be used. In addition, the automatic password login SHOULD be disabled. It SHOULD be checked if clipboard redirects, printers, filing and smartcard connections are necessary, otherwise they SHOULD be disabled. Unless the use of remote control mechanisms is foreseen, they SHOULD be completely disabled.

#### SYS.2.2.2.A21 Using File and Registry Virtualization (CI)

It SHOULD be checked if the operation of legacy applications is still necessary, which require write access to critical system folders or registry keys or if they need to be run with administrator rights. If this is the case, then a strategy SHOULD be developed to convert the legacy applications still needed to secure alternatives. Until the old applications have been replaced, the use of the Windows techniques File Virtualization and Registry Virtualization SHOULD be checked for security. In addition, Registry Virtualization SHOULD only have access to the necessary registry keys.

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the section "Clients under Windows 8.1" can be found in the following publications, among others:

* #### [MicSAO] Security Auditing Overview, Microsoft, 07.2013

  

 <Https://technet.microsoft.com/en-us/library/dn319078.aspx>

 
* #### [MicSE] List of security events: Windows 8 and Windows Server 2012, Microsoft, (most recently downloaded on Sep 27, 2017)

  

 <Https://www.microsoft.com/en-us/download/confirmation.aspx?id=50034>

 
* #### [WIN8] Information about deployment, deployment and administration of Windows 8.1, Micorosoft, (last accessed on 27.09.2017)

  

 <Https://technet.microsoft.com/de-de/windows/windows-8.aspx>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Clients under Windows 8.1" block.

* G 0.16 Theft of devices, data carriers or documents
* G 0.17 Loss of equipment, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.36 Identity theft
* G 0.39 Malware
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
