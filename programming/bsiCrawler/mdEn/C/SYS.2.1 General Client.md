1 description
--------------

### 1.1 Introduction

A "general client" is an IT system with any operating system that allows the separation of users. You should be able to set up at least one administrator and one user environment. Typically, such an IT system is networked and used as a client in a client-server network. The IT system can be operated on any platform. This can be, for example, a PC with or without a hard disk, a mobile or stationary device, but also a Linux workstation or an Apple Mac. The IT system typically has removable media drives, additional interfaces for data exchange, and other peripherals.

### 1.2 Objective

The goal of this module is to protect information that is created, read, edited, stored or sent to clients, regardless of the operating system they run on.

### 1.3 Delimitation

Typically, client systems operate under an operating system that requires its own security measures. Common client operating systems have their own blocks that supplement this block. The module "general client" forms the basis for the concrete building blocks on which they are based. If a concrete module exists for a considered IT system, it must be used in addition to the module General Client. If no specific module exists for deployed client systems, the requirements of this module must be suitably adapted. Safety recommendations for mobile devices that can not be freely configured, such as smartphones or tablets, can generally be found in the SYS.3 Mobile Devices layer.

If the client has other interfaces for data exchange, such. As USB, Bluetooth, LAN or WLAN, they must be secured according to the security requirements of the institution, as described in the corresponding modules. For this, information can be found in SYS.3.4 Mobile Disk, NET.2.3 Near Field Radio and NET.2.2 WLAN Usage.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the General Client area:

### 2 1 Malware

Malicious programs are designed to perform unwanted and malicious functions on computers. They usually become secretly active without the users knowing or agreeing to it. Depending on their characteristics, they offer an attacker extensive communication and control options with many functions. Among other things, they could specifically search passwords, remotely control IT systems, deactivate protection software or spy on data.

Clients are particularly vulnerable to malicious software: they are served directly by users and are often the gateway for malicious software. If users visit infected web pages, open emails with compromised content from private email accounts, or copy malicious software to the client through local disks, the malicious software spreads through clients into the institution's network. Central protection mechanisms, such as e.g. Virus protection on the file or email server can be bypassed so often.

### 2 2 Unstructured local data management

Despite regular contradictory recommendation, many users also store important data exclusively locally. For example, data is often stored in local user directories rather than on a central file server. E-mails are often only archived locally. This procedure can lead to the following problems:

* Data loss on hardware defects and
* no access to relevant data in case of substitution.
But even if basic requirements for central storage are adhered to, often additional local copies of the centrally stored data are created. This can lead to the following problems:

* Waste of local storage space,
* premature or non-deletion of data and
* inconsistent version states
### 2 3 Data loss

Clients typically store a lot of data across their entire organization, the loss of which can have a significant impact on business processes and therefore on the entire institution. If business-relevant data is destroyed or falsified, business processes and specialized tasks can be delayed or even prevented from running. Overall, the loss of stored data, in addition to a loss of work and the cost of replacement, can also lead to long-term consequences, such as loss of confidence among customers and partners, as well as a negative impact on the public. From the direct and indirect damage caused by data loss, institutions can in extreme cases be threatened in their existence.

### 2 4 Hardware defects due to incorrect operation

Unlike central IT systems such as servers, client users work directly at the end device. Physical access can intentionally or unintentionally damage the client. For example, they can step on floor-standing IT systems, upset monitors, tripping over cables, or pouring drinks into keyboards. Often it is not sufficient to replace hardware only in case of a defect. For example, in the event of a hard disk failure, stored data can not be recovered. In addition, the IT system can not be used until the repair is complete. In case of failure of a mobile device on the road, the work can be continued only after the return.

### 2 5 Software vulnerabilities or errors

For any type of software, the more complex it is, the more frequently programming or design errors can occur. Software vulnerabilities are program errors that users are (still) not aware of and that pose a security risk to the system. Almost daily, new vulnerabilities are found in both long-term and new software.

Clients typically install a variety of different applications, which increases the amount of vulnerabilities that can affect the system. In addition, a larger number of (mobile) clients are much more difficult to update with patch fixes than, for example, a few servers.

