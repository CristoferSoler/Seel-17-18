1 description
--------------

### 1.1 Introduction

Smartphones are mobile phones that are equipped with a large, usually touch-sensitive display. Smartphones often combine mobile phones, media players, personal information managers and digital cameras into one device, offering users various applications and features, such as: Web browser, e-mail client or GPS. In addition, they are equipped with mobile, WLAN and Bluetooth interfaces. Tablets are, to put it simply, smartphones with a large form factor, which often can not be phoned over the mobile network. Phablets are hybrid devices made of smartphones and tablets, they are not highlighted separately in the module.

### 1.2 Objective

The aim of this module is to provide the persons responsible for security management and IT operations with information on the typical threats to smartphones and tablets. In addition, the responsible persons are to be shown approaches to create protection-relevant configuration profiles. These configuration profiles can be distributed and managed via a central infrastructure for "Mobile Device Management" (MDM). However, it can not be fundamentally assumed in the multitude of different operating systems that the devices are integrated in such an MDM.

### 1.3 Delimitation

This module is not concerned with how specific operating systems of smartphones and tablets are secured, as this is described in detail in the blocks for the respective systems, eg. For example, SYS.3.2.3 iOS (for Enterprise) or SYS.3.2.4 Android. Safety requirements for operating an MDM are described in SYS.3.2.2 Mobile Device Management.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the smartphone and tablet sector:

### 2 1 Loss of the mobile device

Because mobile devices are often small and are constantly being transported, they can easily be forgotten, lost or stolen. In addition to the economic damage, the loss of confidentiality and integrity of the data contained weighs particularly hard. An escaped mobile device could allow an attacker to access the institution's confidential information or IT resources.

### 2 2 Missing OS updates

New versions of mobile operating systems and updates are regularly released. The updates and versions of devices that have vendor-specific extensions of the operating system must first be integrated by the manufacturers in their version and then distributed. These updates are typically provided for the latest generation of devices and for a number of legacy device generations. However, not all previous operating system versions are supplied with updates and security updates to the same extent, in some cases operating systems are not further developed for economic reasons. Subsequently known vulnerabilities in the operating system of an already discontinued device generation are then no longer supplied with updates and no longer closed.

### 2 3 Software vulnerabilities in applications (apps)

Applications (apps) can contain vulnerabilities that can be exploited for local attacks or attacks over network connections. In addition, many apps are no longer maintained by third-party developers after some time. Detected security deficiencies can then not be remedied by appropriate updates.

### 2 4 Manipulation
An attacker can gain access to the devices to manipulate files. For example, he could change the configuration, start additional services, or install malware. As a result, an attacker on the manipulated system can, for example, record the communication connections (unwanted data outflow) or change the rules according to his needs (eg allow access from the Internet to the intranet).

### 2 5 Malware

Like any device connected to the Internet, mobile devices are also threatened by malicious software. The risk of infection is even lower compared to PC operating systems, but cybercriminals are increasingly focusing on these devices. When a device becomes infected, attackers can, for example, read, modify or delete data.

### 2 6 Web-based attacks on mobile browsers

Even browsers on mobile devices can display full web pages and web content. As a result, the devices may be affected by phishing attacks, drive-by exploits, and other web-based attacks.

### 2 7 Abuse of fitness or location data

The operating system of many devices usually contains special functions to manage fitness and location data. These often personal data are particularly sensitive and represent an attractive target, especially if they are collected and stored over a long period of time, insofar as these functions have been activated by the user.

As a result, the employee's location is identifiable by an attack on the device or the employee's cloud ID. In addition to the data protection effects, this can also lead to other attacks on the employee.

### 2 8 Misuse of sensitive data in the lock screen

Many mobile operating systems have a feature to display messages from enabled widgets and push messages on the lock screen. As a result, sensitive information of the user unprotected on the lock screen unauthorized third party can be disclosed and exploited.

### 2 9 Dangers from private use of mobile devices

If employees are given proprietary smartphones, tablets and phablets, they may be allowed to use the devices privately without permission. This creates several problems for the information security of the institution. So a user could independently install apps that contain malicious features or visit a web page that infects the device with malware. Likewise, many user-privately-installed apps pose a risk to the institution's information stored on the device, as they may be compromised. For example, transfer address books to unknown servers or access e-mail or documents directly. This allows data to flow away or conversely enter the institution in an uncontrolled manner. Well-known examples are social media and chat apps.

### 2 10 Dangers of Bring Your Own Device (BYOD)

