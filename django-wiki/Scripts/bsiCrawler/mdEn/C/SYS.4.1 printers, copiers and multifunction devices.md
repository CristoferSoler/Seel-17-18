Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Although a great deal of information is stored digitally, paper documents can often be dispensed with. Also, many people prefer to read or edit documents on paper rather than on the screen. Printers, copiers and multifunction devices will therefore be indispensable tools that can be found in virtually every office.

It is often not efficient to equip every single workstation with such a device. As a result, centralized network printers, copiers, or multifunction devices are often used to allow users to print, scan, or duplicate their documents. Since there are some drawbacks when jobs are sent from the workstation PC directly to a network printer, most institutions also use a central print server that accepts the jobs and distributes them among the available printers.

This module covers the security of networked printers, copiers, multifunction devices, print servers, and document scanners. Multifunction devices are devices that offer several different paper processing functions that print, copy and scan or enable fax services.

### 1.2 Objective

The aim of the module is to describe how printers, copiers and multifunction devices can be operated safely, so that neither information can flow away from them nor the security of the internal IT networks is impaired.

### 1.3 Delimitation

Print servers can be ordinary IT systems that operate as appropriate servers. In this case, operating system-specific security requirements have to be implemented for the servers, which this module does not describe, but which can be found in the blocks SYS.1.1 * General Server * and the respective b OS-specific server blocks. Also, no security requirements are defined for the network service Samba, with which printers can be centrally provided in networks. For this, the module APP.3.4 * Samba * is to be used.

The present module does not address security requirements for clients; they are part of the SYS.2.1 General Client blocks and the respective operating system-specific client blocks.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​* printers, copiers and multifunction devices *:

### 2 1 Inadequate or incorrect supply of consumables

Many printers, copiers, and MFPs require a sufficient amount of consumables for smooth, uninterrupted operation. If these consumables are missing or incorrectly used, the operation process can be severely disturbed. For example, improper ink can contaminate an inkjet printer and cause the printer to malfunction. In emergencies, the agency's ability to act can be severely impaired and high follow-up costs can arise, for example if important contracts can not be printed out.

### 2 2 Unauthorized access to printed documents
Network printers often leave printed documents in the output tray for a long time. Especially if the printers are not in the immediate vicinity, users often print multiple files before collecting them all together. Since floor or departmental printers are used by many employees, unauthorized persons can also view or steal printouts containing sensitive information. This does not even have to be malicious: if, for example, employees have to wait a long time for their device to print, they may be able to bridge the waiting time and see what other colleagues have printed. Also on copiers are always confidential documents that were forgotten there, for example, in the feeder.

Users often do not look for causes if they do not find their printouts at the printer. Instead, they suspect IT problems and start a new print job, as they are used to the fact that with the hardware and software always problems and inexplicable phenomena occur. However, the printouts could have been taken by others as well. Likewise, it often happens that users have accidentally selected another printer on their workstation computer. Typically, users then look for their printouts on the wrong printer, can not find them, and simply start a new print job, this time on the default printer. As a result, many network printers find misprints that are not picked up.

### 2 3 Incorrect access protection for administration

For some printers, copiers and multifunction devices, access to the administration interface can not be secured, ie it can not be protected by password prompting. With administrator rights an attacker could manipulate the devices. In some cases this is not only possible from local network workstations, but also from the Internet.

Many network printers and high-performance copiers have built-in web servers for easier administration. However, convenience comes with additional risks: often the web interface is neglected during configuration, allowing internal or even external users to manipulate printer configuration and usage. For example, any user may intentionally or unintentionally delete print jobs from others or compromise the availability of the device. Some web servers also return diagnostic data if an overlong URL is specified. Attacks can be developed with this information.

### 2 4 Abuse of the address book function

Several manufacturers have implemented an address book function for integrated e-mail or fax transmission on printers, copiers and multifunction devices. If such functions are used, it is difficult to rule out that data will be forwarded unauthorized by the printer, eg. B. the Internet.

### 2 5 Unencrypted printer communication

Printers, copiers and multifunction devices are often not controlled locally, but via a mains connection. The printer driver of the respective local computer sends all the required information directly to the printer or to a central printer server, which forwards it to a printer. This data transfer is rarely encrypted. This would allow an attacker to read directly over the network what is being printed.

Unencrypted communication interfaces for administration form another source of danger. When accessing via HTTP or Telnet, the transmitted information is transported unprotected. In that case, an attacker could read the communication and thus, for example, the password for configuration and use it for attacks on confidentiality, availability and integrity.

### 2 6 Missing power disconnection
Security gateways between the LAN and the Internet are often configured to enable Internet access for entire subnets. On the other hand, printers, copiers, and multifunction devices are often associated with the same subnet as the workstation PCs that print on those devices. As a result, it can happen that z. B. also the network printers can access the Internet. If the connections from and to the printers from the Internet are not rejected by the security gateways, sensitive information may be able to leave the network undesirably. Conversely, a network-capable device could also unwanted receive data from the Internet and possibly redistribute it. A network printer can thereby z. B. become a gateway for attacks from the Internet.

### 2 7 Impairment of health and the environment

Laser printers and copiers usually use dry toner, which is transferred to the paper. The dust-like toner contains not only the actual dye but also heavy metals such as lead and cadmium. This toner dust is not completely transferred to the paper, so that remnants of it can be distributed throughout the room. Even when replacing an almost empty toner cartridge toner may leak. So the fine health-damaging toner dust can be inhaled and deposited in the lungs. In addition, ozone is released on some devices during operation. However, modern devices have filters that reduce the release of ozone.

### 2 8 Evaluation of residual information

Many copiers, printers and multifunction devices are equipped with a large internal memory. If information has been stored there, even unauthorized persons may be able to access it. In the simplest case, it is only possible to print the last saved document. More problematic is when attackers can read the entire memory to analyze its contents.

Even if the stored information is deleted immediately after use, the deleted data could be reconstructed. Not every device overwrites the data in addition to the deletion again.

Often, digital copiers or printers are only rented. After a predetermined period, the device is then returned and possibly replaced with a more recent. The landlord or the next owner of the device could thus gain access to still existing information in the memory.

### 2 9 Yellow Dots

Certain printers and copiers print so-called "yellow dots" (or "machine identification codes", "tracking dots", "secret dots") on the paper, and these often undocumented watermarks may include the date and time as well as the serial number of the printer and are barely visible to the naked eye, so that an expression can be directly attributed to an institution or even a particular user and thus traced back to the author, as well as privacy issues, so unwanted information could leave the institution.
