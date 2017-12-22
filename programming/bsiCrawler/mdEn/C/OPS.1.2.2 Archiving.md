1 description
--------------

### 1.1 Introduction

Archiving plays a special role in the document management process, as it is expected that the documents will be available until the expiration of a given retention period and, on the other hand, their confidentiality and integrity will be preserved. In addition, the context must be preserved so that the respective stored process can be reconstructed.

Throughout the duration of long-term storage, measures to preserve information and, if necessary, evidential conservation measures must be implemented.

In German information technology usage, the term electronic archiving is sometimes used interchangeably with the term electronic long-term storage. For better comprehensibility, this module therefore generally refers only to archiving or digital long-term archives. An IT process for storing electronic documents is referred to as an archive system or digital archive or long-term storage. The retention period of the documents is determined by the legal and other requirements as well as the purpose of the data.

The term documents used in this module subsumes data and documents, unless they are expressly used in a different meaning.

From a legal point of view, the term archiving in Germany is substantiated and proven by the archival laws of the federal and state governments. Therefore, it is to be distinguished from the time-limited storage considered in this document. Archiving in the legally correct sense concerns only documents of the public administration and refers to the fact that documents of an authority, as soon as they are no longer needed for the purposes of the authority, to be separated and kept by a competent state institution (Bundesarchiv) for an indefinite period ( see §§ 1 and 2 BArchG).

### 1.2 Objective

The module describes how documents can be archived long-term, securely, unchangeable and reproducibly. For this purpose, requirements are defined with which an archive system can be planned, implemented and operated safely.

### 1.3 Delimitation

The Archiving module describes security measures for the preservation and preservation of electronic documents for long-term storage within the current retention periods. Operations for operational backup are not covered in this module. Requirements for this are presented in OPS.1.1.6 Data backup. shown.

A digital long-term storage consists of individual components, eg. A database. How such components can be operated safely in detail, however, is also not the subject of this module. This can z. For example, the requirements from the modules APP.4.3 Relational Database Systems, SYS.1.1 General Server and SYS.1.8 Storage Systems can be supplemented. Systems, SYS.1.1 General Server and SYS.1.8 Storage Systems can be added., SYS.1.1 General Server and SYS .1.8 storage systems. and SYS.1.8 storage systems. be supplemented.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the field of archiving:

### 2 1 Insufficient migration of archive systems

Archived data should typically remain stored for a very long time. During this period, the underlying technical system components, storage media and data formats may physically or technically age and thereby become unusable. In addition, there may be problems with the compatibility of the data formats used over time.
If the aging of the existing system is unresponsive, it can be expected in the long term, for example, that archived raw data will no longer be readable by the archive media or that archived data will be changed by physical errors in the archive system and media.

### 2 2 Inadequate classification criteria for archives

Electronic archives can contain very large amounts of data. The individual data records are stored according to certain classification criteria, which are to be distinguished into index data of the business applications and index data of the archive system. If unsuitable order criteria are used, archived documents may not be retrieved or can only be re-searched with great difficulty, or the semantics of the documents can not be clearly determined. Likewise, there is a risk that retention targets will be missed by an unsuitable or limited selection of ordering criteria, e.g. B. the ability to prove to third parties.

### 2 3 Inadequate documentation of archive accesses

Unauthorized archive access is usually uncovered using log files. However, if not logged sufficiently, there is a risk that such access will not be detected. As a result, attackers could go unnoticed to the information stored there and they z. Copy or modify.

### 2 4 Inadequate transfer of paper data to an electronic archive

When documents are scanned, the appearance or semantics of the recorded data may be falsified or documents may be lost. This leads to incorrect interpretations and calculations, eg. For example, if important parts of the document or stack of documents are forgotten during scanning.

### 2 5 Insufficient renewal of cryptographic procedures during archiving

Cryptographic methods that z. As with signatures, seals, time stamps, technical evidence (Evidence Records) or encodings are used, must be regularly adapted to the current state of the art, so that the protective effect is maintained. Failure to do so may, for example due to an outdated unsafe signature, jeopardize the integrity of the document so that the file will not be admitted as evidence in court. Also, the confidentiality of an encrypted document is lost.

### 2 6 Insufficient performance of archival revisions

If the archiving process is under-scrutinized or under-scrutinized, this can indirectly result in the entire process not functioning properly. Thus, the integrity of the archived documents themselves can be doubted. This may result in legal and economic disadvantages for the institution: Under certain circumstances, a file may not be admitted as evidence in court because it can not be ruled out that it has been manipulated.

### 2 7 Infringement of the legal framework when using archiving

When archiving electronic documents, various legal framework conditions must be observed. Failure to comply with this may result in civil or criminal penalties, eg. For example, minimum retention periods that arise for tax, budgetary or other reasons.

3 requirements
---------------
The following are specific requirements for archiving. Basically, the archive manager is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### OPS.1.2.2.A1 Identification of influencing factors for electronic archiving

