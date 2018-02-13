[toc]
 
1 description
--------------

### 1.1 Introduction

With Windows Server 2012, Microsoft released a server operating system in September 2012 that brings several improvements in terms of security compared to previous versions of Windows (especially Windows Server 2008 R2). Technically, it is based not on the predecessor, but on the code base of the client operating system Windows 8. With the release of Windows Server 2012 R2 from October 2013, further improvements and enhancements are available, the Windows 2012 R2 server counterpart to Windows 8.1 on the Client side.

This module is equally concerned with securing Windows Server 2012 and Windows Server 2012 R2, with relevant differences and peculiarities being appropriately pointed out. The spelling "Windows Server 2012 (R2)" is used if both versions are meant. The expiration date for Mainstream Support and Extended Support ("End-of-Life", EOL) is 09.01.2018 or 10.01.2023 in both cases.

### 1.2 Life cycle

** planning and conception **

The main considerations are in SYS.1.2.2.M1 Planning Windows Server 2012 (R2). Also SYS.1.2.2.M2 Secure installation of Windows Server 2012 (R2) and SYS.1.2.2.M3 Secure administration of Windows Server 2012 (R2) includes essential design considerations.

**Procurement**

With regard to procurement, the general principles that apply to general server systems must be observed. In addition, SYS.1.2.2.M1 Planning for Windows Server 2012 (R2) discusses the topic of choosing the appropriate edition.

**Implementation**

The main measures for the basic protection of the enterprise are described in the following three measures:

* SYS.1.2.2.M2 Secure installation of Windows Server 2012 (R2)
* SYS.1.2.2.M3 Secure Administration of Windows Server 2012 (R2)
* SYS.1.2.2.M4 Secure configuration of Windows Server 2012 (R2)
In addition, there are the more specific but important implementations of:

* SYS.1.2.2.M5 protection against malware
* SYS.1.2.2.M6 Secure Authentication and Authorization in Windows Server 2012 (R2)
* SYS.1.2.2.M8 System Integrity Protection
* SYS.1.2.2.M9 Local Communication Filtering (CI)
In the case of increased protection requirements, the following measures are used by way of example:

* SYS.1.2.2.M10 Disk Encryption on Windows Server 2012 (R2)
* SYS.1.2.2.M12 redundancy and high availability (A)
* SYS.1.2.2.M13 Strong authentication in Windows Server 2012 (R2) (CI)
**Business**

Even during operation, SYS.1.2.2.M3 Secure Administration of Windows Server 2012 (R2) and SYS.1.2.2.M4 Secure Configuration of Windows Server 2012 (R2) remain relevant. As further standard requirements, the achieved security level must be checked regularly (SYS.1.2.2.M7 Security check of Windows Server 2012 (R2)).

In case of increased protection requirements, additional attention can be paid during operation:

* SYS.1.2.2.M11 Intrusion Detection on Windows Server 2012 (R2) (CIA)
* SYS.1.2.2.M14 Shutting Down Encrypted Servers and Virtual Machines (CI)
** Disposal & Emergency Prevention **

With regard to the phases of the rejection and emergency preparedness, there are no special features of Windows Server 2012 (R2) compared to a general server.

2 measures
-----------

The following are specific implementation notes in the "Windows Server 2012" section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### SYS.1.2.2.M1 Planning for Windows Server 2012

Because Windows Server 2012 (R2) is a complex operating system with a variety of features and configuration options, deployment must be carefully and systematically planned. A documentation of the decisions including a brief justification should be created, for example in the form of an operational concept or a server manual.

** ** editions

Windows Server 2012 is available in four editions designed and optimized for different applications:

* Foundation
+ Basic server features
+ no virtualization


 
* Essentials

 
+ simple user interface
+ Default connectivity to cloud services
+ no virtualization


 
* Default

 
+ Full functionality
+ max. two virtual instances


 
* Datacenter

 
+ as standard
+ with unlimited virtual instances


 
Further limitations exist on the foundation or essentials regarding storage (up to 32/64 GB RAM) and licensing (up to 15/25 user accounts), as well as the installable roles and functionalities. For more details about the differences in terms of restrictions, roles, and features, visit their website. ** ** For example, server core mode is available as of Edition Standard, and WSUS is available only on Essentials. At least Foundation is therefore recommended only in very limited scenarios for professional use in the company or in the authority and is not considered in this module closer.

The editions Standard and Datacenter are equivalent from a security point of view and essentially differ in terms of the licensing model. So there is the question of the decision between Essentials and Standard or Datacenter.

** Features of the Essentials Edition **

Foundation and Essentials in Windows 2012 are not intended to run within a full domain. Although this is now technically possible for Essentials with Windows Server 2012 R2, its features are primarily aimed at smaller institutions that use only a single server to run all functions. This is in contrast to the established practice in larger IT environments of running as few services as possible per server to resolve dependencies and spread risk, a trend that is becoming more prevalent as virtualization increases.

The Essentials Edition offers a number of features that can simplify setup without further configuration:

* Add to the domain
 Essentials makes it easy to add machines to the domain that are located remotely. All it takes is a new employee to access the / connect path on the Essentials remote access website.
* Preconfigured VPN
 There is a preconfigured VPN client available. The user can also activate auto dial-in so that he is always connected to the corporate or government network.
* Server StorageFor locations such as user home directories, you can simply create shared folders on another server on the same network. This can be an automatic alert when the directories exceed a certain size.
* Health Report
 A basic "health check" of the Windows Server 2012 R2 Essentials environment is already integrated and does not need to be installed as an add-in. Various values ​​can be configured that are displayed via different media, such as the smartphone.
* BranchCache
 The BranchCache mechanism can already be activated in Essentials, which increases the availability of data in remote locations through caching. It also reduces bandwidth usage across the WAN.
* Remote Web Access
 Many features of Windows Server 2012 Essentials can be remotely accessed and controlled through a web interface (Remote Web Access), which has been streamlined in R2 and optimized for use with tablets and similar devices.
