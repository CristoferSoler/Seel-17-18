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

An AD instance creates a Forest as a top-level container for all domains of that instance. A forest can contain one or more domain container objects that share a common logical structure, global catalog, schema, and automatic transitive trust relationships. So the forest represents the security boundary within which information is passed by default in the AD, not a single tree. If these boundaries are not planned consciously and in a structured manner, it can happen that information flows off unintentionally and the security concept of the institution fails. Therefore, it may be necessary to build more forests if different security requirements apply to parts of the infrastructure. However, this adds complexity in setup and administration.

### 2 2 Too many or too lax relationships of trust
If trust relationships between forests and domains are not regularly evaluated to determine whether they are still needed and justified, if they are of the correct type (ie, whether a two-way trust relationship is really necessary) and if the security controls are sufficient to ensure that they are guaranteed Issues with permissions occur and information flows away. In particular, if the default active SID (Security Identifier) ​​filtering is disabled, complex, hard-to-see vulnerabilities can occur. The same applies to the waiver of selective authentication in trust relationships between Forests.

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

3 requirements
---------------

The following are specific requirements for protecting Active Directory. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The ISB should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### APP.2.2.A1 Active Directory Planning [Responsible Person]

It MUST select a suitable, highest possible domain functional level. The justification SHOULD be suitably documented. An on-demand Active Directory authorization concept MUST be designed. Administrative delegations MUST be equipped with restrictive and needs-based permissions. The planned Active Directory structure including any schema changes SHOULD be documented in a comprehensible way.

#### APP.2.2.A2 Active Directory Administration Planning [Specialists]

A role-based authorization concept MUST be created. All administrative tasks and permissions SHOULD be suitably documented.
In large domains, there must be a distribution of administrative users regarding service management and data management of Active Directory. In addition, the administrative tasks in the Active Directory MUST be distributed without interference according to a delegation model.

#### APP.2.2.A3 Planning Group Policy on Windows

There must be a concept for setting up group policies. Multiple overlaps MUST be avoided as far as possible in the group policy concept. Documenting the group policy concept MUST allow exceptions to be detected. All GPOs MUST be protected by restrictive access rights. The parameters in all GPOs MUST have safe default settings.

#### APP.2.2.A4 Active Directory Administration Training

Administrators MUST be familiar with all of the security mechanisms and aspects of Active Directory in their field of activity. You SHOULD be trained to work with Active Directory prior to setup and regularly.

#### APP.2.2.A5 hardening of Active Directory

Built-in accounts MUST have complex passwords and serve as emergency accounts only. Privileged accounts MUST be members of the Protected Users group. Service accounts MUST use Group Managed Service Accounts.

For all domain controllers, restrictive access rights MUST be assigned at operating system level. The Active Directory Restore Mode MUST be protected by a suitable password. Working in this mode SHOULD only be done in compliance with the four-eye principle.

It SHOULD periodically create an image of the domain controller. The permissions for the Everyone group MUST be limited. The domain controllers MUST be protected against unauthorized reboots.

Domain and domain controller policies MUST include secure passwords, account lockout, Kerberos authentication, user rights, and auditing. A sufficient size for the security protocol of the domain controller MUST be set. For external trusts to other domains, user authorization data MUST be filtered and anonymized.

#### APP.2.2.A6 Maintaining the operational security of Active Directory

All trust relationships in AD MUST be evaluated on a regular basis.

The service administrators on the domain controller MUST have only the necessary rights. These rights MUST be reviewed periodically. The group of domain administrators MUST be empty or as small as possible. Unused accounts MUST be disabled or deleted in AD.

All necessary parameters of Active Directory SHOULD be kept up-to-date and traceable as basic information.

#### APP.2.2.A7 Implementing Secure Management Methods for Active Directory [Specialists]

Administrator accounts MUST NOT be used for ordinary daily work. Server Administrator accounts MUST NOT be used on workstations. Domain Administrator accounts MUST NOT be used on workstations or servers.

Each account MUST be clearly assigned to an employee.

The number of Active Directory service administrators and data administrators MUST be reduced to the minimum of trusted individuals. Your accounts MUST be adequately secured.

