Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

A laptop (or notebook) is a PC that can be used as a mobile device. It has a compact design, integrates peripherals such as keyboard and screen, is at times independent of an external power supply via batteries and often consists of specially designed for mobile use hardware components. Laptops can be operated with all common operating systems like Windows, Apple macOS or Linux. The devices are common in most institutions and replace the classic desktop PC for some employees.

As laptops are often used on the move, they are often not permanently attached to the institution's LAN, but can usually dial in via the Internet or other data networks via Virtual Private Network (VPN) to access the resources of the LAN. Also, the infrastructure of a classic office environment, such as controllable environmental influences, a stable power supply or access protected areas, can not be expected for the mobile use of laptops.

### 1.2 Objective

The aim of the module is to enable the secure operation of laptops in institutions and to sensitize them to the specific hazards of this device class.

### 1.3 Delimitation

To eliminate the risk of misuse or deliberate misuse of laptops, it is necessary to carefully select and install the operating system and software components. The requirements to be met here depend on the operating system of the laptop and are therefore described in the client-specific blocks, for example SYS.2.2.3 * client under Windows 10, * SYS 2.3 * clients under Unix * or * SYS.2.4 clients under OS X *. Similarly, requirements that apply to any type of client are not part of this building block; they can be found in SYS.2.1 * Common Client *.

Also, it does not discuss how to set up the respective data transmission, such. Eg the WLAN configuration (see NET.2.2 * WLAN usage *) or the VPN connection (see NET.3.3 Virtual Private Networks (VPN)).

In order to be able to detect attempted attacks and abusive use, laptops are primarily responsible for organizational requirements. The necessary requirements are considered in the framework of the implementation of the module OPS.1.1.2 * Proper IT administration * and therefore not here.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the * laptop * area:

### 2 1 Impairment due to changing operating environment

Laptops are used in very different environments and are therefore exposed to many threats. These include, for example, damaging environmental influences, such as too high or too low temperatures, as well as dust or moisture. In mobile devices there is always the risk of transport damage. In addition, laptops often communicate with unknown IT systems or networks, especially on the move, which always brings with it a risk potential for your own laptop. For example, it is possible to transmit malicious programs or copy sensitive information.

### 2 2 Theft

Employees also regularly use their laptops outside the institution. The devices are transported in private motor vehicles or public transport, left in other offices in breaks or placed in hotel rooms unguarded. Due to these environmental conditions, laptops are naturally exposed to a higher theft risk. If a laptop is stolen, costs for the recovery and for the restoration of a working condition arise. Likewise, this could also be disclosed to unauthorized data worthy of protection, which can lead to further damage. In many cases, these weigh considerably heavier than the mere material loss of the device.
### 2 3 Unsolicited user switching on laptops

When employees seldom need mobile IT systems, such as infrequent business travel, it is often more convenient to have a few laptops available to many users who are being passed on. However, if the laptop is simply handed over to the next employee during a user change, there is a risk that the device still stores sensitive data and that it is contaminated with malware. In addition, after some time is no longer understandable who used the laptop when or who is currently using it. The unordered change of users without memory controls and without corresponding documentation can lead to the fact that the laptop is only limited available and residual data on the hard disk can be read without authorization.

### 2 4 Synchronization error

When data is edited locally on a laptop, it must be synchronized with the institution's file servers whenever possible, e.g. For example, if the employee logs in again via the VPN. However, the data can also be destroyed. In general, before synchronization, you have to set how to handle conflicting data reconciliation: whether, for example, the version on the laptop or the version also edited by another employee on the server is updated on the server without being asked, or if the user should decide. This is often configured once and then often forgotten. But if data is changed in a different order than originally thought, important information will quickly be lost.

### 2 5 Data loss in mobile use

For laptops, the risk of data loss is higher than for inpatient systems. The cause may be theft or loss of equipment, but also technical problems or simple lack of power. For example, a laptop's data may be temporarily unavailable when the battery is empty. You may be able to B. in older devices, but also completely destroyed, if in addition to the battery and any backup battery is empty and thus all not yet synchronized data are lost.

### 2 6 Data theft with laptops

With laptops, data can easily be exchanged with other IT systems. B. over WLAN, Bluetooth or a cellular connection. Where open access to a laptop is possible, attackers can unobtrusively query, change or take information with them. Subsequent verification or even proof is not always possible, as frequently the accesses are not logged accordingly. In addition, attackers in public WLANs that are not adequately secured and over which a laptop communicates can record all transmitted data and in the worst case can access the files in the institution's network.

3 requirements
---------------

The following are specific laptop requirements. Basically, the * IT operation * is responsible for fulfilling the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.3.1.A1 Regulations for the mobile use of laptops

It MUST be clear what employees should consider when they take laptops. In particular, it is necessary to specify which laptops may be taken outside the home, who may take them with them and what basic security measures should be taken. Users MUST be advised of the regulations.
#### SYS.3.1.A2 Laptop access protection [user]

All laptops MUST have adequate access protection to prevent unauthorized use of the device. It MUST be checked whether all employees comply with the rules for the correct handling of the established access protection.

#### SYS.3.1.A3 Use of personal firewalls

On laptops, a personal firewall MUST be active. The filtering rules of the firewall MUST be as restrictive as possible. They MUST be tested regularly. The Personal Firewall MUST be configured so that users are not bothered by alerts that they can not interpret.

#### SYS.3.1.A4 Use of anti-virus programs [user]

