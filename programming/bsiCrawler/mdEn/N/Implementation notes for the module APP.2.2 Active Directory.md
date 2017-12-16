1 description
--------------

### 1.1 Introduction

The Active Directory is the central data store for all administrative data of a domain based on the server operating systems Windows Server since version Windows 2000 Server. From an abstract perspective, Active Directory is a hierarchical and tree-based object-based database. It is based on the directory service standard X.500, from which it has borrowed the internal structure and structure. However, it is not an X.500 compatible directory service. Active Directory is often abbreviated to "AD" or "ADS" (* Active Directory Services) *.

### 1.2 Life cycle

For the successful construction and operation of a secure Active Directory, a number of measures have to be implemented, beginning with the conception through the installation to the operation. The steps to be taken and the actions to follow in each step are listed below.

** planning and conception **

As a starting point, it is advisable, if you are not already adequately qualified, to first look at the APP.2.2.A4 Active Directory Administration training course, which provides an overview of the structure and terminology of an Active Directory.

Before the actual establishment of the Active Directory, the organizational structure of the institution must be determined in advance in order to derive from it the most optimal configuration possible for the Active Directory. The measure APP.2.2.A1 Planning of the Active Directory explains the procedure in the planning phase and the domain concept of Active Directory.

APP.2.2.A2 Active Directory Administration Planning addresses the basic structure of managing a domain and communicates the tasks and applications of each administrative role. Furthermore, the organizational structure and the rights customization of administrative user accounts of an Active Directory are explained.

Action APP.2.2.A3 Windows Group Policy Planning addresses the group policies for Windows operating systems that can also be managed through Active Directory.

**Procurement**

With regard to procurement, no separate requirements must be fulfilled that go beyond the module APP.2.1 General directory service. It is only to be noted that certain security features are only made possible by newer versions of AD, and thus by the use of newer versions of Windows Server, which may influence procurement decisions (see APP.2.2.A1 Active Directory Planning).

**Implementation**

In order to obtain a uniform security standard, the measure APP.2.2.A7 Implementation of secure administration methods for Active Directory must be observed. Furthermore, the persons responsible for the administration of the directory service on the basis of APP.2.2.A4 Training for Active Directory Administration are to be made familiar with the task areas assigned to them.

Due to their central importance for the entire network environment, the domain controllers of an institution should be sufficiently hardened (see APP.2.2.A5 hardening of the Active Directory). This includes in particular the establishment of the secure channel between DCs, servers and clients (APP.2.2.A8 configuration of the secure channel under Windows) and the other requirements from APP.2.2.A9 Protection of the authentication when using Active Directory.

To ensure the integrity of a productively deployed Active Directory environment by securing the DNS components, you must consider APP.2.2.A10 Secure DNS for Active Directory.

**Business**
In addition to the underlying operating system, the Active Directory itself must be carefully administered (see APP.2.2.A6 Maintaining the operational security of Active Directory) to ensure that the relevant systems of the information network are kept up to date.

In order to be able to react promptly to emerging problems, the corresponding measure APP.2.2.A11 Monitoring of the Active Directory infrastructure should be taken into account. This not only deals with the feedback on exceeding defined thresholds, but also with the logging of system changes.

### rejection

With regard to the sorting, no separate requirements must be observed, which go beyond the module APP.2.1 General directory service.

### Emergency preparedness

Aspects of contingency planning for Active Directory are covered in the ACT.2.2.A12 Domain Controller Data Protection.

2 measures
-----------

The following are specific implementation notes in the "Active Directory" section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### APP.2.2.M1 Active Directory Planning [Responsible Person]

An essential prerequisite for the safe use of Active Directory is adequate planning in advance. Planning for an Active Directory can be done in several steps. First of all, a rough concept for the structure of the domain was created and, based on this, the individual sub-aspects were specified. Planning does not only concern aspects that are classically linked to the term security, but also normal operational aspects that may entail safety requirements. Information about the structure and the basic structure of an Active Directory is provided by the action APP.2.2.M4 Training on Active Directory Administration.

As part of Active Directory planning, the following aspects must be considered:

* Which version of the AD (Domain Functional Level) is needed to set up the required security features.
* Which Active Directory structure should be chosen in the sense of the division into domains and which arrangement of the domains in Trees and Forests?
* Which users and computers should be summarized in which domains?
For each domain, it must be decided

* which OU objects should exist, how they should be arranged hierarchically and which objects they should receive,
* what security groups are needed and how they are grouped into OUs,
* which administrative model is implemented (central / decentralized administration),
* whether and to whom administrative tasks should be delegated,
* which security settings should apply to different types of computers and user groups,
* What group policy settings are required and how the group policies are distributed (see Planning Group Policy).
* which trusts are automatically generated by Windows server and which additional trusts (eg to NT domains or external Kerberos realms) need to be set up,
* which Active Directory information can be accessed by whom through the various Active Directory interfaces (eg ADSI, LDAP) and
* Which Active Directory objects should be included in the so-called Global Catalog, which can be accessed globally in a forest.
Generally, the planned Active Directory structure must be appropriate, i. H. also for expert third parties with a short training period understandable, documented. This contributes significantly to the stability, consistent administration and thus to system security. In particular, it is recommended to note which schema changes are made. The reasons for the change should also be documented.

** Security Features of AD by Operating System or Domain Functional Level **

Every new generation of the Windows Server operating system brings additional security features and enhancements to AD. In addition, the default settings are usually set more and more secure. Some of them are usable once the new system is installed, others when the domain / forest functional level has been raised.

It should always operate as high a domain functional level. At least this should be so high that all safety functions can be offered, which are needed to ensure the necessary protection requirements. The decision for a Domain Functional must be reasonably made and documented and should be reviewed regularly.

The most important new security functions or extensions of those with the last Windows Server versions up to 2012 R2 were the following:

Windows Server 2008 R2 Domain Functional Level:

* Support for Kerberos AES encryptionThis will remove RC4 support from Kerberos. Also, Windows 7 and Windows Server 2008 R2 no longer support DES on Kerberos.
* Managed Service Accounts AD manages the passwords of these service accounts themselves
* Authentication Mechanism Assurance
 Users receive additional group memberships only after authentication via smartcard
Windows Server 2012 Domain Functional Level:

* Managed Service Accounts AD manages the passwords of these service account groups themselves
* Compound Authentication and Kerberos FAST (Kerberos Armoring)

 
+ Combines user and device authentication
+ Protects Kerberos AS and TGT requests.


 
Windows Server 2012 R2 Domain Functional Level:

* Authentication policies and silos
 Protects privileged accounts by restricting where they can log in
* Security group protected users (Protected Users)

 
+ Primary DC (PDC) must be Windows 2012 R2 to get the group
+ Protected Users Host Protection (with Windows 8.1 and 2012 R2) prevents the following on systems:


- Authentication via NTLM, Digest Authentication or CredSSP
- Caching of credentials
- DES and RC4 at Kerberos Pre-Authentication
- Delegation of accounts



+ Protected Users Domain Enforcement prevents users from:


- NTLM authentication.
- DES and RC4 at Kerberos Pre-Authentication
- becoming a delegate
- A renewal of Kerberos TGTs beyond the initial four-hour deadline (then re-authenticate)





 
**Documentation**

For each Active Directory object should be documented:

* Name and position in the Active Directory tree (eg "LocationBerlin", Father object: OU "Branch Germany")
* which purpose the object serves (eg group of users with RAS access to RAS server 1)
* which administrative access rights are to be assigned for the object and its attributes (eg completely managed by "Admin1")
* how to configure the inheritance of Active Directory rights, eg B. Blocking rights inheritance (see also Active Directory Administration Planning, Active Directory Administration Training)
* which GPOs affect this object (see Planning Group Policy)
The planning of the Active Directory administration and the used administrative model has an important role to play. Recommendations can be found summarized in Measure Planning Active Directory Administration.

The security-relevant core aspects of Active Directory planning are summarized:

* Domains limit the administrative power of administrators. As a result, administrators can only act within one domain, so by default, their management authority does not extend beyond the domain boundary. This is especially true in the context of several domains (tree, forest), so that the often voiced concerns that the standard transitive trust model also administrative permissions across domain boundaries are possible, can be eliminated for normal administrator accounts (see, however, organizational admins below) ,
* Cross-domain access assumes that access permissions for the accessing party from another domain are explicitly set up in the target domain. By default, no cross-domain accesses are possible.
* This means that in a tree or forest an administrator of domain "A" can only administratively access any other domain "B" if the domain administrator of "B" explicitly grants permissions to the administrator of domain "A" ( see however organizational admins).
* Members of the Enterprise Admins group enjoy special status because they have administrator rights to Active Directory throughout the forest. In particular, set access rights to Active Directory objects are ignored when accessing organizational admins. The membership of the group of organizational admins therefore has to be restricted and strictly controlled. It should be noted that an organization admin is needed, for example, to create a subdomain.
* Administrative delegation is achieved by granting access to Active Directory objects and their attributes. The distribution of access rights must be according to the administrative model. The mechanisms for access rights in the Active Directory (inheritance, control of inheritance, scope of access settings) can be used to set up very complex authorization structures. These can very quickly become confusing and no longer administrable, so that incorrect configurations in the Active Directory can lead to security gaps. A simple authorization structure is therefore preferable.
 In order to safely plan and deploy delegation, it is recommended to first identify and document the actual requirements in the form of minimum rights that are actually required, for example, initially in linguistic-textual form, and then to translate these into technical access rights.
* Schema changes are critical operations and may only be performed by authorized administrators after careful planning.
Finally, it should be noted that errors in the Active Directory planning and the underlying concepts after installation can be corrected only with considerable effort. Subsequent changes in the Active Directory structure, such as For example, the placement of domains in trees and forests may require the complete rebuilding of domains.

** Active Directory Federation Services (ADFS) **
Active Directory Federation Services (abbreviated to ADFS or ADFS) is another Microsoft software component and part of the ADS that enables mapping federated or federated identities. These are features that enable single sign-on access to systems across institutional boundaries. Since Windows Server 2012, the feature is available as a role in the system and does not require additional installation. Since Windows Server 2012 a management via PowerShell is possible, since 2012 R2 also an integration with OAuth 2.0.

ADFS establishes a trust relationship between two (or more) organizations. A federation server on the one hand can then provide a user with standard means, e.g. B. at the AD, and then equips him with a token that contains certain "claims" (assurances). This can be shown by the user to gain permissions in the other organization.

ADFS is gaining in importance as it has a natural ability to integrate with cloud services. So it can be z. B. in connection with the Microsoft service "Azure AD" are used. Interaction is also possible with other WS - * or SAML 2.0 compliant federation services.

The use of federation in general and ADFS in particular should be justified, thoroughly planned and documented. This concerns in particular the necessary trust relationships. These should be chosen minimal and regularly evaluated. The risks of misuse of rights granted by authentication or authorization in another organization should be systematically described, assessed and appropriately handled.

If cloud services are used, the appropriate building blocks must also be used (in particular OPS.2.2 cloud usage and OPS.3.2 cloud management).

#### APP.2.2.M2 Active Directory Administration Planning [Specialists]

The Active Directory consists of various objects that are organized like a tree. Each object consists of specific attributes that store the object information. Objects are used to manage a Windows system, which must be done by an authorized administrator. Permissions can be assigned for all Active Directory objects that control access to the objects. This can be used to specify which objects can be changed by which users in a certain way, such as the creation of users or the resetting of user passwords.

In a default installation, only administrators have the right to make changes to objects and thus manage a domain. Users usually have maximum read access.

Generally, under Windows Server, the administrative power of the domain administrators also ends at the domain boundary. Only the members of the group Enterprise Admins have full access to all AD objects in every domain of a forest, regardless of the access rights set for these objects. By default, these are the members of the Forest Root Domain (FRD) Administrators group.
In large domains, it is advisable to delegate administrative tasks, so that the administrative burden is distributed among several administrators or, in some cases, a role separation can be implemented. The delegation of administrative tasks takes place in the Active Directory by assigning appropriate access rights to Active Directory objects for the respective administrator groups. The Active Directory right structure allows fine granular rights. In this way, z. For example, an administrator may be allowed to create user accounts and reset user passwords, but not delete user accounts or move them to other organizational units (OUs). In order to simplify the assignment of uniform rights within a complete subtree, it is also possible to inherit rights of an object to objects in the subtree. Since the inheritance of inherited rights by certain objects in the subtree may not be desired, the takeover for objects can also be blocked, so that quite complex scenarios for the distribution of authorizations can arise here (see also APP.2.2.A4 Training on Active Directory administration).

From a security perspective, there are the following aspects to consider when planning Active Directory administration:

* Where delegation is used, only the essential rights required to carry out the delegated administrative activities should be assigned.
* The delegation model and the resulting rights assignments must be documented.
* The administrative activities should be delegated in a way that does not overlap as much as possible. Otherwise, two administrators can make conflicting changes. This leads to replication conflicts, which are automatically resolved by Windows servers, so that one of the changes prevails in any case. However, there are no warnings for this case. It is therefore advisable to design the administration model in such a way that competences that are as non-overlapping as possible exist. In this way, the risk of replication conflicts can be reduced. If replication conflicts are to be expected or have already occurred, a manual check should be carried out at regular intervals or after important changes to determine whether the correct values ​​have always prevailed. Whether the management of an evidence database with the target Active Directory data may make organizational sense, must be decided on a case-by-case basis.
* If the administration of the Active Directory is delegated, this is achieved by granting appropriate access rights within the Active Directory. Typically, the inheritance mechanism is used to manage permissions on objects in subtrees. Complex scenarios with delegation and thus rights inheritance should, however, be avoided at all costs, as otherwise security vulnerabilities can easily arise. For example, it may happen that a user has too few or too many rights.
* A concept for membership in the various administrative groups must be drafted. In particular, the conditions and procedures that define whether, when and how long a user or a user group is included in an administrative group must be defined. Particular care must be taken to restrictively manage and control the membership of the Enterprise Admins group. If the organizational flow permits, it may be considered to remove all members in that group after building the domain structure and to add members only when needed and in compliance with the four-eyes principle. However, it must be remembered that a member of the Enterprise Admins group is needed whenever a new domain is to be created in the forest.
* Administrators must be informed about and trained in the Active Directory structure and organizational processes as part of their administrative work to prevent non-compliant changes leading to security vulnerabilities. For example, when creating a new user, it may be necessary to include it in corresponding security groups or even create a new security group with a special name. If this is forgotten, users may be given incorrect permissions.
* Large domains should be considered to support their management with appropriate tools. There are several commercial and freely available tools that facilitate Active Directory administration. It should be considered to use these. If such tools are used, it must be ensured that Active Directory management is performed exclusively via these tools.
** Role-based authorization concept **

A role-based authorization concept should be implemented that grants granular control over each account's entitlement.

All authorizations should be assigned based on roles. In practice, this means creating security groups to which permissions are attached. Next, groups are created that represent roles and are linked to the necessary previously created security groups. Finally, user accounts are assigned to groups that match their role. In addition, an enterprise identity management solution can ensure, especially in large institutions, that the rights of all users correspond to defined specifications.

** Separation of the administration of services and data of an Active Directory **

The administrative activities for Windows server operating systems can basically be divided into the two roles "service management" and "data management" with different areas of responsibility.

The term "service management" refers to the support of the Active Directory service itself. Service administrators manage the domain controllers, e.g. For example, installing OS-level updates and configuring Active Directory, such as directory-wide settings such as trusts or replication architecture.

The management of data in the Active Directory or Active Directory forest member machines should be done by the data administrators. The data administrators should not make any changes to the Active Directory service itself. Changes to directory service replication. Using access control lists (ACLs), the authorizations should be restricted as far as possible to individual subareas.
Because service administrators need extensive permissions for service management, they should be able to perform administrative data management activities as well. Conversely, the data administrators should not be able to change the configuration of the Active Directory.

To prevent misuse of the administrative accounts, the user accounts of the above roles must be secured accordingly. The necessary configurations in the Active Directory itself are listed in the measure APP.2.2.A7 Implementing Secure Management Methods for Active Directory.

#### APP.2.2.M3 Group Policy Planning on Windows

Since Windows 2000, a powerful mechanism known as Group Policy has been available for configuration. Group Policy is used in Active Directory to apply a set of configuration settings, including security settings, to a group of objects. A so-called Group Policy Object (GPO) summarizes a given set of configuration parameters. For each parameter, a specific value can be given, which may only come from a limited value range. In general, the value can also be set to "not defined" so that the Windows default settings for these parameters automatically apply.

The parameters within a group policy object are summarized thematically in a tree-like manner. This results in a general split at the highest level in settings for computers and for users. From a security perspective, the settings that are found below the following paths are particularly interesting:

* Computer Settings \ Windows Settings \ Security Settings
* Computer Settings \ Administrative Settings \ Windows Components \ Windows Installer
* Computer Settings \ Administrative Templates \ System \ Group Policy
* User Settings \ Administrative Templates \ Windows Components \ Microsoft Management Console
* User Settings \ Administrative Settings \ Windows Components \ Windows Installer
The current Windows server systems generally calculate the valid settings for each group policy parameter for every computer registered to a domain and for each logged-in user. This calculation is necessary because the default settings for the parameter settings can be defined by different GPOs that can overlap each other. The following GPOs can be defined:

* Each computer has a locally defined Group Policy object. This allows the definition of parameter settings locally on the computer, eg. If there is no network connection.
* GPOs can be defined through Windows server sites. This allows settings to be adapted to specific locations.
* Within the Active Directory tree, GPOs can be defined for the domain object, allowing it to control parameter settings for machines and users throughout the domain.
* On each OU object, group policies can be defined whose settings then affect all computers and users below this OU object.
The following calculation or coverage scheme (local <- location <domain <- organizational unit, LSDO) is used to calculate the parameter settings that apply to a particular computer or user: First, the local settings are taken into account (L, local). These settings are then masked by the settings of the GPO defined on the associated site (S, Location). Thereafter, the coverage is performed by the group policy objects defined on the relevant domain object (D, domain). Finally, the Group Policy objects of the OU objects are applied in the order in which they are defined on the way from the domain object to the OU object containing the respective computer or user (O, organizational unit).

The overlap can be influenced by the options block or force. If the settings are blocked and forced to conflict, the enforcement setting is enforced. In addition, at the OU level, it is possible to define multiple GPOs for an OU object. The overlapping takes place according to the order given. It is also possible to enable or disable each individual GPO for an OU object.

Group Policy objects can only be defined in Active Directory on OU objects, but not on individual computers or user objects. The locally defined GPO is not stored in the Active Directory. If you want to prevent a group policy object that is defined on an OU object that summarizes computer objects from acting on all contained computer objects, you can prevent the application from accessing a specific computer object by assigning access rights to the group policy object. For this purpose, this computer object must be deprived of the right to apply to the GPO.

However, the previously used depiction of the definition of GPOs on OU objects was simplified: GPOs are stored separately in Active Directory and form a pool of objects. Each defined GPO can now be associated with one or more OU objects. One speaks then of a link. By marking a link as enabled or disabled, the respective GPO is used in the calculation for the OU object or not (see above). For each GPO, the Properties dialog can be used to determine which OU objects have a link. H. which objects they potentially affect.

From a security perspective, the following aspects should be considered when planning and handling GPOs:

* The group policy concept must be kept as simple as possible. Complex structures of multiple overlaps should be avoided. In particular, the possibility of assigning access rights to GPOs should only be used in exceptional cases. In general, the group policy concept must be documented in such a way that exceptions are easy to recognize.
* The Group Policy concept and the OU object tree have a significant impact on each other because Active Directory group policy objects can only be applied to OU objects, not to machine or user objects. When building up the OU groupings, it must therefore be ensured that only objects that are to be provided with the same GPO settings are combined in an OU object or subordinate OU objects.
* The rights calculation makes it possible to distribute the management of the parameter settings to different "locations" (local, location, domain object, OU objects). It must therefore be decided for each parameter where it is defined. It should be noted that some parameters only become effective if they are defined at certain "places". So z. For example, the password settings are originally defined only on domain objects. Fine-grained password policies have been introduced with Windows Server 2008, allowing different password policy and blocking policies to be defined for different groups of users within a domain
* GPOs must be protected against unauthorized modification. On the one hand, appropriate authorizations must be assigned in the Active Directory (see also Active Directory Administration Planning, Active Directory Administration Training) and, on the other hand, the use of appropriate administration tools, such as: For example, MMC Group Policy snap-in or registry editors.
* In particular for the safety-related parameters within a GPO, the settings must be defined. In addition to the settings specified above, depending on the application scenario, other parameters may also be relevant to safety. These include z. Eg Internet Explorer settings.
The settings of the various GPOs generally have to be based on and implement the security guidelines of the company or the authority.

** Group Policy security settings **

The following are security policy defaults that can be used as the basis for security settings within a group policy. The specified values ​​must in any case be adapted to the local conditions. Within the scope of the Group Policy Concept, the individual values ​​must also be distributed to different Group Policy Objects and adapted to the intended purpose (eg Group Policy Objects for Servers, Group Policy Objects for Workstation Computers). As a result, different values ​​can also be created for individual entries.

password Policy

* Force password history: 6 Saved passwords
* Passwords must meet the complexity requirements: Enabled
* Save passwords for all domain users with reversible encryption: Disabled
* Maximum password age: 90 days
* Minimum password length: 6 characters
* Minimum password age: 1 day
Account Lockout Policy

* Account lockout threshold: 3 Invalid login attempts
* Account Lockout Duration: 0 (Note: Account is locked until administrator cancels lockup)
* Reset account lockout counter after: 30 minutes
Kerberos Policy

* Force user logon restrictions: Enabled
* Maximum validity of the user ticket: 8 hours
* Max. Validity of the service ticket: 60 minutes
* Maximum tolerance for computer clock synchronization: 5 minutes
* Max. Period in which a user ticket can be renewed: 1 day
Audit Policy

* Monitor Active Directory Access: Successful, Failed
* Monitor logon events: Successful, Failed
* Monitor login attempts: Successful, Failed
 Monitor Account Management: Successful, Failed
* Monitor object access attempts: Failed
* Monitor process tracking: No monitoring
* Monitor rights usage: Failed
* Monitor Policy Changes: Successful, Failed
* Monitor system events: Successful, Failed
Assign user rights

* Log in as a service: Defined but empty
* Change the system time: administrators
* Raise Scheduling Priority: Administrators
* Raise odds: administrators
* Log in as a batch job: Defined but empty
* Deny login as batch job: Not defined
* Deny logon as service: Not defined
* Access this computer from the network: Everyone, Administrators, Authenticated Users, Backup Operators
* Omitting the Searching Review: Everyone
* Debugging programs: Undefined
* Insert as part of the operating system: Defined but empty
* Remove the computer from the docking station: Administrators
* Allow computer and user accounts to be trusted for delegation purposes: Administrators
* Replace a process level token: Defined but empty
* Create a paging file: Administrators
* Create a profile of system performance administrators
* Create a profile for a single process: administrators
* Create a token object: Defined but empty
* Create permanently shared objects: Defined but empty
* Force shutdown from a remote system: Administrators
* Generate Security Watches: Defined but empty
* Shut down the system: administrators
* Add workstations to the domain: Defined but empty
* Loading and removing device drivers: administrators
* Log on locally: administrators, backup operators
* Deny local login: Not defined
* Back up files and directories: Backup Operators
* Lock pages in memory: Defines empty
* Synchronize directory service data: Defined but empty
* Take ownership of files and objects: administrators
* Change the firmware environment variables: Administrators
* Manage auditing and security logs: Administrators
* Restore files and directories: administrators
* Deny access from the network to this computer: Undefined
security options

* Rename administrator: Not defined
* Prompt user to change password before password expiration: 7 days
* Do not allow users to install printer drivers: Enabled
* Number of previous logons to cache (in case the domain controller is not available): 0 logins
* Clear paging virtual memory paging file: Enabled
* Allow ejecting of NTFS removable media: Administrators
* Automatically log off users when login time is exceeded (local): Enabled
* Automatically log off users after logon time expires: Enabled
* Digitally sign client communication (always): Disabled
* Digitally sign client communication (if possible): Enabled
* Verify the use of the backup and restore right: Disabled
* Rename guest account: Not defined
* Allow the system to shut down without logging in: Disabled
* LAN Manager authentication level: Send only NTLMv2 responses \ LM deny
* Idle time to disconnect session: 15 minutes
* Do not show last user name in logon dialog: Enabled
* Message for users who want to log in: Not defined
* Message titles for users who want to log in: Not defined
* Digitally sign server communication (always): Disabled
* Digitally sign server communication (if possible): Enabled
* Allow server operators to schedule scheduled tasks (for domain controllers only): Not defined
* Secure Channel: Digitally sign secure channel data (if possible): Enabled
* Secure Channel: Digitally encode secure channel data (if possible): Enabled
* Secure Channel: Digitally Encrypt or Sign Secure Channel Data (Always): Enabled (Note: Unless antiquated systems are incompatible with it.)
* Secure Channel: Strong Session Key Required: Enabled (Note: Unless antiquated systems are incompatible with it.)
* Increase default permissions of global system objects (such as symbolic links): Enabled
* Disable CTRL + ALT + DEL request for login: Disabled
 (Note: ie CTRL + ALT + DEL is required)
