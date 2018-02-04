[toc]
 
1 description
--------------

### 1.1 Introduction

Active Directory Services (often abbreviated as AD or ADS) is a directory service developed by Microsoft and first introduced with the Windows 2000 Server operating system. Based on the Active Directory capabilities of the Microsoft Windows 2000 Server operating system, additional key features have been added to the Active Directory service with each release of the Windows Server family.

Active Directory is mainly used in IT networks with predominantly Microsoft components. Active Directory stores information about objects within an IT network, such as: Via users or computers, and makes it easier for users and administrators to provide, organize, use, and monitor this information. As an object-based directory service, Active Directory allows you to manage objects and their relationships with each other that make up the actual network environment. Active Directory provides central control and monitoring options for the respective network. The use of such a directory service is especially useful where z. B. the number of clients used in the network makes decentralized management difficult. Without a directory service, the reliability of locally made settings, such as: B. Implementation of the requirements of safety guidelines, due to the high staffing costs are no longer guaranteed. Administrative tasks within the network such. B. Password changes, account creation and access rights can be performed more efficiently by using a directory service.

### 1.2 Objective

This module aims to secure Active Directory in the regular operation of an institution (agency or company) that uses ADS to manage its infrastructure of Windows systems (client and server).

### 1.3 Delimitation

This module considers the threats and measures specific to Active Directory. General security recommendations for directory services can be found in the module APP.2.1 General directory service. The general measures described there are specified and supplemented in the present module. This module does not repeat the requirements of securing the operating systems of the servers and clients used for the operation and administration of the AD (eg SYS.1.2.2 Windows Server 2012 or SYS.2.2.3 client under Windows 10) and the underlying network infrastructure. Even processes such as data backup and patch management are treated only to the extent that special features are to be considered in the field of AD.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the Active Directory area:

### 2 1 Insufficient planning of safety limits

An AD instance creates a Forest as a top-level container for all domains of that instance. A forest can contain one or more domain container objects that share a common logical structure, global catalog, schema, and automatic transitive trust relationships. The forest thus represents the security boundary within which information is passed by default in the AD, not a single tree. If these boundaries are not planned consciously and in a structured manner, it can happen that information flows off unintentionally and the security concept of the institution fails. Therefore, it may be necessary to build more forests if different security requirements apply to parts of the infrastructure. However, this adds complexity in setup and administration.

### 2 2 Too many or too lax relationships of trust
If trust relationships between forests and domains are not regularly evaluated to determine whether they are still needed and justified, if they are of the correct type (ie, whether a two-way trust relationship is really necessary), and if the security controls are sufficient to ensure that they are guaranteed Issues with permissions occur and information flows away. In particular, if the default active SID (Security Identifier) ​​filtering is disabled, complex, hard-to-see vulnerabilities can occur. The same applies to the waiver of selective authentication in trust relationships between Forests.

### 2 3 Lack of security features due to older operating systems and domain functional level

Every new generation of the Windows Server operating system brings additional security features and enhancements to AD. In addition, the default settings are usually set more and more secure with each new release. Some of them are usable once the new system is installed, others only when the domain / forest functional level has been raised. The use of older operating systems as a (primary) domain controller or obsolete domain functional level thus prevents the use of modern security functions and increases the risk of unsafe default settings. An insecurely configured domain jeopardizes the information processed in it and facilitates attacks by third parties.

### 2 4 Operating additional roles and services on domain controllers

Any additional domain controller-side service, other than the AD itself, as well as less essential ancillary services such as DNS, increases the attack surface of these core infrastructure components through potential additional vulnerabilities and misconfigurations. These can be abused consciously or unconsciously, for. B. to copy information unauthorized or change.

### 2 5 Abuse of Domain Admins

The AD itself should only be managed by a very small number of administrators. Often, however, many more accounts than DA (domain administrator) are kept. These have full administrative rights on all domain controllers, workstations, group policies, etc. This will give attackers unnecessary leeway if one of these accounts can be taken over. Often, the DA's group includes service accounts and other groups that are not directly involved in the management of the AD itself.

### 2 6 Inadequate monitoring and documentation of delegated rights

By failing to systematically plan and implement the formation of and the right to delegate the rights of individual groups, the delegation can get out of control and give much more access than foreseen, which can be misused by third parties. Without regular auditing of the groups and their access rights, these rights threaten to over time. The use of standard groups and the delegation of their rights to their own groups (eg by delegating "Account Operators" to help desk staff) usually grant more rights than actually needed.

### 2 7 Unsafe authentication

So-called "legacy" (ie historical) authentication mechanisms in the area of ​​AD such as LM (LAN Manager) and NTLM (NT LAN Manager) v1 are considered insecure today and can easily be bypassed by attackers under certain conditions. This allows an attacker to gain and abuse rights without knowing, guessing or otherwise breaking user passwords, thus compromising the domain or parts of it.

### 2 8 Enroll AD administrators on low trust systems
It has to be assumed that malicious code reaches different systems such as normal workstations or servers. An attacker who gains access will be looking for other credentials that he can abuse. When privileged accounts log on to all kinds of IT systems, the attacker gains a variety of opportunities to grab the credentials and gain additional privileges, especially if the credentials are cached there.

### 2 9 Lack of supervision of privileged group membership

In most institutions, the number of accounts with administrative rights is steadily growing and is rarely or never adjusted. This violates the principle of least privilege and leads to more and more opportunities for attackers to gain and abuse additional privileges.

### 2 10 Too powerful or poorly secured service accounts

Application software vendors sometimes require DA privileges on service accounts to simplify testing and deploying their products, although significantly fewer rights would be required to operate. The additional rights of the service account can be exploited by attackers to move on to the domain. Because the credentials of a service running in the context of a service account are held in LSASS's protected storage, the attacker can extract them there. For example, a single low-security service account can compromise the entire domain.

In particular, this applies if the service account is secured with a weak password. For an attacker can easily request a TGS (Ticket Granting Service) ticket when using Kerberos authentication, in which the password of the service account is processed, and the latter offline break brute force.

### 2 11 Using the same local administrator password on multiple systems

Local accounts can log on to a system even if it is not connected to the domain. If the same credentials are used on multiple systems, the administrator can log on to the other systems as well. This increases the risk of an attacker on one of the systems finding and using domain credentials with higher privileges to compromise the domain.

### 2 12 Missing removal of unused accounts from AD

Attackers may prefer to use accounts that are no longer in use but still exist in AD for attacks, as abuse may not be noticed for a long time due to lack of ownership.
