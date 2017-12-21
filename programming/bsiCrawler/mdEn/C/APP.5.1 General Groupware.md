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

Macros can also be used to forward or post messages, appointments or tasks. If macros are faulty or wrong values ​​are calculated in them, then For example, index errors can lead to incorrect results and potentially uneconomic decisions in the institution.

### 2 4 Incorrect assignment of access and access rights to groupware services

If access rights to a groupware client or access rights to stored data in groupware services are not sufficiently limited, security gaps may arise. If these rights are created and administered incorrectly, the operation can also be disturbed, for example if an employee can not access important information. It is also possible for attackers to gain access to sensitive information and access sensitive data.

### 2 5 Inadequate knowledge of the administrators of groupware systems

Even small configuration errors can affect the security of a groupware system. Personnel who know too little about groupware applications and services can inadvertently cause security vulnerabilities due to the complex system architectures and specific protection mechanisms of the groupware deployed. An inadequately trained administrator can often not respond effectively even in an emergency (for example, in case of functional errors and compromises). Insufficiently trained and sensitized administrators can create unwanted conditions within the groupware services and processes. This may include that between the terminals and the groupware systems is not completely synchronized or even that in the calendar, the time zones lead to erroneous start times both existing appointments.

### 2 6 Data loss in groupware applications

The loss of stored data in groupware applications can have a significant impact on business processes and thus on the entire institution. If data in connection with groupware applications are falsified or lost, private-sector institutions can be threatened with their existence. In public authorities, the loss or corruption of those data may delay or even rule out internal administrative and specialized tasks.

Overall, the loss of stored data in groupware applications, in addition to a loss of work and the cost of replacement, can also lead to long-term consequences, such as loss of confidence among customers and partners, as well as a negative public perception.

### 2 7 Attacks on groupware systems and applications
Groupware systems and individual groupware applications can be compromised by third parties. For groupware systems z. B. the users, the internal network, used groupware server and the message recipient are intentionally attacked. Potential security vulnerabilities can be exploited by attackers to read, modify or delete information in closed groupware systems. Even if the access to the groupware applications was not sufficiently protected, attackers could, for example, access confidential data.

### 2 8 Unreliability of groupware

Groupware services exchange data quickly and easily. However, this is not always reliable: Messages can be lost due to faulty IT systems or faulty transmission paths. Causes for this are, for example, damaged cables, failed network coupling elements or incorrectly configured communication software. E-mails can also be lost because the recipient address was not specified correctly. It is also possible that messages are intercepted by third parties or that they read targeted conversations.

Groupware services are usually not cryptographically secured by default. As a result, calendar services may also allow unauthorized persons to view the scheduling of groups or individual persons.

3 requirements
---------------

The following are specific requirements for the Groupware area. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### APP.5.1.A1 Secure installation of groupware systems [IT Manager]

All components required for a groupware system (eg the security gateways) MUST be securely installed and configured according to the planned system landscape. While the system is being installed, all passwords MUST be securely selected. Unused components MUST be disabled. Also, the installation sources MUST be protected against unauthorized access.

#### APP.5.1.A2 Secure configuration of groupware clients [IT, user]

The users' groupware clients MUST be preconfigured by the administrator to be as secure as possible without the user having to do anything. Users MUST be advised that the configuration may not be changed independently. It MUST also be prevented and prohibited that passwords are saved in plain text. If messages are stored on a mail server and z. For example, if accessed through the Internet Message Access Protocol (IMAP), a server-side mailbox size limit MUST be set. Before file attachments are executed, they MUST be checked against malware by a debugging program. You must choose secure settings for email in HTML format, preview features and email filtering rules, and secure email redirection.

#### APP.5.1.A3 Secure Operation of Groupware Systems [Head of IT, Information Security Officer (ISB)]
All security-relevant service packs, updates and patches for the respective software product MUST be imported. Administrators MUST therefore regularly inform themselves about newly discovered vulnerabilities, the groupware systems used and the operating systems used and close them promptly. In order to secure groupware systems in the institution, protections against denial of service (DoS) attacks MUST be taken. Local communication MUST be properly protected. Communication over public networks MUST be encrypted. In addition, the access rights to the locally connected users MUST be limited. A policy SHOULD be created that informs about the protocols and services allowed in the respective groupware. In particular, the mail server MUST be set so that it can not be misused as a spam relay.

