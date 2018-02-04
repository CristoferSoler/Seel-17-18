[toc]
 
1 description
--------------

### 1.1 Introduction

With Windows Server 2012, Microsoft released a server operating system in September 2012 that brings several improvements in terms of security compared to previous versions of Windows (especially Windows Server 2008 R2). Technically, it is based not on the predecessor, but on the code base of the client operating system Windows 8. With the release Windows Server 2012 R2 from October 2013, the operating system was further improved and extended to Windows 2012 R2 to the server counterpart to Windows 8.1 make the client side.

This module is equally concerned with securing Windows Server 2012 and Windows Server 2012 R2, with relevant differences and peculiarities being appropriately pointed out. The spelling "Windows Server 2012 (R2)" is used if both versions are meant. The expiration date for Mainstream Support and Extended Support ("End-of-Life", EOL) is 09.01.2018 or 10.01.2023 in both cases.

### 1.2 Objective

The objective of this module is to protect information and processes that are processed or controlled by server systems based on Windows Server 2012 (R2) in regular operation.

### 1.3 Delimitation

The block Windows Server 2012 (R2) is to be applied to all target objects operating under the operating system Microsoft Windows Server 2012 (R2). It specifies and complements the aspects addressed in the SYS.1.1 General Server building block to specifics of Windows Server 2012 (R2) without repeating the requirements of the APP.2.2 Active Directory building block.

This building block assumes default integration into an Active Directory domain, as is common in businesses and government agencies. Special features of stand-alone systems are mentioned only occasionally, where the differences appeared to be particularly relevant.

Security requirements of possible server roles and functions such as file server (APP.3.3 file server), web server (APP.3.2 web server) or Exchange (APP.5.2 Exchange / Outlook) are the subject of our own components, just like the topic of virtualization (SYS.1.5 server virtualization) , This module is about the basic protection at the operating system level with on-board resources, regardless of the intended use of the server.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in Windows Server 2012 (R2):

### 2 1 Insufficient Planning for Windows Server 2012 (R2)

Windows Server 2012 (R2) is a complex, modern operating system that has a large number of features and configuration options. An example is the various powerful installable server roles. Each additional feature increases the attack surface and increases the likelihood of vulnerabilities and misconfigurations. There are also many degrees of freedom in the integration into the domain and the networking with other systems and services. Although modern Windows versions bring good default settings in many areas, the basic configuration is still not the safest in any case. Inadequate planning can lead to a large number of attack vectors, which attackers can easily exploit. In addition, if key decisions are not made prior to the installation, an insecure and undefined condition begins that is difficult to resolve.

### 2 2 Careless cloud use
Windows Server 2012 (R2) offers the ability to use cloud services in various places without having to install any third-party software. These include, for example, Microsoft Azure Online Backup or the online storage of BitLocker recovery keys. While cloud services can offer advantages in terms of availability in particular, careless use poses risks for confidentiality as well as dependence on service providers. Data on cloud services can thus be put in the hands of unauthorized third parties, whether attackers or state actors. If a cloud service is discontinued by the provider, this can have a significant impact on your own business processes.

### 2 3 Incorrect administration of Windows servers

Windows Server 2012 and Windows Server 2012 R2 have many new security-related features compared to the previous versions. For other features, subfunctions, parameters, or default configurations have changed. If the administrators are not sufficiently trained in the peculiarities of the systems, then configuration errors and malfunctions that can affect not only the functionality but also the security.

There is a particular danger of inconsistent Windows server security settings (eg with (SMB, RPC or LDAP).) If the configuration is not systematically and centrally planned, documented, checked and maintained, a so-called configuration drift threatens: The more the Concrete configurations of functionally similar systems move unfounded and undocumented, the more difficult it is to maintain an overview of the status quo and to maintain security holistically and consistently.

### 2 4 Improper use of Group Policy (GPOs)

Group Policy (GPO) is a useful and powerful way to configure many (security) aspects of Windows Server 2012 (R2), especially in a domain. Given the large number of possible settings, it is easy to accidentally set conflicting or incompatible settings or to forget topics. In the case of unsystematic procedures, this at least leads to malfunctions that are sometimes difficult to resolve, if not too serious, on the server or on connected client systems. In particular, misunderstood inheritance rules and filters can result in GPOs not being applied to a system at all.

### 2 5 Loss of encrypted data

When data is encrypted, such as when using BitLocker or device encryption on Windows Server 2012 (R2), it can result in complete data loss if the key is lost and there is no recovery key. Even a backup of encrypted data does not help here.

### 2 6 Loss of integrity of sensitive information or processes

Windows Server 2012 (R2) has a variety of features to help protect the integrity of information processed by the operating system. Each one of them can be fraught with weaknesses. In addition, there is often a lack of consistent configuration, not least for reasons of perceived ease of use or convenience. Information and processes can be falsified by unauthorized employees or external attackers and often even the traces are blurred. Often malware is also used to manipulate information remotely.

### 2 7 Software vulnerabilities or errors
Each software has vulnerabilities, the more so for complex systems like Windows Server 2012 (R2). Vulnerabilities in components can allow an attacker to inject malicious software, execute malicious software, or bypass security features. This can z. B. cause information to be manipulated or fall into the wrong hands. Any additional installed role or feature increases the chance that vulnerabilities will occur and be detected by attackers. Not all vulnerabilities are publicly known immediately and patches are not immediately available for all known vulnerabilities. In addition, they also have to be recorded first.

### 2 8 Unauthorized acquisition or misuse of administrator rights

