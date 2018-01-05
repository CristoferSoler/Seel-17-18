1 description
--------------

### 1.1 Introduction

Mobile data carriers are used for many different purposes, such as data transport, storage of data or data use on the move. There are many different variants of mobile data carriers, including removable disks, CD-ROMs, DVDs, magnetic tapes, USB hard disks and USB sticks. These various forms and applications do not always make all the necessary safety considerations.

Data carriers can be classified according to whether they are read-only, write-once or rewritable. They can also be subdivided according to further criteria, for example

* according to the type of data storage: analogue or digital media, as they can be edited: without technical aids, such as. As paper, or only with technical aids, such as. As DVDs, according to their design: removable media, external data storage or media that are integrated into other devices.
* how they can be processed: without technical aids, such as: As paper, or only with technical aids, such as. As DVDs, according to their design: removable media, external data storage or media that are integrated into other devices.
* according to their design: removable media, external data storage or data carriers that are integrated into other devices.
Interchangeable media, sometimes referred to as removable media, are inserted into a drive. Examples include CD-ROMs, DVDs, Blu-ray Discs, magnetic tapes, and memory cards. External data storage devices, such as USB sticks and external hard disks, can be connected directly to an IT system. Examples of disks that are integrated with other devices include the storage components in smartphones, tablets, and digital cameras.

In addition to the digital data carriers, information on paper or other analog data carriers must also be taken into account in the security concept. This concerns for example printouts and copies as well as the use of fax services. Further information can be found in the blocks SYS.4.1 Printer, Copier and Multifunction Devices and NET.4.3 Fax Machine.

These implementation notes show on the one hand how the information stored on mobile data carriers can be used safely and how on the other hand how an unauthorized disclosure of information via mobile data carriers should be prevented.

### 1.2 Life cycle

For the safe handling of mobile data carriers, a number of measures have to be implemented, beginning with the planning and conception to the procurement up to the emergency preparedness. The steps that should be taken and the actions that should be followed in each step are listed below.

** planning and conception **

A concept for the safe handling of mobile data media should be developed, which identifies risks and security measures for the various types of mobile data carriers (see SYS.3.4.M4 Creation of a guideline for the safe handling of mobile data carriers).

** procurement **

The selection of suitable data media must be agreed. In addition, OPS.1.2.2 archiving can be taken into account when deciding which types of data carriers to use.

**Business**

Based on the respective safety requirements, safety instructions for all employees should be created on the basis of application scenarios (see SYS.3.4.M1 Raising employee awareness on the safe handling of mobile data carriers). In addition, the drives and interfaces of the IT systems must be protected according to the security specifications (see SYS.3.4.M8 Hedging drives and interfaces for removable media and external data storage).

** ** segregation
If any disk is shared, it should be physically erased before it is re-used or discarded so that no sensitive information falls into the wrong hands (see SYS.3.4.M7 Physical Disk Erase Before and After Use).

** Emergency Preparedness **

Important information stored on portable media should still be stored elsewhere to prevent loss (see SYS.3.4.M3 Backup of Submitted Data).

2 measures
-----------

The following are specific implementation notes in the "Mobile Media" section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### SYS.3.4.M1 Raising employee awareness about the safe handling of mobile data carriers

Public authorities and companies today use a wide variety of mobile data carriers. Similarly, the number of devices that can be used in addition to their actual function in addition as a mobile data carrier. This increases the number of possible distribution channels for information as well as the number of possible security gaps. Although some of these security risks can be minimized technically, without the involvement of employees in the safe and proper handling of mobile data carriers authorities or companies are repeatedly overrun by technical innovations.

All employees must be informed about the types and applications of mobile data carriers. This also includes informing them about the different types and variants, so that, for example, a smartphone is also a mobile data carrier. In addition, employees should be informed about potential risks and problems of use, as well as the benefits, but also the limits, of the security measures used. Employees are also required to be regularly informed about new dangers and aspects of mobile data carriers, such as: Eg via corresponding articles on the intranet or in the employee magazine.

Users should be advised of how to handle the mobile media carefully to prevent loss or theft or to ensure a long service life. For example, questions about storage outside of the office or home, and sensitivity to high or low temperatures should be addressed. Damage or losses must be reported promptly (see SYS.3.4.M2 loss notification of mobile data carriers).

Other aspects that users should be aware of are:

* which data may be stored on mobile data carriers and which not,
* how the data stored on these mobile data carriers are protected against unauthorized access, manipulation and loss,
* How to securely erase data on mobile media and how to dispose of media.
#### SYS.3.4.M2 Mobile Media Loss Report [User]

Loss or theft of an official mobile data carrier must be reported immediately. This also applies to private data media that are used for official purposes. For this, there must be clear reporting channels and contact persons in each institution.

Failures or failures should also be reported, even on low-priced mobile disks, so that IT management can see if larger shipments are affected. Particularly for data carriers used for data backup and archiving, high reliability and a long service life are important. If an employee loses a mobile disk or is stolen, action must be taken quickly, since this is not just about recovering the device, but also about preventing potential misuse of the information involved.
If lost media reappear, it is strongly recommended that you investigate it for possible tampering, such as: For example, if screws have been opened, seals removed, or if the weight has changed from the delivery condition. If there is a suspicion, the device should either be disposed of immediately or further examined by a specialist. To ensure that there are no malicious programs or malware on the recovered media, the SYS.3.4.M7 Physical Disk Erase request should be implemented before and after use.

If data carriers are to be disposed of, it should first be ensured that the residual information stored on the data carriers can not fall into the wrong hands. For this purpose, it should be safely deleted (SYS.3.4.M7 Physical deletion of the data carrier before and after use), generally the requirements of the module OPS.1.2.7 sale / disposition of IT should be implemented.

#### SYS.3.4.M3 Backup copy of submitted data [user]

If the data to be transmitted has been created or compiled solely for the purpose of data transmission and is not stored on another medium, a back-up copy of this data must be provided. If the mobile data medium is lost or damaged, the data will not be lost.

Together with the basic measures, the following measures correspond to the state of the art in the field of "mobile data carriers".

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "mobile data carriers".

#### SYS.3.4.M4 Creation of a policy for the safe handling of mobile data carriers [User]

Depending on the technical design, a large amount of data can be exchanged at high throughput rates via mobile data carriers. The variants of mobile data carriers are now diverse. Also, they are not always recognizable as such at first sight. For example, there are wristwatches or key fobs with integrated data memory. The usual size of this disk starts here with a few hundred megabytes and can certainly reach up to several terabytes.

Therefore, some basic aspects should be considered when dealing with portable media. It is to be clarified,

* which mobile data carriers are to be used in the institution,
* which are actually used and who uses them
* which data may be stored on mobile data carriers and which not,
* how the data stored on these mobile data carriers are protected against unauthorized access, manipulation and loss,
* with which external employees or service providers mobile data carriers may be exchanged and which safety regulations must be observed (see OPS.1.2.3 Data medium exchange),
* how to prevent mobile media from being used to pass on unauthorized information,
* how to prevent the spread of malware via the mobile data carrier.
It should also be clarified whether employees are allowed to use their private mobile storage devices within the institution, and vice versa, whether employees may store or use private data on official mobile data carriers. It should also be clarified whether the mobile data carriers brought in by external parties may be used within the institution, for example to exchange files.

The more restrictive the security requirements are for the handling of mobile data carriers, the higher are also the limitations in the daily work routine. Therefore, all security requirements should be weighed to determine whether they are appropriate.
The variety and variants of data carriers will continue to increase. Mobile disks are becoming increasingly "invisible" as they integrate with other devices. It should be checked regularly whether the security requirements for the handling of mobile data media are still current, starting with whether all variants of currently used data media are still covered.

Mobile data carriers can easily be lost or stolen while traveling. Therefore, depending on protection needs to consider whether the information stored on it should be encrypted. For this purpose, products should be used that automatically encrypt all data that users store on mobile data carriers. For more information, see SYS.3.4.M10 Disk Encryption.

The procedure defined by the institution should be documented and prepared in a security policy for the employees.

#### SYS.3.4.M5 Control of the transport of mobile data carriers

The IT components used within an in-house property are generally adequately protected against misuse and theft by infrastructural security measures. However, mobile data carriers are often used outside the home, e.g. B. on business trips. In order to be able to adequately protect these, the transport of such data carriers must be clearly regulated.

It should be specified

* which mobile data media may be taken outside the home,
* who is allowed to take mobile data media out of the house and
* which basic security measures must be observed (virus protection, encryption of sensitive data, storage, etc.).
The type and extent of security measures to be applied to externally deployed media depends, on the one hand, on the protection requirements of the IT applications and data stored on them and, on the other hand, on the security of the storage or storage locations.

