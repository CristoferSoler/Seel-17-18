1 description
--------------

### 1.1 Introduction

With Windows 10, Microsoft has adapted its Windows client operating system to a new corporate strategy. In particular, the design philosophy of the operating system has also changed away from the previous principle of the "local operating system" towards a service ("Windows as a Service") which, in addition to the previous operating system functionalities, also contains applications that go beyond that, in particular cloud-based, and therefore one tight connection to the server infrastructure of the manufacturer is dependent. The deep-rooted and sometimes uncontrollable data exchange between client and manufacturer infrastructure as well as the increasing outsourcing of security-critical core components of a Windows infrastructure to the cloud, such as: As authentication, are important and before a use necessarily to be evaluated new aspects compared to the previous versions of Windows.

### 1.2 Objective

The goal of this module is to protect information that will be processed by and on Windows 10 clients.

### 1.3 Delimitation

Based on the SYS.2.1 General Client block, this block contains specific requirements that must be observed and fulfilled for the secure operation of clients under the Windows 10 operating system in addition to the requirements from the SYS.2.1 General Client block. The included requirements must always be considered in conjunction with the requirements of the "General Client". Protection against advanced and persistent threats must be realized by meeting additional requirements of the different layers of modernized IT-Grundschutz.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to the Windows 10-based clients under consideration:

### 2 1 Malware on Windows 10

Due to the high prevalence of Windows operating systems and the backwards compatibility with older versions, which is often present between the system generations, the threat from malicious programs and unauthorized intrusion into the IT system is comparatively high. Malicious programs can have a variety of functions and provide an attacker with extensive control options. Among other things, malicious programs can specifically search passwords, remotely control systems, deactivate protection software and spy on data. In particular, loss or falsification of information or applications is of paramount importance. But also a loss of image and financial damage, which can thus result from malicious programs, is of great importance. Windows is a primary target for malware attacks due to its widespread use, posing a major threat from numerous attackers and attack types.

### 2 2 Software Vulnerabilities in Windows 10

Windows 10, including its many included applications, is a very complex software product. If software errors are not detected in time, the crashes or errors that occur during the application can lead to far-reaching consequences (such as incorrect calculation results, incorrect management decisions, and delays in the course of business processes). Software vulnerabilities or errors can lead to serious security vulnerabilities in individual applications, in the entire IT system, or even in all connected IT systems. Vulnerabilities in Windows can sometimes be exploited by attackers to inject malicious software, illegally read data or manipulate.

### 2 3 Integrated cloud functionalities
Windows 10 has many features that store and sync data using Microsoft's services ("cloud services"). As a result, there is a risk of unconsciously (or at least carelessly) using it for possibly sensitive or personal data. At the same time, violations of data protection laws may result if data is stored with third parties, usually abroad. If a user with an already activated Microsoft account logs on to a new device, the Microsoft cloud services he uses are automatically set up. Thus, data of the institution can be unintentionally synchronized to the employees' private devices. As another example, Windows 10 provides the ability to back up the Bitlocker recovery key directly from the Microsoft account in the cloud, leaving critical cryptographic secrets in the hands of third parties.

### 2 4 Impairment of software functions due to compatibility issues

Software that has been successfully run on previous versions of an operating system does not necessarily have to work with the current version of Windows 10. Possible causes are new security features or operating system features, as well as the omission of functionalities or services. As a result, the software can not be used or only with restrictions. Examples of enabled security features that can cause compatibility issues with new versions of Windows include User Account Control (UAC), or 64-bit versions of the Kernel Patch Guard operating system, and the need for signed drivers that may not be available for older devices To be available.

### 2 5 Incorrect administration or use of Windows 10

Windows 10 is a complex operating system whose security is largely determined by its configuration. This results in particular by misconfiguration of individual or multiple components impairments of security for the client itself and for the infrastructure used. Basically, any interface to an IT system not only includes the ability to legitimately use certain services of the IT system, but also the risk of unauthorized access to the IT system. If user IDs and associated passwords can be spied out, for example by misconfiguration of the Windows own authentication mechanisms, then unauthorized use of the applications or IT systems protected by them is possible.

Improper or improper use of devices, systems, and applications can also affect security in Windows, especially if existing security measures are disregarded or bypassed or deliberately shut down. Too generously granted rights, easy-to-guess passwords, insufficiently protected data carriers with backup copies or jobs that are not locked in case of temporary absence can lead to security incidents. Another consequence of improper operation of Windows systems or applications may be the accidental deletion or modification of data. It is also possible for confidential information to reach the public, for example if access rights are set incorrectly.

3 requirements
---------------
The following are specific requirements for Windows 10 protection. Basically * the IT operation * is responsible for fulfilling the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are mentioned separately in the corresponding requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.2.2.3.A1 Planning the use of cloud services

Windows 10-based devices are closely interlinked with the cloud services of the manufacturer Microsoft. Therefore, before using Windows 10-based devices, it is MUST be strategically determined which cloud services are or should be used.