** Microsoft Azure Online Backup **
In Windows Server 2012, Microsoft's cloud storage solution Azure Online Backup is already integrated into Essentials and can be easily activated. All you have to do is install the corresponding Add-in in the Essentials Dashboard and create an account (depending on the storage volume). In R2 is not even an add-in necessary, here can be done directly by clicking the registration with Azure.

While this is a very easy way to generate regular backups of the data stored on the server, this feature should not be lightly activated, but at best after a comprehensive study of the topics of the building blocks OPS.2.2 cloud usage and OPS.1.16 data protection and a trade-off between confidentiality, availability and various providers.

** Block Microsoft accounts **

The following section is not applicable if a well-founded and documented decision has been made regarding the use of Microsoft Azure in connection with the Windows Server 2012 (R2) server system as part of the OPS.2.2 Cloud Usage building block.

Otherwise, no Microsoft account may be created during system setup. Creation of Microsoft accounts on the server must also be blocked. This is done most reliably via the Active Directory and the following security policy:

"Windows Settings / Security Settings / Local Policies / Security Options / Accounts: Block Microsoft Accounts"

#### SYS.1.2.2.M2 Secure installation of Windows Server 2012

Basic features of Windows Server 2012 (R2) are controlled by server roles, role services, and features.

** ** server roles

A server role is a group of programs that can perform a specific role for multiple users or for other IT systems in a network. It is often used to describe the main function of a server. However, a server could also run multiple roles if they are rarely used. If roles are correctly installed and configured, they will run automatically.

** Role Services **

Role Services are programs that provide the functionality of a role. A role can be considered as a set of contiguous, complementary role services, with the installation of a role usually requiring the establishment of at least one associated role service.

For each role, you can specify which role services are provided to other users and IT systems with the role. Some roles (such as DNS servers) have only one role, so there are no role services available to them. Other roles (for example, Remote Desktop Services) have multiple role services that can be installed as needed.

** Features **

Features are programs that support or enhance the functionality of the server or one or more roles. For example, the Failover Clustering feature enhances the functionality of other roles, including file services and DHCP servers, because server clusters can be merged for greater redundancy and better performance. The Telnet client feature, on the other hand, enables remote communication via the Telnet protocol.

Roles, role services, and features must always be installed as sparingly as possible to minimize the complexity and attack surface. The rule "one service per server" also applies mutatis mutandis, as a rule only one institution-specific server role per server should be installed. The selection of roles, role services and features to be installed should be justified and documented.

** Server Core **

Server Core is a minimal installation option for Windows Server (including 2012 and 2012 R2) that provides a server environment with limited functionality and lower maintenance requirements.
Since Windows Server 2012, you can switch between Full Server and Server Core without reinstalling.

Main differences are the lack of the complete Windows shell and an extremely limited graphical user interface (GUI), which is limited to a command prompt with PowerShell support.

Server Core can be managed as follows:

* via PowerShell (local and remote)
* via a terminal server connection from a command line
* remotely via the Microsoft Management Console (MMC)
* remotely with other command-line tools that support remote management
Since Server Core represents the minimum and thus optimum with respect to the attack surface, the Server Core version should be used wherever possible. Deviations should be justified. This also promotes the centralization of the administration.

#### SYS.1.2.2.M3 Secure Administration of Windows Server 2012

** Secure passwords for local administration accounts **

It's important to make sure that the password for each local administrator account is not only secure, but unique. This makes it more difficult for an attacker to move from one compromised IT system to the next.

With the LAPS (Local Administrator Password Solution) tool available for free at Microsoft, it is possible to automatically manage secure local administrator accounts via AD. Its use is highly recommended if a third-party solution is not already available.

** Training ** by administrators

To securely set up and operate Windows Server 2012 (R2), the administrators responsible must have a set of skills and knowledge, some of which are very specific to that operating system. The general knowledge of the administrator includes about basic rules of working on server systems such as

* not to surf the web from servers,
* in particular, not to control potentially unsafe sites,
* To use client systems for downloading files such as drivers and
* to use a standard account for all non-administrative activities.
The following is a description of Windows Server 2012 (R2) specifics that administrators should be familiar with. Necessary training should be done before installing the server systems.

** ** Administration issues

The following table contains a list of security-relevant administration topics. Windows Server 2012 (R2) administrators should be familiar with these topics and their specifics, as well as suitable tools for Windows Server 2012 (R2).

In addition, as part of Windows PowerShell Core Modules, Microsoft offers collections of PowerShell commandlets for security tasks. Administrators should be aware of these for easy and streamlined security management:

* Windows PowerShell Security Cmdlets
* PowerShell cmdlets for Active Directory
* PowerShell cmdlets for Active Directory Rights Management Services
* PowerShell cmdlets for AppLocker
* PowerShell Cmdlets for Group Policy
* PowerShell Cmdlets for Server Manager
* PowerShell Cmdlets for the Best Practice Analyzer
** User Account Control (UAC) **

User Account Control (UAC) was introduced in Windows Vista. It ensures that an increase in rights is required for administrative tasks. Until then, most users had worked as administrators, with appropriate vulnerabilities to malware.
If an administrator logs in with UAC enabled, he works with restricted rights. Only after confirmation in a special dialog box does an application receive administrative permissions. In the background, rights are increased by changing the identity. The UAC is thus the basis for the sandboxing of programs and directories under Windows. It regulates the granting of privileges to processes and isolates processes and windows that run on the same desktop with different rights.

With Windows Server 2012 and Windows 7, the UAC has been refined to make it easier to manage the configuration and messages.

UAC is a compromise between security and convenience. It does not provide full sandboxing and can be bypassed in a number of ways, but can add to the cost of malicious software and related threats or help isolate their effects.

An even stronger coverage would be achieved by working with completely separate accounts with real account switching for administrative tasks. This is recommended for high or very high protection requirements. The second most secure solution is to use separate rights-elevating accounts for standard users through Over-the-Shoulder Query (OTS). At a minimum, work should be enabled in Admin Approval Mode (AAM). The shutdown of the user account control is no longer possible with Windows Server 2012, but also an automatic rights increase without demand is not recommended.

