1 description
--------------

### 1.1 Introduction

A "general client" is an IT system with any operating system that allows the separation of users. You should be able to set up at least one administrator and one user environment. Typically, such an IT system is networked and operates as a client in a client-server network. The IT system can be operated on any platform. This can be, for example, a PC with or without a hard disk, a mobile or stationary device, but also a Unix workstation or an Apple Mac. The IT system typically has removable media drives, additional interfaces for data exchange, and other peripherals.

### 1.2 Life cycle

** planning and conception **

For the secure use of IT systems, the general conditions must be defined in advance. The security requirements for the existing IT systems and the planned deployment scenarios must be included from the very beginning (see SYS.2.1.M9 Planning the Use of Client-Server Networks). A client security policy should be established prior to acquiring clients and software (see SYS.2.1.M8 Setting a Security Policy for a Client-Server Network).

**Procurement**

For the procurement of clients, which typically takes place in larger quantities, criteria for the selection of suitable products must be formulated based on the usage scenarios (see SYS.1.1.M10 Procurement of a Client). When purchasing individual systems, it is also important that the client adapts to the existing structure so that there is no undue burden on integration and operation for a single IT system because of its special features.

If hardware or software does not meet the specified safety requirements, further action is required. These may be of an organizational nature (for example, by regulations that the client may only be operated behind closed office doors) or, in special cases, additional components may be procured to compensate for the identified shortcomings.

In the case of particularly high demands on the availability of the clients, the use of a Uninterruptible Power Supply (UPS) is recommended for these (see SYS.2.1.M35 Uninterruptible and Stable Power Supply). This can be, for example, a "single-user UPS", if the high requirements apply only to individual clients, or to its own corresponding secure circuit ("red outlet").

**Implementation**

To eliminate the risk of misuse or intentional misuse of IT systems, careful selection of operating system and software components, secure installation, and careful configuration are important. The measures to be taken are highly dependent on the operating system used. More about this can be found in specific modules, for example in SYS.2.3 Client under Linux or SYS.2.3 Client under Windows 10.

The foundation for safety is already laid during the preparation of the installation. Before installation, it should be determined which components of the operating system and which application programs and tools should be installed. The decisions made must be documented in such a way that, if necessary, it can be understood how the IT systems were configured and equipped with which software (see SYS.2.1.M14 Secure installation and configuration of a client).

**Business**
One of the most important security measures in the operation of today's client systems is to protect the IT systems by installing and permanently updating a virus scanner (see also SYS.2.1.M6 Use of virus protection programs). In addition, regular data backup (see also SYS.2.1.M4 Regular Data Backup) is a basic prerequisite for preventing hardware defects and program or user errors from causing serious data loss.

** ** segregation

When eliminating a client, it must first be ensured that all user data is saved or transferred to a replacement system. Afterwards it must be ensured that no sensitive data remains on the hard disks of the client. It is not enough just to reformat the disks, but they have to be completely overwritten at least once. It should be noted that the data is not really removed from the hard drives unless they are logically deleted or reformatted by the means of the installed operating system. With suitable software, data that has been deleted in this way can be reconstructed, often without much effort. After eliminating a client, inventories and networks must be updated. More detailed information can be found in SYS.2.1.M24 Regulated decommissioning of a client.

** Emergency Preparedness **

The necessary degree of emergency preparedness for a general client depends heavily on the individual deployment scenario. Often, as a precautionary measure for a client, it will be sufficient to back up the data regularly and to create a bootable data medium for emergencies (see SYS.1.1.M34 Integration into contingency planning). For clients with special availability requirements, it may be useful to take further action, such as having an exchange system ready.

2 measures
-----------

The following are specific implementation hints in the Common Client section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### SYS.2.1.M1 user authentication

The identification and authentication mechanisms of IT systems or IT applications must be designed so that users are uniquely identified and authenticated. Identification and authentication must occur before any other interaction between the IT system and the user. Further interactions may only be possible after the users have successfully identified and authenticated. The authentication information must be stored in such a way that only authorized users can access it (check it or change it). With every interaction, the IT system must be able to determine the identity of the user.

There are several techniques that can prove the authenticity of a user. The most well-known are:

* PINs (Personal Identification Numbers),
* Passwords,
* Tokens such as B. access cards as well
* Biometrics.
For security-critical areas of application, strong authentication should be used, combining two or more authentication techniques, such as password plus transaction numbers (one-time passwords) or plus smart card. Therefore, this is often referred to as two-factor authentication or multi-factor authentication. All authentication techniques used must be state-of-the-art.

** ** Passwords

If passwords are used for authentication in a client, the security of the access and access rights management of the IT system is crucially dependent on the correct use of the passwords. For this, a guideline for password usage should be created and published. In addition, IT users should regularly, e.g. At team meetings, be noted.
When passwords are used for authentication, the IT system should provide mechanisms that meet the following conditions:

* It ensures that each user uses individual passwords (and can select them himself).
* It is checked that all passwords meet the defined specifications (eg minimum length, no trivial passwords). The password quality check should be individually adjustable. For example, it should be possible to specify that the passwords must contain at least one special character or that certain character combinations are prohibited.
* The IT system generates passwords that meet the defined requirements. The IT system must offer the passwords thus generated to the user.
* The password change should be initiated regularly by the IT systems. The lifetime of a password should be adjustable.
* The repetition of old passwords when changing the password should be prevented by the IT system (password history).
* When entering the password, the password should not be displayed on the screen.
* After installing or reconfiguring users, the password system should force a password change after the initial login.
More detailed information on authentication can be found in ORP.4 Identity and Permission Management.

#### SYS.2.1.M2 Role separation

Basically, a distinction can be made between identifiers for users and administrators. Only administrators manage the IT systems, while normal user IDs only have the rights to perform their work-specific tasks. Normal user IDs may not have administration rights to protect the operating system and client configuration from accidental, negligent or intentional modification by the user.

If users only need to perform certain administrative tasks, it is often not necessary to give them all rights associated with their own login, or even system administrator rights. Examples include certain routine system administration activities, such as creating backups or setting up a new user menu-driven with a program, or activities that require a user to have only a single application program. In particular for temporary staff and external service providers, care must be taken that they only use the services and only access the data they actually need. When your activity is over, disable their accounts and remove all access permissions.

If possible, users should be provided with a limited user environment. For example, it can be implemented under Unix with a restricted shell (rsh) and a restriction of the access paths with the Unix command chroot. Another possibility is to run individual application programs, such as web browsers, in the so-called kiosk mode, so that there is only limited access.

If particularly extensive rights are assigned to user IDs, this should be as restrictive as possible. On the one hand the circle of privileged users should be restricted as far as possible and on the other hand only the rights needed for the execution of the work should be assigned. For all tasks that can be performed without extended rights, privileged users should also work under identifiers with standard rights.

#### SYS.2.1.M3 Enable auto-update mechanisms
Many products have automatic update mechanisms (autoupdate) that inform users when there are patches or updates. Often, these also offer the option of downloading and installing the updates immediately via the Internet. In general, the existing auto-update mechanisms must be activated. As a rule, all operating systems and available standard software packages today contain such mechanisms. The functionality of the update mechanism varies depending on the version, installation mode and manufacturer.

Usually, auto-update IT products look for new versions or software packages every time they start their IT systems or every time they dial into the Internet on a public update server. Products provide several ways to configure the auto-update mechanism. When new IT components are put into operation, it should always be checked whether and which update mechanisms they have and how they can be configured. It should also be checked which data is transferred from the auto-update mechanism to the manufacturer. It should first be clarified in principle how these mechanisms are handled. Then it should be determined how the update functions are concretely configured in the different products. The following is an overview of different variants of these mechanisms.

The complete deactivation is not offered by every software. If the institution wants to prevent the uncontrolled communication of IT components with the outside world, then packet filters must be used.

If a query from a public update server is not desired, many software products can be redirected to Internet addresses other than the manufacturer's, such as internal.

Some manufacturers offer software for own operation of update servers or update mirror servers, whereby the update server in the institution is installed locally (eg Windows Server Update Services WSUS). The update server then communicates directly with the manufacturer and loads the desired updates directly from the manufacturer. The advantage of this solution is that the IT systems of an institution affected by the update do not have to communicate themselves with the manufacturer's update server, but only with the locally installed. This allows the traffic to the outside to be minimized. With many products for update servers, the desired settings can be conveniently made via a graphical user interface (GUI). However, there are also products in which the necessary settings to use local update servers or to prevent the query from a public update server are hidden or can only be prevented by packet filters or firewalls.

If public update servers are to be used, the authenticity of the update server must first be checked. In addition, it should be investigated whether time intervals or events for controlling the update request action can be set. The settings must then be made according to the defined change strategy.

It should be examined how the communication with update servers can be limited to the lowest possible level. It must also be decided whether direct communication with the manufacturer should be the only alternative or parallel to internal communication (parallel configuration).
A parallel configuration is often useful for mobile users who do not always communicate within the government or enterprise network. For mobile IT systems, for example, it can be more important to load a current patch when it closes a dangerous security gap than to wait for release from change management. However, it may also be desired that all software changes are made solely by the internal shared software distribution.

Among other things, auto-update mechanisms still have to be aware of whether the changes are only downloaded to an internal IT system by the manufacturer and the installation of the change is subsequently left to the user or whether they are automatically installed immediately after downloading.

In addition, it must be determined how this should be handled if the IT system has to be restarted by an update. It can be decided to restart the IT system immediately, but it can often be determined that such updates will not be installed until the IT system is shut down as scheduled.

#### SYS.2.1.M4 Regular backup

To avoid data loss, regular backups must be performed. In most clients, these can be largely automated. There are regulations to be made, which data will be backed up by whom and when.

At least the data that can not be derived from other information must be backed up regularly.

It is recommended to create a data protection concept, taking into account the requirements of the OPS.1.1.5 data backup module

** Note: ** Even though users should store all work results on central servers, business-relevant data will always be found on clients as long as they provide a means to do so. Therefore, clients must also be included in the institution's data protection concept.

Depending on the amount and importance of the data being re-stored and the possible damage caused by loss of this data, the following must be specified:

* Time interval
 Examples: daily, weekly, monthly
* Time
 Examples: at night, on Fridays in the evening
* Number of generations to keep
 For example, a full daily backup will keep the last seven backups, as well as Friday evening backups for the past two months.
* Scope of the data to be backed up
 The easiest way is to specify partitions or directories that are taken into account during regular data backup. A suitable differentiation can increase the clarity and save effort and costs. Example: self-created files and individual configuration files
* Storage media (depending on the amount of data)
 Examples: tapes, DVDs or Blu-rays, hard drives, USB sticks
* Previous deletion of media before reuse (eg for tapes or cassettes)
* Responsibility for implementation (administrator, user)
* Responsibility for monitoring the backup, especially in the case of automatic execution (error messages, remaining space on the storage media)
* Documentation of the created backups (date, type of execution of the backup as well as selected parameters, labeling of the data carriers)
Due to the great effort, full backups can usually be done at most once a day. The data created since the last backup can not be restored. Therefore, and to reduce costs, differential or incremental fuses should be performed regularly between the full backups. Notes on the different types of data backups can be found in the implementation notes of the OPS.1.1.5 data backup module.
A differential or incremental backup can occur more frequently, for example, immediately after important files have been created or several times a day. Compatibility with ongoing operations must be ensured.

For software used, it must be decided separately whether it has to be recorded by the regular data backup. This depends, for example, on the cost of reinstalling the client and applying patches and updates. It may be sufficient to make backup copies of the original data media.

It has to be tested regularly if the data backup works as desired, especially if backed up data can be replayed without problems.

All users should be informed about the data protection rules in order to be able to point out any shortcomings (for example, too short a time interval for their needs) or to make individual additions (for example, intermediate mirroring of important data on the own disk). Also, informing users about how long the data is re-playable is important. For example, if only two generations are kept with weekly full backup, depending on the time of the loss only two to three weeks remain time to make the re-recording.

If only the network shares are backed up with networked clients, it must be ensured that the data to be backed up is regularly transferred by the users or automatically transferred there. It is better if all data is stored exclusively on the network drives. For major changes to IT systems or the information network, the backup process must be adapted accordingly.

Confidential data should be encrypted as far as possible before the backup, but the data must also be able to be decrypted after a longer period of time (see CON.1 Crypto Concept).

The printout of data on paper is not an adequate way of securing data.

#### SYS.2.1.M5 screen lock [user]

A screen lock is the ability to hide the information currently displayed on the screen and to protect the computer from unauthorized access. A screen lock must only by a successful user authentication, so z. As a password query, can be disabled so that in a shorter absence of the IT user access protection for the IT system is guaranteed.

