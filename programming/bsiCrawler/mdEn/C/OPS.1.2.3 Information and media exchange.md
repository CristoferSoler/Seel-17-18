1 description
--------------

### 1.1 Introduction

In this module, the secure exchange of information is considered, with the focus on digital and analog media as transport media, but also the exchange of information in personal meetings or via IT networks. Even with a broadband network connection, it may be useful or necessary to transmit data carriers for the exchange of information. One reason may be that there is no or no sufficiently trusted connectivity between the affected IT systems. Data carriers can be exchanged during personal meetings or via shipping.

### 1.2 Objective

The aim of this module is to secure the exchange of information between different communication partners and IT systems. In particular, what is to be considered during data medium exchange in order to adequately protect the transported data is shown.

### 1.3 Delimitation

This module is always to be used if there is an exchange of information with offices outside of one's own institution or property and the internal network is not used. He is especially to be applied when

* new transport routes are built up (new communication partners, new media, new networks),
* the exchange of information with the help of data carriers takes place. In addition to the transmission, the storage and handling of the data carriers must be taken into consideration.
The protection of network connections is covered in other components of the IT-Grundschutz Compendium. Further processing in the target IT system is not considered. In this module, the basic rules for a secure exchange of information are in the foreground, especially in the use of mobile data carriers. The reasons why there is no or no sufficiently trusted network between the affected IT systems are not considered.

In addition, this module also takes into account the storage of the data on the sender and receiver system, insofar as it is directly related to the data medium exchange, as well as the handling of the data carriers before or after the transfer. This module considers mobile data carriers such. As removable disks, optical media, USB sticks and hard drives and not to forget paper documents.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance for the exchange of information and data carriers:

### 2 1 Defective media

All types of media can cause damage, errors, or failures. They become a problem when the information stored on the data carriers is not stored elsewhere and can not be reconstructed quickly and easily.

** Impermissible temperature and humidity **

Extreme temperatures and humidity can affect the proper operation of media. For each type of data carriers there are defined limits, within which the proper function is guaranteed. If these are exceeded or exceeded, this can lead to malfunctions and device failures. With digital storage media, excessive temperature fluctuations or excessive humidity can lead to data errors.

** improperly packaged media **

During transport or shipping, data carriers are subject to special loads. For data carriers, even minor contamination can lead to data errors. Hard disks can be destroyed by the "head crash" of the read / write head, tapes or cassettes by direct mechanical action. CD-ROMs or DVDs may become unusable due to scratching of the surface.

** Data loss due to strong magnetic fields **
Typical disks with magnetizable storage media are removable disks, cassettes and tapes. These data carriers are sensitive to magnetic interference, so the proximity to such radiation sources should be avoided.

### 2 2 Not available on time

In the case of data medium exchange, it is of particular importance in many business processes that they can reach their recipient on time or be used there in a timely manner. Even small errors in labeling can cause a disk does not reach its destination in the required time. If the required interfaces or resources are not available on site, a data carrier may not be able to be read out. The resulting delays can lead to significant damage.

### 2 3 Unregulated transfer of information or data media

In the event of an unregulated transfer or disorderly delivery of information or data carriers, there is a risk that confidential information may get into unauthorized hands or fail to reach the desired destination in time.

### 2 4 Inadequate key management with encryption

If encryption systems are used to protect the confidentiality of data to be transmitted, the desired protection can be undermined due to inadequate key management, for example if easily guessable keys have been selected or if the cryptographic keys used for encryption or decryption do not reach the communication partner in a secure way , The simplest negative example is the sending of the encrypted information and the key used on or with the same data medium. In this case, anyone who gains possession of the disk can decrypt the information, provided that the encryption method is known.

### 2 5 Loss of storage media

If data carriers are shipped in containers that are not particularly stable (envelopes or other packaging), there is a risk that the data carriers will be lost if the packaging is damaged. There is also the risk of loss to the recipient, by post or by carelessness of a messenger. Data carriers are becoming smaller and smaller so that they can be lost more easily during transport.

In addition, if the information on the media is not encrypted, they may fall into the wrong hands if lost.

