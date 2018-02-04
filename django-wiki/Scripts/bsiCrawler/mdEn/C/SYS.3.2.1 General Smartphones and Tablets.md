Table of content

[toc]
 
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

New versions of mobile operating systems and updates are regularly released. The updates and versions of devices that have vendor-specific extensions of the operating system must first be integrated by the manufacturers in their version and then distributed. These updates are typically provided for the latest generation of devices and for a number of older device generations. However, not all previous operating system versions are supplied with updates and security updates to the same extent; in some cases, operating systems are not further developed for economic reasons. Subsequently known vulnerabilities in the operating system of an already discontinued device generation are then no longer supplied with updates and no longer closed.

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

If private devices are used for business purposes, legal problems may arise, for example with regard to software licenses. Even if all data needs to be erased by the MDM on the device in case of emergency, the user may not agree.

Often IT managers can no longer check every single device brought by the employee to see if it can also be used in the workplace. As a result, inappropriate devices can be used, violating internal privacy and security requirements. In addition, users are often responsible for maintaining and repairing their equipment. In such a repair, for example, corporate data could be viewed without authorization. If it is not regulated what should happen to the data on the device, if the employee leaves the company, they could be abused.
