1 description
--------------

### 1.1 Introduction

The basic equipment in offices typically includes copiers, printers and multifunction devices. However, it is often not efficient to equip every single workstation with a printer. Therefore, central network printers, copiers or multifunction devices are often used, on which the employees can print or duplicate their documents.

Since there are some drawbacks when jobs are sent from the workstation PC directly to a network printer, most institutions use a central print server that accepts the jobs and distributes them among the available printers.

The integration of paper processing equipment into a network is in many cases not limited to printers. For example, network-enabled document scanners can be made available to a variety of users to digitize paper documents. For example, in conjunction with a printer, a scanner may be operated like a copier.

Multifunction devices in this module are devices that offer several different paper processing functions, such as printing, copying and scanning or even fax services. For readability, not all device types are named individually. However, since security recommendations similar to those for network printers must be observed for digital copiers, the requirements apply to them analogously.

### 1.2 Life cycle

** planning and conception **

The use of network printers, copiers, and MFPs must be carefully planned (see SYS.4.1.M1 * Creating a Basic Approach to Using Printers, Copiers, and Multifunction Devices *) and SYS.4.1.M3 * Planning the Use of Printers, Copiers, and MFPs *). Chapter 3.1.2 * Managing printers * of these Implementation Notes describes in-depth information about what typical printer landscapes are and how they are designed. The security requirements for network printers must be integrated into the overall security strategy of the institution.

Many problems with printers, copiers and multifunction devices can not always be solved with technical measures. Users must be aware of and required to use a safety-conscious operation of the equipment (see SYS.4.1.M5 * Creating * * User Guidelines for Handling Printers, Copiers and Multifunction Devices *).

It should also take into account the specific requirements of certain types of equipment. These include, for example, multifunction devices (see SYS.4.1.M10 * Network separation when using multifunction devices *) and document scanners (see SYS.4.1.M9 * Use of network-capable document scanners *).

**Procurement**

Based on the application scenarios, the requirements for the products to be procured must be formulated and suitable products selected based on them. You will find useful information in chapter 3.1.1 * Criteria for the procurement and suitable selection of printers, copiers and multifunctional devices *.

**Implementation**

Once all the planning steps have been completed, it is about commissioning the devices. It also depends on where the devices are positioned (see SYS.4.1.M2 * Suitable Setup of Printers, Copiers and Multifunction Devices *) and how to restrict access to the devices (see SYS.4.1.M6 * Access Restrictions) on printers, copiers and multifunction devices *).

Like any IT system, network-enabled printers, copiers, and MFPs should be protected from unauthorized use (see SYS.4.1.M13 * Authentication for printers, copiers, and MFPs *). But also the media on which the (digital) information is transmitted and stored must be suitably secured (see SYS.4.1.M14 * Information protection for printers, copiers and multifunction devices *).
In addition to print hardware, software components, such as print servers or clients, are important for secure operation. Depending on the operating system and printing system used, appropriate requirements and modules must be implemented, such as SYS.4.1.M4 * Secure use of CUPS * or APP.3.4 * Samba *.

**Business**

In regular operation, in addition to the logging of important events (see SYS.4.1.M8 * Logging for printers, copiers and multifunction devices *), the supply of devices with consumables (see SYS.4.1.M7 * Supply and Control of Consumables *) is of great importance ,

** ** segregation

Very often in the memory of the printer, copier and multifunction devices sensitive information is stored. When disposing of the equipment, SYS.4.1.M12 * Safe Decommissioning of Printers, Copiers and Multifunction Devices * must be considered.

** Emergency Preparedness **

Aspects of contingency planning for networked printers, copiers, and multifunction devices are addressed in SYS.4.1.M15 * Emergency Preparedness for Printers, Copiers, and Multifunction Devices *.

2 measures
-----------

The following are specific implementation notes in the "Printers, Copiers, and Multifunction Devices" section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### SYS.4.1.M1 Creation of a basic concept for the use of printers, copiers and multifunction devices [Head IT]

A basic requirement for the safe use of printers, copiers and multifunction devices is adequate planning in advance. The use of the devices can be planned in several steps according to the principle of top-down design: Based on a rough concept for the overall system, concrete plans for subcomponents are defined in specific subconcepts (see also * SYS.4.1.M3 Planning the Use of Printers, copiers and multifunction devices *). The rough concept should, for example, cover the following topics:

* It is first necessary to determine where printers, copiers and multifunction devices should be installed and who can enter these rooms or access the devices.
* Furthermore, it must be regulated who gets which access rights to which network devices for which tasks.
* Printers, copiers, and multifunction devices must be protected from attack.

 
+ Through appropriate measures, physical manipulation should be counteracted. For example, if locks or seals attached to maintenance access, such as access doors, unauthorized changes can be difficult or at least recognized.
+ Likewise, attacks over networks should be made more difficult. These include, for example, unauthorized access to interfaces for remote administration via the LAN.
+ In addition, the electronic information must be protected, both during transmission to the devices and during further processing. For example, it should be considered to encrypt all documents that are stored on the hard disks of the devices (possibly only temporarily). All decisions made in the planning phase must be documented in such a way that they can be reconstructed at a later date. It is important to ensure that they are appropriately structured and understandable.


 
#### SYS.4.1.M2 Suitable installation of printers, copiers and multifunction devices
To prevent printers, copiers, or multifunction devices from being tampered with, or printing out or reading the output of unauthorized persons, the devices should be set up so that only authorized personnel have access to them. At a minimum, devices should not be located in areas where external people are often present, especially not near meeting, event or training rooms. Excluded from this are only those devices that are specifically intended for these areas, for example, in classrooms.

Often there are copiers in printer rooms. From a security point of view, it has to be questioned whether this increases the risk that the printouts lying around can be copied. To avoid such problems, it makes sense to set up printers and copiers so that they can be easily viewed by your own staff. It is better, however, to place the devices in a closed room to which only authorized persons have access. This is especially recommended for higher protection needs.

Even better, with large printers, the printouts may be distributed by a trusted person in compartments accessible only to the particular recipient. Printer output must therefore be labeled with the name of the recipient. This can be done automatically by the print programs. In the case of high protection requirements, it should be checked whether this solution is suitable.

Users often find out first at the printer that they have printed out the wrong document or that even a trifle needs to be changed. Such prints are then often thrown directly into the printer in an open wastebasket. Since confidential documents can fall into the wrong hands, it is advisable to set up a shredder next to network printers. Alternatively, users should be advised that such documents must not be left behind and otherwise destroyed.

#### SYS.4.1.M3 Regular update

It is necessary to check regularly whether the printers, copiers and multifunction devices are up-to-date. When vulnerabilities are identified, they need to be resolved as soon as possible. Existing patches and updates must be imported immediately or other security measures be taken if no patches are available. In general, it must be ensured that patches and updates are only obtained from trustworthy sources.

