[toc]
 
1 description
--------------

### 1.1 Introduction

Groupware (also referred to as collaborative software) refers to applications and systems that allow multiple people (groups) to collaborate across spatial and / or temporal distances. Using groupware systems, groups can cooperate with each other and coordinate appointments. Documents and data can be shared and edited by multiple users simultaneously, making the flow of information more efficient.

The term groupware systems includes, among others, the groupware server, the associated groupware clients and the required groupware services. In addition to the basic functions such. For example, project management, email, calendars or notebooks, newer applications offer so-called social media extensions, through which employees can communicate even better and cooperate.

### 1.2 Objective

The aim of this module is to protect information that is stored, processed or transmitted in and with groupware. For this purpose, the IT components used for groupware and their interfaces must be suitably secured and appropriate procedures established.

### 1.3 Delimitation

The block contains only specific threats and requirements for groupware systems. Threats and requirements for the specific building blocks of server platform, operating system and clients are not part of the building block. These can be found in the blocks SYS.1.1 General Server and SYS.1.2 General Client and in the respective operating system-specific blocks.

The module APP.5.1 Groupware is usually used in an information network in connection with another specific module of the layer APP.1 E-Mail / Groupware / Communication, these must also be implemented separately. These building blocks include APP.1.2 Microsoft Exchange / Outlook, APP.1.3 Kontact, APP.1.4 Lotus Notes / Domino and APP.1.5 Instant Messaging.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the * * Groupware area:

### 2 1 Inadequate groupware planning

The groupware process can not be complied with properly in the institution without appropriately documented regulations and a defined security procedure. Potential security risks can occur, in particular, if the groupware is incorrectly integrated into the directory services, databases are deduplicated, and the specific aspects of groupware are not documented in a security policy.

If the process, organizational and technical regulations are neglected in the planning of the groupware systems, the resulting freedoms, faulty settings, programming and attacks (internal / external) could result. This would hamper the groupware systems, the groupware process and cross-process interfaces in their task fulfillment.

### 2 2 Incorrect setting of the groupware

Because groupware systems are complex, many security issues can arise due to the many possible settings and the parameters that interact with each other. For example, server components could operate on inappropriate systems. In addition, it would be possible to ignore or disregard the essential settings (for example, encryption of individual groupware services or rights management rights restrictions). These vulnerabilities can lead to a significant loss of availability, authenticity and confidentiality of information, thereby hindering the functionality of groupware systems and corrupting processed data.
If rights are wrongly assigned to a groupware database, this can cause damaging data leak scenarios or unauthorized manipulation in the authorization management of the institution. The manipulations can result, for example, in incorrect settings that disturb the entire groupware system or individual services.

### 2 3 Misuse of self-developed macros and programming interfaces in groupware services

Many tools and applications have application programming interfaces (such as Application Programming Interface (API)) that allow certain functions to be provided to other applications or to extend the functionality of the application. However, groupware can be misused to spread malicious software. These include, for example, malicious programs that directly infect the groupware systems in order to access, modify or delete information.

Macros can also be used to forward or post messages, appointments or tasks. If macros are faulty or wrong values ​​are calculated in them, eg For example, index errors can lead to incorrect results and potentially uneconomic decisions in the institution.

### 2 4 Incorrect assignment of access and access rights to groupware services

If access rights to a groupware client or access rights to stored data in groupware services are not sufficiently limited, security gaps may arise. If these rights are created and administered incorrectly, the operation can also be disturbed, for example if an employee can not access important information. It is also possible for attackers to gain access to sensitive information and access sensitive data.

### 2 5 Inadequate knowledge of the administrators of groupware systems

Even small configuration errors can affect the security of a groupware system. Personnel who know too little about groupware applications and services can inadvertently cause security vulnerabilities due to the complex system architectures and specific protection mechanisms of the groupware deployed. An inadequately trained administrator can often not respond effectively even in an emergency (for example, in case of functional errors and compromises). Insufficiently trained and sensitized administrators can create unwanted conditions within the groupware services and processes. This may include that between the terminals and the groupware systems is not completely synchronized or even that in the calendar, the time zones lead to erroneous start times both existing appointments.

### 2 6 Data loss in groupware applications

The loss of stored data in groupware applications can have a significant impact on business processes and thus on the entire institution. If data in connection with groupware applications are falsified or lost, private-sector institutions can be threatened with their existence. In public authorities, the loss or corruption of those data may delay or even rule out internal administrative and specialized tasks.

Overall, the loss of stored data in groupware applications, in addition to a loss of work and the cost of replacement, can also lead to long-term consequences, such as loss of confidence among customers and partners, as well as a negative impact on the public.

### 2 7 Attacks on groupware systems and applications
Groupware systems and individual groupware applications can be compromised by third parties. For groupware systems z. B. the users, the internal network, used groupware server and the message recipient are intentionally attacked. Potential security vulnerabilities can be exploited by attackers to read, modify or delete information in closed groupware systems. Even if the access to the groupware applications was not sufficiently protected, attackers could, for example, access confidential data.

### 2 8 Unreliability of groupware

Groupware services exchange data quickly and easily. However, this is not always reliable: Messages can be lost due to faulty IT systems or faulty transmission paths. Causes for this are, for example, damaged cables, failed network coupling elements or incorrectly configured communication software. E-mails can also be lost because the recipient address was not specified correctly. It is also possible that messages are intercepted by third parties or that they read targeted conversations.

Groupware services are usually not cryptographically secured by default. As a result, calendar services may also allow unauthorized persons to view the scheduling of groups or individual persons.
