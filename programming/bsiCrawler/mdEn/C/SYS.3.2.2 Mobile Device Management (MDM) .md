1 description
--------------

### 1.1 Introduction

Smartphones, tablets and phablets are an indispensable part of their work for many employees. However, IT departments need to deploy more and more such devices in many different designs, while providing adequate security. In addition, mobile devices are exposed to special risks and the administration differs fundamentally from other IT systems.

That is why Mobile Device Management (MDM) is indispensable for the controlled and secure operation of these devices, especially in institutions with a larger number of smartphones, tablets and phablets. With such a software, the terminals can be managed centrally, it can enforce security rules and emergency actions can be triggered. An MDM thus ensures the same or at least comparable safety standard on all devices.

### 1.2 Objective

The module shows how an MDM can be used to securely use mobile devices by institutions and how the MDM itself can be operated safely.

### 1.3 Delimitation

Mobile devices in the sense of this module are smartphones, tablets and phablets, on which mobile operating systems such as Android, iOS, Windows Phone and BlackBerry OS are installed. The security requirements of notebooks and tablets with desktop operating systems are described in other building blocks. Also, this module is not on how the smartphones, tablets and phablets of different manufacturers are specifically secured, as this is described in detail in the blocks for the respective operating systems, eg. Eg SYS.3.2.3 * iOS (for Enterprise) * or SYS.3.2.4 * Android. *

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in Mobile Device Management (MDM).

### 2 1 Loss of the terminal

Because mobile devices are often small and constantly being transported, they are easily forgotten, lost or stolen. In addition to the economic damage, the loss of confidentiality and integrity of the data contained weighs particularly hard. There is also the danger that attackers can access the institution's internal IT resources via a stolen mobile device.

### 2 2 Danger from malicious software

Like any device connected to the Internet, mobile devices are also threatened by malicious software. The risk of infection is even lower compared to PC operating systems, but cybercriminals are increasingly focusing on these devices. When a device becomes infected, for example, attackers can read, modify, or delete data, or gain access to the institution's internal IT resources.

### 2 3 Dangers from private use of mobile devices

When employees are given their own smartphones, tablets and phablets, there is always a risk that they will use the devices illegally privately. This creates several problems for the information security of the institution. For example, users could independently install apps that contain malicious software or visit web pages that could infect the device with malware. Similarly, user-installed apps can be a risk to the institution's information stored on the device, such as: For example, you can directly access contacts, calendars, emails, or documents. This allows data to flow away or conversely enter the institution in an uncontrolled manner. Well-known examples are social media and instant messaging apps.

### 2 4 Insufficient synchronization with the MDM
In order for the MDM to enforce the rules defined by the responsible parties on the mobile devices, the devices must be synchronized with the MDM on a regular basis. For example, if a device is not connected to the MDM for an extended period of time, new or updated rules can not be applied. Also, if there is no connection to a lost device, the data can not be deleted remotely.

### 2 5 Incorrect administration of the MDM

MDM solutions are complex applications with typically several hundred different rules. Not all rules can be combined and vice versa many rules depend on each other. Administration errors may expose endpoints to various threats that directly or indirectly affect the confidentiality, availability, or integrity of data and applications.

### 2 6 Inappropriate rights management in the MDM

The rights management of the MDM decides who should make which settings and who may access which data. If an employee is assigned an incorrect role, there is a risk that he or she will be granted too high rights. For example, he could view data without authorization or change settings on the device. It would also be possible for him to install and use apps that are not allowed in the institution, such as using cloud storage services. As a result, sensitive data can flow out of the institution, or the legal data protection regulations are violated.

### 2 7 No or weak encryption of communication between MDM and terminal

If the data connection between the mobile device and the MDM server is not encrypted at all or encrypted with outdated algorithms or if insufficient key lengths are used, the confidentiality and integrity of all transmitted data is compromised. For example, an attacker could then spend his IT system as an MDM server, gaining valuable information or changing settings on all of the institution's mobile devices.

### 2 8 Unauthorized creation of motion profiles by the MDM

With most MDM products, it is possible to determine where a device is currently located and, depending on location, data or apps can be enabled or disabled (so-called geofencing). This results in minute movement profiles of the devices and thus also the user. If these data are collected without informing the user appropriately, the persons responsible may violate data protection regulations. There is also the danger that attackers will access this data. Similarly, Geofencing can be misused to control employees inadmissible.