Regular work under standard user rights for administrators is now good practice. However, as the administrator still has to increase his rights in certain places, an attacker can potentially intervene there and gain privileged rights. Also a misuse of rights by legitimate administrators is a relevant damage scenario. Since the roles are often very powerful, the impact is usually significant, especially for domain administrators. Even without guessing or breaking passwords, attackers can, for. B. by so-called pass-the-hash method read and abuse abusive credentials to move laterally in the network.

### 2 9 Compromise of remote access

Because Windows Server 2012 (R2) has a variety of ways to be remotely managed, they can generally be misused. Remote access, such. RDP user sessions may be reachable to third parties due to insecure or insecure protocols, weak authentication (e.g., weak passwords), or faulty configuration. As a result, the server and the information stored there can be largely compromised. In many cases, other IT systems connected to the server can also be compromised.

3 requirements
---------------

The following are specific requirements for protecting Windows Server 2012 (R2). Basically, the * IT operation * is responsible for fulfilling the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.1.2.2.A1 Planning for Windows Server 2012

The use of Windows Server 2012 (R2) MUST be carefully planned before installation. The requirements for the hardware MUST be checked before procurement. There must be a well-founded and documented decision for an appropriate Windows Server 2012 (R2) edition. The purpose of the server MUST be specified, including a planned integration into the Active Directory. The use of integrated into the operating system cloud services MUST be weighed and planned in principle. If not needed, the establishment of Microsoft accounts MUST be blocked on the server.

#### SYS.1.2.2.A2 Secure installation of Windows Server 2012

The installation medium MUST be obtained from a demonstrably integral source. NO other than the required server roles and features or functions may be installed. If sufficient in terms of functionality, the server core variant MUST be installed. Otherwise, MUST be justified, why the server core variant is not enough. As part of the installation, the server MUST first be brought to a current patch state.

#### SYS.1.2.2.A3 Secure Administration of Windows Server 2012
Local administration accounts MUST have unique, secure passwords. All administrators responsible for the server system MUST be trained in the security-related aspects of Windows Server 2012 or R2 administration. You MAY NOT use administrative rights where they are not mandatory. Browsers on the server MAY NOT be used to surf the web.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​Windows Server 2012. They SHOULD basically be implemented.

#### SYS.1.2.2.A4 Secure configuration of Windows Server 2012

It SHOULD NOT fulfill several essential functions or roles from a single server. Before commissioning, the system SHOULD be fundamentally hardened. For this purpose, function-specific institution-wide security templates SHOULD be created and maintained, which are rolled out to the server systems. The settings SHOULD be tested at the beginning and in case of changes before going live. Internet Explorer SHOULD ONLY be used on the server in Enhanced Security Configuration and Enhanced Protected Mode.

#### SYS.1.2.2.A5 Protection against malware

Except for Windows Server 2012 IT systems, which operate stand-alone without power and removable media, an antivirus program should be installed before connecting to the network or removable media for the first time. The signatures SHOULD be updated regularly. In addition, all hard drives SHOULD be completely scanned on a regular basis. It SHOULD have alerts configured for the administrators responsible for virus detections.

#### SYS.1.2.2.A6 Secure Authentication and Authorization in Windows Server 2012

In Windows Server 2012 R2, all users SHOULD be members of the Protected Users security group. Accounts for services and computers SHOULD NOT be a member of Protected Users. Service accounts in Windows Server 2012 (R2) SHOULD be members of the Managed Service Account group. The Local Credential Store LSA SHOULD be protected. The use of dynamic access rules on resources SHOULD be preferred.

Administrators of Windows Server 2012 (R2) SHOULD work on their own limited-access clients.

#### SYS.1.2.2.A7 Security Check of Windows Server 2012

The security configuration of Windows Server 2012 (R2) SHOULD be regularly reviewed, documented, and improved using appropriate tools.

#### SYS.1.2.2.A8 System Integrity Protection

Secure Boot SHOULD be active. AppLocker SHOULD be activated and configured as strictly as possible. The effects of changes SHOULD be tested in advance.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that go beyond the level of protection afforded by the state of the art and should BE considered AT INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.1.2.2.A9 Local Communication Filtering (CI)

The local firewall SHOULD be activated for incoming and outgoing network traffic and set as strictly as possible. The identity of remote systems and the integrity of the connections to these SHOULD be cryptographically secured.

#### SYS.1.2.2.A10 Disk Encryption on Windows Server 2012 (C)
For systems running Windows Server 2012 (R2), the disks SHOULD be encrypted with BitLocker or another product. This SHOULD also apply to virtual machines with productive data. With higher protection requirements, not only should the TPM serve as key protection alone. The recovery password SHOULD be stored in Active Directory or another suitable secure location. For very high confidentiality or deniability requirements, Full Volume Encryption SHOULD be done.

#### SYS.1.2.2.A11 Intrusion Detection on Windows Server 2012 (CIA)

Security events in Windows Server 2012 (R2) SHOULD be collected and evaluated at a central point. Encrypted partitions SHOULD be locked after a defined number of decryption attempts.

#### SYS.1.2.2.A12 Redundancy and High Availability (A)

It SHOULD check which availability requirements can be met or supported by operating system features such as Failover Cluster and Network Load Balancing or NIC Teaming (LBFO). For branch offices, BranchCache SHOULD be activated.

#### SYS.1.2.2.A13 Strong authentication with Windows Server 2012 (CI)

A role-based administration model for the administration of different server functions SHOULD be designed and implemented. For critical services, a two-factor authentication SHOULD be implemented.

#### SYS.1.2.2.A14 Shutting Down Encrypted Servers and Virtual Machines (CI)

In order to protect the encrypted data during operation, unused servers (including virtual machines) SHOULD always be shut down or put into hibernation. This should be done as automated as possible. The decryption of the data SHOULD require an interactive step, or it SHOULD at least be recorded in the security log.