If software errors are not detected or not rectified immediately, this can lead to serious consequences. A software vulnerability in a widely used standard software can quickly lead to global security problems for all types of institutions.

### 2 6 Unauthorized use of IT

The identification and authentication of users should prevent a client from being used unauthorized. But also IT systems, where users have to identify and authenticate themselves via user IDs and passwords, can be used without authorization if an attacker succeeds in spying on or guessing the access data. If no screen lock is activated, the client can be used without authorization even in the case of a short-term absence.

### 2 7 Provision of unneeded operating system components and applications
When installing an operating system, it is usually possible to install optional software. Software is also regularly installed and tested during operation. With each additional application, not only the computing and memory load of a client is steadily increasing, but also the likelihood of finding vulnerabilities in it. Unnecessary software is also often not subject to regular patch management, so that known vulnerabilities are not closed promptly. This allows attackers to exploit known vulnerabilities for a long time.

### 2 8 Listening to rooms using a microphone and a camera

Many clients have a microphone and a camera. These can be used by anyone who has appropriate access rights, in networked systems also by external users. If these rights are not granted with care, unauthorized persons may misuse the microphone or camera in order to listen to rooms over the Internet or record meetings unnoticed.

3 requirements
---------------

The following are specific requirements for client protection. Basically, the * IT operation * is responsible for fulfilling the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.2.1.A1 user authentication

To use the client, users MUST authenticate themselves to the IT system. If users are to use passwords for this, secure passwords MUST be used. The passwords MUST conform to the password policy of the institution, see ORP.4 Identity and Permission Management.

#### SYS.2.1.A2 Role separation

The client MUST be set up so that normal activities do not take place with administration rights. Only administrators MAY receive administration rights. Only administrators can change the system configuration, install or remove applications, or modify or delete system files. Users MAY have read-only access to system files.

Process, conditions and requirements for administrative tasks as well as the separation of tasks between the various roles of the users of the IT system SHOULD be codified in a user and administration concept.

#### SYS.2.1.A3 Enable auto-update mechanisms

Automatic update mechanisms (auto-update) MUST be enabled unless other mechanisms such as regular manual maintenance or a central software distribution system are used for updates. If a time interval can be specified for auto-update mechanisms, you should automatically check for and install updates at least once a day.

#### SYS.2.1.A4 Regular backup
To avoid data loss, regular backups MUST be created. In most computer systems, these can be largely automated. Regulations MUST be made as to which locally stored data will be backed up by whom and when. At least the data that can not be derived from other information MUST be backed up on a regular basis. Clients MUST also be included in the institution's data protection concept. For confidential and paged backups, the backed up data SHOULD be stored encrypted. For deployed software SHOULD you decide separately whether it has to be recorded by the regular data backup. It must be regularly tested whether the backup works as desired, especially if backed up data can be easily replayed. Users SHOULD be informed about the rules of who and how backups are created.

#### SYS.2.1.A5 Screen Lock [User]

A screen lock MUST be used to prevent unauthorized access to the activated clients. It SHOULD be manually activated by the user as well as be automatically started after a specified inactivity period. It MUST be ensured that the screen lock can only be deactivated after successful user authentication.

#### SYS.2.1.A6 Use of virus protection programs

Depending on the installed operating system and other existing protection mechanisms of the client MUST be checked whether virus protection programs should be used. Concrete statements as to whether virus protection is necessary can generally be found in the operating system components of IT-Grundschutz. The corresponding signatures of a virus protection program MUST be updated regularly. In addition to real-time and on-demand scans, a solution MUST provide the ability to scan even compressed and encrypted data for malicious programs.

Virus protection programs on the clients MUST be configured so that users can neither make security-relevant changes to the settings nor deactivate them.

#### SYS.2.1.A7 logging

It MUST be decided which information should be logged on clients at least, how long the log data is stored and who can see the log data under which conditions. In general, all safety-related system events MUST be logged.

#### SYS.2.1.A8 Hedging the boot process

The starting process of the IT system ("booting") MUST be secured against manipulation. It MUST be specified from which media may be booted. It should be decided whether and how the boot process should be cryptographically protected. It MUST be ensured that only administrators can boot clients from non-default drives or external storage media. Only administrators MUST be able to boot from built-in optical or external storage media. The configuration settings of the boot process firmware MUST be changed only by users with administrative rights.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state of the art in the area of ​​general client. They SHOULD be implemented in principle.