### 2 9 Hazards of Bring Your Own Device (BYOD)

If private devices are used for business purposes, there are various potential threats. For example, there may be legal issues regarding software licenses. In an emergency, when service data needs to be erased by the MDM on the device, it may also affect the user's private data. In addition, the IT managers can no longer check every single employee device to see if it can also be used in official business. There is a risk that inappropriate devices will be used, violating internal privacy and security requirements. In addition, users are often responsible for maintaining and repairing their personal devices. In such a repair, for example, corporate data could be viewed without authorization. The same risk exists when there is no regulation of what should happen to the data on the device when the employee leaves the institution.

3 requirements
---------------
The following are specific requirements for the protection of Mobile Device Management (MDM). Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### SYS.3.2.2.A1 Definition of a strategy for Mobile Device Management

A strategy MUST be developed that defines how employees are allowed to use mobile devices and how the devices are integrated into the institution's IT structures. The basis for this is the protection requirement of the information to be processed. The strategy MUST cover at least the following aspects:

Can the MDM be run as a cloud service?
* Should the MDM be operated by the institution itself?
* Which compliance requirements must be enforced?
* Which mobile devices and operating systems must the MDM support?
* Does the MDM solution have to be multi-client capable?
* Do cloud services have to be integrated?
* Do document management systems have to be integrated?
* Does the MDM also need to integrate and manage peripheral devices?
* Which operating model should be used: bring your own device (BYOD), personal devices (property of the institution) or non-personalized devices (property of the institution, shared)?
The strategy MUST be fixed in writing and approved by the ISB.

#### SYS.3.2.2.A2 Setting Allowed Mobile Devices

It MUST be determined which mobile devices and operating systems are allowed in the institution. All permitted devices and operating systems MUST comply with the requirements of the MDM strategy and fully comply with the institution's technical security requirements. The MDM MUST be configured to access institution-only information with shared devices. When new mobile devices are procured, they MUST be on the list of approved devices.

#### SYS.3.2.2.A3 Selection of an MDM product

If suitable MDM software is to be procured, it MUST be ensured that it meets all the requirements of the MDM strategy. It also MUST implement all technical and organizational security measures and support all approved mobile devices. Further information on purchasing can be found in the module OPS.1.2.6 * Procurement, Tendering and Purchasing *.

#### SYS.3.2.2.A4 Distribution of basic configuration to mobile devices

All mobile devices MUST be integrated into the MDM as soon as possible so that they can be configured and managed according to the institution's policies. If the devices receive the basic configuration, they MUST be in factory condition. For already used devices, all institution-related data MUST be deleted beforehand. A non-MDM terminal MUST NOT be able to access institution information.

#### SYS.3.2.2.A5 Secure basic configuration for mobile devices

All mobile devices MUST be configured to adequately meet their protection needs. For this, a suitable basic configuration MUST be compiled and documented. Details are defined in the specific device modules.

When handing over mobile devices to employees, the MDM client MUST already be installed on them. Otherwise, the users themselves MUST be able to install the client.

#### SYS.3.2.2.A6 logging
The MDM MUST log all security-related events and configuration changes. The collected data MUST NOT be viewed by unauthorized persons and MUST be stored unchangeably. In addition, legal and internal regulations MUST be adhered to during logging.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are in line with the state of the art in mobile device management (MDM). They SHOULD be implemented in principle.

#### SYS.3.2.2.A7 Select and share apps

Apps from public app stores SHOULD be reviewed and approved by those in charge. For this, a release process should be developed in which suitable evaluation criteria are defined. All shared apps SHOULD be published internally in a standard catalog and be available to users there.

#### SYS.3.2.2.A8 Definition of permitted information on mobile devices

The institution SHOULD specify which information the mobile devices may process under what conditions. The basis for the regulation SHOULD be on the one hand the classification or protection requirement of the information and on the other hand the conditions under which the data are processed on the devices, for example in sealed containers. Those responsible SHOULD configure the MDM based on these rules so that it can enforce them on all mobile devices. The users SHOULD be made aware of the rules appropriately.

#### SYS.3.2.2.A9 Selection of security apps

In order to enforce the required level of security, appropriate security apps should be selected for the terminal. The security apps SHOULD be automatically installed by the MDM.

#### SYS.3.2.2.A10 Secure connection of mobile devices to the institution