#### APP.5.1.A4 Data Protection Archiving at Groupware [Information Security Officer (ISB), Data Protection Officer, User]

In a groupware system, the data MUST be backed up regularly. For this it MUST be regulated how the sent and received e-mails of the e-mail clients and on e-mail servers are backed up. Also, a documented procedure should be created on how to archive e-mails. It should be regulated in principle how, when and where sent and received emails are archived, for example, whether centralized or decentralized, if necessary, by the users themselves. When archiving emails SHOULD be z. B. temporal and organizational security aspects are considered. The required period SHOULD be reviewed, the archiving planned and also considered, how the e-mails can be restored.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of general groupware. They SHOULD be implemented in principle.

#### APP.5.1.A5 Definition of the communication partners [Head of Organization, Head of IT, Information Security Officer (ISB), Data Protection Officer]

It SHOULD be determined which communication partners are allowed to receive which information. If information is to be transmitted to a communication partner outside of their own institution, it should be ensured that the recipient has the right to process this information. All information SHOULD be classified according to its strategic importance to the institution. The communication partners SHOULD be advised that the data transmitted may only be used for the purpose for which they were disclosed. Also for reasons of data protection (Federal Data Protection Act (BDSG), transfer control) an overview SHOULD be created, which recipients are entitled to receive information, in particular personal data. In the case of data to be transmitted, it should be clear which communication partners have received or are receiving information.

#### APP.5.1.A6 Representation rules for e-mail usage [supervisor, information security officer (ISB), user]

For e-mail processing, a suitable representative SHOULD be named for each employee at all times. Representatives SHOULD have access to the representative's mailbox. Alternatively, the emails SHOULD be forwarded to the representative. If e-mails are forwarded, the representative users SHOULD at least be informed. In order to support the proxy control processes, special rules should be established for autoreply functions in e-mail programs, with which these functions can be safely controlled. When employees use the autoreply functions, NO internal information SHOULD be shared.

#### APP.5.1.A7 Planning the Safe Use of Groupware Systems [IT Leader, Information Security Officer (ISB)]
Before an institution introduces a groupware system, it should decide what it will be used for and which information clusters will be processed on the groupware system in the future. It SHOULD be decided whether to use a separate groupware server in the institution or to use a provider. SHOULD also determine how the groupware clients access the servers. For each used function of a groupware SHOULD own planning be carried out, in which also their safety aspects are considered.

When planning SHOULD also be determined what data ,. Under what conditions may be transmitted via groupware services and how this affects the need for protection. It SHOULD also be described as how a proper file transfer can be guaranteed, e.g. B. by organizational regulations or technical measures. In addition, it should also be regulated whether and how groupware services may be used privately. Also, institutions SHOULD regulate how employees should deal with webmail.

#### APP.5.1.A8 Definition of a security policy for groupware [IT chief, information security officer (ISB), user]

A security policy for groupware systems and applications SHOULD be created and regularly updated. All users and administrators SHOULD be informed about new or changed security requirements for groupware systems. The groupware security policy SHOULD be compliant with the applicable parent security policy of the institution. It SHOULD check if the security policies are being applied correctly.

It SHOULD create a security policy for users and one for administrators. For the users, SHOULD specify how the communication can be secured (eg, for network or e-mail communication), which user access rights exist (for example, to groupware servers or databases), such as Information should be passed on to communication partners and how information transmitted can be secured (eg signatures / encryptions). The content to be controlled for administrators SHOULD also include the settings options of the groupware components, as well as the specifications for possible access from another server to a groupware server and information about the authorized access point from which a groupware server may be accessed.

#### APP.5.1.A9 Secure administration of groupware systems [Head IT]

Administrative access as well as the associated tasks SHOULD be separated depending on their responsibilities. To run a groupware system smoothly, administrators should be appointed and trained. All administration tasks in the field of groupware and the assigned authorizations SHOULD be sufficiently documented. Administrators SHOULD only be assigned the permissions necessary for the respective tasks. After all groupware components have been installed, they SHOULD be configured securely. It SHOULD be ensured that the groupware systems used are sufficiently dimensioned. Also, trusted groupware documentation should be considered during administration. It SHOULD be checked regularly, if the existing documentation is up-to-date.