#### SYS.2.1.A9 Setting a security policy for clients

Based on the general security policy of the institution, the requirements for general clients SHOULD be specified. The policy SHOULD be known to all users and all persons involved in the procurement and operation of the clients and should be the basis for their work. The implementation of the content required in the guideline SHOULD be regularly reviewed and the results documented in a meaningful way.
#### SYS.2.1.A10 Planning the use of clients

For the secure operation of clients SHOULD be planned in advance, where and how the clients should be used. The design should not only concern aspects that are classically linked to the term security, but also normal operational aspects that entail safety requirements. In addition to client-type-specific requirement profiles, specifications for authentication and user administration SHOULD be defined. All decisions made in the planning phase SHOULD be documented in a way that can be understood later.

#### SYS.2.1.A11 Procurement of clients

Before clients are procured, a list of requirements SHOULD be created to evaluate the products available on the market. The respective manufacturer SHOULD be able to promptly provide patches for vulnerabilities for the entire planned usage period. The systems to be sourced SHOULD have a UEFI SecureBoot firmware configuration interface and TPM (if any) that grants control by the owner (institution), enabling self-managed operation of SecureBoot and the TPM.

#### SYS.2.1.A12 Compatibility check of software

Prior to any intended acquisition of software, their compatibility with the operating system used should be checked in the present configuration and the compatibility check included in the release process of the software. If the manufacturer of the software or other specialist groups does not provide binding information on compatibility, the compatibility should be checked in a test environment. Before any intended hardware change or migration, the driver software for all affected components SHOULD be guaranteed to be compatible with the operating system.

#### SYS.2.1.A13 Access to execution environments with unobservable code execution

Access to execution environments with unobservable code execution (e.g., memory areas specially protected by the operating system, firmware areas, etc.) SHOULD only be possible by users with administrative privileges.

#### SYS.2.1.A14 Updates and patches for firmware, operating system and applications

Administrators SHOULD regularly check for known vulnerabilities. The identified vulnerabilities SHOULD be resolved as soon as possible. In general SHOULD make sure that patches and updates are obtained only from trusted sources. If necessary, the relevant applications or the operating system SHOULD be restarted after the update.

As long as patches are not available, other appropriate IT system protection measures should be taken, depending on the severity of the vulnerabilities.

#### SYS.2.1.A15 Secure installation and configuration of clients

It SHOULD be determined which components of the operating system, specialized applications and other tools should be installed. ** ** The installation and configuration of the IT systems SHOULD only be performed by authorized persons (administrators or contracted service providers) according to a defined process. All installation and configuration steps SHOULD be documented so that the installation and configuration can be reconstructed and repeated by a knowledgeable third party based on the documentation (see also SYS.2.1.A36 Operating Documentation).

The basic settings of clients SHOULD be checked and, if necessary, adjusted according to the guidelines of the security policy. Only after the installation and configuration is complete, the client SHOULD connect to the Internet.
#### SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers

After installation, SHOULD check which components of the firmware, operating system, applications, and other tools are installed and enabled on the clients. Unnecessary modules, programs, services, user IDs and interfaces SHOULD be disabled or completely uninstalled. In addition, unused runtime environments, interpreter languages ​​and compilers SHOULD be uninstalled. Corresponding, unneeded components that are firmly connected to the IT system SHOULD be disabled. Also in the firmware existing, unnecessary components (such as theft protection, remote maintenance) SHOULD be turned off. It SHOULD be prevented that these components can be reactivated. The decisions made SHOULD be documented in such a way that it is possible to understand which configuration and software equipment have been selected for the IT systems.

#### SYS.2.1.A17 deployment clearance

Before the client is used in productive operation and before it is connected to a productive network, a deployment clearance SHOULD be made. This SHOULD be documented. For the deployment clearance, the installation and configuration documentation and the functionality of the IT systems SHOULD be tested in a test. It SHOULD be done by a body authorized to do so in the institution.

#### SYS.2.1.A18 Usage of TLS [user]