However, with complete separation of the accounts the problem arises that if administrators should first be able to log on to servers as standard users, it is also possible to log in all domain users on the server. This is not desirable as it significantly increases the attack surface. Either this must be prevented with complex configuration or the alternative of separate admin systems, so-called Privileged Access Workstations (PAWs), can be used. However, these specially protected dedicated systems are usually only in question with higher protection requirements.

Attention: UAC never limits the predefined account "Administrator". Under client operating systems as of Vista this usually has no effect as this account can not be used for login; instead, additional accounts from the "Administrators" group will be created. On the other hand, Windows Server (as of 2008) does not create any additional accounts during installation and allows you to log in as "Administrator" without UAC. The account "Administrator" should therefore not be used for regular system administration. Other local or domain accounts that are "administrators" members are restricted via UAC.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the area of ​​"Windows Server 2012".

#### SYS.1.2.2.M4 Secure configuration of Windows Server 2012

In the following, those important security mechanisms, i. H. Security techniques that have or have a material effect on them are outlined briefly in Windows Server 2012 (R2), where the security officer or administrator has a choice. Not listed are such mechanisms, in which nothing has changed in comparison to the previous versions or there is no design freedom in the application.

Windows Server 2012 (R2) already comes with a set of resources and tools that can and should be used for backup. These should complement each other in a meaningful way with the security features of other IT systems and third-party products, ideally covering them in the sense of a defense-in-depth and never canceling or weakening each other.

Not several essential functions per ** server **
The requirement that several essential functions should not be fulfilled by a server, a fundamental distribution of critical server functionality is aimed at different systems. The "one service per server" used in the Unix area does not fit here, since service in the narrower sense rather describes a single network service (eg Telnet). This is more about making functionally independent units technically independent of each other. For example, a web server should not be a terminal server at the same time as a file server should not be a WSUS server at the same time. In multi-layer applications, the goal is usually to map the individual layers (such as database / business logic / presentation) into separate servers (clusters). This has the advantage that the network can be segmented more easily and thus better adapted to the protection requirements and the nature of the threats. There are also advantages in maintenance and administration.

S ** ecurity Baseline ** and SCM

Many security-related settings in Windows Server 2012 (R2) are most easily managed through GPOs. It is recommended to create a so-called baseline for all server systems or for server systems of a specific deployment class, ie a template that contains optimal security settings, is regularly checked and updated and is rolled out to all server systems operated.

The Security Compliance Manager (SCM) is a free tool from Microsoft that can be used to quickly create and manage GPOs and also brings security templates for various purposes. These can then with different methods, such. For example, Group Policy Editor or System Center Configuration Manager (SCCM) or DCM (Desired Configuration Management, now renamed Configuration Manager Compliance Settings) can be rolled out centrally. Configuration of stand-alone machines is also possible through the GPO Pack feature, but recommended only for non-domain member exceptions.

The consistent use of SCM or other security templates and the central deployment of GPOs and / or DCMs improve consistency and traceability, helping to prevent configuration drift and increase compliance. In addition to operating system settings, so many applications can be managed.

In particular, the security templates available in the SCM contain settings that are even more secure for many parameters than the default settings in Windows Server 2012 (R2). Often, however, these still have to be adapted to the respective purpose of use and the circumstances of the institution.

If the institution does not already have a security-compliant security template, the Security Baseline for Windows Server 2012 or R2 should be selected in the SCM. The packed .cab file contains the following components:

* Windows Server 2012

 
+ AD Certificate Services Server Security
+ DHCP server security
+ DNS Server Security
+ Domain Controller Security Compliance
+ Domain Security Compliance
+ File Server Security
+ Hyper-V Security
+ Member Server Security Compliance
+ Network Policy and Access Services Security
+ Print Server Security
+ Remote Access Services Security
+ Remote Desktop Services Security
+ Web Server Security


 
* Windows Server 2012 R2

 
+ Domain Controller Security Compliance
+ Domain Security Compliance
+ Member Server Security Compliance


 
* The following attachments are included with both:

 
+ Security Guide.docx: this contains the description of the selected settings
+ CCE Reference.xlsm


 
The adjustment should be based on GPOs for the intended role of Server 2012 (R2). All settings should be thoroughly tested before rolling out to productive systems, otherwise malfunctions can easily occur.
It should be checked after each major change, whether the setting was successfully changed and whether the template is ever applied to the desired server, since there are many sources of error lurking here. An easy way to do this is to run the Group Policy Results command-line tool GPResult.exe on the server.

For further information, see also module APP.2.2 Active Directory.

** Securing the Internet Explorer **

The browser on the server, in the case of Windows Server first the IE, is a potential gateway for attacks from the Internet. It should therefore be particularly secure, even if the wild browsing by policy is organizationally prohibited.

** Enhanced Security Configuration **

When you install Windows Server 2012, IE automatically installs with Enhanced Security Configuration (ESC) enabled. This configuration assigns specific (higher) security levels to the zones defined in IE 10 (Internet, Intranet, Trusted, Restricted). "High" in the case of Internet and Restricted Zone. In addition, the configuration contains a number of other settings, such as deleting the temporary Internet files when closing the browser.

This mode helps to reduce the attack surface in the browser and should therefore be retained.

Enhanced ** Protected Mode **

Enhanced Protected Mode (EPM), also available as of IE 10, is an extension of the protected mode introduced with IE 7 on Windows Vista. Its browser-related measures to prevent software installation and manipulation of the system added further restrictions on intranet information leakage

EPM can either be found in the Group Policy Management Console (GPMC) under "Windows Components \ Internet Explorer \ Internet Control Panel \ Advanced Page" or in the registry (computer-wide) under "HKLM \ Software \ Policies \ Microsoft \ Internet Explorer \ Main! Isolation ".

#### SYS.1.2.2.M5 Malware Protection

Before an IT system is connected to potentially insecure networks, and before removable media is connected to the IT system, an antivirus program should be installed on each Windows Server 2012 (R2) system, unless otherwise provided for malicious programs. This is to be planned and configured in the OPS.1.15 malware protection module.

When using an anti-virus program on the server, the signatures should be updated at least daily, and all hard disks, including the operating system partition, should be scanned regularly. Appropriate alerts for the responsible administrators should be configured for all types of malware related events.

