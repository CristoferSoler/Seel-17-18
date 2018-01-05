1 description
--------------

### 1.1 Introduction

Businesses and governments are storing more and more data and at the same time relying more and more on it. Data is then lost, eg. B. by defective hardware or malware, can cause serious damage. However, regular data backups minimize such effects. A data backup should ensure that redundant data can be used to resume IT operations at short notice if parts of the operational data are lost.

### 1.2 Objective

This module shows how institutions can create a data protection concept and what requirements must be met.

### 1.3 Delimitation

The module describes the basic requirements that contribute to an adequate data backup concept. Not covered are requirements for the preservation and preservation of electronic documents for long-term storage. These can be found in the module OPS.1.2.2 * Archiving *. This module does not contain any system or application-specific requirements for logging; these can be found in the respective modules of the IT-Grundschutz Compendium, such as SYS.1.1. General server, APP.3.2 web server or NET.3.2 firewall.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the field of data protection:

### 2 1 Missing backup

Institutions are more dependent than ever on their IT systems and the data stored in them. If data is lost, eg. Malware, technical malfunctions, a fire or when employees delete data intentionally or unintentionally and there is no data backup, this is sometimes a life-threatening damage to the institution, eg. For example, if all customer data is lost.

### 2 2 Missing recovery tests

An institution regularly backs up its important data, especially its customer data. However, if it is not regularly tested whether the data can be restored, the backed up data in the event of a necessary recovery can not be used. In the case of customer data, this could mean significant damage to the institution, including the cessation of distribution.

### 2 3 Unsuitable storage of backup volumes

Backup media contain a host of valuable institutional information. If the data carriers are stored in an insecure place, an attacker (eg an innocent person) may be able to access them and steal or manipulate information worthy of protection. Similarly, backup media may become unusable due to improper storage or climatic conditions, and then become unavailable when needed.

### 2 4 Missing or insufficient documentation

If data protection measures are not documented or only insufficiently documented, the recovery can take longer than planned. This can delay important processes, eg. In production. It is also possible that a data backup can no longer be imported and the data is lost.

### 2 5 Disregard of legal regulations

If at the data security legal requirements, eg. For example, data protection laws are not respected, fines can be imposed on the institution or claims for damages can be asserted.

### 2 6 Unsafe cloud providers

If institutions outsource their data protection to a cloud provider, an attacker could also access the backup data or the backup can not be restored quickly enough. As a result, data worth protecting has leaked out or emergency backups have not been available in the required time.

### 2 7 Insufficient storage capacity
The amount of processed and therefore also stored data is steadily increasing. If the backup media does not have enough memory, more up-to-date data may no longer be backed up or the backup software used will automatically overwrite old and possibly still necessary backups. Are those responsible not informed about this because z. For example, if monitoring is inadequate, data may be lost or only the wrong versions are available in an emergency.

### 2 8 Insufficient data protection concept

If no adequate data protection concept is created and followed for data protection measures, then backed up data can not be restored if necessary. The backed-up data is usually sensitive information, so the backup is encrypted. If a loss of data also affects the key to decrypt the backup because it was not considered to keep it separate, recovery may not be possible.

3 requirements
---------------

The following are specific requirements for data protection. Basically, the information security officer is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### CON.3.A1 Survey of influencing factors of data protection [IT-Betrieb, Fachverantwortliche]

For each IT system and possibly for some particularly important IT applications, the relevant influencing factors MUST be determined, such as: Change volume, change dates, availability requirements, integrity requirements. For this, the administrators and the persons responsible for the individual IT applications SHOULD be interviewed. The results MUST be traceable and appropriately recorded. New requirements MUST be considered in a timely manner in an updated data protection concept.

#### CON.3.A2 Definition of the procedure for the data backup [IT-Betrieb, Fachverantwortliche]

For each IT system and for each type of data, a method MUST be defined as to how the data is to be backed up. For this, the nature, frequency and timing of the backups MUST be determined. Furthermore, the responsibilities for the backups MUST be set. Also MUST be defined, which storage media used and how the transport and storage modalities have to look.

#### CON.3.A3 Determination of legal factors influencing data backup

The legal requirements for data backup MUST be determined and included in the minimum or in the data backup concept.

#### CON.3.A4 Creation of a minimal data backup concept

A minimum data backup concept MUST be created that determines which data backup requirements are to be met. These include brief descriptions of how to back up and restore the data, which parameters have been selected, and which hardware and software are being used.

#### CON.3.A5 Regular data backup [IT operation]

Regular backups MUST be performed. At least the data MUST be backed up on a regular basis, which can not be derived from other information. The backups created MUST be protected against third party access. It must be regularly tested whether the backup works as desired, especially if backed up data can be easily replayed

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of data backup. They SHOULD be implemented in principle.

#### CON.3.A6 Development of a data protection concept [Head of IT, specialist responsible]
A backup concept SHOULD be created. This SHOULD be coordinated with all those responsible. It SHOULD list all the IT systems to consider. Employees SHOULD be informed about the part of the data protection concept that concerns them. It SHOULD be checked regularly, if the data protection concept is implemented correctly.

#### CON.3.A7 Procurement of a suitable data security system [Head IT, IT Operations]

Before a backup system is procured, a list of requirements SHOULD be created to evaluate the products available on the market. The purchased backup systems SHOULD meet the requirements of the security and data protection concept.

#### CON.3.A8 Function Tests and Recoverability Check [IT Operations]

It SHOULD be tested on a regular basis, whether the data backup works as desired and, above all, whether backed up data can be reproduced easily and in a reasonable amount of time.

#### CON.3.A9 Requirements for online data backup [Head of IT, IT operation]

If an online storage is to be used for the data backup, at least the following points should be regulated:

* Design of the contract,
* Location of data storage,
* Quality of service agreements (SLA),
* suitable authentication methods,
* Encryption of the data and
* Encryption on the way.
#### CON.3.A10 Employee commitment to backup

All employees SHOULD be informed about the data protection regulations. Also, they SHOULD be informed about their responsibilities in creating backups and their commitment to their implementation.

#### CON.3.A11 Backup copy of the software used [IT operation]

Backup copies should be made of software programs used, provided that this is legally permitted and technically possible. It SHOULD have all the necessary packages and information to reinstall the software in an emergency. Also, the original installation sources and the license numbers SHOULD be kept safely in a suitable place.

#### CON.3.A12 Suitable storage of backup data carriers [IT operation]

The backup volumes SHOULD be protected against unauthorized access. They SHOULD be spatially separated from the source systems. The storage location SHOULD be conditioned so that the storage media can be stored for a longer period of time.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### CON.3.A13 Use of cryptographic procedures for data backup [IT operation]

To ensure the confidentiality and integrity of the data backed up, all data SHOULD be encrypted. It SHOULD be ensured that the encrypted data can be imported again after a long time. Used cryptographic keys SHOULD be protected with a separate backup.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on hazards and security measures in the area of ​​"data protection concept" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [BKBU] Guide Backup / Recovery / Disaster Recovery

  

 Bitkom, 2016
<Https://www.bitkom.org/noindex/Publikationen/2017/Leitfaden/170125-LF-Backup-Recovery.pdf>

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the "Data backup concept" building block.

* G 0.2 Unfavorable climatic conditions
* G 0.4 Pollution, dust, corrosion
* G 0.14 Spying out information (spying)
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.22 Manipulation of information
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.31 Incorrect use or administration of devices and systems
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
