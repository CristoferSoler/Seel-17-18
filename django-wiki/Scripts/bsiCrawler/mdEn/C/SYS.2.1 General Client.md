[toc]
 
1 description
--------------

### 1.1 Introduction

A "general client" is an IT system with any operating system that allows the separation of users. You should be able to set up at least one administrator and one user environment. Typically, such an IT system is networked and used as a client in a client-server network. The IT system can be operated on any platform. This can be, for example, a PC with or without a hard disk, a mobile or stationary device, but also a Linux workstation or an Apple Mac. The IT system typically has removable media drives, additional interfaces for data exchange, and other peripherals.

### 1.2 Objective

The goal of this module is to protect information that is created, read, processed, stored or sent to clients, regardless of the operating system they run on.

### 1.3 Delimitation

Typically, client systems operate under an operating system that requires its own security measures. Common client operating systems have their own blocks that supplement this block. The module "general client" forms the basis for the concrete building blocks on which they are based. If a concrete module exists for a considered IT system, it must be used in addition to the module General Client. If no specific module exists for deployed client systems, the requirements of this module must be suitably adapted. Safety recommendations for mobile devices that can not be freely configured, such as smartphones or tablets, can generally be found in the SYS.3 Mobile Devices layer.

If the client has other interfaces for data exchange, such. As USB, Bluetooth, LAN or WLAN, they must be secured according to the security requirements of the institution, as described in the corresponding modules. For this, information can be found in SYS.3.4 Mobile Disk, NET.2.3 Near Field Radio and NET.2.2 WLAN Usage.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the General Client area:

### 2 1 Malware

Malicious programs are designed to perform unwanted and malicious functions on computers. They usually become secretly active without the users knowing or agreeing to it. Depending on their characteristics, they offer an attacker comprehensive communication and control options with many functions. Among other things, they could specifically search passwords, remotely control IT systems, deactivate protection software or spy on data.

Clients are particularly susceptible to malware: they are served directly by users and are often the gateway for malicious software. If users visit infected web pages, open emails with compromised content from private email accounts, or copy malicious software to the client through local disks, the malicious software spreads through clients into the institution's network. Central protection mechanisms, such as e.g. Virus protection on the file or email server can be bypassed so often.

### 2 2 Unstructured local data management

Despite regular contradictory recommendations, many users also store important data exclusively locally. For example, data is often stored in local user directories rather than on a central file server. E-mails are often only archived locally. This procedure can lead to the following problems:

* Data loss on hardware defects and
* no access to relevant data in case of substitution.
But even if basic requirements for central storage are adhered to, local copies of the centrally stored data are often created in addition. This can lead to the following problems:

* Waste of local storage space,
* premature or non-deletion of data and
* inconsistent version states
### 2 3 Data loss

Clients typically store a lot of data across their entire organization, the loss of which can have a significant impact on business processes and therefore on the entire institution. If business-relevant data is destroyed or falsified, business processes and specialized tasks can be delayed or even prevented from running. Overall, the loss of stored data, in addition to a loss of work and the cost of replacement, can also lead to long-term consequences, such as loss of confidence among customers and partners, as well as a negative public perception. From the direct and indirect damage caused by data loss, institutions can in extreme cases be threatened in their existence.

### 2 4 Hardware defects due to incorrect operation

Unlike central IT systems such as servers, client users work directly at the end device. Physical access can intentionally or unintentionally damage the client. For example, they can step on floor-standing IT systems, upset monitors, tripping over cables, or pouring drinks into keyboards. Often it is not sufficient to replace hardware only in case of a defect. For example, in the event of a hard disk failure, stored data can not be recovered. In addition, the IT system can not be used until the repair is complete. In case of failure of a mobile device on the road, the work can be continued only after the return.

### 2 5 Software vulnerabilities or errors

For any type of software, the more complex it is, the more frequently programming or design errors can occur. Software vulnerabilities are program errors that users are (still) not aware of and that pose a security risk to the system. Almost daily, new vulnerabilities are found in both long-term and new software.

Clients typically install a variety of different applications, which increases the amount of vulnerabilities that can affect the system. In addition, a larger number of (mobile) clients are much more difficult to update with patch fixes than, for example, a few servers.

If software errors are not detected or not rectified immediately, this can lead to serious consequences. A software vulnerability in a widely used standard software can quickly lead to global security problems for all types of institutions.

### 2 6 Unauthorized use of IT

The identification and authentication of users should prevent a client from being used unauthorized. But also IT systems, where users have to identify and authenticate themselves via user IDs and passwords, can be used without authorization if an attacker succeeds in spying on or guessing the access data. If no screen lock is activated, the client can be used without authorization even in the case of a short-term absence.

### 2 7 Provision of unneeded operating system components and applications
When installing an operating system, it is usually possible to install optional software. Software is also regularly installed and tested during operation. With each additional application, not only the computing and memory load of a client is steadily increasing, but also the likelihood of finding vulnerabilities in it. Unnecessary software is also often not subject to regular patch management, so that known vulnerabilities are not closed promptly. This allows attackers to exploit known vulnerabilities for a long time.

### 2 8 Listening to rooms using a microphone and a camera

Many clients have a microphone and a camera. These can be used by anyone who has appropriate access rights, in networked systems also by external users. If these rights are not granted with care, unauthorized persons may misuse the microphone or camera in order to listen to rooms over the Internet or record meetings unnoticed.
