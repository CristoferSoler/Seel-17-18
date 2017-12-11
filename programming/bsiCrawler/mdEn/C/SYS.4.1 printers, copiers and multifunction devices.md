1 description
--------------

### 1.1 Introduction

Although a great deal of information is stored digitally, paper documents can often be dispensed with. Many people also prefer to read or edit documents on paper rather than on the screen. Printers, copiers and multifunction devices will therefore be indispensable tools that can be found in virtually every office.

It is often not efficient to equip every single workstation with such a device. As a result, centralized network printers, copiers, or multifunction devices are often used to allow users to print, scan, or duplicate their documents. Since there are some drawbacks when jobs are sent from the workstation PC directly to a network printer, most institutions also use a central print server that accepts the jobs and distributes them among the available printers.

This module covers the security of networked printers, copiers, multifunction devices, print servers, and document scanners. Multifunction devices are devices that offer several different paper processing functions that print, copy and scan or enable fax services.

### 1.2 Objective

The aim of the module is to describe how printers, copiers and multifunction devices can be operated safely, so that neither information can flow away from them nor the security of internal IT networks is impaired.

### 1.3 Delimitation

Print servers can be ordinary IT systems that operate as appropriate servers. In this case, operating system-specific security requirements have to be implemented for the servers, which this module does not describe, but which can be found in the blocks SYS.1.1 * General Server * and the respective b OS-specific server blocks. Also, no security requirements are defined for the network service Samba, with which printers can be centrally provided in networks. For this, the module APP.3.4 * Samba * is to be used.

The present module does not address security requirements for clients; they are part of the SYS.2.1 General Client blocks and the respective operating system-specific client blocks.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​* printers, copiers and multifunction devices *:

### 2 1 Inadequate or incorrect supply of consumables

Many printers, copiers, and MFPs require a sufficient amount of consumables for smooth, uninterrupted operation. If these consumables are missing or incorrectly used, the operation process can be severely disturbed. For example, improper ink can contaminate an inkjet printer and cause the printer to malfunction. In emergencies, the agency's ability to act can be severely impaired and high follow-up costs can arise, for example if important contracts can not be printed out.

### 2 2 Unauthorized access to printed documentsNetwork printers often leave printed documents in the output tray for a long time. Especially if the printers are not in the immediate vicinity, users often print multiple files before collecting them all together. Since floor or departmental printers are used by many employees, unauthorized persons can also view or steal printouts containing sensitive information. This does not even have to be malicious: if, for example, employees have to wait a long time for them to print on the device, they will eventually bridge the waiting time and see what other colleagues have printed out. Also on copiers are always confidential documents that were forgotten there, for example, in the feeder.

Users often do not look for causes if they do not find their printouts at the printer. Instead, they suspect IT problems and start a new print job, as they are used to the fact that with the hardware and software always problems and inexplicable phenomena occur. However, the printouts could have been taken by others as well. Likewise, it often happens that users have accidentally selected another printer on their workstation computer. Typically, users then look for their printouts on the wrong printer, can not find them, and simply start a new print job, this time on the default printer. As a result, many network printers find misprints that are not picked up.

### 2 3 Incorrect access protection for administration

For some printers, copiers and multifunction devices, access to the administration interface can not be secured, ie it can not be protected by password prompting. With administrator rights an attacker could manipulate the devices. In some cases this is not only possible from local network workstations, but also from the Internet.

Many network printers and high-performance copiers have built-in web servers for easier administration. However, convenience comes with additional risks: often the web interface is neglected during configuration, allowing internal or even external users to manipulate printer configuration and usage. For example, any user could intentionally or unintentionally delete print jobs from others or compromise the availability of the device. Some web servers also return diagnostic data if an overlong URL is specified. Attacks can be developed with this information.

### 2 4 Abuse of the address book function

Several manufacturers have implemented an address book function for integrated e-mail or fax transmission on printers, copiers and multifunction devices. If such functions are used, it is difficult to rule out that data will be forwarded unauthorized by the printer, eg. B. the Internet.

### 2 5 Unencrypted printer communication

Printers, copiers and multifunction devices are often not controlled locally, but via a mains connection. The printer driver of the respective local computer sends all the required information directly to the printer or to a central printer server, which forwards it to a printer. This data transfer is rarely encrypted. This would allow an attacker to read directly over the network what is being printed.

Unencrypted communication interfaces for administration form another source of danger. When accessing via HTTP or Telnet, the transmitted information is transported unprotected. In that case, an attacker could read the communication and thus, for example, the password for configuration and use it for attacks on confidentiality, availability and integrity.

### 2 6 Missing power disconnectionSecurity gateways between the LAN and the Internet are often configured to enable Internet access for entire subnets. On the other hand, printers, copiers, and multifunction devices are often associated with the same subnet as the workstation PCs that print on those devices. As a result, it can happen that z. B. also the network printers can access the Internet. If the connections from and to the printers from the Internet are not rejected by the security gateways, sensitive information may be able to leave the network undesirably. Conversely, a network-capable device could also unwanted receive data from the Internet and possibly redistribute it. A network printer can thereby z. B. become a gateway for attacks from the Internet.

