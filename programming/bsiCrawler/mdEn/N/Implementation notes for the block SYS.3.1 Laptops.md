1 description
--------------

### 1.1 Introduction

A laptop is a mobile PC. It has a compact design, integrates peripherals such as the keyboard and screen and can be operated over batteries at times independent of external power supply. It has a hard drive and usually also other storage devices, such as DVD or Blu-ray drives, as well as interfaces for communication via various media, such as LAN, USB, Firewire, WLAN. Laptops can be operated with all common operating systems like Windows, Apple macOS or Linux.

Often used as a mobile device, laptops often are not directly connected to the institution's LAN, but dial in via the Virtual Private Network (VPN) over the Internet or other data networks to access the resources of the LAN. Also, the infrastructure of a classic office environment, such as controllable environmental influences, a stable power supply or access protected areas, can not be expected for the mobile use of laptops.

The laptop is presumed to be used by only one user within a given period of time. A subsequent user change is taken into account.

### 1.2 Life cycle

** planning and conception **

In order to use laptops safely and effectively in institutions, a concept should be created based on the security requirements for the existing IT systems and the requirements of the planned deployment scenarios (see SYS.3.1.M1 * Regulations for the use of laptops * ). Based on this, the laptop usage has to be regulated and security guidelines have to be developed (see SYS.3.1.M6 * Laptops security guidelines *).

** procurement **

For the procurement of laptops, the requirements of the respective products resulting from the concept must be formulated and appropriate products selected on this basis (see SYS.3.1.M15 * Suitable selection of laptops *).

**Implementation**

It is necessary to carefully select and install the operating system and software components. The protective measures to be implemented here depend on the operating system used and are therefore described in the specific blocks, for example * SYS.2.2.3 Client under Windows 10 * or SYS 2.3 * Clients under Unix *. Depending on the security requirements, the software components involved must be configured differently. The measures to be taken here are also dependent on the operating system used.

**Business**

One of the most important security measures when running today's laptops is to install an antivirus program and permanently update it (see SYS.3.1.M4 * Using Anti-Virus Programs *). As laptops have a relatively high risk of theft, the data on the laptop should be encrypted (see SYS.3.1.M13 * Encryption of laptops *) and anti-theft devices used (see SYS.3.1.M18 * Using theft-proofing *).

If laptops are connected directly to the Internet during mobile use, it is essential to protect them against attacks from the network by means of a restrictively configured personal firewall (see SYS.3.1.M3 * Using personal firewalls for clients *). It is also necessary to secure the communication to other networks or to other devices (see SYS.3.1.M9 * Secure remote access on the road) * as well as to the internal network (see SYS.3.1.M8 * Secure connection of laptops via data networks *).

Often it is necessary to synchronize the databases between server and laptop. It must be ensured that it is possible to determine at any time whether the most up-to-date version of the processed data is on the laptop or the server (see SYS.3.1.M10 * Matching the Datasets of Laptops *).
In order to keep track of the laptops currently connected to the local area network and to be able to track the configuration of all laptops at any time, these devices should be centrally managed (see SYS.3.1.M16 * Centralized Administration of Laptops *). Depending on the structural safety in a building or office space, it may also be useful or even necessary to use anti-theft fuses (see SYS.3.1.M18 * Using Anti-theft Fuses *). Also laptops are to be kept suitable on the way (see SYS.3.1.M14 * Suitable storage of laptops *).

** Emergency Preparedness **

The procedure and the required extent of data backup depend on the deployment scenario of the laptop (see SYS.3.1.M5 * Data backup *).

** ** segregation

If a laptop is discarded, make sure that there is no longer any information worth protecting on the hard disk (see SYS.3.1.M7 * Controlled transfer and return of a laptop *).

2 measures
-----------

The following are specific implementation instructions in the Laptops section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### SYS.3.1.M1 regulations for the mobile use of laptops

Laptops that are used exclusively within an in-house property are often already adequately protected against misuse and theft by infrastructural security measures. Often, however, laptops should also be used outside the institution, eg. B. on business trips or telework. In order to be able to adequately protect the devices even in these cases, the transport of data carriers and IT components must be clearly regulated.

It must be determined

* which IT components or data media may be taken outside the home,
* who is allowed to take IT components or data carriers,
* which basic security measures must be observed (eg virus protection, encryption of sensitive data, storage).
The type and extent of security measures to be applied to laptops depends, on the one hand, on the protection requirements of the IT applications and data stored on them, and, on the other hand, on the security of the places of use or storage.

As a general rule, all laptops that are to be used externally should be appropriately licensed.

Outside the institutional real estate, users are responsible for protecting the laptops entrusted to them. These and the precautions to be taken are to be noted.

#### SYS.3.1.M2 Access protection on the laptop [user]

Every laptop should be provided with access protection that prevents it from being used without authorization. Thus it is possible in almost all operating systems to set up login passwords and to provide them with suitable restrictions (eg minimum length, service life). Since these on-board means are only limitedly secure, it is recommended to use additional security hard- or software on laptops with data worthy of protection. These include, for example, chip cards or tokens, which secure the authentication.

If the data on the laptop is not encrypted, employees should be prohibited from storing sensitive information on their hard drive (see SYS3.1.M13 * Encryption of Laptops *). Instead, they should be stored on encrypted mobile disks, eg. B. USB sticks. These are then kept separately from the laptop.

For short work interruptions it is essential to activate an access protection, eg. For example, a password-protected screen saver. If it is foreseeable that the interruption lasts longer, the laptop should be switched off.

#### SYS.3.1.M3 Use of personal firewalls
Personal firewalls control and prevent access to clients via connected IT networks or from clients to these networks. Depending on the type of network service and the direction of the connection setup, the personal firewall of the client can allow or reject a communication setup. For example, a personal firewall could be configured to allow all connections made by the client and to block all incoming requests.