More detailed information is available in OPS.1.2.1. To find patch and change management.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "printers, copiers and multifunction devices".

#### SYS.4.1.M4 Planning the Use of Printers, Copiers, and Multifunction Devices [Head of IT]

Based on a rough concept for the overall system (see * SYS.4.1.M1 Creation of a basic concept for the use of printers, copiers and multifunction devices) * concrete plans for subcomponents in specific subconcepts should be defined. Planning does not only concern aspects that are classically linked to the term security, but also normal operational aspects that may entail safety requirements.

The following subconcepts should be considered when planning the use of printers, copiers, and multifunction devices:

* General aspects:
+ ** Buy or Rent: ** In some cases, it may be useful not to buy the equipment you need, but to rent it. If they are rented, it must be ensured that any documents stored in the memory are securely deleted, so that they can not be restored by the next customer who leases the device. In this case, it must first be checked whether the devices can be returned without memory or whether the memory areas can be reliably deleted without physically destroying them.
+ ** Local or network-ready printers: ** It must be decided where local and network-connected printers should be used. Often, an intermediate solution also offers advantages: Users who often have to print out sensitive information receive a local printer for these printouts. For the printouts of the remaining users or for printouts of information with a lower protection requirement, the intermediate solution provides more powerful, centralized printers.
+ ** Print Servers: ** Network printers can be accessed directly from workstations or via one or more print servers. A print server accepts the print jobs from the IT systems and forwards them to the desired printers. In addition to central administration and logging, printers can be more efficiently protected against attacks if only the print servers are allowed to access the network printers. It is a suitable solution to select.
+ ** Guidelines for Use: ** In order to be able to use printers, copiers and multifunction devices safely and effectively in institutions, security requirements must be created based on the existing security objectives as well as the requirements of the planned deployment scenarios. These specific security requirements must be aligned with the overarching security concept of the institution.
Based on this, the secure use of these devices must be regulated and security guidelines must be developed (see SYS.4.1.M5 Creation of * User guidelines for handling printers, copiers and multifunction devices *). It is important to ensure that printers, multifunctional devices and similar devices are included in security audits and that these devices are also regularly checked for compliance with the security requirements.
+ ** Distribution of privileges: ** It must be decided whether certain functions of a printer, copier or multifunction device should be restricted to selected users.
+ ** Replenishing Consumables: ** Printers, copiers, and MFPs must regularly refill consumables such as ink, toner, or paper. Regulations have to be made as to who is responsible for this and which processes must be observed (see SYS.4.1.M7 * Supply and Control of Consumables *).


 
* ** Document access regulations: ** Measures must be taken to make accessing foreign documents more difficult:

 
+ ** Security Critical Information: ** When network-critical information is frequently printed on critical printers, it must be ensured that only authorized persons can access the printouts. For example, network printers and copiers can be used where users must authenticate to print directly to the device (see SYS.4.1.M13 * Authentication for printers, copiers, and MFPs *). Alternatively, access to the printer could be limited to a few trusted individuals who distribute the printouts to the respective recipients.
+ ** Further restrictions: ** It must be clarified whether and which restrictions should apply to printer accesses. For example, it usually does not make sense for people outside the network to print to remote printers because they can not pick up their printouts directly. Also for the times, in which normally not printed, appropriate restrictions can be implemented.


 
* ** Device Protection: ** Access to network printers should be restricted (see SYS.4.1.M6 * Restricting Access to Printers, Copiers, and Multifunction Devices *):

 
+ ** Administration: ** So that unauthorized persons can not change printer settings, appropriate protective measures have to be implemented for network printers.
+ ** Physical protection: ** It should be considered to take measures against manipulation directly on the device. This includes a suitable list of printers and the protection of the interfaces.
+ ** Network-specific protection: ** For network-capable components, mechanisms must be set up to protect against attacks from the network. If IEEE 802.1X or similar network access control techniques are supported by the network printers and the network infrastructure, they should also be used. This prevents IT systems from being connected to the network without authorization. Furthermore, print servers should not be able to connect to other IT systems except for the default printers.


 
* ** Availability: ** It is recommended to take precautions against failure of print servers or individual devices. For example, maintenance contracts can reduce downtime if there are technical problems (see SYS.4.1.M15 * Emergency Preparedness for Printers, Copiers and Multifunction Devices *).
* ** Encryption: ** Requirement SYS.4.1.M14 * Information Protection for Printers, Copiers and Multifunction Devices * addresses, among other things, the following issues that play an important role in planning:

 
+ ** Hard Disk Encryption: ** Many printers and digital copiers have built-in storage media on which information is stored. If the device supports encryption, it should be used.
+ ** Encryption of communication: ** It should be considered to encrypt the communication between the workstations and the print servers as well as between the print servers and the printers.


 
* ** To clear the device memory: ** Hard drives are frequently used as temporary storage of the information to be printed on larger devices. Depending on the configuration, the information in the cache is stored not only temporarily but permanently. It should be ensured that the information is deleted from the cache after printing. Many copiers have a deletion function for this purpose. If the documents can not be deleted automatically, all users should be advised to use this feature consistently (see SYS.4.1.M5 * User Guidelines for Handling Printers, Copiers, and Multifunction Devices *).
All decisions made in the planning phase must be documented in such a way that they can be reconstructed at a later date.

#### SYS.4.1.M5 Create user policies for handling printers, copiers, and MFPs

Printers, copiers and multifunctional devices can not be secured with technical measures alone. In addition, security policies must be set for administrators and users. The administration policy should describe all the security mechanisms to be implemented for printers, copiers, and multifunction devices. This document is intended for the specialized staff of the institution.
The security guidelines for the users should be summarized in a clear leaflet. This leaflet should be hung up at all locations of the equipment.

The following aspects have to be considered:

* ** Access to the copier and printer compartments: ** If possible, access to rooms containing printers, copiers, and MFPs should be restricted (see also SYS.4.1.M2 * Suitable Setup of Printers, Copiers, and Multifunction Devices *). It makes sense to limit the access to, for example, the employees of a department or the users of a floor. The users are to be informed about the access restrictions and the authorized persons.
* ** Handling unrecovered documents: ** Often, printed documents are not picked up, printed fax transmission reports are missed or misprints are not disposed of. All users must be aware that they need to collect their printouts in a timely manner. Documents that can not be assigned to a user should be collected or better directly destroyed with a shredder.
* ** Handling sensitive documents: ** Information classified as "highly confidential" should not be printed on general accessible printers or duplicated on copiers. Officially protected documents (classified information) must be protected in accordance with applicable regulations and instructions.
* ** Authentication on the device: ** If authentication is to be carried out directly at the printer, copier or multifunction device (see SYS.4.1.M13 * Authentication for printers, copiers and multifunction devices *), users must be instructed in this procedure.
* ** Distribution of printouts: ** If network-critical information is often printed out, it should be considered to have the printouts distributed to the respective recipients by trustworthy persons. This approach is an alternative to authentication on the device and has the advantage that only these people need access to the respective printers.
* ** Selection of a standard printer: ** With several available printers or multifunctional devices, users on their client can usually preselect a standard printer for all applications. The default printer should be a logical (virtual) device such as a print preview program or a PDF generator. This protects against information being printed unnoticed, for example because the print button was accidentally pressed in an application.
* ** Clearing the copier memory by the user: ** An advantage of digital copiers is that a once-scanned document can be printed as many times as desired. To prevent unauthorized persons from accessing such information, the temporary memory used for this purpose must be deleted after use. For many copiers, users can only do this manually, so appropriate instructions and instructions must be attached to the equipment. Each user should familiarize themselves with the leaflet on how to handle printers, copiers and multifunction devices safely.
#### SYS.4.1.M6 Safe use of CUPS

Unix systems often use the network-compatible printing system * Common Unix Printing System * (CUPS) (see [CUPS]). CUPS is compatible with many other printing systems, such as * Common Internet File System / Server Message Block * (CIFS / SMB), which enables file and printer sharing on Windows.

The following aspects must be considered when using CUPS.

** General aspects **

* Local operation or central print server
CUPS can be operated as a distributed application (client on workstation PC with remote server) or locally. Accordingly, a distinction must be made in the configuration as to whether the CUPS client and the CUPS server are located on the same IT system or on different IT systems. If they are located on different IT systems, the IP address or the computer name of the respective server must be defined in the configuration file (* client.conf *) of the CUPS client. For local use, however, the loopback address (* 127.0.0.1 *) or the computer name * localhost * must be entered there. When used locally, the CUPS server must be bound to the loopback address using the configuration entry * Listen * in the * cupsd.conf * file to prevent the service from being reachable from the network. Regardless of whether only local IT systems are allowed to access the printer, CUPS can be managed centrally. Services such as SSH or the CUPS web server (see Administration section) still allow settings to be made over the network.
* Administrative and status information
 The clients must be informed regularly about the available printers and their status. In * Broadcasting *, the server sends a message to all print clients at regular intervals without being asked, and when * polling * the print client retrieves the information from the server.
 If the distribution of information about the available printers should not be done with * Polling * or * Broadcasting * but via manual entries, this must be disabled by the entry * Browsing * in * cupsd.conf * (* off *). If * browsing * is to be used, the access should only be restricted to the compulsory computers or, if necessary, to networks.
* Encryption
 If the print jobs or status requests are to be transmitted in encrypted form, a protocol must be used to support this. The * Internet Printing Protocol * (IPP) preset at CUPS can communicate encrypted through the optional use of TLS / SSL (Transport Layer Security / Secure Sockets Layer).
 Encryption requires the entry * Encryption * in the configuration file of the CUPS client (* client.conf *). It is recommended to set this value to * Always * if possible. In addition, TLS / SSL certificates and cryptographic keys must be provided on the CUPS server.
* High availability
 CUPS can be operated as part of a high-availability printing system. This requires a detailed planning of the associated organizational and technical aspects. In particular, it must be determined which basic approach is used to achieve the desired level of availability, for example * failover-switching * or * load-balancing *. For * failover-switching *, so-called implicit pressure classes must be defined in the configuration file * cupsd.conf * (configuration entry * ImplicitClasses On *). More detailed information can be found in the documentation of CUPS.
** Access to printer **

* User administration
 Print servers should only be accessible to authorized users. The required rights management can either be maintained on the print server itself or an existing authentication service can be integrated. Normal users should be able to use only the printer application on a print server and have no access to the files and directories of that server.
 Because users are typically supposed to use the print server for printing only and not want to log in directly to this server, for example, SSH, the system user group should be disconnected from the printer user group. Printer users should be set up so that they have no rights on the print server except for printing. For example, with the program call * lppasswd -a username * printer users can be created.
The assignment of which users can access which printers can be made in the * cupsd.conf * file. Here, too, the principle applies that users should only be granted the actual required access rights.
 The setting to allow all users to access all printers should be avoided. An exception in this regard is the operation of local printers. If there are only a few printer users for an IT system, and if all printer users are also system users at the same time, no separate printer users need to be created.
* Authentication method:
 CUPS supports several authentication methods, such as HTTP basic, HTTP digest, or certificate authentication. The authentication method can be defined via the entry * AuthType * in the configuration file * cupsd.conf *. Because HTTP Basic transfers usernames and passwords in plain text, this procedure should not be used without additional security. Instead, certificates or HTTP digest should be used as the authentication method.
**Administration**

CUPS may only be administered by authorized persons. These can be specified in the section * / admin * of the configuration file * cupsd.conf *.

With CUPS, numerous configuration settings can be made via a supplied web server. Access to the web server via networks should be kept to a minimum. In the configuration file * cupsd.conf * in the section * / admin * you can enter the computers that are allowed to access the web server. Alternatively, a local packet filter can be used to restrict access to the web server.

** Logging **

CUPS offers many possibilities for logging events. Many of the issues discussed in the SYS.4.1.M8 * Logging Requirements for Printers, Copiers, and Multifunction Devices * can be met by corresponding entries in the * cupsd.conf * configuration file. The level of detail of the logs can be specified, for example, by the entry * LogLevel *.

** ** archiving

CUPS offers functions for the electronic archiving of printed documents in the file system of the print server. The configuration entry * PreserveJobs * in the file * cupsd.conf * serves this purpose. As an option, the maximum number of archived documents can also be specified. Older entries will be overwritten by new documents in this case. If archives are to be created, the archived documents must be protected by appropriate mechanisms against unauthorized access and data loss. Further information can be found in the module OPS.1.2.2 * Archiving *.

#### SYS.4.1.M7 Restricting administration access to printers, copiers and multifunction devices

To complicate attacks on printers, copiers, and MFPs, access to these devices must be restricted. Here are some aspects that should be considered for the safe operation of printers and copiers:

* Restriction to necessary access rights:
 If possible, only as few administrators as needed should have full access. At the same time, only the access rights that are necessary for performing the task should be assigned.
* Security of administration accesses:
Administrative areas and configuration should only be accessible to authorized persons. The access should be possible only after an authentication, for example by a password or a PIN. If printers, copiers or multifunction devices are administrated via a network, it must be ensured that the administrators must also authenticate themselves for this. If no authentication is supported on the system side, suitable substitute measures must be taken.
* Securing the administration with remote access:
 All administration access should only take place over an encrypted channel so that no passwords or other sensitive information can be overheard. For example, some device types can encrypt the transmission of configuration data over HTTPS or SNMPv3. In this case, the unencrypted communication should be prevented, for example by deactivating the HTTP interface for the configuration.