Before deciding which procedures and products to use for electronic archiving, the technical, legal and organizational influencing factors MUST be identified and documented. The results MUST be included in the archiving concept.

#### OPS.1.2.2.A2 Development of an archiving concept

It MUST be defined which goals are to be achieved with the archiving. In particular, it has to be taken into account which regulations have to be adhered to, which employees are responsible and which range of functions and services is desired.

The results MUST be recorded in an archiving concept. Management MUST be involved in this process. The archiving concept MUST be regularly adapted to the current circumstances of the institution.

#### OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]

Since archive systems centrally store sensitive data of an institution, their IT components MUST be installed in secure rooms. It MUST be ensured that only authorized persons are allowed to enter the rooms. For archive storage media to be stored long-term, they MUST be stored properly.

#### OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]

All data, documents and data records stored in an archive MUST be clearly indexed in order to be able to quickly find them again in later search queries. For this, it must already be determined during the conception, which structure and which extent the index data for an archive should have.

#### OPS.1.2.2.A5 Regular processing of archived data [Head IT]

It MUST be ensured throughout the archiving period that

* the used data format can be processed by the used applications,
* the stored data will remain readable and reproducible in the future so that semantics and probative value can be maintained,
* the used file system can be processed on the storage medium by all involved components,
* the storage media can be read at any time technically flawlessly and
* the cryptographic methods used for encryption and evidential value preservation by means of digital signature, seal, time stamp or technical evidence data (Evidence Records) correspond to the state of the art.
#### OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]

The integrity of the index database MUST be ensured and verifiable. In addition, the index database MUST be backed up regularly. The backups MUST be recoverable. Medium and large archives MUST have redundant index databases.

#### OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]

All archive data, the associated index databases and the system data MUST be backed up regularly (see OPS.1.1.6 * Data backup). *).

#### OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
All access to electronic archives MUST be logged. To do this, the date, time, user, client system, and the actions taken and error messages should be recorded. The retention period of the log data SHOULD be specified in the archiving concept.

The log data of the archive accesses SHOULD be evaluated regularly. In doing so, the institution's internal guidelines SHOULD be observed.

Also, SHOULD be defined which events (eg system errors, timouts or data records) are to be signaled to which employees are displayed. Critical events SHOULD be checked immediately after signaling and, if necessary, further escalated.

#### OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]

For archiving a suitable data format MUST be selected. It MUST ensure that archive data as well as selected characteristics of the original document medium can be reproduced long-term and true to the original.

The document structure of the selected data format MUST be clearly interpretable and electronically processable. The syntax and semantics of the data formats used SHOULD be documented and published by a standardization organization. It was intended to use a lossless image compression method for proof-proof and audit-proof archiving.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of archiving. They SHOULD be implemented in principle.

#### OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]

It SHOULD be ensured that employees use the archive system as intended in the archiving concept. For this purpose, an administration and a user policy SHOULD be created. The administration policy SHOULD include the following:

* Determination of responsibility for operation and administration,
* Service Level Agreements,
* Modalities of granting access and access rights,
* Modalities of granting access to the services provided by the archive,
* Regulations for handling archived data and archive media,
* Monitoring the archive system and environmental conditions,
* Regulation for data backup
* Rules for logging
* Separation of producers and consumers (OAIS model).
#### OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]

The responsible IT companies and the users SHOULD be trained for their area of ​​responsibility.

The training of IT companies SHOULD cover the following topics:

* System architecture and security mechanisms of the archive system used and the underlying operating system,
* Installation and operation of the archive system and handling of archive media,
* Documentation of the administrative activities and
* Escalation procedures.
The training of users SHOULD cover the following topics:

* Handling the archive system,
* Operation of the archive system,
* legal framework of archiving.
The implementation and participation in the training SHOULD be documented.

#### OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]

The available free space on the archive media MUST be monitored continuously. As soon as a defined limit value is undershot, a responsible employee MUST be alerted automatically. It SHOULD be ensured that the alerting takes place according to the role. There must always be enough empty archive media available to quickly prevent memory bottlenecks.

#### OPS.1.2.2.A13 Regular revision of the archiving processes
IT SHOULD check regularly whether the archiving processes are still working correctly and correctly. For this, a checklist should be created, which contains questions about responsibilities, organizational processes, use of archiving, redundancy of archive data, administration and the technical evaluation of the archive system. The audit results SHOULD be traceable documented and compared with the target state. Deviations SHOULD be investigated.

#### OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]

The market for archive systems SHOULD be monitored regularly and systematically. Among other things, the following criteria should be observed: changes in standards, changes in technology among manufacturers of hardware and software, published vulnerabilities or vulnerabilities as well as loss of security suitability in cryptographic algorithms.

#### OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]

It SHOULD continuously monitor how the field of cryptography develops to assess whether an algorithm is still reliable and sufficiently secure (see also OPS.1.2.2.A20 Appropriate Use of Cryptographic Techniques).