Personal firewalls can work on different principles:

Stateless personal firewalls use properties of the transmitted data packets (such as source and destination addresses or ports) to decide whether to allow or deny the connection. In essence, this is the sender or destination address and port number of the service used. Stateless personal firewalls can often be bypassed with crafted packages.
* Context-sensitive (stateful) personal firewalls also consider previous packets when deciding. Thus, a context sensitive personal firewall can put a packet under test into the context of a connection and only allow it if the connection itself is allowed. Packages that do not fit into the connection context are discarded.
* Application firewalls can check network traffic based on the application that wants to connect. For this purpose, the application firewall has a whitelist in which the communication-authorized applications are entered. Non-whitelisted applications will not be able to establish or receive connections over the network.
Many operating systems already include a personal firewall. This often only needs to be activated. Depending on the operating system, various functions are available. In addition, various third-party security solutions ("Security Suite") are offered, which include a personal firewall. In many cases, the integrated personal firewalls in the operating system are less extensive and less comfortable than the security solutions. For this, these on-board solutions can be activated immediately and there are no additional costs for the procurement. It has to be decided whether the on-board personal firewall or a solution from a third party manufacturer should be used; mixed operation should be avoided.

** operational environments **

Personal firewalls are not enough to protect a government or enterprise network from attacks from the Internet. The sole use of personal firewalls has the following disadvantages:

* All clients connected directly to the Internet must be specially hardened, i. H. The potential operating system vulnerabilities must be addressed as the client is not protected by other IT systems, such as security gateways.
* As with any decentralized software, it is time-consuming to manage the individual personal firewalls and evaluate the respective protocols.
It should be checked on which laptops and under which conditions a personal firewall should be used. Maybe they can be waived if the laptops are operated only in a LAN with a protective security gateway. In the case of a higher protection requirement, however, the use of personal firewalls should also be checked in this case.

If laptops are connected directly to the Internet, they should be protected by a restrictively configured personal firewall against attacks from the network.

Due to the diverse range of functions of the various variants of personal firewalls and their complexity must be ensured that they are administered only by suitable personnel. Users should not have to configure them themselves or change the settings.
** Personal firewalls as part of a security solution **

Personal firewalls are now offered by many manufacturers. Institutions usually have to buy a license for this. Personal firewalls are often tested in journals. The results of these tests can help to find a suitable product.

In principle, it is z. For example, in the case of large third-party security solutions that include a personal firewall, they can be used to check clients for malicious software that can be transmitted via email, Java, ActiveX, or similar mechanisms. For this purpose, mechanisms such as sandboxing can be used, with which the access of applications that are transferred from the Internet to the local system (Java, ActiveX, etc.) can be restricted. These often extensive security solutions decentralize the check for malware and thus relieve the central firewall system. Another advantage is that the problem of filtering encrypted data on the central firewall can be circumvented.

**Configuration**

When configuring and operating a personal firewall on laptops, the following aspects should be considered:

* The filter rules should be set as restrictive as possible. The principle applies: Everything that is not expressly permitted is prohibited. It is recommended that outgoing connections may only be established by approved applications or services. Based on the IP address of the target system, the port number of the required service and the accessing application or the accessing service, the following accesses established by the client could be restricted or allowed: Incoming connections should be restricted to those for remote maintenance, software distribution, system update and monitoring the required services and the server systems used for this purpose.

 
+ to file servers, to the Internet for the browser via the security gateway,
+ to the internet for the browser via the security gateway,
+ to the email and calendar server for the email and calendar application,
+ to update servers on the local network to update the operating system, applications and especially the antivirus program,
+ Communication to any existing central logging service for all services and applications that log messages.


 
* Incoming connections should be restricted to those required for remote maintenance, software distribution, system upgrading and monitoring of required services and server systems.
* Personal Firewall filtering rules should be tested after initial configuration to allow allowed events and prevent unauthorized events.
* The correct configuration of the filter rules should be checked at sporadic intervals, if the installation of the client is not regularly deleted anyway and re-recorded from a hard disk image (images).
* If the product used offers this option, the rules of the Personal Firewall should also be assigned to special programs. This can be detected and prevented that other than the intended client programs connects to computers on the Internet.
* Since many of the checking mechanisms of a personal firewall are based on current findings, patches or updates released by the manufacturer must be regularly imported. It must be ensured that the required files are obtained from a trustworthy source, for example directly from the manufacturer.
* The Personal Firewall must be configured so that users are not bothered by many alerts that they can not interpret.
* If the product used offers this option, security-related events should be logged. The log data should be evaluated regularly by expert personnel.
Some products have the ability to start with a very restrictive basic configuration and then refine the settings during operation. Each time a security-related event occurs that does not yet have a unique rule, the user is asked if that event is allowed. An example of such a security-related event is the access of a particular installed program to the Internet. Based on the user's responses, the personal firewall will determine the desired configuration step by step, e.g. For example, the filter rules.

The advantage of this incremental configuration is that it makes administration less complex. The disadvantage, however, is that users often can not judge whether a particular event is allowed or not. The incremental configuration of the personal firewall can therefore only be recommended if the users are either given precise instructions on how to respond to queries from the program or if this is done under the supervision of an administrator, eg. B. by telephone inquiries.

#### SYS.3.1.M4 Using Anti-Virus Programs [User]

In order to protect against malicious programs, different principles of action can be used (see OPS.1.1.4 * Protection against malicious programs *). Anti-virus programs that scan IT systems for all known malicious programs are a powerful tool in malicious program prevention. Therefore, they must be installed and activated depending on the installed operating system and other existing protection mechanisms.

** Regular examination of the entire database **

Even if the antivirus program checks for malicious programs every time you access files, it must periodically scan all files on the laptop. This way malware can be found for which there was no signature when it was saved. In such cases, for example, it must be investigated whether the malicious program has already collected confidential data, disabled protection functions or downloaded code from the Internet.

