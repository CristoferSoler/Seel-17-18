1 description
--------------

### 1.1 Introduction

In this module, devices with functions from the field of Internet of Things (IoT) are considered. In contrast to "classic" IT systems, these are "intelligent" objects that contain additional "smart" functions. IoT devices are typically connected to data networks, in many cases wirelessly, and can often access and be accessed over the Internet. This can have an impact on the information security of the entire information network.

IoT devices can be present in institutions because they are brought by employees or external, for. For example, smartwatches or wearables. In many institutions but also IoT devices are procured and operated, z. For example, devices such as fire, gas, and other alarms, coffee machines, or building control elements such as cameras and HVAC (Heating, Ventilation, and Air Conditioning).

In general, a distinction can be made between directly addressable IoT devices and IoT devices, which require a central control unit. Directly addressable devices are usually connected to a data network with their own IP address and can act autonomously or managed by a central control unit. But there are also IoT devices that only communicate directly with control units, eg. B. over wireless networks such as Bluetooth or ZigBee, and thus not directly connected to data networks. The range of these radio links can, if provided, be increased by a separate, meshed network, with each device establishing a radio link with each device.

### 1.2 Objective

The aim of this module is to secure IoT devices so that neither the security of the information and IT of their own institution nor that of outsiders is impaired. Therefore, both unauthorized data leakage and manipulation of the devices should be prevented, especially with regard to attacks on third parties.

### 1.3 Delimitation

This module is generally concerned with IoT devices and is intended to be applicable to a wide range of different IoT devices. Dedicated security features such as control and display systems or specific hardware and software architectures are not discussed in detail.

Depending on the nature of the IoT devices, the transitions to industrial control systems (ICS systems) or embedded systems are fluid. Requirements for equipment used in production and manufacturing can be found in the building blocks of the layer IND (Industrial IT).

Embedded systems are information processing systems that are integrated into a larger system or product, where they take over control, regulation and data processing tasks and are often not directly perceived by the user. For this module SYS.4.3 Embedded Systems has to be implemented.

Requirements for the radio links frequently used in the context are in the building blocks of the layer NET.2 radio networks.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in IoT devices:

### 2 1 Spying on IoT devices

In the development of IoT devices, the aspect of information security is typically a design goal that is not respected or only subordinate. Therefore, IoT devices could be abused again and again to gather information about the users or the field of application. So it has always come back to incidents with networked or IP-based surveillance cameras, z. B .:

* In 2013, several banks in different countries were compromised via surveillance cameras as part of the "Carbanak" campaign. The perpetrators captured a three-digit million amount. These attacks spied screen content and keystrokes in the financial institutions through the cameras.
* In 2014, video images and streams from 73,000 inadequately-protected webcams were made publicly available through the Insecam website.
* In 2015, 8-year-old Malware Conficker infected a variety of bodycams from various police forces.
### 2 2 Using UPnP

LAN's built-in IoT devices often connect to the Internet on their own by configuring routers in the network using UPnP (Universal Plug and Play) to provide port forwarding. The devices can then not only communicate in the local network, but are also not only visible from outside the LAN, but also accessible. If then a vulnerability in the IoT device is exploited by an attacker, this could become part of a botnet, but it could also be introduced more malicious software in the information network. This gap can theoretically be used for other activities at a later date.

### 2 3 Third Party Damage

If IoT devices are not regularly patched, known vulnerabilities remain open and can be exploited for large-scale attacks. One target of an attack could be to integrate the IoT devices into a botnet. In this case, they could be used, for example, to perform Distributed Denial of Service (DDoS) attacks and to limit the availability of services.

Example: At the end of October 2016, a DDoS attack on an Internet service provider using a botnet consisting largely of IoT devices was used. Due to the large number of devices, the so-called Mirai botnet has reached a bandwidth that goes far beyond the previously known botnets. The webcams, cameras, DVR players, routers and printers that already belonged to the botnet independently scanned the Internet for other devices to infect them with malware and add them to the botnet.

### 2 4 espionage attacks using backdoors in IoT devices

At the end of September 2016, it became known that some models of surveillance cameras and room sensors are equipped with backdoors that allow espionage. This particularly applies to surveillance cameras used in data centers and server rooms. The back doors apparently allowed access to the image and video data of the cameras and to copy this data to servers on the Internet. So z. For example, user and administration passwords may be compromised, or device configurations, infrastructure details, and other sensitive information may be accessible to third parties. This facilitates on-going attacks by taking advantage of the habits of the staff.

3 requirements
---------------

The following are specific requirements for the IoT area. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.4.4.A1 Usage criteria for IoT devices

IoT devices MUST meet a minimum of security criteria so that they can be used in institutions. The devices MUST have update features and the manufacturer MUST offer an update process. The devices MUST allow authentication. There must NOT be hard-coded access data in the device.

#### SYS.4.4.A2 authentication
To use an IoT device in an institution, an authentication MUST be activated. If passwords are used for this, secure passwords MUST be used. There should be a password policy for this. These passwords MUST be complex enough to be kept secret and changed regularly. Preset passwords MUST be changed. In addition, the use of alternative authentication mechanisms, such as. B. Certificate-based authentication.