* Abandon unnecessary functions:
 Printers, copiers and multifunction devices often offer more functions than are needed during normal operation. This can lead to unnecessary risks. Therefore, all unneeded features should be disabled or their use limited as much as possible.
* Packet filter:
 Some printers have packet filters built in to filter connections based on IP addresses or port numbers. All ports that are not required for printing and configuration of the printer should be blocked if possible. If the device supports encrypted communication, unencrypted communication with the device should be prevented as much as possible, for example via the corresponding port numbers.
 If print servers are used, make sure that only those servers can establish a connection to the printers. This makes it difficult to connect unauthorized IT systems to the printers. However, an exception are systems from which printers are to be configured. Of course, these systems must also be able to access the printer.
 The packet filters are generally to be configured as restrictively as possible. This also applies to the connection setup from network printers to other IT systems. For example, the packet filters should be configured so that network printers can not connect to an IT system outside the LAN. This complicates the unwanted exchange of data with external IT systems, for example with computers on the Internet. Regardless of local packet filters, communication between the printers and external networks must be blocked at the central security gateway.
* Network segmentation:
 Often it is recommended to combine all printers, copiers and multifunction devices in a logical network. This makes it easier to configure and administer them in many cases. If this is consistently implemented, communication between the printers and other network segments can be specifically controlled on the responsible routers and gateways (both receiving and sending IP packets).
#### SYS.4.1.M8 Supply and Control of Consumables [Internal Service, Users]

Printers, copiers, and multifunction devices rely on certain supplies (such as paper, toner, and ink) to function. Therefore, the supply of consumer goods must be ensured on site. There should be clear and unambiguous rules on which consumables are replenished or ordered by whom.

Certain resources may not be replenished or procured by any employee, but only by authorized persons, for example, very expensive products.
All users should be aware of who to notify when consumables need to be replenished or replenished. For each type of consumable, someone should be named who is responsible for supply and control. This person responsible ensures that

* regularly check if sufficient stocks are available and if they need to be topped up locally,
* the procurement office is notified in good time if consumables need to be reordered,
* used or empty consumables are disposed of properly and
* the consumables are replaced on the device if this is not to be done by the users.
The supply of consumer goods must be sufficiently ensured by the procuring entity.

#### SYS.4.1.M9 Logging on printers, copiers and multifunction devices

Activities on printers, copiers, and multifunction devices should be monitored and logged for many reasons. On the one hand, activated logging helps to identify and eliminate potential weaknesses as early as possible. On the other hand, it serves to detect violations of the security policy or to investigate a security incident. In addition, monitoring can usually also be used to detect early on whether consumables need to be refilled.

The following central questions should at least be answered when logging to printers, copiers and multifunction devices:

* What information should be logged?
* How should be logged?
* Who is authorized or responsible to evaluate the logs?
* How and when are the logs evaluated?
* Who should be notified when certain events occur?
* How long must and can the log data be kept and how is it deleted?
It must be carefully selected which information should be logged. If too much information is saved, important events could be overlooked during the evaluation. If too little is logged, important information may not be collected.

From a security point of view, the following events have proven to be particularly relevant for logging; the enumeration is sorted in descending order of priority:

* Changes to the configuration settings must always be logged.
* Failed and, in the case of a higher protection requirement, also successful authentication processes should be logged. This concerns both local applications and accesses via the network.
* System resources and operational safety measurements should always be monitored for critical values. These include, for example, information about the temperature, the load and the free space.
* To avoid bottlenecks in the supply, information on the consumption of paper and toner should be logged and evaluated.
* Entries, who printed at what time or used the device, may also be recorded, but could lead to privacy problems.
Depending on the device and application, it may be useful to set the scope of logging differently or to look at additional events, such as when a device was turned on or off. In practice, the amount of logging also depends on the extent to which the respective device type technically supports the logging of the different events.

In general, only authorized persons should be able to access the logged information. It should be prevented that e.g. On the displays of the devices or in print queue, you can see who is printing, scanning, or sending which document, or when printing, scanning, or sending which document.
After determining which information to log, it must be clarified where the log data is stored. If possible, central logging servers should be used for this. Otherwise, the log files must be stored locally on each device.

Time synchronization should be used for logging in networked IT systems. It is used to reliably compare the events with the information to be logged from other systems.

Log data not only needs to be stored but also systematically evaluated. Again, it must be determined who is responsible and which procedure is to be followed. Recommendations can be found in the module OPS.1.1.6 * Logging *.

If unexpected or conspicuous events occur in the logs, you must respond accordingly. For example, many failed authentication attempts may indicate an attack or insufficiently informed users. But even normal events may require a response: For example, if consumables reach a minimum level, they must be replaced in good time. Therefore, the responsible administrator or responsible for the consumables should be informed promptly.

If personal data is archived, the applicable laws and regulations must be complied with. These include above all the Federal Data Protection Act (BDSG) and the corresponding laws of the countries. Further information can be found in the module OPS.1.1.6 * Logging *.

#### SYS.4.1.M10 Use of network-capable document scanners

Document scanners can be used to digitize analogue information, for example to copy, archive or further process a paper document on IT systems. Instead of installing a local scanner on each workstation PC, it is usually more economical to provide one or more central scanners. In order to select suitable security measures, a distinction must be made between scan PCs and network-capable document scanners.

A scan PC is a standard PC that is often connected to a LAN and connected to a local scanner. Scan PCs are often operated in similar locations as network printers and can be used by various employees. In addition, scan PCs usually have software installed, with which the scanned information can be post-processed, such as OCR or image editing programs.

Network-compatible document scanners (* office scanners *) are compact devices that can easily read paper documents and the like and send them to the user for further processing via a LAN, for example by e-mail. This feature is often integrated with fax machines. The functionality of network-capable document scanners is usually much lower than with scan PCs.

** Scan-PC **

If a standard PC is used for scanning, the recommendations from block SYS.2.1. Implement the general client and the appropriate operating system-specific client components of the IT-Grundschutz Compendium.

Scan PCs can be operated in the production network, in a test network or as a stand-alone system without a mains connection. They should be configured so that users must authenticate themselves. The scanned data can be transferred via the network or via portable data carriers to the workstation PCs.

The analog scan templates should not be left unattended to the device. Also, the digital scan results should be deleted from all publicly accessible directories after being transferred to the desired target system, for example, the user's workstation PC.

** Networkable document scanners **
With these devices documents can be scanned even without a connected PC. The documents are converted into image files with common file formats.

For further processing, the devices must send the scanned documents to other IT systems in the network. The following transmission and storage methods are usually supported:

* File on network drives.
 The scanned documents are transferred directly to a file server via a network protocol. Usually NFS and SMB shares or transfer via FTP are supported. Basically, it must be ensured that the group of people who have access to the target directories with the scanned data is as small as possible. With increased protection, it may be necessary for only the user who scanned the information to access the scan results. Not all scanners make it possible to save the generated files in user-specific areas of the server. If only a general accessible directory can be selected, the documents must be deleted from these public directories as soon as possible. The users must be instructed accordingly. In addition, these directories should be automatically deleted once a day. The time must be announced to the users and should be chosen so that no users work with the scanners at these times.
* Scan-to-Mail:
 When scanning, the user has the option of specifying an e-mail address or a user ID to which an e-mail address is assigned. The generated file is sent to this e-mail address via a pre-set SMTP server. Since this way confidential information could leave the network anonymously, care should be taken that no external e-mail addresses can be entered. It is better to configure the SMTP server so that the network-capable document scanners can not send e-mails to external e-mail addresses.
* Scan to Print:
 Here, the document is sent directly to a printer, so the scanner-printer combination used as a digital copier. If both devices are physically separated from each other, there is a risk that the documents will be removed from the printer unauthorized during scanning. Therefore, if possible, the systems should be configured to print only when all pages of the document are fully scanned. Otherwise, there may be too much time between scanning the first page and collecting it from the printer.
* Scan-to-fax:
 The Scan to Fax procedure allows you to send scanned documents directly by fax. For this, a fax number is specified during scanning. The generated document is then either sent via an integrated modem, or the scanner establishes a connection to a fax server via the LAN.
 When using scanners that have built-in fax or modem interfaces, special precautions must be taken to prevent unwanted communication links to external networks through these interfaces. Corresponding recommendations are described in the requirement SYS.4.1.M10 * Network separation when using multifunction devices *.
 If possible, a central fax server should act as the interface between the scanner and the telephone network. In this case, in particular the measures recommendations listed in the NET.4.3 * Fax * module must be applied.
If the components used support this, the communication links should be encrypted as much as possible to make it harder for attackers to listen to the transmitted information. Information on how to protect the transmission can also be found in the requirement SYS.4.1.M14 * Information protection for printers, copiers and multifunctional devices *.

Scanners should also be protected against attacks from the network. The requirement SYS.4.1.M6 * Restricting access to printers, copiers and multifunction devices * should be taken into account.

After scanning, no residual information should remain on the system. The document memories of the device should be automatically deleted as soon as the scanning process is completed. If this is not feasible, users should be advised to manually erase the device's memory after use so subsequent users can not see the scanned information. Appropriate safety precautions must also be taken for other memory areas that are used during the scanning process, for example for the network drives used in the process.

#### SYS.4.1.M11 Network separation when using multifunction devices

Often, it is not practical from an economic or practical point of view to use separate devices for printing, scanning, copying and faxing / receiving. As an alternative, multifunction devices, also referred to as all-in-one devices, are available that support multiple or even all of these functions in one device. Some of these devices also provide additional communication interfaces, for example for web access.

Multifunction devices usually have a lower administration overhead compared with single devices and require fewer connection cables (energy and possibly also data lines). Multifunction devices can usually be connected directly or via a LAN to workstations.

Some devices provide fax and modem functionality that requires connection to a telephone network so that a physical connection between the LAN and the telephone network can be established through the link with other IT systems. If this connection is not controlled by a security gateway, uncontrolled Internet access may be possible, allowing attackers to access the LAN from outside, for example. The unauthorized establishment of data connections and unwanted remote maintenance must be prevented in any case.

An exception are multifunction devices with fax functionality that do not need to be connected to a telephone network. These devices scan documents and send them via a data connection to a central fax server, which is typically also located on the LAN. Only the fax server, which is connected to the telephone network, sends the fax to the actual receiver. If a fax server is used, the measures recommended in the NET.4.3 * Fax * block must be implemented.

If multifunction devices can be connected to a telephone network, it must first be decided whether this connection is actually required, that is, whether the corresponding fax or modem functionality is required. If the connection to the telephone network can be waived, the following protective measures should be taken as far as possible:

* The fax or modem functionality must be deactivated on the device.
* The cable for connection to the telephone network must be removed. Under no circumstances may the cable be plugged into the telephone socket.
* If the device is located in a freely accessible location, the telephone sockets in the respective room should be deactivated as far as possible or the interface to the telephone network should be removed from the device. If both are not possible, it should be checked regularly whether the connection to the telephone network has not been established without authorization.
If the fax or modem functionality of the multifunction device is to be used, it must be ensured that the connection to the telephone network required for this purpose can not lead to uncontrolled data connections between the LAN and external networks. The following approaches are possible:

* The multifunction device is connected to a stand-alone PC, that is to a computer that is not connected to the LAN. The disadvantage of this approach is that in many cases data must be transported between the stand-alone PC and the LAN using data carriers (see also SYS.3.4 Mobile data carriers).
* An alternative is to disconnect the multifunction device or the computer to which the device is connected from the LAN using an additional security gateway.
* Another alternative is to place the multifunction device or the computer to which the MFP is connected in a demilitarized zone (DMZ) of an existing security gateway.
All these solutions must be systematically considered in the security concept and require additional security measures, for example to protect against harmful code.

#### SYS.4.1.M12 Proper disposal of equipment worth protecting [Head of Building Services, User]

Resources (eg paper, hard disks, flash memory or cards, but also special toner cartridges) will eventually no longer be needed or have to be eliminated due to defects. If they contain sensitive data, they must be disposed of in such a way that no conclusions can be drawn about previously stored data. For functional media found in printers, copiers, and MFPs, the data should be physically erased. Non-functioning data media must be mechanically destroyed (see OPS.1.18 * Deleting and destruction *).

The nature of the disposal of vulnerable material should be regulated in a specific safety policy. In the institution, the necessary disposal facilities must be present, for. B. Shredder.

If sensitive material is first collected and then disposed of, the collection must be kept under lock and protected against unauthorized access.

Insofar as no environmentally sound and safe disposal can be carried out in the institution, companies assigned to it shall be obliged to comply with the required safety measures. A model contract can be found under the IT Baseline Protection tools on the BSI websites. It should be checked regularly if the disposal process is reliable.

#### SYS.4.1.M13 Safe decommissioning of printers, copiers and multifunction devices

If printers, copiers, multifunction devices or individual components of such devices are to be taken out of service or replaced, all safety-related information must be deleted from the devices (see OPS.1.18 Deleting and Destroying). This is especially true if the components are segregated and passed on to third parties. Examples include sales, return after leasing, replacement by the manufacturer and repair by a service company. But even if the devices are internally used or scrapped, all sensitive information on the devices must be erased.

In the case of rented or loaned equipment, it must first be contractually clarified whether the data carriers with the devices must be returned or how the data on the data carriers can be reliably deleted.
Depending on the purpose and type of device, the following safety-relevant information can be stored, for example:

* ** Cached Information: ** For digital copiers, the entire document is usually scanned before it is printed. Even with printers, the document is cached first. For this purpose, memory components are installed in the devices, usually in the form of hard disks. Under certain circumstances, the documents deleted in the meantime can be restored. Some devices have a feature to clear the contents of the memory.
* ** Configuration settings: ** Especially with network-capable devices, the configuration settings, such as IP addresses, may indicate the network structure. The configuration settings should therefore be deleted or reset to the factory settings. Many devices offer corresponding functions for this purpose.
* ** Passwords: ** Many devices require password- or token-based authentication, but only for administration. However, there are also devices in which authentication can be activated for all user accesses. All passwords should be reset to the delivery condition.
* ** Certificates: ** Some devices may incorporate certificate-based authentication, for example, over IEEE 802.1X. All certificates should be reset to the delivery condition.
* ** Other Remaining Information: ** Occasionally, consumables such as toner drums may be closed on the printed documents. If more protection is required, a risk assessment should be carried out to determine whether used consumables need to be destroyed.
Before devices are decommissioned or passed on to third parties, the internal memory must be deleted. If the hard disk can be removed, it is recommended to delete it separately. After the memory has been deleted, it must be checked if that was successful.

The procedure depends strongly on the type and intended use of the respective device. If particularly safety-critical information is stored on the device and it can not be guaranteed with sufficient certainty that the data is really erased, it may be necessary to physically destroy the memory or render it unusable.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### SYS.4.1.M14 Authentication for printers, copiers and multifunction devices (CI)

In everyday office life, it is often easy to view printouts of confidential documents directly at the printer, as long as they have not yet been picked up. Therefore, measures must be taken that make accessing third-party documents more difficult.

In general, only authorized persons should be able to access the printed or copied documents. The circle of authorized persons should be kept as small as possible.
If access to a network printer can not be restricted, consideration should be given to using devices that provide an authentication feature to users. If this function is activated, the document will not be printed until the user who sent the corresponding print job has identified and authenticated on the device. In practice, smart cards or PINs are often used for authentication. Depending on the device type, PINs can be specified user-specific or document-specific. In the latter variant, a PIN is set when the print job is sent. Only after this PIN has been entered on the device will the document associated with the PIN be printed out. Print jobs that have been sent but not picked up must be deleted regularly. If possible, the printers should be configured in such a way that if a wrong PIN is entered several times, the print job is automatically deleted.

Another gain in security can be achieved if the document to be printed from the workstation PC encrypted transmitted to the printer and encrypted cached. Only after a successful authentication directly at the printer will the document be decrypted and printed out.

There are also copiers that offer a similar authentication function, usually as an optional extension. Only after a chip card has been read in or a PIN has been entered can users copy. Although these authentication functions are mainly offered for cost accounting, these extensions make it more difficult for unauthorized users to make copies.

If network printers or copiers often need to print or duplicate highly confidential documents, consider using devices with authentication capabilities.

#### SYS.4.1.M15 Information Protection for Printers, Copiers and Multifunction Devices (CI)

For a printout to be created, the required information must be transferred from the workstation to the printer. For copiers, this usually takes place internally between scanner unit and memory. An attacker could try to access the memory or listen to the information as it transmits to the printer.

It should be ensured that the information is deleted from the cache after printing (see SYS.4.1.M5 * User Guidelines for Handling Printers, Copiers and Multifunction Devices * and * SYS.4.1.M3 Planning the Use of Printers, Copiers, and MFPs *). If you frequently print or copy information that requires more protection, remember that simple deletion is not enough to prevent deleted data from being restored (see OPS.1.18 Deleting and Deleting). Some devices have mechanisms for * secure deletion *. This is a deletion function which additionally overwrites the data. If such a function exists, it must be activated. Otherwise, adequate alternative solutions must be found.

Whenever possible, steps should be taken to make it harder for an attacker to physically access or expand the hard drives. To detect if an attempt was made to expand or manipulate the internal memory, the devices should be sealed. In general, printers, copiers and multifunction devices should be set up in such a way that no one can get at them unobserved.

For added protection, it is recommended to store the information encrypted in the internal storage. Many printers, copiers, and multifunction devices offer this feature. If the inserted device supports encrypted storage, this feature should be enabled.
The communication between workstations, print servers and network printers is usually via a data network for which the same hazards as with other data connections must be observed. So that this communication can not be intercepted, therefore, the print jobs should be transmitted as encrypted as possible.

Some print protocols, such as the LPR / LPD (Line Printer Remote / Line Printer Daemon) protocol, which is widely used in Unix systems, do not support encryption. The situation is similar in the case of SMB / CIFS (Server Message Block / Common Internet File System) under Windows.

Therefore, a protocol such as Internet Printing Protocol (IPP) should be chosen, which supports encryption, such as TLS / SSL (Transport Layer Security / Secure Sockets Layer) in conjunction with IPP.

On Unix systems, for example, the Common Unix Printing System (CUPS) should be used, which uses the IPP protocol for newer versions in the default setting for communication between client and print server. With a corresponding configuration TLS / SSL can be activated.

#### SYS.4.1.M16 Emergency Preparedness for Printers, Copiers, and Multifunction Devices

If printers, copiers and multifunctional devices last longer, this is intolerable for most institutions. In particular, the failure of key components required for the entire printer infrastructure significantly impacts business processes. Depending on the availability requirements, appropriate measures must therefore be taken to reduce downtime or its effects.

It is important to ensure that there is always enough consumables available, eg. As toner and paper. From a certain residual quantity, which is dependent on consumption, new consumables must be procured and provided.

Various configuration settings must be made on each copier, printer and multifunction device as well as on other components of the printing system. To be able to set up these settings quickly after a failure or replacement, the configurations must be systematically documented.

The fewer devices available, the more serious it is when a single fails. The failure of a print server is particularly problematic because these devices are often present only once or a few times.

To be able to respond to emergencies, a distinction should be made between central components on the one hand and printers, copiers and multifunction devices on the other. With a higher protection requirement regarding availability, consideration should be given to designing central components such as print servers redundantly. Otherwise, if the only central server fails, printing might not be possible across the LAN.

Decentralized components, such as printers, are often found on several floors or in different offices of a building. In general, the printer landscape should be designed so that users can easily use another printer if one printer fails.

* It should be considered to provide replacement devices for local printers who have greater protection needs for availability and are connected directly to a workstation (* cold standby *). In case of failure, the defective printer could be replaced promptly against the replacement device.
* For large copiers, printers, and multifunction devices used by multiple people, maintenance contracts should be completed with a response time appropriate to the protection needs.
* A list of resellers should be kept where new equipment can be easily obtained.
* If necessary spare parts can be stored, which are often needed. However, this only makes sense if appropriate expertise is available to replace the spare parts independently.
3 Further information
------------------------------