For performance reasons, the dataset should only be fully validated when IT resources are not under heavy use. It is ideal if the software monitors whether the laptop is busy and automatically uses its "breaks" to check it. The antivirus program could z. B. also be coupled with the start of the screen saver.

** Data exchange and data transfer **

Data to be sent must be checked for malware immediately prior to shipment. Similarly, received data must be checked for malicious programs immediately upon receipt. These checks are required both when accessing data carriers and when transferring data over communication links. They should be automated as much as possible.

** Interactions with encryption techniques **
When encryption techniques are used, it is important to consider how this affects the protection against malware. If data is encrypted, system components or applications can not access this data unless they have the appropriate key. This implies that an anti-virus program must either run in the context of the user or be equipped with the appropriate cryptographic keys to check an encrypted file for malware. However, if the user ID under which the antivirus program is run is provided with the appropriate cryptographic keys, new security risks are created which should be avoided. Therefore, it is recommended to use a resident antivirus program that checks for malicious programs in the user context each time a file is accessed.

** Protection against unauthorized deactivation or change **

The antivirus programs on the laptops must be configured so that users can not change security-related settings. In particular, it must be ensured that the users can not deactivate them.

#### SYS.3.1.M5 Backup [User]

As a rule, laptops are not permanently integrated in a network. Data exchange with other IT systems usually takes place via temporary network connections. The latter can be realized, for example, by a Virtual Private Network (VPN) or direct connection to a LAN after returning to work. Unlike stationary clients, it is therefore usually unavoidable for laptops that data is at least temporarily stored locally instead of on a central server. It is therefore important to prevent data loss by using appropriate data protection measures.

In general, the following methods for data backup are available:

* ** Data backup on external media **
 The advantage of this method is that it can be backed up almost anywhere, anytime. The disadvantage is that additional disk, z. As external hard drives, must be carried and that arises for the user more effort for the proper handling of the disk. The volumes should have sufficient storage capacity so that the user does not need to use multiple volumes per backup operation. In the case of unencrypted data storage, there is also the danger that data carriers will be lost and thus valuable data can be compromised. The data carriers and the laptop should be kept as separate as possible, so that they do not get lost if the laptop is lost or stolen.
 The storage on external data carriers for data backup is particularly suitable, even if the data exchange with other IT systems via external data carriers takes place. These two processes can also be combined. After returning to the workstation, the data backups on the data carriers must be entered in the backup system or in the production system or central data storage of the institution.
* ** Data backup over temporary network connections **
 If it is possible to connect the laptop regularly to a network, for example via VPNs, the local data can also be secured via the network connection. It is advantageous here that the user does not have to manage and carry data carriers. Furthermore, the method can be largely automated, for example, the backup can be started automatically when using VPNs after each dial-up.
Decisive for data backup over a temporary network connection is that their bandwidth must be sufficient for the volume of data to be backed up. Data transfer should not take too long or cause excessive delays if the user needs to access remote resources at the same time. Some backup programs therefore offer the ability to transfer only information about the changes in the database since the last backup over the network connection. In many cases, this can greatly reduce the volume of data to be transported.
 The backup software must detect and handle unexpected disconnects. The consistency of the backed up data must not be affected by disconnections.
In both methods of data protection, it is desirable to minimize the volume of data to be backed up. In addition to lossless compression methods, which are integrated in many backup programs, incremental or differential backup methods can also be used. However, this may increase the overhead of restoring a backup.

Data backup should be automated as much as possible so that users have only a few actions to perform themselves. If user collaboration is required, they should be required to perform backups regularly. Finally, it should be sporadically checked whether created backups can be restored.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "laptops".

#### SYS.3.1.M6 Security Guidelines for Laptops [IT Leader]

Laptops used outside your own institution are exposed to more risks than those located within protected premises. But there are ways to protect them on the way. A security policy should be created describing all security mechanisms to be implemented. In addition, users should be provided with a short and clear leaflet describing how laptops are used safely.

** Sensitization of users **

The smaller and lighter IT systems become, the more frivolous experience has shown. Therefore, employees should be made aware of the value of mobile IT systems and the value of information stored on them. You should also be educated about the specific hazards of laptops and the necessary measures.

Employees should also be advised that they should not exchange confidential information with anyone on the move and should not make it outside the hearing and sight of others on the move. In particular, the identity of the communication partner should be questioned before providing detailed information.

** Regulations for the use of laptops **

For the safe use of laptops, various points have to be settled:

* Users must be aware of what information they are allowed to handle with laptops on the go. The data should be classified to make restrictions transparent to users. Service secrets may only be processed on laptops if appropriate and approved security mechanisms are used.
* Data that requires a high degree of security (eg offers, design data, economic data of a company) should always be stored encrypted on the laptop.
* Clarify whether on-the-go mobile employees have access to internal data from their institution. If so provided, this access must be adequately protected (see also SYS.3.1.A9 Secure remote access while on the road and SYS.3.1.A8 Secure connection of laptops to local area networks).
* It needs to be clarified if laptops can be used for private purposes.
* Users should be advised how to handle laptops carefully to prevent loss or theft, or to ensure a long service life (eg battery care, safe storage outside of the office or living room, sensitivity to excessive use) or too low temperatures).
* It should be regulated how laptops are managed, maintained and shared.
* Each time a user changes, all required passwords must be securely transmitted.
* Laptops and their applications can often be secured by PINs or passwords. These mechanisms should also be used.
* It should be determined how to work in public environments (see INF.9 Mobile Workplace).
* It should be considered to record when and by whom which laptop was used outside the home.
If laptops are used in foreign office rooms, the security regulations of the visited institution must be observed. In foreign premises such as hotel rooms, they should not be left unprotected. All password protection mechanisms should be activated at the latest now. If the devices are trapped in a closet, this hampers at least occasional thieves.

