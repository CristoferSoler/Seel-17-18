1 description
--------------

### 1.1 Introduction

Mobile devices are a constant companion in today's information society. They are constantly online, that is, connected to the Internet or the internal institutional network, providing access to digital information at all times. The devices can communicate via various interfaces, eg. B. mobile, WLAN or Bluetooth.

Smartphones and tablets are widely used today due to modern, simple operating concepts and high performance. Originally, these devices were designed for home use. Today, however, they are also used in the professional environment.

An often used operating system for mobile phones is Android. Since version 4, Android has been gradually expanded for business use. So z. For example, it integrates features that make it easier for institutions to manage Android devices. Also, the number of policies supported by Android is increasing with each release, and there are vendor-specific extensions that allow additional policies.

### 1.2 Objective

The goal of the module is to inform about typical threats to Android-based devices and to show how Android devices can be safely used in institutions. Security policies can also be created based on the requirements listed in the module.

### 1.3 Delimitation

The module contains basic requirements that must be observed and fulfilled when operating Android-based devices. General and overall requirements for the operation of smartphones and tablets are not dealt with in this module but in SYS.3.2.1 * Smartphone and Tablet *. Also not part of this module are the requirements for the central administration of Android devices, these are listed in the block SYS 3.2.3 * MDM *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to *** *** Android:

### 2 1 Roots of the device

Many of the previous versions of Android included vulnerabilities that could override the manufacturer's established security plan. Freely available tools exploit these vulnerabilities to grant superuser privileges (root) to other apps.

These apps can then access the data of the operating system and those of other apps. Also, malicious programs use these vulnerabilities to install or manipulate the device. This allows the operating system to be used differently than intended and to bypass important security features.

Particularly access data, which stores Android in protected areas, are affected, since an app with superuser rights may be able to read these out and thus access the information stored there.

### 2 2 Malware for the Android operating system

Because of the proliferation and open architecture, Android OS devices are a popular target for malicious software. Since Android makes it relatively easy to install apps not just from the Google Play Store, but also from alternative stores or via direct download, malicious programs often spread this way. An attacker could thus infect a popular software with a malware and then make it available for download again.

### 2 3 Missing updates for the Android operating system

Many manufacturers ship smartphones and tablets with outdated versions of Android or do not provide regular or even no updates. As vulnerabilities in Android are regularly discovered, such devices are particularly vulnerable. This problem mainly affects cheap devices and smaller manufacturers, but also large manufacturers and premium models often do not provide sufficient security updates over a longer period of time.
### 2 4 Risk concentration through a user account (Google ID) for all Google services

With Google ID, users can centrally access all Google services, including: Device management, recorded geographic locations, chat software, cloud storage, play store, music, book and movie offerings, backup, bookmarks, web page password storage, and synchronization services. Many other Internet service providers also use the Google ID to authenticate users.

If an attacker can authenticate himself through the Google ID, he can use all of these services under the stolen identity. It can also access all data stored there and remotely locate or reset devices, thus erasing all data on the device.

### 2 5 Integration for preinstalled apps and their functionality on Android-based devices

With the operating system, manufacturers often ship deeply integrated and pre-installed apps (such as the Play Store and associated Play Services) and interfaces to third-party services (Twitter, Facebook, etc.). Some of these apps can not be removed by the user. This increases the attack surface of the Android operating system. The non-erasable or non-configurable interfaces are often not desired in institutions.

Overall, the deep integration of apps and third-party interfaces increases the risk that the device will be infected with malware or that an attacker could gain unauthorized access. The protection of data on the device decreases.

3 requirements
---------------

The following are specific requirements for the Android section. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.3.2.4.A1 Selection of devices with Android

When selecting a terminal with Android, it MUST be ensured that the manufacturer regularly provides security updates for this device. The device MUST be delivered with or updated to a current version of Android.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of Android. They SHOULD be implemented in principle.

