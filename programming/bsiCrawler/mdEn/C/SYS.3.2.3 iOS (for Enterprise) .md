1 description
--------------

### 1.1 Introduction

Mobile devices are a constant companion in today's information society. They are constantly online, that is connected to the Internet or the internal institutional network, and thus provide access to digital information at all times. Communication takes place via various interfaces, examples being GSM / UMTS / LTE, WLAN, Bluetooth.

Smartphones and tablets are widely used today due to modern, simple operating concepts and high performance. These include the Apple-produced mobile devices iPhone and iPad with the iOS operating system. Originally, these devices were designed for home use. However, due to the reorganization of infrastructures and the way in which information is collected and processed, they are increasingly being used in the professional environment and even partially replacing notebooks.

With the integration of business features, since version 4 iOS has been progressively expanded for enterprise and government use and administrative features have been integrated from an institutional perspective. These include Apple's centralized device registration program and options such as single sign-on (SSO).

### 1.2 Objective

The aim of this module is to show how devices running iOS (for Enterprise) can be safely used in institutions. For this purpose, requirements for settings of the iOS-based devices are set up, which can be distributed in the form of configuration profiles on the terminals. iOS configuration profiles contain uniformly defined settings such as: For example, security policies or individual system aspects to manage and automatically configure iOS-based devices in a consistent and centralized manner.

### 1.3 Delimitation

The building block contains basic requirements that must be observed and fulfilled when operating iOS-based devices that are integrated into the processes of the institution. Requirements for integration into the institution's security or collaboration infrastructure are not the focus of this module. With a so-called "Mobile Device Management" (MDM), it is possible to centrally manage the devices and to roll out configuration profiles for each user group or purpose. An MDM can also be used to enforce safeguards uniformly. It is assumed that the iOS-based devices are integrated into such an MDM. Requirements for the operation of such MDMs can be found in the block SYS.3.2.2 MDM. For smaller environments, the Apple Configurator can also be used to roll out the requirements listed in this module to multiple devices. General and overarching aspects of the operation of smartphones and tablets regardless of the operating system used there are found in the module SYS.3.2.1 Smartphone / Tablet.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the iOS (Apple) area:

### 2 1 Missing or bad quality of the device code (passcode)

The so-called code lock locks iOS-based devices against unauthorized access. If this feature is not activated, or if it uses an easily guessable code and can be bypassed, there is an increased risk of unauthorized access to iOS-based devices. In addition, the device code used is an essential part of the entropy of certain encryption codes.

### 2 2 Jailbreak
In the previous versions of the iOS operating system, vulnerabilities were mostly found that make it possible to undermine Apple's established security framework and thus access system processes and protected storage areas. So-called "jailbreak" exploit these vulnerabilities, for example, to be able to use alternative app stores or Apple's unwanted extensions. Jailbreaking techniques are used by attackers to install malware or perform other malicious manipulation on the iOS-based device.

### 2 3 Risk concentration through an Apple ID account for all Apple services

The Apple ID provides centralized access to all services provided by Apple (such as iMessage, FaceTime, iCloud, App Store, iTunes, iBook Store, iPhone Search, or Sync Services). If an unauthorized person gains access to an insufficiently secured Apple ID, they may be able to use these Apple services under a false identity, disrupt the availability of Apple ID-based services, remotely locate iOS-based devices or reset all data, and so on access information from the cloud service "iCloud". In particular, an attacker with activated iCloud backups can clone the stored data on their own iOS device.

### 2 4 Missing OS updates on old devices

There are regularly new versions of the iOS operating system and updates. These are typically provided for the latest device generation and for a number of older device generations (see Related Information). However, not all previous operating system versions are supplied with updates and security updates to the same extent. Subsequent known vulnerabilities in the operating system of an already discontinued device generation are no longer closed by updates.

### 2 5 Software vulnerabilities in apps

IOS apps can contain vulnerabilities that can be exploited for local attacks or attacks over network connections. In addition, many apps are no longer maintained by third-party developers after some time. As a result, there is a risk that detected security defects will not be remedied by appropriate updates.

### 2 6 Deeper integration for pre-installed apps and their functionalities

With the operating system, Apple already delivers deeply integrated and pre-installed apps (eg the "Mail" and "Clock" apps) as well as interfaces to third-party services (such as Twitter or Facebook). Some of these apps are running with higher permissions than apps downloadable from the App Store, which increases the attack surface of the iOS-based device. The use of the non-erasable or non-configurable interfaces is usually undesirable in professional use and also increases the attack surface of the device.

