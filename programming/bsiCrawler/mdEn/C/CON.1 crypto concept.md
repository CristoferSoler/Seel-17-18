1 description
--------------

### 1.1 Introduction

The procedure described in this module provides an overview of cryptographic procedures and products that can be used in an institution. It describes how, in a heterogeneous environment, both the locally stored data and the data to be transmitted can be effectively protected by cryptographic techniques and techniques. It also describes appropriate organizational and procedural requirements to ensure confidentiality, integrity and authenticity.

In addition to the procedures and techniques that can be used to protect locally stored data and transmitted information, this module also describes crypto modules. A crypto module is a product that provides the security functionality set forth in the crypto concept. Such a product may consist of hardware, software, firmware or a combination thereof. In addition, components such as memory, processors, buses and power supply are necessary to implement the crypto processes. A crypto module can be used in a variety of computer or telecommunication systems to protect sensitive data or information. This is relevant in the present module only with increased protection requirements.

### 1.2 Objective

The module describes how information in institutions is cryptographically secured and how a corresponding crypto concept should be created for this purpose.

### 1.3 Delimitation

This module considers general requirements, organizational framework conditions and procedural processes for cryptographic products and processes. The core IT tasks related to the operation of crypto modules are not covered in this module. For this, the requirements of the components of the layer OPS.1.1 * core IT operation * must be fulfilled.

How individual applications (eg e-mails) or IT systems (eg laptops) can be cryptographically secured is not the subject of the present module, but is dealt with in the respective modules.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the crypto-concept area:

### 2 1 Inadequate key management with encryption

Inadequate key management could allow attackers to access encrypted data. It may be, for example, that due to lack of regulations encrypted information, including the associated keys are on the same disk. As a result, in symmetric methods, anyone who can access the data medium or the communication channel can decrypt the information if the encryption method used is known.

### 2 2 Infringement of the legal framework for the use of cryptographic procedures

When institutions use cryptographic procedures and products, they must observe various legal framework conditions. For example, in some countries, cryptographic procedures may not be used without government approval. This may result in receivers abroad being unable to read encrypted records because they are not allowed to use the required cryptographic products or may even be liable to prosecution.

In addition, exports of products with strong cryptography are also severely limited in many countries. This can lead one to leave sensitive data unencrypted or to protect it with insecure procedures. As a result, on the one hand attackers are opened the door and on the other hand, this can also violate national law. For example, privacy laws may require that adequate cryptographic procedures be used to protect personal information.
### 2 3 Confidentiality or integrity of data due to misconduct

For example, if an institution uses a crypto-module that is either too complicated to use or not intuitive to use, users may, for convenience or pragmatic reasons, refrain from using it and instead transmit the information in plain text. This allows the transmitted information to be intercepted by attackers.

Also, a misuse of a crypto module can cause confidential information to be tapped by attackers, such as when they are transmitted in plain text, because inadvertently the plain text mode has been activated.

### 2 4 Software vulnerabilities or errors in crypto modules

Software vulnerabilities or errors in crypto modules weaken the security of the cryptographic processes used and can lead to the fact that the protected information is read. This makes it possible for attackers to manipulate the crypto modules (eg via malicious software), thus allowing sensitive data to flow away or even entire production processes to stand still because data can no longer be decrypted.

### 2 5 Failure of a crypto module

Crypto modules can fail due to technical defects, power failures or deliberate destruction. As a result, already encrypted data could no longer be decrypted, as long as the required crypto module is no longer available. As a result, entire process chains can stand still, eg. For example, when other IT applications rely on the data.

### 2 6 Unsafe cryptographic algorithms or products

Unsafe or obsolete cryptographic algorithms can be broken by a potential attacker with reasonable resources. For encryption algorithms, this means that it is possible to determine the original plaintext from the encrypted text, without additional information, such. As the cryptographic key used are known. If insecure cryptographic algorithms are used, attackers can circumvent the cryptographic protection and thus access sensitive information of the institution.

Even if only secure (eg certified) products are used in an institution, communication can still be unsafe, for example if the communication partner uses non-state-of-the-art cryptographic techniques.

### 2 7 Errors in encrypted data or cryptographic keys

If information is encrypted and the cipher rate is changed, the encrypted information may no longer be decrypted correctly. Depending on the operating mode of the encryption routines, this can mean that only a few bytes are incorrectly decrypted or even all data is incorrectly decrypted. If there is no backup, such data is lost.

Even more critical can be an error in the cryptographic keys used. Even the change of a single bit of a cryptographic key means that all encrypted data can no longer be decrypted.

### 2 8 Unauthorized use of a crypto module

If an attacker succeeds in using a crypto module unauthorized, he can manipulate critical security parameters. As a result, the cryptographic methods no longer provide sufficient security. Furthermore, an attacker can manipulate the crypto module to work correctly at first glance, but in fact be in an unsafe state. As a result, it remains undetected for a long time and can access numerous sensitive information.