Archive data that has been secured by cryptographic techniques whose security suitability will be lost in the foreseeable future SHOULD be re-secured in a timely manner using secure procedures, e.g. encrypted or signed.

#### OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]

Archive systems SHOULD be kept up-to-date over a long period of time. New hardware and software SHOULD be thoroughly tested before installation in a running archive system. When new components are put into operation or new file formats are introduced, a migration concept SHOULD be created. It SHOULD describe all changes, tests and expected test results. The conversion of the individual data SHOULD be documented (transfer note).

If archive data is to be converted into new formats, it should be checked whether, due to legal requirements, the data must also be archived in its original format.

#### OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]

A new archive system SHOULD always be selected based on the specifications described in the archiving concept. It SHOULD meet the requirements formulated there.

#### OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]

For archiving, suitable media SHOULD be selected and used. The aspects to be archived data volume, average access times and average concurrent accesses to the archive system SHOULD be taken into account. Likewise, the archive media SHOULD meet the requirements for long-term archiving with regard to audit security and service life.

#### OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]

For archiving, there should be regular functional and recovery tests. The archiving media SHOULD be checked at least once a year to see if they are still readable and with integrity. For troubleshooting, suitable processes SHOULD be defined.

Furthermore, the hardware components of the archive system SHOULD regularly be checked for proper operation. It SHOULD be checked regularly if all archiving processes are working properly.

### 3.3 Requirements for increased protection requirements
Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)

In order to cover long retention periods, archive data should only be backed up using cryptographic procedures based on current standards and standards.

#### OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)

If documents are digitized on paper and objects of inspection and transferred to an electronic archive, it should be ensured that the digital copy matches the original document visually and in terms of content.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and security measures in the field of "archiving" can be found in the following publications, among others:

* #### [AlgKat] Notice on the electronic signature according to the Signature Act and the Signature Ordinance

  

 Overview of suitable algorithms, BNetzA, 2017
 [https://www.bundesnetzagentur.de/DE/Service-Funktionen/ElektronischeVertrauensdienste/QES/WelcheAufgabenhatdieBundesnetzagentur/GeeigneteAlgorithmenfestlegen/geeignetealgorithmenfestlegen\_node.html](https://www.bundesnetzagentur.de/DE/Service-Funktionen/ElektronischeVertrauensdienste/ QES / WelcheAufgabenhatdieBundesnetzagentur / Suitable algorithms commiting / geeignetealgorithmenfestlegen_node.html)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the "Archiving" block.

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
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.37 denying actions
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
  * OPS.1.2.2.A3 Appropriate installation of archive systems and storage of archive media [Head of IT, IT operation]
* G 0.14 Spying out information (spying)
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.18 Missing planning or missing adjustment
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
* G 0.19 Disclosure of information worthy of protection
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.22 Manipulation of information
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
* G 0.25 Failure of devices or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.26 Malfunction of equipment or systems
  * OPS.1.2.2.A4 Consistent indexing of data during archiving [IT, IT operation, user]
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.28 Software vulnerabilities or errors
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.29 Violation of laws or regulations
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A5 Regular processing of archived data [Head IT]
  * OPS.1.2.2.A8 Logging of archive accesses [Head of IT, IT operation]
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.30 Unauthorized use or administration of devices and systems
  * OPS.1.2.2.A2 Development of an archiving concept
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.31 Incorrect use or administration of devices and systems
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
* G 0.37 denying actions
  * OPS.1.2.2.A1 Identification of influencing factors for electronic archiving
  * OPS.1.2.2.A10 Creation of a guideline for the use of archive systems [Head IT, IT operation]
  * OPS.1.2.2.A11 Briefing on the administration and operation of the archive system [IT, IT operation, user]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A13 Regular revision of the archiving processes
  * OPS.1.2.2.A14 Regular monitoring of the archive system [Head IT]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A17 Selection of a suitable archive system [Head IT]
  * OPS.1.2.2.A18 Use of suitable archive media [Head IT, IT operation]
  * OPS.1.2.2.A19 Regular function and recovery tests during archiving [Head IT, IT Operations]
  * OPS.1.2.2.A21 Transfer of paper data to electronic archives (CI)
* G 0.45 data loss
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
* G 0.46 Loss of integrity of sensitive information
  * OPS.1.2.2.A6 Protection of the integrity of the index database of archive systems [Head IT, IT Operations]
  * OPS.1.2.2.A7 Regular backup of system and archive data [Head IT, IT Operations]
  * OPS.1.2.2.A9 Selection of suitable data formats for the archiving of documents [Head IT, IT operation]
  * OPS.1.2.2.A12 Monitoring of the storage resources of archive media [Head IT, IT operation]
  * OPS.1.2.2.A15 Regular processing of cryptographically secured data during archiving [Head of IT, IT Operations]
  * OPS.1.2.2.A16 Regular renewal of technical archive system components [Head of IT, IT operation]
  * OPS.1.2.2.A20 Appropriate use of cryptographic procedures in archiving [Head of IT] (CI)