If private devices are used for business purposes, legal problems may arise, for example with regard to software licenses. Even if all data needs to be erased by the MDM on the device in an emergency, the user may not agree.

Often IT managers can no longer check every single device brought by the employee to see if it can also be used in the workplace. As a result, inappropriate devices can be used, violating internal privacy and security requirements. In addition, users are often responsible for maintaining and repairing their equipment. In such a repair, for example, corporate data could be viewed without authorization. If it is not regulated what should happen to the data on the device, if the employee leaves the company, they could be abused.

3 requirements
---------------
The following are specific requirements for the smartphone and tablet sector. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.3.2.1.A1 Defining a Strategy for Smartphones and Tablets

Before an institution provides, operates or uses smartphones or tablets, the general strategy for using and controlling the devices MUST be established. Among other things, it must be determined who may access which information of the institution.

#### SYS.3.2.1.A2 Defining a strategy for cloud deployment

The institution MUST define a general strategy for cloud computing and information control as well as information protection for mobile devices. The access and use of cloud services for information of the institution MUST be clarified and determined. Users MUST be trained regularly on the use of cloud services.

#### SYS.3.2.1.A3 Secure basic configuration for mobile devices

All mobile devices MUST be configured to adequately meet the required protection requirements. For this, a suitable basic configuration MUST be compiled and documented. If an institution uses an MDM, the MDM client MUST be installed when the mobile device is handed over.

#### SYS.3.2.1.A4 Using an Access Protection [User]

All smartphones and tablets MUST be protected with a device lock code. The use of the screen lock MUST be prescribed. The display of confidential information on the lock screen MUST be disabled. All mobile devices MUST lock the screen automatically after a few minutes. The duration MUST be dependent on the protection requirement.

After several failed attempts to unlock the screen, the mobile device MUST reset itself to factory settings. The data or encryption keys SHOULD be destroyed safely.

It SHOULD be avoided that users use recently used passwords when changing passwords. The number of passwords after a password may be repeated SHOULD be specified.

It SHOULD use a complex device password.

#### SYS.3.2.1.A5 Automatic updates of operating system and apps

A process MUST be established for automatic updates of the operating system and the apps used. The updates MUST be tested. After the release, the updates MUST be rolled out in a timely manner. Already when selecting mobile devices to be procured, the institution MUST make sure that the manufacturer provides updates for the devices over the planned period of use. Older devices for which no more current versions are provided MUST be discarded and replaced with devices supported by the manufacturer.

#### SYS.3.2.1.A6 privacy settings

The access of apps and operating system to data and interfaces MUST be restricted appropriately. The privacy settings MUST be configured as restrictively as possible. In particular, access to the camera, microphone and geodata MUST be checked for compliance with the organization's privacy and security standards and restrictively configured or disabled.

#### SYS.3.2.1.A7 Code of Conduct for Security Incidents [Specialists, Users]
In general, all security incidents MUST be reported and handled. If devices are lost or if unauthorized changes to the device and software are detected, those responsible must immediately initiate suitable countermeasures.

The possible consequences of safety-critical events MUST be investigated. Ultimately, all necessary action MUST be taken to rule out access to confidential and mission-critical information of the institution.

#### SYS.3.2.1.A8 No installation of apps from insecure sources

It MUST be prevented that apps can be installed from alternative markets or from the file system.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​general smartphones and tablets. They SHOULD be implemented in principle.

#### SYS.3.2.1.A9 Use of functional extensions

Functional extensions SHOULD only be used restrictively. If possible, refrain from functional enhancements. The functional extensions SHOULD NOT have automatic access to sensitive information. You SHOULD NOT be able to bypass or change the default configuration.

#### SYS.3.2.1.A10 Mobile Employees Policy [User]

A mandatory policy for employees to use mobile devices SHOULD be created. This SHOULD determine how mobile devices should be used and maintained. In it, the topics storage and loss reporting SHOULD be dealt with. It should also be clearly forbidden to uninstall management software or to rooted the device.

#### SYS.3.2.1.A11 Encryption of the file system

The entire memory of the mobile device SHOULD be encrypted. Even existing SD cards SHOULD be encrypted.

#### SYS.3.2.1.A12 Use of non-personalized device name

The device name SHOULD NOT contain any references to the institution or the user.

#### SYS.3.2.1.A13 Screensharing and casting regulations

It SHOULD be decided whether to use screen sharing or casting. Screen sharing and casting SHOULD be organizationally or technically restricted. For this, a corresponding agreement with the users SHOULD be made.

#### SYS.3.2.1.A14 Protection against phishing and malicious programs in the browser

