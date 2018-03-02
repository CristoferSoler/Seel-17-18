[toc]
 
1 description
--------------

### 1.1 Introduction

Microsoft Exchange is a groupware solution for medium to large institutions. It can be used to electronically deliver messages and has additional services to support workflows and to manage mobile devices via Microsoft Exchange ActiveSync. Messages, such as e-mail, can be centrally managed, delivered, filtered and sent using Microsoft Exchange. Also, typical groupware applications, such as newsgroups, calendars, and task lists, as well as Microsoft Exchange Unified Messaging, can be offered and managed. In order to use the functions of Microsoft Exchange, additional client software is required in addition to the server service. The combination of Microsoft Exchange servers and Outlook clients is referred to here as the Microsoft Exchange system.

Microsoft Outlook is a client made directly available by installing the Microsoft Office suite or integrating with the operating systems of mobile devices. In addition, the web application "Outlook Web App" via the browser z. For example, you can access emails, contacts, and the calendar. This service is already included in the Microsoft Exchange package.

### 1.2 Objective

The goal of this module is to inform about typical threats to Microsoft Exchange and Outlook as well as to show how Microsoft Exchange and Outlook are used safely in institutions.

### 1.3 Delimitation

The module contains specific threats and requirements for Microsoft Exchange systems. Threats and requirements for the specific building blocks of server platform, operating system and clients are not part of the building block. These can be found in the blocks SYS.1.1 General Server and SYS.1.2 General Client and in the respective operating system-specific blocks.

The requirements from the module APP.5.1. Groupware must be fulfilled in any case. This component clarifies and complements requirements that are specific to Microsoft Exchange systems.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to Microsoft Exchange and Outlook:

### 2 1 Missing or inadequate rules for Microsoft Exchange and Outlook

Comprehensive rules and guidelines for Microsoft Exchange and Outlook are necessary to ensure the security of the information that is processed with Microsoft Exchange and Outlook. For example, data may be lost, accidentally modified or deleted if Microsoft Exchange is incorrectly and unregulated in the Active Directory. Similarly, if mailbox databases are deprecated unregulated and Microsoft Exchange is insufficiently included in the security policy. The same applies if the Microsoft Outlook clients can access the Microsoft Exchange servers unregulated.

### 2 2 Bad migration from Microsoft Exchange

In practice, Microsoft Exchange systems are migrated more frequently than reinstalled. In some cases, migrating to a new version of the Microsoft Exchange server requires updating the operating system to a newer version. For their part, new operating systems often make demands on the existing domain concept and the existing directory services.
If the migration is not carefully planned and executed, internal communication through Microsoft Exchange in the institution can be severely disrupted, which could lead to a decline in productivity. During migration, configuration problems may occur, such as: For example, you may have changed the configuration settings for the different versions or connect to directory services. Furthermore, incorrect protocol settings can lead to irregularities in information transmission, authentication and encryption.

### 2 3 Illegal browser access to Microsoft Exchange

With Microsoft Exchange, users can access their own e-mail account via a browser. This is done using Internet Information Services (IIS), which are an integral part of the Microsoft Exchange Server. If this function is improperly planned and configured incorrectly, the internal network may be uncontrollably accessed from the outside.

If e-mails are to be accessed via a browser that is used from the Internet, this presents a great potential for danger. Without direct access to the institution's network, attackers could access e-mail, spying on email addresses and content, abusing email, sending spam, and gaining access to in-house information, among other things.

### 2 4 Unauthorized connection of other systems to Microsoft Exchange

Microsoft Exchange systems are closely interlinked with the Microsoft Windows operating system and work together through so-called connectors with third-party systems. Connectors (also known as connectors) allow other systems to retrieve mail from Microsoft Exchange servers using specific protocols (such as POP3).

If the connectors are not included in a migration from Microsoft Exchange, the existing connectors may be incompatible with the migrated version of Microsoft Exchange. This can cause e-mails to be lost or changed inadvertently.

Outside the homogeneous Microsoft environment, security positions that are not related to the Microsoft Exchange system are invalid. The same applies to fixed security parameters in Microsoft Exchange that refer to the Windows server. If different subsystems are administered separately, inconsistencies can always occur. Incorrectly connected external systems can also result in data being lost or the system being blocked.

### 2 5 Incorrect administration of access and access rights under Microsoft Exchange and Outlook

If access rights to a Microsoft Outlook client or to data stored within Microsoft Exchange and Outlook are created and administered incorrectly, security gaps can arise. This is the case, for example, if additional rights are granted in addition to the necessary rights and thus unauthorized persons can access confidential information.

### 2 6 Incorrect configuration of Microsoft Exchange

