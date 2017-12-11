1 description
--------------

### 1.1 Introduction

These implementation notes cover common security requirements for all IT systems that provide services to other IT systems, such as clients or other servers. These services may be basic services for the local or external network, but also allow e-mail exchange or offer databases and print services. Servers are of central importance to information technology and thus to the functioning work processes of an institution. Often, servers perform tasks without any direct interactive use by a user. In addition, there are server services that interact directly with the users and are not perceived at first glance as a server service, for example, X servers under Unix.

### 1.2 Life cycle

** planning and conception **

In the run-up to the actual planning, the general architecture of the network has to be defined or analyzed, from which generally also specifications for the operating systems to be used (server and client) result. In particular, it must be determined which goals are to be pursued with the server to be set up. For this purpose, the expected application scenarios are to be described and the intended use defined.

If a new network is to be set up, the structure of the network as a whole must first be planned, with questions such as the definition of a network topography and the decision on the degree of server centering (terminal server, "classic" client-server architecture or use of peer-to-peer networks). Peer functionality). Here the measures of the module NET.1.1 network architecture and design are to be used.

In a further step, the definition of the operating systems used at the server and client level and, if necessary, the selection of specific variants (eg Windows Server 2016 versus Windows Server 2012 or Linux versus a vendor-specific variant of Unix) follows.

If a new network is set up, the detailed structure of the network must be planned as the exact technical basis for further work. The number and interaction of the intended servers must be specified. The tasks of the servers and the way of their use by the clients are to be determined. Based on the availability requirements, it must be determined to what extent redundant structures are to be provided in the network. Here are also the necessary specifications for the infrastructure (especially air conditioning and power supply, see SYS.1.1.M15 local uninterruptible and stable power supply) set. In parallel, a general security policy must be developed (see SYS.1.1.M11Setting a security policy for a general server), which must then be supplemented by system-specific security guidelines and detailed guidelines for the use of hardware and software in the network (see also the modules for the individual server operating systems).

**Procurement**

The next step is to procure the hardware and any additional software required. Based on application scenarios, the requirements for products to be procured must be formulated and, based on this, the selection of suitable products must be made. The procurement of these products then forms the basis for the work of the next step. More detailed information on procurement can be found in module OPS.1.2.6 Procurement, Tendering and Purchasing.

**Implementation**Users or administrators have a significant impact on the security of a server. Before the actual commissioning, the users and administrators must therefore be trained for the handling or use of the server to be set up. Especially for administrators, intensive training is recommended due to the complexity of planning and administration. The administrators should acquire detailed knowledge of the system so that a consistent and correct system administration is guaranteed. In particular, users should be taught how to use the available security mechanisms. Here are the requirements of the module ORP.3 Sensitization and Information Security Training.

After the organizational and planning preparatory work has been carried out, the installation and commissioning of the server can take place. The following recommendations must be observed:

* Even the installation and basic configuration of a server must be carried out with particular care in order to avoid hard-to-repair errors from the outset. General information can be found in SYS.1.1.M16 Safe Installation. In addition to the general measures described in these implementation notes, the additional measures recommended in the respective blocks for the respective operating system must be implemented in each case.
* After the installation and basic configuration of the servers, higher-level management structures may need to be configured. Among other things, it also comes into play for which purpose the individual servers are planned, for example as a file server, print server or, in the case of thin clients, as a terminal server. Here, in particular, the measure SYS.1.1.M6 deactivation of unneeded services and identifiers is important in order to be able to ensure controllable operation of the server.
* After the installation and basic configuration of the server is completed, the actual server software can be installed and configured. Depending on the type and intended use of the software, the necessary steps differ considerably in some cases and are partly treated in their own modules. In principle it is recommended to proceed in the same way as for the installation and configuration of the server software as for the configuration of the operating system itself:

 
+ Creation of an installation concept
+ If several servers with similar applications and configuration are to be installed: Creating a reference installation
+ Installation, basic configuration, update and hardening
+ Test and optional penetration test with increased protection requirements


 
**Business**

After the initial installation and a test operation phase, normal operation is started. From a security point of view, the following aspects should be considered:

* Client-server networks are changing very often. It must be ensured with every change that the security is not affected even after the change. The aspects to be considered in detail are contained in the modules for the respective server operating systems. It should be remembered that the withdrawal of authorizations as well as the deletion of unneeded databases are regulated in such a way that obsolete structures do not create any security gaps. An essential help here is an efficient, comprehensive system administration, which can always rely on up-to-date information about the state of the system and its legal structures (see SYS.1.1.M3 Restrictive Rights Assignment and SYS.1.1.M21 Operating Documentation).* One means of maintaining the security of a server is to monitor the system or its individual components. The relevant recommendations can be found in SYS.1.1.M10 logging and SYS.1.1.M23 system monitoring. In particular, privacy aspects also play a role. The frequent vulnerabilities of most client-server systems and the plethora of attacks that address these vulnerabilities require administrators to be constantly aware of the security status of the systems and new threats, and to take timely countermeasures (see SYS .1.1.M7 updates and patches for operating system and applications).
** ** segregation

A server must not be shut down without notice. When a server is to be decommissioned, if it has a direct impact on users, it must be timely informed and a number of issues must be addressed to prevent downtime and data loss. These items are described in SYS.1.1.M25 Regulated Decommissioning of a Server.

When segregating a server, it must also be ensured that there is no longer any information worth protecting on the data carriers. It is not enough to simply reformat the disks, but they must be completely overwritten at least once. It should be noted that a mere logical erasure and also not reformatting the data carrier with the means of the installed operating system does not remove the data from the data carriers, so that they can be reconstructed with suitable software, often even without much effort. In-depth information can be found in OPS.1.1.8 Delete and Destroy.

The segregation of the server must be documented. Inventories and networks must be updated, and as long as the separation results in structural changes in the information network, the security concept should also be adapted accordingly.

** Emergency Preparedness **

Only a regular and comprehensive data backup reliably ensures that all stored data can be made available even in case of faults, failures of the hardware or (intentional or unintentional) deletions. The necessary requirements are described in the module OPS.1.1.5 Data backup.

In addition to the protection during operation, however, the emergency preparedness also plays an important role, because only so the damage in an emergency can be reduced. Information on emergency preparedness can be found in the DER.4 Emergency Management module. This includes planning the handling of security incidents, which should be based on the requirements of the module DER.2.1 Incident Management. Some notes on specific aspects that should be considered in emergency preparedness for a server are described in SYS.1.1.M22 Integration with Emergency Preparedness.

It is assumed that the server is housed in a server room (see module INF.12 server room), a server cabinet (see module INF.6 Protective cabinets) or in a data center (see module INF.2 data center). The requirements to be implemented for the server operating systems can be found in the respective operating system-specific blocks. This also applies to the connected clients. The requirements of the module OPS.1.1.2 Network and System Management are in any case the overarching framework for the operation of server-based networks.

2 measures
-----------

The following are specific implementation hints in the General Server section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### SYS.1.1.M1 Suitable installation [building services]A server must always be installed or installed in a lockable computer room or server cabinet. It is to be regulated who receives access to the room or access to the server itself. For this purpose, the requirements of the modules INF.5 technical room, INF.6 protective cabinet or data center must be implemented.

#### SYS.1.1.M2 user authentication

The identification and authentication mechanisms of IT systems or IT applications must be designed so that users are uniquely identified and authenticated. Identification and authentication must occur before any other interaction between the IT system and the user. Further interactions may only be possible after the users have successfully identified and authenticated. The authentication information must be stored in such a way that only authorized users can access it (check it or change it). With every interaction, the IT system must be able to determine the identity of the user.

There are several techniques that can prove the authenticity of a user. The most well-known are:

* PINs (Personal Identification Numbers)
* Passwords
* Tokens such as B. access cards
* Biometrics
For security-critical areas of application, strong authentication should be used, combining two or more authentication techniques, such as password plus transaction numbers (one-time passwords) or plus smart card. Therefore, this is often referred to as two-factor authentication or multi-factor authentication. All authentication techniques used must be state-of-the-art.

** ** Passwords

If passwords are used for authentication in a client, the security of the access and access rights management of the IT system is crucially dependent on the correct use of the passwords. For this, a guideline for password usage should be created and published. In addition, IT users should regularly, e.g. At team meetings, be noted.

When passwords are used for authentication, the IT system should provide mechanisms that meet the following conditions:

* It ensures that each user uses individual passwords (and can select them himself).
* It is checked that all passwords meet the defined specifications (eg minimum length, no trivial passwords). The password quality check should be individually controllable. For example, it should be possible to specify that the passwords must contain at least one special character or that certain character combinations are prohibited.
* The IT system generates passwords that meet the defined requirements. The IT system must offer the passwords thus generated to the user.
* The password change should be initiated regularly by the IT systems. The lifetime of a password should be adjustable.
* The repetition of old passwords when changing the password should be prevented by the IT system (password history).
* When entering the password, the password should not be displayed on the screen.
* After installing or reconfiguring users, the password system should force a password change after initial login.
More detailed information on authentication can be found in ORP.4 Identity and Permission Management.

#### SYS.1.1.M3 Restrictive rights assignment

Access rights to files that are stored on the data carriers of the server must be assigned restrictively. Users are only allowed access to the files they need to complete their tasks. The access right itself is limited to the required access type (see "Allocation of access authorizations"). For example, it is rarely necessary to assign a write permission to program files.In most cases, the inheritance of rights to files in subdirectories may be accessed if an access right to the parent directory existed. As a result, top-level access (volume level) should be granted only very restrictively. In particular, when installing new software products, the assignment of rights must be subject to strict control.

If the server storage space is low, you can set a limit on the maximum amount of storage that a user can use on the server.

** Assignment of access rights **

Access privileges allow the data subject or an authorized representative to use certain IT systems or system components and networks. Access authorizations should be granted as restrictively as possible. These are to be specified for each authorized person on the basis of their function, taking into account the separation of functions. According to the function the access to the computer has to be defined. B. Access to the operating system (system administrator) or access to an IT application (user). In addition, it must be ensured that personnel and task-related changes are taken into consideration without delay.

Access to IT systems or IT applications should only be possible after an identification (eg by name, user ID or chip card) and authentication (eg by a password or via an authentication token) of the authorized user and logged become.

The issue or withdrawal of means of access such as user IDs or smart cards must be documented. Regulations on the handling of access and authentication means (eg handling of chip cards, password handling) must also be taken. All persons entitled to access must be made aware of the correct handling of the means of access.

Access authorizations should be temporarily blocked by authorized persons in the event of longer absences in order to prevent misuse; B. in illness or leave. This should be done at least for people with far-reaching permissions like administrators.

It is necessary to check sporadically the above specifications for their correct compliance.

** Administrators identifiers **

In many complex IT systems, eg. For example, on Unix or in a network, there is an administrator role that is not restricted. Under Unix, this is the super user root, in a Novell network the SUPERVISOR or admin. Missing restrictions increase the risk of errors or misuse.

In order to avoid mistakes, the super-user login should only be used if necessary; Other work should not be performed by administrators under an administrator ID, but by a personal ID. In particular, no programs of other users with administrator rights may be called. If administrative rights are required for certain activities, it is recommended to create and implement a role-based administration concept (see SYS.1.1.M14 Creation of a user and administration concept). In addition, routine system administration (for example, backup, setting up a new user) should only be menu-driven.

By division of tasks, regulations and agreement it must be ensured that administrators do not inconsistent or incomplete interventions. For example, a file may not be edited and changed by several administrators at the same time, as only the last saved version will be preserved.For all administrators, additional user IDs should be set up that have only the limited rights administrators require to perform administrative tasks. For non-administration work, administrators must use only these additional user identifiers.

#### SYS.1.1.M4 Role separation

Basically, a distinction can be made between identifiers for users and administrators. Only administrators manage the IT systems, while normal user IDs only have the rights to perform their work-specific tasks. Normal user IDs may not have administration rights to protect the operating system and client configuration from accidental, negligent or intentional modification by the user.

If users only need to perform certain administrative tasks, it is often not necessary to give them all rights associated with their own login or even system administrator rights. Examples include certain routine system administration activities, such as creating backups or setting up a new user menu-driven with a program, or activities that require a user to have only a single application program. In particular for temporary staff and external service providers, care should be taken that they only use the services and only access the data they actually need. When their activity is over, their accounts should be disabled and all access permissions removed.