### 2 7 Impairment of health and the environment

Laser printers and copiers usually use dry toner, which is transferred to the paper. The dust-like toner contains not only the actual dye but also heavy metals such as lead and cadmium. This toner dust is not completely transferred to the paper, so that remnants of it can be distributed throughout the room. Even when replacing an almost empty toner cartridge toner may leak. So the fine health-damaging toner dust can be inhaled and deposited in the lungs. In addition, ozone is released on some devices during operation. However, modern devices have filters that reduce the release of ozone.

### 2 8 Evaluation of residual information

Many copiers, printers and multifunction devices are equipped with a large internal memory. If information has been stored there, even unauthorized persons may be able to access it. In the simplest case, it is only possible to print the last saved document. More problematic is when attackers can read the entire memory to analyze its contents.

Even if the stored information is deleted immediately after use, the deleted data could be reconstructed. Not every device overwrites the data in addition to the deletion again.

Often, digital copiers or printers are only rented. After a predetermined period, the device is then returned and possibly replaced with a more recent. The landlord or the next owner of the device could thus gain access to still existing information in the memory.

### 2 9 Yellow Dots

Certain printers and copiers print so-called "yellow dots" (or "machine identification codes", "tracking dots", "secret dots") on the paper, and these often undocumented watermarks may include the date and time as well as the serial number of the printer and are barely visible to the naked eye, so that an expression can be directly attributed to an institution or even a particular user and thus traced back to the author, as well as privacy issues, so unwanted information could leave the institution.

3 requirements
---------------

The following are specific requirements for printers, copiers, and multifunction devices. Basically, the * IT operation * is responsible for fulfilling the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.4.1.A1 Creation of a basic concept for the use of printers, copiers and multifunctional devices [Head IT]Before procuring printers, copiers and multifunction devices, the people responsible MUST develop a basic concept for safe use. It must be governed by where the equipment may be installed, who may access it and how it should be protected from attack.

#### SYS.4.1.A2 Suitable installation of printers, copiers and multifunction devices

Printers, copiers and multifunction devices SHOULD BE set up so that only authorized users have access to them. At a minimum, they SHOULD NOT be placed in areas where there are often outside parties, not near meeting, event or training rooms. In addition, users should be made aware that no confidential documents should be left on the devices.

#### SYS.4.1.A3 Regular update

It MUST be checked regularly to see if the printers, copiers and multifunction devices are up to date. If security holes are identified, they MUST be fixed as soon as possible. Existing patches and updates MUST be installed immediately or other security measures taken if no patches are available. Generally MUST be taken to ensure that patches and updates are obtained only from trusted sources.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of printers, copiers and multifunction devices. They SHOULD be implemented in principle.

#### SYS.4.1.A4 Planning the Use of Printers, Copiers, and Multifunction Devices [Head of IT]

Based on the concept from SYS.4.1.A1 Creation of a * basic concept for the use of printers, copiers and multifunctional devices * SHOULD specific security concepts be developed for the respective subcomponents. In it, for example, general questions SHOULD be regulated. For example: Should local or network printers be used? Who is allowed to use which functions? Which guidelines should there be? Furthermore, aspects SHOULD be regulated like

* Document access,
* Patching the devices,
* Protection of the devices,
* Availability and
* Encryption (storage and communication).
Likewise, it should be ensured that the memory of the devices is erased after they have been used. All decisions made SHOULD be documented comprehensibly.

#### SYS.4.1.A5 Create user policies for handling printers, copiers, and multifunction devices

For the safe handling of printers, copiers and multifunction devices, an administrator policy MUST be developed. For users, a leaflet MUST be created, which clearly summarizes the security guidelines for the users. The leaflet MUST be communicated to all users.

#### SYS.4.1.A6 Safe use of CUPS

If an institution uses the network-capable Common Unix Printing System (CUPS) printing system, its configuration should comply with the regulations for printers, copiers and multifunction devices. Administrative access to the CUPS server SHOULD be restricted. The print server SHOULD use (authorized) users only for printing.

#### SYS.4.1.A7 Restricting administration access to printers, copiers, and MFPs

The access to the configuration of printers, copiers and multifunction devices SHOULD be limited. If administrators configure the devices remotely, they should be protected by authentication and an encrypted connection. Likewise, all unnecessary functions of printers, copiers and multifunction devices SHOULD be turned off.

#### SYS.4.1.A8 Supply and Control of Consumables [Internal Service, User]Printers, copiers, and multifunction devices rely on consumer goods such as paper or toner to work. The supply of these consumables SHOULD be ensured. The disposal of consumer goods SHOULD be regulated. The responsibilities for this should be regulated and communicated.