### 2 7 Abuse of the fingerprint sensor

The iOS operating system includes special functions that can be easily used by the Touch ID fingerprint sensor. These are z. B. the simplified activation of the device or shopping on iTunes and the App Store. This biometric security function can be handled with the appropriate effort by replicating an artificial finger based on a digitally cleaned fingerprint. Up to 48 hours after the last entry of the set passcode, the device accepts fingerprint activation, which is the maximum time window for misuse.

### 2 8 Abuse of fitness or location data on iOS

The iOS operating system includes special functions for managing fitness and location data. These data are particularly sensitive and represent an attractive target, especially when collected and stored over a long period of time.
### 2 9 Misuse of sensitive data in the locked state

The iOS operating system has a feature to display messages from enabled widgets and push messages on the lock screen. As a result, there is a risk that sensitive information of the user unprotected on the lock screen unauthorized third parties are disclosed and can be exploited. The voice assistant Siri also provides access to phone functions and contact data even when the phone is locked. This can also lead to unauthorized third parties being able to obtain sensitive information.

### 2 10 Abuse of data stored in iOS-based devices

Because of the many features and expandability options, an iOS-based device often contains sensitive data, such as: E-mails, documents, text messages, passwords, credit card information or health information. There is a risk that these data will be abused if perpetrators reach the device in the event of loss, theft or segregation or if they obtain technical access to the data.

### 2 11 Abusive access to outsourced data

For a set of iOS-specific features, the Apple-powered infrastructure must be used. When using the iCloud Keychain, iMessage, FaceTime, Siri, Continuity, Spotlight suggestions, and iCloud features to create encrypted backups or collaborate on documents, data is always synchronized between different devices or users through Apple's infrastructure. Push messages for iOS-based devices are also routed through this infrastructure. There is thus a risk that unauthorized persons access Apple servers and misuse the data stored or transmitted there for their own purposes.

### 2 12 Web-based attacks on browsers

Browsers, as well as many other iOS-based apps, can display web pages and web content. As a result, iOS-based devices may be affected by phishing attacks, drive-by exploits, and other web-based attacks.

### 2 13 Insufficient requirements for license management

Managing software licenses is one of the core tasks of IT compliance. Thus, there is a need for an institution to define clear responsibilities and regulations. However, the subject of licenses for apps is often not sufficiently considered. As part of overall compliance, the institution's officers must ensure that their employees do not commit a license violation.

3 requirements
---------------

The following are the specific requirements for iOS-based systems. Basically, the * IT operation * is responsible for fulfilling the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### SYS.3.2.3.A1 iOS usage strategy
This building block assumes that iOS devices to be managed are integrated into an MDM infrastructure. A reasonable exception, considering economic considerations, may be the management of a smaller, single-digit number of devices without the use of an MDM. If an MDM is used, the management of the devices MUST be done via the MDM for the purpose of simplified administration and the uniform presentation of security-related and other settings. For this, there must be an iOS usage strategy that defines aspects such as device selection or backup strategies. It also MUST be regulated whether additional apps should be used by third-party providers.

#### SYS.3.2.3.A2 Planning the Use of Cloud Services

iOS-based devices are basically closely interlinked with iCloud services from the manufacturer Apple, this basically already affects the activation of devices with an Apple ID. No Apple ID is required when using the Apple Device Enrollment Program (DEP). If the use of the activation lock can be dispensed with, no linking of the cloud services with a personalized Apple ID is required. Therefore, prior to using iOS-based devices, it is necessary to strategically define which cloud services should or may be used to what extent.

#### SYS.3.2.3.A3 Using the device code

Activating the device code increases the security of the data on the iOS-based device and, in addition, provides improved entropy for certain encryption codes based on the complexity of the device code. Based on the established security policy and protection needs of the data processed or stored on the iOS-based device, a reasonably complex device code MUST be used.

#### SYS.3.2.3.A4 Using the Automatic Lock Configuration Option

Based on the purpose of the application and the need for protection, the time interval for the device's "automatic lock" MUST be set to the lowest possible value. A low value ensures that no unauthorized use of the unattended device is possible. A reasonably short auto-lock period assists the user in complying with the institution's security policies, provided that the device does not linger in the unlocked state by interacting with the user interface. When defining the time period until the passcode query, the requirements for protection requirements and usability MUST be observed.