* Shut down system immediately if security checks can not be logged: Disabled
* Do not allow system maintenance of computer account password: Disabled
* Send an unencrypted password to connect to third-party SMB servers: Disabled
* Behavior when installing unsigned files (except drivers): Warn, but allow installation
* Behavior when installing unsigned drivers: Warn, but allow installation
* Behavior when removing smart cards: lock computer
* Additional restrictions for anonymous connections: No access without explicit anonymous permission
* Recovery Console: Allow automatic administrative logins: Disabled
* Recovery Console: Allow copying from floppies and access to all drives and all folders: Disabled
* Restrict access to CD-ROM drives to locally logged on users: Enabled
* Restrict access to floppy drives to locally logged on users: Enabled
* Check access to global system objects: Disabled
event log

* Keep application log for: Not defined
* Application log retention method: Overwrite events as needed
* Security protocol preservation method: Overwrite events as needed
 (Note: In the high-security area, the following setting must be selected: Do not overwrite events (clean up log manually).)
* System log retention method: Overwrite events as needed
* Restrict guest account access to application log: Enabled
* Restrict guest account access to security log: Enabled
* Restrict guest account access to system log: Enabled
* Maximum size of application log: 30080 kilobytes
* Maximum size of the security log: 100992 kilobytes
* Maximum size of the system log: 30080 kilobytes
* Keep safety log for: Not defined
* System when reaching the max. Shutdown Security Log Size: Disabled
 (Note: Enable for high security systems)
* Keep system log for: Not defined
** Security Compliance Manager (SCM) **

Group Policy is one of the most important tools in Windows environments to provide adequate system protection. However, manually setting hundreds of settings to safe values ​​that are appropriate for the purpose in the institution can be a great expense.

One tool that makes it easier to manage GPOs on Windows client and server systems is Microsoft's Security Compliance Manager (SCM). This should help to enforce Microsoft and third-party recommended security policies institution-wide. He belongs to the group of "Solution Accelerators", which are freely available for download from Microsoft and support tasks related to the planning and deployment of system environments and applications.

After installation, the SCM provides a variety of current baselines for Windows operating systems and applications that can be customized and extended to meet an organization's security and compliance needs. A baseline is a collection of relevant security and configuration settings that ultimately contribute to the overall security of the system.
The selection of baselines is not limited to individual products and versions, but is also divided into application roles and security requirements. For example, there are separate templates for file and web servers, Hyper-V, domain controllers or Remote Desktop Services, as well as various versions of the Windows client operating system and application software such as Internet Explorer, Microsoft Office, SQL Server or Exchange Server ,

Version 4 of the SCM now also supports Windows 10 and Windows Server 2016 in addition to Windows 8 / 8.1 and Windows Server 2012 (R2).

The most important functions of the Security Compliance Manager are shown below:

* Protection of Microsoft products (Windows Server, Windows Client, Office, Exchange Server, SQL Server, Internet Explorer)
* Central storage and administration of baselines
* Possibility to use baselines on stand-alone and domain systems
* Comparison and Merge of Baselines
* Various import and export options
* Detailed integrated help and description of the individual setting options
For example, Windows Server 2012 R2 ships with the following baselines:

* Domain Controller Security Compliance (Version 1.0: 620 Settings)
* Domain Security Compliance (Version 1.0: 9 Settings)
* Member Server Security Compliance (Version 1.0: 421 Settings)
For Windows Server 2016, this looks like this:

* Domain Controller Security Compliance (Version 1.0: 1013 Settings)
* Domain Security Compliance (Version 1.0: 9 Settings)
* Member Server Security Compliance (Version 1.0: 1011 Settings)
The settings must not simply be adopted, but must be checked for compatibility with the security requirements and specific circumstances of the institution. This also applies to settings that are set to "undefined". Before rolling out to productive system, the settings should be tested.

** Fine Granular Password Policy **

Fine-grained password policies have been introduced with Windows Server 2008, allowing different password policy and blocking policies to be defined for different groups of users within a domain.

In a fine-grained password policy, all password settings including the blocking parameters can be set with the exception of the domain-wide Kerberos settings. All these parameters must be defined when using a fine granular password policy. By default, only members of the Domain Administrators group can set fine-grained password policies. However, this right can also be delegated to other users.

Fine-grained password policies should be used to enforce adequate password strength throughout an institution.

** Shadow Groups **

Fine granular password policies and some other parameters can not be applied directly to OUs. To apply a fine granular password policy to all users of a particular OU, so-called shadow groups can be used. A shadow group is a global security group that is logically assigned to an OU. The users are assigned to the Shadow Group, and the password policy is applied to the Shadow Group. It should be noted that when moving a user to another OU, the membership in the shadow groups must be adjusted.

** No password management via GPO **

Basically, local accounts can be managed via GPO. This applies, for example, to the creation of local (also administrative) accounts, the setting of passwords, the creation of services with service accounts, etc. The problem with this is that the credentials in this case are stored in XML files on the SYSVOL share on all domain controllers Domain are stored and can be relatively easily read or reversed.
GPOs should not be used for setting passwords. If there are already passwords in GPOs, the guidelines should be removed and the corresponding files deleted. The same applies to scripts (eg VBS or PowerShell) that contain passwords. Microsoft offers a PowerShell script that searches SYSVOL for passwords in GPO XML files.

#### APP.2.2.M4 Active Directory Administration training

The Active Directory is the central database of server operating systems as of Windows Server 2000, in which user data, group memberships and other administrative data are stored. Clients can be managed in Active Directory since the Windows 2000 release.

The administration of a Windows network requires detailed knowledge of the Active Directory and its basic concepts. Otherwise it can easily lead to misconfiguration, which can have significant safety implications. Training administrators in this area, and in particular on Active Directory security topics, is therefore essential.

** training content **

Depending on the size and complexity of the network, an Active Directory is not carried out by a single administrator but by a whole range of administrators with special tasks and areas of activity. In that regard, not all administrators of an Active Directory have the same training needs. To ensure safe operation, however, each administrator must have sufficient basic knowledge to be able to classify his own activities in an overall context.

Training content should in any case include and explain the following keywords. How deeply an administrator has to deal with the individual points depends on his later field of activity.

** ** Basics

* Overview of the security mechanisms of Windows Server
* What's new in security mechanisms of current Windows client operating systems (including changes made by new operating system versions or service packs)
* Security Management (MMC, Security Editor, GPMC)
* Active Directory and DNS
* Trust relationships between domains
Necessary physical protection of all domain controllers as carriers of Kerberos data
** Active Directory **

* General: planning, setup, administration
* Scheme management
* Replication
* Backup
* Rights assignment
* Authentication
* Group Policy
** PKI (Public Key Infrastructure) **

* How a PKI works
* Certificates and certificate types
* Planning a PKI
* Setting up a PKI
* Manage a PKI
* User interaction with the PKI
** ** IPsec

* How IPsec works
* Configuration of IPsec
* Checking the successful establishment of secure connections, tools
** DFS (Distributed File Service) **

* How the DFS works
* Administration of DFS
* Planning the DFS structure
* Protection of data accessible via DFS
The individual Active Directory topics should be presented in more detail as follows:

** Schema Management **

Normally, an installation-specific modification of the Active Directory schema by an administrator is not necessary. The training can therefore be limited to the problems and effects of schema changes.

If individual adjustments of the schema are to be made, further training on the internals of the Active Directory is necessary.

** Active Directory replication **

* Mechanisms used to replicate Active Directory (RPC and SMTP)
* Default parameters for replicating Active Directory content
* Problems of decentralized administration of AD in connection with replication conflicts
** Backup **

* Issue of creating a backup of Active Directory
* Restore backups of a domain controller
* Action to take in the event of domain controller failures involving FSMO roles
** Rights assignment in Active Directory **
* Assign access rights to attribute-level AD objects
* Inheritance of access rights and blockage of inheritance
* Possible access rights
* Delegation of administrative tasks at the level of individual OUs
** ** authentication

* Kerberos
* PKI
* Smart cards
** Group Policy **

* Local Group Policy and Group Policy stored in Active Directory
* Configuration options using Group Policy
* When are group policies applied? How can I configure this?
* Group Policy Objects (GPOs) as objects in Active Directory
* GPOs can be bound to sites / domains / OUs
* Order in which group policies are processed
* Ways to control the application of Group Policy

 
+ Assignment of access rights to group policies
+ No Override Property of binding a GPO to an AD object
+ Block Policy Inheritance property of AD objects


 
* Options for selective application of Group Policy:

 
+ Safety filter
+ WMI Filters and their inappropriateness (performance reasons)


 
* Security Compliance Manager (SCM)

 
+ Operation
+ Included baselines
+ Adaptation of Baselines
+ Application locally and via AD / SCCM


 
** Introduction to Active Directory **

The following information is the minimum of what each administrator should be familiar with and familiar with as an introduction to AD and its security. This can not replace either thorough training or the necessary work experience that can be achieved and demonstrated by other means.

In a domain, computers and users are grouped together and can be managed by the domain administrator. A domain boundary basically forms an administrative boundary, although no security limit (see below and measure APP.2.2.A5 hardening of the Active Directory) and also limits the scope of permissions. In addition to this concept, Windows servers offer tree-like inter-domain relationships so parent-child relationships can exist between domains. A child domain is also called a subdomain because the name of the child domain is derived from the name of the parent domain by appending that name to the name of the domain separated by a period.

Example:

Name of the parent domain: unternehmen.de Name of the sub / child domain: verwaltung.unternehmen.de

The namespace spanned in this way is identical to the corresponding DNS namespace and can not be formed differently from it. Domains that share a common name stem form a tree.

Domains that are located in several trees, ie spanning different namespaces, can still be managed together.

Such merged domain trees form a forest (English Forest). In particular, a single stand alone domain also forms a tree and at the same time a forest.

In a forest, there is always an excellent domain, which has a certain special status. It is the first created domain, also known as forest root domain (FRD). The special feature is that forest root domain administrators have extensive permissions throughout the forest. For the members of the Enterprise Admins group, the domain boundaries do not represent administrative boundaries because they have access rights in all domains. When building a Windows domain federation, keep in mind that the first created domain is always the forest root domain. In particular, the "role" of the forest root domain can not be subsequently "transferred" to another domain, so the domain structure must be completely recreated in the desired form.
The Active Directory consists of various objects, the Active Directory Objects (ADOs). Each object has an excellent type, such as B. User object or computer object and is composed of various attributes according to this type. The different object attributes can hold different values, such as: Phone number or IP address. The Active Directory knows different predefined object types:

* Domain Object: This object is the root of all Active Directory objects in a domain and contains information about the domain, such as: For example the name. Below a domain object, other objects may be arranged.
* Grouping objects: These objects are used to group other objects together. By default, the Organizational Unit (OU) object is available. Below an OU object, further OU objects can be contained as well as computer, user and user group objects.
* Calculator object: This object represents Windows client computers. Below a computer object, no further objects can be arranged. The Active Directory is designed only for the administration of Windows machines, so that computer objects can only represent Windows computers that work together with the Active Directory. These are by default computers with the operating systems from Windows NT.
* User object: This object represents domain users. Below a user object, no further objects can be arranged.
* User Group Objects: These so-called security groups represent Windows groups. There are several types of groups that differ in scope (domain, forestwide) and in possible group members (domain, forest). A distinction is made between local, domain local, global and universal groups. Security groups are used to grant permissions. In Windows Server, large institutions with a high number of groups can be expected (several tens of thousands), so u. U. via a tool-based administration must be considered. This can be done via self-written scripts as well as third-party products. Whether and which tools are useful here, however, must be decided on a case-by-case basis.
The general Active Directory structure can be represented as follows:

* The domain object is the root of the Active Directory tree of a domain.
* OU objects are created under the domain object in order to group together computer, user and user group objects. Since OU objects can be nested, this results in an institution-specific tree structure.
After a standard installation, there is a simple and flat Active Directory structure that is created by a Windows server and then has to be modified according to Active Directory planning. Since the Active Directory primarily serves the administration of a Windows system, care should be taken when setting up the Active Directory structure that the structure is primarily attuned to administrative circumstances. If, instead, the organizational structure of an institution is reproduced to the smallest detail, this can lead to problems in the administration, but at least to high administrative costs.
The possible arrangements of Active Directory objects, i. H. The definition of which object may contain which other objects, which attributes exist and on which attributes objects are composed is defined by the so-called Active Directory schema. The Microsoft Active Directory schema can also be changed. However, this represents a serious interference with the Active Directory, which may only be carried out after careful planning. A schema change affects all co-managed domains; H. in the woods, out. Because the schema change is a critical operation, it can only be done on one machine, the so-called schema master, by members of the Schema Admins group. In addition, schema changes may not be reversed. Membership in this group is therefore strictly restrictive and strictly controlled.

