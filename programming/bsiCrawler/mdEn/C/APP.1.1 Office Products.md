1 description
--------------

### 1.1 Introduction

The Office Products group includes all applications that are used to create, edit, and view documents. These include, among others, the free application LibreOffice and the proprietary application Microsoft Office, which are used in many institutions. Office products are part of the necessary basic IT equipment for most institutions. They include word processing programs, spreadsheets and presentations, as well as drawing programs and simple database systems. Using Office applications makes it easier and easier to gather and process information.

### 1.2 Objective

The aim of this module is to protect the information that is processed and used when using Office products. There are special requirements for the functionality of the components of Office products. The module displays requirements that should be implemented to protect Office products against specific threats.

### 1.3 Delimitation

This module looks at the use of Office products from the perspective of IT operations and provides guidance to users on how Office products should be used. There are specific requirements to be met when using Office products. In addition to the requirements of this module, the implementation of the requirements of the higher-level POU CON.4 * Selection and use of standard software * must be ensured. E-Mail and PIM applications are excluded in this module, the corresponding requirements are documented in the module APP.1.4 * Groupware *. In the case of e-mail and PIM applications from Microsoft, the module APP.1.1 * Microsoft Exchange / Outlook * must also be observed. When using integrated database systems such as Base in LibreOffice or Access in Microsoft Office, the module APP.4.3 * Database * must be taken into account. Also excluded in this module are pure cloud office applications such as Google's G Suite (Docs, Sheets and so on). Requirements for cloud applications are defined in the building blocks OPS.2.2 * Cloud usage * and * * APP.5.3 * Cloud applications from the client point of view *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​Office products:

### 2 1 Lack of adaptation of Office products to the needs of the institution

Lack of attention to Office product requirements when purchasing or customizing the software can significantly disrupt operations. This may be due to lack of compatibility with existing templates and documents, lack of functionality of the version used or lack of interoperability with business partner applications. If office products are not adapted to the needs of the institution, this can lead to performance losses, disruptions or errors within the business processes.

### 2 2 Lack of or insufficient testing and approval of Office products

If new Office products and their integration into the institution are not or insufficiently tested and released without installation instructions, it may happen that errors are not detected or that the installation parameters that are necessarily observed are not recognized or ignored. Errors in Office products that result from a missing or inadequate testing and approval process pose a significant threat to IT operations. Workflows can be significantly hampered by Office Product Errors. Incorrect updates to the Office products can lead to data loss or reduce the availability of used databases.

### 2 3 Protective data in residual information in Office documents
Office documents typically store metadata about the document itself, as well as author and institution information. This meta-information can be extended to any, user-defined entries, support the workflows of the business processes and ensure appropriate transparency. In addition, Office products provide the ability to create comments in the document and add or modify information in Review mode. This and other residual information may contain confidential information that may not be disclosed to third parties. Otherwise, this may result in a loss of confidentiality and subsequent falsification of the residual information and cause financial, procedural and image damage.

### 2 4 Obtain Office products and updates from unreliable sources

If you obtain installation sources or updates of Office products from unofficial sources, there is no guarantee that the software will function properly and be free from malicious code. This applies both to the Office products themselves and to functions that exist as plug-ins or add-ons or as macros in documents. This can cause calculations to yield incorrect results or affect the integrity and availability of systems.

### 2 5 Manipulation of Office documents

The manipulation of Office documents means changing information. Office documents can typically contain a variety of Active Content, sometimes used for complex automation. However, active content may also contain malicious code that runs when the user opens the document with the rights. Such malicious programs in Office documents, in addition to manipulation of the affected document, can change other documents unrecognized or spread in other documents. All affected business processes of the institution can be disturbed or blocked in their functions. In the worst case, the manipulation remains undetected and leads to security vulnerabilities and processing of corrupted information.

### 2 6 Lack of commitment of Office documents

Depending on the intended use, it may be necessary to be able to assign Office documents to one or more authors in a binding manner or to prove that someone has taken note of a document. If this function can easily be circumvented or is it not intended or if it does not comply with the legal requirements, invalid contracts can be created or the legality of existing contracts can be challenged.

### 2 7 Loss of Office document integrity

