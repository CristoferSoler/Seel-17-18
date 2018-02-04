[toc]
 
1 description
--------------

### 1.1 Introduction

* Samba * is a freely available and fully-featured Active Directory Domain Controller (ADDC) that can provide authentication, file and print services, enabling interoperability between the Windows and Unix worlds. * Samba * brings together many different protocols and techniques. These include, for example, the * Server Message Block (SMB) * protocol, also known by the newer name * Common Internet File System * (CIFS). * Samba * servers are servers on which * Samba * is operated. In general, these are the Linux server.

* Samba * has been properly designed and neatly configured, the application interacts with a Windows client or server as if it were a Windows system itself.

### 1.2 Objective

The goal of the module is to show how * Samba * can be used safely in institutions and how the information provided by Samba can be protected.

### 1.3 Delimitation

This module considers * Samba * as an authentication, file and print service. Since * Samba * is generally used on Linux servers and represents services known from the Windows server world, the security aspects of the blocks SYS.1.1 * General Server * and SYS.2.1 * Server under Linux * must be taken into account. Security requirements for printers, file servers or directory services, on the other hand, are not part of this module but are described in the blocks SYS.4.1 * Printers, Copiers and Multifunction Devices *, APP.2.1 * General Directory Service * and APP.3.6 * DNS Server * and APP.2.3 * OpenLDAP *, even if the * Samba * internal DNS and LDAP services are used. Furthermore, due to the * Samba * functions, the components APP.3.3 * Fileserver * and APP.2.2 * Active Directory * have to be considered.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in * Samba *:

### 2 1 Listening to unprotected communications from Samba

When attackers hear unprotected * Samba * communication links, information can be intercepted and abused. When transferring files between Linux servers, Windows servers and clients, protocols are often used without extensive security features, so that both authentication and user data are accessible to third parties and could be misused by unauthorized persons. This can lead to valuable information flowing from the institution.

### 2 2 Incorrect logging in Samba

Improperly designed or missing logging in * Samba * can lead to security issues. Without proper logging, errors or attacks go undetected and preventive measures and early warning system indicators can not be defined.

### 2 3 Incorrect emergency preparedness in Samba

Also deficits in the emergency preparedness can lead to longer downtime of * Samba *. For example, after a successful attack, a necessary reinstallation may be delayed if installation packages are not available. Existing installation packages, in turn, can produce undesirable results if you have not used versioning of the configuration files or if the * Samba * server compilation and installation options are not kept.

### 2 4 Missing adaptation of Samba
To show some capabilities of the * Samba * server and to give administrators a quick start, the configuration file * smb.conf * is created with default settings during the installation of the * Samba * server. With the options preset in this file, the * Samba * server can be started afterwards. If this file is thoughtlessly used without further settings, this can lead to considerable security gaps. However, even if the file is modified, errors may occur that may result in the disclosure of sensitive information or compromise the security, availability and performance of a * Samba * server's services.

### 2 5 Software vulnerabilities or errors in Samba

* Samba * is free software that is created and developed within a community. A consistent quality of the source code can not be guaranteed. This can lead to software vulnerabilities or errors and thus to serious security vulnerabilities in the application or all connected IT systems. Attackers can use such vulnerabilities for various attacks. For example, to infiltrate malicious software and thus possibly gain unauthorized access to sensitive information, such as confidential data or documents and access data. Furthermore, attackers can manipulate IT systems via security vulnerabilities, which can cause them to be inoperable or malfunctioning.

### 2 6 Unauthorized use or administration of Samba

Unauthorized persons may gain access to confidential information, manipulate it or cause malfunctions through the use of applications or systems, so that they * can administer * Samba * without authorization. It is particularly critical when configuration tools such. For example, the * Samba Web Administration Tool * (SWAT) can be used. SWAT was an integral part of * Samba * until version 4, but was given a low priority by * Samba * developers. Therefore, weaker or no security mechanisms were implemented, for example, HTTPS was not supported.

### 2 7 Incorrect administration of Samba

If administrators are not familiar enough with * Samba *'s extensive features, components, options, and configuration settings, it can lead to far-reaching complications. For example, misconfiguration of DNS or of user and rights management can lead to unauthorized access to resources. Furthermore, this can lead to business interruptions or protect information can be disclosed.

### 2 8 Malicious programs around Samba services

If * Samba * is used as a file server on Linux systems, then the server itself is not directly susceptible to Windows malware. These can however be contained in infected files that are stored on them. Through the * Samba * system these infected files are then provided to all connected Windows clients and thus actively distributed.

### 2 9 Data loss at Samba

Data loss has a significant impact on IT use. If business-relevant information is destroyed or falsified, business processes and specialist tasks can be delayed or even stopped. For example, * Samba * notes that the file system properties of Windows and Unix are significantly different. Therefore, it is not always guaranteed that access rights will be maintained under Windows. It can also cause information on * Alternate Data Streams * (ADS) and DOS attributes to be lost.

### 2 10 Integrity loss of sensitive information at Samba
If information is no longer integer, it can lead to many problems. In the simplest case, information can then no longer be read, so it can no longer be further processed. * Samba * itself stores important operating data in * Trivial Database * (TDB) format databases. If these databases are not adequately and consistently handled by the operating system, they can cause problems when * Samba * services are used.