The members of the Enterprise Admins group, which by default is the Forest Root domain administrator, have special powers in all domains of the network. You can z. For example, you can add new domains to the forest and have administrative rights to all domain controllers in Active Directory.

Within a single domain, the administration is done by members of the respective domain-specific Domain Admins group. This group has unlimited administrative privileges within a domain. However, it is also possible to enable individual administrative tasks for other user accounts and thus to delegate administrative tasks (see also APP.2.2.A2 Active Directory Administration Planning).

Delegation of administrative tasks within a domain can also be done by delegating only the administration of part of the user accounts and computers of a domain. This is possible within the limits of the OUs that are used to group user or computer accounts within the domain.

A variety of Windows client configuration parameters are grouped in Group Policy. In addition to the local group policies on each Windows client machine, there are also group policies that are stored in the Active Directory. This allows computers or user accounts to be centrally configured. The scope of such a group policy stored in AD can be, among other things, entire domains or OUs. Here, OUs are used to group identically configured computers or user accounts. Because OUs can be nested and multiple group policies can be connected to a single OU, many different group policies may be affected by a single machine (see also APP.2.2.A3 Planning Group Policy on Windows and the corresponding client building blocks).

To store the data, a relational, transactional database is used. This database is distributed on special servers, the "domain controllers". The domain controller uses the Active Directory to provide centralized authentication and authorization of users and computers in a domain. The following protocols are used:

* Lightweight Directory Access Protocol (LDAP) to query Active Directory objects and attributes
* Kerberos for the authentication of users and computers
* CIFS (Common Internet File System) for the transfer of files in the computer network
* DNS (Domain Name System) for name resolution of computer systems in the network
With some exceptions, each domain controller will only contain the data of its own domain. These exceptions are:

* Each domain controller contains the schema and configuration data for the entire forest.
* At least one domain controller of each domain additionally contains the "Global Catalog".
The Active Directory is kept on domain controllers and synchronized within a domain between them through replication. The Active Directory of a domain contains only domain-related information. In order to be able to quickly access information from the entire forest in a forest, the so-called Global Catalog (GC) is set up. It consists of partial information from Active Directory objects and is replicated throughout the forest so that global catalog information in one domain also provides direct access to information from other domains.

In addition to the described tree-like and hierarchical structure, Windows Server automatically builds an additional and orthogonal structure. Spatially close to the computer (this determines Windows server over network runtimes) are summarized to so-called locations (English sites). Sites also control, among other things, the replication structure of domain controllers. Each site must have at least one computer holding a copy of the Global Catalog. The Global Catalog must be requested as part of a user's sign-in process so that a Global Catalog server must always be accessible when logging in. The automatic structure of Windows Server should be adapted to internal institutional conditions such as: B. locations in different cities or countries can be customized. Because this affects the Active Directory replication relationships, there is a concept to create.

Active Directory data is replicated between the domain controllers of an institution using multi-master replication. Each domain controller has a replica of the Active Directory that can be modified and used as a basis for future replication. Using multiple domain controllers in an institution creates redundant copies of Active Directory and minimizes the chance of total failure.

Matching the data between each domain controller can be done through two different replication mechanisms (RPC or asynchronous SMTP). Which mechanism is used can be configured as well as the intervals at which replication occurs.

Through the concept of distributed databases, some resilience of the Active Directory can be achieved by operating a sufficient number of suitably distributed DCs. The problem is, however, the owners of the FSMO roles.

** FSMO or Operations Master **

Operations Master or FSMO (Flexible / Floating Single Master Operations), as it was officially called until 2005 (the name is still in use anyway), is a feature of AD. The FSMO is a set of domain controller tasks that can not be handled like normal DC tasks on multiple DCs that have copies of the AD database and that synchronize through multi-master replication. On the other hand, FSMO tasks can only be performed in a single database called a master database.

There are several FSMO roles, including at the domain level

* PDC (primary domain controller) emulator: responsible among other things for time synchronization
* RID (Relative ID) master: for consistent ID assignment
* Infrastructure master: for the consistency of cross-domain links
and on a forest level

* Schema master: to replicate schema changes (such as when upgrading DCs or deploying Exchange Server or Skype for Business (formerly Lync) servers)
* Domain naming master: to distribute namespace changes
Due to the high importance of DCs, which have FSMO roles, they have to be specially protected.

#### APP.2.2.M5 hardening of Active Directory

Since the protection of infrastructure components that map the functions of the AD are essential to the security of the entire institution, a thorough hardening of all components is necessary.
** Built-in accounts as emergency accounts **

Built-in accounts should be given complex passwords (at least 20 characters) and should serve as emergency accounts only. For this, the passwords are stored in a safe place and a process is defined by whom they should be used in an emergency.

** Protected Users Group **

For privileged accounts, it is recommended to use the Protected Users group (see module APP.2.2 Windows Server 2012). Accounts of this group, authentication is only allowed via Kerberos. Effectively this prevents pass-the-hash attacks. This measure requires a Domain Function Level 2012. All applications must be compatible with Kerberos.

** (Group) Managed Service Accounts **

If possible, (Group) Managed Service Accounts should be used if applications on servers require special corrections (see module APP.2.2 Windows Server 2012).

If this is not possible, to prevent brute force breaking of a service account password, all service accounts should be secured with at least 20 characters of password length. From Domain Functional Level Windows Server 2008 this can and should be enforced by password policy.

** Configuring Windows Server as domain controller **

Domain controllers provide the services needed to manage a Windows Server domain in a network based on the Windows Server operating systems, of which ADS plays the most important role. As a rule, a domain controller also offers the name service DNS (Domain Name Service), without which the Active Directory can not be operated. In Windows, Windows references to important Windows Server resources whose integrity is essential to the proper functioning of a Windows Server domain. Because a domain controller acts as a logon server, it runs the necessary Kerberos service. The Kerberos components on the domain controller also retain the secret keys used in the authentication protocol.

As each domain controller has an important role to play and valuable data is saved by it, the following points should be noted for the configuration. In addition, the aspects described in the corresponding suitable block for the operating system (eg SYS.1.2.2 Windows Server 2012) also apply to a domain controller.

The security of a domain controller derives mainly from two main areas: the security of the operating system configuration and the security of the Active Directory, which uses its own security mechanisms (see also APP.2.2.A4 Active Directory Management Training). The security settings of the operating system are essentially based on group policies. The security settings of the Active Directory require appropriate planning and implementation (see APP.2.2.A1 Planning the Active Directory, APP.2.2.A3 Planning Group Policy under Windows).
* Only authorized administrators may log on to a domain controller locally. User operation on a domain controller must not be allowed. Therefore, after a default installation, normal users are not allowed to log in locally to a domain controller.
* A domain controller should, in addition to the mandatory standard domain controller services such. For example, Active Directory, Kerberos, and DNS do not provide any additional infrastructure services (such as DFS, DHCP). In particular, the operation of a DHCP server on a domain controller must be discouraged for security reasons. Both services run under the same permissions. As a result, simplified access rights to DNS data can no longer be enforced if the DHCP service makes changes to DNS data.
* A domain controller should not offer any (application) server services, as faults in the server programs can compromise the domain controller and thus the entire Windows Server domain.
* The configuration of the channel used to communicate administrative data between computers in a Windows server domain should be as secure as possible (see APP.2.2.A8 Configuring the secure channel under Windows).
* If a domain controller can be booted in the so-called Active Directory Restore mode, it is possible to make changes to the AD by For example, old states (partial or full) can be loaded from backup media. These changes can be imported in such a way that they are propagated to all other domain controllers in a domain after regular booting through Active Directory replication. It is therefore important to ensure that the Active Directory Restore mode is protected by a suitable password and working in this mode is only in compliance with the four-eye principle. The Active Directory restore mode is command line based, and typing errors can have serious consequences, such as: For example, delete or overwrite the wrong Active Directory topic. Therefore, the four-eyes-principle offers here beside the activity control also a security by the control of all entries by two persons.
* The domain controllers of the Forest Root Domain (FRD) are particularly vulnerable due to the special nature of the FRD.
** Secure operation of domain controllers **

To avoid configuration errors and maintain a consistent level of security, an image-based setup of the domain controllers should be performed from a reference installation. Furthermore, the security settings in the base device of the domain controller should be made uniform. This should be achieved by implementing a predictable and easy-to-repeat deployment process. This includes:

* Regular import of current hotfixes and service packs
 At regular intervals current hotfixes and service packs should be recorded. However, the effects should be thoroughly tested in advance on an image of the reference domain controller.
* Assign strong enough passwords
 For the user accounts in the Active Directory sufficiently strong passwords are to be assigned. Indications of sufficiently strong passwords can be found in the institution-wide regulation of password usage. In addition to the creation of complex passwords, it must be ensured that the passwords are passed on to the persons concerned through trusting channels. Also, the user accounts should be equipped with individual passwords, especially during the initial setup.
* Ensure the integrity of the installation
 If the domain controllers are deployed to a different destination location, signatures should be used to transport them to ensure the integrity of the installations
** Authorization of executable files **

To protect the root folders of the volumes from disk space attacks after the domain controllers have been promoted, the permissions on the Everyone group should be limited to read and execute. The "full access" is only for the administrators to grant.

** Prevent system startup from other operating systems **

Booting from other operating systems on the domain controllers can leverage NTFS access restrictions and allow access to critical data. In addition to the already mentioned spatial security of the server therefore also organizational arrangements have to be made.
The remote network start and thus the possibility for remote network installation z. Remote Installation Services (RIS) or Bootstrap Protocol (BOOTP) should be disabled and the use of a BIOS password at system startup should be disabled.

** Restart protection with hard disk encryption (BitLocker) **

Even safer is a hard drive encryption, which requires the entry of a password or use of a disk at system startup of the DC. The measure is described in the corresponding Windows Server block (eg SYS.1.2.2 Windows Server 2012).

** Secure domain and domain controller policy settings **

A Windows Server with Active Directory includes default security policy settings for the domain and for the domain controllers. However, we recommend that you change the default policy settings to increase domain and domain controller security by:

* Secure password policy settings
 Access to domain controllers must be secured with strong mechanisms. For more information about the necessary password policy settings, refer to the Microsoft server-specific blocks.
* Account Blocking Policies
 The logging of the logon attempts (see also APP.2.2.M11 Monitoring the Active Directory Infrastructure) should be set up so that attacks can be detected. For example, a large number of unsuccessful password entries during a login attempt could indicate a brute force attack. The actual account lockout is defined by the options Account Lockout Duration, Account Lockout Threshold, and Resetting the Account Lockout Counter as described in Action APP.2.2.M3 Planning Group Policy on Windows.
* Kerberos policy settings
 The authentication service provided by Kerberos will provide the appropriate client with the required resource access authorization information. This grants access to network resources based on session tickets. For this purpose, the domain controller issues a so-called Ticket Granting Ticket (TGT) to the client in advance. If the client attempts to access a resource, the client sends the TGT to the domain controller for review. The domain controller, in turn, generates the client a session ticket after successful verification, which allows temporary access to the resource.
 By customizing the Kerberos policy setting, Kerberos ticket aspects such as validity period can be customized for domain user accounts (see action APP.2.2.A3, Group Policy Planning on Windows).
For secure domain controller policy settings, the following are also recommended:

* User rights should be restrictive so that users in the domain or on the domain controller can only perform the operational or administrative tasks they are responsible for. The access possibilities of users should be restricted in such a way that they do not endanger the security of the domain controllers (see also measure APP.2.2.A1 Planning of the Active Directory).
* Setting up Domain Controller Monitoring policy settings will provide proof of responsibility for sensitive directory operations, such as: Management or configuration changes. You should set up logon attempts, account management, Active Directory access, object access attempts, policy changes, rights usage, process tracking, and system events (see action APP.2.2.A11 Active Directory Infrastructure Monitoring).
* Important Active Directory objects such as: For example, the directory partitions should be monitored with appropriate policy settings. This requires the monitoring of directory partitions (logical sections of the Active Directory database) to be enabled. The directory partitions affected by this are "Schema", "Configuration" and "Domain" (ditto).
The above recommendations for setting policy settings cause the default maximum size of the security log to be increased to accommodate a larger number of monitored events. The logs must be evaluated promptly. In addition, there must be a clearly defined procedure for regular and timely archiving, as well as backup of security and system event logs so that no events are lost or overwritten.