The integrity of Office documents may be corrupted by unintended changes or deliberate manipulation of document content. Weak handling of Office products or ignorance of users when handling Office documents may result in undetected changes to documents. This is particularly problematic when it comes to documents in productive use. Working with documents that have been forged unrecognized may result in wrong business decisions or damage to the image of the institution.

### 2 8 Software vulnerabilities in Office products
Software vulnerabilities in Office products are often not fully discovered before delivery to customers, despite intensive testing. Failure to detect these software vulnerabilities in time may result in application crashes and errors. The consequences of unresolved bugs can include incorrect calculation results or loss of integrity in documents. Software vulnerabilities or errors can also cause serious security vulnerabilities in Office products. Such vulnerabilities may be exploited by attackers to inject malicious code.

### 2 9 Use of unlicensed Office products

Unlicensed office products are a potential financial hazard for institutions. If Office products are used without a valid software license because, for example, the license volume has been exceeded unnoticed, this can lead to contractual penalties upon discovery. Conversely, excessive licensing costs may be incurred because office products are installed in workplaces where they are not needed.

### 2 10 Data loss due to password protection of Office documents

Data loss on Office documents can block business processes. Typically, Office products provide the ability to provide documents with a password when saving, which is required to open or edit the document. Careless use of this feature may result in lost document passwords being no longer known or unidentifiable. As a result, important documents can no longer be read or further edited at great expense. This additional effort must be compensated technically and organisationally, which in turn leads to an increased workload.

### 2 11 Unauthorized exercise of rights in Office products

Access rights are used as organizational measures to protect information, business processes and IT systems from unauthorized access. Improper access to Office products by unauthorized persons can compromise the confidentiality and integrity of the information by altering, deleting, or improperly creating information. Such vulnerabilities usually arise due to incorrect rights. Affected business processes can be corrupted, inadvertently process incorrect information or disclose sensitive information.

3 requirements
---------------

The following are specific requirements for protecting Office products. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### APP.1.1.A1 Ensure the integrity of Office products

When installing Office products, you MUST ensure that only unmodified copies of the original shared software are used. Updates MUST be sourced exclusively from secure sources. If checksums are offered for an Office product, they should be checked before installation. If digital signatures are available for an Office product, they should be checked before installing the package. The administrators SHOULD be informed about the meaning and significance of checksums and digital signatures. Just as with a new installation, it must be ensured during the installation of updates that the update packages are unchanged.

#### APP.1.1.A2 Restricting Active Content [User]
The automatic execution of embedded Active content, such as macros or ActiveX elements, MUST be disabled in the settings of all Office products used. If Active Content Execution is required for a business process, care must be taken to ensure that only Active Content from trusted sources is executed. All users MUST be educated in Active Content Danger Training and briefed on Active Content Restriction features.

#### APP.1.1.A3 Opening documents from external sources

All documents obtained from external sources MUST be checked for malware prior to opening. All classified as problematic and additionally all file formats that are not required within the institution MUST be banned. The users MUST be trained and sensitized to handle documents from external sources. The examination of documents from external sources SHOULD be enforced by technical measures.

#### APP.1.1.A4 Securing ongoing operation of Office products

IT operations and ISB MUST regularly check for known security vulnerabilities in Office products. Existing patches MUST be recorded in a timely manner.

Users SHOULD be informed about the possibilities and limitations of the security features of the software used and the storage formats used. The requirements for secure use of Office products SHOULD be integrated into the security policy.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of office products. They SHOULD be implemented in principle.

#### APP.1.1.A5 Selection of suitable office products

As part of the procurement of office applications, the institution's requirements for office products SHOULD be charged by the technical and IT department. These should be documented in a requirements catalog. If all the requirements for the Office product to be procured are documented, the products available on the market SHOULD be examined to what extent they fulfill these requirements of the institution. When choosing between several alternatives, additional costs SHOULD also be considered; These include, for example, overhead for training administrators and users or for migration.

#### APP.1.1.A6 Testing new versions of Office products

New versions of Office products SHOULD be checked for compatibility with established tools (such as document templates, forms) of the institution prior to production. For this purpose, test methods for the individual tests (test types, methods and tools) SHOULD be developed and released. It SHOULD be made sure that important work equipment works well even with the new software function. In case of detected incompatibilities, a migration plan for the affected documents SHOULD be created.

#### APP.1.1.A7 Installation and configuration of Office products