Depending on the installed operating system and other existing protection mechanisms, an anti-virus program MUST be installed and activated on all laptops of the institution. It MUST be ensured that both the scanning program and the signatures are always up to date. Users MUST be familiarized with the antivirus software, especially with on-demand scans.

The entire database of laptops MUST be regularly checked for malicious programs. If the computer is infected, it MUST be examined in offline mode whether the detected malware has already collected confidential data, disabled protection features or downloaded code from the Internet.

The antivirus program MUST also look for malicious software when exchanging or transferring files. Also, all Internet services (HTTP, FTP) used on the laptop as well as encrypted data MUST be adequately protected against malicious programs.

It MUST also be ensured that users can not make any security-relevant changes to the settings of the anti-virus programs.

#### SYS.3.1.A5 Backup [User]

All data stored locally on laptops MUST be backed up regularly. For this, depending on the volume of the data stock, suitable methods for data backup MUST be selected. Data backup MUST be extensively automated so that users have to perform as few actions as possible themselves.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of laptops. They SHOULD be implemented in principle.

#### SYS.3.1.A6 Laptops Security Policy [IT Leader]

For laptops, a security policy SHOULD be created that governs how the devices may be used. Users SHOULD be made aware of the protection needs of laptops and the data on them. Also, they SHOULD be made aware of the specific hazards or requirements for their use. They SHOULD also be informed about what kind of information they are allowed to process on laptops.

#### SYS.3.1.A7 Controlled Handover and Withdrawal of a Laptop [User]

If laptops are used in turn by different people, SHOULD it be regulated how laptops can be safely handed over to employees or how they can be safely taken back. When changing the user of a laptop, any existing sensitive data SHOULD be safely deleted. If the laptop is not replaced after the user has changed, make sure that there is no malware on the system or any other media attached to it. With a laptop SHOULD give the staff a leaflet for the safe handling of the device.

#### SYS.3.1.A8 Secure connection of laptops to data networks [user]
It was intended to regulate how laptops are securely connected to own or foreign networks and to the Internet. Laptops SHOULD be effectively protected against malicious code and attacks from third-party networks and the Internet. For this, the operating system and the installed software of laptops SHOULD always be up to date. Only approved laptops should be able to log into the institution's internal network. Unnecessary interfaces SHOULD be disabled on all laptops.

#### SYS.3.1.A9 Secure remote access from the road [user]

Data transmitted between a laptop from outside and the institution's internal network SHOULD be adequately protected by appropriate means, such as a VPN or TLS. Also, the laptop SHOULD be secured by itself when sharing data with other IT systems.

#### SYS.3.1.A10 Synchronization of Laptop Datasets [User]

It was intended to regulate how data from laptops are transferred to the information network of the institution. When using a synchronization tool, make sure that synchronization conflicts can be resolved, the synchronization process is logged, and users are instructed to check the synchronization logs.

#### SYS.3.1.A11 Ensuring power supply [user]

All users SHOULD be informed about how they can optimally ensure the power supply of laptops in mobile use. If replacement batteries are available for the laptops, they SHOULD be stored and transported in appropriate cases.

#### SYS.3.1.A12 loss report [user]

It SHOULD be reported immediately if a laptop is lost or stolen. For this, there should be clear reporting channels in every institution. If lost laptops reappear, SHOULD investigate if they have been compromised. They SHOULD be completely reinstalled.

#### SYS.3.1.A13 Encryption of laptops

The hard drives of a laptop SHOULD be encrypted. For encryption, a secure encryption algorithm SHOULD be used. The keys SHOULD be generated randomly and data and keys kept separately.

#### SYS.3.1.A14 Suitable storage of laptops [user]

All users SHOULD be advised on how to keep laptops outside the institution properly. Also in the rooms of the institution, Laptops SHOULD be protected against theft outside the times of use or stored locked.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.3.1.A15 Appropriate Selection of Laptops [Procurement] (A)

Before laptops are procured, the people in charge SHOULD perform a requirements analysis. It SHOULD also focus on additional hardware needed, such as: As docking stations and monitors to be extended. Based on the results, all candidate devices SHOULD be evaluated. The procurement decision SHOULD be coordinated with the administrators and the technical staff.

#### SYS.3.1.A16 Central administration of laptops (CI)
It should be defined a suitable approach, how to centrally manage laptops, as not only easier to distribute software and information, but also the institution's own security policies can be better enforced. Therefore, a suitable procedure should be defined, as laptops are centrally administered. A tool for centralized laptop management SHOULD support as many operating systems as possible.

#### SYS.3.1.A17 Collective Storage (A)

Unused laptops SHOULD be kept in a suitably secured room. The space used SHOULD meet the requirements of * INF.5 technical room *.

#### SYS.3.1.A18 Using theft-proofing (CIA)

It should be regulated which anti-theft devices should be used for laptops. For mechanical fuses, special attention should be paid to a good lock.

4 Further Information
------------------------------

### 4.1 Literature

Further information on "Laptops" threats and security measures can be found in the following publications, among others:

5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Laptops" building block.

* G 0.4 Pollution, dust, corrosion
* G 0.14 Spying out information (spying)
* G 0.16 Theft of devices, data carriers or documents
* G 0.17 Loss of equipment, data carriers or documents
* G 0.19 Disclosure of information worthy of protection
* G 0.22 Manipulation of information
* G 0.39 Malware
* G 0.45 data loss
The cross reference tables can be found in the download area due to their size.
