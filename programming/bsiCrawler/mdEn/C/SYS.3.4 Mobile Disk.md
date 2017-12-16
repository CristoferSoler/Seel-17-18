1 description
--------------

### 1.1 Introduction

Mobile media is used for a variety of purposes, such as transporting, storing or using data on the move. There are many different types of portable media, including external hard drives, CD-ROMs, DVDs, memory cards, magnetic tapes and USB sticks.

Data carriers can be classified according to whether they are read-only, write-once or rewritable. They can also be subdivided according to further criteria, for example the type of data storage (analogue or digital), how they can be processed (without technical aids, such as paper, or only with technical aids, such as DVDs) ) and their design (removable media or external data storage or data carriers integrated with other devices).

### 1.2 Objective

This module shows how the information stored on mobile data carriers can be safely used and how unauthorized disclosure of information via mobile data carriers should be prevented.

### 1.3 Delimitation

This module deals only with the basic security features of mobile data carriers.

The different and sometimes complex requirements for devices that can be used in addition to their main function in addition as a mobile disk, such. As smartphones and tablets are also listed in the blocks that deal with the topic. Likewise, in-depth aspects concerning the exchange of digital as well as analog media are not considered.

Mobile data carriers can be exchanged during personal meetings or by mail. The exchange of digital and analog data carriers to transfer information between different communication partners and IT systems is not considered in this module. For this purpose, the requirements of block OPS.1.2.3 Data medium exchange must be implemented.

In addition to the digital data carriers are z. B. also to consider information on paper or other analog media in the security design. These aspects go beyond the basic security features of mobile data carriers and are therefore covered in other modules (for example [* SYS.4.1 Printers, Copiers and Multifunction Devices *] (DE / topics / IT Grundschutz / IT Grundschutz Compendium / Modules / SYS / SYS_4_1_Printers, _Copier_and_Multifunction_C3) % A4te.html? Nn = 10137184 "SYS.4.1 Printers, Copiers and Multifunction Devices"), NET.4.3 Fax, OPS.1.1.5 Data Backup or [* OPS.1.2.2 Archiving *] (DE / Themen / ITBrundschutz / ITBrundschutzKompendium /bausteins/OPS/OPS_1_2_2_Archivierung.html?nn=10137184 "OPS.1.2.2 Archiving")).

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to mobile media:

### 2 1 Carelessness in handling information

Frequently it can be observed that organizational regulations and technical security procedures for mobile data carriers exist in institutions, but these are again undermined by the careless handling of specifications and technology. For example, it can be observed again and again that mobile data carriers brought along are left unattended in the meeting room or in the train compartment during the breaks.

### 2 2 Insufficient knowledge of regulations

If employees and officials are not sufficiently familiar with the regulations for the correct handling of mobile data carriers, they can not adhere to it. This can lead to numerous threats to information security, for example when USB sticks are thoughtlessly connected to IT systems in the institution.

### 2 3 Data loss in mobile use
For mobile data carriers, the risk of data loss is higher than for stationary systems. One cause of this may be theft or loss of equipment, but also technical problems or simple lack of power. The information stored on the data carriers is often irretrievably lost.

### 2 4 Broken disk

Because of their size and application fields, mobile data carriers are susceptible to damage, errors or failures. Cause are, for example, constantly changing operating environments or mechanical effects.

### 2 5 Theft

Again and again, mobile data carriers are stolen. The smaller and more desirable such devices, such as USB hard drives or USB sticks, the higher this risk. In addition to material loss, further damage can result if sensitive files are lost or disclosed.

### 2 6 Impaired by changing operating environment

Mobile data carriers are used in very different environments and are therefore exposed to many threats. These include, for example, damaging environmental influences, such as too high or too low temperatures, as well as dust or moisture. Other problems caused by device mobility include, for example, shipping damage. Another important aspect is that they are often used in areas with different levels of security. Communication with unknown IT systems and networks always poses a risk potential for your own mobile device. For example, if the media is attached to other IT systems, confidential information that is not intended to be shared can also be copied.

### 2 7 Spread of malware

Mobile data carriers are often used to exchange data between different devices and workplaces. There is a danger that malware will nest on the mobile data carriers and thus transfer to the workstation systems.

### 2 8 Data theft with mobile data carriers

Mobile data carriers, such as. As USB sticks or memory cards, are usually small, unobtrusive and have a high storage capacity. Since almost all IT systems have an appropriate interface for the use of replaceable data carriers, there is a risk that they can copy large amounts of data without authorization and inconspicuity.

3 requirements
---------------

The following are specific requirements for the protection of Mobile Media. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### SYS.3.4.A1 Raising employee awareness about the safe handling of mobile data media