### 2 6 Passing on false or internal information

When passing on information, it often happens that other information is transmitted in addition to the desired information. As a result, confidential information or information that is not suitable for publication keeps falling into the wrong hands. Thus, it happens that data carriers are passed on without the previously stored data being deleted in an appropriate manner. Similarly, confidential documents may be inadvertently mailed to the wrong recipient, or letters may be printed out and sent with internal comments.

### 2 7 Theft, tampering or destruction of data media

Outsiders, but also inner perpetrators, can try for various reasons (spying, revenge, malice, frustration) to steal, manipulate or destroy data carriers. The manipulations range from the unauthorized access to sensitive data about content modification of data to the destruction of data carriers.

### 2 8 Malicious programs in transferred files or on data carriers
If the work environment is insufficiently secured against malicious programs, malicious programs could be located on data media that are forwarded to external users. This could destroy or corrupt the stored data, but above all IT systems at the receiving end could be compromised. But the loss of image and the financial damage caused by malicious programs are also of great importance.

### 2 9 Unauthorized copying of information or data media

If information or data carriers are exchanged or transported via an insecure transport route, there is a risk that the information transmitted may be copied by unauthorized persons during transport. Likewise, attackers could try to intercept communications over IT networks.

3 requirements
---------------

The following are specific requirements for information and media protection protection. Basically, the Information Security Officer (ISB) is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]

The institution MUST specify which communication partners may receive and share which information. This MUST be communicated to all purposes in the institution. Before exchanging information it MUST be clarified that the recipient has the necessary permissions to receive and process the information.

#### OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]

If information is exchanged, it MUST be clarified in advance how vulnerable the relevant information is, with whom the information may be exchanged and how it should be specifically protected. The employees MUST be sufficiently sensitized. Recipients MUST be advised that the data transmitted may only be used for the purpose for which they were disclosed.

#### OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]

Staff MUST be informed about the framework conditions for the exchange of information. It MUST know what information they are allowed to give when, where and how.

#### OPS.1.2.3.A4 Malware Protection [User]

Digital data MUST be checked by both the sender and the recipient for malware. The anti-virus programs used must comply with the current state of the art.

#### OPS.1.2.3.A5 loss report [user]

It MUST be reported immediately if a data carrier is lost, stolen, or suspected of being tampered with during media exchange. For this there must be clear reporting channels and contact persons in each institution.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of information and data medium exchange. They SHOULD be implemented in principle.

#### OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]

In a regular exchange of information with external partners, the framework should be formally agreed.

#### OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]

The proper data medium exchange SHOULD be regulated. It SHOULD be determined how the data carriers are to be protected in their own institution, during transport and at the recipient. When choosing the shipping method, the type of data carriers and the protection requirements of the information SHOULD be taken into account. It also SHOULD specify when and how disks are physically deleted.
#### OPS.1.2.3.A8 Physical deletion of media before and after use [user]

Before and after a data medium exchange, previously used data carriers SHOULD be physically deleted. The employees SHOULD be provided with suitable programs for physical deletion.

#### OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]

Users SHOULD be informed about the risks of residual and additional information in files. The users SHOULD be taught how to avoid residual and additional information in files. Remaining information SHOULD be removed accordingly. Before passing on files, random checks of the files should be performed for any residual information contained.

#### OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]

External parties SHOULD make confidentiality agreements before gaining access to and access to confidential information. The confidentiality agreements used SHOULD take into account all important aspects of the protection of confidential information.

#### OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]

Before exchanging information, the systems and products used on the transmitter and receiver side SHOULD be checked for compatibility.

#### OPS.1.2.3.A12 Appropriate marking of the data carrier during shipping [User]

When tagging media, SHOULD ensure that sender and recipient are immediately identifiable. The marking of the data carriers or their packaging SHOULD make the contents of the data carriers clearly identifiable to the recipient. The labeling of data carriers with information worth protecting SHOULD NOT allow any conclusions as to the nature and content of the information.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)