Communication links SHOULD be protected by encryption as far as possible. Users SHOULD make sure that web pages use SSL / TLS.

The IT operation SHOULD make sure that the client products used support a secure version of TLS. Clients SHOULD use cryptographic algorithms and key lengths that reflect the state of the art and the security requirements of the institution.

New certificates SHOULD only be activated after checking the "fingerprint". Validation of certificates SHOULD be enabled in application programs such as browsers and email clients. Session Renegotiation and TLS Compression SHOULD be disabled.

#### SYS.2.1.A19 Restrictive rights assignment

The available functionality of the IT system SHOULD be restricted for individual users or user groups so that they have the exact rights and access to the functions they need to perform their tasks. Access authorizations SHOULD be awarded as restrictively as possible. It SHOULD be checked periodically if the permissions, especially for system directories and files, comply with the requirements of the security policy. System files SHOULD have access only to system administrators if possible. The circle of authorized administrators SHOULD be kept as small as possible. Even system directories SHOULD only provide the necessary privileges for the users.

#### SYS.2.1.A20 Protection of the administration interfaces

Depending on whether clients are administered locally, over the network or via central network-based tools, appropriate security precautions should be taken. The methods used for administration SHOULD be specified in the security policy and the administration SHOULD be performed according to the security policy. Administration over the network SHOULD be done via secure protocols.

#### SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
Access to the microphone and camera of a client SHOULD only be possible by the user as long as he works locally on the IT system. If an existing microphone or camera is not to be used and their misuse is to be prevented, they should, if possible, be switched off, covered (camera only), deactivated or physically disconnected from the device. It should be regulated how cameras and microphones are used in clients and how the rights are granted.

#### SYS.2.1.A22 Log out after task completion [User]

All users SHOULD be required to log out of the IT system or IT application after the task has been completed, especially if multiple users are using the system. If a user foresees that only a brief interruption of work is required, he SHOULD activate the screen lock instead of logging off. If technically possible, the screen lock should be automatically activated after a long period of inactivity or the user should be logged off automatically.

#### SYS.2.1.A23 Use of client-server services

If possible, dedicated server services should be used to exchange information and direct connections between clients should be avoided. If this is not possible, SHOULD specify which client-to-client services (formerly often referred to as "peer-to-peer") may be used and what information may be exchanged thereon. If necessary, users SHOULD be trained to use such services. Direct connections between clients SHOULD only be limited to the LAN. Auto-discovery protocols SHOULD be limited to the extent necessary.

#### SYS.2.1.A24 Handling of removable media in the running system

It SHOULD prevent unauthorized software from being installed on clients of drives or via interfaces or unauthorized copying of data. It SHOULD generally prevent clients from accessing data from untrusted sources. More detailed information on removable data carriers can be found in the SYS.3.4 Mobile data carrier block.

#### SYS.2.1.A25 Secure IT Use Policy [User]

A guideline SHOULD be created that transparently describes for all employees which framework conditions must be adhered to in the use of IT and which security measures have to be taken. The guideline SHOULD cover the following points:

* Security objectives of the institution
* Important terms
* Tasks and roles related to information security
* Contact for information security issues
* Safety measures to be implemented and followed by the employees
The policy SHOULD be made known to all users. Each new user SHOULD confirm the acknowledgment of the policy before being allowed to use the information technology. After major changes to the policy or after two years at the latest, a new confirmation should be required.

#### SYS.2.1.A26 Protection of applications

To make it difficult to exploit vulnerabilities in applications, ASLR and DEP / NX SHOULD be activated in the kernel and used by the applications. Security features of the kernel and standard libraries such as: B. Heap and stack protection SHOULD NOT be disabled.

#### SYS.2.1.A27 Controlled decommissioning of a client

When decommissioning a client SHOULD ensure that no important data that may be stored on the disks are lost, and that no sensitive data is left behind. It SHOULD give an overview of what data is stored on the IT systems. A checklist SHOULD be created that can be processed when decommissioning an IT system. This checklist SHOULD include at least aspects for data backup of the data that is still required and the subsequent secure deletion of all data.
### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.2.1.A28 Encryption of clients (C)