#### SYS.3.2.3.A5 Using the device locking configuration option

To prevent unauthorized access to user files on a locked device, the time period for a passcode query MUST be defined. When defining the time period until the passcode query, the requirements for protection requirements and usability MUST be observed.

#### SYS.3.2.3.A6 Using the configuration option "Maximum number of failed attempts"

In order to prevent the systematic spying of the passcode, a number of maximum possible incorrect entries of the passcode must be configured in accordance with the protection requirements. Exceeding this set value MUST automatically initialize a full local wipe on the iOS-based device.

#### SYS.3.2.3.A7 Prevent unauthorized deletion of configuration profiles

In order to prevent an unauthorized deletion of configuration profiles, suitable regulations MUST be made and implemented by those responsible. For example, the deletion can be technically realized by a password-protected authentication or organizationally prohibited.

#### SYS.3.2.3.A8 Timely update of the operating system
Apple will periodically release new versions of iOS-integrated security updates for currently supported devices. Before all the institution's iOS-based devices are updated to a new version, they MUST have been tested. The aim of this validation process is the verification of existing functions, security mechanisms and the enforceability of compliance requirements. In order to close any security gaps, an update of the installed operating system MUST be rolled out soon after it has been released to the devices. By actively participating in Apple's beta program, in most cases, the new operating system version can be pre-tested to enable timely release for those issues. Older devices that are no longer running iOS versions MUST be discarded and replaced with supported devices.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state of the art in iOS (for Enterprise). They SHOULD be implemented in principle.

#### SYS.3.2.3.A9 Using a complex device code

Based on the need for protection, a complex password SHOULD be used to maintain confidentiality. In the regulation of complexity (minimum length of the code, minimum number of special characters) a balance between usability, risk acceptance and protection needs SHOULD be maintained. For example, the regulations established in the institution for mobile work equipment (notebooks) can form the basis for the complexity to be implemented.

#### SYS.3.2.3.A10 Using the fingerprint sensor

For iOS-based devices with a biometric fingerprint sensor, the so-called Touch ID, SHOULD be released to users as an alternative to unlocking the device, while at the same time organisationally and technically regulated that the users must use more complex device codes. Along with the activation of the Touch ID, the users should be sensitized regarding the falsability of fingerprints.

#### SYS.3.2.3.A11 Using non-personalized device name

When an iOS-based device is paired with iTunes or loaded with a notebook or workstation, it will automatically display the device name, allowing you to draw conclusions about the owner or institution. To prevent the user and device password (passcode) from being guessed, the device name SHOULD NOT contain personal name and institution characteristics.

#### SYS.3.2.3.A12 Use of Institutional Apple IDs

In the terms and conditions, Apple excludes the possibility of transferring the Apple ID to another employee. For the purposes of emergency preparedness against loss of business data stored on the device itself or in the iCloud, and the ability to reuse the device, the iOS-based device SHOULD be used with an institution-based Apple ID.

As an additional precautionary measure to prevent the misuse of official means of payment (credit cards), Apple's Volume Licensing Program (VPP) SHOULD be used.

#### SYS.3.2.3.A13 Using the Restrictions on iOS Configuration Option

To ensure the confidentiality and integrity of the data processed or stored on the device, any functions or services that are not required or allowed should be disabled. Which to disable must be decided based on the purpose and underlying protection needs for the lock screen, unified communication, siri, wallpaper, host system and diagnostics and usage data.

#### SYS.3.2.3.A14 Using the iCloud infrastructure
Apple provides the iCloud infrastructure to all users with an Apple ID. So there is z. For example, share the ability to share documents and photos through iCloud infrastructure, retrieve friends' location information, or add continuity capabilities to OS X-based and iOS-based devices. Before releasing the full or selective use of the iCloud infrastructure, an assessment should be made of the compatibility of Apple's terms and conditions with its internal policies regarding availability, confidentiality, integrity and privacy. If the use of the iCloud infrastructure is allowed, the authentication on the iCloud web service SHOULD be done by a two-factor authentication. By using managed apps, iCloud usage can be reduced to a minimum or completely eliminated for purely business use.

#### SYS.3.2.3.A15 Using the continuity functions