#### SYS.4.4.A3 Regular update

It MUST be checked periodically to see if the IoT devices and associated components such as sensors or management systems are up to date. If security holes are identified, they MUST be fixed as soon as possible. Existing patches and updates MUST be installed immediately or other security measures taken if no patches are available. Generally MUST be taken to ensure that patches and updates are obtained only from trusted sources.

#### SYS.4.4.A4 Enable auto-update mechanisms

Automatic update mechanisms (auto-update) MUST be enabled unless other mechanisms such as regular manual maintenance or a central software distribution system are used for updates. If a time interval can be specified for auto-update mechanisms, you should automatically check for and install updates at least once a day.

#### SYS.4.4.A5 Network access restriction

The network access of IoT devices MUST be restricted and controlled to the minimum required. This includes:

* Traffic control at gateways, z. For example, through policies on firewalls and access control lists (ACLs) on routers. Only previously defined incoming and outgoing connections may be allowed.
* Restrictive configuration of routing on IoT devices and sensors, especially the suppression of default routes.
* Signatures on Intrusion Prevention Systems (IPS).
* The IoT devices and sensors SHOULD be operated in a separate network segment that is only allowed to communicate with the network segment for management.
* Configure virtual private networks (VPNs) between IoT device networks and sensor networks and management networks.
* UPnP function MUST be disabled on all routers.
### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of general IoT device. They SHOULD be implemented in principle.

#### SYS.4.4.A6 Inclusion of IoT devices in the security policy of the institution

In the general security policy of the institution, the requirements for IoT devices SHOULD be specified. The guideline SHOULD be known to all persons involved in the procurement and operation of IoT devices and should be the basis for their work. The implementation of the content required in the guideline SHOULD be regularly reviewed and the results documented in a meaningful way.

#### SYS.4.4.A7 Planning the use of IoT devices

For the safe operation of IoT devices SHOULD be planned in advance, where and how they should be used. Planning should not only concern aspects that are classically associated with the term information security, but also normal business aspects that entail security requirements. In this case, specifications for authentication, update mechanisms and network connection SHOULD be defined. All decisions made in the planning phase SHOULD be documented in a way that can be understood later.

#### SYS.4.4.A8 IoT Device Procurement Criteria [Information Security Officer (ISB), Procurement Agent]
The ISB SHOULD also be involved in procuring equipment that does not have obvious IT functionality. BEFORE OBTAINING IoT DEVICES, SHOULD DEFINE THE SAFETY REQUIREMENTS THAT THEY HAVE TO SATISFY. Procurement of IoT devices should take sufficient account of material security issues as well as software security requirements. A list of requirements SHOULD be created to evaluate the products available on the market. IoT devices with a cloud concept SHOULD NOT be procured.

#### SYS.4.4.A9 Control of the use of IoT devices

For each IoT device, a person responsible for the operation SHOULD be named. The responsible persons SHOULD be sufficiently informed about the handling of the IoT device. All users, users and administrators SHOULD be aware of the Code of Conduct and how to report failures, malfunctions or suspected security incidents.

#### SYS.4.4.A10 Secure installation and configuration of IoT devices

It should be determined under which conditions IoT devices are installed and configured. * * The installation and configuration of the IoT devices SHOULD only be performed by authorized persons (responsible for IoT devices, administrators or contracted service providers) according to a defined process , All installation and configuration steps SHOULD be documented so that the installation and configuration can be understood and repeated by a knowledgeable third party based on the documentation.

The basic settings of IoT devices SHOULD be reviewed and, if necessary, adjusted in accordance with the requirements of the security policy. If possible, IoT devices should first be connected to IT networks after installation and configuration is complete, especially for public networks.

#### SYS.4.4.A11 Using secure protocols

Data SHOULD only be transmitted in encrypted form. IoT devices SHOULD support an encryption-based protocol (eg SSL / TLS or SSH). If the product itself does not provide encryption, SHOULD this during commissioning, eg. B. over a Virtual Private Network (VPN), flanking be implemented.

#### SYS.4.4.A12 Secure integration with higher-level systems [Information Security Officer (ISB)]

When IoT devices are used in conjunction with higher-level management systems, they SHOULD only communicate with them.

#### SYS.4.4.A13 Disabling and uninstalling unneeded components

After installation, SHOULD check which protocols, applications, and other tools are installed and enabled on the IoT devices. Unnecessary protocols, services, user IDs and interfaces SHOULD be disabled or completely uninstalled. This applies in particular to unsafe services, such. Telnet or SNMPv1 / v2. The use of unnecessary radio interfaces, z. B. for WLAN, ZigBee, Bluetooth, SOLLTE be prevented.

If this is not possible on the device itself, unnecessary services should be restricted via the security gateway (firewall). The decisions made SHOULD be documented so that it can be reconstructed which configuration was selected for the IoT devices.

#### SYS.4.4.A14 deployment clearance