The screen lock should be manually activated by the user as well as automatically started after a specified inactivity period. All users should be aware that they will activate the screen lock when they leave work for a short time. For longer absences, users should log out.

The period after which a screen lock activates due to missing user input should not go below or below certain limits. The period should not be too tight, so that the screen lock does not start after a brief pause for thought. Under no circumstances may this period be too long so that the user's absence can not be exploited by third parties. A reasonable default is a period of 15 minutes. It is recommended to set the waiting time, which takes into account the security requirements of the respective IT systems and their environment of use.

Almost all operating systems contain screen locks. When using them care must be taken to activate the password prompt.

#### SYS.2.1.M6 Use of virus protection programs
Different modes of action can be used to protect against malicious programs. Programs that search IT systems for all known malicious programs have proven to be a potential tool in malware prevention in the past. Therefore, according to the requirements described in OPS1.1.4 Protection against malicious programs, virus protection programs should be used.

** Regular examination of the entire database **

Even if the virus protection program checks for malicious programs each time it accesses files, it makes sense to regularly examine all files on clients and file servers. This way malware can be found for which there was no signature when it was saved. In such cases, for example, it must be examined whether the malicious program has already collected confidential data, disabled protective functions or downloaded code from the Internet before it was discovered.

For performance reasons, a complete audit of the dataset should be performed at times when IT resources are not under heavy use. It is ideal if the software monitors the utilization of the client and automatically uses its "work breaks" for the check. On the clients, the virus protection program z. B. also be coupled with the start of the screen saver. Even under heavy load, it is advisable to carry out a regular check of the data stock on a regular basis.

** Data exchange and data transfer **

Data to be sent must be checked for malware immediately prior to shipment. Similarly, received data must be checked for malicious programs immediately upon receipt. These checks are required both when accessing data carriers and when transferring data over communication links. The reviews should be automated as much as possible.

** Detection of malicious programs even in encrypted or compressed files **

When using encryption techniques, the potential impact on malware protection must be considered. If data is encrypted, system components or applications can not access this data unless they have the appropriate key. This implies that a virus protection program must either run in the context of the user or be equipped with the appropriate cryptographic keys in order to check an encrypted file for malware. However, if the user ID under which the virus protection program is run is provided with the appropriate cryptographic keys, new security risks arise which must be avoided. Therefore, it is recommended that you use a resident virus protection program that checks for malicious programs in the user context every time you access a file.

The virus protection program should also find malicious programs in compressed files, supporting all popular compression and archive formats. Malicious programs in nested archive files should also be found.

** Protection against unauthorized deactivation or change **

The virus protection programs on the clients and endpoints must be configured so that users can not make any security-relevant changes to the settings of the virus protection programs. In particular, it must be ensured that the users can not deactivate the virus protection programs.

#### SYS.2.1.M7 logging

The possible logging on the client is to be activated to a reasonable extent. The IT operation must periodically check the client's log files. All security-related events should be logged. The following events are of particular interest:
* incorrect password entry for a user ID up to the blocking of the user ID when the failed test limit is reached,
* Attempts of unauthorized access,
* Data from which the network utilization and congestion can be determined.
How many events are logged depends, among other things, on the protection requirements of the respective IT systems. The higher their protection requirements, the more should be logged.

Since the log files can become very extensive over time, the evaluation intervals should be chosen so short that a meaningful evaluation is possible. In order to enable a meaningful evaluation, each protocol entry should contain user identification or process number, identification of the terminal, date and time.

It is necessary to check which legal or contractual retention periods for log files have to be observed. In order for actions to be reproduced for a long time, a minimum storage period may be required, for privacy reasons there may also be a deletion obligation.

Especially with a large number of clients, the log data should be combined and evaluated centrally. For this, it is recommended to use a central logging server, see OPS.1.1.6 Logging.

#### SYS.2.1.M8 Hedging the boot process

When booting from removable media or installing third-party software, not only can security settings be bypassed, but the IT system can also become infected with malicious programs. In addition, malicious programs can also intervene in the boot process. Those responsible should counteract these risks by appropriate organizational or technical security measures. For this purpose, there are various procedures which are described concretely in the implementation notes of the block SYS.3.4 mobile data carrier:

* Removal of drives
* Locking drives
* Disable drives in the BIOS or operating system
* Control of interface usage
* Encryption (exclusive access to encrypted data carriers)
* Guidelines for use
Regardless of what the institution chooses to do, it is important to prevent content from mobile media from being automatically executed when it is connected. To do this, deactivate the corresponding autorun and autoplay functions of the operating system.

To cryptographically secure the boot process, on systems with UEFI firmware, the SecureBoot option should be enabled and the key databases should be configured to the institution's specifications. This configuration should be secured so that it can not be turned off. The access to the configuration interface of the firmware should at least be password protected.

In order for safety measures to be accepted and observed, users must be informed and sensitized about the hazard.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the "general client" area.

#### SYS.2.1.M9 Setting a security policy for clients

The security requirements for all clients result from the institution-wide security policy. Based on the general policy, the requirements for the given context must be specified and summarized in a security policy for the respective group of clients. In this context, it has to be examined whether, in addition to the institution-wide security guideline, further superordinate requirements such as IT guidelines, password guidelines or Internet usage guidelines must be taken into account.
The security policy must be known to all users and other persons involved in the procurement and operation of the clients and be the basis for their work. As with all directives, their content and implementation must be regularly reviewed by a higher level audit.

The security policy should specify the level of security generally to be achieved and make basic determinations. In order to improve the clarity, it may be useful to develop separate security guidelines for different fields of application.

First of all, the general configuration and administration strategy ("Liberal" or "Restrictive") should be defined, as the further decisions depend essentially on this definition.

For clients with normal protection needs, a relatively liberal strategy can be chosen, which in many cases simplifies configuration and administration. In general, however, it is also advisable in these cases to interpret the strategy only "as liberally as necessary".

For clients with a high protection requirement, a restrictive strategy is generally recommended. For clients with greater protection needs regarding one of the three core values, a restrictive configuration and administration strategy should be implemented.

Here are some things to consider:

* Regulations for the work of the users of the clients:

 
+ Should a client only be used by a single user at a time, or is it intended to operate with changing users?
+ Are users allowed to change certain configuration settings themselves (eg screen background, screensaver or similar) or are all settings defined centrally?
+ Are users allowed to access certain areas of the IT systems? These specifications usually affect both the rights granted in the IT system itself and the specifications for the installation and basic configuration.
+ What information can users store locally on the clients? In general, all business-related information should be stored centrally on a server where it is regularly backed up. Otherwise, care must be taken to ensure that all information of the users stored locally on the clients is taken into account in the client's data protection concept.
+ Are users required to shut down and shut down the client in the evenings, or do they need to be on 24/7? For example, fire shutdown and power conservation are key to turning clients off at work. In addition, hard disks used in clients are usually not suitable for continuous operation. A continuous operation of the clients may still be desirable, for example, if automatic backups are created overnight.


 
* Regulations for the work of IT operations and auditors:

 
+ According to which scheme are administration rights assigned? Which administrator is allowed to exercise which rights and how does he obtain these rights?
+ Which access routes may administrators and auditors use to access the IT systems?
+ Which processes and events must be documented? In what form is the documentation created and maintained?
+ Is a four-eye principle valid for certain changes?


 
* Specifications for the installation and basic configuration:

 
+ Which installation media are used for installation?
+ Should a central authentication service be used or is user administration and authentication only local?
* Regulations for user and role administration, authorization structures (procedure and methods of authentication and authorization, authorization for installation, update, configuration changes, etc.). If possible, a role concept for the administration should be developed. You must not use collective identifiers that use different users with the same ID.

 
+ If the client has decided to encrypt parts of the file system, then you should specify how this should be done (see also SYS.2.1.M25 Client Encryption).
+ When using encrypted file systems, a separate concept should be created for this and the details of the configuration should be documented with particular care, as in the case of problems (loss of key or passphrase to the key, incorrect configuration or similar) the data on the encrypted file systems would otherwise be completely lost could be.
+ Regulations for the creation and maintenance of documentation


 
* Requirements for safe operation:

 
+ Which user group is allowed to log on to the IT systems?
+ How can users authenticate themselves to the IT system? In general, an automatic login, in which the users are logged in without active authentication when the client starts up, should be avoided.
+ Can users access one or more LANs or the Internet? Which protocols may be used? For clients that are used as workstations in an institution, it is usually not necessary and often undesirable for normal users to access another workstation over the network.
+ What resources can users access?
+ Requirements for password usage must be established (password rules, rules and situations for password changes, if applicable, deposit of passwords).
+ How is the starting process of the IT system ("booting") secured against manipulation? Only administrators should be able to boot the clients from drives or external storage media. Therefore, clients should be provided with a boot lock that prevents booting from external media such as CD-ROMs, DVDs, or USB storage (see SYS.2.1.M12 Hedging the boot process) to provide such a lock that can only be removed by IT operations as part of troubleshooting if it starts the IT system with the emergency boot media (see SYS.2.1.M4 Periodic Backup).
+ Should the IT system cryptographically secure the boot process? Eg via UEFI Secure Boot?


 
* Network communication and services:

 
+ Should a local packet filter be set up?
+ Which external network services should be accessible from the client?
+ If a distributed file system is to be integrated Distributed file systems in which the user data is transmitted unencrypted should only be used in exceptional cases and exclusively in the internal network. If a distributed file system is to be used over an insecure network, it must be secured by additional measures (cryptographically protected VPN, tunneling).


 
* Logging:

 
+ Which data is logged? How and at what intervals are the log data evaluated? Who carries out the evaluation?


 
Based on the above points, a checklist can be created that can be helpful in audits or revisions.

Responsibility for the security policy lies with security management. Changes and deviations from this may only be made in coordination with the safety management.
When creating a security policy, it is advisable to proceed in such a way that first of all a maximum of requirements and specifications for the security of the IT systems is established. These can then be adapted to the actual circumstances. Ideally, this will ensure that all necessary aspects are taken into account. The reason for non-consideration should be documented for each deficient or weakened default in the second step.

Regarding user regulations, however, it should be kept in mind that they only make sense as far as they are applicable in normal day-to-day work, but also how they can be monitored and enforced. For example, it is not expedient for access restrictions to prohibit users from accessing certain directories only in the security policy, but not to actually protect them from access by granting appropriate rights. Access restrictions that were set when the security policy was created should therefore always be enforced as far as possible via the appropriate installation and configuration guidelines for the clients.

While the security policy is formulated for clients, it is also important to strike a balance between security (by restricting functionality and restricting user rights) and ease of use. If users are restricted by regulations that are not transparent to them and which may even be perceived as harassment, they may in turn be tempted to circumvent these restrictions with particular creativity.

This differentiates the security policy for clients from the corresponding policies, for example, for servers or active network components, which usually only address technically savvy users and administrators, to whom many restrictions can be made more plausible.

#### SYS.2.1.M10 Planning the use of clients

A basic requirement for clients to operate safely is an adequate level of planning in advance.

The planning of the assignment can be carried out in several steps according to the principle of top-down design: Based on a rough concept for the overall system, concrete plans for sub-components are defined in specific sub-concepts. Planning does not only concern aspects that are classically associated with the term security, but also normal operational aspects that entail security requirements.

In the rough concept, for example, the following typical questions should be dealt with:

* What tasks should the clients fulfill? Which services must be accessible by the clients? Are there any special requirements for the availability of the IT systems or the confidentiality or integrity of the stored or processed data?
* Should specific hardware components be used in the IT systems? This can be important, for example, for the selection of the operating system.
* Which hardware requirements (CPU, memory, hard disk capacity, network capacity, etc.) are based on the general requirements?
* Is the network in which the clients are to be used a homogeneous or heterogeneous computer network?
* Do the clients serve as a replacement for existing IT systems? Do you want to transfer data stocks or hardware components from the old IT systems?
* Should other operating systems be installed on the clients by multiboot?
It is recommended to create one or more generic requirement profiles (for example, "General Office PC", "Development Calculator" or "Administration Client") that can be used as the basis for concrete planning.

The following subconcepts should be considered in the planning:
* Authentication and user management: Which types of user management and user authentication should be used? Are users only managed locally or should a central administration system be used? Should the IT systems access a central, network-based authentication service or is only a local authentication required?
* User and group concept: Based on the institution-wide user, rights and role concept, appropriate rules must be created for the clients (see ORP.4 Identity and Permission Management).
* Administration: How should the IT systems be administered? Are all settings made locally or are the clients integrated in a central administration and configuration management?
* Partition and file system layout: In the planning phase, a first estimate of the required disk space should be made. For ease of administration and maintenance, it is recommended that as far as possible the operating system (system programs and configuration), application programs and data (for example, database server and data) and, if applicable, user data be separated. Different operating systems offer different mechanisms (partitioning into drives under Windows, mount points under Unix). Often it may be useful to save certain data even on its own hard disk or on its own hard disk system. This allows, for example, for a new installation or an update of the IT system, the data on the other partitions without copying to take over.
In the planning phase, the planned division of the partitions and their size should be documented.

