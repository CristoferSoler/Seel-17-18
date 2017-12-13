1 description
--------------

### 1.1 Introduction

In every institution there are legal, contractual, structural and internal guidelines and guidelines that have to be observed from many different directions. Many of them have a direct or indirect impact on information security management. The requirements vary depending on industry, country and other conditions. For example, an authority is subject to other external regulations than a stock corporation. The management level of the institution must ensure compliance with the requirements through appropriate monitoring measures (New German: Compliance) and operate a compliance management system.

The aim of compliance management is to have an overview of the various requirements of the individual areas of the institution at all times and to identify and implement suitable measures to avoid violations of these requirements.

This task is typically delegated to an employee. The role is referred to below as "Compliance Manager". For example, in some companies, B. also the term "request manager" used. Unless otherwise required, no new posts need to be created. The task can be taken over, for example, by security management, auditing, controlling or the legal department.

Depending on the size of an institution, it may have different management processes that deal with different aspects of risk management, such as: Security management, privacy management, compliance management, controlling. They should work together in a spirit of trust in order to exploit synergy effects and resolve conflicts at an early stage.

### 1.2 Life cycle

Within the framework of compliance management, a series of measures has to be implemented, beginning with the conception through the development of suitable organizational structures up to the regular revision. The steps to be taken and the actions to follow in each step are listed below.

** planning and conception **

Processes and organizational structures should be established to ensure an overview of the various requirements (see ORP.5.A4 Conception and Organization of Compliance Management). In addition to the external regulations affecting the institution, the internal guidelines and requirements must also be defined and transparent. An important basis for adequately securing all business-relevant information, business processes and systems is the classification of their protection needs (see ORP.5.A10 Classification of Information). As a result, specific security requirements for these objects are derived.

**Implementation**