#### SYS.2.2.3.A2 Appropriate selection of Windows 10 version and procurement

The functional scope and the supply of functional changes of a Windows 10 version MUST be selected taking into account the identified protection needs and purpose and the feasibility of the necessary safeguards must be checked. Based on the result of the review, the established procurement process MUST be extended to include the appropriate license model and release path (CB, CBB or LTSB).

#### SYS.2.2.3.A3 Appropriate patch and change management

To capture and evaluate all changes, all Windows 10 systems MUST be subject to patch and change management. For complex patches or changes, an implementation plan MUST define tests, control and breakpoints, and distribution priorities. After a functional update of the operating system it MUST be checked whether all requirements from the IT-Grundschutz and the internal specifications are still fulfilled.

#### SYS.2.2.3.A4 telemetry and privacy settings

The telemetry services, the diagnostic and usage data that Microsoft uses to identify and resolve problems, improve its services and products, and personalize the system with unique identifiers, can not be completely shut down in the operating system. It is therefore necessary to take appropriate measures, such as at the network level, to ensure that these data are not transmitted to Microsoft.

#### SYS.2.2.3.A5 Protection against malware

Unless equivalent or superior other mitigating measures have been taken to protect the IT system from malware infection, the use of a specialized malware protection component MUST be implemented on Windows 10 clients.

#### SYS.2.2.3.A6 Integration of Online Accounts in the Operating System [User]

The registration on the system and the domain MAY ONLY be possible with the account of a self-operated directory service. Registrations with local accounts SHOULD be reserved for administrators. Online accounts for registration, such as a Microsoft account or accounts of other providers of identity management systems, MUST NOT be used because personal data is transferred to the manufacturer's systems.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​clients under Windows 10. They SHOULD be implemented in principle.

#### SYS.2.2.3.A7 Local Security Policy
All security-relevant settings SHOULD be configured, tested and regularly checked as needed. The security policies SHOULD be configured in accordance with the operating system manufacturer's recommendations and the default default behavior, unless the default behavior conflicts with other IT security or organization requirements. Deviations MUST be documented and justified. All unnecessary applications and components SHOULD be disabled. Security policies SHOULD be set in any case, even if the setting does not deviate from the default behavior of an unset security policy.

#### SYS.2.2.3.A8 Central management of client security policies

All settings of the Windows 10 client SHOULD be managed by centralized management and configured according to the identified protection needs based on the internal policies. Technically non-implementable configuration parameters SHOULD be documented, justified and agreed with the security management.

#### SYS.2.2.3.A9 Secure centralized authentication of Windows clients

For the central authentication only Kerberos SHOULD be used. A group policy SHOULD prevent the use of older protocols. If this is not possible, alternatively NTLMv2 MUST be used. The authentication via LAN Manager and NTLMv1 MUST NOT be allowed within the institution and in a productive operating environment. The cryptographic mechanisms used SHOULD be configured, documented and based on the internal guidelines in accordance with the identified protection requirements and justified by different attitudes and coordinated with the security management.

#### SYS.2.2.3.A10 Configuration for protecting applications in Windows 10

The data execution prevention for all programs and services (opt-out mode) SHOULD be activated.

#### SYS.2.2.3.A11 Credential protection in Windows 10

If Windows 10 is (native) installed on a hardware system in the Enterprise version, the Virtual Secure Mode (VSM) SHOULD be activated. In addition to enabling VSM, Credential Guard SHOULD be activated to prevent attacks on the authentication tokens and hashes stored in the system. If this is not possible, Protected Process Light (PPL) should be enabled to operate the LSAS service responsible for managing credentials. Network logon from local accounts SHOULD be banned.

#### SYS.2.2.3.A12 File and Share Permissions

Access to files and folders on the local system and network shares SHOULD be configured according to an authorization and access concept. This includes in particular the standard administrative shares on the system. The write permissions for users SHOULD be limited to a defined area in the file system. In particular, users SHOULD NOT receive write permissions to folders of the operating system or installed applications.

#### SYS.2.2.3.A13 Using SmartScreen features

The SmartScreen feature, which scans files and web content downloaded from the Internet for possible malware and may transfer personal information to Microsoft, SHOULD be disabled.

#### SYS.2.2.3.A14 Using the language assistant Cortana [User]

Cortana uses personal data such as: Voice data, user input, calendar and contact information, preferred location names and used applications being transferred to Microsoft. For this reason, Cortana SHOULD be disabled.

#### SYS.2.2.3.A15 Use of Synchronization Mechanisms in Windows 10

The synchronization of user data with Microsoft Cloud services and the sharing of Wi-Fi passwords SHOULD be completely disabled.
#### SYS.2.2.3.A16 Connecting Windows 10 to the Windows Store

The use of the Windows ** ** Store SHOULD be checked for compatibility with the privacy and security policies of the institution. The general installation of apps on Windows 10 is not tied to the connection to the Windows Store. Therefore, this feature SHOULD be disabled if it is not needed.

