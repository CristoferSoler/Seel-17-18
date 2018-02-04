Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

With Windows 10, Microsoft has adapted its Windows client operating system to a new corporate strategy. In particular, the design philosophy of the operating system has also changed away from the previous principle of the "local operating system" towards a service ("Windows as a Service") which, in addition to the previous operating system functionalities, also contains applications that go beyond that, in particular cloud-based, and therefore one tight connection to the server infrastructure of the manufacturer is dependent. The deep-rooted and sometimes uncontrollable data exchange between client and manufacturer infrastructure as well as the increasing outsourcing of security-critical core components of a Windows infrastructure to the cloud, such as: As authentication, are important and before a use necessarily to be evaluated new aspects compared to the previous versions of Windows.

### 1.2 Objective

The goal of this module is to protect information that will be processed by and on Windows 10 clients.

### 1.3 Delimitation

Based on the SYS.2.1 General Client block, this block contains specific requirements that must be observed and fulfilled for the secure operation of clients under the Windows 10 operating system in addition to the requirements from the SYS.2.1 General Client block. The included requirements must always be considered in conjunction with the requirements of the "General Client". Protection against advanced and persistent threats must be realized by meeting additional requirements of the different layers of modernized IT-Grundschutz.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to the Windows 10-based clients under consideration:

### 2 1 Malware on Windows 10

Due to the high prevalence of Windows operating systems and the backwards compatibility with older versions, which is often present between the system generations, the threat from malicious programs and unauthorized intrusion into the IT system is comparatively high. Malicious programs can have a variety of functions and provide an attacker with extensive control options. Among other things, malicious programs can specifically search passwords, remotely control systems, deactivate protection software and spy on data. In particular, loss or falsification of information or applications is of paramount importance. But also a loss of image and financial damage, which can thus result from malicious programs, is of great importance. Windows is a primary target for malware attacks due to its widespread use, posing a major threat from numerous attackers and attack types.

### 2 2 Software Vulnerabilities in Windows 10

Windows 10, including its many included applications, is a very complex software product. If software errors are not detected in time, the crashes or errors that occur during the application can lead to far-reaching consequences (such as incorrect calculation results, incorrect management decisions, and delays in the course of business processes). Software vulnerabilities or errors can lead to serious security vulnerabilities in individual applications, in the entire IT system, or even in all connected IT systems. Vulnerabilities in Windows can sometimes be exploited by attackers to inject malicious software, unauthorized read data or tampering.

### 2 3 Integrated cloud functionalities
Windows 10 has many features that store and sync data using Microsoft's services ("cloud services"). As a result, there is a risk of unconsciously (or at least carelessly) using it for possibly sensitive or personal data. At the same time, violations of data protection laws may result if data is stored with third parties, usually abroad. If a user with an already activated Microsoft account logs on to a new device, the Microsoft cloud services he uses are automatically set up. Thus, data of the institution can be unintentionally synchronized to the employees' private devices. As another example, Windows 10 provides the ability to back up the Bitlocker recovery key directly from the Microsoft account in the cloud, leaving critical cryptographic secrets in the hands of third parties.

### 2 4 Impairment of software functions due to compatibility issues

Software that has been successfully run on previous versions of an operating system does not necessarily have to work with the current version of Windows 10. Possible causes are new security features or operating system features, as well as the omission of functionalities or services. As a result, the software can not be used or only with restrictions. Examples of enabled security features that can cause compatibility issues with new versions of Windows include User Account Control (UAC), or 64-bit versions of the Kernel Patch Guard operating system, and the need for signed drivers that may not be available for older devices To be available.

### 2 5 Incorrect administration or use of Windows 10

Windows 10 is a complex operating system whose security is largely determined by its configuration. This results in particular by misconfiguration of individual or multiple components impairments of security for the client itself and for the infrastructure used. Basically, any interface to an IT system not only includes the ability to legitimately use certain services of the IT system, but also the risk of unauthorized access to the IT system. If user IDs and associated passwords can be spied out, for example by misconfiguration of the Windows own authentication mechanisms, then unauthorized use of the applications or IT systems protected by them is possible.

Improper or improper use of devices, systems, and applications can also affect security in Windows, especially if existing security measures are disregarded or bypassed or deliberately shut down. Too generously granted rights, easy-to-guess passwords, insufficiently protected data carriers with backup copies or jobs that are not locked in case of temporary absence can lead to security incidents. Another consequence of improper operation of Windows systems or applications may be the accidental deletion or modification of data. It is also possible for confidential information to reach the public, for example if access rights are set incorrectly.