The connection of mobile devices to the network of the institution SHOULD be adequately secured. When data is transferred between the mobile devices and the IT network of the institution, appropriate measures (eg VPN) should prevent unauthorized persons from changing or viewing them.

#### SYS.3.2.2.A11 Authorization Management in MDM

For the MDM, an authorization concept SHOULD be created, documented and applied. The user groups and administrators SHOULD only grant the MDM as many authorizations as are necessary for the task fulfillment (minimum principle). It SHOULD be checked regularly to see if the assigned rights are still appropriate.

#### SYS.3.2.2.A12 Hidden MDM operating environment

The MDM itself SHOULD be protected by technical measures to meet the protection requirements of the stored or processed information. For example, the underlying operating system SHOULD be hardened and all necessary patches SHOULD be recorded.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.3.2.2.A13 Restricting the app installation via whitelist (CIA)

With increased protection requirements, the users of mobile devices SHOULD ONLY be allowed to install approved and approved apps. The MDM SHOULD prevent other apps from being installed or, alternatively, immediately remove unauthorized apps.

#### SYS.3.2.2.A14 Using external reputation services for apps (CI)
If the administrators of an institution can not select the allowed apps themselves and users can independently install apps on their devices, a so-called reputation service SHOULD be used. This is an external service that scans apps for specific criteria and provides the results as a service. The MDM SHOULD then use this information to at least limit the installation of apps.

#### SYS.3.2.2.A15 Use of PIM containers (CI)

To protect information on mobile devices from espionage apps, they SHOULD be encapsulated, for example in a PIM container. In addition, the data SHOULD be secured by a password and an encryption independent of the operating system.

#### SYS.3.2.2.A16 Use of Separate Work Environments (CI)

If employees are allowed to use personal devices privately, they should use solutions for separate work environments on the end device. If possible, only certified products (eg according to Common Criteria) should be procured for this purpose.

#### SYS.3.2.2.A17 Control of the use of mobile devices (I)

MDM solutions control how the mobile devices are used. It would be appropriate to define appropriate criteria by which to monitor the equipment without violating any legal or internal regulations.

#### SYS.3.2.2.A18 Particularly Secure Operating Systems (CIA)

There are several providers of specially secured mobile devices, some of which are certified to process information according to legal information protection classifications. If there is a very high need for protection, the institution SHOULD use such a device and integrate it into the MDM.

#### SYS.3.2.2.A19 Geofencing (CI)

Using geofencing policies it is possible to allow or prohibit certain features or apps only at predefined locations. A protection needs analysis SHOULD identify areas where these additional security measures are needed. Subsequently, they SHOULD be implemented in compliance with legal and internal regulations.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the area of ​​"Mobile Device Management (MDM)" can be found in the following publications, among others:

* #### [BSICS052] Mobile Device Management BSI-CS 052

  

 BSI, Version 1.00, 03.2013
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_052.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_052.pdf)

 
* #### [BYOD] Outline Consumerization and BYOD

  

 BSI, Version 1.2, 07.2013
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Download/Ueberblickspapier\_BYOD\_pdf.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/ DE / BSI / Grundschutz / download / Ueberblickspapier_BYOD_pdf.pdf)

 
* #### [NIST18001D] SECURING ELECTRONIC HEALTH RECORDS ON MOBILE DEVICES

  

 SPECIAL PUBLICATION 1800-1d, NIST, 07.2015
 [https://nccoe.nist.gov/sites/default/files/nccoe/NIST\_SP1800-1d\_Draft\_HIT\_Mobile-StandardsControls.pdf] (https://nccoe.nist.gov/sites/default/ files / nccoe / NIST_SP1800-1d_Draft_HIT_Mobile-StandardsControls.pdf)

 
* #### [NIST800124] Guidelines for Managing the Security of Mobile Devices in the Enterprise

  

 Special Publication 800-124 Revision 1, NIST, 06.2013
 [http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf] (http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Mobile Device Management (MDM)" building block.

* G 0.11 Failure or disruption of service providers
* G 0.13 Interception of compromising radiation
* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.16 Theft of devices, data carriers or documents
* G 0.17 Loss of equipment, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.24 Destruction of equipment or data media
* G 0.25 Failure of devices or systems
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.36 Identity theft
* G 0.37 denying actions
* G 0.38 Abuse of personal data
* G 0.39 Malware
* G 0.45 data loss
The cross reference tables can be found in the download area due to their size.
