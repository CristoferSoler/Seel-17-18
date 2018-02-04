Table of content

[toc]
 
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

Electronic archives can contain very large amounts of data. The individual data records are stored according to certain classification criteria, which are to be distinguished into index data of the business applications and index data of the archive system. If unsuitable ordering criteria are used, archived documents may not be retrievable, or only very laboriously re-searched, or the semantics of the documents can not be determined unambiguously. Likewise, there is a risk that retention targets will be missed by an unsuitable or limited selection of ordering criteria, e.g. B. the ability to prove to third parties.

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