** Disposal of data carriers **

It is to be regulated how disused data carriers and devices are to be disposed of. A laptop that has become defective on the way must be transported back with it and must not be disposed of on the way. This also applies if the data carriers are defective, since experts can recover valuable information from this as well.

** Terms ban **

Consideration should be given to restricting or prohibiting the use or bringing in of laptops in all or certain areas of an institution. This can z. B. be useful for meeting rooms. If the institution's security policy does not allow laptops to be brought along, it must be clearly indicated on all entrances. That should then be checked regularly.

#### SYS.3.1.M7 Regulated handover and return of a laptop [user]

Depending on the purpose, laptops are only used by a single employee. B. as a workstation, which is also used for mobile. But they can also be used alternately by different employees, for. For presentations. Depending on the type of application, different security requirements arise. Therefore, the purpose and type of use should be carefully planned.

If the laptop is a workstation, it is typically used alternately mobile and stationary. It is possible to access different networks. For this purpose, the laptops must be secured in such a way that on the one hand the mobile application can not compromise, manipulate or lose important data of the laptop. On the other hand, laptops should not introduce any threats to the internal networks.

When laptops are used in turn by different people, a controlled transfer is extremely important. For this to work, a laptop pool should be set up (see SYS.3.1.A17 * Collective Storage of Portable IT Systems *).

If a laptop is handed over or taken back, the following points should be noted:

**Handing over:**

* The new user is prompted to change the old password of the laptop or the default password immediately upon transfer.
* The new user should be given a leaflet for safe handling of the portable IT system.
* In order to make it comprehensible at all times, where the devices are located, each user should be entered in a handover / return journal with name, organizational unit, telephone number, purpose.
** Redemption or transfer: **

* The user announces his last used password or sets a default password.
* The laptop must be scanned for malware using a current antivirus program.
* The user must ensure that all data still required by the user is transferred to data media accessible to him prior to handing over the device. In addition, the user must ensure that all files and data generated by him are deleted. For this purpose, suitable tools must be available.
* The return of the laptop and the result of the virus scan are documented. The completeness of the device, the accessories and the documentation must be ensured.
* To ensure that the defined secure basic configuration is present and there are no more vulnerable files on the laptop, it should be reinstalled using a reference installation.
The intended use of the laptops must be documented.

#### SYS.3.1.M8 Secure Connection of Laptops to Data Networks [User]

It is important to determine which regulations are to be observed when connecting laptops to own and third-party LANs and to the Internet. It should be avoided that this affects the secure operation of your own LAN and other IT systems coupled with it, eg. B. by imported malware.

If a laptop is to be reconnected to the corporate or government network after an external deployment, it must first be ensured by a thorough check with current virus signatures that this laptop is not infected.

** Coupling with other IT systems **

Laptops also often exchange data with other IT systems, such as those of business partners. Also, to access the Internet, it is often necessary to pair your device with other IT systems. This can be done in different ways, depending on which techniques the participating devices support, for example via Bluetooth or WLAN interfaces. On the one hand, the transmission techniques must be used safely, on the other hand, the own laptop must be securely configured. These include security measures such. Such as access protection, user authentication, virus protection, personal firewall, restrictive file and resource sharing at the operating system level, and local encryption.

If a laptop is to be connected to third-party networks or to the Internet, it should always be secured via a personal firewall (see SYS.3.1.M3 * Using personal firewalls for clients *).

It should be clearly defined in all institutions which data may be accessed on the way and which not. Above all, all users must be aware of the conditions under which they are allowed to exchange data via external networks or directly with external IT systems.

** Certificates / MAC addresses **

It should be ensured that not every laptop can log on to a LAN. Before a laptop is allowed to access a LAN, it should have successfully authenticated against an authentication server.

To check which devices are in principle authorized for network access, device certificates or MAC addresses can be used, for example. It should be noted, however, that MAC addresses can be forged and therefore should not be used as the sole authentication criterion.

** ACCESS RESTRICTION **

It must be ensured that a VPN user can only access the services required for completing tasks on the servers in the LAN. This could be ensured, for example, by user-level authentication at the application level and the control of traffic using packet filters (packet filters alone are not sufficient due to the forgery of IP addresses).

** DHCP **
Dynamic Host Configuration Protocol (DHCP) automatically assigns temporary IP addresses and routing and DNS server information to connected clients in IP-based networks, eliminating the need for the user to configure the laptop for Internet access.

When DHCP is enabled, an IT system is automatically assigned a valid IP address for the local network so that it can access all shared folders and drives. As a remedy DHCP should be disabled on the laptop, if it is not needed (but then the IP addresses must be distributed manually). On the other hand, the IP address assignment should additionally be checked via the MAC address to determine whether the client should be allowed to join the network.

** Internet access **

It must be regulated whether laptops are allowed to access the internet directly. The critical point here is that it bypasses the intrinsic security gateways and security mechanisms, potentially causing security issues.

If laptops are predictably connected directly to the Internet during mobile use, it is essential to protect them against attacks from the network by means of a restrictively configured personal firewall. The virus protection alone is not enough to ward off all expected attacks. Likewise, it is absolutely necessary to keep the software of the laptop up to date and to install necessary security patches in a timely manner. It makes sense to check whether personal firewalls, other security programs and security patches on the laptop are up-to-date before accessing the production network. It is recommended to use automated tools to carry out these checks automatically, so that in the case of security deficiencies, access to the internal network can be rejected.

The Internet application programs installed on the laptop, especially browsers and e-mail clients, should be operated with secure settings. It should be prevented administratively that the user can change preset options. In addition, tools could be used that limit the functionality of the browser so that it runs in a sandbox-like environment.

For access to Internet applications, where sensitive data such as personal data, internal information or account data is exchanged, at least TLS must be used for encryption.

