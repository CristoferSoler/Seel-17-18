[toc]
 
1 description
--------------

### 1.1 Introduction

In addition to Windows, more and more client operating systems Linux or less often Unix are installed. Examples of classic Unix systems are the BSD series (FreeBSD, OpenBSD and NetBSD), Solaris and AIX. Linux, on the other hand, is not a classic Unix (the kernel is not based on the original source code that made the various Unix derivatives), but a functional Unix system. Because the configuration and operation of Linux and Unix clients are similar, this module looks at all Unix family operating systems.

Linux is free software and is developed by the open source community. In addition, there are providers who combine the Linux kernel and the various software components to a distribution and maintain, and offer other services. Often derivatives are used for the distributions Ubuntu, Debian, Red Hat Enterprise Linux SUSE Linux Enterprise. In addition, there are custom Linux distributions for specific applications and devices, such as Qubes OS, which seeks to achieve a high level of security through virtualization, IGEL Linux as a thin client, LibreElec for use with a Home Theater PC (HTPC) or Kali Linux , a distribution specializing in security, computer forensics and penetration testing. In addition, clients can also start live distributions without changing the existing operating system.

The market share of the operating system Linux on clients has increased in recent years, in special operating environments continue to use "classic" Unix systems in various derivatives. The amount of pre-selected software packages of a standard installation of common Linux distributions, or the Unix derivatives, increases the attack surface, at the same time offer unix-like operating systems but also extensive protection mechanisms. Typically, such an IT system is networked and operates as a client in a client-server network. Since clients are often operated for security reasons under Unix or Linux and as with all clients can not be trusted to correct user behavior, the protection of unix-like clients is of particular importance.

### 1.2 Objective

The goal of this module is to protect information that is created, edited, stored or sent on Unix clients. The requirements of the block primarily address Linux clients, but can generally be adapted for Unix clients. The present module does not differentiate between Unix and Linux. Unix and Linux clients are grouped under the term "Unix".

### 1.3 Delimitation

This module contains basic requirements for operating unix-like clients on standard IT systems. It concretizes and complements the aspects that are dealt with in the building block SYS.2.1 General Client to specifics of Unix systems. Even if Apple OS X is a unix-like operating system, this operating system is not covered in this module, recommendations can be found in the module SYS.2.4 client under Apple OS X.

If the client is not to be managed by itself, but is managed by a third party, the requirements of the module OPS.3.1 Outsourcing usage must also be taken into account.

The building block includes only the Unix-like operating system that is typically installed in a base installation of a Linux desktop distribution. The module includes, in particular, software that does not rely on it, such as e-mail clients or office software. Requirements for this can be found in the IT-Grundschutz Compendium layer APP.1 Client Applications. If the client has interfaces for data exchange, such. As CD / DVD, USB, Bluetooth or WLAN, the security requirements of the block SYS.3.4 Mobile data carrier must be met
It is assumed in this client module that in addition to the administrator, only an unchanged person with an interactive user account is permanently active. Clients that are used by several people, one after the other or at the same time, require additional measures, which are not dealt with in this module.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to clients running Unix:

### 2 1 Malware

Malicious programs are designed to perform unwanted and usually malicious functions. Malicious programs are usually secretly, without the knowledge and consent of the user active. Malicious programs nowadays provide an attacker with extensive communication and control options and have a large number of functions. Among other things, the programs can specifically search passwords, remotely control systems, disable protection functions and spy on data. In particular, users who rely on the inherently higher security of unix-like systems are often more careless when dealing with unknown files.

### 2 2 Software from third party sources

With unix-like IT systems, it is not uncommon to download and compile software yourself, rather than install finished software packages. When ready-made software packages are used, they are often not only installed from the existing package sources of the Unix derivative, but are sourced from third-party sources without further testing. Each of these alternative ways of installing software entails additional risks in installing faulty or incompatible software and malicious software.

### 2 3 Software vulnerabilities or errors

On unix-like IT systems, a variety of applications are usually offered for installation. Because each of the installable applications may have software vulnerabilities and faults, the potential attack surface is increased if the installation did not care to install only the required software.

### 2 4 Exploitation of the script environment

Often, scripting languages ​​are used in unix-like operating systems. Scripts are a list of individual commands that are stored in a text file and called, for example, in the command line. The rich functionality of the scripting environments allows attackers to leverage scripts for their own purposes. In addition, activated scripting languages ​​are very difficult to contain.

### 2 5 Dynamic loading of shared libraries

The command line option LD \ _PRELOAD loads the given library before any other libraries needed in an application, and its functions are used by the application. An attacker could manipulate the operating system to carry out malicious use of certain applications.

### 2 6 Incorrect configuration

Even in a standard installation, unix-like operating systems install numerous applications that need to be configured separately. Post-installed applications must also be configured separately so that countless configuration files can be found on unix-like operating systems.

Because these applications are configured independently of each other, the configuration options may conflict with each other without being apparent from the individual settings. For example, a remote administration service may be listening on a port that is blocked by packet filtering rules, or Samba unintentionally releases its own home directory on the network. In this way, the applications can unintentionally provide additional functionality, or fail to provide critical functionality, making it difficult to complete client tasks.