Regardless of which antivirus product you choose, you can use Windows Defender, a Microsoft Windows Defender product integrated with Windows Server 2012 (R2), until the final malware-protection solution is activated.

** Windows Defender **

Windows Defender was a pure anti-spyware solution before Windows Server 2012 and has since been a full-fledged antivirus, but is optimized for the consumer market. Since R2, Windows Defender is enabled by default on Server Core.

Windows Defender should remain enabled until an alternative full-featured antivirus solution is installed. Several anti-virus programs (including Windows Defender) in parallel may only be operated if the recommendations of both manufacturers expressly permit this, as a rule this is not the case. In addition, each virus scanner increases potential vulnerabilities and the attack surface of the server.

#### SYS.1.2.2.M6 Secure Authentication and Authorization in Windows Server 2012
Authentication and authorization play important roles as two basic security techniques in various places in Windows Server 2012 (R2). The following principles can serve as general guidelines for the realization:

* Restrict and protect privileged domain accounts

 
+ Separate accounts for administration and other use for administrators
+ Special secured admin workstations
+ Restrict the accounts that can log in interactively
+ Limitation of account delegation rights for administrative accounts


 
* Restrict and protect local adminscounts

 
+ Local account restrictions for remote access
+ No network login for local accounts
+ Individual passwords for local admin accounts

** protected users **

R2 added the domain-based global security group Protected Users. The credentials of the members of this group are additionally protected by default more restrictive security settings.

Non-reconfigurable protection applies to all devices running Windows Server 2012 R2 and Windows 8.1 and to domain controllers in domains with a primary Windows Server 2012 R2 domain controller.

Credential storage footprint is significantly reduced by several limitations:

* NTLM, Digest Authentication or CredSSP are disabled.
* Kerberos does not use the weaker DES or RC4 encryption in pre-authentication.
* The account can not be delegated with restricted and unrestricted Kerberos delegation. This means that previous connections to other systems will fail if the user is a member of the Protected Users group.
* A four-hour ticket granting ticket life can be configured via Active Directory Management Center (ADAC) through authentication policies and silos, requiring the user to re-authenticate every four hours.
All human users should be members of the Protected Users group if possible.

Attention: Accounts for services and computers should not be members of Protected Users because the group does not provide local protection: password or certificate are always available on the system.

** Group "Managed Service Accounts" **

Managed Service Accounts (MSA) are one of the special features that have been added with Windows Server 2008 R2 and Windows 7. These are accounts for services (such as SQL Server or Exchange) in the Active Directory that are bound to a specific machine. The account has its own complex password and is managed automatically. Thus, an MSA can easily and securely perform services on a particular system while maintaining the ability to access resources on the network as a particular user principal. The Managed Service Account group created with Windows Server 2012 provides the same functionality in the domain, but with the added ability to span multiple servers.

Wherever possible, MSA should be used for service accounts, as well as the Managed Service Account group if possible in the sense of uniform configuration and complexity limitation.

** LSA - ** Protection in Windows Server 2012 R2

The Local Security Authority (LSA), which includes the Local Security Authority Server Service (LSASS) process, authenticates users to local and network logons and enforces local security policies. Windows 8.1 and Windows Server 2012 R2 provide additional protection mechanisms that make it difficult to read memory and inject code. This increases protection for credentials stored and managed in the LSA, such as pass-the-hash attacks. Smartcard data including PINs are also stored there.
To do this, enter a DWORD (32-bit) of the name "RunAsPPL" with content "1" in the registry under "HKEY \ _LOCAL MACHINE> SYSTEM> CurrentControlSet> Control> Lsa" and restart the server. Alternatively, this can also be done via a GPO (Computer Configuration> Windows Settings> Hive> ** HKEY \ _LOCAL \ _MACHINE> SYSTEM \ CurrentControlSet \ Control \ Lsa) **.

To check the successful setup, look for the following WinInit event in the Event Viewer under Windows Logs> System: "LSASS.exe was started as a protected process with level: 4".

In combination with Secure Boot, the protection is particularly secure, as it is generally enabled in UEFI, regardless of the contents of the registry.

** Dynamic access rules **

In Windows Server 2012, it has been possible to define dynamic access rules for files and folders for authorization. Since these can allow a much leaner and thus easier to maintain set of rules, their use should be checked and preferred, unless other, operational reasons speak against it.

#### SYS.1.2.2.M7 Security Check of Windows Server 2012

Even with Windows Server 2012 (R2), the actually effective security should be regularly audited, because only then can a complete implementation of the measures be reliably checked.

** Security Assessment Tools (Assessment Tools) **

In addition to the standard means technical configuration audit and penetration test (see module SYS.1.1 general server), Windows Server 2012 (R2) includes a number of tools that administrators can use to check the configuration. These should be used regularly and the results should be documented and used for planning the improvement.

** Microsoft Security Assessment Tool 4.0 **

The Security Assessment Tool is a so-called risk management application. This is realized as a two-part questionnaire. The first, shorter questionnaire is called Business Risk Profile and attempts to measure how much risk is associated with the institution's business. Since comparable procedures are used in IT-Grundschutz, an application can be dispensed with here. The second part is called "Assessment" and is more time-consuming to answer. The result is an evaluation of the effectiveness of the security strategy in the four areas of personnel, processes, resources and technology, based on best practices and standards such as ISO 27001 and NIST-800.x. Although this is already covered in the ITA policy, the recommendations generated by the tool may be worthwhile sources, especially due to additional references and references to material from Microsoft's Trustworthy Computing Group.

In addition, there is the possibility of anonymized upload of results in exchange for the download of benchmarks. In case of doubt, the upload should be avoided in order to prevent the possible disclosure of internal information.

** Microsoft Baseline Security Analyzer 2.3 **

The Baseline Security Analyzer provides an efficient way to detect a variety of common, security-related misconfigurations.

First, it checks for missing security-related updates (and only those) on Windows, Windows components such as Internet Explorer, IIS, other Microsoft products, such as SQL Server, and Office macro settings. The updates are queried via the Windows Update Agent, which has been available on all systems since Windows 2000 Service Pack 3. The test for so-called "less-secure settings", also known as Vulnerability Assessment (VA), is checked against a database of registry and file settings. For example, a VA might indicate that the permissions in a directory under / www / root are too lax
The executor needs local admin rights on the server to be scanned and the administrative shares must be activated.