When confidential information is stored on the clients, the vulnerable files, selected file system areas, or better, the entire hard disk should be encrypted. For this purpose, a separate concept SHOULD be created and the details of the configuration should be documented with particular care, as in the case of problems, the data on the encrypted file systems may otherwise be completely lost. In this context, the following should be regulated: authentication (eg password, PIN, token), storage of recovery information, drives to encrypt, write access to unencrypted media, and how to ensure that recovery information is accessible only to authorized persons. Even encrypted files, partitions or data carriers SHOULD be backed up regularly. The used key material MUST NOT be stored in clear text on the clients.

Users SHOULD be informed about how to behave if they lose an authentication medium.

#### SYS.2.1.A29 System Monitoring (A)

The clients SHOULD be integrated into a suitable system monitoring or monitoring concept that constantly monitors the system status and the functionality of the clients and reports fault conditions as well as the exceeding of defined limit values ​​to the operating personnel.

#### SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)

For clients, a reference installation SHOULD be created in which the basic configuration and all configuration changes, updates and patches can be pre-tested by the users before importing them to the clients. In addition, such a reference installation SHOULD also be used to simplify the installation and re-installation of the clients by appropriately copying an appropriately pre-configured installation to the clients to be installed ("cloning"). For several typical and more frequently recurring test cases, checklists SHOULD be created that can be run during testing. In addition, all tests SHOULD be documented so that they can be retraced at a later date.

#### SYS.2.1.A31 Local packet filter (CIA) setup

On each computer, in addition to the central security gateways used, local packet filters SHOULD be used. As a strategy for packet filter implementation, a whitelist strategy SHOULD be chosen.

#### SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)

The IT system SHOULD include additional explicit protection against exploits (protection: mitigating successful execution). If necessary protective measures can not be met by means on board, additional suitable safety products SHOULD be used. If it is not possible to implement appropriate measures with on-board resources or a suitable security product, other appropriate (usually organizational) security measures SHOULD be taken.

#### SYS.2.1.A33 Application Whitelisting (CIA)
It should be ensured via application whitelisting that only permitted programs and scripts are executed. The rules SHOULD be made as narrow as possible. If paths and hashes can not be specified explicitly, alternatively certificate based or path rules should be used.

#### SYS.2.1.A34 Application Isolation (CIA)

Applications that manipulate external data SHOULD only be operated in a runtime environment isolated from the operating system.

#### SYS.2.1.A35 Active Management of Root Certificates (CI)

During the procurement and installation of the client SHOULD you document which root certificates are necessary for the operation of the client. The client SHOULD only contain the root certificates required for operation and previously documented. It SHOULD be checked regularly whether the existing root certificates still meet the requirements of the institution. All certificate stores on the IT system SHOULD be included in the check (e.g., UEFI certificate store, web browser certificate store, etc.).

#### SYS.2.1.A36 Self-managed use of SecureBoot and TPM

On UEFI-compatible systems, the bootloader, kernel, and any required firmware components SHOULD be signed by self-keyed key material and unwanted key material should be removed. Unless the TPM is needed it SHOULD be disabled.

#### SYS.2.1.A37 Protection against unauthorized registrations (CIA)

To prevent access to the system through compromised credentials, multi-factor authentication SHOULD be used.

#### SYS.2.1.A38 Integration into contingency planning (A)

The clients SHOULD be considered in the emergency management process. Clients are to be prioritized for recovery based on the business processes for which they are needed. It is appropriate to provide appropriate emergency procedures by creating at least recovery plans, generating system recovery boot media, and securely storing passwords and cryptographic keys.

#### SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)

With increased requirements for the availability of stationary clients, they SHOULD be connected to an uninterruptible power supply (UPS). The UPS SHOULD be sufficiently dimensioned in terms of power and support time. If changes have been made to the consumers, SHOULD check again if the support time is sufficient. Both the UPS devices and the clients SHOULD have an overvoltage protection.

The actual capacity of the battery and thus the support time of the UPS SHOULD be tested regularly. The UPS SHOULD be maintained regularly.

#### SYS.2.1.A40 Operation documentation

The execution of operational tasks on clients SHOULD be traceable documented (who, when, what?), Especially when this concerns groups of clients. In particular, configuration changes SHOULD be traceable from the documentation, including security-related tasks (for example, who is authorized to install new hard disks) SHOULD be documented. Everything that can be automatically documented SHOULD also be automatically documented. The documentation SHOULD be protected against unauthorized access and loss.