For these users, a limited user environment should be created. For example, it can be implemented under Unix by a restricted shell (rsh) and a restriction of the access paths with the Unix command chroot. Another possibility is to run individual application programs, such as web browsers, in the so-called kiosk mode, so that there is only limited access.

If particularly extensive rights are assigned to user IDs, this should be as restrictive as possible. On the one hand the circle of privileged users should be restricted as far as possible and on the other hand only the rights needed for the execution of the work should be assigned. For all tasks that can be performed without extended rights, privileged users should also work under identifiers with standard rights.

#### SYS.1.1.M5 Protection of administration interfaces

There are different access options to administrate servers. Depending on the type of access used, a number of security precautions must be taken. For larger networks, it is recommended to integrate the servers in a central network management system, since otherwise a secure and efficient administration can hardly be guaranteed. The methods used for administration must be defined in the security policy and the administration must be performed only in accordance with the security policy.

In general, it is important to get an overview of what part of the administration of a server is normally

* locally via the console,
* remotely over the network, but using the standard mechanisms of the operating system, or
* via a central network-based administration tool
should be carried out. It is recommended to provide an overview of the various types of use, which administration activities can be carried out by which route. In particular, it is important to note whether certain activities can not normally be carried out in a particular way.

* Local administrationA server should in principle be installed in a server room or at least a lockable server cabinet. For the part of the administration, which should or must be done partially locally via the console, appropriate specifications must be made for who gets access to the console, which type of authentication may be used for local access and which other requirements must be taken into account.
* Remote administration
 Usually a server is not administered locally at the console but from a workstation via the network. In order to prevent authentication information of the administrators and configuration data of the servers from being intercepted or even manipulated by an attacker, the administration should only take place via secure protocols (for example, not via Telnet, but via SSH, not via HTTP but via HTTPS). Alternatively, a separate administration network can be set up that is separate from the rest of the network. Unsecured remote administration over external (insecure) networks must never take place. This must already be taken into account when establishing the security policy. Also in the internal network, as far as possible, no unsafe protocols should be used.
* Administration via a central management system
 If a central management system is to be used for the administration of the server, analogous considerations should be made for this access channel, as for remote administration. In addition, it is important that the central management system itself be configured and administered accordingly.
** secure authentication **

In principle, IT systems should ensure that all users who want to access them have to authenticate themselves. This is the only way to prevent unauthorized persons from gaining access to the services offered by the system or to the data stored on the system.

As a rule, servers are administered via a network connection. The information needed for network-based authentication must be transmitted over a LAN or WAN. Therefore, it is imperative that this information can not be read or changed.

It must also be ensured that an attacker can not log in by replaying recorded credentials. Therefore, the credentials that are exchanged for authentication between server and client must be encrypted and additionally dynamized, for example with challenge-response methods.

After the authentication has been successfully completed, the system must ensure that users only have access to those services and data for which they have appropriate permissions.

If there is a danger of listening to lines to terminals, administrators should only work on the console so that passwords can not be intercepted. When administering Unix systems, encrypted communication can be done using the Secure Shell protocol, for example. This allows secure administration from remote workstations.

#### SYS.1.1.M6 Deactivation of unneeded services and identifiers

The standard installation of an operating system often includes a number of programs and services that are not normally needed and that can be a source of security vulnerabilities for that very reason. This applies in particular to network services. After installation, it therefore needs to be checked which services are installed and activated on the system. Unnecessary services must be disabled or completely uninstalled.On the one hand, checking for running services can be carried out locally with the means of the installed operating system and, on the other hand, in the case of network services, from the outside through a port scan from another system. By a combination of both methods can be largely excluded that the system offers even more unwanted network services.

** Secure Login **

You should use a login program or activate options so that the following actions can be taken:

* Each user must have their own ID and password. No access without identifier or password may be possible. As a password replacement, the authentication of the user can also be done via electronic signatures, passport tickets or the like.
* The number of unsuccessful login attempts can be limited. After each unsuccessful login attempt, the waiting time increases until the next login request. After a certain number of failed attempts, the affected user ID and / or the terminal will be blocked. It should be remembered that this does not exclude the administrators, it must remain open at the console access to the administration.
* The time of the last successful login is reported to the user at login.
* Unsuccessful login attempts are reported to the user at login. It may be necessary to repeat this message for several subsequent logins.
* The time of the last logout is reported to the user at login. A distinction is made here between logouts for an interactive login and those for a non-interactive login (logout of background processes).
* For login via networks in which passwords are transmitted unencrypted, the additional use of one-time passwords is recommended.
** Block and delete unneeded accounts and terminals **

If there are no serious reasons to do so, accounts that are not used for a long period of time should be blocked and deleted later. If deleting accounts leaves files that are no longer associated with an existing user entry, there is a risk that these files will be assigned to unauthorized users later on.

Before the home directories of the users are deleted, they should be backed up beforehand. When blocking or in any case before deleting an account, the affected user should be informed. When deleting accounts, make sure to find the files of the user who are not in his home directory. Such files must be deleted or assigned to other users. Furthermore, it is important to ensure that ongoing processes and pending orders are deleted, z. B. under Unix in the crontab.

Similarly, terminals that are not used for a long period of time should be blocked and removed later.

If a newly created user needs his or her account for a limited time, it should only be set up for a limited time. It may be advantageous to set up accounts only for a limited period of time and to renew them at regular intervals (eg annually) if necessary.

** ** Quotas

Even if the procurement of an IT system has been made to ensure that it has enough storage space, storage space sooner or later becomes scarce in the event of prolonged use. On IT systems that are used by different users, the existing resources must therefore be divided so that all users can work as optimally as possible.Often you can observe the phenomenon that users want to have more storage space than is available to them. In addition to the ever-growing storage footprint of applications, another reason is that many users are reluctant to part with old and unneeded files. If no restrictions are made on storage space limitation and archiving, there is a risk that storage space for large amounts of legacy data will be wasted or the user directories will overflow.

A simple solution would be to always provide more and more storage space as needed as demand increases. However, this is not always feasible in practice. Even if the users are sensitized for economical data storage, each unnecessary file is nevertheless often considered important.

For users or user groups, but also for applications, Disk Quotas can set a storage volume that must not be exceeded. On servers and all IT systems that are used concurrently by multiple users or applications, disk space should therefore be restricted for individual users as well as for applications through disk quotas. This includes servers (such as file, web, and mail servers) and clients with multiple user IDs. For clients where the data is separated from the system partition and used by only one user, a disk quota can be omitted.

The choice of the quota volume is important. If all users are to receive the same quota volume, the required volume can be calculated by dividing the space to be used by the number of users. In addition, however, a space reserve should be scheduled. The problem is the choice of a too small disk quota. If users have too little disk space available, they might try to store the information outside the intended directories to circumvent the restrictions. For this purpose, then frequently used locations that are not suitable for such. Temporary directories or other directories writable to all users. When space on file servers is too tight, users often rely on local disks. In many cases, this violates the regulations and may, for example, result in the files not being included in the central backup.

On the one hand, it should be determined which information should be stored where and how many versions of a file should be stored on the production system for how long.

Data from completed projects should be archived in an orderly manner and should not be kept in stock on the production systems "for all cases". On the other hand, it should be determined how much storage space is made available to the various user groups and applications. In addition, a reserve should be scheduled. It also needs to be determined how users can be allocated more storage when needed. The set values ​​must be documented. They also need to be regularly reviewed and updated.Once the size of the disk quota has been determined, consideration should be given to whether and how to respond to a higher demand for disk space. This decision is influenced by the selection of a quota type. Hard quota limits are set so users will not be able to use more than their allocated storage quota. A soft quota, on the other hand, allows users to exceed the disk quota for a fixed amount of time and up to a specified limit. If the disk quota is exceeded, at least the user must be informed about this, for example by e-mail. Consideration should also be given to notifying IT operations so that they can respond to any problems that may arise. In addition, it must be determined whether and how individual users can be allocated additional storage space. This should be a regulated and comprehensible procedure. Disk quotas should not be increased "on demand".

Many popular operating systems include tools to set up Disk Quotas. However, it should be checked if additional software is needed to set up and manage a disk quota.

#### SYS.1.1.M7 Updates and patches for firmware, operating system and applications

Often, errors in products become known, which can lead to the information security of the information network, where they are operated, is affected. Corresponding errors can affect hardware, firmware, operating systems, and applications. These vulnerabilities need to be addressed as soon as possible so that they can not be exploited by internal or external attackers. This is especially important when the systems are connected to the Internet. Operating system or software component manufacturers typically release patches or updates that must be installed on their IT system to correct the error (s).

The system administrators should therefore regularly inform themselves about known vulnerabilities.

It is important that patches and updates, like any other software, can only be obtained from trustworthy sources. For each system or software product used, it must be known where security updates and patches are available. It is also important to verify the integrity and authenticity of the products already installed, or the security updates and patches to be incorporated (see the section "Ensuring the Integrity and Authenticity of Software Packages") before installing an update or patch. Before installation, they should also be checked using a computer virus protection program. This should also be done for packages whose integrity and authenticity have been verified.

Security updates or patches, however, must not be prematurely recorded, but must be tested before importing. These tests should always use up-to-date, system-tuned test plans or automated tests for a consistent, meaningful result. Otherwise, if a conflict arises with other critical components or programs, such an update may cause the system to fail. If necessary, an affected system must be protected by other means until the tests are completed. It should be ensured that updates that are imported by automatic update mechanisms are also tested.

Before installing an update or patch, you should always back up the system, which will allow it to recover to its original state if problems occur. This is especially true if detailed tests can not be performed due to lack of time or due to a lack of a suitable test system.In any case, it must be documented when, by whom and for what reason patches and updates were recorded. From the documentation the current patch level of the system must be able to be determined quickly at any time, in order to gain clarity as soon as the weaknesses become known as to whether the system is at risk.

If it is determined that a security update or patch is incompatible with another major component or program or is causing problems, it is important to consider how to proceed. If it is decided that a patch will not be installed due to the problems that have arisen, this decision must be documented in any case. In addition, it must be clear in this case which measures have been taken to prevent exploitation of the vulnerability. Such a decision must not be made by the administrators alone, but must be agreed with the supervisor and the ISB.

** Ensuring the integrity and authenticity of software packages **

Carelessly executing programs that originate from "unsafe" sources can cause considerable harm. Malware, for example, can install password-spying programs, Trojan horses, or backdoors on a computer, or easily corrupt or erase data.

Typical sources of such malware are, for example, programs that display themselves as screen savers, virus scanners or other utilities and are attached to e-mails. Often these are sent under fake sender addresses to many recipients. Often the programs are downloaded from the internet and installed without verification.

Even if no encryption or signature techniques are used otherwise, the use should be considered to the extent described in this measure.

In principle, software should only be installed from well-known sources, especially if it has not been delivered on data carriers but has been downloaded from the internet, for example. This is especially true for updates or patches that are typically no longer delivered on disk. Most manufacturers and distributors offer checksums that allow at least an integrity check of a package. The checksums are usually published on the websites of manufacturers or sent by e-mail. To verify the integrity of a downloaded program or archive file, the published checksum is then compared to a locally generated checksum by a corresponding program.

If checksums are offered for a software package, these should be checked before installing the package.

A verification of authenticity can not be done with checksums. Therefore, in many cases, digital signatures are offered for programs or packages. In turn, the public keys needed to verify the signature are usually available on the manufacturer's websites or from public-key servers. Often the checksums are generated with one of the programs PGP or GnuPG.

If the check reveals that it is a valid signature of the respective manufacturer, this results in a significantly higher degree of trustworthiness for the package than simply the presence of a checksum.

Sometimes even the built-in software update mechanisms of the respective operating system or application software do not perform checksum comparisons. If possible, however, a checksum check should be performed on each software package before importing.Furthermore, not all checksum comparisons can be performed without the involvement of the users, since the checksums, signatures or certificates required for this purpose are not provided by the manufacturers in a uniform manner. This often requires manual verification on the manufacturer pages or customization of URLs in the patch and change software.

If digital signatures are available for a software package, they should always be checked before installing the package.