If the use of the iCloud infrastructure has not been prohibited by the institution's security management, the compatibility of the continuity functions (AirDrop and Handoff) with the internal policies should be assessed taking into account the confidentiality and integrity aspects. On the basis of the evaluation results SHOULD be regulated to what extent technically or organisationally these functions are limited.

#### SYS.3.2.3.A16 Using the configuration option for AirPlay

AirPlay allows the user to transfer music, videos, presentations or the entire screen content of the device to an AirPlay receiver (such as the Apple TV). In order to ensure proper handling of the AirPlay function, there should be technical or organizational regulations as well as user awareness and support in the safe handling of AirPlay.

#### SYS.3.2.3.A17 Using the device code history

In order to maintain the confidentiality of the passcode used and to prevent too fast repetitions of passwords used by the user, the configuration profile SHOULD set the number of unique codes until the first retry. When establishing the value, for example, the established rules within the Windows domain or similar can be used as a basis.

#### SYS.3.2.3.A18 Using the configuration option for the Safari browser

The Safari browser is deeply integrated in iOS and has in some cases higher rights than the browsers of other providers installed from the App Store. The browser guidelines already established in the institution SHOULD be implemented accordingly for Safari through technical and organizational measures. The already established requirements for browsers on stationary and portable PCs SHOULD serve as a basis for securing the iOS-based devices, as well as the application scenarios and the application environment of the devices.

#### SYS.3.2.3.A19 Using the filtering option for web pages

If the devices are not integrated into an existing proxy and reputation infrastructure of the institution, the safari browser should use whitelist URLs by using filtering options based on allowed URLs (which are complementary to the URL groups already pre-selected by Apple) , Blacklist URLs or the integration of content filters of third parties, the fulfillment of legal regulations and internal guidelines.

If a reputation service or a proxy infrastructure is already offered by those responsible in the IT, the iOS-based devices can be integrated by depositing a global HTTP proxy for all installed browsers. When using a global, only internally accessible HTTP proxies, the integration using a VPN connection SHOULD be done either permanently or based on the apps used in the infrastructures.
#### SYS.3.2.3.A20 Integration of the devices in the internal infrastructure via VPN

To maintain the confidentiality and integrity of the institution's information, the iOS-based devices SHOULD be integrated into the infrastructure via VPN. Depending on the protection requirements, purpose and technical possibilities of the VPN server, a VPN connection based on the IKEv2, IPSec, L2TP, PPTP or SSL / TLS technologies SHOULD be implemented. The authentication SHOULD preferably be implemented and operated by one-time passwords and certificates instead of the use of classic passwords.

#### SYS.3.2.3.A21 Sharing apps and integrating the Apple App Store

If additional third-party apps are used (see SYS.3.2.3.A1), those responsible must complement the internal software approval process for validating and sharing applications (apps) from the Apple App Store. To support in-house app approval processes, the MDM used SHOULD enable filtering based on whitelists, blacklists, or app reputation services.

All shared applications SHOULD be published internally in a standard catalog and made available to users. As a supportive means of ensuring that the required apps are sufficiently available to the authorized users at the appropriate time, the integration of the volume licensing program (VPP) for Apple companies into the MDM infrastructure can be implemented. Another aspect of using the VPP is that the used Apple IDs do not have to be deposited with a form of payment. The payment confirmation of apps in the App Store MUST NOT be done with the Touch ID.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.3.2.3.A22 Enforcement of compliance requirements (CI)

Detecting a violation of the institution's regulations or even manipulating the operating system is not possible by querying an Apple-enabled interface. This task SHOULD be done by the solution provided by the MDM provider. The following actions should be taken in case of suspected violation or manipulation of the operating system. For this purpose, appropriate functions should be provided:

If a violation or manipulation is suspected, an alert must be sent to the responsible administrators and security management in the institution.

#### SYS.3.2.3.A23 Using Automatic Configuration Profile Deletion (CI)

By using the automatic configuration profile deletion SHOULD be ensured that even non-permanently accessible devices without the intervention of IT managers lose the access granted to the internal infrastructure after a defined period or on a certain day, unless the period by accessing the internal network is renewed. To ensure that the user still owns the device, this methodology can also be used preventively.

#### SYS.3.2.3.A24 Use of location-based policies (CI)
By depositing a geofencing policy SHOULD ensure that devices with information of high protection need do not leave the previously defined geographic area. Should the geographical area be left, a selective erasure of the classified information or a complete erasure of the device should be made. Before a selective or complete deletion of the device, the responsible administrators and security management as well as the user must provide information, eg. B. via push message, e-mail or SMS, about this issue. For the sake of better acceptance and to give the user the opportunity to return to the permitted geographic area, the selective or complete deletion should be delayed for a period of time temporarily. The use of geofencing policies must not violate internal and legal requirements.

