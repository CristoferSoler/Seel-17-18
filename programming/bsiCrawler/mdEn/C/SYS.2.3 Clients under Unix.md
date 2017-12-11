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

The building block includes only the Unix-like operating system that is typically installed in a base installation of a Linux desktop distribution. The module includes, in particular, software that does not rely on it, such as e-mail clients or office software. Requirements for this can be found in the IT-Grundschutz Compendium layer APP.1 Client Applications. If the client has interfaces for data exchange, such. As CD / DVD, USB, Bluetooth or WLAN, the security requirements of the block SYS.3.4 Mobile data carrier must be metIt is assumed in this client module that in addition to the administrator, only an unchanged person with an interactive user account is permanently active. Clients that are used by several people, one after the other or at the same time, require additional measures, which are not dealt with in this module.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to clients running Unix:

### 2 1 Malware

Malicious programs are designed to perform unwanted and usually malicious functions. Malicious programs are usually secretly active without the knowledge and consent of the user. Malicious programs today offer an attacker extensive communication and control options and have a variety of functions. Among other things, the programs can specifically search passwords, remotely control systems, disable protection functions and spy on data. In particular, users who rely on the inherently higher security of unix-like systems are often more careless when dealing with unknown files.

### 2 2 Software from third party sources

With unix-like IT systems, it is not uncommon to download and compile software yourself, rather than installing finished software packages. When finished software packages are used, they are often not only installed from the existing package sources of the Unix derivative, but are sourced from third-party sources without further testing. Each of these alternative ways of installing software entails additional risks in installing faulty or incompatible software and malicious software.

### 2 3 Software vulnerabilities or errors

On unix-like IT systems, a variety of applications are usually offered for installation. Because each of the installable applications may have software vulnerabilities and faults, the potential attack surface is increased if the installation did not care to install only the required software.

### 2 4 Exploitation of the script environment

Often, scripting languages ​​are used in unix-like operating systems. Scripts are a list of individual commands that are stored in a text file and called, for example, in the command line. The rich functionality of the scripting environments allows attackers to leverage scripts for their own purposes. In addition, activated scripting languages ​​are very difficult to contain.

### 2 5 Dynamic loading of shared libraries

The command line option LD \ _PRELOAD loads the given library before any other libraries needed in an application, and its functions are used by the application. An attacker could manipulate the operating system to carry out malicious use of certain applications.

### 2 6 Incorrect configuration

Even in a standard installation, unix-like operating systems install numerous applications that need to be configured separately. Post-installed applications must also be configured separately so that countless configuration files can be found on unix-like operating systems.

Because these applications are configured independently of each other, the configuration options may conflict with each other without being apparent from the individual settings. For example, a remote administration service may be listening on a port that is blocked by packet filtering rules, or Samba unintentionally releases its own home directory on the network. In this way, the applications can unintentionally provide additional functionality, or fail to provide critical functionality, making it difficult to complete client tasks.

3 requirements
---------------The following are specific requirements for the Client section on Unix. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.2.3.A1 Authentication of administrators and users [user]

To use the client, users MUST authenticate themselves to the IT system. Administrators MAY NOT log in as root during normal operation. For system administration tasks, "sudo" or a suitable alternative with appropriate logging SHOULD be used. It SHOULD prevent multiple users from logging into one device at the same time.

#### SYS.2.3.A2 Selection of a suitable distribution

A suitable Unix derivative or Linux distribution MUST be selected based on security requirements and purpose. All preinstalled application programs that are not needed MUST be uninstallable. It MUST be offered for the planned operating time of the operating system support. All required application programs SHOULD be directly available without having to obtain them from third party sources.

You should only select and install application programs for which support is offered. Operating system and application programs without regular security updates SHOULD NOT be used. It SHOULD be waived on distributions with a rolling-release model. Distributions where the operating system itself is compiled SHOULD NOT be used in production environments.

#### SYS.2.3.A3 Cloud and Online Content [User]

Only absolutely necessary cloud and online services of the operating system may be used. The necessary cloud and online services SHOULD be documented. The operating system settings MUST be checked for compliance with organizational privacy and security guidelines and restrictedly configured or disabled.

#### SYS.2.3.A4 Importing Updates and Patches

Those responsible MUST inform themselves about known vulnerabilities. Updates and patches MUST be loaded as soon as possible. First, it should be checked on a test system, whether the security updates are compatible and do not cause any errors. Unless patches for known vulnerabilities are available, other appropriate measures MUST be taken to protect the client. The client SHOULD reboot soon after the kernel has been updated. Alternatively, live patching of the kernel MUST be enabled.

#### SYS.2.3.A5 Secure installation of software packages

Only required applications may be installed. Unused applications MUST be uninstalled.