### 3.1 Worth knowing

** 3.1.1 Procurement criteria and appropriate selection of printers, copiers and multifunction devices **

When new printers, copiers or multifunctional devices are procured, they can be selected from the outset in such a way that a high level of security can be achieved in later operation with minimal additional personnel and organizational overhead.

Many printers and copiers are modular. The basic device can be extended by additional functions. These include, for example, additional security mechanisms, such as the support of an authentication via PINs or smart cards. Before printers, copiers and similar devices are procured, therefore, in addition to the general requirements and the security requirements are set. The requirements and the decisions taken on this basis must be documented. Here are some basic requirements for purchasing printers:

* Basic functional requirements

 
+ Should network-compatible devices be procured?
+ Is the performance of the device appropriate to the size of the users?
+ What kind of printer with which printing method should be purchased?
+ Can the device be subsequently extended with additional functions?
Many devices can be retrofitted with corresponding accessories such as network capability, duplex printing, additional paper trays and authentication.
+ Is it acceptable to leave watermarks on the printouts that allow an expression to be assigned to a specific printer ("Yellow Dots")?


 
* General security

 
+ Does the system support secure protocols for administration?
For the devices to be managed from a central location, network-capable devices must support secure protocols for administration, for example, SSL / TLS in the case of a browser-based configuration.
+ Can information be stored encrypted?
In order to prevent access to the data after an (unauthorized) removal of the hard disk, some devices encrypt the information on the hard disk.
+ Is there a possibility of authentication directly on the device (eg via password or PIN entries or chip cards) or can this function be retrofitted?
Authentication is provided for many devices, but only for the administration in some cases in order to secure access to the configuration. However, there are devices that can secure all user access, so that information is not printed until the user authenticates to the device. This serves as protection against the fact that information transmitted to a network printer or scanned on a copier can be printed out by unauthorized persons. Such a function can also be used for cost control.
+ Are eyelets or other options available to physically protect the devices from theft?
+ Can hardware manipulation be hindered by housing locks or similar precautions?
It often happens, for example, that memory modules from printers, copiers or multifunction devices can be stolen, for example.


 
* Secure memory clearing

 
+ Can the memory be deleted by the user after each copy?
Many devices have memory built in, mostly in the form of hard drives. If data is stored there unencrypted, it may be read out by unauthorized persons. In addition, there is a risk that attackers will have the pages stored in the device reprinted. Some devices therefore offer functions for clearing the memory. If possible, they should be able to be set to automatically clear after each copy.
+ Is it possible to delete the entire hard drive?
For later disposal, the entire hard disk should be deleted by overwriting. This should only be possible after an appropriate deletion command has been entered by an authorized person. Alternatively, the memory should be removed and deleted separately.
+ Will information on the display be displayed?
If possible, it should be shown on the device's display if the last saved data or the entire hard disk is deleted by overwriting.


 
* Network security

 
+ Does the device have network protection mechanisms, such as IP and port filters?
+ Does the device need to be WLAN or Bluetooth enabled, or is a wired connection sufficient?
The use of wireless technologies is associated with higher security risks than the connection via cable. Radio-based solutions therefore usually require additional security measures.
+ Does the device support the encryption of printer communication?
If the information to be printed is transmitted via a network, it should be prevented that it can be read or changed. Therefore, network protocols should be used to support encryption of the information. An example of this is the Internet Printing Protocol (IPP) in conjunction with SSL (Secure Sockets Layer) or TLS (Transport Layer Security).
+ Can the device be integrated into an existing IEEE 802.1X environment?
IEEE 802.1X enables the authentication of the terminals on the network. This protects against IT systems being operated unauthorized on the LAN.


 
* Maintainability

 
+ Does the manufacturer offer regular updates and quick security patches?
It is particularly important that the manufacturer responds promptly to known security flaws.
+ Can maintenance contracts be concluded for the product?
Often access to updates and support services of the manufacturer is only possible in conjunction with a valid maintenance contract. Can the maintenance contracts specify maximum response times for problem solving?
A maintenance contract is only suitable if the guaranteed reaction and restart times can meet the specified availability requirements.
+ Does the dealer or manufacturer provide a technical support service (hotline) that is able to help in case of problems?
This aspect should be part of a maintenance contract. When concluding the contract, it must be ensured that the hotline or support staff also speak the language of the people who will usually call there.


 
* Costs

 
+ What are the initial costs of the devices?
+ What are the anticipated ongoing costs, including maintenance, operation and support? These costs should be taken into account during the procurement phase. The content of the maintenance and support contracts should be reviewed, for example with regard to the response times, hotline and qualification of the staff.


 
** 3.1.2 Printer Management **

Institutions often need a lot of printers for their different purposes. For this purpose, suitable devices must be selected. In addition, it must be determined where the hardware components are installed.

In the following, typical printing systems, their components and communication relationships are presented. Printing systems typically consist of client and server-side software components.

** Printing Systems **
In the rarest cases, an application sends the print job directly to a printer, but a printing system operates between the application and the printer. This often requires that these printing systems are network capable and multiple clients can access a printer. Even with an exclusively local installation, a printing system is needed. The client internally sends the print job to the print server.

A printing system can fulfill the following tasks, among others:

* Acceptance of the print job from the application,
* Management of print jobs in a waiting list (spooling),
* Supplementary additional information, such as separator pages, paper size or other properties,
* Conversion into a data format understandable by the printer, such as PostScript or PCL,
* Management of logical and physical printers,
* User management and
* Logging.
Different operating systems favor different printing systems. Especially in heterogeneous IT landscapes, it is crucial that the printing systems are compatible with each other. Many systems provide interfaces to other printing systems. This allows, for example, a Unix system to access a printer managed by a Windows system.

Depending on the operating system, the following printing systems are the most widespread:

* Berkeley Printing System,
* Common Unix Printing System (CUPS) and
* Printer Sharing based on SMB on Windows.
For heterogeneous network landscapes, a print system should be selected that is supported by all operating systems. Alternatively, it may be convenient to use several different printing systems that may communicate with one another under certain circumstances. The decision on the printing systems to be used must be justified and documented.

** ingredients **

The print job that was created by an application and should be output to a printer must go through several intermediate steps. Individual components are responsible for these steps, which are presented below.

* ** print client **
 A print client is a software component that is installed on the workstation PC. Typically, the print client receives a corresponding instruction from an application and sends the print job to the print server.
 By selecting a printer name, the target printer can be selected in many cases. An exception is the expression in printer pools, where a different printer can be specified by the print server for each print job.
 Often, additional features such as duplex printing and stapling can be specified by the print client. To do this, the print client sends the print data to the print server. How the printer can be controlled and which formats it masters, is usually made known to the printing system when installing the printer.