### 2 9 Cryptographic key compromise
The security of cryptographic procedures depends crucially on how confidential the cryptographic keys used remain. Therefore, a potential attacker will usually try to identify the keys used. For example, he could do this by reading out volatile memory or finding unprotected keys, which are stored in a data backup, for example. If he knows the key used and the crypto method used, he can decrypt the data relatively easily.

In a hard disk encryption (such as Trusted Disk), an attacker z. For example, you can use a keylogger between the keyboard and the computer to get to the password needed to decrypt the hard disk.

### 2 10 Fake certificates

Certificates serve to bind a public cryptographic key to a person. This binding of the key to the name of the person is in turn cryptographically secured by means of a digital signature often from a trusted third party.

These certificates are then used by third parties to check the digital signatures of the person named in the certificate or to send this person encrypted data with the key recorded in the certificate.

If such a certificate is forged, digital signatures are incorrectly verified as correct and associated with the person in the certificate, or data is encrypted and sent with a potentially insecure key.

3 requirements
---------------

The following are specific requirements for crypto concepts. Basically, the Information Security Officer (ISB) is responsible for meeting the requirements. He is also responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### CON.1.A1 Selection of suitable cryptographic procedures [specialist responsible]

Suitable cryptographic methods MUST be selected. It MUST be ensured that established algorithms are used, which have been extensively studied by experts and of which no security vulnerabilities are known. Likewise, currently recommended key lengths MUST be used.

#### CON.1.A2 Data backup using cryptographic procedures [IT operation]

In backups, cryptographic keys MUST be stored in such a way that they can not be accessed by unauthorized persons. Long-lived cryptographic keys MUST be kept outside the IT systems used. In the case of long-term storage of encrypted data, it should be regularly checked whether the cryptographic algorithms used and the key lengths still correspond to the state of the art. It MUST be ensured that encrypted stored data can still be accessed even after longer periods of time. Used crypto products SHOULD be archived. The configuration data of crypto products SHOULD be saved.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of crypto concepts. They SHOULD be implemented in principle.

#### CON.1.A3 Encryption of the communication connections

It SHOULD be checked whether with reasonable effort an encryption of the communication connections is possible and practicable. If this is the case, communication links SHOULD be suitably encrypted.

#### CON.1.A4 Appropriate key management [IT operation, specialist responsible]
Cryptographic keys SHOULD always be generated using appropriate key generators and in a secure environment. A key SHOULD serve as one purpose only. In particular, different keys SHOULD be used for encryption and signature formation.

When keys are used, the authentic source and integrity of the key data SHOULD be checked.

All cryptographic keys SHOULD be changed sufficiently frequently. It SHOULD provide a set course of action in case a key was revealed. All generated cryptographic keys SHOULD be securely stored and managed.

#### CON.1.A5 Secure deletion and destruction of cryptographic keys [IT operation]

Keys and certificates no longer needed SHOULD be safely deleted or destroyed. Products with uncontrollable key deposit SHOULD generally be dispensed with.

#### CON.1.A6 Needs Assessment for Cryptographic Procedures and Products [IT Operations, Specialists]

It SHOULD be determined for which tasks cryptographic procedures should be used. After that, the applications, IT systems and communication links that are necessary to complete the tasks SHOULD be identified. These SHOULD be cryptographically secured.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### CON.1.A7 Creating a Security Policy for the Use of Cryptographic Procedures and Products (CIA)

Based on the institution's general security policy, a specific policy for the use of crypto products SHOULD be prepared. The security policy SHOULD regulate who is responsible for the secure operation of the cryptographic products. For the crypto products used, there should be representation rules.

Also SHOULD the necessary training and awareness raising measures for users as well as rules of conduct and reporting channels for problems or security incidents be determined. Further, the policy SHOULD define how to ensure that crypto modules are securely configured, properly deployed, and regularly maintained.

The policy SHOULD be known to all relevant employees and fundamental to their work. If the policy is changed or deviated from, this should be agreed and documented with the ISB. It SHOULD be checked regularly to see if the directive is still correctly implemented. The results SHOULD be sensibly documented.

#### CON.1.A8 Cryptographic and Product Impact Assessment (CIA)

Before a decision can be made as to which cryptographic methods and products are used in the event of increased protection requirements, the following influencing factors, among others, should be determined:

* Security aspects (see CON.1.A6 * Needs Assessment for cryptographic procedures and products *),
* technical aspects,
* Personnel and organizational aspects,
* economic aspects,
* Lifetime of cryptographic procedures and key lengths used
* Approval of cryptographic products and
* legal framework.
#### CON.1.A9 Selection of a suitable cryptographic product [IT operation, specialist responsible persons] (CI)
Before a cryptographic product is selected, the institution SHOULD specify what requirements the product must meet. In doing so, aspects such as functional scope, interoperability, economic efficiency as well as operating errors and malfunction safety SHOULD be considered. It SHOULD be checked if certified products should be used as a priority. Also, the future locations SHOULD be considered in the selection, as it is z. For example, there are export and import restrictions on cryptographic products.