** Security Configuration Wizard **

Since Windows Server 2003 Service Pack 1 on Windows Server systems, the Security Configuration Wizard (SCW) tool is available. It is used to review the server profile and generate recommendations for improving security. For Windows Server 2012 (R2), the SCW is in the new Server Manager dashboard.

Generally accepted basic recommendations such as "Disabling unused services" or "Uninstalling unused features" are also used in this module. But how is it verifiable in practice that a large number of servers with potentially dozens of roles on the network server and many different groups of file servers, web servers, databases, etc. are all configured for security best practice?

SCW can help reduce the attack surface by generating policies that limit a server to the minimal functionality needed for its role (s).

Generated policies can be applied directly or, as a recommendation, saved as an XML file. These can be accessed via the PowerShell via

scwcmd transform /p:TemplateMyServer.xml / g: GPO Hardening MyServer

Create a policy (GPO) that can then be applied to all servers with the same characteristics. As always, new settings should be critically appraised and tested on production systems before rolling out. The chance is that this will lead to a stronger standardization of the policies and reduce the configuration drift.

#### SYS.1.2.2.M8 System Integrity Protection

Secure Boot should be active. AppLocker should be enabled and configured as strictly as possible.

** Secure Boot **

Secure Boot is a security standard from the ranks of computer manufacturers. The procedure tries to ensure that only software that is trusted by the PC manufacturer is booted. This is realized by digital signatures on software components as well as a database maintained by the manufacturer of the computer.

When starting the PC, the firmware checks the signature of each component of the boot software, including the drivers and the operating system. Only if all signatures are valid, the boot process is completed, otherwise vendor-specific emergency measures come into play.

It is not possible to use Secure Boot with old, incompatible hardware or in a generally ineffective dual mode for server operation as well as with virtual machines that do not support Secure Boot.

Today's hardware and compatibility are generally reasonable enough that there is no reason not to use the valuable integrity protection that Secure Boot offers.

** ** AppLocker

AppLocker provides policy-driven access control for applications and other executables. This allows certain applications to be allowed while blocking others. Windows Server 2012 added the ability to define rules for application packages, allowing the configuration of AppLocker for apps from the Windows Store. Since R2, it is possible to monitor and record runtime information of processes that can be used to fine tune AppLocker (audit mode). This should be used to prevent failures, including locking out administrators from the system.
AppLocker is a powerful tool to significantly hinder the execution of malicious software. Despite various simplifications, however, there is still a considerable amount of configuration work, so that the use of AppLocker is especially recommended if there is a high degree of integrity or if the configuration of a server is relatively static. This is often the case for server systems running Windows 2012 (R2) that only have a role.

** Software Restriction Policies **

Software Restriction Policies (SRP) is an older feature that identifies programs that should run on computers in the domain. Like AppLocker, it can also be used to control the permitted software throughout the institution with great flexibility. SRP is required to configure software limitations for Windows Server 2008 R2 or Windows 7 operating systems that do not support AppLocker.

Like AppLocker, SRP is configured through GPOs. If both SRP and AppLocker policies in the same domain are applied through Group Policy, the SRP policies on computers that support AppLocker are overruled by the AppLocker policies.

Separate GPOs should always be used to configure SRP and AppLocker to eliminate errors and, in particular, facilitate troubleshooting.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### SYS.1.2.2.M9 Local Communication Filtering (CI)

Basically, central measures such as segmentation of networks, zoning and packet filtering in the corporate and government sector are usually realized by dedicated active network components that are set up at appropriate locations. However, in the sense of a staggered defense (defense-in-depth), the local firewall should be activated if more protection is required.

Windows Server 2012 (R2) includes a local firewall for this purpose, the so-called "Windows Firewall with Advanced Security (WFAS)". This should be activated and set as strictly as possible for incoming and outgoing traffic.

The WFAS can be managed by GPOs. This is recommended to keep the configuration consistent and central. The administration of concrete firewall rules is outside the scope of this building block. For this, the building block firewall is to be used.

Also implemented by WFAS are the native IPsec features of Windows Server 2012 (R2). These should be used to ensure the identity and integrity of the connection to remote systems, as this is not possible with packet filtering alone. The secure configuration of IPsec connections is also not content of this block. It is handled in the module VPN.

#### SYS.1.2.2.M10 Disk Encryption on Windows Server 2012 (C)
A suitable means of protecting the confidentiality of data at rest, not during transport, is the encryption of hard disks and other data carriers. It should be noted that the data must be decrypted for processing (for example, in the case of encryption of the boot medium already during the boot process) and always remain readable until the system is shut down or put into sleep mode. With server systems often running around the clock, protection is ultimately limited, but can be helpful against physical attacks such as theft of media when combined with appropriate other measures. Windows brings with it the tool BitLocker, which is also available in Windows Server 2012 (R2) in all editions.

BitLocker supports device encryption on x86 and x64-based systems that meet the requirements of the Windows Hardware Certification Kit (HCK) for a Trusted Platform Module (TPM) and Connected Stand-by Secure Boot. The device encryption protects both the operating system and other connected hard drives. Basically, device encryption can be used with a Microsoft account or a domain account.

BitLocker supports the AES-128-CBC and AES-256-CBC algorithms with Windows Server 2012 (R2). Encryption with BitLocker requires a key protector, which must be present in order to decrypt the drive. In the default configuration, these are a TPM module and an additional recovery key that can be used to decrypt the drive without the TPM module. For enterprise environments with an Active Directory, the recovery key can also be stored in the Active Directory.

** Windows Server 2012 **

In terms of previous versions, the capabilities of BitLocker in Windows 8 and Server 2012 have expanded:

**Installation**

BitLocker can now encrypt disks during installation. This is recommended because the system will not be in plain text for a while.