* ** Print Server **
 The print server receives the client's print jobs and manages them. The jobs are added to a waiting list and then transferred to the printer. Depending on the configuration, the document received first is forwarded to the printer for the first time in the case of several print jobs, or it is treated preferentially by a corresponding priority. In some cases, special time periods can be set in which print jobs are executed.
* The document is usually processed directly on the print server. For this, the printing system requires the device-specific printer information and filters. For example, this printer information may be defined as a PPD (PostScript Printer Description). Generally speaking, this is a specification which formats and functions are controlled by the printer. Examples of the specified parameters are paper sizes, screen resolutions, fonts, duplex, stapling, punching and color printing. Based on this specification, the print instruction sent to the printer can be generated.
* The print server is preparing the print job. For this he converts it into a data format that is supported by the respective printer. For example, if the input format is PostScript, the document must be converted to an output format that is understandable to that printer if the printer is not PostScript-enabled. Examples of output formats are PDF, PCL and PostScript.
* ** printer **
 The printer receives the prepared document from the print server and outputs it. It is possible to distinguish between logical and physical printers. The following connection types are used in practice for physical printers:
   
 

 
+ Local Printers: These printers typically have a USB port and connect directly to a client system.
+ Network printer: The printer is addressed via a network.
+ Print server with local printers: The printer is connected locally to a print server that has a network connection. The print server can be realized in the form of an appliance or as a classic server. With this approach, the print server often needs to convert between the network and the local port, for example as a USB Ethernet bridge.


 
* Logical printers can have different tasks within the printing system. The following scenarios are common in practice:
 

 
+


- Several physical printers are addressed via a logical printer. In addition to the advantage of higher print performance (it can be printed in parallel), another printer can be accessed without major configuration overhead if one fails. It is recommended that only devices with similar properties be grouped together.
- A physical printer is addressed by multiple logical printers, each installed on different print servers. This is useful when using multiple print servers. If one print server fails, it is easy to switch to another print server so that printing can continue without much configuration.
- Furthermore, logical printers can be used to assign a separate printer name to a physical printer with several different settings. For example, for a physical printer, two logical printers can be defined: one for simplex and one for duplex printing. All logical printers must be documented.





 
** ** communication relationships

Between the individual components of a printing system, different communication connections are created.

* ** Communication between print client and print server **
 The communication link can be established between a print client and the print server and between different print servers. Depending on the scenario, the printing information is exchanged over a network or locally.
 Depending on the printing system, the following protocols can be used:

 
+ HTTP (Hypertext Transfer Protocol),
+ IPP (Internet Printing Protocol),
+ LPR / LPD (Line Printer Remote / Line Printer Daemon),
+ SMB (Server Message Block) and
+ Appletalk or Bonjour.
Depending on the printers used and the printing system selected, suitable protocols should be selected. Within a network as few as possible different printing protocols should be used. The decision has to be documented.
 Management also needs to share information on some printing systems. For example, the clients need to be regularly informed about the available printers and their status. Depending on the printing system, the following strategies can be pursued:

 
+ Broadcasting: Periodically, the server sends a message unsolicited to all clients in the broadcast domain.
+ Polling: The print client queries the information from the server.
Broadcasting simplifies the administration, but it involves further problems. If the clients and servers are in different broadcast domains, the packets do not reach all clients. In practice, problems can also occur if the print server has multiple network interfaces and sends the broadcast packets to the wrong interfaces. For the configuration a procedure has to be selected and documented.

 
* ** Communication between print server and printer **
 Appropriate protocols are also required for communication with the printers. These depend on the printer specifications and the type of connection. For example, there are protocols for

 
+ communication via the parallel interface,
+ the connection via USB,
+ the operation over the serial interface and
+ network-based communication with the printers, for example via the HP JetDirect protocol or via IPP (Internet Printing Protocol).
Some printer systems also allow you to configure the printers via the print server. In addition to proprietary protocols, the Simple Network Management Protocol (SNMP) is often used here.
 It is necessary to select protocols that are suitable for the requirements of the institution and the components to be used. The decisions have to be documented.

 
** Design of the printer landscape **

In addition to the selection of the printing system, the arrangement of the individual components, such as clients, servers and printers, plays an important role. Roughly, the following approaches to the printer architecture can be distinguished:

* Local Printers: Both the application that generates the print job and the print server and print client work together on an IT system. The printer is connected to the IT system via the USB, parallel or serial interface.
* Workstation PC with network printer: In addition to the sending application, one or more IT systems also contain the print client and the print server. The print servers of the individual IT systems send the print jobs to a network-capable printer.
* Central Print Server: Only the print clients are installed on the workstation systems. These accept the print job and forward it via a network to a central print server.
 The print jobs are managed on this print server. The print server sends the jobs to local or network-based printers where they are issued.
* Combinations: Numerous combinations of the above arrangements are possible. An example is the connection of a local printer at the workstation PC for smaller print jobs and the parallel operation of a central print server for extensive printouts.
The decisions made to build the printer landscape must be documented.

### 3.2 Literature

Further information on hazards and safety measures in the area of ​​"printers, copiers and multifunctional devices" can be found in the following publications, among others:

* #### [ACSD] Privacy and security in print infrastructures
mc² management consulting GmbH, 12.2016 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/partner/161219\_mc2\_drucker\_sicherheit.pdf](https://www.allianz-fuer -cybersicherheit.de/ACS/DE/_/partner/161219_mc2_drucker_sicherheit.pdf)

 
* #### [CERT] Information about vulnerabilities and vulnerabilities in printers and related services, alert and information service

  

 CERT-Bund, (last accessed on 28.09.2017)
 <Https://www.cert-bund.de/search>

 
* #### [CSE015] Network-connected office equipment

  

 CSE 015, V1.0, Alliance for Cybersecurity, 10.2012 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_015.html]https:/ /www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_015.html)

 
* #### [CSE069] Secure passwords in embedded devices

  

 CSE 069, V1.0, Alliance for Cyber ​​Security from 12.2013 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_069.html](https:/ /www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_069.html)

 
* #### [CUPS] Common Unix Printing System

  

 (last accessed 05.10.2017)
 <Https://www.cups.org/>

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
* #### [PP0058] IEEE Standard Protection Profiles for Hardcopy Devices in IEEE Std 2600-2008

  

 Operational Environment B, IEEE Std 2600.2-2009, IEEE Computer Society, Information Assurance (C / IA) Committee, BSI-CC-PP-0058-2010, 07.2010
 [https://www.bsi.bund.de/SharedDocs/Zertifikate\_CC/PP/aktuell/PP\_0058.html](https://www.bsi.bund.de/SharedDocs/Zertifikate_CC/PP/aktuell/ PP_0058.html)