The integrity and authenticity of the software packages to be installed MUST always be checked. The software packages MUST be unpacked, configured and translated under an unprivileged user account. Only the last step, the actual installation of the translated program, can be done with higher privileges. The software to be installed MAY NOT be installed uncontrolled in the root file system of the server.If the software is translated from the source code then the selected parameters SHOULD be suitably documented. Based on this documentation, the source code SHOULD be able to be compiled comprehensibly and reproducibly at any time. All further installation steps SHOULD also be documented so that the configuration can be quickly reproduced in an emergency.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state of the art for clients under Unix. They SHOULD be implemented in principle.

#### SYS.2.3.A6 Automatic integration of removable drives [user]

Removable drives SHOULD NOT be automatically included. The inclusion of removable drives SHOULD be configured so that all files are marked as not executable (mount option "noexec").

#### SYS.2.3.A7 Restrictive rights assignment to files and directories

Users' access to files and directories SHOULD always be restricted to the minimum required. It should in any case be ensured that services and applications may only create, modify or delete their assigned files. On directories where all users have write permissions (eg / tmp) the sticky bit SHOULD be set.

#### SYS.2.3.A8 Use of application restriction techniques

To restrict the access rights of applications to files, devices and networks SHOULD App-Armor or SELinux be used. It SHOULD use the solution best supported by the respective Unix derivative or Linux distribution. Instead of blacklisting, the necessary applications SHOULD be regulated by whitelisting. Rights Restrictions SHOULD be used in Enforcement Mode or with appropriate alternatives.

#### SYS.2.3.A9 passwords on the command line [user]

Passwords SHOULD NOT be passed as parameters to programs.

#### SYS.2.3.A10 Hedging the boot process

The client SHOULD be secured by assigning a boot password in the firmware. In addition, a boot order SHOULD be set to boot from the built-in boot disk first. The bootloader SHOULD be password protected so that only the unchanged default entry without password can be used.

When booting, the integrity of the (pre) boot loader SHOULD be checked up to the kernel. The keys used for this purpose SHOULD be checked during initial setup. It SHOULD be checked if Secure Boot could be used as part of the UEFI specification or equivalent solutions.

#### SYS.2.3.A11 Prevention of hard disk overload

Quotas SHOULD be set up for users or services that leave enough free space for the operating system. In general, different partitions for the operating system and data SHOULD be used. Alternatively, mechanisms of the used file system SHOULD also be used, which only grant the user root write access from a suitable fill level.

#### SYS.2.3.A12 Use of Appliances as Clients

It SHOULD ensure that appliances meet a similar level of security to clients on standard IT systems. It SHOULD document how appropriate security requirements are met with a deployed appliance. If the requirements can not be met beyond doubt, a declaration of conformity should be requested from the manufacturer.

### 3.3 Requirements for increased protection requirementsListed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.2.3.A13 Protection against unauthorized applications (CIA)

A two-factor authentication SHOULD be used.

#### SYS.2.3.A14 Protection against the use of unauthorized peripherals (CIA)

Peripherals SHOULD only be usable if they are run on a centrally managed whitelist. Kernel modules for peripherals SHOULD ONLY be charged and activated when the device is whitelisted.

#### SYS.2.3.A15 Additional protection against the execution of unwanted files (CI)

Partitions and directories where users have write permissions SHOULD be mounted so that no files can be executed (/ noexec).

#### SYS.2.3.A16 Additional safeguarding of boot process (CIA)

Bootloader and Kernel SHOULD be signed by self-controlled key material and unneeded key material should be removed.

#### SYS.2.3.A17 Additional prevention of spread when exploiting vulnerabilities (CI)

The use of system calls SHOULD be limited to the absolutely necessary system calls, in particular for exposed services and applications (eg by "seccomp"). The existing default profiles or rules of "SELinux", "AppArmor" as well as alternative extensions SHOULD be checked manually and, if necessary, adapted to your own security policy. If necessary, new rules or profiles SHOULD be created.

#### SYS.2.3.A18 Additional Kernel Protection (CI)

Special hardened kernels should use appropriate protection mechanisms such as storage protection, file system protection, and role-based access control to prevent the exploitation of vulnerabilities and propagation in the operating system (eg, "grsecurtiy", "PaX").

#### SYS.2.3.A19 Hard Disk or File Encryption (CI)

Hard drives or the files stored on them SHOULD be encrypted. The associated keys SHOULD NOT be stored on the IT system. It SHOULD use "AEAD" for hard disk and file encryption. Alternatively, "dm-crypt" should be used in combination with "dm-verity".

#### SYS.2.3.A20 Shutdown Critical SysRq Functions (CIA)

SHOULD critical SysRq functions be disabled.

4 Further Information
------------------------------

### 4.1 Literature

Further information about threats and security measures in the section "Clients under Unix" can be found in the following publications:

* #### [ISiClient] Securing a PC client (ISi client),

  

 (last accessed on 27.09.2017)
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/Isi-Reihe/Isi-Client/client\_node.html](https://www.bsi.bund.de/DE/Themen/ standard criteria / Isi-series / Isi client / client_node.html)

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008
 <Https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Clients under Unix" building block.

* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.28 Software vulnerabilities or errors
* G 0.30 Unauthorized use or administration of devices and systems* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.39 Malware
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.