Administrators can enable BitLocker before installing the Windows Preinstallation Environment (WinPE). This is done with a random plaintext key applied to the freshly formatted disk before the setup process starts. Also newly added is the option "Used Disk Space Only", in which only the previously used memory is encrypted. This usually only takes a few seconds at this point and thus does not noticeably hinder the installation process.

The administrator can check the BitLocker status of a partition in the BitLocker Control Panel or in Windows Explorer. If a hard disk was initially encrypted with plain text keys during installation, the status "Waiting For Activation" is displayed with a yellow exclamation mark. This means that for complete protection of the partition, the key still needs to be protected. To do this, the administrator adds suitable key protection via the control panel, the manage-tool, or the WMI APIs.

** Key Protector **

For a complete BitLocker protection, the random encryption key itself must be protected. There are different variants for this:

** Used Disk Space Only **

BitLocker now offers two encryption methods, "Used Disk Space Only" and "Full Volume Encryption". The former works much faster during the initial encryption because initially only the already used blocks of the partition are encrypted. Full encryption always encrypts all blocks, including free space.

The following GPOs for BitLocker that enforce Used Drive Encryption or Full Volume Encryption are available in \ Computer Configuration \ Administrative Templates \ Windows Components \ BitLocker Drive Encryption
* Fixed Data Drives \ Enforce drive encryption type on fixed data drives
* Operating System Drives \ Enforce drive encryption type on operating system drives
* Removable Data Drives \ Enforce drive encryption type on removable data drives
If nothing is configured here, the administrator can decide freely if he activates BitLocker.

Under normal and high confidentiality requirements, partial encryption is usually sufficient. In the case of very high confidentiality requirements, a full encryption should always be selected, since even the changing amount of data, which in this case is easy to read, can reveal information about the data (a so-called side channel attack). Also for the achievement of the goal of repudiation a full encryption is recommended.

If the increased time required for full encryption has no negative impact on the deployment process, it should always be fully encrypted.

** PIN- ** and password change for standard users

This feature allows a standard user to change the BitLocker PIN or password on operating system partitions or the BitLocker password on data partitions themselves, which may help to reduce requests to support.

** Network Unlock **

This feature allows you to automatically decrypt a BitLocker-protected system over the network during bootup. Again, this can avoid requests for support and adds to the ease of use.

Technically, Network Unlock is a new option for key protection. This requires a DHCP driver implemented in the UEFI firmware.

Operating system partitions that are protected by TPM + PIN require manual entry of the PIN at boot time and awakening from hibernation. Eg with configured Wake-on-LAN. This makes it expensive, for example, to automatically roll out patches. Network Unlock provides a way to boot the machines without interaction.

Similar to TPM + StartupKey, an encrypted startup key is downloaded from the network and decrypted using the TPM. The network key is stored on a network system drive and encrypted with an AES 256-bit session key and the 2048-bit RSA public key of the server certificate. If Network Unlock is not available, the normal TPM + PIN input screen is displayed as usual. On the server side, the distribution of an RSA key pair via the Group Policy Management Console on the Server 2012 Domain Controller is required.

** Support for hardware encryption **

With Windows Server 2012, you can also manage other hardware-encrypted hard drives in the BitLocker console to create a common management interface.

** Windows Server 2012 R2 **

With Windows 8.1 and Server 2012 R2, the following enhancements to the BitLocker functionality were added:

Unlike the previous BitLocker implementation, so-called Device Encryption, which is also based on BitLocker in the background, is automatically enabled so that the device is encrypted from the beginning. This happens as follows:

During a clean installation of Windows Server 2012 R2, the server is prepared for first use. The device encryption is also initialized and the data carrier of the operating system and the other hard disks are first encrypted with a key stored in plain text. The security of the data at this time corresponds to a BitLocker encryption in standby mode (Suspended), in which the key is in plain text on the hard disk.
If the server is not added to a domain, it requires a Microsoft account that has been granted administrative rights on the server. Once the administrator logs in with the Microsoft account, the plain text key is deleted, a recovery key is uploaded to the Microsoft account (online), and TPM protection is created. If the recovery key is needed later (for example, if the TPM is damaged), the administrator can get it back using a second device and the Microsoft account.

If the user logs on via a domain account, the plaintext key is not deleted until the server has entered the domain and the recovery key then successfully created has been successfully saved in the Active Directory Domain Services. The Computer Configuration \ Administrative Templates \ Windows Components \ BitLocker Drive Encryption \ Operating System Drives GPO must be enabled and the "Do not enable BitLocker until recovery information is stored in AD DS for operating system drives" option should be selected. Only then does TPM protection become active, thus completing device encryption.

In use in government agencies and companies, the recovery key should be stored in the AD and the online variant with the Microsoft account should be omitted, since in the latter case there is no control over what happens with this key.

** FIPS support for the recovery password **

Since Windows Server 2012 R2, there is a FIPS mode that allows BitLocker to be compliant with the US Federal Information Processing Standard (Crypto) standard.

** BitLocker on virtual machines **

The encryption of virtual machines is useful if either the host system can not or should not be encrypted, or if the confidentiality requirement of the data in the VM is higher or should be shielded from the host system for other reasons. Again, hard disk encryption (FDE: Full Disk Encryption) does not provide effective protection against read-out of data during operation, i. H. with decrypted data carriers, represents. As an additional measure, it can therefore be specified in organizational terms that encrypted VMs may only be decrypted when they are needed and have to be shut down as soon as possible after use.

Because virtual machines do not have a TPM, the following two steps must be taken before BitLocker (which must be installed on the server) can be activated:

1. In the "Computer Configuration / Administrative Templates / Windows Components / BitLocker Drive Encryption / Operating System Drives" GPO, "Require additional authentication at startup" must be configured to "Enable" and "Allow BitLocker without a compatible TPM" (eg with the local Group Policy Editor gpedit.msc).

2. After restarting the VM, activate BitLocker in the Control Panel.

#### SYS.1.2.2.M11 Intrusion Detection on Windows Server 2012 (CIA)

It often turns out during security incident handling that the logging was insufficient to clarify the incident and plan countermeasures in a targeted manner. Common mistakes are:

