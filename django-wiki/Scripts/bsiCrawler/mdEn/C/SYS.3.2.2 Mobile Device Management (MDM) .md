Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Smartphones, tablets and phablets are an indispensable part of their work for many employees. However, IT departments need to deploy more and more such devices in many different designs, while providing adequate security. In addition, mobile devices are exposed to special risks and the administration differs fundamentally from other IT systems.

That is why Mobile Device Management (MDM) is indispensable for the controlled and secure operation of these devices, especially in institutions with a larger number of smartphones, tablets and phablets. With such a software, the terminals can be managed centrally, it can enforce security rules and emergency actions can be triggered. An MDM thus ensures the same or at least comparable safety standard on all devices.

### 1.2 Objective

The module shows how an MDM can be used to securely use mobile devices by institutions and how the MDM itself can be operated safely.

### 1.3 Delimitation

Mobile devices in the sense of this component are smartphones, tablets and phablets, on which mobile operating systems such as Android, iOS, Windows Phone and BlackBerry OS are installed. The security requirements of notebooks and tablets with desktop operating systems are described in other modules. Also, this module does not focus on how the smartphones, tablets and phablets of different manufacturers are specifically secured, as this is described in detail in the blocks for the respective operating systems, eg. Eg SYS.3.2.3 * iOS (for Enterprise) * or SYS.3.2.4 * Android. *

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in Mobile Device Management (MDM).

### 2 1 Loss of the terminal

Because mobile devices are often small and constantly being transported, they are easily forgotten, lost or stolen. In addition to the economic damage, the loss of confidentiality and integrity of the data contained weighs particularly hard. There is also the danger that attackers can access the institution's internal IT resources via a stolen mobile device.

### 2 2 Danger from malicious software

Like any device connected to the Internet, mobile devices are also threatened by malicious software. The risk of infection is even lower compared to PC operating systems, but cybercriminals are increasingly focusing on these devices. For example, when a device becomes infected, attackers can read, modify, or delete data, or gain access to the institution's internal IT resources.

### 2 3 Dangers from private use of mobile devices

When employees are given their own smartphones, tablets and phablets, there is always a risk that they will use the devices illegally privately. This creates several problems for the information security of the institution. For example, users could independently install apps that contain malicious software or visit web pages that could infect the device with malware. Similarly, user-installed apps can be a risk to the institution's information stored on the device, such as: For example, you can directly access contacts, calendars, e-mails, or documents. This allows data to flow away or conversely enter the institution in an uncontrolled manner. Well-known examples are social media and instant messaging apps.

### 2 4 Insufficient synchronization with the MDM
In order for the MDM to enforce the rules defined by the responsible parties on the mobile devices, the devices must be synchronized with the MDM on a regular basis. For example, if a device is not connected to the MDM for an extended period of time, new or updated rules can not be applied. Also, if there is no connection to a lost device, the data can not be deleted remotely.

### 2 5 Incorrect administration of the MDM

MDM solutions are complex applications with typically several hundred different rules. Not all rules can be combined and vice versa many rules depend on each other. Administration errors may expose endpoints to various threats that directly or indirectly affect the confidentiality, availability, or integrity of data and applications.

### 2 6 Inappropriate rights management in the MDM

The rights management of the MDM decides who should make which settings and who may access which data. If an employee is assigned an incorrect role, there is a risk that he or she will be granted too high rights. For example, he could view data without authorization or change settings on the device. It would also be possible for him to install and use apps that are not allowed in the institution, such as using cloud storage services. As a result, sensitive data can flow out of the institution, or the legal data protection regulations are violated.

### 2 7 No or weak encryption of communication between MDM and terminal

If the data connection between the mobile device and the MDM server is not encrypted at all or encrypted with outdated algorithms, or if insufficient key lengths are used, the confidentiality and integrity of all transmitted data is compromised. For example, an attacker could then spend his IT system as an MDM server, gaining valuable information or changing settings on all of the institution's mobile devices.

### 2 8 Unauthorized creation of motion profiles by the MDM

With most MDM products, it is possible to determine where a device is currently located and data or apps can be enabled or disabled depending on location (so-called geofencing). This results in minute movement profiles of the devices and thus also the user. If these data are collected without informing the user appropriately, the persons responsible may violate data protection regulations. There is also the danger that attackers will access this data. Similarly, Geofencing can be misused to control employees inadmissible.

### 2 9 Dangers of Bring Your Own Device (BYOD)

If private devices are used for business purposes, there are various potential threats. For example, there may be legal issues regarding software licenses. In an emergency, when service data needs to be erased by the MDM on the device, it may also affect the user's private data. In addition, the IT managers can no longer check every single employee device to see if it can also be used in official business. There is a risk that inappropriate devices will be used, violating internal privacy and security requirements. In addition, users are often responsible for maintaining and repairing their personal devices. In such a repair, for example, corporate data could be viewed without authorization. The same risk exists when there is no regulation of what should happen to the data on the device when the employee leaves the institution.