* If confidentiality data is stored on the clients, the use of encrypted file systems is strongly recommended (see also SYS.2.1.M25 Client Encryption). Not necessarily all file systems need to be encrypted, but it will often be sufficient to provide encryption for the part of the file system on which the data itself is stored as well as for the part in which the data can be cached (paging file / file). partition or temporary directories). It must be ensured in all variants that no key material is saved in plain text, as this undermines the protection. This is facilitated by proper planning of the partition and file system layout.
* Increased protection requirements for the confidentiality of data stored on clients may require IT systems to be equipped with an encryption program that encrypts the entire hard disk and provides user authentication before the operating system is started ( for example via a chip card) ("pre-boot authentication").
* Network services and network connectivity: Depending on the security requirements of the data that must be accessed by the clients, the network connectivity of the clients must be planned.
* Depending on the intended use of the clients, access to other services in the network may also be required. This must already be taken into account in the planning, so that difficulties do not arise at a later date, for example due to insufficient transmission capacities or problems with interconnected security gateways.
* Monitoring: If there are special requirements for the availability of the clients, then a monitoring system can be used. For this, a monitoring daemon is installed on a server to which a locally installed on the client agent sends the monitored data, such as system usage or remaining free space. In the case of problems, for example, an alarm can be automatically generated (see also SYS.1.1.M26 System Monitoring).
* Logging: Logging also plays an important role for clients, for example when diagnosing and resolving malfunctions or when detecting and resolving attacks. In the planning phase it should be decided which information should be logged at least and how long the log data should be stored. In addition, it must be specified whether the log data should be stored locally on the IT systems or on a central log server in the network. More detailed information can be found in the module OPS.1.1.6 Logging
* It makes sense to specify in the planning phase how and at what times log data should be evaluated.
* High availability: If special requirements are placed on the availability of the clients, then it should be considered in the planning phase how these requirements can be met.
All decisions made in the planning phase must be documented in such a way that they can be reconstructed at a later date. It should be noted that usually other people next to the author need to evaluate this information. Therefore, attention must be paid to appropriate structuring and comprehensibility.

#### SYS.2.1.M11 Acquisition of clients

For the procurement of clients, which typically takes place in larger quantities, criteria for the selection of suitable products must be formulated based on the application scenarios. When clients are procured, it is important that the IT systems fit the existing structure, so that an individual IT system does not incur an unreasonable amount of integration and operation overhead due to its unique nature. More detailed information can be found in OPS.1.2.6 Procurement, Tendering and Purchasing.

#### SYS.2.1.M12 Software Compatibility Check

Prior to any intended procurement of software, their compatibility with the operating system used should be checked in the present configuration and the compatibility check should be included in the release procedure of the software. If the manufacturer of the software or other expert groups does not provide secure compatibility information, the compatibility should be checked in a test environment. Before any intended hardware change or migration, the driver software for all affected components should also be guaranteed to be compatible with the operating system.

#### SYS.2.1.M13 Access to execution environments with unobservable code execution

The use of execution environments with unobserved code execution, such. For example, Intel Software Guard Extensions (SGX) should be disabled in the client's firmware in the (UEFI) setup menu. The setting is named differently by the different manufacturers. It is usually in the security settings.

It should be kept in mind that sometimes the execution environments with unobserved code execution can not be switched off anymore. It should therefore z. B. be ensured by regular patching that the existing vulnerabilities are promptly resolved and thus have only the IT system and the respective manufacturer of the execution environment full access to these areas.

#### SYS.2.1.M14 Updates and patches for firmware, operating system and applications
Often, errors in products become known, which can lead to the information security of the information network, where they are operated, is affected. Corresponding errors can affect hardware, firmware, operating systems, and applications. These vulnerabilities need to be addressed as soon as possible so that they can not be exploited by internal or external attackers. This is especially important when the IT systems are connected to the Internet. Operating system or software component manufacturers typically release patches or updates that must be installed on their IT system to correct the error (s).

The system administrators should therefore regularly inform themselves about known vulnerabilities.

It is important that patches and updates, like any other software, can only be obtained from trustworthy sources. For each IT system or software product used, it must be known where security updates and patches are available. It is also important to verify the integrity and authenticity of the products already installed or the security updates and patches to be incorporated (see the section "Using Trusted Installation Media") before installing an update or patch. Before installation, they should also be checked using a computer virus protection program. This should also be done for packages whose integrity and authenticity have been verified.

Security updates or patches should be loaded quickly, but not prematurely, but must be tested before they are loaded. Otherwise, if a conflict arises with other critical components or programs, such an update may result in a failure of the IT system. If necessary, an affected IT system must be protected by other means until the tests are completed.

Before an update or patch is installed, the data should be backed up to the IT system so that the original state can be restored after problems. This is especially true if due to time constraints or lack of a suitable test system can not be tested in detail.

In any case, it must be documented when, by whom and for what reason patches and updates were recorded. If vulnerabilities are known, the documentation must be able to quickly determine the current patch level of the IT systems at any time to quickly clarify whether the IT systems are at risk.

If it is determined that a security update or patch is incompatible with another major component or program or is causing problems, it is important to consider how to proceed. If it is decided that a patch will not be installed due to the problems that have arisen, this decision must be documented in any case. In addition, it must be clear in this case which measures have been taken as a substitute so that the vulnerability can not be exploited. Such a decision must not be made by the administrators alone, but must be agreed with the supervisor and the ISB.

** Use of trusted installation media **

Carelessly executing programs that originate from "unsafe" sources can cause considerable harm. Malware, for example, can install password-spying programs, Trojan horses, or backdoors on a client, or easily corrupt or erase data.
Typical sources of such malware are, for example, programs that display themselves as screen savers, virus scanners or other utilities, and are sent by e-mail under fake sender addresses to many recipients. Often careless users download programs from the Internet and install them without verification.

In principle, software should only be installed from well-known sources, especially if it has not been delivered on data carriers but has been downloaded from the internet, for example. This is especially true for updates or patches that are typically no longer delivered on disk. Most manufacturers and distributors offer cryptographic checksums for this purpose, which allow at least a check of the integrity of a package. The checksums are usually published on the (transport encrypted) websites of the manufacturer or sent by (signed) e-mail. To verify the integrity of a downloaded program or archive file, the published checksum is then compared to a locally generated checksum by a corresponding program.

If checksums are offered for a software package, these should be checked before installing the package.

With checksums the authenticity can not be verified. Therefore, in many cases, digital signatures are offered for programs or packages. In turn, the public keys needed to verify the signature are usually available on the manufacturer's websites or from public-key servers. Often the checksums are generated with one of the programs PGP or GnuPG.

If the check reveals that this is a valid signature from the manufacturer, the package is more trustworthy than a package that has checksums. The package management system RPM (Redhat Package Manager), which is widely used in Linux distributions, and the APT / DPKG package management system already have built-in checking functionality for Debian-based distributions.

Sometimes even the built-in software update mechanisms of the respective operating system or application software do not perform cryptographic checksum comparisons. Software without these tests should not be used. If possible, however, the checksum should be verified for each software package before it is loaded.

Furthermore, the checksums often can not be automatically compared because the checksums, signatures, or certificates required for this are not provided by the manufacturers in a consistent manner. Therefore, they often need to be compared manually using the checksums from the manufacturer pages or by customizing the URLs in the patching and modification software.

If digital signatures are available for a software package, they should be checked in any case before the package is installed.

A fundamental problem with the use of digital signatures is the verification of the authenticity of the key used itself. If the public key carries no signature of a known trustworthy person or organization (such as a trust center), the signatures generated with the corresponding private key offer no real security in that the software package actually comes from the developer, manufacturer or distributor. Therefore, if not certified, public keys should preferably be obtained from a source other than the software package itself, such as a manufacturer's DVD, another mirror server on which the package can also be downloaded, or a public key Server.
In order to check checksums and digital signatures, the corresponding programs must be available locally. Administrators should be aware of the meaning and validity of checksums and digital signatures. In addition, the administrators must have enough time to use the appropriate programs in their daily work and familiarize themselves with the operation.

Patches and changes should not be emailed for a variety of reasons. The origin of emails is difficult to determine without the use of additional security mechanisms and the recipient addresses in the institutions are often distribution lists, whose address is easy to guess. Patches and changes can also be very extensive by now. Many companies and government agencies have limited the size of email attachments and may prohibit them from accepting executable attachments. Furthermore, the large amounts of data unnecessarily burden the e-mail systems. Therefore, a timely availability of the software changes, which can be critical, especially in the case of security patches, can not be adequately ensured via e-mail.

Furthermore, some manufacturers offer to send changes and patches to the customer directly on data carriers. In this case too, the patches and changes should be verified using checksums or digital signatures, as sender information on mailpieces and manufacturer logos on CDs and DVDs can easily be faked.

Another aspect of verifying the authenticity of the update may be news published by the manufacturer on its website, newsletter or similar channels. Some manufacturers have established cycles and timings that systematically release information about changes.

#### SYS.2.1.M15 Secure installation and configuration of clients

After completing the planning of a new client and creating a security policy, you can begin installing the client.

The installation and configuration of the IT system should only be performed by authorized persons (administrators or contracted service providers). Administrators of IT systems and their representatives must be carefully selected. You must be regularly informed that the powers may be used only for the required administrative tasks. Since administrators have a key role to play in the functionality of the hardware and software used, the continuation of activities must be guaranteed even if administrators fail. For this, the named representatives must have the current state of the system configuration and have access to the passwords, keys and security tokens required for the administration.

It is recommended to first create a short installation concept according to the functional requirements of the planning and the specifications of the security guideline. In principle, it is advantageous to carry out the installation in two phases: First, a basic system is installed and configured, then the other required applications are set up. The installation programs of most operating systems support this procedure more or less well.
The described steps do not necessarily need to be performed again for each client. This could even be counterproductive in that constant repetition increases the risk of error. It is therefore recommended that the steps described above be carried out with particular care on a reference system, that the exact documentation of the necessary configurations is documented in order to obtain an adapted installation concept for the respective operating system (see SYS.2.1.M27 Setting up a reference installation for clients). It must be noted that this installation concept must also be checked and, if necessary, adapted for changes to the operating system that do not represent a completely new release (service packs, update releases or the like).

**Installation**

During installation and later configuration, at least the important steps should be documented so that they can be understood at a later time. For example, a checklist can be created for the installation, where the steps taken can be ticked off and any settings made can be noted. A corresponding documentation is helpful for an error analysis or later reinstallation. It should be noted that, in addition to the author, other administrators, who may be less specialized in this field, have to resort to the documentation. Therefore, it is important that the documentation is well structured and understandable.

If the client is being installed from data carriers such as DVDs or other storage media, it is recommended that the installation and basic configuration be performed offline or at least in a secure network (installation or administration network). In general, it should be prevented that other IT systems can access the IT system to be installed during installation. This is important because during the installation usually no passwords are assigned and no protection mechanisms are active, but possibly already accesses are possible. If the installation of several IT systems is partly to take place over the network (for example, reloading of packages), it is recommended to use an installation server in the administration network.

Especially with the operating system itself, it is important that the installed version comes from a trustworthy source. This is especially important when, for example, CD images have been downloaded from the Internet. In this case, it is important to check whether digital signatures of the packages are available that can be used to verify the integrity and authenticity of the packages. If possible, packages and CD images for which no digital signatures or at least checksums exist should not be used (see also SYS.2.1.M13 Updates and patches for firmware, operating system and applications).

When setting up disk partitions, the concept created in the design phase must be implemented. If an encrypted file system is to be used, it usually has to be initialized before data can be copied into it, because often a file system can not be encrypted in retrospect.

If this has not already been done automatically, logging of the system events should be activated at the latest when completing the basic installation. The log data can provide valuable information in case of problems during further installation and configuration.

**Configuration**
The basic settings, which are made by the manufacturer or distributor of an operating system, are usually not optimized for security, but on an easy installation and commissioning and often on the fact that each user can access as easy as possible to many features of the operating system. When using IT systems (whether as a client or server) in government agencies or companies, this is often undesirable.

The first step in the basic configuration must therefore be to check the basic settings and, if necessary, to adapt them to the specifications of the security policy. The basic configuration is of course relatively heavily dependent on the operating system used. For this reason, the operating system-specific components contain corresponding, more detailed recommendations.

Goals of a secure basic configuration should be that

