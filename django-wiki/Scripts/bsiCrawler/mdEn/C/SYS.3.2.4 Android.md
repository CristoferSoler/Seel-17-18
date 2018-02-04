Table of content

[toc]
 
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

Overall, the deep integration of apps and third-party interfaces increases the risk that the device will become infected with malicious software or that an attacker may gain unauthorized access. The protection of data on the device decreases.