For the office products used, a standard configuration adapted to the needs of the institution SHOULD be created and used. This configuration SHOULD be documented in an installation and configuration statement. The installation and configuration SHOULD be done according to the instruction and apply the default settings. All necessary deviations from the defined standard configuration SHOULD be comprehensibly documented and require the approval of a suitable approval authority. In the case of pilot installations, these should always be accompanied by the IT department. Before and after the installations, backups of the Office products SHOULD be performed on all affected IT systems.
#### APP.1.1.A8 Version control of Office products

There SHOULD be a regular check of the installed versions of Office products. This inventory of software licenses SHOULD be updated each time you install or uninstall. In addition, the different configurations of installed Office products SHOULD be documented.

#### APP.1.1.A9 Removal of residual information before forwarding documents [User]

Before passing on documents to third parties, all unnecessary and confidential residual information from Office documents SHOULD be removed. In addition, the metadata SHOULD be cleaned up. All users SHOULD be sensitized and trained in the risks of residual information as well as the possibilities of elimination in the office products used. The transmission of documents SHOULD be done in a non-modifiable format if processing by the recipient is not required.

#### APP.1.1.A10 End User Software Development [User]

Binding rules for software development based on Office applications (eg macros, spreadsheets) by end users SHOULD be made, see also APP.5.2.A2 Restricting Active Content. First, in each institution SHOULD be made the fundamental decision whether such self-developments are desired or not. The decision SHOULD be documented in the affected security policy. If proprietary developments are allowed, a procedure should be developed for dealing with the corresponding functions of Office products for end users. Responsibilities SHOULD be clearly defined. All information about the created applications SHOULD be documented. Current versions SHOULD be made available to all affected users in a timely manner.

#### APP.1.1.A11 Regulated use of extensions for Office products

All Office product enhancements SHOULD be tested on new releases prior to productive use, as in the test procedure. The tests to be performed SHOULD ONLY be performed on isolated test systems. The tests SHOULD verify that extensions have no negative impact on Office products and on-going IT systems. The tests of the extensions used SHOULD follow a defined test plan, which guarantees traceability for third parties.

#### APP.1.1.A12 Waiver of Cloud Storage [User]

The cloud storage features built into some Office products SHOULD be disabled. All cloud drives SHOULD be disabled. All documents SHOULD be stored on centrally managed file servers of the institution. To share documents with others for review or editing, use specialized applications such as appropriate data rooms that have security features such as encrypted data storage and distribution, and a suitable user and rights management system.

#### APP.1.1.A13 Using Viewer Functions [User]

Data from potentially insecure sources such as the Internet or e-mail attachments SHOULD automatically be opened in a protected mode where they can not be edited immediately. Only a general navigation SHOULD be enabled. This feature SHOULD NOT be disabled by the user. SHOULD use appropriate viewer applications if they are available. A list of trusted places can be defined from which content can be opened and edited immediately.

#### APP.1.1.A14 Protection against subsequent changes of information [user]
Depending on the intended use of documents, the existing security mechanisms in application programs SHOULD be used to restrict further handling of the created files. Employees SHOULD be advised on how these security mechanisms work and how to apply them.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.1.1.A15 Use of encryption and digital signatures (CI)

Data with increased protection requirements SHOULD be encrypted prior to transmission or storage to ensure confidentiality. BEFORE using an encryption feature built into an Office product, SHOULD check if it provides adequate protection, especially for older product versions. The IT systems of sender and recipient SHOULD ensure access protection to the encryption method used. Users SHOULD be trained and sensitized in handling the encryption functions. In addition, a method SHOULD be used to digitally sign macros and documents. The validity of the used certificates SHOULD be limited in time.

#### APP.1.1.A16 Integrity check of documents (I)

To protect against accidental alteration of data with increased protection requirements during transmission and / or storage, checksum procedures SHOULD be used. A method should be selected that is able to independently correct the data. In addition, cryptographic checksum procedures SHOULD be used to protect against manipulation.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the "Office Products" area can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [LIBRE] LibreOffice

  

 The Document Foundation - LibreOffice, (last accessed on 28.09.2017)
 <Https://de.libreoffice.org>

 
* #### [MSTN] Microsoft Technet

  

 Microsoft, (last accessed on 28.09.2017)
 <Https://technet.microsoft.com/de-de>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Office Products" building block.

* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.37 denying actions
* G 0.39 Malware
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