#### SYS.2.1.A41 Prevention of local hard drive overload

It SHOULD be considered setting up Quotas. Alternatively, mechanisms of the file or operating system used should be used, which warn the user at a certain fill level of the hard disk or only grant write access to the system administrator.

4 Further Information
------------------------------

### 4.1 Literature
Further information on threats and security measures in the "General Client" area can be found in the following publications, among others:

* #### [ISiClient] Securing a PC client (ISi client),

  

 (last accessed on 27.09.2017)
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/Isi-Reihe/Isi-Client/client\_node.html](https://www.bsi.bund.de/DE/Themen/ standard criteria / Isi-series / Isi client / client_node.html)

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008
 <Https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "General Client" building block.

* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.28 Software vulnerabilities or errors
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.36 Identity theft
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
* G 0.43 Importing messages
The cross reference tables can be found in the download area due to their size.
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.14 Spying out information (spying)
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.15 Listening
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.19 Disclosure of information worthy of protection
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.20 Information or products from unreliable sources
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
* G 0.21 Manipulation of hardware or software
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A40 Operation documentation
* G 0.22 Manipulation of information
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.23 Unauthorized intrusion into IT systems
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A7 logging
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.25 Failure of devices or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.26 Malfunction of equipment or systems
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A7 logging
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
* G 0.28 Software vulnerabilities or errors
  * SYS.2.1.A3 Enable auto-update mechanisms
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A38 Integration into contingency planning (A)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A36 Self-managed use of SecureBoot and TPM
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.31 Incorrect use or administration of devices and systems
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A30 Setting Up a Client Reference Installation (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A39 Uninterruptible and Stable Power Supply [Home Automation] (A)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.36 Identity theft
  * SYS.2.1.A1 user authentication
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A11 Procurement of clients
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A13 Access to execution environments with unobservable code execution
  * SYS.2.1.A14 Updates and patches for firmware, operating system and applications
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A17 deployment clearance
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A5 Screen Lock [User]
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.39 Malware
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
* G 0.40 Denial of Service
  * SYS.2.1.A6 Use of virus protection programs
  * SYS.2.1.A12 Compatibility check of software
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A31 Local packet filter (CIA) setup
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A35 Active Management of Root Certificates (CI)
* G 0.43 Importing messages
  * SYS.2.1.A18 Usage of TLS [user]
* G 0.45 data loss
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A9 Setting a security policy for clients
  * SYS.2.1.A10 Planning the use of clients
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
  * SYS.2.1.A41 Prevention of local hard drive overload
* G 0.46 Loss of integrity of sensitive information
  * SYS.2.1.A2 Role separation
  * SYS.2.1.A20 Protection of the administration interfaces
  * SYS.2.1.A21 Prevention of unauthorized use of computer microphones and cameras
  * SYS.2.1.A22 Log out after task completion [User]
  * SYS.2.1.A23 Use of client-server services
  * SYS.2.1.A24 Handling of removable media in the running system
  * SYS.2.1.A25 Secure IT Use Policy [User]
  * SYS.2.1.A26 Protection of applications
  * SYS.2.1.A27 Controlled decommissioning of a client
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A29 System Monitoring (A)
  * SYS.2.1.A4 Regular backup
  * SYS.2.1.A40 Operation documentation
  * SYS.2.1.A41 Prevention of local hard drive overload
  * SYS.2.1.A8 Hedging the boot process
  * SYS.2.1.A15 Secure installation and configuration of clients
  * SYS.2.1.A16 Disabling and uninstalling unneeded components and identifiers
  * SYS.2.1.A18 Usage of TLS [user]
  * SYS.2.1.A19 Restrictive rights assignment
  * SYS.2.1.A28 Encryption of clients (C)
  * SYS.2.1.A32 Use of Additional Exploit Prevention Measures (CIA)
  * SYS.2.1.A33 Application Whitelisting (CIA)
  * SYS.2.1.A34 Application Isolation (CIA)
  * SYS.2.1.A37 Protection against unauthorized registrations (CIA)