Confidential information SHOULD be encrypted before exchanging information. Information with a high integrity claim SHOULD be digitally signed. For this purpose, suitable crypto-proxy methods should be selected which meet the protection requirements and can be used without problems on the sender and receiver side. ** ** A suitable key management SHOULD be established for the use of cryptographic methods.

#### OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)

For higher protection, a disk management SHOULD be set up to regulate access to disks, their marking and proper storage. All types of media should be handled properly, including storage, distribution, transportation and deletion. It SHOULD create an inventory. The data carriers SHOULD be handled properly according to the manufacturer's instructions.

#### OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)

If information is subject to increased protection requirements, SHOULD investigate how it can be adequately protected during a data medium exchange. SHOULD use secure shipping packaging for media that identifies tampering with changes to the packaging. The consignor SHOULD inform the post office about the necessary shipping and packaging types. Basically, the data SHOULD be encrypted.
#### OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)

Described data carriers SHOULD be stored so that only authorized users can access them. All employees involved SHOULD be made aware of the proper and safe storage and handling of data carriers.

#### OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)

SHOULD BE CHECKED BEFORE SENDING MEDIA,

* whether the requested information is completely contained and
* if there is no additional information that should not be disclosed.
#### OPS.1.2.3.A18 Backup copy of submitted data [user] (A)

If the data to be transmitted has been created or compiled solely for the purpose of data transmission and is not stored on another medium, a backup copy of this data SHOULD be provided. In case of loss or damage of the data during the transport, the shipment can be made again with little effort.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and security measures in the area of ​​"information and data medium exchange" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [NIST800150] Guide to Cyber ​​Threat Information Sharing

  

 Special Publication 800-150, National Institute of Standards and Technology (NIST), 10-2016
 <Http://dx.doi.org/10.6028/NIST.SP.800-150>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "Information and data medium exchange".

* G 0.2 Unfavorable climatic conditions
* G 0.4 Pollution, dust, corrosion
* G 0.14 Spying out information (spying)
* G 0.16 Theft of devices, data carriers or documents
* G 0.17 Loss of equipment, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.22 Manipulation of information
* G 0.24 Destruction of equipment or data media
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.29 Violation of laws or regulations
* G 0.38 Abuse of personal data
* G 0.39 Malware
* G 0.42 Social engineering
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.14 Spying out information (spying)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.16 Theft of devices, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.20 Information or products from unreliable sources
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
* G 0.22 Manipulation of information
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
* G 0.24 Destruction of equipment or data media
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.25 Failure of devices or systems
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
* G 0.38 Abuse of personal data
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A6 Agreements to exchange information with external [Head of Organization]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A8 Physical deletion of media before and after use [user]
  * OPS.1.2.3.A9 Eliminate Remaining Information in Files Before Redistributing [User]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
* G 0.39 Malware
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
* G 0.42 Social engineering
  * OPS.1.2.3.A1 Definition of permitted communication partners [Head of Organization]
  * OPS.1.2.3.A10 Conclusion of Confidentiality Agreements [Head of Organization]
  * OPS.1.2.3.A11 Compatibility check of the sender and receiver system [IT operation]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A15 Safe shipping method and packaging [Post Office, User] (C)
  * OPS.1.2.3.A16 Secure Storage of Media Before and After Shipping [User, Post Office] (CIA)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
  * OPS.1.2.3.A2 Regulation of Information Exchange [Head of Organization]
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
* G 0.45 data loss
  * OPS.1.2.3.A3 Instructing staff to exchange information [Specialists]
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A5 loss report [user]
  * OPS.1.2.3.A7 Control of data medium exchange [Head of Organization]
  * OPS.1.2.3.A12 Appropriate marking of data carriers during shipping [user]
  * OPS.1.2.3.A14 Disk Management [Head of Organization, IT Operations] (CIA)
  * OPS.1.2.3.A18 Backup copy of submitted data [user] (A)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.3.A4 Malware Protection [User]
  * OPS.1.2.3.A13 Encryption and Digital Signatures [User] (CI)
  * OPS.1.2.3.A17 Verifying Media Before Shipping [User] (CI)