The default account "Administrator" SHOULD be renamed and an unprivileged account named "Administrator" SHOULD be created. Everyday, non-administrative tasks MUST be done with unprivileged user accounts.

It MUST be ensured that the administration of service administrator accounts is done exclusively by members of the service administrator group. The group "Account Operators" SHOULD be empty.
Administrators SHOULD only be assigned to the Schema Admins group temporarily for the duration of the schema changes. For the groups "Organization Admins" and "Domain Admins" for the administration of the root domain, a four-eye-principle SHOULD be established.

The workstations for the administration of Active Directory MUST be adequately secured. For remote administration of the domain controllers, the traffic MUST be properly encrypted.

It MUST be ensured that the Administrators or Domain Administrators groups own the domain root object of each domain.

The use of domain-local groups for the control of read authorization for object attributes SHOULD be avoided.

The trash of the AD SHOULD be activated.

In large institutions, an enterprise identity management solution should ensure that the rights of all users are defined.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of Active Directory. They SHOULD be implemented in principle.

#### APP.2.2.A8 Configuring the secure channel under Windows

The secure channel under Windows SHOULD be configured according to security requirements and local conditions. All relevant group policy parameters SHOULD be considered.

#### APP.2.2.A9 Protection of authentication when using Active Directory

In the environment of the Active Directory STRICTLY the authentication protocol Kerberos SHOULD be used. If transitional NTLMv2 is used for compatibility reasons, then the migration to Kerberos SHOULD be scheduled and scheduled. The LM authentication SHOULD be deactivated. The SMB traffic SHOULD be signed. Anonymous access to domain controllers SHOULD be prevented.

#### APP.2.2.A10 Secure use of DNS for Active Directory

Integrated DNS zones or secure dynamic update of DNS data SHOULD be used to prevent DNS client queries from unauthorized systems. The access to the configuration data of the DNS server SHOULD only be allowed by administrative accounts. The DNS cache on the DNS servers SHOULD be protected against unauthorized changes. Access to the DNS service of the domain controllers SHOULD be limited to the necessary extent. Network activities related to DNS requests SHOULD be monitored. Access to DNS data in Active Directory SHOULD be restricted to administrators using ACLs.

Secondary DNS zones SHOULD be avoided. At a minimum, the zone file SHOULD be protected from unauthorized access.

If IPsec is used to secure the DNS communication, sufficient data throughput in the network should be ensured.

#### APP.2.2.A11 Active Directory Infrastructure Monitoring

The Active Directory infrastructure SHOULD be monitored and logged based on native events. The results of the security monitoring of the Active Directory SHOULD be evaluated regularly. The availability and system resources of the domain controllers SHOULD be monitored. Changes at the domain level and in the forest of the Active Directory SHOULD be monitored, logged and evaluated.

#### APP.2.2.A12 Data backup for domain controllers

There SHOULD exist a domain controller backup and restore policy. The backup software used SHOULD be explicitly released by the manufacturer for the backup of domain controllers. For the domain controllers SHOULD be set up a separate backup account with service administrator rights. The number of members of the group "Backup Operators" SHOULD be limited to the necessary level. Access to the AdminSDHolder object SHOULD be specially protected to protect permissions.
The data of the domain controllers SHOULD be backed up at regular intervals. A method should be used that largely avoids obsolete objects.

The backup media SHOULD be stored in a suitable location. The correct procedure and the re-loading of data backups of the domain controllers SHOULD be checked at regular intervals.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.2.2.A13 Two-Factor Authentication (CIA)

Privileged accounts in the area of ​​AD SHOULD be protected by means of two-factor authentication.

#### APP.2.2.A14 Dedicated Privileged Administration Systems (CIA)

The administration of Active Directory SHOULD be restricted to dedicated administration systems. These should be hardened by the limited task particularly strong.

#### APP.2.2.A15 Separation of administration and production environment (CIA)

Particularly critical systems, such as domain controllers and domain administration systems, SHOULD be spun off into their own forest, which has a one-sided trust in the direction of the production forest.