#### SYS.3.2.4.A2 Disable the developer options

In all Android-based devices, the developer options SHOULD be disabled.

#### SYS.3.2.4.A3 Using Multi-User and Guest Mode

It should be regulated whether the multi-user and guest mode may or may be used. A user on the Android-based device SHOULD match a natural person.

#### SYS.3.2.4.A4 Control and configuration of cloud print

Cloud Print SHOULD only be allowed if it is ensured that the user can only select approved printers.

#### SYS.3.2.4.A5 Advanced security settings

Only the shared security apps SHOULD register as device administrators or trust agents. The security management SHOULD check this regularly.

Furthermore, the "Access to usage data and access to notifications" settings should only allow allowed apps to access this sensitive data.

### 3.3 Requirements for increased protection requirements
Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.3.2.4.A6 Using a Malware Protection (CIA) Product

It SHOULD be installed on Android-based devices, a software to protect against malware. The software SHOULD always be up to date. It SHOULD use a software that has been rated as very good in independent tests.

#### SYS.3.2.4.A7 Additional Firewall (CI)

On Android-based devices, a firewall SHOULD be installed and enabled.

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the "Android" section can be found in the following publications, among others:

* #### [AN2] Two-factor authentication

  

 Google, (last accessed on 27.09.2017)
 <Https://www.google.com/landing/2step/>

 
* #### [ANH] Android Help

  

 Google, (last accessed on 27.09.2017)
 <Https://support.google.com/android/?hl=de>

 
* #### [ANL] Overview Android-based devices

  

 Google, (last accessed on 27.09.2017)
 <Https://www.android.com>

 
* #### [ANS] networks and security

  

 Google, (last accessed on 27.09.2017)
 <Https://www.android.com/security/overview>

 
* #### [ANU] App Updates

  

 Google, (last accessed on 27.09.2017)
 <Https://support.google.com/googleplay/answer/113412?hl=de>

 
* #### [GAGB] Google Terms

  

 Google, (last accessed on 27.09.2017)
 <Https://www.google.com/policies/terms/>

 
* #### [GPP] Goggle Piracy Policy

  

 Google, (last accessed on 27.09.2017)
 <Https://www.google.com/policies/privacy/>

 
* #### [GSUITE] G Suite for Business and Education

  

 Google, (last accessed on 27.09.2017)
 <Https://gsuite.google.com>

 
* #### [TR02102] Cryptographic method recommendations and key lengths

  

 BSI, (last accessed on 27.09.2017)
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Android" component.

* G 0.14 Spying out information (spying)
* G 0.16 Theft of devices, data carriers or documents
* G 0.21 Manipulation of hardware or software
* G 0.28 Software vulnerabilities or errors
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.38 Abuse of personal data
* G 0.39 Malware
* G 0.41 Sabotage
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.14 Spying out information (spying)
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.16 Theft of devices, data carriers or documents
  * SYS.3.2.4.A4 Control and configuration of cloud print
* G 0.21 Manipulation of hardware or software
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.28 Software vulnerabilities or errors
  * SYS.3.2.4.A1 Selection of devices with Android
* G 0.30 Unauthorized use or administration of devices and systems
  * SYS.3.2.4.A3 Using Multi-User and Guest Mode
  * SYS.3.2.4.A5 Advanced security settings
* G 0.32 Abuse of permissions
  * SYS.3.2.4.A2 Disable the developer options
* G 0.38 Abuse of personal data
* G 0.39 Malware
  * SYS.3.2.4.A1 Selection of devices with Android
  * SYS.3.2.4.A6 Using a Malware Protection (CIA) Product
  * SYS.3.2.4.A7 Additional Firewall (CI)
* G 0.41 Sabotage
  * SYS.3.2.4.A2 Disable the developer options
* G 0.46 Loss of integrity of sensitive information
  * SYS.3.2.4.A2 Disable the developer options
  * SYS.3.2.4.A4 Control and configuration of cloud print