#### CON.1.A10 Development of a crypto-concept (CI)

A crypto-concept SHOULD be developed, which is integrated into the security concept of the institution. The concept SHOULD describe all technical and organizational requirements for the cryptographic products used. Also, all relevant applications, IT systems and communication links SHOULD be listed. The created crypto-concept SHOULD be updated regularly.

#### CON.1.A11 Secure configuration of crypto modules [IT operation] (CI)

Crypto modules SHOULD be securely installed and configured. All preset keys SHOULD be changed. Subsequently, it should be tested whether the crypto modules function correctly and can be operated by the user.

Furthermore, the requirements for the environment of use SHOULD be specified. If an IT system is changed, SHOULD it be tested whether the cryptographic methods used are still effective. The configuration of the crypto modules SHOULD be documented and regularly checked.

#### CON.1.A12 Secure role sharing when using crypto modules [IT operation] (CI)

When configuring a crypto module, user roles SHOULD be specified. It should be verified with access control and authentication mechanisms, whether an employee may actually use the service requested. The crypto module SHOULD be configured so that the authentication information must be reentered every time the reel changes or inactivity occurs after a certain period of time.

#### CON.1.A13 OS Security Requirements When Using Crypto Modules (CI)

The interaction of operating system and crypto modules SHOULD ensure that

* the installed crypto modules can not be switched off or bypassed unnoticed,
* the applied or stored keys can not be compromised
* the data to be protected can only be stored unencrypted on data media with the knowledge and control of the user or can leave the information-processing system; and
* Manipulation attempts are detected on the crypto module.
#### CON.1.A14 Training of users and administrators [supervisors, IT managers, specialists] (CIA)

There should be training sessions that teach users and administrators how to handle the crypto modules they serve. Users SHOULD explain exactly what the specific security settings of crypto modules mean and why they are important. You should also be alerted to the dangers of bypassing or disabling these security settings for convenience. The training contents SHOULD always be adapted according to the respective application scenarios.

Administrators SHOULD also learn how to use tools to investigate cryptographic settings. Also they SHOULD get an overview of cryptographic basic concepts.

#### CON.1.A15 Reaction to practical weakening of a crypto-method (CI)
It SHOULD establish a process that can be used in case of a weakened cryptographic process to ensure the information security of the institution. It should be ensured that the weakened cryptographic process can be secured or replaced by a suitable alternative.

#### CON.1.A16 Physical Protection of Cryptomodules [Head IT] (CI)

It SHOULD prevent unauthorized physical access to module contents of the crypto module. Hardware and software products used as crypto modules SHOULD perform a self-test.

#### CON.1.A17 Radiation Safety [Head IT] (C)

It SHOULD be investigated whether additional measures with regard to radiation safety are necessary. This SHOULD be done in particular when processing state classified information (VS) classified as VS-CONFIDENTIAL and higher.

#### CON.1.A18 Cryptographic Replacement Modules [IT Leader] (CIA)

SHOULD spare crypto modules be kept in stock.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the area of ​​"crypto concept" can be found in the following publications, among others:

* #### [27001A10] ISO / IEC 27001: 2013 - Annex A.10 Cryptography

  

 Information technology - Security techniques - Information security management systems - Requirements, in particular Annex A, A.10 Cryptography, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [BSILEK] Guide Creating Crypto Concepts

  

 Federal Office for Security in Information Technology (BSI), 07.2008
 [https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Arbeitshilfen/Kryptokonzept/Kryptokonzept\_node.html](https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Arbeitshilfen/ encryption concept / Kryptokonzept_node.html)

 
* #### [BSIMKK] Sample crypto concept

  

 BSI, 05.2010
 [Https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Sicherheitsberatung/Krypto/2010-04-28\_Musterkryptokonzept\_V12\_pdf.pdf](https://www.bsi.bund. de / SharedDocs / Downloads / dE / BSI / security consulting / crypto / 2010-04-28_Musterkryptokonzept_V12_pdf.pdf)

 
* #### [ISFTS2] The Standard of Good Practice - Area TS2 Cryptography

  

 Information Security Forum (ISF), in particular Area TS2 Cryptography, 06.2016

 
* #### [NIST800175B] NIST Special Publication 800-175B

  

 Guidelines for Using Cryptographic Standards in the Federal Government, 03.2013
 [Https://csrc.nist.gov/publications/drafts/800-175/sp800-175b\_draft.pdf](https://csrc.nist.gov/publications/drafts/800-175/sp800-175b_draft. pdf)

 
* #### [TR02102] Cryptographic method recommendations and key lengths

  

 BSI, (last accessed on 27.09.2017)
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "crypto concept" building block.

* G 0.13 Interception of compromising radiation
* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.27 Resource shortage
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.37 denying actions
* G 0.40 Denial of Service
* G 0.43 Importing messages
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