All employees MUST be sensitized for the safe handling of mobile data carriers. Employees MUST also be advised of how to handle mobile media with care to prevent loss or theft or to ensure a long service life.

#### SYS.3.4.A2 Mobile Media Loss Report [User]

It MUST be reported promptly if a commercial mobile volume is lost or stolen. This SHOULD also apply to private data media that are used for business purposes. For this there must be clear reporting channels and contact persons in each institution.

#### SYS.3.4.A3 Backup copy of submitted data [user]
If the data to be transmitted on a mobile data carrier were created or compiled only for the purpose of data transmission and not stored on another medium, a backup copy of this data MUST be maintained.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of mobile data carriers. They SHOULD be implemented in principle.

#### SYS.3.4.A4 Creation of a guideline for the safe handling of mobile data carriers [user]

A policy SHOULD be created that determines how mobile media is handled. The following basic aspects SHOULD be considered:

* which mobile data carriers are actually used and who can use them,
* which data may be stored on mobile data carriers and which not,
* how data stored on mobile data carriers is protected against unauthorized access, manipulation and loss,
* how the data on the mobile data carriers should be deleted
* if and how private media may be used,
* with which external employees or service providers data carriers may be exchanged and which safety regulations must be observed,
how to prevent the use of mobile data carriers for the unauthorized disclosure of information and
* how to prevent the spread of malware via mobile data carriers.
In addition, it should be regulated how private mobile data media may be used in the institution. In addition, it should be checked regularly whether the security requirements for the handling of mobile data carriers are still current.

#### SYS.3.4.A5 Control of the transport of mobile data carriers

There SHOULD set clear written rules that determine if and how mobile media may be taken. In particular, it should be determined which data carriers may be transported outside the home, who may take them away from home, and which basic security measures must be observed (virus protection, encryption of sensitive information, storage, etc.). The users SHOULD be advised of the regulations.

#### SYS.3.4.A6 Disk Management [Specialists]

It SHOULD give a regulated management of mobile data carriers. For this, the data carriers SHOULD be marked uniformly. Inventories SHOULD be kept. Furthermore, in the context of data carrier management, it should be ensured that mobile data carriers are handled and stored properly and properly used and transported. Finally, it should also be ensured that they are safely deleted or destroyed.

#### SYS.3.4.A7 Secure Disk Erase Before and After Use [Specialists]

Before rewritable media are to be redistributed, they SHOULD be erased appropriately before being used or discarded.

#### SYS.3.4.A8 Hedging drives and interfaces for removable media and external data storage

The drives and interfaces of the IT systems for the use of mobile data carriers SHOULD be protected by technical and organizational measures in accordance with the security specifications. This is to prevent contents of inserted removable media from being automatically executed. Also, technical measures SHOULD be taken so that the IT system can not be booted from sources other than the intended ones and can not be connected to unauthorized external devices and data carriers.

### 3.3 Requirements for increased protection requirements
Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.3.4.A9 Control and monitoring of interfaces (CI)

The use of interfaces to which data carriers can be connected SHOULD be regulated by an appropriate assignment of rights at the level of the operating system or with the help of additional programs. It SHOULD be checked whether it can be monitored alternatively, whether devices are added. The connection of data carriers SHOULD be logged and the logs regularly evaluated by the persons in charge.

#### SYS.3.4.A10 Disk Encryption (C)

Mobile data carriers SHOULD always be completely encrypted when the need for protection increases, even if they are occasionally used for confidential information. A secure encryption algorithm SHOULD be used. In order to meet the requirements of confidentiality of the information to be transmitted, appropriate encryption programs SHOULD be installed on the IT system of the sender and the recipient.

#### SYS.3.4.A11 Integrity Protection by Checksums or Digital Signatures (I)

In order to ensure only the integrity of confidential information when exchanging data via mobile data carriers, a method should be used to protect against accidental or intentional changes. Examples are checksum procedures, error-correcting codes, message authentication code (MAC) or "digital signatures". The procedures for protection against changes SHOULD comply with the current state of the art.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and security measures in the area of ​​"Mobile data carriers" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [NIST800150] Guide to Cyber ​​Threat Information Sharing

  

 Special Publication 800-150, National Institute of Standards and Technology (NIST), 10-2016
 <Http://dx.doi.org/10.6028/NIST.SP.800-150>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the "Mobile data carrier" building block.

* G 0.1 fire
* G 0.2 Unfavorable climatic conditions
* G 0.3 water
* G 0.4 Pollution, dust, corrosion
* G 0.14 Spying out information (spying)
* G 0.16 Theft of devices, data carriers or documents
* G 0.17 Loss of equipment, data carriers or documents
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.24 Destruction of equipment or data media
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.38 Abuse of personal data
* G 0.39 Malware
* G 0.41 Sabotage
* G 0.42 Social engineering
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
