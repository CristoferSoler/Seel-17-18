Table of content

[toc]
 
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

If new Office products and their integration into the institution are not or insufficiently tested and released without installation instructions, it may happen that errors are not detected or that the installation parameters that are necessarily observed are not recognized or ignored. Errors in Office products that result from a missing or inadequate testing and approval process pose a significant threat to IT operations. Workflows can be significantly hampered by Office product errors. Incorrect updates to the Office products can lead to data loss or reduce the availability of used databases.

### 2 3 Protective data in residual information in Office documents
Office documents typically store metadata about the document itself, as well as author and institution information. This meta-information can be extended to any, user-defined entries, support the workflow of the business processes and ensure appropriate transparency. In addition, Office products provide the ability to create comments in the document and add or modify information in Review mode. This and other residual information may contain confidential information that may not be disclosed to third parties. Otherwise, this may result in a loss of confidentiality and subsequent falsification of the residual information, causing financial, procedural and image damage.

### 2 4 Obtain Office products and updates from unreliable sources

If you obtain installation sources or updates of Office products from unofficial sources, there is no guarantee that the software will function properly and be free from malicious code. This applies both to the Office products themselves and to functions that exist as plug-ins or add-ons or as macros in documents. This can cause calculations to yield incorrect results or affect the integrity and availability of systems.

### 2 5 Manipulation of Office documents

The manipulation of Office documents means changing information. Office documents can typically contain a variety of Active Content, sometimes used for complex automation. However, active content may also contain malicious code that runs when the user opens the document with the rights. Such malicious programs in Office documents, in addition to manipulation of the affected document, change other documents unrecognized or spread in other documents. All affected business processes of the institution can be disturbed or blocked in their functions. In the worst case, the manipulation remains undetected and leads to security vulnerabilities and processing of corrupted information.

### 2 6 Lack of commitment of Office documents

Depending on the intended use, it may be necessary to be able to assign Office documents to one or more authors in a binding manner or to prove that someone has taken note of a document. If this function can easily be circumvented or is it not intended, or if it does not meet the legal requirements, invalid contracts can be created or the legality of existing contracts can be challenged.

### 2 7 Loss of Office document integrity

The integrity of Office documents may be corrupted by unintended changes or deliberate manipulation of document content. Weak handling of Office products or ignorance of users when handling Office documents may result in undetected changes to documents. This is particularly problematic when it comes to documents in productive use. Working with documents that have been forged unrecognized may result in wrong business decisions or damage to the image of the institution.

### 2 8 Software vulnerabilities in Office products
Software vulnerabilities in Office products are often not fully discovered before delivery to customers, despite intensive testing. Failure to detect these software vulnerabilities in time may result in application crashes and errors. The consequences of unresolved bugs can include incorrect calculation results or loss of integrity in documents. Software vulnerabilities or errors can also cause serious security vulnerabilities in Office products. Such vulnerabilities may be exploited by attackers to inject malicious code.

### 2 9 Use of unlicensed Office products

Unlicensed office products are a potential source of financial risk to institutions. If Office products are used without a valid software license because, for example, the license volume has been exceeded unnoticed, this can result in contractual penalties upon discovery. Conversely, excessive licensing costs may be incurred because office products are installed in workplaces where they are not needed.

### 2 10 Data loss due to password protection of Office documents

Data loss on Office documents can block business processes. Typically, Office products provide the ability to provide documents with a password when saving, which is required to open or edit the document. Careless use of this feature may result in lost document passwords being no longer known or unidentifiable. As a result, important documents can no longer be read or further edited at great expense. This additional effort must be compensated technically and organisationally, which in turn leads to an increased workload.

### 2 11 Unauthorized exercise of rights in Office products

Access rights are used as organizational measures to protect information, business processes and IT systems from unauthorized access. Improper access to Office products by unauthorized persons can compromise the confidentiality and integrity of the information by altering, deleting, or improperly creating information. Such vulnerabilities usually arise through incorrect rights. Affected business processes can be corrupted, inadvertently process erroneous information or disclose sensitive information.