A fundamental problem with the use of digital signatures is the verification of the authenticity of the key used itself. If the public key carries no signature of a known trustworthy person or organization (such as a trust center), the signatures generated with the corresponding private key offer no real security in that the software package actually comes from the developer, manufacturer or distributor. Therefore, if not certified, the public keys should preferably be obtained from a source other than the software package itself, for example from a manufacturer's CD-ROM, from another mirror server on which the package can also be downloaded, or from one Public key server.

To check checksums and digital signatures, the corresponding programs must be available locally. Administrators should be aware of the meaning and validity of checksums and digital signatures. In addition, the administrators must have enough time to use the appropriate programs in their daily work and familiarize themselves with the operation.

Obtaining patches and email changes is not recommended for a variety of reasons. The origin of emails is difficult to determine without the use of additional security mechanisms and the recipient addresses in the institutions are often distribution lists, whose address is easy to guess. Patches and changes can also be very extensive by now. Many companies and government agencies have limited the size of email attachments and may also prohibit the adoption of executable attachments. Furthermore, the large amounts of data unnecessarily burden the e-mail systems. Therefore, a timely availability of the software changes, which can be critical, especially in the case of security patches, can not be adequately ensured via e-mail.

Furthermore, some manufacturers offer to send changes and patches to the customer directly on data carriers. In this case too, the patches and changes should be verified using checksums or digital signatures, as sender information on mailpieces and manufacturer logos on CDs and DVDs can easily be faked.

Another aspect of verifying the authenticity of the update may be news published by the manufacturer on its website, newsletter or similar channels. Some manufacturers have established cycles and timepoints that typically release information about changes systematically.

#### SYS.1.1.M8 Regular backup

Only a regular and comprehensive backup reliably ensures that all stored data can be made available even in the event of malfunction, the effects of malicious software, hardware failures or (intentional or unintentional) deletions. The necessary requirements are described in the module OPS 1.1.5 Data Backup.

#### SYS.1.1.M9 Use of virus protection programsDifferent modes of action can be used to protect against malicious programs. Programs that search IT systems for all known malicious programs have proven to be an effective means of malicious program prevention in the past. Therefore, according to the requirements described in OPS1.1.4 Protection against malware, virus protection programs should be used.

#### SYS.1.1.M10 logging

The possible logging on the server is to be activated to a reasonable extent. The IT operation must periodically check the server's log files. All security-related events should be logged. The following events are of particular interest:

* incorrect password entry for a user ID up to the blocking of the user ID when the failed test limit is reached,
* Attempts of unauthorized access,
* Power failure,
* Data on network utilization and congestion.
How many events are logged depends, among other things, on the protection requirements of the respective IT systems. The higher their protection requirements, the more should be logged.

Since the log files can become very extensive over time, the evaluation intervals should be chosen so short that a meaningful evaluation is possible. In order to enable a meaningful evaluation, each protocol entry should contain user identification or process number, identification of the terminal, date and time.

It is necessary to check which legal or contractual retention periods for log files have to be observed. In order to ensure the traceability of actions, a minimum storage period may be prescribed, for privacy reasons there may also be a deletion obligation.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "general server".

#### SYS.1.1.M11 Setting a security policy for servers

The security requirements for each server are based on the organization-wide security policy. Based on the general policy, the requirements for the given context must be specified and summarized in a security policy for the server or a group of servers. In this context, it must be examined whether, in addition to the organization-wide security guideline, further superordinate specifications such as IT guidelines, password guidelines or Internet usage guidelines must be taken into account.

The security policy must be known to all persons and groups involved in the procurement and operation of the servers and be the basis for their work. As with all directives, their content and implementation must be regularly reviewed by a higher level audit.

The security policy should specify the level of security generally to be achieved and make basic determinations about the operation of the server. To improve clarity, it may be useful to develop separate security guidelines for different areas of application.

First of all, the general configuration and administration strategy ("Liberal" or "Restrictive") should be defined, as the further decisions depend essentially on this definition.

For servers that only store and process data with normal protection requirements, a relatively liberal strategy can be chosen, which in many cases simplifies configuration and administration. In general, however, it is also advisable in these cases to interpret the strategy only "as liberally as necessary".In principle, a restrictive strategy is recommended for a server that stores or processes sensitive data. For servers with special protection needs regarding one of the three basic values, a restrictive configuration and administration strategy should be implemented.

Here are some things to consider:

* Physical access control regulations: A server should always be installed or installed in a lockable computer room or server cabinet. It is to be regulated who receives access to the room or access to the server itself.
* Decide if the server should be virtualized (see SYS.1.5 Server Virtualization).
* Regulations for the work of administrators and auditors:

 
+ According to which scheme are administration rights assigned? Which administrator is allowed to exercise which rights and how does he obtain these rights?
+ Which access paths should administrators and auditors use to access the systems (for example, only locally at the console, via their own administration network or via encrypted connections)?
+ Which processes have to be documented? In what form is the documentation created and maintained?
+ Is a four-eye principle valid for certain changes?


 
* Specifications for installation and basic configuration

 
+ Which installation media are used for installation?
+ Should a central authentication service be used or is user administration and authentication only local?
+ Rules for user and role management, authorization structures (procedure and methods of authentication and authorization, authorization for installation, update, configuration changes, etc.). If possible, a role concept for the administration should be developed.
+ Defaults for the software packages to be installed.


 
* If the server has been scheduled to encrypt parts of the file system, it is recommended that you specify how this should be done:

 
+ Which parts of the file system should be encrypted?
+ What mechanism should be used to implement the encrypted file system?
+ Which crypto algorithms and key lengths should be used?
+ Which data should be stored in the encrypted file systems?
+ How are the encrypted file systems included in the backup?


 
* Regulations for the creation and maintenance of documentation
* Requirements for safe operation

 
+ Which user group is allowed to log on locally on the system?
+ Which users get access through the network? Which protocols may be used?
+ What resources can users access?


 
* Password usage rules (password rules, rules and situations for password changes, password deposit, if applicable)

 
+ Who can shut down the system?


 
* Network communication and services

 
+ Should a local packet filter be set up?
+ Which network services are offered by the server?
+ Which authentication methods should be chosen for the offered services?
+ Which external network services should be accessible from the computer?
+ If a distributed file system is to be integrated Distributed file systems in which the user data is transmitted unencrypted should only be used in the internal network. If a distributed file system is to be used over an insecure network, it must be secured by additional measures (cryptographically protected VPN, tunneling).


 
* Logging

 
+ Which events are logged?
+ Where are the log files stored? Are they stored locally or should a central server be used where the individual systems in the network send their logging information?+ How and at what intervals are the logs evaluated?
+ Who has access to the log files?
+ Is it guaranteed that personal information will not reach unauthorized persons?
+ How long should the log files be saved?


 
Based on the above points, a checklist can be created that can be helpful in audits or revisions.

Responsibility for the security policy lies with the security management, changes and deviations from it may only be made in coordination with the security management.

When creating a security policy, it is advisable to proceed in such a way that first of all a maximum of requirements and specifications for the security of the systems is established. These can then be adapted to the actual circumstances. Ideally, this will ensure that all necessary aspects are taken into account. The reason for non-consideration should be documented for each deficient or weakened default in the second step.

#### SYS.1.1.M12 Planning the server deployment

A basic requirement for a server to operate safely is an adequate level of planning in advance.

Planning for the use of a server can be carried out in several steps according to the principle of top-down design. Based on a rough concept for the overall system, concrete plans for sub-components are defined in specific sub-concepts. Planning does not only concern aspects that are classically associated with the term security, but also normal operational aspects that entail security requirements.

In the rough concept, for example, the following typical questions should be dealt with:

* Which tasks should the system to be planned fulfill? Which services should be provided by the server? Are there any special requirements for the availability of the system or for the confidentiality or integrity of the stored or processed data?
* These specifications come from overarching planning and are determined by the general objectives. The more precisely the general conditions are known and the more precisely the requirements are formulated, the easier the following planning steps become.
* Should specific hardware components be used in the system? This can be important, for example, for the selection of the operating system.
* Which requirements for the hardware (CPU, main memory, capacity of the data media, capacity of the network, etc.) arise from the general requirements?
* Is the network used a homogenous or heterogeneous computer network?
* Does the system replace an old, existing one? Do you want to transfer datasets or hardware components from the old system?
* Should the data be stored locally or on a SAN system?
* Should the servers be virtualized?
The following subconcepts should be considered when planning the server deployment:

* Authentication and user management:
 What types of user management and user authentication should be used on the system? Are users only managed locally or should a central administration system be used? Should the system access a central, network-based authentication service or is only a local authentication required?
* User and group concept:
 Based on the organization-wide user, rights and role concept, appropriate rules for the system must be created.
* Administration:
 How should the system be administered? Are all settings made locally or the server integrated in a central administration and configuration management?
* Partition and file system layout:In the planning phase, a first estimation of the required disk space should be carried out. For ease of administration and maintenance, it is recommended that as far as possible separate the operating system (system programs and configuration), application programs and data (for example, database server and data), and possibly user data. Various operating systems offer different mechanisms for this (division into drives under Windows, file systems under Unix). Often it can be useful to save certain data even on your own hard disk or your own disk system. This allows, for example, to take over the data on the other partitions without copying when reinstalling or updating the system.
 If confidentiality data is stored on the server, the use of encrypted file systems is strongly recommended. Not necessarily all file systems need to be encrypted, but it will often be sufficient to provide encryption for the part of the file system on which the data itself is stored. This is facilitated by proper planning of the partition and file system layout. When selecting encryption of individual files and directories, users should be given the option of whether the files are encrypted or stored unencrypted. During the planning phase, the planned partitioning of the partitions and their size should be documented.
* Network services and network connection:
 Depending on the requirements for the confidentiality, integrity and availability of the data that is to be stored or processed on the server, the network connection of the server must be planned.
 In general, it is recommended that you do not place a server directly on the same IP subnet as the clients you want to access the server. If the server is disconnected from the clients by at least one router, then there are much better ways of controlling access and detecting network traffic anomalies that indicate potential problems.
* A server that stores or processes data with a high confidentiality or integrity protection requirement should be located on its own IP subnet and at least be separated from the rest of the network by a packet filter. With a very high protection requirement, an application level gateway should be used.
* With normal protection requirements, a server that is used exclusively by clients from the internal network can, exceptionally, also be located in the same subnet. However, in this case it is recommended to relocate the server to a separate subnet when pending changes in the network structure.
* Depending on the intended use of the computer, it may also require access to certain services in the network (such as web, file, database, print, DNS or mail servers). This must already be taken into account in the planning, so that difficulties do not arise at a later date, for example due to insufficient transmission capacities or problems with interconnected security gateways.* In addition to the actual service for which a server is set up, other services are often needed to efficiently use and administer the server. For example, administration over the network requires secure access (for example, SSH), or the files for a web offering can be transferred to the web server over the network. If the resulting network communication takes place over insecure networks, appropriate secure protocols must be used. In addition, the services may only be made available to authorized users and computers. This can be realized by password assignment, by using a packet filter or other mechanisms. No service should be provided on an insecure network, such as the Internet, unless expressly provided for.
* In the planning phase, an overview of the envisaged and required network services and the necessary network connections should be compiled. In general, it is important to consider in the planning phase how large a system's dependence on the functioning of the network connection may be.
* Tunnel or VPN:
 If it is foreseeable already in the planning phase that the system must be accessed via insecure networks, suitable solutions should be investigated at an early stage. For example, the access can be made via a VPN.
* Monitoring:
 To monitor the availability and utilization of the system and the services offered, a monitoring system can be used. As a rule, a monitoring daemon is installed on another server, to which a locally installed agent sends the data to be monitored. It is also possible to monitor the activities of network services offered by external systems. In case of problems, for example, the IT operation can be automatically alerted.
* Logging:
 The logging of messages from the system and the services used plays an important role, for example in the diagnosis and correction of malfunctions or in the detection and resolution of attacks. In the planning phase it should be decided which information should be logged at least and how long the log data should be stored. In addition, it must be determined whether the log data should be stored locally on the system or on a central log server in the network. It is sensible to specify in the planning phase how and at what times data should be evaluated.