#### APP.5.1.A10 System Architecture and Security of Groupware Systems for Administrators [IT Director, Information Security Officer (ISB)]

To administer a groupware system correctly and securely, the responsible administrators SHOULD be trained. For the training SHOULD be considered to define a training plan. The administrators SHOULD be trained in all security related areas of the groupware system. Further training focuses SHOULD be:
* Overview of solutions for communication security (eg encryption, VPN),
* Logging,
* Backing up and managing configuration data
* Data backup,
* Incident handling as well
* Disaster recovery measures.
#### APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]

The assigned privileges, especially the privileged one, SHOULD regularly be aligned with the authorization concept and adapted promptly as the tasks of users and administrators change. An authorization concept SHOULD be created that includes all groupware components. Permissions SHOULD be awarded as restrictively as possible. Administrative activities at operating system level and groupware application level SHOULD be separated as far as possible. Within the administration, roles and responsibilities SHOULD be separated.

#### APP.5.1.A12 Training for Security Mechanisms of Groupware Clients for Users [Head of IT, Information Security Officer (ISB)]

All users SHOULD be trained and instructed to work with the groupware client. It SHOULD show the users which security mechanisms are available and how they can be used. Those who use groupware SHOULD be sensitized to hazards and safety measures to be adhered to. Users SHOULD be taught about potential misconduct. You SHOULD also be warned against participating in e-mail chain letters and subscribing to many mailing lists.

#### APP.5.1.A13 Verification of the data to be transmitted before disclosure and removal of residual information [IT manager, user]

Before a file is sent via email via a groupware service, SHOULD check if it contains any residual information that should not be published. All users SHOULD be made aware of the dangers of residual and additional information in files. To minimize these risks, files should be randomly checked for any residual information. All additional information (file properties) of files in standard software formats SHOULD be identified, reviewed, and adjusted if necessary before being distributed. Likewise SHOULD make sure that the files contain no so-called slack bytes.

#### APP.5.1.A14 Prevention of problematic file formats [user]

It SHOULD be specified how to deal with emails in HTML format, with other file formats and file attachments. For HTML-formatted emails, a policy SHOULD be created that includes related content from user training, redirection settings, conversion options (eg, in text formats), user instructions, and possible secure and separate workstations.

#### APP.5.1.A15 Logging of groupware systems [Head IT]

All security-relevant events of groupware systems SHOULD be logged. For this, a suitable logging concept SHOULD be created. Access to the log data SHOULD be restricted. Important system events, such as changes, errors and faults in hardware, operating system, drivers, services and other software, SHOULD be logged and regularly evaluated.

#### APP.5.1.A16 Handling SPAM [IT Director, Information Security Officer (ISB), User]

Basically, all users SHOULD ignore and delete unwanted emails. It SHOULD NOT respond to unsolicited emails, follow links in the email, or run an attachment. If the institution wishes to introduce e-mail filtering programs, this should be discussed with the data protection officer, the staff representatives and the users. For newsgroups and mailing lists, regulations SHOULD be created.
#### APP.5.1.A17 Selection of a groupware or mail provider [supervisor, data protection officer]

If no own groupware server is to be operated but a service provider is commissioned to operate the groupware server, the functional aspects SHOULD be identified and agreed with the possible provider. It should also be ensured that the groupware or mail provider implements all necessary security mechanisms and that its servers are operated securely. Required internal requirements SHOULD be fixed in writing considering legal aspects. It SHOULD inform all employees what to look for when using external groupware services.

#### APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]

On the central mail server SHOULD an e-mail scanner with built-in memory-resistant anti-virus program should be installed, which checks incoming and outgoing e-mails, in particular their attachments, for spam features and harmful content. Since encrypted e-mails can not be automatically checked, it should also be determined how to deal with such e-mails. If an e-mail scanner is used, all employees, the data protection officer and the staff representatives SHOULD be informed.

#### APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]

Data transmitted by groupware systems SHOULD be secured using appropriate protection mechanisms. Thus, encryption and digital signatures should ensure the integrity and confidentiality of electronically transmitted information, for example through TLS connection encryption.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)

