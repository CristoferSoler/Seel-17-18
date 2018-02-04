[toc]
 
1 description
--------------

### 1.1 Introduction

A laptop (or notebook) is a PC that can be used as a mobile device. It has a compact design, integrates peripherals such as keyboard and screen, is at times independent of an external power supply via batteries and often consists of specially designed for mobile use hardware components. Laptops can be operated with all common operating systems like Windows, Apple macOS or Linux. The devices are common in most institutions and replace the classic desktop PC for some employees.

Often, laptops are not permanently connected to the institution's LAN because they are often used as mobile devices, but can usually dial in via the Internet or other data networks via Virtual Private Network (VPN) to access the resources of the LAN. Also, the infrastructure of a classic office environment, such as controllable environmental influences, a stable power supply or access protected areas, can not be expected for the mobile use of laptops.

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

Employees also regularly use their laptops outside the institution. The devices are transported in private motor vehicles or public transport, left in other offices in breaks or placed in hotel rooms unguarded. Due to these environmental conditions, laptops are naturally exposed to higher theft risk. If a laptop is stolen, costs for the recovery and for the restoration of a working condition arise. Likewise, this could also be disclosed to unauthorized data worthy of protection, which can lead to further damage. In many cases, these weigh considerably heavier than the mere material loss of the device.
### 2 3 Unsolicited user switching on laptops

When employees seldom need mobile IT systems, such as infrequent business travel, it is often more convenient to have a few laptops available to many users who are being passed on. However, if the laptop is simply handed over to the next employee during a user change, there is a risk that the device still stores sensitive data and that it is contaminated with malware. In addition, after some time is no longer understandable who used the laptop when or who is currently using it. The unordered change of users without memory controls and without corresponding documentation can lead to the fact that the laptop is only limited available and residual data on the hard disk can be read without authorization.

### 2 4 Synchronization error

When data is edited locally on a laptop, it must be synchronized with the institution's file servers whenever possible, e.g. For example, if the employee logs in again via the VPN. However, the data can also be destroyed. In general, before synchronization, you have to set how to handle conflicting data reconciliation: whether, for example, the version on the laptop or the version also edited by another employee on the server is updated on the server without being asked, or if the user should decide. This is often configured once and often forgotten afterwards. But if data is changed in a different order than originally thought, then important information is quickly lost.

### 2 5 Data loss in mobile use

For laptops, the risk of data loss is higher than for inpatient systems. The cause may be theft or loss of equipment, but also technical problems or simple lack of power. For example, a laptop's data may be temporarily unavailable when the battery is empty. You may be able to B. in older devices, but also completely destroyed, if in addition to the battery and any backup battery is empty and thus all not already synchronized data are lost.

### 2 6 Data theft with laptops

With laptops, data can easily be exchanged with other IT systems. B. over WLAN, Bluetooth or a cellular connection. Where open access to a laptop is possible, attackers can unobtrusively query, change or take information with them. Subsequent verification or even proof is not always possible, as frequently the accesses are not logged accordingly. In addition, attackers in public WLANs that are not adequately secured and over which a laptop communicates can record all transmitted data and in the worst case can access the files in the institution's network.