* missing central logging,
* missing logging of member servers and endpoints (domain controllers only),
* Confusion caused by too much data in the log,
* missing recording of central events,
* too fast overrunning (rolling / rotating) of the logs.
For example, by default, central events such as logins are only logged to the system itself. The AD logs only the ticket creation, but has no picture of the session as such (including their beginning and end).

As a minimum requirement, the following events should be logged and evaluated by all systems:

* deleting security logs,
* Changes to critical groups such as domain administrators,
* Changes to local admin groups,
* creating and deleting local users,
* the installation of new services, especially on domain controllers (a possible sign of malware or lateral movement by attackers).
The first step to attack detection is the central collection of all relevant event data. Specially developed systems such as SIEM (Security Incident and Event Management) are usually expensive and expensive to set up and operate. You are not the subject of this building block. However, you can already achieve essentials with Windows Server on-board resources.

** Using the Windows Event Framework (WEF) **

With the Windows Event Framework (WEF), Windows has an integrated solution that can at least be used as a complement to a SIEM. Important basic functions of event monitoring can even be realized completely with WEF.

Event forwarding, ie the targeted automatic forwarding of events, can significantly increase the visibility of critical events, in particular those of remote servers or even clients that do not have agents of a proprietary monitoring system installed. The selection of which events should be centrally logged is to be seen outside of this block and as part of an overall logging concept (see block OPS1.1.7 Logging).

WEF can be configured with GPOs. Events can be exported in native .evtx format. This is XML-based and therefore easy to evaluate.

In push mode, systems automatically forward certain events to the Collector (server). Thus it is possible for administrators who are not security officers to configure additional events for the systems they are responsible for.

The setup only requires a Windows server and a GPO. In addition, the network service (only the local on the respective system) must be granted read access to the protocol and the WinRM service must be started on all systems to be monitored. He does not need to be (auto) -configured, which would leave him in the listening, rather vulnerable state. If only critical events are logged, then not very large log files can be expected.

Autoconfiguration is invoked on the Collector by the command "winrm qc" in an administrative prompt. Automatic start of the WinRM service should be activated on demand, the also queried automatic opening of the firewall can be done even more secure by GPO. Now incoming events can be viewed in the Eventviewer under "Subscriptions".

Subsequently, the events to be forwarded can be defined via GPO. Systems using the GPO will ask the Windows Event Collector if they have any subscriptions and only then send the desired events.

It is quite possible to collect the entirety of all domain security events in the WEF. This can be useful if no other central logging system is available and still forensic investigations should be possible. Otherwise, the strength of the WEF mainly lies in the targeted collection and filtering of critical events. Thus, a SIEM recording all events can be best complemented: the SIEM for completeness, WEF for visibility, even in areas of the environment that are not covered by the SIEM. The SIEM can then retrieve events from these at the collector and thus even better provide a uniform view of everything.

** Block after failed decryption attempts **

User accounts can be thresholded for how many login attempts are possible before the account is locked. This is a standard procedure to hinder brute force attacks. At the same time, there is a danger that locks will be deliberately provoked to achieve denial of service.
Since disk encryption is an extension of access protection to the data on hard drives, which can also be attacked by brute force, a comparable measure is possible here:

Since Windows 8 and Server 2012, the "\ Computer Configuration \ Windows Settings \ Security Settings \ Local Policies \ Security Options \ Interactive logon: Machine account lockout threshold" policy allows you to automatically lock partitions after a defined number of unsuccessful attempts to log in primary key protectors. After that, the volume can only be decrypted using the recovery key. This must be entered by an authorized user in the so-called "Device Lockout Mode", in which the system automatically reboots, to gain access again. It counts faulty login attempts on both Ctrl-Alt-Entf locked systems and password-protected screensavers.

The threshold can be selected between 4 and 999 (1-3 are automatically interpreted as 4), 0 disables the inhibit. The value should correlate with the threshold for the normal account lock and at least not be lower than this, so that after a normal account lock nor a normal unlocking of the account can be initiated.

#### SYS.1.2.2.M12 redundancy and high availability (A)

If there are particularly high availability requirements for a system running Windows Server 2012 (R2), then possible measures will essentially result from the particular application. For a file server, a distributed file system will represent a solution variant, for an Active Directory the use of multiple domain controllers and for a web server z. Eg load balancing. For the subject of high availability, reference should therefore be made in particular to the respective application modules.

In addition, there are some actions that can be taken at the operating system level of Windows Server 2012 (R2) to increase availability.

** Failover Cluster **

Several Windows servers can be operated in a network. Similar to the server roles that run on individual systems, there are also various cluster roles that can be operated in a failover cluster. One of the nodes of the cluster is always responsible for the operation of the role. If the node fails or loses connectivity, one of the other nodes takes over. The reliability can be increased, as in case of failure, another system takes over the operation. The list of roles that can be run directly on a cluster is relatively limited. However, virtual machines can also be run on a failover cluster so that entire systems that provide critical services can be made highly available as a virtual machine.

** Network Load Balancing **

The Network Load Balancing feature allows two or more Windows Server to provide network services over TCP / IP at a common address. The servers and services are independent and do not share resources. Network requests to the shared address are distributed to the servers in the federation.

** NIC teaming **

NIC teaming (by Network Interface Card), also known as Load Balancing / Failover (LBFO), allows multiple network interfaces to be grouped into so-called teams

a.) bundling bandwidth capacities and / or

b.) in the event of an interface or connection failure to have a failover for the network traffic.

Since Windows Server 2012, this technique is natively available in the operating system.

Since the topic of NIC teaming is varied and depends heavily on the concrete application scenario, only general information can be given in these implementation notes. For details on NIC teaming in Windows Server 2012 (R2), Microsoft therefore offers a "NIC Teaming User Guide".

** Basic function of NIC teaming **
Network adapters of the same speed can be combined into teams without additional tools as far as the manufacturers support the function. This is not possible with Bluetooth or WLAN adapters. The configuration takes place in the server manager or by PowerShell, also over the net.

The LBFO in Windows Server 2012 can not be combined with NIC teaming from other manufacturers. If problems occur in such a case, you can use PowerShell to delete the team configuration as follows:

Get-NetLbfoTeam | Remove-NetLbfoTeam