In addition, to support collaboration between domains in different forests, e.g. For example, for application sharing or limited collaboration between different forests in an institution, external trusts should be established. External trusts, however, create a potential security risk as security limits are exceeded. Therefore, the domain controllers in the relying domain should filter user authorization data and remove security identifiers (SIDs) that are not related to the domain of the user account. A detailed description of how to recover comprehensive privileges by spoofing SIDs and the countermeasures of SID filtering is given in Microsoft Knowledge Base articles 289243 and 289246.

The domain controller security policy settings affect the security-related configuration settings of the Windows Server operating systems and should therefore be carefully set. This applies not only to the Active Directory-related configuration, but also to other components of the Windows Server operating systems (for example, network security configuration, file system, and user logon settings).

** Virus protection for domain controllers **

For a sufficient protection against computer viruses and other malicious programs an extensive virus protection concept must be implemented in an institution. The corresponding procedure is described in the module OPS.1.1.5 Protection against malicious programs. In principle, the domain controllers of an institution should also be considered in the virus protection concept.

However, in order for the use of a virus protection program on a domain controller to have no negative effects on the ongoing operation, there are some special considerations for domain controllers.

The notes in this measure are to be understood as general instructions. Under certain circumstances, the special instructions of the manufacturer of the virus protection program used in each case must also be taken into account.

When selecting anti-virus software, care must be taken to explicitly support deployment on a domain controller. The decisive factor here is that the virus protection software uses the programming interfaces provided by the operating system manufacturer (Application Programming Interface, API).

When using incorrect programming interfaces, the metadata of the examined files may be changed by the access of the virus protection software. In this case, it is possible that the File Replication Service (FRS) of the operating system causes a replication of the supposedly changed file within the institution. Such unnecessary replications can lead to reduced system performance and should therefore be avoided. Further details regarding compatible virus protection programs can be found in the Microsoft Knowledge Base article with article ID 815263.
The proper functioning of the virus protection software should be extensively tested for correct functionality prior to final deployment in a production environment in a test environment. The test environment should be modeled as much as possible on the circumstances of the production environment in order to determine the overall performance of the domain controller.

In order to avoid the introduction of malware, domain controllers should only use the Active Directory functionality of the operating system and, if possible, offer no other services. In particular, a domain controller may not be used as a traditional workstation. For example, users logged in locally to a domain controller should not be able to surf the Internet, receive e-mail, or access external media, such as a computer. B. USB memory or optical media.

Similarly, the domain controller should not be used as a file sharing server. If files are made available on the domain controller via file sharing on the network, these files are examined by the virus protection program every time they access malicious software, which can lead to performance problems on the domain controller. File shares on the domain controller should therefore be disabled.

Basically, the virus protection program should monitor all file accesses transparently in the background. However, there are some files in Windows Server operating systems, such as: Directory service database, log files, file replication service database, which may interfere with the functions of the domain controller when accessed by a virus protection program. Therefore, to avoid unnecessary file locking by the virus protection program and to ensure the correct operation of the domain controller, the following points should be noted.

** Access to the Active Directory database and log files through the Extensible Storage Engine (ESE) **

The directory service database and log files are opened by Active Directory using ESE for exclusive file access. Therefore, the ESE can only access the files that are not blocked by the virus protection software. At the same time, the virus protection software can only access the files that are not blocked by the ESE.

Both the database files and the log files use Active Directory-internal checksums, which can be invalidated by the file access of a virus protection program and can lead to inconsistent databases. An inconsistent database can lead to a failure of Active Directory.

Therefore, exclude the following files from the regular virus scan:

* Active Directory main database
* Active Directory transaction log files
* Active Directory working folder
** Access to the File Replication Service (FRS) database and log files through ESE **

As already described, the improper use of virus protection programs in the case of database or log file access can lead to concurrent accesses by the replication service. Likewise, changing the internal checksums of these files may cause the Active Directory to fail. Therefore, the following files should be excluded from the regular virus scan:

* Files in the working folder of the file replication service
* File Replication Service database log files
* Staging folders (cache for new and changed files to be replicated) and root replica (copy of the distributed file system root and its child links) of the file replication service
* File Replication service preinstallation folder
If the File Replication service is used to replicate Windows shares whose shortcut destination is on Windows Server operating systems, these files must also be excluded from the SYSVOL folders.
** File Replication by the File Replication Service (FRS) **

The File Replication service is used by the Windows Server operating systems to replicate logon scripts and SYSVOL folder system policies between domain controllers. If the metadata (security information or timestamp) of a file is changed by a virus protection program, FRS replicates the file between the domain controllers. This behavior results in increased replication of the SYSVOL files and thus

* increased network bandwidth consumption,
* increased resource consumption on the domain controllers and
* a high number of files in the staging folder.
To prevent excessive replication, the following points should be noted:

* Select a virus protection program that does not change the metadata of SYSVOL files.
* If a corresponding selection is not possible, the SYSVOL directory including all subdirectories must be removed from the automatic check by the virus protection program. However, this increases the risk of virus attack, because unlike the above files in this case executable files, such. For example, login scripts that are no longer captured by the virus protection software. Therefore, if the SYSVOL directories can not be secured by the virus protection program, only signed-in scripts should be used on the domain controllers and workstations of the administrators.
** Update function of the Microsoft operating system **

As part of the update feature of the Windows Server operating system ("Microsoft Update", "Windows Update" or "Automatic Update"), the exclusive right to access files of a virus protection program can cause problems.

To avoid these issues, exclude the following files from the periodic virus scan:

* Database files related to the update functionality, such as: For example, in the% windir% \ SoftwareDistribution \ Datastore folder, the file "Datastore.edb"
* the transaction log files stored in the% windir% \ SoftwareDistribution \ Datastore \ Logs folder
More details on the files to exclude can be found online in the "Virus scanning recommendations on enterprise computers running supported versions of Windows" document.

** ** RDP

When closing an RDP session, the user should be automatically logged out. This can be realized by GPO.

The use of Restricted Admin Mode has to be checked individually. When activated, access data can not be transferred when logging in via RDP. As a result, there are no hashes on the host system. However, this setting allows you to perform pass-the-hash attacks on the RDP service.

#### APP.2.2.M6 Maintaining the operational security of Active Directory

The domain controllers used in the production environment must be maintained by the administrators at the previous level of security and adjusted accordingly if the requirements are higher. For changes to the systems resulting, among other things, from the regular maintenance work, written guidelines must be developed in advance.

** Limitation of trust relationships **

The relationships of trust between domains and especially from and to other forests or between different forests (eg tiers) of the institution should be evaluated on a regular basis to see if they are still needed and justified, if they are of the correct type (ie before) whether a two-way trust relationship is really necessary) and whether the security controls are sufficient to ensure that they are guaranteed.
The question "What happens if this trust relationship is deleted?" should be asked for any relationship of trust. If the answer is unknown or not clear, this is an indication that the trust relationship should be disabled, taking into account standard test procedures and fallback planning, and should be cleared if problems do not occur.

** Security of Services Administrator Accounts **

The responsibility for controlling the configuration and operation of the directory service is to be delegated only to reliable, trusted persons. This group of persons must be familiar with the current security guidelines of the institution and demonstrate readiness to enforce them consistently.

The access rights of the service administrators should be reduced to the minimum necessary for their work and be used exclusively for tasks that require increased rights. To ensure the legitimate need for persons with administrative privileges, they should be periodically reviewed and adjusted as necessary. Also, the number of members of the administrator accounts is kept to a necessary minimum. The use of sufficiently strong passwords for the accounts of the administrators groups is mandatory. It should be considered to use strong authentication methods such as: B. the additional use of smart cards for logging on the operating system.

** Limitation of Domain Administrators (DA) **

Ideally, the group DA (domain administrators) should even be empty to ensure that each group receives only the exact rights it needs for its work.

The administrators of the AD itself, for example, only require membership in the group of administrators of the corresponding domain in order to obtain full administrative rights on the AD as well as on the DC. Only who is actually charged with the administration of the ADS, should be DA.

In addition, a domain administrator account (eg the default DA with a strong password) should be set up in case of emergency and stored securely and at the same time easily accessible in case none of the DAs are available.

** Removal of Inactive Accounts from AD **

Unused accounts should be disabled or deleted in AD so they can not be misused by attackers. If the account is deactivated, then an attempted use is noticed and should be logged and evaluated, because a legitimate use should not occur now.

The safest way to do this is when accounts are automatically removed from the AD at the end of their use in a process. This can be ensured technically or organizationally.

** Ensuring the timeliness of basic information **

The term "basic information" summarizes the most important configuration parameters of Active Directory. The basic information should at least include the following points:

* Audit policies
* GPOs and their assignment
* existing trusts
* Organizational unit of domain controllers and service admins
* Owner of the operations master roles
* Replication topology
* Database properties
* used service packs and hotfixes for domain controllers and administrative workstations and their current system state
* currently available backup media
* Checking the backup media
* Check the currently required service administrator permissions
Documented basic information allows for tracking and reviewing changes made to the Active Directory. The basic information should be summarized for all domain controllers in a base database. This basic database additionally provides an overview of the currently used components. The responsibilities for maintaining the basic information must be clarified.
#### APP.2.2.M7 Implementing Secure Management Methods for Active Directory [Specialists]

** separation of standard and privileged identities **

Administrator accounts should not be used for ordinary daily work. The same should apply to administration systems, if there is the possibility for dedicated systems. In particular, administrator accounts and administration systems should not access the Internet.

Each user should therefore have a standard user account for general use. Administrative activities should be done with a separate account. The administration account may not be used for general activities.

** named accounts **

Every account that is used should be clearly assigned to an employee. This not only increases employee responsibility, but also facilitates traceability in the event of an attack.

** Restrictions on the registration of administrators **

The number of systems that ADS administrators log on to should be limited as much as possible. If AD administrators only log on to the systems they actually manage, and indirectly to select few administration workstations, the places where valuable credentials are tapped can be severely curtailed. Therefore, server administrator accounts should not be used on workstations, domain administrator accounts should not be used on workstations or servers. It should be excluded as technically possible that a privileged account is used to log in to a system of another layer.

Starting at a Domain Functional Level 2012, GPOs can be used to ensure that interactive logon from one layer to another is not possible. Thus, a domain administrator may not log on to a production IT or office IT system. A server administrator must not log on to a domain controller or office IT device.

** Service and Data Administration **

To administer a domain, responsibilities and task fields are divided into additional subgroups. Because the user accounts are located in the Service Administrators management groups (responsible for performing the tasks required to deploy the directory service) and Data Administrators (responsible for managing content stored in Active Directory or protected by Active Directory) ) have particularly far-reaching access rights, appropriate precautions must be taken to protect them:

** services administrator accounts **

In each domain of the forest, the default administrator account is created during the installation. As a standard account, this user account is particularly vulnerable to attacks. Since the administrator account can not be disabled or deleted, it should be renamed as a safeguard. When renaming, make sure that the description of the administrator account is also changed. After the account has been renamed, you should then set up an unprivileged account named "Administrator" that must not be used in daily operations. In the evaluation of the log files, it can be recognized whether there were successful or unsuccessful logins to this unprivileged user account. This would indicate an attack attempt.

The number of service and data administrators should be kept to a minimum. Routine administration and administration tasks, such as B. Management of domain users that do not affect the configuration of the Active Directory itself should not be performed by service administrators, but delegated to data administrators.
The administrator accounts should be used as sparingly as possible. Unnecessary login to the domain with administrative rights should be avoided. Therefore, the administrators of an institution should be responsible for everyday, non-administrative tasks, such as For example, obtaining information on the Internet using unprivileged user accounts.

The administration of service administrator accounts may only be performed by members of the service administrator group. In particular, users with fewer privileges, eg. For example, data administrators may not make changes to service administrator accounts because less-privileged users might otherwise be granted extended privileges.

Therefore, to manage the service administrator accounts, you should have your own organizational unit, for example: As service admins, are created in the user management of the Active Directory. The authorizations for this substructure must be selected as follows:

* Disable Inheritance of permissions of parent objects
* Access permissions to the organizational unit to be created (including subordinate objects)

 
+ Administrators: full access
+ Organization Admins: Full Control
+ Domain Admins: Full Control


 
The service administrator groups (Domain Admins, Enterprise Admins, and Schema Admins) are then moved to the new subtree. In addition, the administrative user accounts of the domain admins in the Users and Groups organizational unit and the workstation accounts must be moved to the administrative workgroup organization tree of the new subtree. It should be noted that domain controller accounts must not be moved.

In addition, you should monitor the logging of changes, deletions and setup of service administrator accounts and workstations, as well as policy changes.

Because some of the predefined service administrator accounts can not be moved to the newly created subtree, these accounts must be separately protected.

** Local Administration Accounts **