All mobile devices SHOULD be protected from malicious programs. In the browser used "Safe Browsing" or the function to warn against harmful content SHOULD be activated.

#### SYS.3.2.1.A15 Deactivation of download boosters

Download Boosters that route data through the manufacturer's servers SHOULD be disabled.

#### SYS.3.2.1.A16 Deactivation of unused communication interfaces [User]

Unused communication interfaces SHOULD be disabled. Necessary interfaces SHOULD only be activated in suitable environments.

#### SYS.3.2.1.A17 Using the SIM card PIN

The use of the SIM card of the institution SHOULD be protected by a PIN. The Super PIN / PUK SHOULD only be used within the framework of the defined processes by those responsible.

#### SYS.3.2.1.A18 Using a fingerprint sensor

When using a biometric fingerprint sensor, SHOULD it be checked if similar or higher protection can be achieved than with a device password. In case of doubt or worse protection, a biometric fingerprint sensor SHOULD NOT be used. Users SHOULD be made aware of the falsifiability of fingerprints.

#### SYS.3.2.1.A19 Using a language assistant

Language assistants SHOULD only be used if the function is necessary. Otherwise they SHOULD be deactivated. In general, a voice assistant SHOULD NOT be able to be used if the device is locked.
#### SYS.3.2.1.A20 Select and share apps

Apps from public app stores SHOULD be reviewed and approved by those in charge. For this, a release process should be developed in which suitable evaluation criteria are defined. All shared apps SHOULD be published internally in a standard catalog.

#### SYS.3.2.1.A21 Definition of allowed information and applications on mobile devices [Specialists, Users]

The institution SHOULD specify what information may be processed on the mobile devices. The basis for the settlement SHOULD be on the one hand the classification of the institutional data and on the other hand the conditions under which the data are processed on the devices.

Mobile device users SHOULD only install approved and verified apps from sources classified as secure.

#### SYS.3.2.1.A22 Integration of the devices in the internal infrastructure via VPN

Mobile devices SHOULD only be integrated into the institution's infrastructure via a VPN. For this, a suitable method SHOULD be selected and used. The authentication SHOULD preferably be implemented and operated by certificates instead of the use of classic passwords.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.3.2.1.A23 Additional password for confidential applications (CI)

All applications with confidential data SHOULD be protected by an additional password.

#### SYS.3.2.1.A24 Use of a closed user group (CI)

The password for the access point name (APN) of a closed user group SHOULD be complex. Authentication SHOULD use the CHAP protocol.

#### SYS.3.2.1.A25 Use of Separate Work Environments (CI)

It was intended to use solutions for separate work environments. For this, only certified products SHOULD be procured. The working data SHOULD remain in the official environment.

#### SYS.3.2.1.A26 Use of PIM containers (CIA)

Information on the mobile terminals SHOULD be encapsulated, for example in a PIM container. In addition, the data SHOULD be secured by a password and an encryption independent of the operating system.

#### SYS.3.2.1.A27 Use of Safe Operating Systems (CIA)

Institution SHOULD use a device that is certified to process information in accordance with legal information protection classifications.

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the "General Smartphones and Tablets" area can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [BSICS052] Mobile Device Management BSI-CS 052

  

 BSI, Version 1.00, 03.2013
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_052.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_052.pdf)

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NIST18001D] SECURING ELECTRONIC HEALTH RECORDS ON MOBILE DEVICES

  

 SPECIAL PUBLICATION 1800-1d, NIST, 07.2015
[https://nccoe.nist.gov/sites/default/files/nccoe/NIST\_SP1800-1d\_Draft\_HIT\_Mobile-StandardsControls.pdf] (https://nccoe.nist.gov/sites/default/ files / nccoe / NIST_SP1800-1d_Draft_HIT_Mobile-StandardsControls.pdf)

 
* #### [NIST800124] Guidelines for Managing the Security of Mobile Devices in the Enterprise

  

 Special Publication 800-124 Revision 1, NIST, 06.2013
 [http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf] (http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf)

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
* #### [TR02102] Cryptographic method recommendations and key lengths

  

 BSI, (last accessed on 27.09.2017)
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the building block "General Smartphones and Tablets".

* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.16 Theft of devices, data carriers or documents
* G 0.17 Loss of equipment, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.24 Destruction of equipment or data media
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.36 Identity theft
* G 0.37 denying actions
* G 0.38 Abuse of personal data
* G 0.39 Malware
* G 0.42 Social engineering
* G 0.43 Importing messages
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