* High availability:
 If special requirements are placed on the availability of the system and its services, consideration should already be given in the planning phase as to how these requirements can be met.
All decisions made in the planning phase must be documented in such a way that they can be reconstructed at a later date. It should be noted that usually other persons besides the author must evaluate this information. Therefore, attention must be paid to appropriate structuring and comprehensibility.

#### SYS.1.1.M13 Obtaining servers

The procurement of a server affects both the hardware and the software from which the server is to be built. If mistakes are made in the procurement of a server, this can have serious consequences for the secure operation of a network, since with unsuitable hardware and software, the desired level of security may be difficult to achieve.

Before a server is procured, therefore, a list of requirements must be created, by means of which the products available on the market are evaluated. Based on the evaluation, a sound purchasing decision can then be made to ensure that the server meets the requirements in practical operation.Even purely functional features of servers can have an impact on information security. In most cases, the basic value availability is affected, for example if a server does not achieve the required response times or throughput rates due to insufficient memory. In addition, the support provided by the manufacturer plays a not insignificant role, for example, when it comes to providing promptly patch for security vulnerabilities.

From the perspective of information security are key requirements to server that

* Hardware and software are designed to meet server availability and data integrity requirements
* Administration via secure protocols is possible
* the user management allows to implement the organization-wide role concept accordingly, and
* that it may be possible to encrypt particularly sensitive data.
Here are some requirements that should be considered when sourcing servers:

* Basic functional requirements

 
+ Does the device support all required hardware interfaces?
+ Does the software support all required protocols and data formats?
+ Security
+ Does the system support secure protocols for administration?
+ If servers are not administered via their own administration network, administration must be possible using secure network protocols.


 
* Maintainability

 
+ Is the hardware and software sufficiently supported and maintained by the manufacturer?
The manufacturer should support the server as long as it should be used. This includes providing support and providing updates.
+ Does the manufacturer provide regular updates and quick security patches for the software?
It is particularly important that the manufacturer reacts promptly to known safety deficiencies.
+ Is the product offered the option of concluding maintenance contracts?
Often access to updates and support services from the manufacturer is only possible in conjunction with a valid maintenance contract.
+ Can maximum service response times be set in the service contracts?
A maintenance contract is only suitable if the guaranteed response times and recommissioning times can cover the specified requirements for the availability of the devices.
+ Does the manufacturer offer a technical support service (hotline) that can help in case of problems?
This item should be part of the completed maintenance contract. When concluding the contract, attention must be paid to the language of the manufacturer's hotline provided.


 
* Reliability / reliability

 
+ Is there reliable information about the reliability and reliability of hardware and software?
+ Does the manufacturer possibly offer high availability solutions?
+ If the availability requirements can not be covered by maintenance contracts, the system should support high availability solutions.


 
* User friendliness

 
+ Is the product easy to install, configure, administer and use?
+ Training for the product should also be offered.


 
* Costs

 
+ What are the initial costs for hardware and software?
+ What are the anticipated running costs (maintenance, operation, support)?
These costs must already be taken into account during the procurement phase. The contents of the maintenance and support contracts should be checked (reaction times, hotline, qualification of personnel, etc.).
+ What are the expected running costs for the staff?
+ Do you need to purchase additional software or hardware components?This question should be answered already in the planning phase. If, for example, a network management system is already in use, the compatibility with the devices to be procured should be checked.
In addition, the effort for integration into an existing infrastructure should be considered.
+ What are the costs of training administrators?
+ Which costs have to be expected if an upgrade of the hardware is necessary due to increased capacity requirements?
In this case, the costs can be considerably higher than the costs for the hardware itself, since in many license models of software providers, the license price depends on the number of processors or the processor clock, so that a hardware upgrade can also require a new program license at the same time.


 
* Logging

 
+ Which logging options are available?
The logging options offered must at least meet the requirements specified in the security policy. In particular, the following points are relevant:
+ Is the level of detail of the logging configurable?
+ Are all relevant data recorded by logging?
+ Does the system support central logging (eg syslog)?
+ Can logging be carried out in such a way that the provisions of data protection can be fulfilled?
+ Are alarm functions supported?


 
* Infrastructure

 
+ Dimensions and compatibility with protective cabinets
The space requirement of a server must also be taken into account during procurement. Can the device be installed in the provided protective cabinets (form factor, weight, fastening elements)?
+ Power supply and waste heat
The manufacturer should provide information on power consumption and ambient temperature requirements. Is the existing capacity of the power supply and the UPS sufficient? Is the existing cooling capacity sufficient to dissipate the heat from the device?


 
The requirements and the selection decisions made on their basis should be documented in such a way that it becomes comprehensible at a later time how the decision was made.

#### SYS.1.1.M14 Creation of a user and administration concept

Process, conditions and requirements for administrative tasks, as well as the task separation between the different roles of the users of the IT system should be codified in a user and administration concept. For this purpose, the users authorized on the IT system, created user groups and rights profiles should be documented. The following information on the assignment of rights to users and user groups should be specified:

Allowed users:

* assigned rights profile (if applicable deviations from the standard rights profile used)
* Justification for the choice of the rights profile (and any deviations, if any)
* Assignment of the user to an organizational unit, room and telephone number
* Date and reason of the facility
* Time limit of the institution
Approved groups:

* associated users
* Date and reason of the facility
* Time limit of the institution
More detailed information and specific requirements can be found in the module ORP.4 Identity and Authorization Management.

#### SYS.1.1.M15 Uninterruptible and stable power supply [Building Services]

A local uninterruptible power supply (UPS) has the task of protecting a single IT system or very few IT devices from the consequences of short-term power interruptions. This objective is usually given in smaller IT structures, which also do not have a network backup system.

For larger IT structures or even the supply of entire buildings mainly central UPS systems are used.Regardless of whether a local UPS is used as a cradle or as a 19-inch slot, its performance and support time are dictated by device properties and typically can not be changed.

With the local UPS devices available today and the low power levels that can usually be provided by them (in the range up to approximately 1 kVA), these power failures can be bridged without any problem for up to 120 minutes (support time). Which support time is actually required in the specific scenario depends on how long, on the one hand, the shutdown of the connected devices takes (shutdown) and how long, on the other hand, to wait for the power supply to restart (waiting time). Since a large part of all power outages only last a few minutes, a waiting time of 15 minutes is usually sufficient to bridge a supply interruption. If the supply interruption lasts longer than the waiting time, and the supplied IT system has to be shut down in order to avoid data loss, the total support time should follow the formula

Support time = waiting time plus twice the shutdown time

be dimensioned. The dual approach of the shutdown time provides a safety margin if the shutdown takes longer than expected. Every time you replace or supplement IT equipment that is powered by a UPS, you need to recheck if your existing backup time is sufficient.

Three types of UPS are to be distinguished:

* VFD UPS
 In the VFD UPS (VFD stands for Voltage and Frequency Dependent) the connected loads are fed directly from the power supply network during normal operation. Smaller disturbances in the supply network can thus reach directly to the connected consumers. Only when this fails, the VFD UPS automatically turns on and takes over the supply. It takes up to 10 ms (switching gap), which can be too much for some IT devices. The VFD UPS was formerly called offline UPS.
* VI-UPS (Voltage Independent)
 In this case, the supply voltage is readjusted for smaller fluctuations (VI stands for Voltage Independent), without the UPS as such completely taking over the supply of the connected consumers. However, the frequency at the output of a VI-UPS is directly dependent on the supply network, as with a VFD UPS. Even with the VI-UPS can occur when switching to battery operation to a switching gap.
* VFI UPS (Voltage and Frequency Independent)
 The VFI UPS (Voltage and Frequency Independent) normally does not have a direct connection between the UPS input and output. The electrical energy is rectified on the input side and fed into the DC link. From there, the batteries are kept in the optimum state of charge and the inverter is supplied. This generates the AC voltage required for the connected loads.
 Since the output energy is generated independently of the input permanently via the inverter, there is no switching gap here. The VFI UPS was formerly referred to as an online UPS.
Since the VFI UPS is the only one of the three systems that really works uninterrupted, it should always be given preference. Taking into account further quality features not discussed here, a UPS classified according to DIN IEC 62040-3 in accordance with VFI-SS-111 represents the optimum for IT supply.Contrary to an assumption made again and again, a UPS of any type does not provide overvoltage protection in the strict sense. A UPS is able, in the context of its normal function, to keep too high voltages away from the connected consumers. However, a UPS does not help against overvoltages such as those that are intercepted by the overvoltage protection equipment. On the contrary, a UPS, like all other electrical consumers, must be protected against overvoltages by suitable protective measures (see section "Overvoltage protection").

To avoid potential problems with protective earth currents, IT equipment that is powered by a local UPS should not be connected through shielded wires (such as printer cables) to other IT equipment that is powered by another path.

Since the batteries of a local UPS are rarely operated in their optimum temperature range (typically around 20 ° C), the battery life of local UPS devices is quite low, in the best case up to 5 years, usually less. During this period of operation, the batteries permanently lose power so that a local UPS can provide at most half of the support time when new after perhaps two or three years. To ensure that the UPS provides the necessary support time, the actual time of support should be calculated once a year. Some UPS systems have built-in testing mechanisms. If this is not the case, the value can be determined by a load test.

As with all other electrical equipment, care must be taken in UPS systems to operate within the temperature ranges specified by the manufacturer. This must be taken into account when dimensioning the cooling.

Since the UPS is the last bastion against the power failure in front of the IT hardware, it is very important for ensuring availability. So it has the same protection needs as the IT supplied by the UPS. If the UPS-supplied IT systems are redundant, UPS systems should also be redundant.

In addition, in a UPS is to pay particular attention to the protection against the access of unauthorized persons, fire and water. A meaningful protection against fire makes it almost indispensable to accommodate redundant UPS units in separate fire compartments. This is the only way to prevent a fire from burning out after a short period of time.

To maintain the protection of a UPS, it must be maintained regularly. For this, the maintenance intervals of the UPS provided by the manufacturer must be observed.

**Overvoltage protection**

In any electrically conductive network, whether it is the power supply or the data transmission, it can come at any time to overvoltages. Predominantly such overvoltages are caused by other current consumers in the same supply network. Lightning overvoltages, on the other hand, are much rarer, but have much greater potential for damage.

Overvoltages can enter into a building and the IT operated there, not just via the lines laid in the building, but also via all electrically conductive external connections such as telephone, water or gas lines. In addition, overvoltages can also be coupled to internal lines.

The necessary measures to protect IT equipment are essentially the same regardless of the cause of the overvoltage. The series of standards for lightning protection of structures DIN EN 62305 "Lightning protection" (corresponds to the standards series VDE 0185-305 and IEC 62305) describes an overall concept for lightning protection. On the basis of this series of standards DIN EN 62305 a surge protection concept is to be created.In its Part 2 "Risk Management", DIN EN 62305 generally describes the way to a risk-oriented lightning and surge protection. Part 3 deals with the "Protection of Structures and Persons", in Part 4 "Electrical and Electronic Systems in Buildings".

In the overvoltage protection concept, of course, stand-alone power supply systems (NEA) and uninterruptible power supplies (UPSs) must be taken into account. Although UPSs provide some protection to the connected equipment, they are in no way to be considered a surge protector, but solely as an electronic device to be protected.

The former three levels of coarse, medium and fine protection have been replaced by the concept of energetic coordination. According to the standard, energetic coordination is only mandatory if there is external lightning protection. In terms of information security, the energetic coordination should also be considered in cases without external lightning protection. Simplified, this means the following:

* Behind each protection element (SPD - Surge Protecting Device), the maximum amount of energy caused by overvoltage must be the same as that of all the electrical devices behind it (including the following SPDs). A pure network is of course much more robust and tolerates significantly more energy than z. B. the interface of a network card in a computer.
* All used SPDs must be compatible. The output of a front SPD and the input of the following must be matched. Evidence of energetic coordination can be provided in three ways:
The construction of the lightning and overvoltage protection means that lightning protection zones (LPZ, LPZ, Lightning Protection Zone) are formed like onion shells. With increasing protection they are called from outside to inside with LPZ 0, LPZ 1, LPZ 2 etc. In this case, a zone can only be formed if there is the next outer one: Thus, it is not possible to realize an LPZ 2 without having the LPZ 1 as well.