* the clients are protected against "simple" attacks via the network,
* no normal user can gain access to sensitive data that is not intended for him by pure curiosity or even accidental
* no ordinary user working normally with the clients due to mere operator error or carelessness ("what happens if I delete this file?") can cause serious damage to the IT systems or other users' data, and that
* also for the work of the system administrators the impact of smaller errors are limited as far as possible.
The settings that should be checked and adjusted as part of the basic configuration concern in particular the following areas:

* Settings for system administrators
 The identifiers under which system administrators work should be particularly secure. For example, this affects the settings for the user environment such as
*

 
+ Search paths for programs and files,
+ Environment variables and the
+ Configuration of certain programs.


 
These settings should be checked and adjusted if necessary. In addition, system administrator user directory settings should be set so that normal users will not have access to them.

* System directory and file settings
 The basic configuration must verify that the system directory and file permissions comply with the security policy. On a server, relatively restrictive settings should be selected for the permissions of the system directories and files.
* Settings for user IDs and user directories
 As part of the basic configuration, it should be checked which standard settings apply to user IDs and user directories. The settings may need to be adjusted according to the security policy. This essentially applies to the same parameters as system administrator identifiers, but other users may want to make other settings useful.
* Settings for accessing the network
 As part of the basic configuration, the settings for access to the network and important external services should also be taken and documented. This applies for example (if not already done during installation):

 
+ Assigning the IP address and configuring the basic network parameters or configuring access to a server that distributes network settings automatically, for example via Dynamic Host Configuration Protocol (DHCP). For servers, however, the use of DHCP is not recommended.
+ Configuration of access to a DNS server and, if necessary, other name services and the
+ Configure access to distributed file systems, databases or other external services.


 
* Additional protection through a local packet filter
Clients with high protection requirements should be protected with a local packet filter (see SYS.2.1.M28 Local Packet Filter Setup) or a personal firewall, in addition to protection by the institution-wide security gateways or packet filters that segment the internal network. Corresponding functionalities are present in practically all modern operating systems.
* Disable "Call Home" features
 Some operating systems and applications send information directly to the manufacturer, such as about errors that have occurred or about the system configuration, so that they can adapt the product to the needs of the users in the future. For this purpose, a data connection is established via data networks, such as the Internet, to the servers of the manufacturer. Such a form of data leakage can be critical, especially if users are not informed about the frequency and content of the data transfer. As a general rule, this often unwanted exchange of information should be prevented. Whether and how information is sent can usually be found in the license agreements of the software used. Many applications offer the option of deactivating this "Call Home" function. Only in justified exceptional cases, this should remain activated. After updates, it should be checked whether the "Call Home" function is still deactivated. Local packet filters or the central security gateway (firewall) can also be used to prevent the establishment of a connection with the manufacturer. For example, based on the destination addresses or port numbers, the data connections could be rejected. It should be noted that the consideration of all applications is complex and automatic update functions, if needed, are then often no longer available.
* Disable unnecessary interfaces
 In a basic configuration, all existing or potentially retrofittable interfaces are usually activated. Often, not all of them are needed and should therefore be removed or disabled. Some of these interfaces may also pose potential security issues that must be addressed through appropriate organizational or technical security measures. Interfaces whose use should be controlled include Bluetooth, WLAN, Firewire, eSATA (external SATA HDD connection) and Thunderbolt.
* Directory-based execution control
 With current operating systems, a directory or partition-based execution control is possible. The execution rights for all files in a directory and all subdirectories are suppressed. For example, on Windows-based operating systems, this can be accomplished through appropriate Group Policy with Software Restriction Policies. On Linux systems, the hard drive can be suitably partitioned and integrated with appropriate mount options "ro" (read only) and "noexec" (no execute). In addition, tools that set file-related permissions in the operating system exist for high protection requirements. Directory- or partition-based execution control, when properly configured, ensures that users

 
+ from directories to which they are allowed to write, can not start programs and
+ in directories from which they are allowed to start applications can not write. This makes it difficult for users to run a program file that they have downloaded from the Internet or copied from a USB flash drive.


 
* Monitoring
In order to be able to react to critical system events, these can be monitored by monitoring. For this purpose, status information is usually retrieved from a central IT system on which the events are evaluated. However, the interface needed to retrieve the system events from the IT system can often change system settings of the operating system, e.g. Via SNMP (Simple Network Management Protocol). If such a modification is not desired, then these features should be disabled.
* Memory protection mechanisms
 In order to protect the operating system and application against possible buffer overflows, appropriate memory protection mechanisms should be activated, as long as they are supported by the hardware (CPU) and the operating system used. For example, Executable Space Protection (ESP) can prevent programs from running out of unauthorized areas of memory.
* Creating an integrity database
 After completing the basic configuration, it is recommended that you create an integrity database using an appropriate tool. For some operating systems, such programs are already included in the scope of a standard installation. The integrity database should not be stored on the IT systems themselves, but on a read-only medium (such as CD-R) or another secure IT system. If there is a suspicion that the IT system is being compromised, the generated checksums can be used to identify files modified by an attacker. During regular system integrity checks, this database serves as a reference for a defined, secure state of the IT systems.
It should be documented which settings were checked in the basic configuration and if and how they were changed. The documentation must be such that, in an emergency, a person other than the actual administrator can understand what has been done without prior knowledge of the IT systems based on the documentation. Ideally, it should be possible to restore the IT systems with the help of documentation alone.

#### SYS.2.1.M16 Disabling and uninstalling unneeded components and identifiers

Often, as part of the standard installation of an operating system, a larger number of user IDs, programs, services and other components are set up, which are not necessary for the operation in each case. Therefore, it should be checked in the basic configuration, which user accounts are really needed. User IDs that are not required should either be deleted or at least deactivated in such a way that it is not possible to log in to the IT system under the ID in question.

The default installation of an operating system often includes a number of programs and services that are not normally needed and that can be a source of security vulnerabilities for that very reason. This applies in particular to network services. After installation, it should therefore be checked which services and applications are installed and activated on the IT systems. Unnecessary services should be disabled or completely uninstalled. In addition, unused runtime environments, interpreter languages ​​and compilers SHOULD be uninstalled.

On the one hand, checking for running services can be carried out locally with the resources of the installed operating system and, on the other hand, in network services from the outside through a port scan from another system. By a combination of both methods can be largely excluded that the IT systems offers even more unwanted network services.

#### SYS.2.1.M17 deployment clearance
Before clients are used in productive operation and before they are connected to a productive network, the application should be released, this must be documented. The deployment clearance is based on an examination of the installation and configuration documentation and the functionality of the IT systems in a test. It is carried out by a body authorized to do so in the institution.

More detailed information can be found in OPS.1.1.7 Software Testing and Approvals.

If it is determined that a security update or patch is incompatible with another major component or program or is causing problems, it is important to consider how to proceed. If it is decided that a patch will not be installed due to the problems that have arisen, this decision must be documented in any case. In addition, it must be clear in this case which measures have been taken as a substitute so that the vulnerability can not be exploited. Such a decision must not be made by the administrators alone, but must be agreed with the supervisor and the ISB.

#### SYS.2.1.M18 Usage of TLS [user]

The most common security protocol used in web browsing is SSL / TLS (Secure Socket Layer / Transport Layer Security), further information can be found in [TR02102], [RFC5246] and [RFC5246]. The first version of the SSL protocol (SSL v1.0) was developed by Netscape. Newer versions are standardized under the designation TLS in different RFCs. SSL / TLS is supported by all recent browsers. With SSL / TLS connections can be secured:

* by encryption of the connection contents,
* by checking the completeness and correctness of the transmitted data,
* by checking the identity of the server and
* optional by checking the identity of the client side.
At the beginning of a new communication connection secured with SSL / TLS, a so-called handshake takes place between client and server. Here, client and server communicate via the cryptographic algorithms used for key exchange, encryption and integrity assurance. In addition, client and server agree on the SSL version being used. In addition, the server sends its X.509 certificate to the client. Optionally, the client can also send the server its X.509 certificate if requested by the server. Using an asymmetric encryption method, a symmetric key is then securely exchanged. For the encryption of the actual data transmission, a symmetrical method is now used, because this allows large amounts of data to be encrypted faster. For each transaction, a different symmetric key is negotiated as the session key, which then encrypts the connection.