In principle, employees should obtain the appropriate authorization for all mobile data carriers they wish to use externally. In particular outside of the institution's own real estate, users should ensure the protection of the data carriers entrusted to them. These and the precautions to be taken are to be noted. These include the following rules:

* Mobile data carriers must always be stored safely. On business trips they should not be left unattended.
* Mobile data carriers that contain sensitive data should be encrypted as completely as possible (SYS.3.4.M10 volume encryption). If such media allows encryption without any additional resources, it is recommended that you use these features even if less sensitive data is included on the media.
* The management, maintenance and transfer of externally used mobile data storage devices should be regulated. For example, pools can be set up for this purpose.
* It should be noted when and by whom disc was used outside the home.
#### SYS.3.4.M6 Disk Management [Specialists]

The task of the disk management as part of the resource management is to be able to guarantee the access to mobile data carriers to the required extent and within a reasonable time. This requires a regular management of the data carriers, which requires uniform labeling and inventory management. Furthermore, in the context of data carrier management, the proper handling and storage of the data carriers, their proper use and transport and, last but not least, the deletion or destruction of the data carriers must be ensured.

** Inventories ** provide fast and targeted access to mobile media. For example, they provide information about the storage location, retention period and authorized recipients.
The external ** identification ** of mobile data carriers enables their rapid identification. However, the labeling should not allow unauthorized persons to infer the content (eg the inscription of a USB stick with the keyword "confidential") in order to make it more difficult to misuse. It should be noted, however, that flanking regulations and requirements that apply to the institution require a corresponding labeling. In this case, additional requirements from these regulations and requirements usually have to be implemented. A defined structure of identification features (eg date, filing structure, serial number) facilitates the assignment to stock records.

For ** proper handling ** of mobile data carriers, the manufacturer's instructions, which can usually be found on the packaging, are to be used. With regard to the storage of data storage devices on the one hand measures for storage (magnetic field and dust-proof, climate-friendly) and on the other hand measures to prevent unauthorized access (suitable containers, cabinets, rooms) to make.

The ** shipping or transport ** of mobile data media must be made in such a way that they can not be damaged if possible (eg magnetic tape mailing bag, air-cushioned envelopes). The packaging of the data carrier must be aligned with its need for protection (eg by means of lockable transport containers). Shipment or transport methods (eg courier transport) must be defined in the same way as the proof of delivery procedure (eg accompanying note, dispatch notes) and receipt at the consignee (eg acknowledgment of receipt). The data carrier must not contain any "residual data" beyond the data to be sent. This can be achieved by physical deletion.

It should also be noted that a backup copy is made before important data carriers are delivered. Further information on the shipping and transport of data media is contained in the module OPS.1.2.3 Data medium exchange.

For the internal transfer of data carriers, regulations can be made such as acknowledgment procedures, pick-up / take-along authorizations and the keeping of inventories of the whereabouts of data carriers.

In the event that ** data carriers received from third parties ** are used, regulations must be made regarding their treatment before use. If, for example, digital data are transmitted, a computer virus check of the mobile data carrier or data records should generally take place. This also applies accordingly before the first use of new digital data carriers. It is recommended to check for computer viruses not only when receiving but also before sending digital media.

A regulated procedure for the deletion or destruction of data carriers prevents the misuse of the stored data. Before reusing mobile data carriers, the data stored on them must be securely deleted (see OPS.1.1.8 Deleting and destroying data).

#### SYS.3.4.M7 Secure Disk Erase Before and After Use [Specialist]

In addition to the information contained in the module OPS.1.1.8 Deleting and destroying data for the deletion or destruction of data carriers, the following points should be noted for data medium exchange:

* A physical deletion sufficient for the normal protection requirement can be achieved by overwriting the entire data medium or at least the areas used with a specific pattern. It is also possible to format the data carrier if it can not be undone. It should be avoided to delete only individual files, this often remains residual information obtained, which allow the reconstruction of the deleted files.
* Magnetic media intended for replacement should be physically erased before writing to the information to be transmitted. This is to ensure that no residual data is passed on to unauthorized recipients.
* As a rule, the transmitted data is also worth protecting for the recipient. Analogously, a physical deletion of the data carrier is also provided here after the data is re-imported.
* For the purpose of data exchange, the use of non-erasable data media is to be waived if there are further information not intended for the recipient which can not be deleted.
#### SYS.3.4.M8 Securing drives and interfaces for removable media and external data storage