For simple electrical and electromechanical devices, the LPZ 1 is usually sufficient. To protect electronic devices (IT hardware, UPS, etc.), at least the LPZ 2 must be implemented. For particularly sensitive devices, such. B. in medical or instrumentation can quite the LPZ 3 may be required.

**Note:**

The LPZ (lightning protection zones) should not be confused with the protection classes of the external lightning protection system, which is called LPS (Lightning Protection System).

Whether an LPS is required and with which protection class must be decided on the basis of the risk assessment (in accordance with Part 2 of DIN EN 62305). The earlier sufficient view into a building list is no longer enough!

In many cases, it is not necessary to build a LPZ 2 or LPZ 3 building-wide. While the transition from LPZ 0 (which is anything outside of a building, where lightning can actually strike directly) to LPZ 1 actually has to be as close to the building envelope as possible, the construction of higher LPZ can be done anywhere and to any extent , However, it is important to ensure that no line that only enjoys the protection of the LPZ 1 (eg heating pipes) passes through higher-quality LPZ.

The previously required minimum line lengths between the SPDs, ie the protective elements, and the different LPZs are no longer compulsory today. There are SPDs that realize the transition from the LPZ 0 directly into the LPZ 2 in one component.

The protective effect of an SPD extends on both sides (to the incoming and outgoing line) only over a specific cable route, which must be named in detail by the manufacturer. If the cable length is exceeded, repeatedly install SPDs to maintain protection.According to DIN EN 62305, lightning protection systems (LPS) must be checked at intervals of one to four years, depending on the protection class. For surge protective devices, the standard does not provide for explicit test intervals. For the purposes of information security, however, all SPDs should be reviewed periodically (at least once a year) and after known events and replaced if necessary. To be able to carry out this test at all, only those SPDs should be installed, if available, which have a built-in defect indicator or (even better) a life indicator.

In addition to overvoltage protection on all electrically conductive systems, measures against electrostatic charge must be taken in server rooms and the core units of a data center. The volume resistance of floor coverings in such rooms must be between 10 and 100 megohms. The classification according to DIN regulation 4102-1 "Fire behavior of building materials and components" must reach at least "B1 flame retardant". This also applies to a raised floor or installation floor.

Regardless of the scope and expansion of the overvoltage protection, it must be ensured that a comprehensive equipotential bonding of all electrical equipment included in the overvoltage protection is required! The majority of damage to IT equipment due to overvoltages can be attributed to incorrectly implemented equipotential bonding.

#### SYS.1.1.M16 Secure installation and basic configuration of servers

After completing the planning of a new server and creating a security policy, you can start installing the server.

The installation of the system should only be performed by authorized persons (administrators or contracted service providers). Administrators of IT systems and their representatives must be carefully selected. You must be regularly informed that the powers may be used only for the required administrative tasks. Since administrators play a key role in the functionality of the hardware and software used, the continuation of activities must be guaranteed even if administrators fail. For this, the named representatives must have the current state of the system configuration and have access to the passwords, keys and security tokens required for the administration. More detailed information can be found in ORP.4 Identity and Permission Management.

It is recommended to first create a short installation concept according to the functional requirements of the planning and the specifications of the security guideline. In principle, it is advantageous to carry out the installation in two phases: First, a basic system is installed and configured, then the other required services and applications are set up. The installation programs of most operating systems support this procedure more or less well.

The described steps do not necessarily need to be performed again for each server. This could even be counterproductive in that constant repetition increases the risk of error. It is therefore recommended to carry out the described steps with great care on a reference system, to document the necessary configurations precisely and thus to obtain a customized installation concept for the respective operating system. It must be noted that this installation concept must also be checked and, if necessary, adapted for changes to the operating system that do not represent a completely new release (service packs, update releases or the like).In the rare case of virtual servers, a modified operating system is installed for each instance; in this case, a basic system is usually created that is copied into the instance and started as a stand-alone clone. In this instance, the next step is to install the required server services or application programs, and at any later time, a new clone can be generated, for example, to obtain multiple instances of identical server services or application programs. This can also inherit wrong decisions and wrong settings that were made during the creation of the basic system when installing the clones on numerous other instances. For each clone, therefore, all the recommendations of this measure should also be carefully implemented.

**Installation**

This action only includes recommendations for the first steps of an installation and not for the final configuration for the intended use. The further configuration steps are very dependent on the respective system and field of application and are treated in own measures in the operating system modules.

During installation and later configuration, at least the important steps should be documented so that they can be understood at a later time. For example, a checklist can be created for the installation, where the steps taken can be ticked off and any settings made can be noted. A corresponding documentation is helpful for an error analysis or later reinstallation. It should be noted that, in addition to the author, other administrators, who may be less specialized in this field, have to resort to the documentation. Therefore, it is important that the documentation is well structured and understandable.

If the server is being installed from data carriers such as DVDs or other storage media, it is recommended that the installation and basic configuration be carried out offline or at least in a secure network (installation or administration network). In general, it should be prevented that other IT systems can access the IT system to be installed during installation. This is important because during the installation usually no passwords are assigned and no protection mechanisms are active, but possibly already accesses are possible. If the installation of several IT systems is partly to take place over the network (for example, reloading of packages), it is recommended to use an installation server in the administration network.

Especially with the operating system itself, it is important that the installed version comes from a trustworthy source. This is especially important when, for example, CD images have been downloaded from the Internet. In this case, it is important to check for digital signatures of the packages that can be used to verify the integrity and authenticity of the packages. Packages and CD images for which there are no digital signatures or at least checksums should, if possible, not be used.

When setting up disk partitions, the concept created in the design phase must be implemented. If an encrypted file system is to be used, it usually has to be initialized before data can be copied into it, because often a file system can not be encrypted in retrospect. Also, some RAID systems and levels require a configuration that must be completed before the file systems can be set up.

If this has not already been done automatically, logging of the system events should be activated at the latest when completing the basic installation. The log data can provide valuable information in case of problems during further installation and configuration.**Update**

If the system is being installed from a CD, DVD or other "offline medium", after the basic installation it should be checked whether in the meantime updates or security patches have been published by the manufacturer or distributor.

** Installation of the respective server services and application programs **

After the operating system has been installed and the basic configuration and update completed, the respective server services can be installed and configured. Both clients and servers typically require server services for remote administration. For servers, the actual server services are added; for clients, typically graphical user interfaces and application programs must be installed and set up. For this purpose, an analogous procedure is recommended as for the operating system itself. It is also recommended to harden the operating system.

#### SYS.1.1.M17 deployment clearance

Before the server system is used in productive operation and before it is connected to a productive network, an application release should be carried out and documented. The deployment clearance is based on a test of the installation and configuration documentation and the functionality of the system in a test. It is carried out by a body authorized to do so in the institution.

More detailed information can be found in OPS.1.1.7 Software Testing and Approvals.

If there is an increased need for protection, consideration should be given to performing an internal penetration test (see DER.3.3 Penetration test).

If it is determined that a security update or patch is incompatible with another major component or program or is causing problems, it is important to consider how to proceed. If it is decided that a patch will not be installed due to the problems that have arisen, this decision must be documented in any case. In addition, it must be clear in this case which measures have been taken to prevent exploitation of the vulnerability. Such a decision must not be made by the administrators alone, but must be agreed with the supervisor and the ISB.

#### SYS.1.1.M18 Encryption of communication links

If possible, network communication should be encrypted to or from a server. The encryption depends on the service provided by the server, for more detailed information on the respective network services can be found in APP.3 Network-based services. One of the most common ways to encrypt network services is to use TLS.

Transport Layer Security (TLS) is a further development of Secure Sockets Layer (SSL) and is used to cryptographically secure information during transmission in networks, usually between server services and clients or between server services. Clients can only use encryption over SSL / TLS if it is supported by the server services. SSL / TLS can be used to encrypt information from the application layer (such as HTTP, LDAP, POP3, IMAP, and SMTP) over TCP / IP. In addition, secure VPNs (Virtual Private Networks) can be established using SSL / TLS. With OpenVPN, a software freely available under the GNU GPL (General Public License), VPNs can be realized using SSL / TLS encrypted connections. More detailed information about VPNs can be found in the module NET.3.3 Virtual Private Networks (VPN).Typically, many server services require only a small amount of overhead to configure them to support SSL / TLS encryption or to use them exclusively for information exchange. Therefore, it must be checked for all server services whether encryption with SSL / TLS is feasible and practicable with reasonable effort. If this is possible with reasonable effort, the SSL / TLS encryption should be activated. Generally, the internal and external message stream should be encrypted to and from LDAP, email, and web servers using SSL / TLS.

** Choosing a trusted certification authority **

At the beginning of a new SSL / TLS secure communication setup, a so-called handshake takes place between client and server. Here, the client and server communicate via the cryptographic algorithms used for key exchange, encryption and integrity assurance. In addition, client and server agree on the SSL version being used. In addition, the server sends its X.509 certificate to the client. Optionally, the server can also be configured to prompt the client to submit its X.509 certificate to the server.

The identity of the communication partners is checked via these certificates. X.509 certificates contain the public keys as well as a confirmation from another instance, the certification authority or trust center or certificate authority (CA), about the correct assignment of the public key to its "owner". The value of a certificate depends on which fields of the X.509 certificate are checked by the certification authority before the certificate is issued, and how trustworthy the certification authority itself is. Therefore, the selection of a trusted certification authority plays an important role.

Due to the large number of certification bodies in the market, an institution should carefully select the certification authority. It is advisable to specify in advance the essential selection criteria for later operation. These may include, for example:

* whether the root certificate is already in CA lists of clients, such as the browser,
* where the seat and legal status of the certification body are located, and also where the technical office is located,
* What is the business orientation of the certification authority (Is CA operation a central business field?), which includes the CA services offered (eg OSCP, CRL),
* which security level the certification body can demonstrate
* how good the scope and quality of technical support are, and
* how high the certificate costs are.
In principle, however, the cost of a certificate should by no means be the only decisive criterion. If the offered server service is used by a limited number of users, e.g. B. only within a LAN s, a certificate can be created and signed even without the involvement of a certification authority itself and recorded on all clients on which the server service is to be used.

** Extended Validation Certificates **In order to make it harder to attack with fake websites and to counteract the problem that various certification authorities do not always reliably check SSL / TLS applications, Extended Validation Certificates have been introduced to handle certificates with higher security requirements. These are to prevent that when a certificate is issued, a CA checks only the domain name. In addition, the CA should also clearly understand by whom the domain in question was registered. Unlike the standard X.509 SSL / TLS certificates, these extended certificates (Extended Validation SSL Certificates, EV-SSL) will further verify the identity of the claimant. In doing so, the involved certification authorities and browser manufacturers undertake to adhere to the "Guidelines for the Issuance and Management of Extended Validation Certificates" of the CA / Browser Forum. According to this, the following criteria must be fulfilled by the applicant, among others:

* Proof of identity and address of the applicant,
* Proof that the applicant is the sole owner of the domain,
* Confirmation that the applicant is at all entitled to make the application and
* Mention of a main contact person.
In addition, the applicant or the applicant may not be on a list of prohibited organizations or persons. In addition, the country in which the applicant's registered office or legal status is located may not be subject to trade embargoes or any other sanctions imposed by the country whose legislation is subject to the certification body.

For users, EV-SSL certificates can be recognized by the fact that certain areas in the supported browsers, such as the URL in the address field or the padlock symbol used by many browsers, which identifies an encrypted page, have a green background. However, depending on the configuration of the security gateway (firewall) behind which users access web pages with EV SSL certificates, these markers may not be displayed in the clients' browsers. If, for example, the message flow between the client and the web server is encrypted by a proxy and then re-encrypted, only the SSL / TLS certificate of the security gateway is displayed in the browser.

In addition to the higher financial costs associated with issuing an EV-SSL certificate, it usually takes longer to complete an application, as additional information is reviewed by the certification authority. If possible, it is recommended to put up with this extra effort. Especially in areas where information with higher protection requirements regarding confidentiality and integrity is transferred, EV-SSL certificates should be preferred.

** Common Name Entry **