#### SYS.4.1.A9 Logging on printers, copiers and multifunction devices

Activities on printers, copiers and multifunction devices SHOULD be logged. It SHOULD be tuned, what is logged, where this is stored and who evaluates this in which periods. Only authorized persons SHOULD have access to the logged information. When evaluating the logs, those in charge should comply with applicable laws and regulations, such as privacy. Unauthorized persons should NOT be able to access the log data. In addition, it should be ensured that all devices have a correct system time.

#### SYS.4.1.A10 Use of network-capable document scanners

If network-enabled scanners are used, only authorized persons should be able to access the digitized documents. The scanned information SHOULD be transmitted securely to the client of the acquirer. All memory areas of the scanner SHOULD be deleted after use. When scanning, suitable image compression methods SHOULD be used.

#### SYS.4.1.A11 Network separation when using multifunction devices

If an institution uses multifunction devices that connect directly to the telephone network, SHOULD check if the fax and modem functionality of the devices can be turned off. If this function is nevertheless used, then uncontrolled data connections between the LAN and external networks should be reliably prevented. Network-compatible printers, multifunctional devices and also document scanners SHOULD be connected in a separate network segment, which is especially separated from external networks.

#### SYS.4.1.A12 Proper Disposal of Protected Equipment [Home Technician, User]

It SHOULD be ensured and regulated that all sensitive equipment used in printers, copiers and multifunction devices is disposed of properly. In order for employees to dispose of sensitive material, appropriate disposal facilities SHOULD be in place, eg. B. Shredder.

If the material is first collected and disposed of later, it should be protected from unauthorized access. The waste management companies SHOULD regularly check to see if the disposal process is reliable.

#### SYS.4.1.A13 Safe decommissioning of printers, copiers and multifunction devices

Before * disposing, returning or replacing printers, copiers and multifunction devices *, all information on them SHOULD be safely erased. Also, the persons in charge SHOULD verify that the memory contents are actually deleted.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.4.1.A14 Authentication for printers, copiers and multifunction devices (CI)

It SHOULD use devices with an authentication option. This function SHOULD be activated and used.

#### SYS.4.1.A15 Information Protection for Printers, Copiers and Multifunction Devices (CI)With an increased protection requirement, the printers, copiers and multifunctional devices used SHOULD store information in encrypted form. Also, print jobs should only be encrypted and transferred to the devices.

Furthermore, it should be ensured by suitable mechanisms that deleted data from the device memory can not be restored. Ultimately, action should also be taken to make it harder for attackers to expand internal storage components of printers, copiers, and multifunction devices.

#### SYS.4.1.A16 Emergency Preparedness for Printers, Copiers and Multifunction Devices

The downtime of printers, copiers and multifunction devices SHOULD be as low as possible. Therefore, with higher protection needs, among others

* Have spare equipment ready,
* in maintenance contracts to ensure a reasonable response time,
* keep a list of resellers to quickly find replacement parts or parts; and
* If necessary, spare parts that are frequently needed.
4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and safety measures in the area of ​​"printers, copiers and multifunctional devices" can be found in the following publications, among others:

* #### [ACSD] Privacy and security in print infrastructures

  

 mc² management consulting GmbH, 12.2016 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/partner/161219\_mc2\_drucker\_sicherheit.pdf](https://www.allianz-fuer -cybersicherheit.de/ACS/DE/_/partner/161219_mc2_drucker_sicherheit.pdf)

 
* #### [CERT] Information about vulnerabilities and vulnerabilities in printers and related services, alert and information service

  

 CERT-Bund, (last accessed on 28.09.2017)
 <Https://www.cert-bund.de/search>

 
* #### [CSE015] Network-connected office equipment

  

 CSE 015, V1.0, Alliance for Cybersecurity, 10.2012 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_015.html](https:/ /www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_015.html)

 
* #### [CSE069] Secure passwords in embedded devices

  

 CSE 069, V1.0, Alliance for Cyber ​​Security from 12.2013 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_069.html](https:/ /www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_069.html)

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
* #### [PP0058] IEEE Standard Protection Profiles for Hardcopy Devices in IEEE Std 2600-2008

  

 Operational Environment B, IEEE Std 2600.2-2009, IEEE Computer Society, Information Assurance (C / IA) Committee, BSI-CC-PP-0058-2010, 07.2010
 [https://www.bsi.bund.de/SharedDocs/Zertifikate\_CC/PP/aktuell/PP\_0058.html](https://www.bsi.bund.de/SharedDocs/Zertifikate_CC/PP/aktuell/ PP_0058.html)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Printer, Copier and Multifunction Device" module.

* G 0.14 Spying out information (spying)
* G 0.16 Theft of devices, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.27 Resource shortage
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.37 denying actions
* G 0.39 Malware
The cross reference tables can be found in the download area due to their size.