The identified requirements are implemented through the management processes of the institution, in particular through the security process. Employees, as well as visitors and external service providers, must be made aware of their due diligence obligations and the measures to be followed in dealing with information and IT systems before gaining access to or accessing them (see ORP.5.A3 Employees' Obligation to Adhere to Relevant Laws, Rules and regulations).

**Business**

The security requirements that the institution has established to meet the requirements must be permanently adhered to. This should be reviewed regularly (see ORP.5.A7 maintaining information security). Both your own regulations and the legal framework to which an institution is subject may change. This must be taken into account within the scope of compliance management (see ORP.5.A2 Compliance with legal framework conditions).

2 measures
-----------
The following are specific implementation notes in the section "Compliance Management".

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### ORP.5.M1 Identification of the legal framework [Head of Organization, Head of Institution]

A server must always be installed or installed in a lockable computer room or server cabinet. It is to be regulated who receives access to the room or access to the server itself. For this purpose, the requirements of the modules INF.5 technical room, INF.6 protective cabinet or data center must be implemented.

#### ORP.5.M2 Observance of legal framework conditions [Supervisors, Head of Organization, Institution Management]

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

#### ORP.5.M3 Commitment of Employees to Compliance with Relevant Laws, Rules and Regulations [Supervisors, Human Resources Department]
Access rights to files that are stored on the data carriers of the server must be assigned restrictively. Users are only allowed access to the files they need to complete their tasks. The access right itself is limited to the required access type (see "Allocation of access authorizations"). For example, it is rarely necessary to assign a write permission to program files.

In most cases, the inheritance of rights to files in subdirectories may be accessed if an access right to the parent directory existed. As a result, top-level access (volume level) should be granted only very restrictively. In particular, when installing new software products, the assignment of rights must be subject to strict control.

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
By division of tasks, regulations and agreement it must be ensured that administrators do not inconsistent or incomplete interventions. For example, a file may not be edited and changed by several administrators at the same time, as only the last saved version will be preserved.

For all administrators, additional user IDs should be set up that have only the limited rights administrators require to perform administrative tasks. For non-administration work, administrators must use only these additional user identifiers.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the area of ​​"compliance management".

#### ORP.5.M4 Conception and Organization of Compliance Management [Head of Institution]

Basically, a distinction can be made between identifiers for users and administrators. Only administrators manage the IT systems, while normal user IDs only have the rights to perform their work-specific tasks. Normal user IDs may not have administration rights to protect the operating system and client configuration from accidental, negligent or intentional modification by the user.

If users only need to perform certain administrative tasks, it is often not necessary to give them all rights associated with their own login or even system administrator rights. Examples include certain routine system administration activities, such as creating backups or setting up a new user menu-driven with a program, or activities that require a user to have only a single application program. In particular for temporary staff and external service providers, care should be taken that they only use the services and only access the data they actually need. When their activity is over, their accounts should be disabled and all access permissions removed.

For these users, a limited user environment should be created. For example, it can be implemented under Unix by a restricted shell (rsh) and a restriction of the access paths with the Unix command chroot. Another possibility is to run individual application programs, such as web browsers, in the so-called kiosk mode, so that there is only limited access.

If particularly extensive rights are assigned to user IDs, this should be as restrictive as possible. On the one hand the circle of privileged users should be restricted as far as possible and on the other hand only the rights needed for the execution of the work should be assigned. For all tasks that can be performed without extended rights, privileged users should also work under identifiers with standard rights.

#### ORP.5.M5 Exemptions [Supervisors, Information Security Officer (ISB)]

There are different access options to administrate servers. Depending on the type of access used, a number of security precautions must be taken. For larger networks, it is recommended to integrate the servers in a central network management system, since otherwise a secure and efficient administration can hardly be guaranteed. The methods used for administration must be defined in the security policy and the administration must be performed only in accordance with the security policy.

In general, it is important to get an overview of what part of the administration of a server is normally

* locally via the console,
* remotely over the network, but using the standard mechanisms of the operating system, or
* via a central network-based administration tool
should be carried out. It is recommended to provide an overview of the various types of use, which administration activities can be carried out by which route. In particular, it is important to note whether certain activities can not normally be carried out in a particular way.

* Local AdministrationA server should be installed in a server room or at least a lockable server cabinet. For the part of the administration, which should or must be done partially locally via the console, appropriate specifications must be made for who gets access to the console, which type of authentication may be used for local access and which other requirements must be taken into account.
* Remote AdministrationMost a server is not administered locally at the console but from a workstation over the network. In order to prevent authentication information of the administrators and configuration data of the servers from being intercepted or even manipulated by an attacker, the administration should only take place via secure protocols (for example, not via Telnet, but via SSH, not via HTTP but via HTTPS). Alternatively, a separate administration network can be set up that is separate from the rest of the network. Unsecured remote administration over external (insecure) networks must never take place. This must already be taken into account when establishing the security policy. Also in the internal network, as far as possible, no unsafe protocols should be used.
* Administration via a central management systemIf a central management system is to be used for the administration of the server, analogous considerations should be made for this access channel, as for remote administration. In addition, it is important that the central management system itself be configured and administered accordingly.
** secure authentication **

In principle, IT systems should ensure that all users who want to access them have to authenticate themselves. This is the only way to prevent unauthorized persons from gaining access to the services offered by the system or to the data stored on the system.

As a rule, servers are administered via a network connection. The information needed for network-based authentication must be transmitted over a LAN or WAN. Therefore, it is imperative that this information can not be read or changed.

It must also be ensured that an attacker can not log in by replaying recorded credentials. Therefore, the credentials that are exchanged for authentication between server and client must be encrypted and additionally dynamized, for example with challenge-response methods.

After the authentication has been successfully completed, the system must ensure that users only have access to those services and data for which they have appropriate permissions.

If there is a danger of listening to lines to terminals, administrators should only work on the console so that passwords can not be intercepted. When administering Unix systems, encrypted communication can be done using the Secure Shell protocol, for example. This allows secure administration from remote workstations.

#### ORP.5.M6 Instructing the staff in the safe handling of IT [Supervisors, Human Resources]
The standard installation of an operating system often includes a number of programs and services that are not normally needed and that can be a source of security vulnerabilities for that very reason. This applies in particular to network services. After installation, it therefore needs to be checked which services are installed and activated on the system. Unnecessary services must be disabled or completely uninstalled.

On the one hand, checking for running services can be carried out locally with the means of the installed operating system and, on the other hand, in the case of network services, from the outside through a port scan from another system. By a combination of both methods can be largely excluded that the system offers even more unwanted network services.

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
Even if the procurement of an IT system has been made to ensure that it has enough storage space, storage space sooner or later becomes scarce in the event of prolonged use. On IT systems that are used by different users, the existing resources must therefore be divided so that all users can work as optimally as possible.

Often you can observe the phenomenon that users want to have more storage space than is available to them. In addition to the ever-growing storage footprint of applications, another reason is that many users are reluctant to part with old and unneeded files. If no restrictions are made on storage space limitation and archiving, there is a risk that storage space for large amounts of legacy data will be wasted or the user directories will overflow.

A simple solution would be to always provide more and more storage space as needed as demand increases. However, this is not always feasible in practice. Even if the users are sensitized for economical data storage, each unnecessary file is nevertheless often considered important.

For users or user groups, but also for applications, Disk Quotas can set a storage volume that must not be exceeded. On servers and all IT systems that are used concurrently by multiple users or applications, disk space should therefore be restricted for individual users as well as for applications through disk quotas. This includes servers (such as file, web, and mail servers) and clients with multiple user IDs. For clients where the data is separated from the system partition and used by only one user, a disk quota can be omitted.

The choice of the quota volume is important. If all users are to receive the same quota volume, the required volume can be calculated by dividing the space to be used by the number of users. In addition, however, a space reserve should be scheduled. The problem is the choice of a too small disk quota. If users have too little disk space available, they might try to store the information outside the intended directories to circumvent the restrictions. For this purpose, then frequently used locations that are not suitable for such. Temporary directories or other directories writable to all users. When space on file servers is too tight, users often rely on local disks. In many cases, this violates the regulations and may, for example, result in the files not being included in the central backup.

On the one hand, it should be determined which information should be stored where and how many versions of a file should be stored on the production system for how long.

Data from completed projects should be archived in an orderly manner and should not be kept in stock on the production systems "for all cases". On the other hand, it should be determined how much storage space is made available to the various user groups and applications. In addition, a reserve should be scheduled. It also needs to be determined how users can be allocated more storage when needed. The set values ​​must be documented. They also need to be regularly reviewed and updated.
Once the size of the disk quota has been determined, consideration should be given to whether and how to respond to a higher demand for disk space. This decision is influenced by the selection of a quota type. Hard quota limits are set so users will not be able to use more than their allocated storage quota. A soft quota, on the other hand, allows users to exceed the disk quota for a fixed amount of time and up to a specified limit. If the disk quota is exceeded, at least the user must be informed about this, for example by e-mail. Consideration should also be given to notifying IT operations so that they can respond to any problems that may arise. In addition, it must be determined whether and how individual users can be allocated additional storage space. This should be a regulated and comprehensible procedure. Disk quotas should not be increased "on demand".

Many popular operating systems include tools to set up Disk Quotas. However, it should be checked if additional software is needed to set up and manage a disk quota.

#### ORP.5.M7 Maintaining Information Security [Information Security Officer (ISB)]

Often, errors in products become known, which can lead to the information security of the information network, where they are operated, is affected. Corresponding errors can affect hardware, firmware, operating systems, and applications. These vulnerabilities need to be addressed as soon as possible so that they can not be exploited by internal or external attackers. This is especially important when the systems are connected to the Internet. Operating system or software component manufacturers typically release patches or updates that must be installed on their IT system to correct the error (s).

The system administrators should therefore regularly inform themselves about known vulnerabilities.

It is important that patches and updates, like any other software, can only be obtained from trustworthy sources. For each system or software product used, it must be known where security updates and patches are available. It is also important to verify the integrity and authenticity of the products already installed, or the security updates and patches to be incorporated (see the section "Ensuring the Integrity and Authenticity of Software Packages") before installing an update or patch. Before installation, they should also be checked using a computer virus protection program. This should also be done for packages whose integrity and authenticity have been verified.

Security updates or patches, however, must not be prematurely recorded, but must be tested before importing. These tests should always use up-to-date, system-tuned test plans or automated tests for a consistent, meaningful result. Otherwise, if a conflict arises with other critical components or programs, such an update may cause the system to fail. If necessary, an affected system must be protected by other means until the tests are completed. It should be ensured that updates that are imported by automatic update mechanisms are also tested.

Before installing an update or patch, you should always back up the system, which will allow it to recover to its original state if problems occur. This is especially true if detailed tests can not be performed due to lack of time or due to a lack of a suitable test system.
In any case, it must be documented when, by whom and for what reason patches and updates were recorded. From the documentation the current patch level of the system must be able to be determined quickly at any time, in order to gain clarity as soon as the weaknesses become known as to whether the system is at risk.

If it is determined that a security update or patch is incompatible with another major component or program or is causing problems, it is important to consider how to proceed. If it is decided that a patch will not be installed due to the problems that have arisen, this decision must be documented in any case. In addition, it must be clear in this case which measures have been taken to prevent exploitation of the vulnerability. Such a decision must not be made by the administrators alone, but must be agreed with the supervisor and the ISB.

** Ensuring the integrity and authenticity of software packages **

Carelessly executing programs that originate from "unsafe" sources can cause considerable harm. Malware, for example, can install password-spying programs, Trojan horses, or backdoors on a computer, or easily corrupt or erase data.

Typical sources of such malware are, for example, programs that display themselves as screen savers, virus scanners or other utilities and are attached to e-mails. Often these are sent under fake sender addresses to many recipients. Often the programs are downloaded from the internet and installed without verification.

Even if no encryption or signature techniques are used otherwise, the use should be considered to the extent described in this measure.

In principle, software should only be installed from well-known sources, especially if it has not been delivered on data carriers but has been downloaded from the internet, for example. This is especially true for updates or patches that are typically no longer delivered on disk. Most manufacturers and distributors offer checksums that allow at least an integrity check of a package. The checksums are usually published on the websites of manufacturers or sent by e-mail. To verify the integrity of a downloaded program or archive file, the published checksum is then compared to a locally generated checksum by a corresponding program.

If checksums are offered for a software package, these should be checked before installing the package.

A verification of authenticity can not be done with checksums. Therefore, in many cases, digital signatures are offered for programs or packages. In turn, the public keys needed to verify the signature are usually available on the manufacturer's websites or from public-key servers. Often the checksums are generated with one of the programs PGP or GnuPG.

If the check reveals that it is a valid signature of the respective manufacturer, this results in a significantly higher degree of trustworthiness for the package than simply the presence of a checksum.

Sometimes even the built-in software update mechanisms of the respective operating system or application software do not perform checksum comparisons. If possible, however, a checksum check should be performed on each software package before importing.
Furthermore, not all checksum comparisons can be performed without the involvement of the users, since the checksums, signatures or certificates required for this purpose are not provided by the manufacturers in a uniform manner. This often requires manual verification on the manufacturer pages or customization of URLs in the patch and change software.

If digital signatures are available for a software package, they should always be checked before installing the package.

A fundamental problem with the use of digital signatures is the verification of the authenticity of the key used itself. If the public key carries no signature of a known trustworthy person or organization (such as a trust center), the signatures generated with the corresponding private key offer no real security in that the software package actually comes from the developer, manufacturer or distributor. Therefore, if not certified, the public keys should preferably be obtained from a source other than the software package itself, for example from a manufacturer's CD-ROM, from another mirror server on which the package can also be downloaded, or from one Public key server.

To check checksums and digital signatures, the corresponding programs must be available locally. Administrators should be aware of the meaning and validity of checksums and digital signatures. In addition, the administrators must have enough time to use the appropriate programs in their daily work and familiarize themselves with the operation.

Obtaining patches and email changes is not recommended for a variety of reasons. The origin of emails is difficult to determine without the use of additional security mechanisms and the recipient addresses in the institutions are often distribution lists, whose address is easy to guess. Patches and changes can also be very extensive by now. Many companies and government agencies have limited the size of email attachments and may also prohibit the adoption of executable attachments. Furthermore, the large amounts of data unnecessarily burden the e-mail systems. Therefore, a timely availability of the software changes, which can be critical, especially in the case of security patches, can not be adequately ensured via e-mail.

Furthermore, some manufacturers offer to send changes and patches to the customer directly on data carriers. In this case too, the patches and changes should be verified using checksums or digital signatures, as sender information on mailpieces and manufacturer logos on CDs and DVDs can easily be faked.

Another aspect of verifying the authenticity of the update may be news published by the manufacturer on its website, newsletter or similar channels. Some manufacturers have established cycles and timepoints that typically release information about changes systematically.

#### ORP.5.M8 Regular reviews of Compliance Management

Only a regular and comprehensive backup reliably ensures that all stored data can be made available even in the event of malfunction, the effects of malicious software, hardware failures or (intentional or unintentional) deletions. The necessary requirements are described in the module OPS 1.1.5 Data Backup.

### 2.3 Measures for increased protection requirements
The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### ORP.5.M9 Protection against subsequent changes to information [Information Security Officer (ISB), user] (I)

Files that are passed on to third parties can generally be further processed by them. This is not always in the sense of the creator. Therefore, data should be protected against subsequent changes, partial disclosure or processing.

Frequently, the problem is that information via the Internet or other networks should be made available to third parties, but not printed out hundredfold or seamlessly integrated into other works.

There are various solutions for this, some of which can be combined with each other. Examples for this are:

* The use of digital signatures to prevent unnoticed changes to files (see also CON.1 crypto concept).
* Adding copyright notices to information such as brochures or files on web pages. These may read as follows: "The work including all its parts is protected by copyright and any use outside the terms of the copyright law without the consent of the author is inadmissible and punishable." as well as "Copyright (©) 7/2016 by BSI".
* The use of file formats that make subsequent changes or partial further processing more difficult. For this purpose, z. B. postscript or the security properties of application programs, such. Eg for PDF files.
Many application programs provide security mechanisms to limit further handling of the created files. In the following, some such security mechanisms are presented using the example of PDF files. Since the security mechanisms of the different application programs are very different and sometimes even vary from version to version, it is important to inform employees about how to use them and what steps to take before handing over electronic documents. It often makes sense to train one employee (plus representative) thoroughly. He should then process all documents to be forwarded according to the security requirements or be available as a contact person.

** Protection of PDF documents **

PDF documents can be provided with access restrictions during creation. So z. For example, the opening, printing or copying of PDF files can be restricted.

* Often, individual passages in a document are to be rendered unrecognizable prior to publication. A popular, but extremely error-prone method is to "blacken" text passages electronically. However, the overpainted information is in many cases easily readable. Therefore, this is absolutely necessary.
* By using cryptographic methods, PDF documents can be signed or encrypted so that only certain users can use them.
* PDF security policies can be created. Any user can create these for themselves or use security policies specified by the institution, which requires an Adobe Policy Server.
* File ProtectionWith Adobe Acrobat, the most common application for creating and editing PDF files, you can assign two types of passwords. Some are needed to open the document, the others are needed to change the security attributes. When assigning a password, it first asks which program versions the protection function should be compatible with. Up to the version "Adobe 5.0 and higher", only a 40-bit encryption with RC4 is possible, from "Adobe 5.0 and higher" is a 128-bit encryption with RC4 and from "Adobe 7.0 and higher" is a 128- Bit encryption with AES provided. Care should be taken to encrypt at least 128 bits, as document protection can otherwise be easily undone. The following security features can be limited, among others:

 
+ Open the document
+ Print
+ Change the document
+ Copy of texts, images or other content
+ Access to metadata of a document
+ Add or change notes and form fields


 
It should be carefully considered which metadata the file should contain. Here, for example, it may be desirable to provide a file with a multitude of metadata so that it can be found via search engines. It may also be useful not to pass on metadata, for example, the name of the author should be removed if a document is to be forwarded anonymously.

Unfortunately, this only provides rudimentary protection, since PDF files (depending on the version of the program they were created with) can also be opened with programs that ignore these security attributes. As long as z. If, for example, printing is allowed, the document can even be converted back into a PDF file at any time without any restrictions.

It must therefore be noted that depending on the application program used, version used and options set with the provided program properties can not be achieved sufficient protection. Depending on the protection requirements, files must therefore be signed using cryptographic methods (see also CON.1 Crypto Concept).

#### ORP.5.M10 Classification of Information (CIA)

Basically, employees should, of course, handle all information carefully. In addition, there are data in many areas that have a higher need for protection or special restrictions, such. Personal, financial, confidential or copyrighted information. Depending on their categorization, they are subject to different restrictions when dealing with them. Therefore, it is important to alert all employees to the restrictions that apply to these data (see also ORP.5.A3 Employee Commitment to Compliance with Relevant Laws, Rules and Regulations). The data should be marked as appropriate, eg. For example, by naming the category for documents in the header or footer.

Of course, the protection required by data directly affects all media on which they are stored or processed. Data with special protection requirements may be incurred in a wide variety of areas, eg. For example, fax or e-mail. There should therefore be regulations in all areas which also specify who may read, process or pass on such data. This includes, if necessary, the regular check for correctness and completeness of the data.

Many information, but also applications, are subject to copyright notices or passing restrictions ("for internal use only"). All employees must be made aware that no documents, files or software may be copied without taking into account any copyright notices or license terms.
Special attention must also be paid to all information that forms the basis for the task. This includes all business-relevant data, so z. For example, those data that, if lost, could incapacitate the institution that may affect the economic relationships of collaborating companies, or from whose knowledge a third party (such as a competitor) may derive financial benefits. Every agency and every company should have an overview of which data should be considered business-critical. In addition to the general due diligence requirements, special rules and regulations may apply to these data for storage, processing, transfer and destruction. This business critical information needs to be protected against loss, manipulation and falsification. Longer-term stored or archived data must be regularly tested for readability. Information that is no longer required must be reliably deleted (see also CON.7 Delete and Destroy).

#### ORP.5.M11 Survey of the legal framework for cryptographic processes and products [IT operation, person responsible for the individual applications] (CI)

Before deciding which cryptographic methods and products to use, a number of factors must be identified. For this, the system administrators and the persons responsible for the individual systems or IT applications can be interviewed. The results must be comprehensible z. B. in a crypto-concept documented (see also CON.1 crypto concept).

The following influencing factors must be determined for all specified storage locations and transmission routes:

* Safety aspects, z. B. to be achieved protection needs and attacker potential
* Technical aspects, e.g. IT system environment, data volume, performance
* Personnel and organizational aspects, eg. B. Ease of use, training needs, additional staffing requirements
* Economic aspects, eg. Eg one-time investments, running costs, personnel costs, royalties
* Use of key recovery mechanisms
* maximum lifetime of the cryptographic procedures
* Legal framework for the use of cryptographic products
When using cryptographic products, various legal conditions must be observed. For example, some countries may not use cryptographic techniques without permission. Therefore it must be investigated

* whether restrictions on the use of cryptographic products should be observed within the countries of operation (there are no restrictions within Germany) and
* whether export restrictions must be observed for eligible products.
If mobile IT systems or components are used on trips abroad, it must be clarified before each border crossing which country-specific regulations are to be observed (see also CON.8 Security on trips abroad).

However, there are not only maximum requirements but also minimal requirements for the cryptographic algorithms or methods used. So z. B. in the transmission of personal data encryption method with sufficient key length can be used.

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Additional information on threats and security measures in the area of ​​compliance management can be found in the following publications:

* #### [19600] ISO 19600: 2014

  

 ISO, compliance management systems, 2014
* #### [27002K18] ISO / IEC 27002: 2013 Chapter 18 Compliance

  

 ISO, Information Technology-Security Technique- Code of Practice for Information on Security Controls, especially Chapter 18 "Compliance", 2013

 
* #### [GSKHM] Tools for using the IT-Grundschutz catalogs

  

 BSI, (last accessed on 05.10.2017)
 [https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Hilfsmittel/Bausteine/bausteine\_node.html](https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ ITGrundschutzKataloge / resources / blocks / bausteine_node.html)

 
* #### [ISFSM2.3] Standard of Good Practices for Inforation Security 2016 SM2.3 and SI2.3

  

 Information Security Forum Limited, in particular SM2.3 Legal and Regulatory Compliance and SI2.3 Information Security Compliance Monitoring, (last accessed 05.10.2017)
 <Www.securityforum.org>