Browsers always display a security warning if the common name entered in the certificate of a web page does not match the fully qualified domain name (DNS) that the server can access on the web. Therefore, it should be ensured that the common name matches the URL that is actually used to communicate with the server. If possible, wildcard certificates (such as * .example.de) should be avoided. These are often used to secure multiple subdomains with a single certificate.

** Full certificate chain **

Since all intermediate certificates are required for the check of the hierarchical certificate chain by the browser, the SSL certificate of the server alone is not sufficient. Therefore, the server should be configured to send all required certificates to the client when connecting. For this, the certificate chain should be stored accordingly in the web server.It should also be noted that in addition to certificates that are missing, expired or revoked certificates also fail to validate the certificate chain. Only if all certificates are valid and have been transferred when the connection is established can the certificate chain be checked successfully.

** Selection of a SSL / TLS protocol version **

There are currently five SSL / TLS protocol versions: SSL v2, SSL v3, TLS v1.0, TLS v1.1, and TLS v1.2. SSL v1 was not published. To ensure a secure connection between client and server, TLS 1.2 should be used. TLS 1.1 provides sufficient security, but compared to TLS 1.2 it has some weaknesses, such as: For example, in TLS 1.1, cipher suites based on IDEA and DES are no longer available in TLS 1.2. TLS 1.0 can be transitionally deployed in existing applications if immediate migration to TLS 1.1 or, preferably, TLS 1.2 is not possible and appropriate action is taken against Chosen Plaintext attacks (eg, BEAST) on the CBC implementation. In general, however, a migration to TLS 1.2 should be carried out as quickly as possible. SSL v2 and SSL v3 may not be used anymore. See also the BSI migration guide for the minimum standard TLS 1.2.

** Secure Cipher Suites **

SSL / TLS uses cipher suites that determine how secure an HTTPS connection is. Each suite consists of specific modules. If a particular module is considered unsafe or weak, changing the cipher suite will allow you to switch to a more secure module.

Since the use of weak cipher suites can be enforced on the client side, it is necessary to only offer server-side servers that use sufficient strength for authentication and encryption. In addition, the cipher suites used should support Perfect Forward Secrecy (PFS). Further notes on cryptographic algorithms and key lengths are contained in the Technical Guideline of the BSI "Cryptographic Methods: Recommendations and Key Lengths - Part 2 Use of TLS" (TR-02102-2) and in CON.1 Crypto Concept.

** Session Renegotiation / TLS Compression **

Using session renegotiation, both client and server can renegotiate the parameters of an existing HTTPS session. Due to an error in the specification of the TLS protocol (RFC 5246), a man-in-the-middle attacker may be able to misuse the session renegotiation to insert any content into an existing HTTPS session. Meanwhile, the TLS protocol has been extended (RFC 5746) and this design bug has been fixed. In general, it should be considered whether server-side session renegotiation is required. If this is the case, then it should be configured securely, based on RFC 5746. Renegotiation initiated by the client should be denied by the server.

In addition, the TLS compression should be disabled.

** Web server specific aspects **

In general, it is recommended to protect the content provided on web servers during the transfer from the server to the client and vice versa using SSL / TLS.

If possible, avoid offering mixed content websites. A mixed content web page is a page that uses encryption, but also includes unencrypted content (such as JavaScript, CSS, or images). A man-in-the-middle attacker can exploit the transmission of a single unencrypted file to take over an HTTPS session. In addition, because mixed content web pages typically generate browser alerts, it will degrade usability.HTTP Strict Transport Security (HSTS) is another method that protects against known weaknesses of SSL. This makes it difficult for a visitor to be redirected from a secure to an unsecured page due to an attack or server-side configuration issues. For example, if an attacker is in the same WLAN as the victim, he or she could read the session cookies and take over the HTTPS session. To enable HSTS, the HSTS header must be configured on the server.

** Protection of the private server key **

A particularly important security aspect when using SSL / TLS is the protection of the private server key. Therefore, it is advisable to configure the server so that the private server key must be unlocked when the server starts up. If it is suspected that the private key has been compromised, the underlying certificate must be revoked.

** validation **

The impact of configuration changes on the server is not always predictable. Even software updates can sometimes lead to surprising changes. It is therefore recommended that the SSL / TLS configuration be checked for errors before being released for use and periodically (periodically) validated.

#### SYS.1.1.M19 Set up local packet filter

The entire network of an institution should be protected by an appropriate security gateway. Servers offering services to the outside should be deployed in a Demilitarized Zone (DMZ). Nevertheless, it is recommended to set up appropriate access restrictions at application or network level on every computer. This also applies to servers that are only used internally and not least for clients.

A local packet filter can protect a machine against attacks launched from the same subnet. In addition, such a packet filter can be used to realize a finer graded access control for individual services, as is possible, for example, with packet filters only at gateways.

In addition, a local packet filter can also be used to restrict outgoing network connections and thus limit the consequences of compromising the system. Although such protection may be disabled by an attacker after a successful compromise of the computer, on the other hand, an attacker is at least hindered in this way. In this way, crucial time can be gained in the discovery and possible reactions.

Lastly, the log function of a local packet filter can allow certain attacks to be detected at all.

Virtually all current operating systems provide the ability to define filters that examine and handle all packets received or to be sent according to specific rules. The filter options differ considerably between the individual operating systems. Practically, however, rules can be defined based on the source and destination address of the packet as well as the type of protocol used (TCP / IP, UDP / IP, ICMP, etc.) and, if applicable, the source or destination port. With the help of packet filter rules, for example, packets originating from specific computers or from specific subnets can be deliberately discarded.

Some server applications have their own mechanisms to allow or deny access to the service for individual IP addresses or ranges of addresses. In contrast to these mechanisms, a local packet filter at the operating system level has the advantage of protecting the service itself against possible attacks leading to compromise before the built-in access restriction can even take effect.

In principle, all servers with high protection requirements should be protected with a local packet filter.There are two general strategies that can be used to implement packet filtering rules: The blacklist strategy allows all kinds of connections that do not meet certain exclusion criteria (Floating strategy: "Everything is allowed, which is not explicitly forbidden"). The advantage lies in a possibly lower effort in administration and troubleshooting. A serious drawback, however, is that forgotten rules that allow access to non-secure network services can serve as the basis for an attack.

In contrast, the whitelist strategy blocks all types of connections that do not belong to a list of allowed services (Restrictive strategy: "Everything is forbidden, which is not explicitly allowed").

The whitelist strategy offers greater security and should therefore be used in principle unless there are important reasons against it. The disadvantage lies in the fact that administration costs tend to be higher because new rules have to be defined each time the requirements change. In exceptional cases, for example if a protocol does not work on firmly defined ports, the blacklist strategy can be used.

It is recommended to set up a local packet filter with a basic set of rules on all servers as part of the basic configuration, in which all connection requests are rejected from the outside. This policy should be active when the system is connected to the mains. Depending on which services are to be offered by the system, after their configuration, the required protocols and ports can be unlocked. For clients, too, this approach should at least be taken into account if they make special demands on security.

Packet filters usually allow detailed logging of network traffic. Setting up a local packet filter is therefore also useful in secure networks that are separated with a security gateway from an insecure network such as the Internet, because information gained can be helpful in detecting attacks. However, care must be taken to ensure that no privacy policy is violated. Where appropriate, the relevant bodies (data protection officers, staff representatives or others) should be involved.

** Problem ICMP **

The Internet Control Message Protocol (ICMP) is used to transmit messages about errors in the transmission of IP packets. For example, there are messages that tell the sender of a packet that the destination network is unreachable or that the packet was too large to be forwarded to the destination system. The function of the tools ping and traceroute are also based on ICMP.

However, in addition to many useful features, there are some ICMP message types that allow attackers to gain important information about a network and use it directly for attacks. Unfortunately, the radical approach to blocking ICMP on the security gateway is also not a satisfactory solution, as certain features are no longer available. Although ping and traceroute can typically do away with normal workstations and servers, global blocking of ICMP can lead to impairments that are difficult to diagnose. Therefore, consideration should be given to both the security gateway and the local packet filter for selective ICMP filtering, provided it provides the appropriate capabilities. This should always be done taking into account the purpose of the computer (server or workstation), its protection needs and the measures taken at the security gateway. For example, a larger number of message types may be allowed for the internal network than for the external network.

** implementation and review **The possibilities of filtering and logging differ depending on the operating system. Before setting up a local packet filter, refer to the existing documentation.

Care should be taken when setting up packet filter rules, as an error in a rule may result in an administrator working on the network on the computer "locking out" and making corrections from the system console must make out.

After activating the local packet filter, on the one hand, it should be checked whether the required services are still reachable, on the other hand, a port scan should be used to check whether the remaining ports are all blocked.

#### SYS.1.1.M20 Restriction of access via networks

The use of a security gateway and appropriate network segmentation reduce the attack surface of a server. However, these recommendations can not be implemented directly on a server, but have to be considered during network planning. In-depth information can be found in the NET1.1 network architecture and design.

#### SYS.1.1.M21 Operation documentation

To ensure a smooth operation, administrators need to have an overview of the system. This must also be possible for their representatives if an administrator fails unexpectedly. The overview is also required to be able to carry out system checks (eg on problematic settings, consistency in case of changes).

Therefore, the changes that administrators make to the system should be documented, automated if possible. This applies in particular to changes to system directories and files.

When installing new operating systems or updating, the changes made must be documented with particular care. By activating new or changing existing system parameters, the behavior of an IT system (in particular also safety functions) can be significantly changed.

#### SYS.1.1.M22 Integration into emergency planning

The partial or complete failure of a server can have serious consequences if the server is an integral part of in-house workflows or supports a publicly available offer (such as in e-commerce or e-government applications).

In the context of emergency preparedness, therefore, a concept should be drafted on how the consequences of a failure can be minimized and what activities should be carried out in the event of a failure.

The following aspects have to be considered:

* The emergency planning for the server must be integrated into the existing emergency plan (see also module DER.4 Emergency Management).
* A system failure can also lead to data loss. Therefore, as part of the general data protection concept (see also OPS.1.1.5 Data Backup), a data protection concept for the server must be created. Not only the server itself needs to be considered, but also the systems on which the operation of the server depends or for which the operation of the server is necessary.
* Within the scope of maintenance and service contracts or own warehousing, the supply of spare parts must be ensured within a period of time. Downtime is therefore reduced to a manageable level. For special server availability requirements, a high availability solution may need to be deployed.* The system configuration must be documented. Important tasks must be described so that the entire system can be restored in an emergency even without prior knowledge of this system configuration. The documentation should by no means only be available electronically, but instructions should also exist in paper form. If necessary, configuration files can also be appropriately stored on external data carriers.
* A recovery plan must be created to ensure the controlled startup of the system. For this purpose, a boot medium should be created in advance, see section "Boot medium".
* All necessary procedure descriptions must be regularly checked and rehearsed. You may need to consider varying approaches for different operating systems.
** boot media **

When setting up a computer, a boot medium should be created that can be used to start the system if a hard drive fails or to create a controlled system state if a malicious program occurs. Such media may be, for example, CDs whose creation the respective operating system may offer, but it is also possible to create specially furnished CDs or portable drives (for example USB sticks or external hard disks with USB or Firewire interface). In addition to "physical" media and image files can be used, which are copied or burned on the boot medium only when needed. The nature and extent of the emergency boot medium depends on the purpose of the computer and the existing interfaces.

The emergency boot medium can be used for problems such as:

* Data loss due to operating errors,
* Operating and administration errors that prevent use and reboot
Infection of the system with malicious programs (such as computer viruses)
Compromise of the system by an attacker, or else
* Hardware problems.
Ideally, the rescue boot media should contain all the programs and data needed to investigate and, if possible, resolve the issues. If necessary, different media can be created for different problem scenarios.

The following programs are recommended as the "basic configuration" for an emergency boot medium:

* Virus protection programs with up-to-date signatures, or the ability to update current signatures,
* Programs for editing configuration files or databases of the system (editors for files, registry or similar),
* Program to restore the boot sector and the MBR (Master Boot Record) of the system disk,
* Backup / recovery programs,
* Diagnostic programs to analyze hardware defects.
In addition, programs can be added for further analysis, such as forensic investigation of a compromised system.

