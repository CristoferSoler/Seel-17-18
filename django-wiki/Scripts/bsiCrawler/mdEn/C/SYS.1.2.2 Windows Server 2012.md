Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

With Windows Server 2012, Microsoft released a server operating system in September 2012 that brings several improvements in terms of security compared to previous versions of Windows (especially Windows Server 2008 R2). Technically, it is not built on the predecessor, but on the code base of the client operating system Windows 8. With the release of Windows Server 2012 R2 from October 2013, the operating system was further improved and extended to Windows 2012 R2 to the server counterpart to Windows 8.1 make the client side.

This module is equally concerned with securing Windows Server 2012 and Windows Server 2012 R2, with relevant differences and peculiarities being appropriately pointed out. The spelling "Windows Server 2012 (R2)" is used if both versions are meant. The expiration date for Mainstream Support and Extended Support ("End-of-Life", EOL) is 09.01.2018 or 10.01.2023 in both cases.

### 1.2 Objective

The objective of this module is to protect information and processes that are processed or controlled by server systems based on Windows Server 2012 (R2) in regular operation.

### 1.3 Delimitation

The block Windows Server 2012 (R2) is to be applied to all target objects operating under the operating system Microsoft Windows Server 2012 (R2). It specifies and complements the aspects addressed in the SYS.1.1 General Server building block to specifics of Windows Server 2012 (R2) without repeating the requirements of the APP.2.2 Active Directory building block.

This building block assumes default integration into an Active Directory domain, as is common in businesses and government agencies. Special features of stand-alone systems are mentioned only occasionally, where the differences appeared to be particularly relevant.

Security requirements of possible server roles and functions such as file server (APP.3.3 file server), web server (APP.3.2 web server) or Exchange (APP.5.2 Exchange / Outlook) are the subject of our own components, just like the topic of virtualization (SYS.1.5 server virtualization) , This module is about the basic protection at the operating system level with on-board means independent of the intended use of the server.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in Windows Server 2012 (R2):

### 2 1 Insufficient Planning for Windows Server 2012 (R2)

Windows Server 2012 (R2) is a complex, modern operating system that has a large number of features and configuration options. An example is the various powerful installable server roles. Each additional feature increases the attack surface and increases the likelihood of vulnerabilities and misconfigurations. Integration into the domain and networking with other systems and services are also very many degrees of freedom. Although modern Windows versions bring good default settings in many areas, the basic configuration is still not the safest in any case. Inadequate planning can lead to a large number of attack vectors, which attackers can easily exploit. In addition, if key decisions are not made prior to the installation, an insecure and undefined condition begins that is difficult to resolve.

### 2 2 Careless cloud use
Windows Server 2012 (R2) offers the ability to use cloud services in various places without having to install any third-party software. These include, for example, Microsoft Azure Online Backup or the online storage of BitLocker recovery keys. While cloud services can offer benefits in terms of availability in particular, careless use poses risks to confidentiality and dependence on service providers. Data on cloud services can thus be put in the hands of unauthorized third parties, whether attackers or state actors. If a cloud service is discontinued by the provider, this can have a significant impact on your own business processes.

### 2 3 Incorrect administration of Windows servers

Windows Server 2012 and Windows Server 2012 R2 have many new security-related features compared to the previous versions. For other features, subfunctions, parameters, or default configurations have changed. If the administrators are not adequately trained in the special features of the systems, configuration errors and malfunctions that could impair safety as well as functionality are at risk.

There is a particular danger of inconsistent Windows server security settings (eg in the case of (SMB, RPC or LDAP).) If the configuration is not systematically and centrally planned, documented, checked and maintained, a so-called configuration drift threatens: the more Concrete configurations of functionally similar systems move unfounded and undocumented, the more difficult it is to maintain an overview of the status quo and to maintain security holistically and consistently.

### 2 4 Improper use of Group Policy (GPOs)

Group Policy (GPO) is a useful and powerful way to configure many (security) aspects of Windows Server 2012 (R2), especially in a domain. Given the large number of possible settings, it is easy to accidentally set conflicting or incompatible settings or to forget topics. In the case of unsystematic procedures, this at least leads to malfunctions that are sometimes difficult to repair, if not too serious, on the server or on connected client systems. In particular, misunderstood inheritance rules and filters can result in GPOs not being applied to a system at all.

### 2 5 Loss of encrypted data

When data is encrypted, such as when using BitLocker or device encryption on Windows Server 2012 (R2), it can result in complete data loss if the key is lost and there is no recovery key. Even a backup of encrypted data does not help here.

### 2 6 Loss of integrity of sensitive information or processes

Windows Server 2012 (R2) has a variety of features to help protect the integrity of information processed by the operating system. Each one of them can be fraught with weaknesses. In addition, there is often a lack of consistent configuration, not least for reasons of perceived ease of use or convenience. Information and processes can be falsified by unauthorized employees or external attackers and often even the traces are blurred. Often malware is also used to manipulate information remotely.

### 2 7 Software vulnerabilities or errors
Each software has vulnerabilities, the more so for complex systems like Windows Server 2012 (R2). Vulnerabilities in components can allow an attacker to inject malicious software, execute malicious software, or bypass security features. This can z. B. cause information to be manipulated or fall into the wrong hands. Any additional installed role or feature increases the chance that vulnerabilities will occur and be detected by attackers. Not all vulnerabilities are publicly known immediately and patches are not immediately available for all known vulnerabilities. In addition, they also have to be recorded first.

### 2 8 Unauthorized acquisition or misuse of administrator rights

Regular work under standard user rights for administrators is now good practice. However, as the administrator still has to increase his rights in certain places, an attacker can potentially intervene there and gain privileged rights. Also a misuse of rights by legitimate administrators is a relevant damage scenario. Since the roles are often very powerful, the impact is usually significant, especially for domain administrators. Even without guessing or breaking passwords, attackers can, for. B. by so-called pass-the-hash method read and abuse abusive credentials to move laterally in the network.

### 2 9 Compromise of remote access

Because Windows Server 2012 (R2) has a variety of ways to be remotely managed, they can generally be misused. Remote access, such. RDP user sessions may be reachable to third parties due to insecure or insecure protocols, weak authentication (e.g., weak passwords), or faulty configuration. As a result, the server and the information stored there can be largely compromised. Often, other IT systems connected to the server can also be compromised.