A concept SHOULD be designed to minimize the consequences of a failure and what to do in the event of a failure. The emergency planning for the groupware system SHOULD consider the existing emergency plan of the institution. Important tasks to be able to maintain or re-start the groupware system SHOULD be described as being able to be performed by appropriately trained personnel. A recovery plan for the groupware system SHOULD be created, which describes how to reboot the systems after a failure. System recovery emergency exercises SHOULD be performed on a regular basis, including all aspects of a system failure or compromise.

#### APP.5.1.A21 End-to-end encryption (CI)

To keep sensitive information confidential across all communication partners, end-to-end encryption SHOULD be used. Only encryption protocols should be used which correspond to the current state of the art (see CON.1 crypto concept).

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the area of ​​"General Groupware" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013
Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [KOLAB] Kolab Groupware

  

 Documentation, (last accessed on 29.09.2017)
 <Https://docs.kolab.org/>

 
* #### [TN170645] Exchange Server 2016

  

 Microsoft Technet, (last accessed 29.09.2017)
 [Https://technet.microsoft.com/de-de/library/mt170645.asp](https://technet.microsoft.com/de-de/library/mt170645(v=exchg.160).asp)

 
* #### [ZIMBRA] Zimbra Groupware

  

 Documentation, (last accessed on 29.09.2017)
 <Https://www.zimbra.com/documentation/>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "General Groupware" block.

* G 0.11 Failure or disruption of service providers
* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.16 Theft of devices, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.27 Resource shortage
* G 0.28 Software vulnerabilities or errors
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.33 Personnel loss
* G 0.36 Identity theft
* G 0.37 denying actions
* G 0.40 Denial of Service
* G 0.41 Sabotage
* G 0.42 Social engineering
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
* G 0.11 Failure or disruption of service providers
  * APP.5.1.A7 Planning the Safe Use of Groupware Systems [IT Leader, Information Security Officer (ISB)]
  * APP.5.1.A17 Selection of a groupware or mail provider [supervisor, data protection officer]
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
* G 0.14 Spying out information (spying)
  * APP.5.1.A6 Representation rules for e-mail usage [supervisor, information security officer (ISB), user]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A21 End-to-end encryption (CI)
* G 0.15 Listening
  * APP.5.1.A1 Secure installation of groupware systems [IT Manager]
  * APP.5.1.A10 System Architecture and Security of Groupware Systems for Administrators [IT Director, Information Security Officer (ISB)]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A12 Training for Security Mechanisms of Groupware Clients for Users [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A13 Verification of the data to be transmitted before disclosure and removal of residual information [IT manager, user]
  * APP.5.1.A14 Prevention of problematic file formats [user]
  * APP.5.1.A15 Logging of groupware systems [Head IT]
  * APP.5.1.A16 Handling SPAM [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A17 Selection of a groupware or mail provider [supervisor, data protection officer]
  * APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A2 Secure configuration of groupware clients [IT, user]
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
  * APP.5.1.A21 End-to-end encryption (CI)
  * APP.5.1.A9 Secure administration of groupware systems [Head IT]
* G 0.16 Theft of devices, data carriers or documents
  * APP.5.1.A4 Data Protection Archiving at Groupware [Information Security Officer (ISB), Data Protection Officer, User]
  * APP.5.1.A9 Secure administration of groupware systems [Head IT]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A21 End-to-end encryption (CI)
* G 0.18 Missing planning or missing adjustment
  * APP.5.1.A3 Secure Operation of Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A6 Representation rules for e-mail usage [supervisor, information security officer (ISB), user]
  * APP.5.1.A7 Planning the Safe Use of Groupware Systems [IT Leader, Information Security Officer (ISB)]
  * APP.5.1.A8 Definition of a security policy for groupware [IT chief, information security officer (ISB), user]
  * APP.5.1.A10 System Architecture and Security of Groupware Systems for Administrators [IT Director, Information Security Officer (ISB)]
  * APP.5.1.A12 Training for Security Mechanisms of Groupware Clients for Users [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A13 Verification of the data to be transmitted before disclosure and removal of residual information [IT manager, user]
  * APP.5.1.A14 Prevention of problematic file formats [user]
  * APP.5.1.A17 Selection of a groupware or mail provider [supervisor, data protection officer]
* G 0.19 Disclosure of information worthy of protection
  * APP.5.1.A5 Definition of the communication partners [Head of Organization, Head of IT, Information Security Officer (ISB), Data Protection Officer]
  * APP.5.1.A6 Representation rules for e-mail usage [supervisor, information security officer (ISB), user]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A13 Verification of the data to be transmitted before disclosure and removal of residual information [IT manager, user]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
  * APP.5.1.A21 End-to-end encryption (CI)
* G 0.20 Information or products from unreliable sources
  * APP.5.1.A1 Secure installation of groupware systems [IT Manager]
  * APP.5.1.A10 System Architecture and Security of Groupware Systems for Administrators [IT Director, Information Security Officer (ISB)]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A12 Training for Security Mechanisms of Groupware Clients for Users [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A13 Verification of the data to be transmitted before disclosure and removal of residual information [IT manager, user]
  * APP.5.1.A14 Prevention of problematic file formats [user]
  * APP.5.1.A15 Logging of groupware systems [Head IT]
  * APP.5.1.A16 Handling SPAM [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A17 Selection of a groupware or mail provider [supervisor, data protection officer]
  * APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A2 Secure configuration of groupware clients [IT, user]
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
  * APP.5.1.A21 End-to-end encryption (CI)
  * APP.5.1.A10 System Architecture and Security of Groupware Systems for Administrators [IT Director, Information Security Officer (ISB)]
  * APP.5.1.A12 Training for Security Mechanisms of Groupware Clients for Users [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A13 Verification of the data to be transmitted before disclosure and removal of residual information [IT manager, user]
  * APP.5.1.A14 Prevention of problematic file formats [user]
  * APP.5.1.A16 Handling SPAM [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]
* G 0.21 Manipulation of hardware or software
  * APP.5.1.A2 Secure configuration of groupware clients [IT, user]
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
  * APP.5.1.A21 End-to-end encryption (CI)
  * APP.5.1.A15 Logging of groupware systems [Head IT]
  * APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]
* G 0.22 Manipulation of information
  * APP.5.1.A1 Secure installation of groupware systems [IT Manager]
  * APP.5.1.A10 System Architecture and Security of Groupware Systems for Administrators [IT Director, Information Security Officer (ISB)]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A12 Training for Security Mechanisms of Groupware Clients for Users [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A13 Verification of the data to be transmitted before disclosure and removal of residual information [IT manager, user]
  * APP.5.1.A14 Prevention of problematic file formats [user]
  * APP.5.1.A15 Logging of groupware systems [Head IT]
  * APP.5.1.A16 Handling SPAM [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A17 Selection of a groupware or mail provider [supervisor, data protection officer]
  * APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A4 Data Protection Archiving at Groupware [Information Security Officer (ISB), Data Protection Officer, User]
  * APP.5.1.A15 Logging of groupware systems [Head IT]
  * APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A21 End-to-end encryption (CI)
* G 0.25 Failure of devices or systems
  * APP.5.1.A4 Data Protection Archiving at Groupware [Information Security Officer (ISB), Data Protection Officer, User]
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
* G 0.26 Malfunction of equipment or systems
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
* G 0.27 Resource shortage
  * APP.5.1.A2 Secure configuration of groupware clients [IT, user]
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
  * APP.5.1.A21 End-to-end encryption (CI)
  * APP.5.1.A9 Secure administration of groupware systems [Head IT]
* G 0.28 Software vulnerabilities or errors
  * APP.5.1.A1 Secure installation of groupware systems [IT Manager]
  * APP.5.1.A10 System Architecture and Security of Groupware Systems for Administrators [IT Director, Information Security Officer (ISB)]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A12 Training for Security Mechanisms of Groupware Clients for Users [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A13 Verification of the data to be transmitted before disclosure and removal of residual information [IT manager, user]
  * APP.5.1.A14 Prevention of problematic file formats [user]
  * APP.5.1.A15 Logging of groupware systems [Head IT]
  * APP.5.1.A16 Handling SPAM [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A17 Selection of a groupware or mail provider [supervisor, data protection officer]
  * APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.5.1.A1 Secure installation of groupware systems [IT Manager]
  * APP.5.1.A10 System Architecture and Security of Groupware Systems for Administrators [IT Director, Information Security Officer (ISB)]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A12 Training for Security Mechanisms of Groupware Clients for Users [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A13 Verification of the data to be transmitted before disclosure and removal of residual information [IT manager, user]
  * APP.5.1.A14 Prevention of problematic file formats [user]
  * APP.5.1.A15 Logging of groupware systems [Head IT]
  * APP.5.1.A16 Handling SPAM [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A17 Selection of a groupware or mail provider [supervisor, data protection officer]
  * APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A2 Secure configuration of groupware clients [IT, user]
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
  * APP.5.1.A21 End-to-end encryption (CI)
  * APP.5.1.A9 Secure administration of groupware systems [Head IT]
* G 0.31 Incorrect use or administration of devices and systems
  * APP.5.1.A1 Secure installation of groupware systems [IT Manager]
  * APP.5.1.A10 System Architecture and Security of Groupware Systems for Administrators [IT Director, Information Security Officer (ISB)]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A12 Training for Security Mechanisms of Groupware Clients for Users [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A13 Verification of the data to be transmitted before disclosure and removal of residual information [IT manager, user]
  * APP.5.1.A14 Prevention of problematic file formats [user]
  * APP.5.1.A15 Logging of groupware systems [Head IT]
  * APP.5.1.A16 Handling SPAM [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A17 Selection of a groupware or mail provider [supervisor, data protection officer]
  * APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A2 Secure configuration of groupware clients [IT, user]
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
  * APP.5.1.A21 End-to-end encryption (CI)
  * APP.5.1.A9 Secure administration of groupware systems [Head IT]
* G 0.32 Abuse of permissions
  * APP.5.1.A9 Secure administration of groupware systems [Head IT]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
* G 0.33 Personnel loss
  * APP.5.1.A6 Representation rules for e-mail usage [supervisor, information security officer (ISB), user]
* G 0.36 Identity theft
  * APP.5.1.A9 Secure administration of groupware systems [Head IT]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
* G 0.37 denying actions
  * APP.5.1.A5 Definition of the communication partners [Head of Organization, Head of IT, Information Security Officer (ISB), Data Protection Officer]
  * APP.5.1.A9 Secure administration of groupware systems [Head IT]
  * APP.5.1.A10 System Architecture and Security of Groupware Systems for Administrators [IT Director, Information Security Officer (ISB)]
  * APP.5.1.A11 Authorization Management for Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A12 Training for Security Mechanisms of Groupware Clients for Users [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A13 Verification of the data to be transmitted before disclosure and removal of residual information [IT manager, user]
  * APP.5.1.A14 Prevention of problematic file formats [user]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A21 End-to-end encryption (CI)
* G 0.40 Denial of Service
  * APP.5.1.A3 Secure Operation of Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
* G 0.41 Sabotage
  * APP.5.1.A15 Logging of groupware systems [Head IT]
  * APP.5.1.A20 Creating an Outage Plan for Groupware System Failure [Emergency Response Officer, IT Leader, Information Security Officer (ISB)] (A)
* G 0.42 Social engineering
  * APP.5.1.A16 Handling SPAM [IT Director, Information Security Officer (ISB), User]
* G 0.45 data loss
  * APP.5.1.A3 Secure Operation of Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A4 Data Protection Archiving at Groupware [Information Security Officer (ISB), Data Protection Officer, User]
  * APP.5.1.A15 Logging of groupware systems [Head IT]
  * APP.5.1.A16 Handling SPAM [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]
* G 0.46 Loss of integrity of sensitive information
  * APP.5.1.A3 Secure Operation of Groupware Systems [Head of IT, Information Security Officer (ISB)]
  * APP.5.1.A5 Definition of the communication partners [Head of Organization, Head of IT, Information Security Officer (ISB), Data Protection Officer]
  * APP.5.1.A6 Representation rules for e-mail usage [supervisor, information security officer (ISB), user]
  * APP.5.1.A14 Prevention of problematic file formats [user]
  * APP.5.1.A15 Logging of groupware systems [Head IT]
  * APP.5.1.A16 Handling SPAM [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A18 Spam and virus protection by using an e-mail scanner on the mail server [Information Security Officer (ISB)]
  * APP.5.1.A19 Encryption of Groupware [IT Director, Information Security Officer (ISB), User]
  * APP.5.1.A21 End-to-end encryption (CI)