Local administration accounts should have secure, unique passwords. With Local Administrator Password Solution (LAPS), Microsoft provides a free tool to automatically generate and manage them automatically via AD, see SYS.1.2.2 Windows Server 2012.

** ** adminSDHolder

Active Directory regularly checks the protected service administrator accounts. The security settings of the protected accounts are overwritten with the security descriptions of the AdminSDHolder object (freely translated "Security Account Security Keeper Admin", in the system container "CN = AdminSDHolder, CN = System, DC = domain-name"). The corresponding process that triggers overwrite starts at fixed intervals (every hour by default).

This mechanism applied to Windows Server 2000 systems for the Administrators, Domain Admins, Enterprise Admins, and Schema Admins user groups. In the Windows Server 2003 operating system release, the mechanism has been extended to include the Server Operators, Account Operators, Backup Operators, Print Operators, and Certificate Publishers groups.

The following permissions should be allowed for the AdminSDHolder object:

* Everyone

 
+ Change password


 
* Administrators

 
+ List content
+ Read all features
+ Write all properties
+ Delete
+ Read permissions
+ Change permissions
+ Change owner
+ All confirmed writes
+ All extended rights
+ Create all child objects
+ Delete all subordinate objects


 
* Authenticated users

 
+ List content
+ Read all features
+ Read permissions


 
* Domain Admins

 
+ List content
+ Read all features
+ Write all properties
+ Read permissions
+ Change permissions
+ Change owner
+ All confirmed writes
+ All extended rights
+ Create all child objects
+ Delete all subordinate objects


 
* Organization Admins

 
+ List content
+ Read all features
+ Write all properties
+ Read permissions
+ Change permissions
+ Change owner
+ All confirmed writes
+ All extended rights
+ Create all child objects
+ Delete all subordinate objects


 
* SYSTEM

 
+ Full access


 
**People**

The people in the service administrator groups must be both trusted and have sufficient knowledge of Active Directory administration. To ensure a straight-forward implementation of the institution's security policies, the service administrators must be familiar with the appropriate policies.

The membership list of the service administrator groups can only consist of users of their own Active Directory forest. If service administrators from remote domains become familiar, the institution automatically trusts the security measures of the remote institution. Since these security measures can not usually be influenced, a user account must be set up in the own forest for non-institution users. In this way, the access to the own domain can be better regulated and it is prevented that users access the domain whose rights are not known due to the automatic trust control.

Because of their far-reaching permissions, service administrator accounts are the preferred targets for attacking. Therefore, with increased security requirements, it is recommended that the membership information of all service administrator groups be disabled for non-privileged users.

It should be noted, however, that some server applications require read access to the list of members of the service administrators for trouble-free operation. Therefore, the first step is to determine if such server applications are being used in the institution.

The user accounts under which the identified server processes are started are in their own group, e.g. For example, server applications. Then the following permissions are granted in the ACL of the AdminSDHolder object for this group:

* List content
* Read all features
* Read permissions
Access can thus be limited to the authenticated users who must have read access to the member list.

Because hiding the group membership for service administrator groups can affect operations, it is highly recommended that you review the above changes to the AdminSDHolder object in advance for possible effects.

The members of the Active Directory Backup Operators group are considered service administrators because they can restore domain controller system files. The number of members of these user groups should be kept as small as possible. Therefore, administrators responsible for backing up and restoring application servers within the Active Directory should not be enlisted in the Backup Operators Active Directory group. Rather, the corresponding user accounts are to be entered in the local groups "Backup Operators" of the application server.

The Active Directory Account Operators group should not be used for data management (such as account management) because members have the ability to extend their own rights. For security reasons, there should be no members in the Account Operators group.
The same applies to the Active Directory group "Schema Admins". Because changes to the Active Directory schema are usually very rare, trusted administrators should be added to the Schema Admins group only as long as the permissions are actually needed. Once the changes have been made to the schema, the members should be removed from the group again.

The user accounts of the Enterprise Admins and the Domain Admins groups in the root domain of the Active Directory forest of an institution should be specially protected because of its extensive privileges. Therefore, each of these accounts should be assigned two administrators and the password split in half. Each of the two administrators may be known only one half of the password, so that within the user account can only be worked in accordance with the four-eyes principle. This will help prevent the unrecognized use of root domain service administrator accounts in the Active Directory forest.

Alternative methods of enforcing the four-eye principle, such as As the use of smart cards, PIN and smart card are separated from each other, are also conceivable.

In addition to securing the service and data administrator accounts, the workstations of the administrators must also be secured as follows:

* The user accounts of the administrators should be set up so that the accounts can only be used from certain workstations. Thus, compromised administrator accounts can only be used by certain workstations.
* After 5 minutes of inactivity by the user, the automatic blocking is to be activated. It is important to ensure that no cached data may be used to remove the console lock, but a re-authentication on the domain controller must be made mandatory. To do this, the value of the ForceUnlockLogon registry key in the HKLM \ Software \ Microsoft \ Windows NT \ CurrentVersion \ Winlogon \ directory must be set to "1".
* Virus protection programs should be used on the workstations of the administrators.
* Applications should not be run in the context of the administrators. When adding a new workstation to the domain, care should be taken to ensure that the domain admins are not automatically added to the local workstation administrators group.
* Processes should not be run with the permissions of domain admins. Instead, the security context of the local administrator group of the workstation should be used.
* The data traffic between the workstations of the administrators and the domain controllers must be safeguarded accordingly. To do this, the LDAP packet signatures should be enabled. To do this, set the LDAPClientIntegrity registry key to "2" in the Windows registry path HKLM \ System \ CurrentControlSet \ Services \ LDAP \.
For remote administration of domain controllers, only protocols that enable encryption of traffic should be used.

** Data administrator accounts **

In principle, the structures and authorizations of the data administrator accounts depend strongly on the structure of the respective institution. For the following aspects, therefore, it must be verified whether they can be combined with the requirements of the institution.

Data management is delegated via groups to which the appropriate user rights are assigned. The members of these groups apply the Group Policy settings. After these steps, it is sufficient to add user accounts to the created groups for delegation. This ensures maximum security and allows administrators to continue performing their assigned tasks.
Access to Group Policy should be restricted to trusted individuals. Users whose accounts allow the creation and modification of Group Policy settings can grant higher privileges to other user accounts through these policies and must therefore be trusted.

Data administrators also become the creator of an object. In the Windows Server access control model, the owner of an object has full control over this object. This includes the ability to change the ACL of the object. The owner of an object also has full access to all child objects. It also has the ability to block ACL inheritance from parent objects and block access by service administrators to that object.

Make sure that the Administrators or Domain Administrators groups in each domain own the domain root object for each domain partition. Owners of these partition root objects can use inheritable access control entries (ACEs) to change the security settings of all other objects in that partition.

It is important to ensure that when planning for account management tasks, group membership in a delegated scope is changed by a single data administrator, or the task is performed by a few data administrators. If a conflict arises between two concurrent changes in group membership by different domain controllers during replication, the most recent change to an account has priority. Until the server replication, the change made to the respective server is valid.

The use of domain-local groups to control read permission on object attributes that are replicated to the global catalog should be avoided, as it could incorrectly deny or grant object access. To control access to the global catalog data, global or universal groups should be used instead.

**Waste paper bin**

Until Windows Server 2008 had accidentally deleted AD objects or those that were intentionally deleted, but still needed later, consuming and error-prone restore from backups. In Windows Server 2008 R2, a Trash Bin was introduced, but it could only be operated from the command line. Only since Windows Server 2012 does an easy-to-use recycle bin exist, which can be operated both from the command line via PowerShell and via GUI.

The Recycle Bin is disabled by default. It should be activated to prevent the loss of AD objects. Once activated, the trash can not be turned off. Because it requires Windows Server 2008 R2 Domain Functional Level, all forest domain controllers must be at least that level. Once the recycle bin is activated, the functional level can not be rolled back to an older one, so thorough initial planning is necessary on initial activation. Like all changes to the AD, it should first be tested in a test environment.

Activation is performed as an organization admin or schema admin in the ADAC (AD Administration Center) in the Forest Root Domain (FRD). Thereafter, the display of the ADAC should be reloaded to check the activation. This must now replicate through the forest until deleted objects can be restored.

** Enterprise Identity Management **

A separate Enterprise Identity Management solution can be used to ensure, especially in large institutions, that the rights of all users correspond to defined specifications.

### 2.2 Standard measures
Together with the basic measures, the following measures correspond to the state of the art in the field of Active Directory.

#### APP.2.2.M8 Configuring the secure channel under Windows

Between computers of a Windows domain administrative data must be exchanged. For example, domain controllers in a domain exchange administrative data. In general, sensitive data is transported, which must be transmitted securely. Even under Windows NT, the so-called Secure Channel was available for this purpose. Even on Windows 2000 or later, this mechanism is used and must be configured according to security requirements and local conditions. In this case, the authentication of the two communication partners, encryption to maintain confidentiality and signatures to ensure integrity are used as security mechanisms.

The secure channel configuration is done through Group Policy. When configuring them, consider the following:

* Mutual authentication is always guaranteed, but encryption and signature can be required independently. If the communication partner does not support the required protection, this is not used. The communication is then unsecured.
* Encryption or signature can be specified as a necessary condition for communication recording. If the communication partner does not support the backup, no communication is established. For example, this may result in clients being unable to log in to a domain. This option should only be enabled if all the IT systems in a domain and all IT systems of all known domains support encryption and signing. This is the case from Windows Server 2000 and should therefore be taken for granted today.
For Windows Server (as well as clients since Windows XP) the settings are:

* Domain member: Digitally sign secure channel data (if possible)
* Domain member: digitally encode secure channel data (if possible)
* Domain member: Digitally encrypt or sign secure channel data (always)
* Domain member: Strong session key required (128-bit encryption whenever Windows 2000 or later)
* Domain Member: Disable computer password changes
* Domain member: maximum age of computer passwords (default: 30 days, should not normally be changed to larger values)
These parameters can be found under Computer Configuration | Windows Settings | Security Settings | Local Policies | Security Options. All options should be activated accordingly.

#### APP.2.2.M9 Protection of authentication when using Active Directory

The Active Directory acts as a central component within the network. To ensure trustworthy communication between the affected subscribers within the network, security and reliability in terms of authentication and authorization when accessing network resources is required. To maximize the protection of Active Directory authentication, disable LAN Manager authentication and sign server message block (SMB) traffic between domain controllers and between domain controllers and domain computers. In addition, pre-Windows 2000-compatible access should be disabled, as well as restricting anonymous access to domain controllers.

** ** authentication
A high level of security can only be achieved if all domain controllers, member servers, and workstations support at least the NTLMv2 (NT LAN Manager Version 2) authentication protocol. NTLMv2 is available by default as of Windows NT 4.0 SP4. Older authentication protocols from earlier versions of Windows provide less security. For example, in the LAN Manager Authentication Protocol (LM), the account passwords are stored in an insecure LM hash format. The passwords for the Windows NT authentication protocol NT LAN Manager (NTLM) and NT LAN Manager Version 2 (NTLMv2) are stored in NTLM hash format. The NTLM hash is cryptographically stronger than the LM hash format.

Uncertain legacy authentication via LM and NTLMv1 should urgently be prohibited by GPO. If not possible because of the use of legacy systems, then the conversion to NTLMv2 or (since NTLMv2 also has replay attack vulnerabilities) must be at least planned, and an appointment must be made for pure Kerberos.

Windows Server 2008 R2 or later can identify and report insecure network authentication via NTLM or worse, thus helping to plan the transition.

** SMB signing **

The SMB protocol forms the basis for Microsoft file and print sharing and for many other network operations such. For example, remote administration of Windows. For example, to prevent man-in-the-middle attacks that change SMB packets during transmission, the SMB protocol supports the digital signature of SMB packets.

The following four settings should be enabled under Computer Configuration \ Windows Settings \ Security Settings \ Local Policies \ Security Options:

* Microsoft Network Client: Digitally Sign Communications (Always)
* Microsoft Network Server: Digitally Sign Communications (Always)
* Microsoft Network Client: Digitally Sign Communications (If Server Agrees)
* Microsoft Network Server: Digitally Sign Communications (If Client Agrees)
#### APP.2.2.M10 Secure use of DNS for Active Directory

An Active Directory installation typically consists of multiple servers with different directory partitions. So that the access for both the clients and the access between the servers z. For example, when facilitating replication, Active Directory uses Domain Name System (DNS) to find Active Directory servers. Thus, the DNS service must be considered as a foundation of Active Directory.