#### SYS.2.2.3.A17 Using automatic login

The storage of passwords, certificates and other credentials for automatic login to websites and IT systems SHOULD NOT be allowed.

#### SYS.2.2.3.A18 Using Windows Remote Assistance

The impact on local firewall configuration SHOULD be taken into account when planning Windows Remote Assistance (this does not mean RDP). Remote support SHOULD only take place after an explicit invitation. When saving an invitation to a file, it SHOULD have a password. The currently logged-in user SHOULD always vote explicitly for the structure of a session. The maximum duration of the invitation for remote assistance SHOULD be reasonable. Unless this service is used, it SHOULD be completely disabled.

#### SYS.2.2.3.A19 Using Remote Access over RDP [User]

The impact on the configuration of the local firewall SHOULD be taken into account when planning the remote access. The group of authorized users for Remote Desktop Access (RDP) SHOULD be set by assigning appropriate user rights. In complex infrastructures, the RDP target system SHOULD only be reached by an intermediate RDP gateway. For the use of RDP, a test and its implementation SHOULD ensure that the following comfort features are consistent with the protection requirements of the target system:

* the use of the clipboard,
* the integration of printers,
* the integration of removable media and network drives
* the use of file storage and smart card connections
Unless the use of remote desktop access is provided for, they SHOULD be completely disabled. The cryptographic protocols and algorithms used SHOULD comply with the internal requirements of the institution.

#### SYS.2.2.3.A20 Use of user account control for privileged accounts

The configuration parameters of the User Account Control (UAC) SHOULD be used for the privileged accounts between usability and security level. The decisions for the configuration parameters to be used SHOULD be documented. In addition, the documentation SHOULD include all accounts with administrative privileges, as well as a periodic review to determine if the need to extend the rights still exists.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.2.2.3.A21 Use of the Encrypting File System EFS (CI)
Since the Encrypting File System (EFS) protects the keys used with the password of the user account, a complex password SHOULD be used. In addition, restrictive access rights SHOULD protect EFS encrypted files. Instead of the administrator, a dedicated account SHOULD be the recovery agent. In this context, its private key SHOULD be saved and removed from the system. In doing so, backups of all private keys SHOULD be created. When using EFS with local user accounts, encryption of the local password storage using Syskey SHOULD be used. This can be omitted if the operating system function Credential Guard is used. When using EFS, users should be trained in using EFS correctly.

#### SYS.2.2.3.A22 Windows PowerShell (CIA)

The execution of PowerShell and WPS files SHOULD only be granted to administrators. The PowerShell execution itself SHOULD be centrally logged and the logs monitored. The execution of PowerShell scripts SHOULD be restricted by the Set-ExecutionPolicy-AllSigned command to prevent the accidental execution of unsigned scripts.

#### SYS.2.2.3.A23 Extended Credential Protection in Windows 10 (CI)

On UEFI-based systems, SecureBoot SHOULD use and monitor the status of LSASS protected mode at system startup (see SYS.2.2.3.A11 Credential protection in Windows 10). If remote maintenance of the client systems is provided by means of RDP, the option "restrictedAdmin" SHOULD be used when using Windows 10 in a domain from the functional level 2012 R2.

#### SYS.2.2.3.A24 Activation of the last-access timestamp (A)

To facilitate the analysis of system abuse, the NTFS load access timestamp SHOULD be activated. BEFORE activating, SHOULD the impact of activation on system performance be assessed. The results of the review and decision on activation SHOULD be documented.

#### SYS.2.2.3.A25 Handling Connected User Experience and Telemetry (CI) Remote Access Features

The Connected User Experience and Telemetry (CUET) component of Windows 10 is an integral part of the operating system and provides telemetry functionality as well as remote access for the OS vendor to the local system. A remote access to the Windows 10 client by the operating system manufacturer SHOULD be logged on the network side and blocked if necessary.

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the section "Clients under Windows 10" can be found in the following publications, among others:

* #### [TN408187] Configuring Additional LSA Protection

  

 Microsoft Technet, 03.2014
 <Https://technet.microsoft.com/en-us/library/dn408187.aspx>

 
* #### [TN621547] Credential Guard - Overview

  

 Microsoft, (last accessed on 27.09.2017)
 <Https://docs.microsoft.com/de-de/windows/access-protection/credential-guard/credential-guard-requirements>

 
* #### [TN986865] Device Guard - Overview

  

 Microsoft, (last accessed on 27.09.2017)
 <Https://technet.microsoft.com/de-de/library/dn986865.aspx>

 
* #### [WIN10E] Compare Windows 10 editions

  

 Microsoft, (last accessed on 27.09.2017)
 <Https://www.microsoft.com/de-de/WindowsForBusiness/Compare>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Clients under Windows 10" block.

* G 0.15 Listening
* G 0.16 Theft of devices, data carriers or documents
* G 0.17 Loss of equipment, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
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