Commercially available PCs today are usually equipped with a CD / DVD burner. In addition, it is possible to connect external storage media via interfaces, which are automatically recognized and integrated by most operating systems. Examples include USB storage connected to the USB port and Firewire hard drives. In addition, card readers for memory cards are installed in many IT systems. Such removable media and external storage drives pose the following potential security issues:

* The IT system could be booted uncontrollably from such drives.
* Uncontrolled software could be imported from such drives.
* Data could be copied unauthorized to removable media.
When booting from removable media or installing third-party software, not only can security settings be bypassed, but the IT system can also become infected with malicious programs. Those responsible should counteract these dangers by means of appropriate organizational or technical security measures. For this purpose, various approaches are available whose specific advantages and disadvantages are briefly described below:

* Removal of drives
 Although the removal of drives for removable media (or the lack of procurement) provides the safest protection against the above-mentioned threats, but is usually associated with considerable effort. Often, a removal is not possible at all, eg. B. with memory card readers in notebooks. It should also be considered that IT systems may be difficult to administer and maintain when these drives have been upgraded. This solution should be considered if special security requirements exist.
* Locking drives
 For some types of drives, there are lockable plug-in devices that can help prevent uncontrolled use. Procurement should ensure that the drive locks are suitable for the existing drives and can not damage them. It should be noted that locks are not offered for all types of drives, such as built-in memory card readers. It should also be ensured that the locks are offered by the manufacturer with a sufficient number of different keys. The disadvantage is the procurement costs for the drive locks and the cost of the required key management. Therefore, this solution makes sense only with higher protection requirements or special security requirements.
* Deactivation in the BIOS or operating system
In the BIOS, most PCs provide options for booting from which drives. In conjunction with password protection of the BIOS settings, this can prevent the uncontrolled booting of removable media and mobile data carriers. Furthermore, the existing drives and interfaces in modern operating systems can be disabled individually. This complicates the unauthorized use, eg. For example, installing third-party software or copying to removable media. The deactivation of the drives in the BIOS or operating system has the advantage that no hardware changes are required. The corresponding settings in the operating system can be made centrally if necessary. For this procedure to be effective, it must be ensured that users do not have the permissions in the operating system to re-enable the drives.
* Control of interface usage
 The use of interfaces should be regulated by appropriate rights at the level of the operating system or with the help of additional programs. Some of these add-on programs to secure the USB or Firewire interfaces can be set to read only from portable media. Alternatively it can be monitored if devices are added.
* Encryption
 There are products that ensure that only access to authorized mobile data carriers is possible. One solution, for example, is that only mobile data carriers that have been encrypted with certain cryptographic keys can be read and written. This not only protects against unauthorized access via manipulated mobile data carriers, but also protects the data on the mobile data carriers in the event of loss or theft.
* Guidelines for use
 In many cases, users may use the built-in drives for removable media or storage media on external interfaces, but use is governed by appropriate policies. On a technical level, only booting removable media should be disabled in the BIOS. Removing, locking or disabling the drives in the operating system is out of the question. In this case, the guidelines for using the drives and storage media should be defined as explicitly as possible. For example, a general ban may be imposed, only the copying of public text documents is allowed. The policies must be made known to all users and compliance monitored. The installation and launching of programs that have been recorded by removable media should be prohibited and as far as possible prevented technically. This purely organizational solution should only be selected if the users have to access the drives every now and then or regularly. Otherwise, the access should, as described above, be prevented by technical measures. When choosing a suitable approach must always be considered all connectivity options for mobile devices, but also all ways to exchange data via networking, so in particular e-mail and Internet bindings. If the IT system is connected to the Internet, it is not enough to disable or extend all removable media drives.
Regardless of which approach the institution chooses, it is important to prevent content from mobile media from being automatically executed when connected. To do this, deactivate the corresponding autorun and autoplay functions of the operating system.

In order for safety measures to be accepted and observed, users must be informed and sensitized about the hazard.

### 2.3 Measures for increased protection requirements
The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### SYS.3.4.M9 Control and monitoring of interfaces (CI)

Via the interfaces of an IT system, many additional devices can be connected to PCs, for example hard disks or memory sticks. USB memory sticks consist of a USB plug and a memory chip. Despite their large storage capacity, they are so handy that they can be produced, for example, in the form of key rings and fit into any pocket. In today's operating systems, the mass storage drivers are already integrated, eliminating the need for software installation for operation. However, this measure does not only apply to USB storage devices, but generally to all devices that can store data. Among other things, USB printers and USB cameras can be "misused" to store the data. This is especially true for "smart" USB devices, such as MP3 players, which can accept any USB identity if they are equipped with special software. Not only via the USB interface, data carriers can be connected, but also via numerous other interfaces, such as Firewire or PCMCIA.