A common cause of successful attacks on services such as Microsoft Exchange are misconfigured systems. Since a Microsoft Exchange system is very complex, various configuration settings and the mutually influencing parameters can cause numerous security problems. The possible misconfigurations range from the installation and operation of Microsoft Exchange components to inappropriate systems, to in-capped encryption and inadequate access restrictions on Microsoft Exchange servers, to the incorrect granting of rights when creating or initializing a Microsoft Exchange database.

### 2 7 Incorrect configuration of Outlook
The email client Microsoft Outlook is an important part of the Microsoft Exchange system. For the overall security of the system, it is important that the client is configured correctly. Even the selected communication protocol can cause special security problems. Similarly, private keys could be compromised to encrypt and sign emails. If encrypted at the network level, for example by IPSec or TLS, this encryption mechanism can become ineffective if the client is configured incorrectly. Misconfiguration can create security issues, such as loss of confidentiality due to unauthorized access.

### 2 8 Malfunctions and misuse of self-developed macros and programming interfaces under Microsoft Outlook

Many software manufacturers provide programming interfaces in their tools and applications, for example as an application programming interface (API). These allow you to use certain functions from other programs or to extend the functionality of the application. Microsoft Outlook can be misused to spread malicious software. The malicious software variants include, for example, malicious tools and macros that directly exploit Microsoft Outlook and the associated e-mail functions to access, modify or delete information. In turn, macros can be used to forward or post messages, appointments, or tasks. Errors in macros can be an increased risk. Index errors within macros can lead to incorrect results and potentially uneconomic decisions in the institution. Specific consequences can be unnecessary costs or automated data drainage.

3 requirements
---------------

The following are specific requirements for the Microsoft Exchange and Outlook sections. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### APP.5.2.A1 Planning the Use of Microsoft Exchange and Outlook [IT Director, Information Security Officer (ISB)]

Before Microsoft Exchange and Outlook can be used, the use of Microsoft Exchange and Outlook MUST be carefully planned. At least the following points MUST be observed:

* Development of the e-mail infrastructure,
* clients or server systems to be connected,
* Use of functional extensions,
* Securing the access ports of the server / client components,
* Confidentiality, integrity and availability,
* protocols to use and
* Integration of server and client systems in the dedicated network segments.
#### APP.5.2.A2 Choosing a Suitable Microsoft Exchange Infrastructure [IT Leader]

It MUST be decided with which systems and application components, as well as in which hierarchical gradation the Microsoft Exchange infrastructure should be realized. The selection MUST also decide whether to run the systems as a cloud or local service.

#### APP.5.2.A3 Authorization Management
For the systems of the Microsoft Exchange infrastructure, a correction concept MUST be created, suitably documented and applied. The privileged users as well as the administrators MUST only have as many authorizations as is necessary for the task fulfillment (minimum principle). It MUST be checked on a regular basis to see if the allocated rights are still appropriate.

#### APP.5.2.A4 Access rights to Microsoft Exchange objects

Access permissions to Microsoft Exchange objects MUST be set based on the least privilege. Server-side user profiles MUST be used for non-machine access to Microsoft Exchange data. The default NTFS permissions on the Microsoft Exchange directory MUST be adjusted so that only authorized administrators and system accounts can access the data in that directory.

#### APP.5.2.A5 Backup from Microsoft Exchange [Emergency Response Officer]

The existing Microsoft Exchange system MUST be backed up before installations and configuration changes, as well as cyclically.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state of the art in Microsoft Exchange and Outlook. They SHOULD be implemented in principle.

#### APP.5.2.A6 Secure installation of a Microsoft Exchange system

The installation SHOULD be done on the basis of the mission planning of Microsoft Exchange and Outlook and the defined security policy (see APP.1.2.A1 Planning the Use of Microsoft Exchange and Outlook). Because Microsoft Exchange systems integrate heavily with the Windows environment, especially the Active Directory, the specific security policies should be considered. The systems on which Microsoft Exchange and Outlook should be installed SHOULD be properly secured.

#### APP.5.2.A7 Migrating from Microsoft Exchange systems

All migration steps SHOULD be thoroughly planned and documented. The Microsoft Windows system administrators SHOULD be involved in the planning. When planning your migration, you should consider mailboxes, objects, security policies, Active Directory concepts, e-mail systems, and functional differences in Microsoft Exchange and Outlook in the various versions. The new system SHOULD BE tested on a separate test network before it is installed to counteract software errors and compatibility issues.

#### APP.5.2.A8 Secure operation of Microsoft Exchange

All infrastructure systems and applications SHOULD be configured to adequately meet their protection needs. For this, a suitable basic configuration SHOULD be compiled and documented. The settings of the individual connectors SHOULD also be adjusted.

The responsible persons SHOULD fix known weaknesses in a timely manner depending on the protection requirements and the criticality. In general SHOULD make sure that patches and updates are obtained only from trustworthy sources.