For example, a user can recognize web pages that enable SSL / TLS-secured data transfer because the Internet address is extended by an "s" (https: // www ...). In addition, such websites are also marked with most popular browsers, for example, by a displayed icon (key, padlock, etc.) or by a color tag of the Internet address.

The use of SSL / TLS is not limited to HTTP clients and servers. Even protocols such as SMTP, FTP, IMAP or LDAP can be cryptographically secured by SSL / TLS, but this requires that the respective clients and servers support this security function.
SSL / TLS consists of two layers. The SSL / TLS handshake protocol works on the upper layer. This serves the client and the server to authenticate each other and to negotiate a key and encryption algorithm for subsequent traffic. The lower layer, the SSL / TLS Record Protocol, which forms the interface to the TCP layer, encrypts and decrypts the actual traffic. Since SSL / TLS is based on the socket interface for accessing TCP and replaces it with a security-enhanced version, it can also be used for other services.

** version number **

There are several SSL / TLS protocol versions, such as SSL v2, SSL v3, TLS v1.0, TLS v1.1, and TLS v1.2. SSL v1 was not published. To ensure a secure connection between client and server, at least TLS 1.2 should be used.

TLS 1.1 provides sufficient security, but compared to TLS 1.2 it has some weaknesses, such as: For example, in TLS 1.1, cipher suites based on IDEA and DES are no longer available in TLS 1.2.

TLS 1.0 can be transitionally used in existing client applications if an immediate migration to TLS 1.1 or preferably TLS 1.2 is not possible and appropriate action against Chosen Plaintext attacks (eg BEAST) on the CBC implementation is made , In general, however, a migration to TLS 1.2 should be carried out as quickly as possible. SSL v2 and SSL v3 may no longer be used, see also the BSI Migration Guide for the minimum standard TLS 1.2 (see [MIGLFTLS]).

** Algorithms and key lengths **

With SSL / TLS, different cryptographic algorithms with different key lengths can be used. When connecting, the client and server agree on the procedures used in the session.

By selecting the products (browser, web server, plug-in, etc.) and appropriate configuration, it is important to ensure that SSL / TLS protected communication uses only algorithms and key lengths that are state of the art and security requirements of the institution. In addition, the cipher suites used should support Perfect Forward Secrecy (PFS). Further notes on algorithms and key lengths can be found in the module CON.1 Crypto Concept.

** ** Certificates

It is difficult to verify the identity of the communication partners in the data communication over open networks, since it is not certain that name information is correct. For SSL / TLS, the identity of the communication partner is verified by certificates. Certificates contain their public keys as well as a confirmation of another instance about the correct assignment of the public key to its "owner", in this case a server or client. The value of a certificate depends not least on how trustworthy this confirmation instance (also called trust center or certification authority) is. The authenticity of the certificate can in turn be checked with the public key of the confirmation instance.

Common operating systems and application programs, such as browsers, already contain SSL / TLS certificates from some certification authorities during installation. These CAs have very different security policies and conditions under which they issue certificates. Therefore, before security-critical information is transmitted over an SSL / TLS-protected connection, the security policy of the respective certification authority should be checked.
When adding a new certificate, care should be taken to activate it only after checking the "fingerprint". The fingerprint is a hexadecimal number that is transmitted along with the certificate. In addition, it should be transmitted and compared in a different way, as this should ensure the correctness of the certificate.

In the past, CAs have been compromised, exposing hundreds of fake certificates, including those for online information services, online portals, other certification authorities, and anonymization services. However, revocation lists and validation protocols such as OCSP (Online Certificate Status Protocol) can invalidate counterfeit, manipulated or outdated certificates in a timely manner. Therefore, certificate validation should be enabled in application programs such as browsers and e-mail clients. OCSP is preferable to the use of Certificate Revocation Lists (CRLs) because OCSP allows timely updates over the Internet.

If a certificate can not be validated, for example because the OSCP server can not be reached or the revocation lists can not be accessed, there are two options from the client's point of view: It can terminate the connection or accept a possibly manipulated or invalid certificate. Deciding what to do in such cases should be consistent with the institution's security policies.

** Session Renegotation and TLS Compression **

Using session renegotiation, both client and server can renegotiate the parameters of an existing HTTPS session. Due to a bug in the specification of the TLS protocol (see [RFC5246]), a man-in-the-middle attacker may be able to misuse session renegotiation to insert any content into an existing HTTPS session. Meanwhile, the TLS protocol has been extended (see [RFC5746]) and this design bug has been fixed. On the client side, session renegotiation should be deactivated.

TLS provides the ability to compress the transmitted data prior to encryption. This can result in side channel attacks on the encryption over the length of the encrypted data. An example of this is CRIME (Compression Retro Info-leak Made Easy), a page channel attack introduced in 2012 that aims to handle an HTTPS session. To prevent this, TLS compression should be disabled.

Note: When using SSL / TLS, it should be noted that encrypted data is not centralized in terms of active content and malicious programs. B. on the security gateway, can be checked. This must be taken into account in the security concept, so that no security gaps arise. Other recommendations can be found in the module OPS1.1.4 malware protection.

#### SYS.2.1.M19 Restrictive rights assignment

In principle, authorizations should always be restrictive so that users can access exactly the services and data they need for their tasks. This is especially important for system files or directories.
System files or directories are files and directories for which IT operations are responsible. These are either important for all users or serve administration purposes. System files should only have access to IT operations. Editor programs or compilers may not be used if they are not required for the task. The circle of authorized administrators should be kept as small as possible. Also directories may only provide the necessary privileges for the users. The granting of access rights to system files should always be restrictive and only in accordance with the in-house security policies.

System files should be stored separately from application data and user files. This provides a better overview and makes it easier to create backups and to properly protect access thereto.

Access to system files should always be logged. Unnecessary system files should be removed from the IT system so that they can not be misused for attacks or constantly monitored for integrity.

When granting access rights restrictively, it is not enough just to check the rights of a program. In addition, the rights assignment of all programs that are called from this program must be checked.

The integrity of all system files and directories, as well as the correctness of the access rights should be verified regularly if possible. For many operating systems there are tools for doing such tests quickly and reliably.

#### SYS.2.1.M20 Protection of administration interfaces

There are different ways to manage clients. Depending on the type of access used, a number of security precautions must be taken. With larger networks, it is advisable and often unavoidable to integrate the clients in a central network management system, since otherwise a secure and efficient administration can not be guaranteed. The methods used for administration should be defined in the security policy and the administration should be performed only according to the security policy.

It is recommended to create an overview of the various administrative activities, which work can be carried out in which way. First and foremost, it is important to note whether certain activities can not normally be carried out in a particular way.

* Local administration
 The administration of clients directly through access via the console is only manageable for a small number of computers and will usually represent an exceptional case in environments with a larger number of clients. If, for once, the IT operation has to work locally on a client, it is important, for example, that the administrator ensures that the password can not be spied out when authenticating via a password. If necessary, consideration should be given to using one-time passwords or the like for such work.
* Administration with the help of a boot medium
 For certain administration work to be performed locally on a client, it may be advantageous to use an external boot medium from which the client is started (see also SYS.2.1.M4 Regular Backup). This offers the advantage that the administrator can be sure of a "clean" system environment. However, this method also has a number of disadvantages, such as a higher cost. In addition, it is usually not possible in this way to understand certain error messages that occur during operation.
* Remote administration
Clients are often administrated from administration computers over the network. In order to prevent the authentication information of the administrators from being intercepted or even manipulated by an attacker, the administration should only be carried out via secure protocols (for example, not via Telnet, but via SSH.) Unsecured remote administration over external (insecure) networks may take place in This must be taken into account when setting up the security policy and, as far as possible, in the internal network as well as in non-secure protocols.
* Administration via a central management system
 If a central management system is to be used for the administration, analogous considerations must be made for this access path, as for remote administration. In addition, it is important that the central management system itself be configured and administered accordingly.
** Routine administration activities **

It is recommended to create administration notes for the usual routine IT operations according to the security policy. This includes, for example, activities such as

* Create and delete users,
* Install and uninstall programs,
* Importing security updates and patches,
* Import other updates and patches or
* Regular integrity check with appropriate tools.
#### SYS.2.1.M21 Prevention of unauthorized use of computer microphones and cameras

Many IT systems are equipped with microphones and sometimes also with cameras. Microphones and cameras of networked clients can be used by those who have access rights to the corresponding device file. For example, for a microphone, this would be / dev / audio for the sound card or / dev / video for a camera under Unix. Under Windows, the access rights to the corresponding keys of the registry (HKEY \ _LOCAL \ _MACHINE \ HARDWARE \.) Determine who can activate the computer microphone or the computer camera. These rights must therefore be given carefully. Access to the device file should only be possible while someone is working locally on the IT system. If existing microphones or cameras are not to be used and therefore not misused, they must, if possible, be switched off, deactivated or physically disconnected from the device.

If the microphone or camera is permanently installed in the client and can only be switched on and off by software, the access rights must be set in such a way that no unauthorized person can use them. This can be z. This can be done, for example, by revoking the read rights to the device files / dev / audio, / dev / video, or, under Windows, the access rights to the corresponding keys of the registry under Unix. This prevents a normal user from using the microphone or camera, but can still play audio or video files. Cameras can also be easily covered, for example with a suitable sticker.

For IT systems with microphone or camera, check whether access rights and owners are changed when accessing the device file. If this is the case, or if it is desired that each user can use a microphone or camera and not only be released by the IT operation in individual cases, the administrator must provide a command that

* can only be activated if someone is logged on to the IT system,
* can only be activated by this user and
* withdraws the access rights to the user after logging out.
As long as access to the microphone or camera is not controlled by a secure command, it must be physically disconnected from the client or the client from the network.
Clients with a built-in microphone or camera should be removed from the room during a face-to-face meeting, or at least turned off. For a laptop, any connections to communication networks that are not needed should be disconnected. In most cases, this is the easiest way to unplug the cable.

#### SYS.2.1.M22 Log out after task completion [User]

If an IT system or an IT application is used by several users and the individual users have different access rights to data or programs stored there, then the required protection can only be achieved by means of an access control if each user System or IT application logs off. If it is possible for a third party to continue working on an IT system or in an IT application under the identity of another, any meaningful access control is impossible. Therefore, all users must be obliged to log off from the IT system or the IT application after the task has been completed. For technical reasons (eg to close all open files), regulations should be made for logging out of IT systems and IT applications even if no access control has been implemented.

If it is foreseeable that only a brief interruption of the work is required, manual deactivation of the screen lock can be performed instead of logging off (see also SYS.2.1.M5 screen lock). In case of prolonged absence, the screen lock should be activated automatically.

Some IT systems and IT applications provide the ability to set a time period after which a user is automatically logged out of the IT system during inactivity. It should be considered whether this method is used as it can also lead to data loss. An automatic logout can z. B. in PC pools are used with strong public traffic, since a registered user can block the workplace using the screen lock unauthorized.

Depending on the workplace environment, consideration should be given to what provisions should be made for short-term absences of users. Thus, automatic activation of the screen lock should be faster in multi-user systems than those for a user, so z. B. already after five minutes.

#### SYS.2.1.M23 Use of client-server services

The exchange of information between equitable IT systems is often referred to as a "client-to-client" or often as a "peer-to-peer". Each IT system can offer or use services. The communication connection established for this purpose allows several IT systems to share resources decentrally with one another. This unites the typical functions of a server and a client on an IT system.

Often, such applications are used to provide the following services to other IT systems:

* Use of printers that are locally connected to an IT system by users on other IT systems
* Access to memory areas of the hard disks installed in the IT system or locally connected ("file sharing"),
* Direct communication via text messages ("Messaging") and
* Internet telephony.
** Benefits of client-to-client services **

Unlike server-based architecture, client-to-client services have many advantages:

* A dedicated server costs extra to purchase and operate.
* If the central server fails, the resources are no longer available ("single point of failure"). In the case of client-to-client services, if one client fails, generally enough other clients may be able to join in.
* Neighboring clients can exchange information more efficiently with each other more efficiently than when using a server that is far away.
* Servers require more bandwidth, more CPU, and more disk and memory than clients. These requirements can be distributed to the clients in client-to-client networks, where unused resources can be used.
* Shared information is often available on multiple clients simultaneously and redundantly.
However, the use of client-to-client services also has a number of disadvantages, many of which are due to the lack of centralization. For example, the exchanged information can not be centrally scanned for malicious software.

**Architecture**

Depending on requirements, client-to-client services can only be used on a local network or across the Internet. The number of IT systems that can share these resources ranges from just a few, selected clients, to an unmanageable set of unknown clients. In general, however, a distinction can be made between two types of client-to-client services:

* Local client-to-client services
 With local client-to-client services, individual clients can share resources with other clients in a LAN. These shares can often be managed directly by the operating system. An example of this is file and printer sharing in Windows operating systems. Access to these services can often be limited by passwords or a selection of IP addresses. Typically these services are not used beyond the local area network and are rejected at the security gateway (firewall). Because these services do not require a separate server, they can save hardware and software procurement costs.
* Public client-to-client services
 To exchange information with users who do not have access to the LAN, public client-to-client services can be used. For this, additional applications usually have to be installed on the respective IT system so that they can use the services provided by other clients. Since information is exchanged directly between two or more IT systems in client-to-client services, additional information about how these IT systems can be accessed is required for establishing a connection. For this reason, especially for large client-to-client networks, there should be an overview of which resources are provided to which client.
 In principle, the following types are distinguished:

 
+ Central client-to-client services
The installed application connects to a server that manages information about other clients. To do this, the application of the client first has to transmit information about the resources that it wants to provide to the server. Only after this step can an IT system usually access information about the other logged on clients. These include, for example, the IP address, the user, and the content provided. With the help of this information, a direct connection to the remote client can be established and its resources used. If the central server fails, the contact information of the connected IT systems is no longer available and the clients can no longer establish a data connection with each other. This results in the failure of the entire client-to-client network.
+ Decentralized client-to-client services:
Distributed client-to-client services do not require a central server that manages the connected users. The users of these services' IT systems establish data connections with each other to exchange information about the resources provided. Here, not only the resources of the IT systems, with which a connection is established directly, are searched, but also information about other clients, who in turn have established a data connection, are retrieved. Because each client can connect to multiple clients, a network is created that allows each client to retrieve information about the resources provided by other clients. These decentralized client-to-client services assume that the application must be set up with a client which is part of this network in order to become a member of the network. The required contact information must be known in advance. Since many networks benefit from a large amount of connected IT systems, this contact information is often published on websites.
+ Hybrid client-to-client services
Hybrid client-to-client services are similar to central client-to-client services, except that multiple independent servers can be used. As with core client-to-client services, clients provide a server with the resources they provide and contact information on how to reach them. The servers in turn share this information with other servers. If necessary, the clients can access the resources of other clients that are not managed by the same server.


 
** Alternatives for Using Client-to-Client Services **

Only a few services require client-to-client communication between IT systems. For example, resources can also be provided centrally by servers. Only by using servers can defaults be implemented centrally, for example, that only authorized persons may access the information. The following services, which typically can be distributed through client-to-client networks, can be centralized:

* Provision of printers
 If multiple people in a LAN need access to printers, they can be centrally provisioned in the network. This can be done with the use of network-capable printers or management via print servers (see SYS.4.1 Printers, Copiers and Multifunction Devices).
* File Sharing
 Instead of releasing memory on several clients in the LAN, the information can be stored centrally on a file server. If only users within a LAN can access the server, for example, Samba servers (see APP.3.4 Samba) or NFS servers (see SYS.1.3 server under Unix) can provide the information., General recommendations are in APP3.3 File server to find. If external users are also allowed to access the information, the information could be stored on an externally accessible web server (see APP.3.2 web server).
* Messaging
 If you need to send text messages and not use e-mail, consider using an instant messaging server, such as Jabber. Through this server, the messages could be centrally checked for malicious software.
 Communication with external contacts can also be achieved by means of a central instant messaging server operated by the institution and accessible both internally and externally. More detailed information can be found in APP.1.5 Instant Messaging
* VoIP (Voice over Internet Protocol) and Internet telephony
VoIP solutions, as described in the module NET.4.2 VoIP, differentiate between the signaling and the media transport. For the signaling often servers are required, on which the participants are managed. After initiating a conversation between two or more users via the signaling, many solutions exchange the voice information directly between the users. This type of client-to-client makes sense in a LAN and should be used.
 Client-to-client should not be used beyond the limits of a LAN for telephony, for example, an institution should not allow such communication to communicate with external parties ("Internet telephony"). Also in this case, both the signaling and the media transport on a concentrator, similar to a proxy, should be bundled. In this way, the direct connection establishment of individual clients to external call partners, which may be located on the Internet, for example, avoided.
** Recommendations for using local client-to-client services **

If possible, dedicated servers should be used to exchange information through client-to-client services rather than shares. In exceptional cases, however, the use of client-to-client solutions is necessary, such as in VoIP. Therefore it is necessary to specify:

* which client-to-client services are used and
* what information exchanged
be allowed to. If necessary, users should be trained to use client-to-client services. It is important to ensure that client-to-client services are limited to the LAN only.

** Recommendations for Using Client-to-Client Public Services **

In general, the uncontrolled flow of information from a LAN must be prevented. This includes direct client-to-client connections from clients to IT systems that are not on the LAN. Due to the lack of centralization, uncontrolled information can leave the LAN (eg confidential information) or get in (eg malware). The following actions can prevent the use of public client-to-client services:

* Local packet filter
 By using local packet filters, client communication can be restricted to a few IT systems (see SYS.2.1.M28 Local Packet Filter Setup). For example, the filter rules could be set so that only servers can communicate.
 Based on the IP address of the server and the port number of the permitted service, an undesirable communication setup can be made more difficult. By using local packet filters, both the use of local and public client-to-client networks can be prevented.
* Central filtering on the security gateway (firewall)
 In general, the security gateway should allow only the necessary communication to or from the local network, all other connections should be rejected (see NET.3.2 firewall). If the security gateway prevents the communication of the clients from the LAN with IT systems on the Internet, the use of public client-to-client networks can be prevented.
* Directive
 In addition to technical recommendations, employees of the institution should also be prohibited from using client-to-client services. This statement can be formulated in the security policy for users.
If client-to-client services are to be used in the institution, this must be decided by the executive level of the institution. The information security officer must be involved and the decision including the residual risks must be documented.

#### SYS.2.1.M24 Handling of removable media in the running system
Commercially available PCs today are usually equipped with a CD / DVD / Blu-ray drive or CD / DVD / Blu-ray burner, therefore, the recommendations of the module OPS.1.2.3 disk exchange and SYS. 3.4 Mobile data carriers are taken into account. In addition, it is possible to connect external storage media via interfaces that are automatically recognized and integrated by many operating systems. Examples include USB storage connected to the USB port and Firewire hard drives. In addition, card readers for memory cards are installed in many IT systems. Such drives for removable media and external data storage pose the following potential security issues:

* The IT system could be booted uncontrollably from such drives.
* Uncontrolled software could be imported from such drives.
* Data could be copied unauthorized to removable media.
When booting from removable media or installing third-party software, not only can security settings be overridden, but the IT system can become infected with computer viruses and other malware.

These dangers must be counteracted by appropriate organizational or technical security measures. For this purpose, various approaches are available whose specific advantages and disadvantages are briefly described below:

* Removal of drives
 Although the removal of drives for removable media (or the lack of procurement) provides the safest protection against the above-mentioned threats, but is usually associated with considerable effort. Often, a removal is not possible at all, eg. B. with memory card readers in notebooks. It should also be taken into account that the expansion may hinder the administration and maintenance of the IT system. This solution should be considered if special security requirements exist. If it is foreseeable that the drives for removable media are not needed, devices without built-in drives should be preferred when purchasing.
* Locking drives
 For some types of drives, there are lockable plug-in devices that can help prevent uncontrolled use. Procurement should ensure that the drive locks are suitable for the existing drives and can not damage them. It should be noted that locks are not offered for all types of drives, such as built-in memory card readers. In addition, care should be taken that the locks are offered by the manufacturer with a sufficient number of different keys. The disadvantage is the procurement costs for the drive locks and the cost of the required key management. Therefore, this solution makes sense only with higher protection requirements or special security requirements.
* Deactivation in the BIOS or operating system
 In the BIOS, most PCs provide options for booting from which drives. In conjunction with password protection of the BIOS settings, this can prevent the uncontrolled booting of removable media and mobile data carriers. Furthermore, the existing drives and interfaces can be disabled individually in modern operating systems.
The client can now be difficult to use without authorization because, for example, No external software can be installed by the removable media or information can be copied to it. Disabling the drives in the BIOS or operating system has the advantage that the hardware does not need to be changed. The corresponding settings in the operating system can possibly even be made centrally. For this procedure to be effective, it must be ensured that the users do not have the permissions in the operating system to undo the deactivation of the drives.
* Encryption
 There are products that ensure that only access to authorized mobile data carriers is possible. One solution, for example, is that only mobile data carriers that have been encrypted with certain cryptographic keys can be read and written. This not only protects against unauthorized access via manipulated mobile data carriers, but also protects the data on the mobile data carriers in the event of loss or theft.
* Guidelines for use
 In many cases, users may use the built-in drives for removable media or storage media on external interfaces, but use is governed by appropriate policies. On a technical level, booting removable media should then be disabled in the BIOS. Thus, it is not necessary to remove the drives, lock and disable the operating system.
 In this case, the guidelines for using the drives and storage media should be defined as explicitly as possible. For example, everything can generally be banned, non-public text documents may be copied. The policies must be made known to all users and compliance monitored. It should be prohibited to install and start programs that have been recorded by removable media, this should be technically prevented as much as possible.
 This purely organizational solution should only be chosen if users need to access the drives at least once in a while. Otherwise access should be prevented by technical measures as described above.
When selecting a suitable procedure, all drives for removable media must always be taken into account, as well as all options for exchanging data via networking, in particular e-mail and Internet connections. If the IT system is connected to the Internet, it is not enough to disable or extend all removable media drives. Particular attention is paid to the protection against malware, eg. Computer Viruses or Trojan Horses (see also SYS.2.1.M6 Use of Anti-Virus Programs).

Regardless of the selection of a suitable procedure, it should be prevented that contents of removable media are automatically executed when the media are connected. To do this, deactivate the corresponding autorun and autoplay functions of the operating system.

In order for the security measures to be accepted and respected, users must be informed and sensitized about the dangers of removable media drives.

** handling of USB devices **
Via the USB interface a variety of additional devices can be connected to PCs. Examples are hard disks, CD / DVD writers and USB sticks. Despite their large storage capacity, USB sticks are so handy that they can be produced, for example, in the form of key fobs and fit in any pocket. In modern operating systems, the drivers for USB mass storage devices are already integrated, so that no software installation is necessary for operation. In general, these recommendations are not specific to USB storage devices, but generally to all USB devices that can store data. Among other things, USB printers and USB cameras can be "misused" to store the data. This is especially true for "smart" devices with a USB port, which can accept any USB identity if they are equipped with special software. These can be programmable USB development boards, but even with many smartphones such use is possible.

USB storage media can be used to uncheck information and programs. Therefore, USB storage media should be treated in the same way as conventional storage media. It is very difficult to prevent the operation of USB storage media if the USB interface is used for other devices. For example, notebooks are delivered that only provide the USB interface for connecting a mouse. Therefore, it usually does not make sense to use a "USB lock" or disable the interface by other mechanical measures. The use of interfaces should therefore be regulated by granting appropriate rights at the level of the operating system or with the help of additional programs. Alternatively it can be monitored if devices are added. In order to connect data storage to external interfaces, drivers or kernel modules are often loaded by the operating system or entries in configuration files (such as the Windows registry) are generated which can be detected. After the changes have been detected, for example, a log file can be created or the IT operation can be notified. However, all this can only be achieved with the help of additional software. This requires either a proprietary development or a third-party product.

** handling of USB devices **

Via the USB interface a variety of additional devices can be connected to PCs. Examples are hard disks, CD / DVD writers and USB sticks. Despite their large storage capacity, USB sticks are so handy that they can be produced, for example, in the form of key fobs and fit in any pocket. In modern operating systems, the drivers for USB mass storage devices are already integrated, so that no software installation is necessary for operation. In general, these recommendations are not specific to USB storage devices, but generally to all USB devices that can store data. Among other things, USB printers and USB cameras can be "misused" to store the data. This is especially true for "smart" devices with a USB port, which can accept any USB identity if they are equipped with special software. These can be programmable USB development boards, but even with many smartphones such use is possible.
USB storage media can be used to uncheck information and programs. Therefore, USB storage media should be treated in the same way as conventional storage media. It is very difficult to prevent the operation of USB storage media if the USB interface is used for other devices. For example, notebooks are delivered that only provide the USB interface for connecting a mouse. Therefore, it usually does not make sense to use a "USB lock" or disable the interface by other mechanical measures. The use of interfaces should therefore be regulated by granting appropriate rights at the level of the operating system or with the help of additional programs. Alternatively it can be monitored if devices are added. In order to connect data storage to external interfaces, drivers or kernel modules are often loaded by the operating system or entries in configuration files (such as the Windows registry) are generated which can be detected. After the changes have been detected, for example, a log file can be created or the IT operation can be notified. However, all this can only be achieved with the help of additional software. This requires either a proprietary development or a third-party product.

#### SYS.2.1.M25 Secure IT Use Policy [User]

In order to promote the safe and proper use of information technology in larger companies or public authorities, a directive should be drawn up which sets out mandatory requirements, which boundary conditions must be adhered to and which security measures are to be taken. The policy should be made known to all users, for example in electronic form on an intranet server. Each new user must acknowledge the acknowledgment of the policy before being allowed to use the information technology. After major changes to the Directive or after two years at the latest, a new confirmation is required.

The following is a rough outline of what content is useful for such a policy:

** Objectives and Definitions **

The first part of the guideline serves to sensitize and motivate users for information security. At the same time, the necessary terms for common understanding are defined, such as: PC, server, network, users, users, vulnerable objects.

**Scope**

This part must specify which parts of the company or authority the Directive applies to.

** Legislation and internal regulations **

Here is an overview of which key legislation, eg. B. the Federal Data Protection Act and the Copyright Act, are to be observed. Using examples, it should be made clear what effects this has on the use of information technology in the respective environment. In addition, this position can be used to list all relevant company-internal regulations.

** responsibility distribution **

In this part, it is defined which function carrier has to bear some responsibility in connection with the use of IT. In particular, the roles of user, supervisor, IT operation, auditor, data protection officer and security management team must be differentiated.

**Contact Person**

The policy should include contacts and contact information (telephone, e-mail, etc.) for users on information security issues or where this information can be found. It should be noted that confusion often results when users are given too many different contacts. It is usually better to name only a few different contact persons, who then refer the users to the right place if necessary (help-desk concept).

** Security measures to be implemented and adhered to **
The last part of the IT usage policy is to determine what security measures the user should follow or implement. Depending on the need for protection, this can also go beyond the IT-Grundschutz measures. Typical examples of security measures in the workplace are the secure login and logout on the PC, the proper handling of passwords and rules of conduct for the use of the Internet.

If teleworkers are employed in the company or in the authority, the directive should be supplemented with teleworking-specific regulations.

#### SYS.2.1.M26 Protection of applications

In order to be able to react to critical system events, a suitable system monitoring or monitoring concept should be created for clients. This includes that the system status and functionality of the clients are constantly monitored. If errors occur or defined limit values ​​are exceeded or undershot, this should be reported automatically to the operating personnel.

For this purpose, status information is usually retrieved from a central IT system on which the events are evaluated. However, the interface needed to retrieve the system events from the IT system can often change system settings of the operating system, e.g. Via SNMP (Simple Network Management Protocol). If such a modification is not desired, then these features should be disabled.

#### SYS.2.1.M27 Controlled decommissioning of a client

When decommissioning a client, it must first of all be ensured that

* no important data that may be stored on the client is lost, and that
* no sensitive data remain on the data media of the client.
In particular, it is important to have an overview of what data is stored on the IT systems.

* Data backup
 Before decommissioning the client, locally stored data that is still needed must be either externally backed up or archived (for example, on external hard drives, CDs or DVDs) or transferred to a backup or file server. After the backup, it should be checked that all data has been backed up correctly.
 In this context, it may be useful to provide users with a suitable drive, such as an external CD or DVD burner, for backing up any stored local data.
 Further information on this topic can be found in SYS.2.1.M4 Regular data backup as well as the blocks OPS.1.1.5 Data backup and OPS.1.1.2 Archiving.
* Dismiss the IT system from directory services and databases
 Any authorizations in the network that are linked to the client itself (and not to a user) must be deleted. Examples include entries on proxy servers on the security gateway or access rights to network services that are granted based on the IP address. If the client is entered in network-wide directory services or databases (for example in a Windows domain, Active Directory, NIS or similar), the associated entries must be deleted or at least the corresponding identifiers must be deactivated.
* Delete the data on the IT system
 It must be ensured that no more valuable information is available on the hard disks. It is not enough just to reformat the disks, but they have to be completely overwritten at least once. It should be noted that neither deleting the operating system deletion nor reformatting the disks actually removes the data from the disks. With suitable software, data can be reconstructed in such cases, often without much effort.
SSDs can not be overwritten effectively due to wear leveling and reserve capacity, and the expected remaining life of the SSD is reduced. For SSDs, it is better to use the SECURE ERASE functionality provided by the SSD and then check the result.
* Delete backup media
 After decommissioning the IT systems, the corresponding data backup media may also have to be deleted if the data stored on them is no longer needed.
* Remove any other information
 If potentially sensitive data (for example certain configuration data) are stored on a client at locations other than on the hard disk (such as in a non-volatile memory), these must also be removed before the device is transferred.
It is recommended to use the above recommendations to create a checklist that can be run when the IT system is decommissioned. In this way it can be avoided that individual steps are forgotten. In-depth information can also be found in OPS.1.2.7 Sale / Disposal of IT.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### SYS.2.1.M28 Encryption of clients (C)

Confidential information on data media can be encrypted in various ways and thus protected against unauthorized access. For example, the entire volume, a single partition or just individual files can be encrypted. From a security point of view, it is better to encrypt the entire data carrier, since then less user intervention is required and all data is protected against unauthorized access. Encrypting an entire volume or partition is almost transparent to users. Only when booting or the first access to the partition, the user must authenticate. If only individual files or file containers are encrypted, there is a risk of accidentally storing sensitive data in unencrypted areas of the hard disk. In addition, an encryption program must be explicitly started by the users.

Even if individual partitions are completely encrypted, this can lead to confidential information ending up on unencrypted partitions for various reasons. Therefore, full encryption of media is the best and most efficient way to reliably protect sensitive data from unauthorized access.

Disk encryption can be implemented with software, but also with hardware support. Software solutions are BitLocker from Microsoft or appropriate open source programs, such as dm-crypt or Veracrypt.

Mobile data carriers, such as USB sticks and laptops, should always be completely encrypted, even if they are occasionally used for confidential information. In the case of stationary IT systems, the data carriers should be completely encrypted if confidentiality requirements are high.
In addition to the encryption program (see section "Using an encryption product") itself, the encryption keys still require the cryptographic keys. The cryptographic keys should be properly created and kept separate from the encrypted volume. For this example, smart cards or USB tokens can be used. Such a separation is usually not possible with the encryption of USB sticks, which should be taken into account in the security analysis. Further information can be found in CON.1 Crypto Concept.

Of course, the data stored on the encrypted volumes must also be backed up regularly.

Some disk or partition encryption programs or the use of encrypted file containers offer the option of "hiding" the encrypted areas. Since such functions are difficult to apply and misoperation can lead to complete data loss, they should only be used in special cases.

For in-depth information about hard disk encryption, see [NIST800111].

** Use of an encryption product **

In order to avoid the need to retrieve sensitive data from a portable IT system stolen despite all precautionary measures, an encryption program or an existing operating system function should be used. With the help of the marketable products, it is possible to encrypt individual files, certain areas or the entire hard disk in such a way that only the one who has the secret key is able to read and use the data.

The security of the encryption depends on three different points centrally:

* The encryption algorithm used must be designed so that it is not possible to reconstruct the plaintext from the encrypted text without knowing the key used. Not possible in this case means that the effort required to break the algorithm or decode the proof test in no relation to the information gain that can be achieved thereby.
* The key is suitable to choose. If possible, a key should be generated randomly.
* The encryption algorithm, the encrypted files and the keys must not be stored together on a data medium. It is advisable to keep the key individually. The cryptographic keys should be stored on a removable medium such as a hard disk. On chip card or USB stick, and stored separately from the portable IT system (eg in the wallet).
Encryption can be done online or offline. Online means that all hard drive (or partition) data is encrypted without the user having to actively do so. Offline encryption is explicitly initiated by the user. He then has to decide which files should be encrypted.

** Self-encrypting disks **

To prevent unauthorized access to confidential data on hard drives, they should be completely encrypted if possible. There are hardware- and software-based encryption methods, at this point the hardware-based encryption is handled in the form of self-encrypting hard disks ("Self-Encrypting Device", SED). SEDs access a special hardware crypto controller for encryption and are therefore very performant. The encryption solutions used often only provide that they are only used by one user; multi-user solutions are generally not provided.
Using self-encrypting disks, the IT system may no longer be susceptible to memory because all data is encrypted when the disk is shut down and a key stored in RAM poses a security risk. This is to be considered before use.

Self-encrypting hard drives should not be combined with a TPM module because such a combination usually does not provide the ability to decrypt the hard drive in another IT system with a master key. If the IT system is damaged in such a case, the data on the hard disk can no longer be decrypted because the hard disk is firmly interwoven with the IT system thanks to the TPM module.

Self-encrypting hard drives typically use AES. The key with which the information is encrypted is the so-called "Data Encryption Key" (DEK). Care should be taken to ensure that the DEK is only in the crypto controller and that it is specially protected against manipulation (for example read-out). The DEK should be generated based on random hardware events. This DEK is encrypted with an "Authentication Key" (AK). The AK is typically generated by the user by choosing a password. With some self-encrypting hard disks, the AK can also be stored on a token, for example a chip card or a stick, and additionally encrypted with a password. This allows the implementation of a two-factor authentication.

In addition to the DEK and AK, there is usually also a master key, which allows to decrypt the data, even if the password or token was lost. Such a key must be created during installation and kept safe in case the password or token is lost. It is necessary to regulate how organizational is done when a user forgets the password to an encrypted hard disk. In this case, the password must be reset with the master key and the user must set a new password.

If the user has successfully authenticated, the DEK is decrypted. With the DEK, all data on the hard disk is encrypted and encrypted, without the user noticing anything of it during operation. If the computer shuts down or if the drive integration of the SED is solved, all data is encrypted with the DEK and the DEK with the AK.

In general, the key length used for the encryption process used by the hard disk should be sufficiently long. Care should be taken to operate the encryption algorithm in a secure disk encryption mode. Otherwise, decryption can cause problems if the ciphertext is moved between two sectors.

Before self-encrypting hard disks are procured, it should be checked whether the hard disks are compatible with the other hardware of the IT system. Furthermore, it should be checked whether the read and write rate of the selected hard disk is appropriate. In addition, it should be checked whether further boundary conditions for use in the IT system must be met. For example, very few models of self-encrypting hard drives can be integrated into an existing "single-sign-on" architecture. It should also be checked whether and how IT systems can be migrated with normal hard disks to self-encrypting hard disks (with a supplied program or via a new installation).
The installation of a self-encrypting hard disk should be done in institutions by trained administrators. To do this, they first have to create a new DEK and assign a password and create a master key that must be stored safely. The DEK start password must first be changed by the user of the client to a secure password.

If a self-encrypting hard drive is repaired or should it be sold or disposed of, it must be ensured that it can not be extracted from any valuable information. To do this, the DEK should be regenerated before repair, sale or disposal, or a deletion command "ATA Secure Erase" should be executed.

#### SYS.2.1.M29 System Monitoring (A)

In order to be able to react to critical system events, a suitable system monitoring or monitoring concept should be created for clients. This includes that the system status and functionality of the clients are constantly monitored. If errors occur or defined limit values ​​are exceeded or undershot, this should be reported automatically to the operating personnel.

For this purpose, status information is usually retrieved from a central IT system on which the events are evaluated. However, the interface needed to retrieve the system events from the IT system can often change system settings of the operating system, e.g. Via SNMP (Simple Network Management Protocol). If such a modification is not desired, then these features should be disabled.

#### SYS.2.1.M30 Setting Up a Client Reference Installation (CIA)

It is recommended to create a reference installation for clients in which the basic configuration and all configuration changes, updates and patches can be pre-tested by the users before importing them to the clients. This concerns the basic settings of the IT system, security patches and updates as well as normal updates issued by the manufacturer.

In addition, such a reference installation may also be used to facilitate the installation or re-instalation of clients by appropriately cloning a suitably preconfigured installation onto the client to be installed ("cloning"). Ideally, then only a few settings need to be adjusted. A reference installation that is used to clone clients must be configured and tested with great care.

The reference installation must be such that the essential parameters of the hardware and software platform are the same for all IT systems derived from this reference installation. This does not necessarily mean that an identical hardware and software configuration must exist on all clients. However, the configuration of different clients must be sufficiently similar in order to maintain the reference character of the installation.

In addition, when testing application programs and settings that affect users on the clients, IT operations do not do so with administrator privileges, but under a user ID that has the same privileges and the same settings for the user environment as the users who should work with the IT system.
Optionally, it may be advantageous to use different test systems for different types of tests, such as one or more IT systems for device driver or low-level program testing and operating system patches, and another for application program testing. In such a case, however, it is important to be aware that in this way certain types of interactions between operating system environment and application programs can not be covered. In the case of special demands on the security of the clients, it may therefore be necessary to use only identically equipped and configured IT systems for specific deployment scenarios.

For several typical and more frequently recurring test cases, checklists should be created that can be executed during testing and which, in addition to the pure documentation of the test, can often also contribute to increasing efficiency and avoiding errors.

All tests should be documented so that they can be retraced at a later date. This is especially necessary when testing security updates and new device drivers where improper configuration or failure of the installation can cause the affected clients to lose access to the network or even stop booting. Especially in such cases, a meaningful documentation can significantly reduce the time required for troubleshooting.

#### SYS.2.1.M31 Local packet filter (CIA) setup

The entire network of an institution should be protected by an appropriate security gateway. In addition, it is recommended to set up appropriate access restrictions at application or network level on each client.

A local packet filter can protect a client against attacks launched from the same subnet. In addition, such a packet filter can be used to realize a finer graded access control for individual services than is possible, for example, with packet filters only at gateways.

In addition, a local packet filter can also be used to restrict outgoing network connections and thus limit the consequences of compromising the IT systems. While such protection may be disabled by an attacker after a successful compromise of the client, on the other hand, an attacker is at least hindered in this way. In this way, crucial time can be gained in the discovery and possible reactions.

Lastly, the log function of a local packet filter can allow certain attacks to be detected at all.

Virtually all current operating systems provide the ability to define filters that examine and handle all packets received or to be sent according to specific rules. The filter options differ considerably between the individual operating systems. Practically, however, rules can be defined based on the source and destination address of the packet as well as the type of protocol used (TCP / IP, UDP / IP, ICMP, etc.) and, if applicable, the source or destination port. With the help of packet filter rules, for example, packets originating from specific IT systems or from certain subnets can be purposefully discarded.

Some applications have their own mechanisms to allow or deny access to the service for individual IP addresses or ranges of addresses. In contrast to these mechanisms, a local packet filter at the operating system level has the advantage of protecting the service itself against possible attacks that result in compromise before the built-in access restriction can even take effect.
There are two general strategies that can be used to implement packet filtering rules: The blacklist strategy allows all kinds of connections that do not meet certain exclusion criteria (Floating strategy: "Everything is allowed, which is not explicitly forbidden"). The advantage lies in a possibly lower effort in administration and troubleshooting. A serious drawback, however, is that forgotten rules that allow access to unprotected network services can serve as the basis for an attack.

In contrast, the whitelist strategy blocks all types of connections that do not belong to a list of allowed services (Restrictive strategy: "Everything is forbidden, which is not explicitly allowed").

The whitelist strategy offers greater security and should therefore be used in principle unless there are important reasons against it. The disadvantage lies in the fact that administration costs tend to be higher because new rules have to be defined each time the requirements change. In exceptional cases, for example if a protocol does not work on firmly defined ports, the blacklist strategy can be used.

It is recommended that clients that have special security requirements set up a local packet filter with a basic set of rules in the basic configuration, which basically rejects all connection requests from the outside. This policy should be active when the client is connected to the network. Depending on which services are to be used by the client, after their configuration, the required protocols and ports can be unlocked.

Packet filters usually allow detailed logging of network traffic. Setting up a local packet filter is therefore also useful in secure networks that are separated with a security gateway from an insecure network such as the Internet, because recovered information can be helpful in detecting attacks. However, care must be taken to ensure that no privacy policy is violated. Where appropriate, the relevant bodies (data protection officers, staff representatives or others) should be involved.

** Problem ICMP **

The Internet Control Message Protocol (ICMP) is used to transmit messages about errors in the transmission of IP packets. For example, there are messages that tell the sender of a packet that the destination network is unreachable or that the packet was too large to be forwarded to the destination system. The function of the tools ping and traceroute are also based on ICMP.

However, in addition to many useful features, there are some ICMP message types that allow attackers to gain important information about a network and use it directly for attacks. Unfortunately, the radical approach to blocking ICMP on the security gateway is also not a satisfactory solution, as certain features are no longer available. Although ping and traceroute can typically do away with normal workstations and servers, global blocking of ICMP can lead to impairments that are difficult to diagnose. Therefore, consideration should be given to both the security gateway and the local packet filter for selective ICMP filtering, provided it provides the appropriate capabilities. This should always be done taking into account the purpose of the client, its need for protection and the measures taken at the security gateway. For example, a larger number of message types may be allowed for the internal network than for the external network.

** implementation and review **
The possibilities of filtering and logging differ depending on the operating system. Before setting up a local packet filter, refer to the existing documentation.

Care should be taken when setting up packet filter rules, as a rule rule might cause an administrator working over the network on the client to "lock out" and correct from the system console must make out.

After activating the local packet filter, on the one hand, it should be checked whether the required services are still reachable, on the other hand, a port scan should be used to check whether the remaining ports are all blocked.

#### SYS.2.1.M32 Use of Additional Exploits Prevention (CIA)

Depending on which security requirements are placed on an IT system, the existing security functionalities may not be sufficient, so that suitable security products should also be used. Typical examples are access control, access rights management and verification, logging or encryption.

For IT systems, for example, it must be ensured that

* only authorized persons can use the IT system. For this purpose, suitable authentication mechanisms must be selected.
* Users can access the data only in the way they need to accomplish their task. This support suitable user separation and rights assignment.
* Irregularities and manipulation attempts become recognizable. This is supported by logging, encryption and digital signature.
* Data is protected against accidental destruction or loss (availability control). For example, backup programs support this.
If the logging options of the IT system are insufficient to ensure sufficient evidence, they must be retrofitted. There are also various laws that require this. For example, under BDSG's input control, "it must be ensured that it can be subsequently verified and ascertained whether and by whom personal data has been entered, altered or removed in data processing systems".

If it is not possible with the IT system to prevent the administrator from accessing certain data or at least to log and control this access, then, for example, For example, encryption of the data prevents the administrator from reading this data in plain text if he does not possess the corresponding key.

** Recommended minimum functionalities **

IT systems should have at least the following security features. If these are not available as standard, they should be retrofitted with additional security products.

* Identification and authentication: There should be a lock on the IT system after a specified number of failed authentication attempts, which only the IT operation can reset. If a password is used, the password should be at least eight digits long and should not be stored unencrypted in the IT systems.
* Rights management and control: There should be a rights management and control on hard disks and files, with at least between reading and writing access to be distinguished. For users, system access at the operating system level should not be possible.
* Role separation between administrator and user: There should be a clear separation between administrator and user, whereby only the administrator should be able to assign or revoke rights.
* Logging of the processes Login, Logout and Rights violation should be possible.
If one or more of these security features are not supported by the operating system, appropriate additional security products must be used as a substitute.

Additional requirements for security products:

* User-friendly interface to increase acceptance.
* Meaningful and comprehensible documentation for IT operations and users.
Desirable additional functionality of security products:

* Role separation between administrator, auditor and user; Only the administrator can assign or revoke privileges and only the auditor has access to the log data.
* Logging of administrative activities,
* Support of log evaluation through configurable filter functions,
* Encryption of the data with an appropriate encryption algorithm and in such a way that data loss in case of malfunction (power failure, abort) is intercepted by the system.
The realization of this functionality can be done both in hardware and in software. When purchasing a new product, module OPS.1.2.6 Procurement, Tendering and Purchasing should be taken into account.

** temporary solution **

If it is not possible to obtain a suitable security product at short notice, other suitable security measures must be taken. These are then typically organizational in nature and must be consistently adhered to by the users. For example, if an IT system does not have a screen lock, it must be locked in or out during the short periods when it is not in use.

#### SYS.2.1.M33 Application Whitelisting (CIA)

Basically, clients need only be able to run applications that are necessary for the services offered to work. Corresponding whitelist solutions can ensure that only permitted programs can be executed. There are proprietary mechanisms and third-party solutions that can be used to implement whitelisting.

A simple approach is path-based application whitelisting for full paths. For example, program directories or directories with operating system files are allowed. This can prevent a malicious program from being executed from the browser cache or a temporary folder.

Alternatively, the execution can be explicitly allowed for individual applications. This approach adds security, as only pre-defined applications can be started. At the same time, however, the effort increases because z. B. must be ensured that all necessary operating system components can be executed. Even with updates, additional effort is needed to update changed programs in the whitelist.

For whitelisting it should be noted that e.g. Scripts may not be executed.

#### SYS.2.1.M34 Use of Application Isolation (CIA)

The different operating systems offer different ways to isolate applications. These include container solutions such as AppContainer (Windows), Linux Containers (LXC) or Docker as well as with the operating systems supplied virtualization solutions such as Hyper-V (Windows), KVM / Xen (Linux), VMware Workstation or Virtualbox. In addition, specialized solutions from third-party manufacturers can be used. This has the advantage that applications that open Internet content or data from external sites can gain significant security through isolation. This includes z. For example, web browsers, office applications, e-mail programs, and PDF viewers.

#### SYS.2.1.M35 Active Management of Root Certificates (CI)

Further information on the management of root certificates can be found in the following documents:

* Windows: Configure Trusted Roots and Disallowed Certificates [MSROOT
* Mozilla: CA: Root Change Process [MOZRCP]
* Java: keytool - Key and Certificate Management Tool [KEYTOOL]
* OpenSSL: Certificate Installation with OpenSSL [OPENSSL]
* GnuPG: Agent Configuration - Using the GNU Privacy [GNUPG]
#### SYS.2.1.M36 Self-managed use of SecureBoot and TPM

On UEFI-compliant systems, the boot loader, kernel, and any required firmware components should be signed by self-controlled key material and any unneeded key material should be removed. Unless the TPM is needed, it should be disabled.

#### SYS.2.1.M37 Protection against unauthorized applications (CIA)

To prevent access to the system through compromised credentials, multi-factor authentication should be used.

#### SYS.2.1.M38 Integration into contingency planning (A)

In the context of emergency preparedness, a concept should be drafted to minimize the consequences of a failure and what to do in the event of a failure.

The following aspects have to be considered:

* The contingency planning for the clients should be integrated into the existing emergency plan (see also module DER.4 Emergency Management).
* Data may be lost due to a system failure. For this reason, as part of the general data protection concept (see also OPS.1.1.5 Data backup), a data protection concept must be created for the clients.
* Within the scope of maintenance and service contracts or own warehousing, the supply of spare parts must be ensured within a period of time.
* The system configuration must be documented. Important tasks must be described so that the entire system can be restored in an emergency even without prior knowledge of this system configuration.
** Creating an Emergency Boot Medium **

If a client is set up, a boot medium should be created directly. In this way, the IT system can be started if a hard disk fails and it can also be used to restore a controlled system state after e.g. a malicious program has occurred. Such media may for example be DVDs that are created by the respective operating system, but it can also be specially created DVDs or portable drives (for example, USB sticks or external hard drives) are created. The nature and extent of the emergency boot medium depends on the purpose of the client and the existing interfaces.

The emergency boot medium can be used for problems such as:

* Data loss due to operating errors,
* Operating and administration errors that prevent use and reboot
Infection of the IT system with malicious programs (such as computer viruses)
* Compromising the IT system by an attacker, or even
* Hardware problems.
Ideally, the emergency boot media should contain all the programs and data needed to inspect the IT system and troubleshoot problems. If necessary, different media can be created for different problem scenarios.

The following programs are recommended as the "basic configuration" for an emergency boot medium:

* Virus protection programs with up-to-date signatures,
* Programs for editing configuration files or databases of the IT system (editors for files, registry or similar),
* Programs to restore system disk data structures such as boot sector and MBR (Master Boot Record) or GPT (GUID Partition Table),
* Backup / recovery programs,
* Diagnostic programs to analyze hardware defects.
In addition, programs can be added for further analysis, for example to forensically investigate compromised IT systems.
It is important that all programs and libraries are loaded exclusively from the boot medium. No components of the installed IT system may be used. If a boot medium is created, it is also important to ensure that in addition to the necessary programs, there are also all the drivers needed to access the client's built-in disks. These include, for example, drivers for hard disk controllers (especially RAID controllers) and drivers for hard disk encryption or hard disk compression.

If the boot media provides enough space, additional programs or documentation can be stored on the media. For example, it can increase the efficiency of debugging if there is always up-to-date documentation of the system configuration on the boot media.

The emergency boot medium itself must be free from viruses and other malicious programs. For this reason, only programs originating from trustworthy sources (eg directly from the manufacturer's CD / DVD) or whose digital signature has been checked may be used. After the boot media is created and changed, it should also be scanned with a virus protection program.

It is not absolutely necessary to create a separate boot medium for each IT system. A suitably flexible boot medium can be sufficient for a large number of different IT systems. Not even the same operating system needs to be deployed on the boot medium as on the target system itself. However, for compatibility reasons, this is often beneficial. However, it must be ensured by appropriate tests that the medium really works for all clients for which it is to be used. Depending on the operating system, system-specific aspects must also be considered, which are described in the respective IT-Grundschutz modules.

If the target system has changed, for example after an operating system update or configuration changes, the emergency boot medium and the documentation stored thereon may need to be updated. If the boot medium is changed, this must be documented.

The emergency boot medium must be quickly accessible to system administrators so that valuable time is not lost in the event of a malfunction. On the other hand, it must also be kept safe so that unauthorized persons have no access to it.

The emergency boot media function should be tested regularly and the operation of the programs stored on it should be checked to ensure that the media is functioning in the event of problems and the IT operations are familiar with the operation. It should be considered to keep a short printed manual with the medium, which summarizes the most important steps for typical application scenarios.

#### SYS.2.1.M39 Uninterruptible and Stable Power Supply [Home Automation] (A)

If there are increased availability requirements for clients, they should be connected to an uninterruptible power supply (UPS) so that power outages can be bypassed until either the (backup) power supply is restored or the clients are shut down in an orderly manner. More detailed information about an uninterruptible and stable power supply can be found in the module and the implementation notes for the SYS.1.1 General Server.

#### SYS.2.1.M40 Operation Documentation

To ensure a smooth flow of operations, administrators need to have an overview of the IT systems. This must also be possible for their representatives if an administrator fails unexpectedly. The overview is often required to check the IT systems (eg for problematic settings, consistency in case of changes).
Therefore, the changes that administrators make to the IT systems should be documented, if possible automated. This applies in particular to changes to system directories and files.

When installing new operating systems or updating, the changes made must be documented with particular care. By activating new system parameters or changing existing ones, the behavior of an IT system (especially security functions) can be significantly changed.

#### SYS.2.1.M41 Preventing local disk overload

It should be considered setting up Quotas. Alternatively, mechanisms of the file or operating system used should be used, which warn the user at a certain fill level of the hard disk or only grant the system administrator write access.

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Further information on threats and security measures in the "General Client" area can be found in the following publications, among others:

* #### [GNUPG] Using the GNU Privacy Guard

  

 Agent Configuration, (last accessed 05.10.2017)
 <Https://www.gnupg.org/documentation/manuals/gnupg/Agent-Configuration.html>

 
* #### [ISiClient] Securing a PC client (ISi client),

  

 (last accessed on 27.09.2017)
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/Isi-Reihe/Isi-Client/client\_node.html](https://www.bsi.bund.de/DE/Themen/ standard criteria / Isi-series / Isi client / client_node.html)

 
* #### [KEYTOOL] Key and Certificate Management Tool

  

 Oracle, (last accessed 05.10.2017)
 <Https://docs.oracle.com/javase/6/docs/technotes/tools/windows/keytool.html>

 
* #### [MIGLFTLS] Minimum TLS 1.2 Migration Guide

  

 Federal Office for Security in Information Technology, as of 2015
 [Https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Migrationsleitfaden\_Mindeststandard\_BSI\_TLS\_1\_2\_Version\_1\_2.pdf](https://www. bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Migrationsleitfaden_Mindeststandard_BSI_TLS_1_2_Version_1_2.pdf)

 
* #### [MOZRCP] Mozilla CA: Root Change Process

  

 Mozilla Wiki, (last accessed 05.10.2017)
 [Https://wiki.mozilla.org/CA:Root\_Change\_Process](https://wiki.mozilla.org/CA:Root_Change_Process)

 
* #### [MSROOT] Configure Trusted Roots and Disallowed Certificates

  

 Configure Trusted Roots and Disallowed Certificates, (last accessed 05.10.2017)
 <Https://technet.microsoft.com/en-us/library/dn265983 (v = ws.11) .aspx>

 
* #### [NIST800111] NIST Special Publication 800-111

  

 Guide to Storage Encryption Technologies for End User Devices, 2007
 <Http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-111.pdf>

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008
 <Https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf>

 
* #### [OPENSSL] Certificate Installation with OpenSSL- Other People's Certificates

  

 (last accessed 05.10.2017)
 <Http://gagravarr.org/writing/opensslcerts/other.shtml>

 
* #### [RFC5246] RFC 5246, The Transport Layer Security (TLS) Protocol

  

 Internet Engineering Task Force (IETF), (last viewed 05.10.2017)
 <Https://tools.ietf.org/html/rfc5>

 
* #### [RFC5746] RFC 5746, Transport Layer Security (TLS) Renegotiation Indication Extension

  

 Internet Engineering Task Force (IETF), (last accessed 05.10.2017)
 <Https://tools.ietf.org/html/rfc5746>

 
* #### [TR02102] Cryptographic method recommendations and key lengths

  

 BSI, (last accessed on 27.09.2017)
[Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)