Storage media can be used to uncheck information and programs. Therefore, they are generally the same as dealing with conventional storage media. Access to DVD drives is relatively easy to prevent (see SYS.3.4.M8 Hedging drives and interfaces for removable media and external data storage). The operation of storage media, however, can be very difficult to prevent when the interfaces are used for other devices, eg. For example, the USB interface for the printer or the mouse. Therefore, it usually does not make sense to use a "USB lock" or disable the interface by other mechanical measures. The use of interfaces should therefore be regulated by granting appropriate rights at the level of the operating system or with the help of additional programs. Alternatively it can be monitored if devices are added. When data memories are connected to external interfaces, the operating system often loads drivers or kernel modules or creates entries in configuration files (such as the Windows Registry) that can be detected. After the changes have been detected, for example, a log file can be created or an administrator can be notified. However, all this can only be achieved with the help of additional software. This requires either a proprietary development or a third-party product.

#### SYS.3.4.M10 Disk Encryption (C)

Confidential information can be encrypted in various ways and thus protected against unauthorized access. For example, the entire volume, a single partition or just a single file can be encrypted. From a security point of view, it is better to encrypt the entire data carrier, since then less user intervention is required and all data is protected against unauthorized access. If only individual files or file containers are encrypted, there is a risk of inadvertently removing sensitive data in unencrypted areas of the hard disk. In addition, the user must explicitly start an encryption program for this purpose.
Disk encryption can be implemented with software, but also with hardware support. Software solutions are z. For example, BitLocker from Microsoft or the open source program VeraCrypt. Mobile data carriers, such as USB sticks, should always be completely encrypted whenever possible, even if they are occasionally used for confidential information.

The key feature of an encryption method is the quality of the algorithm and the key selection. A recognized algorithm that is sufficient for normal protection needs is the Triple DES based on the Data Encryption Standard (DES). This is easy to program, especially since the source code is printed in many textbooks in the C programming language. Another recognized algorithm is the Advanced Encryption Standard (AES).

The cryptographic keys should be generated securely and stored separately from the encrypted mobile data carrier (see CON.1 crypto concept). For this example, smart cards or USB tokens can be used. Such a separation is usually not possible with the encryption of USB sticks, which should be taken into account in the security analysis.

In order to meet the confidentiality requirements of the information to be transmitted, the sender's and recipient's IT systems should sufficiently ensure access protection to the encryption program. If necessary, this program should be stored on a removable medium, kept locked and only be imported and used if necessary.

Used passwords must meet the requirements for length and characters to be used.

#### SYS.3.4.M11 Integrity Protection by Checksums or Digital Signatures (I)

If only the integrity of the data to be transmitted is to be ensured for the exchange of data, a distinction must be made as to whether protection should be provided only against accidental changes, such as: B. by transmission errors, or against manipulation to be made. If only random changes are to be detected, checksum methods (eg Cyclic Redundancy Checks) or error-correcting codes can be used. In addition, protection against manipulation is provided by methods which generate a so-called Message Authentication Code (MAC) from the information to be transmitted by means of a symmetric encryption algorithm (eg triple DES). Other methods use an asymmetric encryption algorithm (eg RSA) in combination with a hash function and generate a "digital signature". The respective generated "fingerprints" (checksum, error-correcting codes, MAC, digital signature) are transmitted via an independent transport path with the information to the receiver and can be checked by the latter.

3 Further information
------------------------------

### 3.1 Worth knowing

Many mobile data carriers have directly integrated protection mechanisms. These should always be used to protect data from unauthorized access. Mobile data carriers, such as USB sticks with integrated hardware encryption, generally offer a much higher level of protection than those that only provide access protection without encrypting the data themselves. In all procedures, care should be taken to prevent a misoperation counter from systematically testing the password, PIN or finger. In a mobile data carrier with fingerprint sensor should also be careful to use other possible parts of the finger instead of the fingertips to discourage attacks by cloning fingerprints.

### 3.2 Literature

Further information on hazards and security measures in the area of ​​"Mobile data carriers" can be found in the following publications, among others:

* #### [CS008] BSI-CS 008
Protection of data on USB sticks, Version 1.00, 05.2012
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_008.html](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_008.html)