It is important that all programs and libraries are loaded exclusively from the boot medium. No components of the installed system may be used. When creating the boot medium, it is also important to ensure that in addition to the necessary programs, all the drivers required for access to the built-in disks of the computer are also available. These include, for example, drivers for hard disk controllers (especially RAID controllers) and drivers for hard disk encryption or hard disk compression.

As a rule, other programs or documentation can also be stored on the medium. For example, it can increase the efficiency of debugging if the boot media always contains up-to-date documentation of the system configuration.The emergency boot medium itself must be free from viruses and other malicious programs. Therefore, only programs that originate from trustworthy sources (eg directly from the manufacturer) or whose digital signature has been checked may be used. At least once after the creation and every change, the boot medium should also be checked with a virus protection program.

It is not absolutely necessary to create a separate boot medium for each system. A correspondingly flexible boot medium can be sufficient for a large number of different systems. Not even the same operating system needs to be deployed on the boot medium as on the target system itself. However, for compatibility reasons, this is often beneficial. However, it must be ensured by appropriate tests that the medium really works on all computers for which it is to be used. Depending on the operating system, system-specific aspects must also be considered, which are described in the respective IT-Grundschutz modules.

After changes to the target system, such as an update of the operating system or configuration changes, if necessary, the emergency boot medium and the documentation stored on it must be updated. Changes to the boot medium must be documented.

The emergency boot medium must be quickly accessible to system administrators so that valuable time is not lost in the event of a malfunction. On the other hand, it must also be kept safe so that unauthorized persons have no access to it.

The emergency boot media function should be tested regularly and the operation of the programs stored on it should be checked to ensure that the media is functioning in the event of problems and the administrators are familiar with the operation. It should be considered to keep a short printed manual with the medium, which summarizes the most important steps for typical application scenarios.

#### SYS.1.1.M23 system monitoring

In order to be able to react to critical system events, a suitable system monitoring or monitoring concept should be created for servers. This includes the continuous monitoring of the system status and functionality of the servers and the services operated on them. If errors occur or defined limit values ​​are exceeded or undershot, this should be reported automatically to the operating personnel.

For this purpose, status information is usually retrieved from a central IT system on which the events are evaluated. However, the interface needed to retrieve the system events from the IT system can often change system settings of the operating system, e.g. Via SNMP (Simple Network Management Protocol). If such a modification is not desired, then these features should be disabled.

#### SYS.1.1.M24 security checks

It should be done regularly, at least monthly, a security check of the server. For virtually all operating systems, programs are available or already included with the operating system or operating system distribution that provide the functionality.

In such a security check, for example, the following points should be checked:

* Are there any users without a password?
* Are there users who have not used the servers for a long time?
* Are there users whose passwords do not meet the required conditions?
* Which users have administrator rights?
* Are system programs and system configuration unchanged and consistent?
* Match the permissions of

 
+ System programs and system configuration
+ Application programs and data
+ User directories and data
+ the requirements of the security policy?* Which network services run on the individual systems? Are they configured according to the security policy?
In a regular security check, penetration tests can also be integrated in the local subnet. In doing so, the "degree" of the penetration tests can be varied (for example: weekly simple automated checks, monthly more thorough test with partial manual execution, once a year a basic test of the entire network).

When carrying out the security check, the administrators should document their steps in such a way that they can be followed (for example, in the case of a suspected compromised system). The results of the safety check must be documented, deviations from the "target state" must be investigated.

#### SYS.1.1.M25 Regulated decommissioning of a server

If a server is taken out of service, this must not happen unprepared and without notice to the users, but a number of measures must be taken to ensure that

* no important data is lost,
* no services or systems that depend on the server are affected and that
* no sensitive data remains on the data carriers of the server.
In particular, it is important to have an overview of what data is stored on the system, where it is accessed, and where it is accessed. Based on this information, a plan should be made for decommissioning the server. The following points should be considered:

* Data backup
 Before decommissioning the server, data that is still needed must either be externally backed up or archived (for example, on magnetic tape, CD or DVD-ROMs) or transferred to a replacement system. After the backup, it should be checked that all data has been backed up correctly. Further information on this topic can be found in the blocks OPS.1.1.5 Data backup and OPS.1.2.2 Archiving.
* Replacement system
 If the services provided by the server continue to be needed, an adequate backup system must be provided in a timely manner. Appropriate resources must be available for the corresponding planning, procurement and commissioning, see also section "Migration of a server".
* Information of users
 If the system is shut down without replacement, users must be informed in good time of the imminent shutdown and, if necessary, have the opportunity to save their own data.
* Remove references to the system
 When decommissioning a system, references to the system must also be deleted. This includes, for example, deleting the DNS entry and the entries in other directory services as well as other references depending on the purpose. For example, if a web server is taken out of service, then references to this server, which are still contained in their own websites should be deleted.
* Deleting the data on the system to be shut down
 It must be ensured that no more valuable information is available on the data media. It is not enough just to reformat the disks, but they have to be completely overwritten at least once. It should be noted that neither deleting the operating system erasure nor reformatting the disks actually removes the data from the volumes. With suitable software, data can be reconstructed in such cases, often without much effort.
* Delete backup media
 After decommissioning a system, the corresponding backup media may need to be deleted or rendered unusable if the data stored on it is no longer needed.
* Remove any other informationOften, server systems contain other data (such as configuration data) stored in nonvolatile memory or are labeled externally (for example, with the computer name, IP address, and other technical information). If possible, this information should be removed prior to transferring the device, as an attacker may be able to extract information from such information for possible attacks.
It is recommended to use the recommendations given above to create a checklist that can be used when decommissioning a system. In this way it can be avoided that individual steps are forgotten.

** Migration of a server **

If the services of the server are to be taken over by another system, the transition must be planned. In particular, if special requirements for the availability of the services exist, a particularly careful planning is required.

In most cases it is recommended to perform the "function transition" to the replacement system outside normal operating hours. If this is not possible, measures must be taken to ensure that data is not lost during the functional transition, and that there are still unsustainable downtimes.

Therefore, an appropriate migration concept must be created in advance for the migration of important servers. In particular, the following points should be taken into account:

* Data migration and configuration
 After transferring the data to the new system, check that the data has been completely and correctly transferred.
 If a new version of the server software is to be used on the new system, it must be ensured that the new version can handle the existing data correctly. This not only concerns the task of correctly importing data from the old version, but also, in particular, modifying this data or adding new data records. Especially in such cases, problems often arise, so that thorough tests are recommended. It is also important that the configuration of the old service on the new system can be correctly taken over or at least "functionally equivalent reconstructed".
* Compatibility of the service
 It must be ensured that the service on the replacement system is compatible with the original service. This is particularly important if a new version of the server program is to be used on the new system as part of the migration, but this will continue to be accessed with old version clients. Even if a manufacturer provides reference customer reports of successful migrations, or assures "backward compatibility", "full backward compatibility with previous versions," or the like, it is strongly recommended that you perform the appropriate tests in advance.
* Cryptographic keys
 If parts of the data or file systems of a server are encrypted, then the backup or transmission of the corresponding cryptographic keys is of particular importance: Often these are stored in a different location on the system than the user data itself. For example, if the data using system-specific programs are copied directly in blocks or the hard disks are converted from the old into the new system, it must be ensured that the cryptographic keys are also transmitted, otherwise access to the encrypted data is no longer possible.
* Change of names and addressesIf a server is only accessed via its IP address or a DNS name, then a migration is usually relatively unproblematic, because in this case simply the replacement system can take over the IP address of the old system. It becomes more problematic, for example, if the new system is to receive the same DNS name but can not accept the IP address. Because it takes some time until the change of the address has "arrived" at all clients. Such latencies must be taken into account when planning the migration.
 If the system is otherwise accessed (for example, if the address is resolved by another directory service), then it must be kept in mind that the change in that way may also have some latency before it takes effect.
 The biggest problem arises when clients access the servers through an application that stores the IP address or name of the server in a local configuration file or database. If a larger number of clients have to be manually reconfigured, this can take a considerable amount of time and must be planned in advance.
* Permanent connections
 If there are clients who build longer existing or even permanent network connections to the service that has to be migrated to a new computer (this is the case with some database applications, for example), this must be taken into account during the migration. If necessary, these connections must be terminated manually on the relevant clients. This also requires appropriate planning.
For the implementation of the migration, it is advisable to create a checklist as part of the development of the migration concept, which can be followed through step by step during the migration. When planning the migration and creating the checklist, care must be taken that each step depends only on the previous steps.

In the case of high service availability requirements, the entire transition should be pre-tested in a test environment under the most realistic conditions possible in order to identify and eliminate potential problems at an early stage.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### SYS.1.1.M26 Multi-factor authentication (C)

There are different methods of authentication that can be based on the following factors: knowledge, ownership, and biometric features. For higher protection needs, multi-factor authentication is recommended using two of the three factors.

The most common is the use of the factors knowledge and possession. The authentication key is in this case in a hardware, for. B. chip card, stored (factor ownership), which can be used only after entering a PIN or password (factor knowledge). Depending on the security requirements, keys can also be stored on clients (eg notebook) or servers in the network of the institution.

Alternatively, the use of a Public Key Infrastructure (PKI) based on digital signatures and asymmetric cryptography techniques can be recommended. The validity of the signatures is checked by a recognized certification authority (CA). The length of the key or the signature correlates with the security of the crypto method used.

#### SYS.1.1.M27 Host-based Attack Detection (IA)Host-based Intrusion Detection Systems (IDS) should monitor system behavior for anomalies and misuse. The IDS mechanisms used should be suitably selected, configured and extensively tested. In the case of attack detection, appropriate alarming of the operating personnel must be ensured (see building block NET.3.4 IDS / IPS).

** Regular integrity check **

Periodic control of the file system, file attributes and process information, as well as other important elements of the system configuration (for example, the Windows Registry) for unexpected changes, helps to detect inconsistencies. The detection of such inconsistencies can be used to prevent system instabilities. It can also be detected in a timely manner attacks. If an attack is actually present, it is important to reconstruct the attacker's approach. On the one hand, this serves to detect manipulation of data and, on the other hand, to detect hidden backdoors that an attacker could have installed on the computer for later access.

** Calculation of cryptographic checksums **

To detect tampering, programs can be used that calculate cryptographic checksums over much of the system's files or through other resources. A distinction should be made between integrity checking programs, which work only at the file level, and those that can also check processes and special configuration data, such as the Windows registry or kernel data structures. It is recommended to make sure that these tools can also be centrally administered and monitored. In addition, the cryptographic mechanisms used by the programs must conform to the state of the art.

Some programs only detect if changes have been made to the file system. For this, they check whether the access rights, the date of the last modification or the contents of the respective file have been changed. Modifications are detected by comparing the previously created cryptographic checksum with the currently calculated checksum. With a special setting, in many cases even a read-only access to the file can be noticed.

** Protection of the checksum file **

To prevent the integrity checker itself or the file containing the checksums of the system from being corrupted by an attacker or malicious software, they should be located on a read-only medium. However, the checksum file must also be changed if changes are allowed to the file system so that CDs, DVDs or removable disks are recommended for this purpose. Alternatively, the checksum file can also be made read-only via the network. In managing the integrity checking program over the network, this approach should also be preferred. Some malicious programs camouflage themselves so that they can not be detected with methods of the manipulated operating system. Therefore, in case of suspicion, it makes sense to examine the system using a tamper-free operating system. For this purpose, for example, an external data carrier can be created via a trusted reference system, from which the tamper-free operating system is then started.

** test interval and test scope **An integrity check should be performed regularly, for example every night. The choice of a suitable test interval depends heavily on the intended use of the respective IT system or the environment of use. Integrity checks should also consider the amount of disk space and computation time required to verify the checksums. Use of the Integrity Check Program must not interfere with proper operation.

In the normal operation of any major IT system, there are constantly smaller and larger changes to system files. In general, it is therefore advisable to configure the integrity checking program so that only changes to relevant files are recorded. Otherwise, there is a risk that a large number of change notifications are triggered, which are due to normal business processes and not to attack attempts (false positives). As a result, it may happen that the log files can no longer be evaluated promptly.

** Process information in RAM **