To ensure the integrity and availability of Active Directory, care must be taken to ensure that DNS client queries can not be misled by unauthorized systems on the network. In Windows environments, the protection of DNS data should be increased by Active Directory-integrated DNS zones on the domain controllers. The zone-specific DNS data is stored in the "MicrosoftDNS" container of the Active Directory.

The configuration data for Active Directory-integrated DNS zones are stored in the Windows Registry. Access to the configuration data should be restricted to administrative accounts.

In the following, we will focus solely on Active Directory-integrated DNS zones and Windows Server-specific properties that support the secure operation of Active Directory. Further general measures to protect DNA are not described here.

To protect the DNS infrastructure, it was important to protect the DNS servers, as well as to adequately secure DNS data stored on the DNS servers, and to ensure the integrity of the DNS responses to the client requests during transmission. How this can be done is explained below.
To ensure the integrity of the DNS data cached on the domain controller, the Back Up Caching option must be enabled for the DNS server process. This is to ensure that only authorized DNS records can be inserted in the clipboard.

Access to the DNS service of the domain controllers should be restricted as much as possible. This can be z. This can be achieved, for example, by restricting the DNS service (UDP port 53) at the security gateways between two network segments. The DNS service must be available for the following components:

* between the DNS clients and the corresponding DNS server,
between DNS servers that perform zone transfers
* between DNS servers that delegate client requests to the appropriate zones and the DNS servers responsible for that zone,
* between DNS servers that forward client requests and DNS servers at the higher-level hierarchy.
Furthermore, the DNS activity network activity should be monitored as there is an unusually high volume of DNS requests for a denial-of-service (DoS) attack against a DNS server, and possibly against a domain controller can indicate. In this case, the attacker should be identified as quickly as possible and appropriate countermeasures should be initiated (see also the action Creating an emergency plan in the module APP.2.1 General directory service).

IPsec (Internet Protocol Security) can be used to ensure the confidentiality, authenticity and integrity of IP traffic in the network. When an IPsec connection is established, the client and the server authenticate each other so that the authenticity of the data can be checked by the DNS client.

The integrity of the DNS data during transmission can be ensured by IPsec using Authentication Header (AH) or Encapsulating Security Payload (ESP).

In contrast to the authentication header of IPsec, the data traffic is additionally encrypted when using ESP. ESP also ensures the confidentiality of DNS data. ESP should therefore be preferred.

Using IPsec increases the amount of traffic. Therefore, before using IPsec, it should be ensured that sufficient resources are available so that sufficient data throughput in the network is possible when encryption or signing is enabled.

** Sufficient protection of the stored DNS data **

To protect the DNS data on the server, the following points should be considered:

* For Windows Server operating systems, a DNS server is included. When used, it must be configured to process only registration requests from authorized Active Directory forest clients. If it is not used, disable it.
* If a third-party DNS server is used, make sure that it supports and has been configured to securely update DNS data dynamically.
* Users' access to the DNS data in the corresponding Active Directory container "MicrosoftDNS" should be set up via ACLs so that only administrators, domain administrators, organization administrators, and DNS administrators have full access to the domain data.
* The administration of the DNS servers and thus of the DNS data is just as critical as the configuration of the Active Directory. For this reason, the assignment of administrator authorizations must be carried out in the same way as for the assignment of the authorizations for the service administrator accounts (see APP.2.2.M2 Planning Active Directory Administration).
* Secondary DNS zone information is stored on a domain controller, not in Active Directory, but in a text-based zone file. If possible, a distributed DNS structure should be used in which each DNS server manages only one zone and corresponding client requests are forwarded from the other servers to the responsible DNS server. Can not avoid secondary DNS zones in this way, eg. B. due to the increased data volume, the zone file must be protected by NTFS permissions against unauthorized access. Only general administrators, domain administrators, organization administrators, and DNS administrators should have full access to the secondary domain data.
Additional information about configuring DNS servers can be found online in the Securing the DNS Server Service document on Microsoft TechNet.

#### APP.2.2.M11 Active Directory Infrastructure Monitoring

The security status of the Active Directory infrastructure is monitored and evaluated by logging the native events. The log depth is to be adapted to the respective requirements and should be reassessed regularly.

The log data should be evaluated regularly. As a check, they should also be compared with a reference value that can be determined, for example, from earlier data.

** Active Directory **

The evaluation of the log data generated in the monitoring can be done manually or with the help of special monitoring software, depending on their scope. In large Active Directory structures, a purely manual evaluation of the monitoring data can usually no longer be realized.

The results of the security monitoring should be summarized and evaluated in regularly created reports, so that basic security problems can be identified and remedied at an early stage.

During logging, security alerts can also occur, which must be responded to immediately, as intended in the emergency plan (see also the emergency management module) of the institution.

Basically, two methods can be used to detect changes to security-related configuration parameters of the domain controller or Active Directory. On the one hand this is the event notification, on the other hand it is the trend analysis.

Event notification defines so-called thresholds or limits for configuration parameter changes in Active Directory or on the domain controller itself. If a configuration parameter is changed and thus a previously defined limit value is exceeded, this event is logged by the operating system.

As part of the trend analysis, defined parameters are recorded over a longer period at regular intervals. If extreme changes are detected in the evaluation of this data, this could indicate security-related incidents. For example, collecting free disk space at regular intervals (such as every 5 minutes) and noticing a dramatic increase in disk space consumption may indicate a denial-of-service (DoS) attack against the domain controller.

** Domain controller status changes **

Changes to the domain controllers can affect the security of the Active Directory. Therefore, at least the domain availability and system resources areas should be monitored:
The availability of domain controllers can be monitored in several ways. It is conceivable, for example, the use of special monitoring software. Alternatively, regular LDAP queries can be sent to the domain controllers. Not only can this method be used to determine whether the corresponding domain controller is active (the test client receives a response), but also to draw conclusions about the system utilization of the domain controller from the response time.

It is also important to ensure that domain controller restarts are detected, as unauthorized domain controller restarts may indicate an attack. Accordingly, the system event logs of all domain controllers in an institution should be examined for unauthorized system reboots.

In addition to the direct availability of domain controllers, the domain controller's system resources should also be monitored. A change in system resources does not necessarily indicate an attack. Rather, the cause may also be technical in nature, for. For example, misconfiguration or obsolescence of hardware as Active Directory structures grow.

The following system resources should be monitored on all domain controllers in an institution:

* Percent processor utilization (upper limit: 80%)
* Free space on disk with the Active Directory database in percent (lower limit: 25%)
* Available memory in percent (lower limit: 10%)
* Bind time for LDAP connections (Noticeable would be an unusually large increase in binding time.)
* Number of successful LDAP connections per second (Noticeable would be an unusually large increase in LDAP connections, depending on the volume of LDAP connections within the institution.)
** Changes in Active Directory **

Changes made at the domain level usually affect all domain controllers, member servers, users, and workstations. The following changes are conceivable in this context:

* Change the domain-wide operations master role
 Changes to the domain-wide operations master roles affect the entire domain. The domain-wide operations master functions include the emulation master of the primary domain controller (PDC). In the event of a misconfiguration, this can adversely affect the overall construct of the domain and lead to far-reaching disruption within the network. A careful planning in advance with regard to proposed changes to the operations master functions is therefore indispensable.
* Change the trusts
 Trust relationships can be established between different domains of an institution. It is important to monitor changes in trust relationships, in particular to ensure that the addition of trust relationships and possibly extended rights of domain users are recognized as quickly as possible.
* Change the AdminSD folder
 The AdminSDHolder object is used by the primary domain controller (PDC) to protect the users of the service administrator groups and the service administrators group itself from unauthorized changes in permissions. For this purpose, the PDC should check every hour whether the user-definable access control lists (D ACLs) of the aforementioned user accounts match the DACL of the AdminSDHolder object. If the DACLs differ from each other, the DACLs of the user accounts must be adapted to the setting of the AdminSDHolder object.
* Changes to GPOs and their assignment
Changes to Group Policy such as: B. Domain user password policies affect the domain, and therefore all domain controllers in the affected domain, and should therefore be monitored. In addition, you must monitor the assignments of GPOs to domain containers and GPOs to the Domain Controllers Organizational Unit.
* Change the membership of predefined service administrator groups
 The unauthorized addition or removal of users in predefined service administrator groups such as: For example, administrators or backup operators may indicate an attack. Therefore, changes to memberships of service administrator groups should be monitored.
* Monitoring membership in the privileged groups
 The groups with AD administrative rights need to be considered regularly, especially when new members are added. Even more effective is a system (technically or organizationally implemented) that obtains formal confirmation before adding an account to a privileged group. This system can also exclude users from groups when their membership approval expires
* Modify audit policies for a domain
 An unauthorized change to the audit policy may interfere with the monitoring or even completely disable it. In order to detect a deactivation of the monitoring, the monitoring guidelines themselves must also be monitored.
Changes are made that affect the entire Active Directory tree, such as For example, if all defined domains affect the institution, it is called changes to the forest. Changes to the forest include the following events:

* Changes to the classification of domain controllers
 When a domain controller is promoted or demoted, there are changes in the domain controller rating.
* Changes to the Active Directory schema
 If the structure of the directory service database is changed, for example Changes to object classes or attributes within the Active Directory change the Active Directory schema.
* Changes to LDAP policies
 LDAP policies can be used to restrict LDAP requests and thus also access to the Active Directory data via LDAP.
* Replication topology changes between domain controllers
 Replication topology changes mean creating, deleting, and modifying Active Directory sites, site links, and subnets.
* Change the dSHeuristic attribute
 The dSHeuristic attribute controls the behavior of the Active Directory. For example, the collection of objects can be enabled or disabled.
* Changes to forest-wide operations master roles
 The forest-wide operations master roles are also historically referred to as Flexible or Floating Single Master Operations (FSMO). The FSMO includes the schema master and domain master functions.
All of the above-mentioned change events, both at the level of individual domains and in terms of forest, should be monitored and evaluated on all domain controllers in an institution. If an unauthorized change is detected during the evaluation of the security monitoring logs of a domain controller, appropriate emergency measures must be initiated which must be planned in advance.

For some events, the log files do not tell you which objects or attributes have changed. For this reason, the schema of the Active Directory must be documented so that changes can be identified and remedied later, if necessary, by means of manual synchronization.
If full remedying of unauthorized changes in the Active Directory can not be ensured, consider restoring the forest.

In the Service Admins group, you must monitor the creation, deletion, and modification of user accounts in the Services Administrators group. In addition, adding or deleting administrative workstations in the Service Admins organizational unit should be monitored.

When the space on the domain controller for the Active Directory database is exhausted, new objects can no longer be created in the Active Directory. Therefore, the space used by Active Directory objects should be continuously monitored.

With such monitoring, not only can the sprawling storage space for the Active Directory database be tracked, but also object flooding attacks can be detected, in which the storage space requirement increases dramatically in a relatively short time.

For a quick intervention in an object flood attack, a reserve file of any size can be created on the domain controllers. In the case of a disk space attack, the backup file on the affected domain controllers can be deleted to free up space short-term to ensure normal operation.

Afterwards, the unwanted objects of the attack in the Active Directory must be determined and removed.

** changes to critical files **

Both the domain controllers themselves and the administrative workstations should be set up to monitor for a change in critical files. It should at least monitor the files used to configure the operating system and installed applications. In addition, important executable files, such as For example, administration tools on the administrator workstations can also be monitored for changes.

To monitor the system configuration, you must first select a suitable software. Subsequently, a trusted basic configuration of the operating systems to be monitored should be created.

The monitoring software uses this configuration to create a reference image that will be used as the basis for future reviews. Check at regular intervals whether the current configuration of the domain controllers or administrator workstations has changed compared to the reference configuration. If changes are detected, the original system state must be restored as soon as possible.

#### APP.2.2.M12 Data backup for domain controllers

Because domain controllers typically enable centralized authentication and authorization tasks to access critical resources in the network, failure directly leads to severe network degradation. For this reason, the domain controller must be set as the central IT component for data backup. This should be documented either in the institution's data protection concept or in an independent data protection policy. The basic procedure is described in the module OPS.1.1.6 Data backup. In addition, additional domain controller-specific features must be considered when developing the data protection policy for Active Directory. This policy should consider the following aspects:

* On domain controllers, backups must be made on a regular and traceable basis.
* No institution-wide, general user accounts should be used for backups.
* Backup systems should only be deployed in locations where the security of the hardware and media is guaranteed.
* You must periodically test whether the domain controllers can be recovered using the backup media.
* Separate backup media must be destroyed.
Compared to conventional server backups, the following points should also be considered for domain controllers:

Recovery of a failed domain controller is rarely done using only backup media. It has proven useful to upgrade a member server to the domain controller and then replicate the Active Directory data from another domain controller. However, this method can only be used if the use of multiple domain controllers after the failure of one or more systems still has at least one valid Active Directory replica.

