[toc]
 
1 description
--------------

### 1.1 Introduction

Microsoft Exchange is a groupware solution for medium to large institutions. It can be used to electronically deliver messages and has additional services to support workflows and to manage mobile devices via Microsoft Exchange ActiveSync. Messages, such as e-mails, can be centrally managed, delivered, filtered and sent using Microsoft Exchange. Also, typical groupware applications, such as newsgroups, calendars, and task lists, as well as Microsoft Exchange Unified Messaging, can be offered and managed. In order to use the functions of Microsoft Exchange, additional client software is required in addition to the server service. The combination of Microsoft Exchange servers and Outlook clients is referred to here as the Microsoft Exchange system.

Microsoft Outlook is a client made available directly from mobile devices by installing the Microsoft Office suite or integrating with operating systems. In addition, the web application "Outlook Web App" via the browser z. For example, you can access emails, contacts, and the calendar. This service is already included in the Microsoft Exchange package.

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

If e-mails are to be accessed via a browser that is used from the Internet, there is a great potential for danger. Without direct access to the institution's network, attackers could access e-mail, spying on email addresses and content, abusing email, sending spam, and gaining access to in-house information, among other things.

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