#### APP.5.2.A9 Secure configuration of Microsoft Exchange servers

Microsoft Exchange servers SHOULD be configured based on the requirements of the security concept. A maximum size for both inbound and outbound messages SHOULD be set. Existing connectors SHOULD be configured appropriately. Logging the Microsoft Exchange system SHOULD be enabled. For existing customization, a corresponding concept SHOULD be created.
When using functional enhancements (for example, Microsoft Exchange Access Sync, Mirror Port, Spam Filter, Outlook Web App, or Data Loss Prevention), make sure that the defined confidentiality, integrity, and availability protection goals are still met.

#### APP.5.2.A10 Outlook settings

Only administrators SHOULD be able to change the Outlook environment. For this purpose, a separate Outlook profile with the user-specific settings SHOULD be created for each user. Users SHOULD only be able to change user-defined settings (eg set up signature, activate absence agent). , Attachments SHOULD not be opened automatically from emails. Preview window and the car preview SHOULD be deactivated. E-mails SHOULD NOT be forwarded automatically.

#### APP.5.2.A11 Secure communication to and from Microsoft Exchange systems

It should be made comprehensible with which protection mechanisms the communication to and from Microsoft Exchange systems is secured. It should be decided and comprehensible documented which of the various possible methods Internet Protocol Security (IPSec) or Transport Layer Security (TLS) should be used.

It SHOULD be the

* Administration interfaces,
* Client-server communication,
* existing Web-based Distributed Authoring and Versioning (WebDAV) interfaces,
* the server-server communication, the message communication and
* the public-key infrastructure based on Microsoft Outlook (S / MIME) email encryption
be encrypted.

#### APP.5.2.A12 Use of Microsoft Exchange for Outlook Anywhere

Outlook Anywhere SHOULD be configured according to the security requirements of the institution. Access to Microsoft Exchange over the Internet SHOULD be restricted to the necessary users. Communication to Outlook Anywhere SHOULD be encrypted (see APP.1.2.A11 Securing Communications to and from Microsoft Exchange Systems).

#### APP.5.2.A13 Training of administrators [Head IT]

For the operation of the components of the Microsoft Exchange infrastructure, only suitable and trained personnel SHOULD be used.

#### APP.5.2.A14 Training for Security Mechanisms of Outlook for Users [Information Security Officer (ISB)]

Outlook users SHOULD regularly be sensitized and trained on existing and new dangers when working with Microsoft Outlook. All users SHOULD be provided with relevant security mechanisms and procedures within Outlook. Here, regulations should z. This can be taken into account, for example, for access mechanisms, forms of authentication and cryptographic specifications for e-mail encryption.

#### APP.5.2.A15 Application documentation for Microsoft Exchange

The contents of the operating manual for Microsoft Exchange SHOULD be comprehensibly documented. The operating manual SHOULD be based on the phases of commissioning, operation, rejection and restart based on the life cycle. The documentation SHOULD be protected against unauthorized access. Changes SHOULD be comprehensibly documented or referenced.

#### APP.5.2.A16 Creation of a contingency plan for the failure of Microsoft Exchange and Outlook [Emergency Response Officer]

As part of the emergency preparedness SHOULD be designed a concept that can minimize the consequences of a failure of Microsoft Exchange and Outlook components. The emergency plan SHOULD define what to do in the event of a failure to ensure a timely restoration of normal operation.

### 3.3 Requirements for increased protection requirements
Listed below are exemplary proposals for requirements that go beyond the level of protection afforded by the state of the art and should BE considered AT INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.5.2.A17 Encryption of Microsoft Exchange System Databases (CIA)

A concept for the encryption of pst files and information store files SHOULD be created. The users SHOULD be informed about the functionality and the protection mechanisms when encrypting pst-files. Other aspects of local pst files that should be considered when encrypting Microsoft Exchange system databases are:

* own encryption functions,
* Encryption levels as well
* Mechanisms to secure the data in a pst file.
Mechanisms such. B. Encrypting File System or Windows BitLocker Drive Encryption SHOULD be used to secure the data in a pst file.

#### APP.5.2.A18 Regular Security Checks for Microsoft Exchange Systems (CIA)

The Microsoft Exchange system SHOULD regularly be checked for misconfigurations and vulnerabilities. For this purpose, it should be regularly subjected to a safety test by different people. It is recommended to set up a checklist to ensure a defined scope of testing. The following aspects SHOULD be taken into consideration during an examination:

* regular searches of safety-related information,
* Authorizations for revision users,
* regular checking of authorizations,
* Checking the timeliness of updates and
* Checking the security of the communication interfaces.
The Microsoft Exchange permissions SHOULD regularly be checked at least randomly.