If virtualization with Hyper-V is used, the team process must be performed before creating virtual switches in Hyper-V, otherwise the physical network connection will no longer be available for the team process. In addition, here are more special features to note.

** NIC Teaming Architecture **

There are several architectures in which NIC teaming can be used. With switch-independent teaming, the switch does not know about team affiliation, but the NICs may or may not be connected to different switches. In switch-dependent teaming, where the entire team has to hang on the same physical switch, network cards and switches are configured for teaming. This can be done statically (a feature typically supported by server-enabled switches) or dynamically negotiated through the IEEE 802.1ax (Link Aggregation Control Protocol) protocol.

** Traffic distribution algorithms **

In order to be able to use the possible combined bandwidth, it is necessary to distribute the traffic sensibly to the network cards. Typically, this is done after address hashing, a procedure that pseudo-randomly distributes packets to their adapters based on their address information. When using virtualization, a much finer granular distribution can be achieved if in addition the Hyper-V virtual switch port is included in the distribution algorithm.

Depending on the setup and requirements, different combinations of architecture and distribution algorithm offer different advantages and disadvantages.

** Differences between Windows Server 2012 and 2012 R2 **

The main differences in terms of NIC teaming concern

* the addition of the dynamic load balancing mode (see above) and
* Improved interoperability and performance in connection with Hyper-V Network Virtualization (NVGRE).
** ** BranchCache

BranchCache is a technique for optimizing the use of transmission capacity in the WAN, e.g. B. in the connection of field offices. In order to save bandwidth, BranchCache copies content from central servers and caches it in the branch office (so-called caching) so that they no longer need to be transferred when accessed again.

BranchCache is based on deep functions of the Windows file server. So files are divided into small sections to find and eliminate duplicates. In particular, smaller changes in large files do not lead to a complete retransmission.

Configuration can also be done for larger institutions through a single small set of GPOs.

With Windows Server 2012 (R2), the cache is now encrypted, so that at least for normal confidentiality requirements on a further encryption about the volume can be waived.

In previous releases, server certificates were required, which required complex PKI operation. In the meantime these are no longer needed because encryption and authentication are solved differently.

#### SYS.1.2.2.M13 Strong Authentication with Windows Server 2012 (CI)

A role-based administration model for the administration of different server functions was to be designed and implemented. For critical services, two-factor authentication should be implemented.
** Role-based administration concept **

The distinction between administrators and ordinary users is important, but relatively crude. It disregards the fact that in reality there are different types of administrative tasks or, more generally, hierarchical and sometimes overlapping roles and responsibilities. To enforce the principle of least privilege more consistently, a finer granular role-based administration concept has to be developed. This is sensible and realistic, especially for larger institutions.

Such an administration concept can not be set up solely with regard to Windows Server 2012 (R2). Rather, different roles (different types of domain controllers, member servers, client systems, etc.) are to be considered. This attempt is made in the module APP.2.2 Active Directory.

** smart cards **

Smart cards are hard-to-copy mobile security features, such as two-factor authentication or signatures. With Windows Server 2012, the use of smart cards has been improved for greater integration into a larger number of applications. In addition, the option was added to use so-called virtual smart cards.

** Virtual Smart Cards **

Virtual smart cards enable multi-factor authentication in many types of infrastructures even in the event that users do not carry a physical card with them. For this, the process of registering any device with TPM as a virtual smart card device has been simplified, whether they are domain members or their hardware otherwise. This significantly reduces the hurdle for using smart cards as another authentication feature.

** Windows Biometric Framework **

The Windows Biometric Framework (WBF), a set of services and interfaces for biometric devices, has also been extended. Fast user switching and password synchronization with fingerprints are now possible.

However, it should be noted that biometric data have some disadvantages that make them largely unusable as identification and authentication features from a security point of view. In addition to the fact that many biometric features are not unique worldwide, they are often relatively easy to counterfeit and, above all, can not be changed.

#### SYS.1.2.2.M14 Shutting Down Encrypted Servers and Virtual Machines (CI)

If hard disks are encrypted to protect the confidentiality or integrity of data, ideally the key to decryption is not permanently available, but requires an administrator interaction or at least a logged technical request on the network or AD. Otherwise, an attacker or innate perpetrator can read out or manipulate the data during operation. For this, BitLocker or the device encryption must be activated in a mode that is not exclusively based on the TPM, and the additional key protection, such as a USB key, should not be permanently plugged. Although this increases the effort in operation, but represents a much higher hurdle for attackers.

3 Further information
------------------------------

### 3.1 Worth knowing

Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Additional information about threats and security measures in the "Windows Server 2012" area can be found in the following publications, among others:

* #### [LAPS1] Local Administrator Password Solution

  

 Microsoft Technet, (last accessed on 05.10.2017)
 <Https://technet.microsoft.com/en-us/mt227395.aspx>

 
* #### [LAPS2] Microsoft LAPS Security

  

 Active Directory Security, (last accessed 05.10.2017)
 <Https://adsecurity.org/?s=laps+security>
* #### [PAYNE] Windows Event Forwarding for everyone

  

 Microsoft Technet, Blog, Jessica Payne, 11.2015
 <https://blogs.technet.microsoft.com/jepayne/2015/11/23/monitoring-what-matters-windows-event-forwarding-for-everyone-even-if-you-already-have-a-siem />

 
* #### [TN730960] Security Tools to Administer Windows Server 2012

  

 Microsoft Technet, 06.2013
 <Https://technet.microsoft.com/en-us/library/jj730960.aspx>

 
* #### [TN831360] Secure Windows Server 2012 R2 and Windows Server 2012, Microsoft

  

 Micorosoft Technet, 11.2013
 <Https://technet.microsoft.com/en-us/library/hh831360.aspx>

 
* #### [TN831778] Security and Protection, Micorosoft

  

 Microsoft Technet, 02.2014
 <Https://technet.microsoft.com/en-us/library/hh831778.aspx>

 
* #### [TN832031] Secure Windows

  

 For Windows 8 / 8.1, mostly also applies to Windows Server 2012/2012 R2, 03.2014
 <Https://technet.microsoft.com/en-us/library/hh832031.aspx>