#### SYS.3.2.3.A25 Using the configuration option for AirPrint (CI)

On the part of the Apple company, the AirPrint functionality was firmly integrated into the operating system. This feature can not be turned on or off. Shared AirPrint printers SHOULD be provided to the user through a configuration profile. In order to prevent users from printing information on untrusted printers, it is important to ensure that all communication links are always routed through the institution's infrastructure systems.

#### SYS.3.2.3.A26 No connection with host systems (CI)

To prevent iOS-based devices from being unauthorizedly connected to laptops, PCs, etc., users SHOULD connect iOS-based devices to the MDM only. This ensures that local backups can not be made using iTunes or similar programs. In addition, this makes attacks with the help of forensic means much more difficult or completely prevented.

#### SYS.3.2.3.A27 Using the configuration option for APN

When using an institution-specific access point to the mobile network (APN, Access Point Name) this forms the basis for the limitation of the allowed device pool. All devices using this APN will receive from the mobile service provider an IP address range agreed with the institution. To avoid security incidents caused by too short passwords for authentication, a complex password with a maximum of 64 characters SHOULD be agreed with the mobile service provider. When using an institution-related APN, authentication should be based on the CHAP protocol.

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the "iOS (for Enterprise)" area can be found in the following publications, among others:

* #### [ACSIOS] Cyber ​​Security Alliance: Recommendation on iOS - BSI-CS 074

  

 BSI, Version 1.20, 12.2015
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_074.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_074.pdf)

 
* #### [AppAGB] Terms and Conditions for iTunes

  

 Apple (last accessed on 27.09.2017)
 <Https://www.apple.com/legal/internet-services/itunes/de/terms.htm> l

 
* #### [AppAGBCl] Apple Terms iCloud

  

 Apple (last accessed on 27.09.2017)
 <Https://www.apple.com/legal/internet-services/icloud/de/terms.html>

 
* #### [AppAGBGC] Terms & Conditions for Game Center

  

 Apple (last accessed on 27.09.2017)
 <Https://www.apple.com/legal/internet-services/itunes/gamecenter/de/terms.html>

 
* #### [AppCon] Appel Configuration

  

 Apple, (last accessed on 27.09.2017)
 <Https://support.apple.com/de-de/apple-configurator>

 
* #### [AppDS] Apple Privacy Policy

  

 Apple (last accessed on 27.09.2017)
 <Https://www.apple.com/legal/privacy/de-ww/>
* #### [AppLPG] Apple's Legal Process Guidelines

  

 Apple, 06.2017
 <Https://images.apple.com/legal/privacy/law-enforcement-guidelines-outside-us.pdf>

 
* #### [AppSiup] Apple security updates

  

 Apple (last accessed on 27.09.2017)
 <Https://support.apple.com/de-de/HT201222>

 
* #### [AppViPro] Discontinued and vintage products

  

 Apple, (last accessed on 27.09.2017)
 <Https://support.apple.com/de-de/HT201624>

 
* #### [DEP] Device Registration Program

  

 Apple, (last accessed on 27.09.2017)
 <Https://www.support.apple.com/de-de/HT6578>

 
* #### [Support] Support for businesses and educational institutions

  

 Apple, (last accessed on 27.09.2017)
 <Https://www.apple.com/de/support/business-education/>

 
* #### [TR02102] Cryptographic method recommendations and key lengths

  

 BSI, (last accessed on 27.09.2017)
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)

 
* #### [VPP] Volume License Program

  

 Apple, (last accessed on 27.09.2017)
 <Https://vpp.itunes.apple.com/de/store>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "iOS (for Enterprise)" building block.

* G 0.9 Failure or malfunction of communication networks
* G 0.11 Failure or disruption of service providers
* G 0.14 Spying out information (spying)
* G 0.16 Theft of devices, data carriers or documents
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.27 Resource shortage
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.35 coercion, blackmail or corruption
* G 0.36 Identity theft
* G 0.37 denying actions
* G 0.38 Abuse of personal data
* G 0.39 Malware
* G 0.41 Sabotage
* G 0.42 Social engineering
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