Before IoT devices are used in productive operation and before they are connected to a productive network, a deployment clearance SHOULD be made. This SHOULD be documented. For deployment clearance, the installation and configuration documentation and the functionality of the IoT devices SHOULD be tested in a test. It SHOULD be done by a body authorized to do so in the institution.

#### SYS.4.4.A15 Restrictive rights assignment
The access rights to IoT devices SHOULD be assigned as restrictively as possible. If this is not possible on the IoT devices themselves, you should consider to regulate this on the network side.

#### SYS.4.4.A16 Eliminate malware on IoT devices

The IT operation SHOULD regularly check whether the IoT devices used are infected with malicious programs and how they can be eliminated. Malware should be removed immediately. If the cause of the infection can not be remedied or a new infection can be effectively prevented, the affected IoT devices SHOULD NOT be used again.

#### SYS.4.4.A17 Monitoring the network traffic of IoT devices

It SHOULD be monitored whether network traffic is from IoT devices or sensor systems to non-management systems.

#### SYS.4.4.A18 Logging of safety-related events on IoT devices

Security relevant events SHOULD be automatically logged. If this is not possible by the IoT devices themselves, routers or other protocol mechanisms should be used. The protocols SHOULD be evaluated to a reasonable extent.

#### SYS.4.4.A19 Protection of the administration interfaces

Depending on whether IoT devices are administered locally, directly via the network or via central network-based tools, suitable security precautions should be taken. The methods used for administration SHOULD be specified in the security policy. The IoT devices SHOULD be administered according to the security policy. Administration over the network SHOULD be done via secure protocols.

#### SYS.4.4.A20 Regulated decommissioning of IoT devices

When decommissioning IoT devices, make sure that no important data that might be stored on the installed data carriers is lost, and that no sensitive data is left behind. It SHOULD give an overview of what data is stored on IoT devices. A checklist SHOULD be created that can be used when decommissioning IoT devices. This checklist SHOULD include at least aspects for data backup of the data that is still required and the subsequent secure deletion of all data.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.4.4.A21 Operating environment and power supply [Information Security Officer (ISB), Building Services] (I)

It should be clarified whether IoT devices may be operated in the envisaged operating environment (protection requirements of other systems, data protection). IoT devices SHOULD be protected from theft, destruction and manipulation in the environment of use.

It should be clarified if an IoT device has specific physical environment requirements, such as: As humidity, temperature or energy supply. If necessary, complementary infrastructure measures SHOULD be implemented.

When operating IoT devices with batteries, the regular function test and replacement of the batteries SHOULD be regulated.

IoT devices SHOULD be protected against dust and dirt according to their intended use and intended location.

#### SYS.4.4.A22 System Monitoring (A)
The IoT devices SHOULD be integrated into a suitable system monitoring or monitoring concept that constantly monitors the system status and the functionality of the IoT devices and reports fault conditions and the exceeding of defined limit values ​​to the operating personnel. If high availability of IoT devices is required, check if the devices used meet this requirement or if additional measures are required, such as setting up a cluster or purchasing standby devices.

#### SYS.4.4.A23 Auditing IoT Devices (CIA)

In safety-critical areas, all IoT devices used should be checked by experts for safety-related reasons.

#### SYS.4.4.A24 Secure Configuration and Use of an Embedded Web Server (CIA)

Web servers integrated in IoT devices SHOULD be configured as restrictively as possible. It SHOULD only the required components and functions are installed or activated. The web server SHOULD NOT be operated under a privileged account, as far as possible. Security relevant events SHOULD be logged. The access MUST be possible only after authentication. The transmission SHOULD be encrypted.

4 Further Information
------------------------------

### 4.1 Literature

More detailed information on hazards and safety measures in the area of ​​"general IoT device" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [ACS1] Security of IP-based surveillance cameras

  

 CSE 128, Version 1.0, Alliance for Cyber ​​Security, 11.2016
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_128.html](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_128.html)

 
* #### [ACS2] Espionage attacks using backdoors in security cameras and room sensors

  

 How To Protect Your Business, Expert Group Cyber ​​Security, Alliance for Cyber ​​Security, 10-2016
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/partner/161010\_expkr\_statement01.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/partner/161010_expkr_statement01.pdf)

 
* #### [DHS] Department of Homeland Security

  

 Securing the Internet of Things, 12.2016,
 <Https://www.dhs.gov/securingtheIoT>

 
* #### [OWASP] Open Web Application Security Project

  

 OWASP, (last accessed on 28.09.2017)
 <Https://www.owasp.org>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the "General IoT device" block.

* G 0.2 Unfavorable climatic conditions
* G 0.4 Pollution, dust, corrosion
* G 0.8 Failure or malfunction of the power supply
* G 0.9 Failure or malfunction of communication networks
* G 0.14 Spying out information (spying)
* G 0.16 Theft of devices, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.23 Unauthorized intrusion into IT systems
* G 0.24 Destruction of equipment or data media
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.38 Abuse of personal data
* G 0.39 Malware
* G 0.40 Denial of Service
The cross reference tables can be found in the download area due to their size.