Depending on the security requirements and the operating environment, there are also various other possible solutions.

* Prohibition of direct internet access: Of course, this solution has the advantage that it is the easiest to implement. However, it limits users' freedom of movement the most and will therefore not be easy to enforce.
* Use of different user IDs: At the operating system level, two different user IDs should be used in this case, one for general business use and the other for Internet access. Here, the Internet ID should have only minimal rights.
* Using different partitions / operating system installations: This solution creates different partitions that are as strongly separated as possible, for example, by different operating and file systems. The stronger the separation, the higher are the hurdles that prevent malware from the Internet or the like from affecting the production environment.
* Virtual machines: In this case, the Internet can only be used via an operating system that is operated in a virtual machine (eg User Mode Linux, UML). The virtual machine separates the browser used from the actual host operating system more than it does without a virtual machine. However, this variant has the residual risk that malicious programs can be copied back and forth between the host operating system and the virtual operating system by means of copy and paste. In this case, the host operating system could be in an unsafe state at the next VPN dial-up.
* Using Boot CDs: This creates a Web-enabled operating environment for Internet use from a read-only medium such as a CD-ROM, which limits its usability by possibly requiring manual entry of necessary IP information. For example, Knoppix can be used for this, a compilation of GNU / Linux software that can run completely from a CD (see [KNOP]).
* Internet access only via VPN (via Intranet via the institution's own security gateway to the Internet). This has the advantage that dangerous contents are sorted out.
** Use of IrDA interfaces **

The Infrared Data Association (IrDA) has published specifications that initially defined the lower layers of a protocol for an infrared interface. Infrared light is used as the carrier for data exchange over short distances. Meanwhile, IrDA also provides higher protocols for different applications. Today, IrDA is supported by all major operating systems, but this interface is becoming less important than Bluetooth, WLAN or USB.

The IrDA standard does not specify security mechanisms that help attackers capture traffic. The data is saved only at the protocol level by means of checksum methods against transmission errors. Security mechanisms such as authentication, cryptographic integrity protection and encryption are not available. Therefore, the IrDA interface should only be activated if there is a specific need.

Since the coupling is only possible in a very limited area, the communication can usually not be overheard. The existing low residual risk due to the scattered radiation of the IrDA components can be further minimized by additional security mechanisms (eg authentication and encryption at the application level) or the replacement of IrDA by line-based transmission.

#### SYS.3.1.M9 Secure remote access from the road [user]

Laptops are also often used to access data from the internal network of an institution while on the move. Usually public communication networks are used. Since neither the institution nor the mobile workers can greatly influence the confidentiality, integrity and availability of the public communications network, additional measures to protect the information are required.

In general, data transfer between a laptop and the LAN of an institution must meet the following security requirements:
* Ensuring the confidentiality of the transmitted data: The data transmission must be encrypted sufficiently securely. In addition to a suitable encryption method, this also includes adapted key management with periodic key changes. Ensuring the integrity of the transferred data: With the transmission protocols used, it must be possible to detect changes in the transmitted data and possibly even correct them. Such changes can be caused, for example, by transmission errors (technical problems) or deliberate manipulation by an attacker. In addition, the use of digital signatures can be useful to ensure data integrity. Ensuring the authenticity of the data: When transferring the data must be trustworthy to determine whether the communication between the right participants takes place, so z. B. a man-in-the-middle attack can be excluded. For this purpose, the communication partners have to authenticate each other, for example via digital certificates. Ensuring the traceability of the data transmission: In order to make a communication comprehensible, logging functions can be used, which can subsequently determine which data was transmitted when and to whom.
* Ensuring the integrity of the transmitted data: With the transmission protocols used, it must be possible to detect changes in the transmitted data and possibly even fix them. Such changes can be caused, for example, by transmission errors (technical problems) or deliberate manipulation by an attacker. In addition, the use of digital signatures can be useful to ensure data integrity. Ensuring the authenticity of the data: When transferring the data must be trustworthy to determine whether the communication between the right participants takes place, so z. B. a man-in-the-middle attack can be excluded. For this purpose, the communication partners have to authenticate each other, for example via digital certificates. Ensuring the traceability of the data transmission: In order to make a communication comprehensible, logging functions can be used, which can subsequently determine which data was transmitted when and to whom.
* Ensuring the authenticity of the data: When transferring the data, it must be possible to reliably determine whether the communication is taking place between the right participants. B. a man-in-the-middle attack can be excluded. For this purpose, the communication partners have to authenticate each other, for example via digital certificates. Ensuring the traceability of the data transmission: In order to make a communication comprehensible, logging functions can be used, which can subsequently determine which data was transmitted when and to whom.
* Ensuring the traceability of the data transfer: To make a communication comprehensible, logging functions can be used, which can determine afterwards, which data was transferred when and to whom.
The strength of the mechanisms required depends on the protection requirements of the transmitted data. How adequate cryptographic procedures and systems can be selected and used is described in module CON.1 * Crypto Concept *.

** ** VPN
External access to the internal network from a laptop should only be done via a Virtual Private Network (VPN) (see NET.3.3 Virtual Private Networks (VPN)). Corresponding products are available from various manufacturers and for virtually all common platforms. Data or systems with high protection requirements may not be accessed without appropriate safeguards. If the institution operates a filter for malicious software in its network, then the network connection of the laptop should be routed through this filter in order to better protect the end device against malicious software.

If the institution allows to retrieve business e-mails via the Internet using a web-mail solution, it must be ensured that the e-mails are only transmitted in encrypted form from the server to the laptop. B. by TLS. However, not only the transport channel, but also the end system itself must be specially secured. A laptop can be compromised if, in addition to the use of VPN at the same time also standard protocols such. B. HTTP or SMTP can be used on the Internet. Therefore, laptops should be secured in such a way that no other connections are possible with existing VPN connection into the internal network (split tunneling). It must be ensured that all outgoing data packets of the client go into the tunnel and only data packets from the tunnel are accepted.

In this context, it should also be ensured that, in addition to the VPN-secured laptop access, other network accesses to the internal network are not possible at the same time. In particular, no WLAN or Bluetooth may be active on the laptop during the VPN accesses.

** Authentication of VPN usage **

A laptop can easily fall into the wrong hands. Before a VPN is established, the authenticity of the user should be ensured with strong authentication procedures. Strong authentication methods are, for example, one-time password or challenge-response methods.

** ** logging

The accesses to server services should be logged. It should also be apparent whether the laptop access was from the institution or from external. More detailed logging information can be found in OPS.1.1.6 Logging.

** Temporary data **

It should be ensured that all cached authentication information that enables the establishment of a VPN will be automatically deleted after the end of the VPN usage. This applies to both intentionally and unintentionally terminated VPN connections. In addition, for example, with browser-based SSL VPNs, care should be taken to deactivate all intermediate stores, so that authentication information is not temporarily stored at all. Otherwise, this could allow an attacker to recover the VPN connection.

Further BSI recommendations for secure remote access can be found in the document * * "Secure Remote Access to the Internal Network (ISi-S)" [SFIN].

#### SYS.3.1.M10 Synchronization of Laptop Databases [User]

If a laptop is being used on the road and is not being used directly on the institution's file servers over a VPN, it is important that all the necessary data and applications are up-to-date. Likewise, data processed on the move should be quickly stored on IT systems within the information network of the institution so that inconsistent data sets do not occur. The easiest way to do this is to periodically synchronize laptops, such as with tools to synchronize files and directories between laptops and workstations or servers.
This should be considered, which information is stored in which places, ie on which servers and in which directories. The first sighting usually shows how many different places in an information network the information relevant for a job is.

So that synchronization processes do not take too long, tools should be selected for this purpose.

* via the files and directories can be automatically adjusted and updated according to predetermined criteria, which can exclude complete directories or even individual files from a copy process via filtering options that can resolve synchronization conflicts. Synchronization conflicts can occur if a file has been changed in different directories since the last synchronization.
* which can exclude complete directories or even individual files from a copy process via filter options, which can resolve synchronization conflicts. Synchronization conflicts can occur if a file has been changed in different directories since the last synchronization.
* can resolve the synchronization conflicts. Synchronization conflicts can occur if a file has been changed in different directories since the last synchronization.
Synchronization tools should also be as user-friendly as possible and still protect against incorrect operation. Synchronization processes should be access-protected, with laptops this can be done via existing access protection procedures.

To prevent attackers from manipulating the synchronization, users should periodically inspect the relevant directories for any unknown files. The synchronization software should be configured to prompt the user before programs are installed. The synchronization process should not run unnoticed, even the information on which files are transferred, can contain crucial information. The synchronization should be logged. The logs should then be at least regularly flown over to see if any unauthorized synchronization has taken place.

#### SYS.3.1.M11 Ensuring power supply [user]

In order to maintain the power supply of a laptop on the road, usually batteries are used. These can power the laptop for a limited period of time, usually a few hours, depending on capacity and design. It is difficult to estimate this period more accurately because it depends heavily on the age of the accumulator and the intensity of use. To avoid losing data in volatile memory when the battery is empty, some boundary conditions should be met:

* The laptop's warning lights showing the voltage drop should not be ignored. They should be configured so that after the first warning there is still enough time to For example, to store important data or close open programs.
* If a long-term mobile use is foreseeable, the batteries must first be fully charged and possibly carry spare batteries. In addition, many laptops have so-called battery packs that can be connected via an external interface. A replacement battery should be kept in a protective cover, as it may result in overheating or fire damage if the contacts of the battery come into contact with conductive materials. This can be caused by many items of daily use, e.g. By keys or chains.
* Especially with older batteries, the use times are shortened and they discharge towards the end of the capacity very quickly. Open files must therefore be saved regularly to avoid data loss. Since such batteries can discharge quickly even in stand-by mode, the state of charge should be checked regularly. For emergencies, backups of the laptop's configuration data should be included. It is recommended to replace the battery as soon as such aging phenomena occur.
* The laptop should be charged as recommended in the manual so as not to affect the life of the battery.
* Before traveling or when a laptop is handed over, make sure that the batteries or batteries are sufficiently charged. The state of charge should be checked regularly as a battery discharges when it is not in use.
* The charger should always be carried. Only in exceptional cases, for example, predictable short mobile use, it is unnecessary.
It is also advisable to additionally store the processed data on a non-volatile medium at short intervals. Automatic backups can also be used in standard programs.

Before the battery is replaced, the laptop should be turned off to prevent damage to the memory.

#### SYS.3.1.M12 loss report [user]

If an office laptop fails, it is defective, destroyed, lost or stolen should this be reported immediately. This also applies to private devices that are used for business purposes. For this purpose, there should be clear reporting channels and contact persons in each institution.

In particular, if a laptop is lost or stolen, must be acted quickly, since it is not just about the replacement of the devices, but also that the information concerned will not be misused. Laptops may contain sensitive data that requires immediate action, such as:

* Access data such as passwords: All access data in any affected IT system must be changed immediately. Information classified as confidential: All affected areas (eg department, customers) must be notified in order to take appropriate action.
* Information classified as confidential: all affected areas (eg, department, customers) must be notified to take appropriate action.
If possible, measures should be taken after a laptop is lost to lock, erase, or locate the device. Most Mobile Device Management (MDM) solutions (see SYS.3.2.2 Mobile Device Management) provide these features. Clear rules must first be defined and appropriate measures must be taken immediately in consultation with the user whose terminal device was lost.

If lost devices reappear, they should be examined for possible tampering. For example, if screws have been opened, seals removed, or if the weight has changed from the delivery condition. If there is a suspicion, the device should either be disposed of immediately or further examined by a specialist. To ensure that there are no malicious programs on the recovered devices, the devices must at least be reinstalled (SYS.3.1.M7 * Controlled transfer and return of a laptop *).

#### SYS.3.1.M13 Encryption of laptops

An encryption program should be used to prevent sensitive data from a stolen laptop being read out. With the help of the marketable products, it is possible to encrypt individual files, certain areas or the entire hard disk in such a way that only the person with the secret key can read and process the data.
The security of the encryption depends on three different points centrally:

* The encryption algorithm used must be such that, without knowing the key used, it is not possible to reconstruct the plaintext from the encrypted text. Not possible here means that the required effort, with which the algorithm can be broken or decrypted, is disproportionate to the information gain that can be achieved thereby.
* The key is suitable to choose. He should be generated randomly. If it is possible to choose a key such as a password, the rules of the institution should be followed for password usage.
* The encryption algorithm (the program), the encrypted text and the keys must not be stored together on a data medium. It is advisable to keep the key individually. This can be done by writing it on a cardboard card in the form of a check card and then storing it in the wallet like a bank card. The cryptographic keys should be stored on a removable disk such as a hard disk. B. stored on a USB stick and stored separately from the laptop.
Encryption can be done online or offline. Online means that all hard drive (or partition) data is encrypted without the user having to actively do so. Offline encryption is explicitly initiated by the user. He then has to decide which files should be encrypted. For selection and use of cryptographic methods, module CON.1 * crypto concept * should also be considered.

#### SYS.3.1.M14 Suitable storage of laptops [user]

Users must be careful to keep their laptops safe outside of the institution. For this only a few hints can be given, which are to be considered:

* Laptops should not be left unattended if possible.
* If a laptop is stored in a motor vehicle, the device should not be visible from the outside. For example, it should be covered or locked in the trunk. A laptop can be a high value that attracts potential thieves, especially as such IT systems can be easily sold.
* If the laptop is used in a foreign office, the employee should take it with him if he only leaves the room for a short time or he locks the device. At least one access protection should be activated to prevent unauthorized use. If the room is left for a long time, the laptop should also be switched off.
* In hotel rooms, the laptop should not be left unattended. If the device is locked in a cupboard, it stops at least occasional thieves.
* A laptop can also be secured by a lock. A thief then needs tools to steal it.
* A laptop should never be exposed to extreme temperatures. In particular, the battery and the display can be damaged. Neither laptops nor batteries should be left in parked cars when the outside temperature is extremely high or low.
* Similarly, laptops should be protected from harmful environmental influences, such as moisture from rain or splashing water.
* Laptops are not indestructible, so they should be transported as shockproof as possible, even on shorter transport routes. For example, they should always be collapsed, as both the hinges and the screen can be easily damaged in a fall. In principle, a protective container should be used for the transport, for example bags or rucksacks with their own compartments and padding for laptops.
It is advisable to create a leaflet for the users of laptops containing the most important information and precautions on how to properly store and transport the devices.

** Suitable storage of laptops in stationary use **

Due to their design, laptops are always popular targets for theft. Therefore, they must be kept safe even if they are in the supposed safe office. Therefore, the requirements described in module INF.8 * Workstation * must be observed. However, since a laptop is particularly easy to transport and hide, the device can be locked away during off-peak hours, such as being locked or chained in a closet or desk.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### SYS.3.1.M15 Appropriate Selection of Laptops [Procurement] (A)

Laptops are available in various variants and device classes. These differ not only in their dimensions and features, but also in the safety mechanisms and ease of use. In addition, they make different demands on hardware and software components in the operating environment.

With the large number of different laptop models with the most different operating systems, compatibility problems with hardware, software on laptop and PC as well as interfaces are obvious.

First, a requirement analysis should be carried out. On the one hand, the goal here is to determine all possible application scenarios and, on the other hand, to derive requirements for the required hardware and software components.

The following list gives a rough overview of possible general evaluation criteria. However, it does not claim to be complete and can be extended to include further general requirements.

** General criteria **

* Maintainability
*

 
+ Is the product easy to maintain?
+ Is the device supported by the manufacturer for the intended period of use? Does the manufacturer offer regular software updates?
+ Are maintenance contracts offered for the product?


 
* Reliability / reliability
*

 
+ How reliable and fail-safe is the product?
+ Is the product suitable for continuous operation?
+ Is there a built-in backup mechanism in the product? Can an automatic backup be performed?


 
* User friendliness
*

 
+ Is the product easy to install, configure and use?
+ Is the synchronization software configurable so that users are minimally burdened with technical details? Is security always guaranteed?
+ Are dimensions and weight appropriate to the application? Is the battery life sufficient for your daily work? Can the battery be replaced if the battery life is insufficient and the device can not be charged in the meantime?


 
* Costs
*

 
+ What are the initial costs of hardware and software?
+ What are the anticipated running costs of hardware and software (maintenance, operation, support)?
+ What are the expected running costs for the staff (administrator / support)?
+ Do you need to purchase additional software or hardware components (eg docking station, conversion software)?


 
**Function**

* Installation and commissioning
*

 
+ Can the device as well as the synchronization software be configured in such a way that the specified safety goals can be achieved?
+ Can important configuration parameters be protected against changes by users?
+ Does the product work with common hardware and software (operating systems, drivers)?


 
* Administration
*

 
+ Does the supplied product documentation contain an exact description of all technical and administrative details?
+ Can the laptops be administered via a centrally controlled management software? Is the administrative interface designed to point out or prevent erroneous, insecure, or inconsistent configurations?


 
* Security: communication, authentication, access and logging
*

 
+ Does the laptop support all the necessary data transmission technologies (eg Bluetooth, WLAN, LAN)?
+ Can the product transfer the data to other devices securely?


 
*

 
+ Does the laptop have suitable mechanisms for identifying and authenticating users?
+ Can additional security mechanisms (eg encryption or anti-virus programs) be used?
+ Does the product architecture allow the subsequent installation of new security mechanisms?
+ Is the mobile user allowed access to local devices only after successful authentication?
+ Is the system architecture designed so that new authentication mechanisms can be integrated later?
+ Can the laptop be used for appropriate logging or can it be integrated into existing logging processes?


 
Once all the requirements for the product to be procured have been documented, the laptops available on the market must be examined to what extent they meet these requirements. It is to be expected that not every product will meet all requirements at the same time or equally well. Therefore, the individual requirements should be weighted. Based on the product evaluation, a sound purchasing decision can be made.

Practice shows that due to various application requirements, it may be sensible to select several different device types for procurement. The variety of devices should be limited, so that the support is easier.

#### SYS.3.1.M16 Central administration of laptops (CI)

The administration of mobile devices is not an easy task, especially for large institutions and for users who move frequently and around the world. There are tools that facilitate central administration and the implementation of security policies. Centralized administration not only distributes software and information, but also enforces the institution's own security policies on laptops. For authentication, access or backup.

If software is used for centralized laptop management, the laptops synchronize with a server. Not only can data be reconciled, but also technical specifications can be forced by restoring safety-relevant settings to their specified values. Typical features of such tools for centralized laptop management include:

* Backups can be done centrally without the users having to worry about it. Likewise, specifications can be made as to when or how often data is to be saved or synchronized and which boundary conditions must be met.
* It is possible to get feedback on the status of the laptops and to perform diagnostics remotely.
* User profiles can be created to simplify user administration.
* Password rules and other security rules can be specified.
A tool for centralized laptop management should support as many as possible operating systems used in the institution so that several such tools do not have to be used in parallel. The same applies of course to the groupware and e-mail platform used. More detailed information can also be found in SYS.3.2.2 Mobile Device Management.

#### SYS.3.1.M17 Collective Storage (A)

If many laptops are in mobile use in an institution and the users change frequently, it may be appropriate to keep the temporarily unused devices in a collective pool. The space used should comply with the requirements of INF.5 * Technikraum *.

In addition, ensure the power supply of the laptops so that the batteries of these devices allow immediate use (see SYS.3.1.M11 * Ensuring the power supply *). In addition, the return and the issue of portable IT systems must be documented (see SYS.3.1.M7 * Regulated transfer and return of a laptop *).

#### SYS.3.1.M18 Using theft-proofing (CIA)

Anti-theft devices can be used wherever there is a need to protect large assets or where other measures can not be implemented, such as laptops in mobile use. Anti-theft backups are also useful where there is public traffic or where the turnover of users is very high. It should always be kept in mind that the values ​​to be protected are only a small part of the replacement cost of the device, but that the value of data stored on laptops must be taken into account.

** Preventing a Cold Boot Attack **

In areas that are not sufficiently protected against unauthorized access, for example, could be read by a cold boot attack the memory. The same applies to systems that have been put into a power-saving mode by Suspend to RAM.

In a cold boot attack, the memory chips are heavily cooled before the system is turned off. The memory content is retained for several minutes and can be read while using a suitable device.

Cold boot attacks can only be prevented if attackers are unable to access the memory of an active IT system without being disturbed. Access protection, such as a physically locked computer chassis, makes it difficult to open an IT system without authorization to cool and extend the memory, but it can not permanently prevent it. Therefore, an unused laptop should always be turned off when it is not in an access-protected area.

** Types of theft-fuses **

The market offers a wide variety of theft security devices. These can first be divided into mechanical and electronic fuses.

The mechanical fuses include, but are not limited to, cable retainers, housing retainers (to protect the housing from opening), security panels, and security enclosures. There are hardware backups that prevent the theft of IT equipment, such as: For example, by connecting the laptop to the desk. On the other hand, there are a number of safety mechanisms to prevent the case from being opened. This is to prevent attackers stealing parts or manipulating security-related settings, such as removing security cards.

When purchasing mechanical fuses, it is important to choose a good lock that has a locking system that is tailored to the individual needs. Depending on the product, different locking systems are possible:
* concurrent: A key fits all device backups of an institution, department, etc. This has the advantage that the expense of key management is lower. However, it also means that very many similar keys can be in circulation and that in case of damage often no evidence is possible.
* different closing: Each device fuse has an individual key. This has the disadvantage that the expense of key management is higher. But it has the advantage that there are fewer key duplicates.
* Master Key System: Each device backup has an individual key, but can also be opened by a master key. This has the advantage that the effort for key management is lower. But it has the disadvantage that such systems are more expensive to buy.
Most laptops have a small slot marked with a chain or lock symbol. This small opening is located on the side or rear of the unit. There are a wide range of cable retainers and other products that use this opening for securing devices.

In the case of cable fuses, only one cable loop must be placed around a solid object close to the device, and the associated lock must be pulled and closed by the resulting tab.

For devices that do not have this opening, or where this is not strong enough, there are backup products where a stable plate is glued to the device. At this then the security cable is attached.

In addition, there are electronic fuses, for example, trigger an acoustic deterrent alarm on the device itself, which should bring potential thieves to leave the laptop.

When buying new laptops, care should be taken that they have eyelets on the housing so that they can be attached to other objects.

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Further information on "Laptops" threats and security measures can be found in the following publications, among others:

* #### [KNOP] KNOPPIX

  

 Live Linux File System On CD,
 <Www.knoppix.org>

 
* #### [SFiN] Secure remote access to the internal network (ISi-S)

  

 Federal Office for Security in Information Technology (BSI), 09.2010
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/isi\_fern\_studie\_pdf.html](https://www.bsi.bund.de/SharedDocs/Downloads/ DE / BSI / Internet security / isi_fern_studie_pdf.html)