If there is only one domain controller, or if there is no Active Directory replica available after the domain controllers have failed, the recovery must be done through the backup media. It should be noted that under certain circumstances, problems such as faulty backup media, incomplete recovery procedures or lack of process know-how can occur among those responsible. To address these issues, ensure that administrators are familiar with the forest recovery procedures.

** Selection of compatible backup software **

Failure to properly handle the metadata of the files being backed up by the backup program, as well as the use of inappropriate antivirus software, may result in increased file replication by the File Replication Service (FRS).

Similar to the use of anti-virus programs (see APP.2.2.A5 hardening of the Active Directory) it is essential to make sure that the software to be used for the backup of domain controllers has been approved by the manufacturer when selecting the backup software.

** Special Security Requirements **

The service account that is used to back up domain controllers must have Services Administrator privileges and therefore high privileges. In order to prevent the misuse of these rights, the group of users who have access to these accounts should be kept as low as possible.

Therefore, it is recommended that you use different service accounts for the backup agent on the domain controllers than on the rest of the institution's servers. In addition, different user accounts on domain controllers and other servers additionally protect the domain controller in the event that a traditional server of the institution has been compromised.

Furthermore, the members of the Backup Operators group should be restricted to users required to back up the system files. Users responsible for backing up application data should not be a member of the domain controller's Backup Operators group. Rather, these users should be registered as members in the local group "Backup Operators" of the respective application server.

The domain group Backup Operators is not protected by default. In order to implement the corresponding protection, the access to the corresponding AdminSDHolder object (container object for storing authorizations) must be regulated as closely as possible (see APP.2.2.M7 Implementing secure administration methods for Active Directory).
Data backups of the domain controllers must be performed at regular intervals. When defining a suitable backup interval, it must be taken into consideration that Active Directory objects marked for deletion are not directly removed from the Active Directory but are first moved to a special container of the Active Directory ("Deleted Objects"). Such objects marked for deletion are called obsolete or "tombstone" objects.

After an adjustable period of time (default: 60 days), the obsolete objects are finally deleted. This method has the advantage that accidentally deleted objects can be reactivated within the deadline. When deleting the account or object is therefore initially effectively disabled so that it can no longer be used. However, if it turns out that it has been deleted prematurely, it can be quickly recovered.

To avoid problems with replication, care should be taken to ensure that the backups contain as few as possible obsolete objects with exceeded lifetimes. To ensure this, the backup media should be overwritten after approximately 75% of the lifetime of obsolete objects during regular backup. It should therefore be backed up as often as possible, but it is recommended to overwrite the backup media after 45 days (with an object life of 60 days) again with new backups, so that a restoration of obsolete objects is excluded.

Because the domain controller's backup media contains all the information in the Active Directory database, the same physical security precautions should be applied to them as they apply to the domain controllers. In particular for branch office backups, it must be checked whether sufficient security of the backup hardware and media can be guaranteed. There are the following options for this:

* There is no backup of the domain controllers in the branches.
* Branch office backup is done using remote backup systems (offline media) in secure data centers.
* Backup in the branch offices is done using local backups on disk.
These options should be assessed in terms of administrative, recovery and security guarantees. The health and fitness of the backup media must be checked at regular intervals by performing data recovery.

The backup media used in the field must be stored in a safe and secure location to prevent changes or theft of data. The medium itself is only to be inserted in the corresponding drive during the backup and restore. Also, procedures should be established that provide signatures of authorized administrators when retrieving archive backup media.

** Selection of domain controllers to backup **

If domain controllers are distributed in multiple locations (for example, in branch offices), data protection solutions should be sought that allow adequate protection of the backup process and the media used for it. It is important to ensure that the data backup concept is implemented appropriately for all domain controllers across all locations. Exist in a location z. If, for example, there are no secure storage options for the backup media, the backup media should be moved to a suitable location.

For branch offices, remote solutions are conceivable in which the data to be backed up is collected in a central location via the network. The following points should be noted in the context of a remote data backup solution:
* The integrity and confidentiality of the data must be protected by appropriate measures when transmitted over the network, eg. By encrypting the data to be backed up before or during transmission.
* There must be enough bandwidth so that neither operation nor backup is disturbed during a remote backup.
* If the data backup is carried out locally in the locations and then the backup media are collected from a central location, the access must be secured accordingly, eg. For example, access to file shares with locally cached backups should be restricted to domain administrators.
** Incremental Fuses **

For space-saving data backup system files are often resorting to incremental data backup procedures. These procedures only back up the files that have changed since the last backup. In the case of restoration, however, this method also entails an increased time requirement. Incremental backup should not be used for domain controllers, even the manufacturer advises against.

** recovery methods **

If, however, incremental backups are made, only the newly created data since the last full backup will be backed up. Older updates are not considered. In some cases, however, there may be a requirement to restore older update statuses and replicate them accordingly. B. in the course of a roll-back action. The affected data can be prioritized for replication using the ntdsutil command-line tool. Prioritization determines what data from the backup should be restored or what data should be retained. For this reason, the prioritization of the data should be carried out carefully, as this could lead to inconsistencies in the overall structure. For example, that locked or invalid user accounts are available again.

Image backup and restore of domain controllers is not recommended due to the inconsistency of updating sequence rollback (USN).

** Sufficient availability of backups **

So that the backups are also available in an emergency, it must be checked at the end of each backup process if it could be carried out without error.

In all domains, a backup check should be performed on a regular basis to ensure three aspects:

* It must be ensured that sufficient domain controllers have been successfully backed up during the relevant week.
* Make sure that the created backup media are clearly labeled with the unique name of the domain controller and the date of the backup, and then kept secure. The caption of the backup media should include the role of the domain controller to facilitate later identification.
* In the case of an unsuccessful data backup, the error must be remedied as soon as possible.
It is to be tested at regular intervals, whether the backups can be imported again. Successfully checked backup media should be marked accordingly. These tests must be performed in a separate test environment separate from the production environment.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### APP.2.2.M13 Two-Factor Authentication (CIA)
Privileged accounts in the area of ​​AD should be protected by means of two-factor authentication. Smart cards can be used for this purpose. Smart cards alone, however, do not provide protection against compromise because smart card logon sessions have an NTLM hash that can be read by attackers if improperly configured and misused as part of pass-the-hash attacks. The measure is therefore related to the safe configuration and hardening of the AD.

#### APP.2.2.M14 Dedicated Privileged Administration Systems (CIA)

It is possible to perform the administration of the Active Directory Services only by systems specially provided for this task (ie dedicated) and especially for this purpose hardened systems and to prevent the administrative access of all other systems. Such systems are often referred to as PAWs (Privileged Access Workstations) or, for example, internally at Microsoft, as SAWs (Secure Admin Workstations).

Recommended measures for securing the PAWs include the following points (for details, see the respective client blocks):

* UEFI / TPM / Secure Boot / Measured Boot
* BitLocker
* Standard User Configuration
* Applocker
* USB Media Restrictions
* Device Guard (Windows 10)
* Credential Guard (Windows 10)
* EMET (discontinued)
* Outbound traffic restrictions (no internet)
* Inbound Traffic restrictions (Default Deny)
* Automatic updates
* Endpoint protection
* Known Good Media Build Process
* Rapid Build Process
* Logon Restrictions
* Microsoft Security Baselines (SCM)
* Analysis of unsigned code
* OU and GPO ACL Lockdowns
* Lateral Traversal Mitigation (s)
* Authorized administrative tools only
#### APP.2.2.M15 Separation of administration and production environment (CIA)

For partitioning the user data, the administration environment can be outsourced to a separate forest. A one-way trust is established between the administration forest and the production forest so that the production environment trusts the administration forest. This option offers some advantages. For example, accounts in the administration environment can be provisioned as standard users who have no special rights in their own environment, but are highly privileged in the production environment. Further, by selectively authenticating the trust relationship further restrictions can be made as to which accounts can be used to log in to which systems.

At Microsoft, the concept is named "Enhanced Security Administrative Environment" (ESAE). This describes a set of reference implementations based on the idea of ​​forming "tiers" for workstations, servers, and AD. Different variants use different forests and additional technologies such as Microsoft Identity Manager (MIM) or Privileged Access Management (PAM) for fine-grained rights control and logging of privileged actions.

Each institution must create and validate its own tiering concept according to its own enhanced security requirements.

** gradation of protective layers **

Domain Controllers> Servers> Workstations

All systems should be classified into three categories:

* Critical systems (domain controllers, CA ...) that have control over other systems
* Server (Production IT)
* Workstations (Office IT)
No lower layer system may have control over a system of the overlying layer (s).

** Effort and complexity **

It should be noted that setting up and operating multiple forests entails high levels of complexity and potentially significant costs, as many systems and services need to be provisioned multiple times. This affects not only the AD infrastructure itself, but also the consistent implementation of the idea and other infrastructure components such as WSUS, antivirus, backup and clients / workstations.

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Further information on threats and security measures in the "Active Directory" area can be found in the following publications, among others:

* #### [ADFS] ADFS

  

 Microsoft TechNet and Faq-o-Matic, (last accessed 05.10.2017)
 <https://technet.microsoft.com/windows-server-docs/identity/active-directory-federation-services> and
 <Https://www.faq-o-matic.net/2014/04/02/adfs-grundlagen-und-architektur>

 
* #### [ADRC] Recycle Bin

  

 TechGenix, (last viewed 05.10.2017)
 <Http://techgenix.com/configuring-active-directory-recycle-bin/>

 
* #### [ADRL] AD Reading Library

  

 With further literature from the AD Security Blog, (last accessed on 28.09.2017)
 [https://adsecurity.org/page\_id=41] (https://adsecurity.org/page_id=41)

 
* #### [ADSB] Active Directory Security Blog

  

 Sean Metcalf, (last accessed on 28.09.2017)
 [https://adsecurity.org] (https://adsecurity.org)

 
* #### [ADSR] List of security resources

  

 AD Security Blog (last accessed on 28.09.2017)
 [Https://adsecurity.org/page\_id=399](https://adsecurity.org/page_id=399)

 
* #### [ESAE] Enhanced Security Administrative Environment

  

 Microsoft TechNet (last accessed on 28.09.2017)
 <Https://docs.microsoft.com/de-de/windows-server/identity/securing-privileged-access/securing-privileged-access>

 
* #### [LAPS2] Microsoft LAPS Security

  

 Active Directory Security, (last accessed 05.10.2017)
 <Https://adsecurity.org/?s=laps+security>

 
* #### [MSAV] Virus scanning recommendation on enterprise computers running supported versions of Windows

  

 Microsoft (last viewed 05.10.2017)
 <Https://support.microsoft.com/de-de/help/822158/virus-scanning-recommendation-for-enterprise-computers-that-are-running-currently-supported-versions-of-windows>

 
* #### [PAM] Privileged Access Management

  

 Microsoft, (last viewed 05.10.2017)
 <Https://docs.microsoft.com/en-us/microsoft-identity-manager/pam/privileged-identity-management-for-active-directory-domain-services>

 
* #### [PAW] Privileged Access Workstations

  

 Microsoft TechNet, 04.2016
 [http://download.microsoft.com/download/9/3/9/9392A4D2-D530-4344-8447-4A7CF1C01AEE/Privileged%20Access%20Workstation\_Datasheet.pdf](http://download.microsoft.com/ download / 9/3/9 / 9392A4D2-D530-4344-8447-4A7CF1C01AEE / Privileged% 20Access 20Workstation_Datasheet.pdf%)

 
* #### [SYSOPS] Enhanced Security Amdinistrative Environment ESAE 4sysops

  

 Microsoft, (last viewed on 05.10.2017
 <Https://4sysops.com/archives/microsoft-enhanced-security-administrative-enviroment-esae/>

 
* #### [TN283324] Entry Point Active Directory for Windwos Server 2012 (R2)

  

 Microsoft TechNet, (last accessed on 28.09.2017)
 [https://technet.microsoft.com/en-us/library/dn283324.aspx] (https://technet.microsoft.com/en-us/library/dn283324.aspx)

 
* #### [TN378801] Active Directory entry point for Windows Server 2008 R2

  

 Microsoft TechNet, 05.2009
 <Https://technet.microsoft.com/en-us/library/dd378801.aspx>

 
* #### [TN731367] Securing the DNS Server Service

  

 Microsoft TechNet, (last accessed 05.10.2017)
 <Https://technet.microsoft.com/en-us/library/cc731367.aspx>

 
* #### [TN755321] Security Considerations for Trust

  

 Microsoft TechNet, (last accessed 05.10.2017)
 <Https://technet.microsoft.com/en-us/library/cc755321.aspx>