In addition to file-based integrity checks, it is also possible to check process information from the main memory against a list of permitted processes (whitelist). In this way, certain manipulations can be detected that leave no traces in the file system. On the other hand, there are manipulations that do not affect the processes themselves, but only their configuration. Such manipulations may be more easily detected by an integrity check of the configuration files. Integrity checks of the file system and the memory thus have partially different protective effects. An advantage of checking process information in memory is that it requires little or no disk access that is significantly slower than memory access. This can be checked much more often than a file-based method that requires a lot of information to be read from the disk. This way, unwanted programs can usually be detected faster than with a file-based integrity check.

**Notification**

Notification of the result, even if no changes were detected, should be made automatically by e-mail or a similar route to the IT operation. It should be decided in advance which measures should be taken if a loss of integrity is detected. It is important, for example, whether automatic or manual actions are performed.

#### SYS.1.1.M28 Redundancy (A)

The availability of business processes, applications and services often depends on the functionality of a central server. But the more applications that run on a server, the more resilient it must be. As a rule, a server contains several potential sources of error ("single points of failure"), ie components whose failure can trigger the failure of the entire system: hard disks, power supply, fans, backplane, etc. Restoring the entire system can take a considerable amount of time in this case take advantage of. In addition to the provision of spare parts, the following additional options can be used to increase availability:

Cold Standby
* Hot-Standby (manual panning)
* Cluster (automatic panning)
* Load balanced cluster
* Failover cluster
Each of these techniques offers a different level of availability and is usually associated with different costs. In some cases, higher availability can be achieved if the affected servers are virtualized (see SYS.1.5 Server Virtualization).

** Cold Standby **In cold standby, a second identical replacement system is kept in addition to the actual production system, but this is not active. If the first system fails, the backup system can be manually powered up and integrated into the network.

After providing individual parts, this is the simplest redundancy solution, with the associated advantages and disadvantages:

Advantages of a cold standby solution:

Cold-Standby solutions do not increase the complexity of the overall system.
* The cost of a cold-standby system only adds up to the cost of the additional hardware and is thus the lowest among the options presented.
* Reboot or changes in the system are possible without loss of availability. The productive operation is transferred during the changes to the cold-standby system.
Disadvantages of a cold-standby solution

* A second system must be maintained for the existing system.
* The replacement system must be kept up-to-date at the current configuration and patch level.
* Because the backup system must be manually activated, administrators must continuously monitor the system and intervene in an emergency.
* If the application data is not stored on an external storage system so that it can be accessed directly from the replacement system, then it must be migrated to the cold standby system.
It is well suited for servers with applications where short or limited downtime is required to intervene in IT operations. Examples are:

* Server in smaller networks (intranet)
* Least frequented servers on the internet
** Hot Standby (manual panning) **

In the case of a hot standby, a replacement system is also available, which is kept in parallel with the production system in parallel. The function of the productive system is monitored, in case of failure the replacement system becomes active. The change can be automatic or manual. For the automatic change, additional functionalities are required in the overall system. As the automatic detection of failures. This case is covered in the next section under "Clusters".

In order to keep the downtime as low as possible, the condition of the replacement system has to be checked continuously.

Advantages of a hot standby solution

* Downtime is lower compared to cold standby.
* As with cold standby, this solution is also relatively inexpensive compared to higher-value high-availability solutions, which are described below.
* The replacement system is in operation and can also be used for data replication.
* New or changes in the system are possible without loss of availability. The productive operation is transferred during the changes to the hot-standby system.
Disadvantages of a hot standby solution

* Here, too, only half of the existing hardware is used.
* The replacement system must be constantly updated.
* Manual activation of the hot standby system requires continuous monitoring by a system owner.
The use of hot-standby systems is suitable for applications where short downtime is not critical. The problem of system monitoring and active switching of the hot standby server must be taken into consideration. Possible applications are z. For example:

* Web server with often varying content
* Server in smaller networks (application server, mail server)
* Database server and file server (eg secondary server constantly replicates primary server and will be used as primary server in case of failure)
** Cluster (automatic panning) **A cluster consists of a group of two or more computers that operate in parallel to increase the availability or performance of an application or service. The application or the service can be carried out actively on one of the computers or distributed over several (performance increase).

Clusters are in depending on the type of function in

* Load balanced cluster
* Failover clusters and
distinguished.

** Load balanced cluster **

With the Load balanced cluster, instances of an application or service are distributed among the servers depending on the load. If this is possible for an application or service, not only can load balancing be achieved, but performance can be increased, and failure problems are reduced.

One of the requirements for the use of load balancing is that the respective applications or services must not require write data access.

Redundancy can be created in this case by providing systems of similar performance "side-by-side" with the help of a load-balancing process, and ensuring that if one server fails, the other servers will intercept that failure.

Advantages of a Load balanced cluster

* It can be achieved both increase availability and performance.
* All available resources are used permanently.
* The solution is highly scalable.
* Complexity of the overall system is lower than with a failover cluster.
Disadvantages of a Load balanced cluster

* The use is not possible for all types of applications. In particular, applications that do not use read-only access while requiring all servers access to the same storage resources are not suitable for load balancing.
If the performance is very important in addition to the availability and the application allows a distributed deployment, a load balanced cluster offers an optimal solution. This can z. For example:

* Web server
* Front-end applications with read-only access (eg web server farms)
** Failover Cluster **

A failover cluster is referred to here as a cluster if, in the event of a failure of one of the cluster systems, the active operation of the application or service is automatically taken over by another part of the cluster (takeover). The automatic transfer of services in case of failure of a system component by a functionally equivalent component is called failover. For the failover functionality, a dedicated "heartbeat" connection is common, ensuring communication between the cluster servers. The cluster servers must be connected to the administration network in addition to the connection to the client network, in order to provide direct access in the event of an emergency.

An automatic failover assumes that all software and hardware components are properly monitored. Therefore, it is important to ensure that the failover mechanism is not based on false assumptions.

The following points must be considered when using a failover cluster:

* Shared memory access:
 In addition to the server's hard drives, which contain the operating system and the data necessary for the operation, it is advisable in a cluster to manage the application data on shared memory.
 Access to these disks is granted to the part of the cluster that is currently active. It is also possible to use replicated disks instead of shared disks. This is useful when failover occurs from a remote location. Local failover should consider whether the complexity and dependencies created by replication do not pose an additional threat to availability.
* Portability of the application:Installing and deploying an application on two or more servers in parallel requires the use of additional licenses in most cases. In addition, it must be checked whether the application allows failover functionality.
* NSPoF (No Single Points of Failure):
 If the failover functionality of the cluster can be disrupted by the failure of a single component, this contradicts the true purpose of the cluster architecture. To avoid single points of failure, you need to analyze the overall system and consider the failure of individual components (power supplies, system memory, memory, network cards, switches, hubs, etc.).
* Operating system and cluster server configuration:
 The cluster servers should be equipped with the same operating system versions, patches, libraries and application versions. The most identical possible hardware and software configuration can ensure identical behavior in the event of a failover. Moreover, in the case of identical systems, the complexity of the entire system is reduced (use of the same failover software, network interfaces, compatibility of the shared storage system, administration, service).
* Dedicated and redundant connection between the servers:
 The communication between the cluster servers must take place independently of the network load, as quickly as possible, so that the failover can take place as quickly as possible. Redundancy is also required due to high availability requirements.
* Use of sophisticated software products for failover management:
 Deciding whether or not to fail over is a very complex one. New or self-developed tools can contain errors and ultimately reduce the availability of the entire system.
* Extensive testing of all possible failover aspects:
 Extensive testing is also needed to determine that there are no single points of failure. In particular, server monitoring and failover management must be tested for all possible errors.
Benefits of a failover cluster

* The automatic takeover can significantly increase availability.
* No manual intervention is needed.
Disadvantages of a Failover Cluster

* This solution is highly complex.
* Failover clusters are not scalable well.
* Only a part of the resources is used.
* There are high costs due to additional hardware and software
As can be seen from the comparison of the advantages and disadvantages, the use of a failover cluster only makes sense if one or more applications have very high availability requirements. In addition to the high cost, very good knowledge of the responsible personnel both on the operating systems and applications used as well as the failover functionality is required. In addition, the use of failover solutions for servers makes sense only if all dependencies such as network connection or availability of the clients are also designed with the appropriate redundancies.

Areas typically used for failover clusters with high availability requirements are e.g. B .:

* Database applications
* File storage
* Applications with dynamic content
* Mail Server
Whenever business processes, applications or services have high availability requirements, it is important to consider how these requirements can be met. The IT managers and the security management should develop a concept for the corresponding servers and select appropriate architectures.

#### SYS.1.1.M29 Setting up a test environment (CIA)For servers with high security requirements, a test environment should be set up in which configuration changes, updates and patches can be pre-tested prior to importing to the production system. This applies to security patches and updates as well as normal updates issued by the manufacturer.

The test environment must be designed to allow a "functionally equivalent" installation of hardware and software. This does not necessarily mean that a second, identically configured system has to be procured for an expensive server computer. For testing configuration changes, updates and patches of application programs and server software, a technically much more economical system is usually sufficient.

However, it should also be possible to test new device drivers before importing. Therefore, it may be advantageous to use different test systems for different types of tests, such as one system for testing near-system programs or operating system patches, and another for tests related to the actual server software. In such a case, however, it is important to be aware that in this way certain types of interactions between operating system environment and server software can not be covered. In the case of special requirements for the security and reliability of a server, it may therefore be necessary to actually have a second, identically configured system as a test environment.

For several typical and more frequently recurring test cases, checklists should be created that can be executed during testing and that, in addition to the pure documentation of the test, can often also contribute to increasing efficiency and avoiding errors.

All tests should be documented so that they can be understood at a later date.

#### One service per server (CIA)

#### Application whitelisting (CI)

3 Further information
------------------------------

### 3.1 Worth knowing

Server virtualization is often used to increase data center efficiency. Because current server hardware is so powerful that classic server installations often do not take full advantage of hardware resources, multiple virtual servers can run on one physical server. This saves space and energy.

However, consolidating multiple servers into one hardware may require a better backup than a single server. The Federal Office for Information Security (BSI) has therefore published a recommendation on the topic: CSE-113: Server Virtualization. It is aimed at those responsible for the planning and operation of IT infrastructures as well as IT data center operators. The focus is on product-independent recommendations for the secure use of server virtualization products that are used as bare-metal hypervisors. In such deployment scenarios, besides the hypervisor, an operating system optimized specifically for virtualization, no other applications run on the physical hardware.

### 3.2 Literature

Additional information on threats and security measures in the "General Server" area can be found in the following publications, among others:

* #### [BSITLS] Minimum TLS Migration Guide 1.2

  

 Federal Office for Information Security, 2015
 [Https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Migrationsleitfaden\_Mindeststandard\_BSI\_TLS\_1\_2\_Version\_1\_2.pdf](https://www. bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Migrationsleitfaden_Mindeststandard_BSI_TLS_1_2_Version_1_2.pdf)

 
* #### [CSE113] CSE-113: Server virtualization

  

 CSE-113: Server Virtualization, BSI Cyber ​​Security Release, 03.2015[https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_113.htm](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_113.htm)

 
* #### [IEC62305] IEC 62305 (VDE 0185-305 / DIN EN 62305) - Lightning protection

  

 Standard series for lightning protection of structures, (last accessed 05.10.2017)
 <Https://www.vde.com/resource/blob/936756/5b65d838e75e83f750bd8fa23bb620b1/merkblatt-blitzschutznormen-13-download-data.pdf>

 
* #### [ISi server] Securing a server (ISi server), BSI, 09.2013

  

 Federal Office for Security in Information Technology, 02.2017
 <Https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102-2.pdf>

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008
 <Https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf>

 
* #### [RFC5246] RFC 5246, The Transport Layer Security (TLS) Protocol

  

 Internet Engineering Task Force (IETF), (last viewed 05.10.2017)
 <Https://tools.ietf.org/html/rfc5>

 
* #### [RFC5746] RFC 5746, Transport Layer Security (TLS) Renegotiation Indication Extension

  

 Internet Engineering Task Force (IETF), (last accessed 05.10.2017)
 <Https://tools.ietf.org/html/rfc5746>

 
* #### [TR02102] Cryptographic method recommendations and key lengths

  

 BSI, (last accessed on 27.09.2017)
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)