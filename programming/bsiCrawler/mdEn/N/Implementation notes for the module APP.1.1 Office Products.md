1 description
--------------

### 1.1 Introduction

Office products have long been an integral part of the standard IT equipment in the office environment. Editing documents digitally and creating calculations and presentations on the PC has greatly changed the office routine. Accordingly, most employees view office products as basic IT equipment. Precisely because of the widespread use of Office products, these are also used as an attack path, for example, to spread malicious software using macros in Office documents.

Therefore, security measures should be planned and implemented for safe use of Office products, which are appropriate to the protection needs of the institution.

Unless otherwise stated, the following implementation notes refer to Microsoft Office 2007 or later and LibreOffice 5.1 or later in some examples. Older versions of Microsoft Office and LibreOffice are no longer supplied with updates by the manufacturers and should therefore no longer be used in productive operation.

### 1.2 Life cycle

** planning and conception **

In the planning and design phase, principles should be defined as to how Office products are to be used in the institution and what requirements the institution has for Office products. In this way, suitable office products should be selected for the institution and the requirements of the employees (see APP.1.1.M5 Selection of Suitable Office Products). It should also be defined in the planning and design phase how to handle active content (eg macros) in Office documents (see APP.1.1.M2 Restricting Active Content) and if enhancements to the selected Office products to be used (APP.1.1.M11 Regulated use of extensions for office products).

**Procurement**

License management plays an important role in the procurement of office products. Manufacturers usually offer multiple licensing models, of which other models make sense, depending on the size of the installations required for the institution (see APP.1.1.M8 version control of Office products).

**Implementation**

Before deploying to the institution, new versions of Office products should be tested (see APP.1.1.M6 Testing New Versions of Office Products) to ensure that the institution's existing work equipment (such as templates or forms) as well work correctly with the new version. Depending on the established principles on how to work within the institution with Office products, the software used must be configured differently. During the configuration it should be ensured that the most uniform configuration of Office products has been implemented in all workplaces of the institution.

**Business**

To meet the security needs of the institution in the daily use of Office products, the users of the Office products must be integrated. So they need to be informed about security measures that can not be implemented technically and require the involvement of users. Relevant topics include opening office documents from external sources, dealing with meta or other information in Office documents, handling cloud storage options, checking the integrity of Office documents, and handling signed or password-protected Office documents. Documents, see e.g. B. APP.1.1.M9 Eliminate residual information before sharing documents and APP.1.1.M12 Avoid cloud storage.

2 measures
-----------

The following are specific implementation notes in the Office Products section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### APP.1.1.M1 Ensure the integrity of Office productsIn principle, Office products should only be obtained from well-known sources, such as original data carriers or the manufacturer's website. It should be documented which source is chosen for the Office products used and how the process for securing the integrity of the installation sources is designed.

In the past, incidents have repeatedly occurred in which attackers were able to manipulate software packages on the download pages of software manufacturers. In order to prevent that manipulated software is rolled out in the institution, the authenticity of software packages of the office products used should be strictly checked.

To prevent unauthorized modification of Office products from being installed in the institution, the software should be checked for integrity and authenticity prior to installation. For this test, many manufacturers provide signed checksums that can be used to verify that the software has been modified exclusively by the manufacturer.

The authenticity of Microsoft Office is ensured when it is installed by the installation agent. In addition, the signature can be accessed via the file properties of the software packages under * Digital Signatures | Details * to be checked. Microsoft also offers the command line tool SignTool, which can be used to check program signatures. If Microsoft Office is kept up to date via the Windows Update mechanism, the signature is automatically checked for updates.

Several methods are available for LibreOffice to verify the integrity of software packages:

If the integrity of Office products is manually verified, the test should be on a hardened system. The integrity checking programs should be protected against manipulation.

The selected procedure for the integrity check of office products should be comprehensibly documented for third parties in a suitable place (for example in the operating manual). In the case of high demands on the integrity of Office products, it may make sense to keep the logs of the performed integrity checks.

#### APP.1.1.M2 Restricting Active Content [User]

Office products often provide the ability to add documents to Active Content. Active content includes macros that perform more complex calculations, or Active X controls that allow rich forms to be embedded in Office documents. In integrated programming environments of Office products Active Content can be developed with any complex functions.

However, Active Content is also widely used to embed malicious code into Office documents and spread it. Therefore, the automatic execution of Active Content should be prevented in the settings of the Office products.

In Microsoft Office, the handling of Active Content in the Security Center can be configured. The security center can be found at * File | Options | Security Center | Settings for the security center *. There you can configure how Microsoft Office should handle macros and Active X components.

In LibreOffice you can set options for how Active Content is handled. The security options for the macros can be found under * Extras | Options | LibreOffice | Security | Macro Security *.

Some Office products have the ability to enable digitally signed Active Content originating from trusted sources. This feature is especially useful when macros are needed in organization-owned Office documents. As a result, users are not unnecessarily often confronted with the Active Content Alert, which benefits the user.In addition, users must be made aware of the dangers of Active Content. Under no circumstances should users activate the Active Content when opening it. When in doubt, users should contact the IT Service Desk of the institution, who can work with IT to decide how to handle the documents. For example, it is possible to audit Active Content documents in foreclosed IT environments.

Active content in PDF files also creates security risks but is rarely needed. Therefore, automatic execution of such content should be disabled in the PDF viewer.

#### APP.1.1.M3 Opening documents from external sources

Office documents that originate from external sources (for example, downloaded from web pages, obtained from outside employees or business partners) must be handled with particular care. No documents may be opened that have been received unexpectedly or whose sender or origin is unknown. Basically, Office documents from external sources must be treated as executable files and at least checked for malware before being opened for the first time.

Microsoft has introduced the Open XML file format as standard with Microsoft Office 2007. Files in the Open XML file format that contain macros are marked with an "M" in the file extension. For example, Word documents with macros have the extension .DOCM instead of .DOCX. If an Office Open XML file contains macros without being marked, Microsoft Office denies opening the file (for example, if macros are included in a .DOCX file). Older document formats (such as .DOC) can always include macros and are handled by Microsoft Office 2007 or later as per Security Center settings (see APP.1.1.M2 Restricting Active Content). The following list shows Microsoft Office document types that may contain macros and should therefore be given special attention:

* .DOC
* .DOT
* .DOCM
* .DOTM
* .XLA
* .XLS
* .XLT
* .XLSB
* .XLSM
* .XLTM
* .XLAM
* .PPT
* .PPTM
* .POTM
* .PPSM
* .PPAM
* .PPA
Microsoft Office can also enable Office File Validation. It compares older Office file formats when opened against a binary schema to detect possible attacks on unknown software bugs in Microsoft Office. If the opened file does not match the known binary scheme, a warning will be issued. For more stringent security requirements, Office File Validation can be configured so that documents that fail the scan can not be opened.

The operating system, web browser, and email client should be configured to check for malicious software before opening files from external sources (such as third-party USB flash drives, website downloads, or emails) (see Module OPS.1.1.4 protection against malicious programs).

Caution is also required when dealing with less common file formats in everyday use. For example, PostScript, which is still widely used in the print environment, is a full-featured programming language in addition to a page description language that describes how information should be displayed exactly on paper or in the corresponding display programs. This can lead to problems similar to macro viruses.

#### APP.1.1.M4 Securing ongoing operations of Office products

Most Office application manufacturers provide recommendations on their websites for the secure configuration of their products and the handling of identified security vulnerabilities. These should be used. Available patches and updates should be recorded promptly.Office software and other standard software should never be started with administrator rights. Only those files should be opened directly in the applications whose origin is considered trustworthy. Before files are opened from external sources, they must be checked in advance by a current anti-virus program.

Standard software is generally not designed for a high level of security. All employees should therefore be cautioned that particularly sensitive information should not be arbitrarily processed on a standard office workstation. Some standard products offer a number of security features, but usually much less security than special security products for increased protection needs. Users should be informed about these security features and their effectiveness. First and foremost, make sure that users do not lodge themselves in false, deceptive security and that the use of these security features does not open any security gaps. Users should be informed that Office products are not suitable for any purpose.

For forwarding documents to external users, file formats should preferably be used which contain less residual information and with which the subsequent changes or partial further processing can be made more difficult. For this purpose, z. For example, PDF files that have been restricted by the security options of the creating application.

Even PDF files can contain malicious code that exploits vulnerabilities. In PDF files, functions such as program calls can be embedded, which pose a security risk to the files of the local IT system. Often, JavaScript is used for such attacks. Especially older versions of PDF applications are vulnerable to such infiltration. Often the users are lured to a manipulated website where a prepared PDF file is loaded in the background. The code hidden in the file installs malware on the user's machine. The file does not even have to be opened manually.

Anti-virus programs detect infected PDF in many, but not all, cases as attackers constantly vary the malicious code. It is therefore all the more important to regularly check the applications used for updates and to quickly install security updates.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "office products".

#### APP.1.1.M5 Selection of suitable Office products

The functions of the Office products should be based on the needs of the users. To ensure this, future users of Office products should be properly involved in the selection process. For example, it makes sense that the criteria for the selection of office products should be set up jointly by IT operations and users. For a new procurement, a market analysis by the IT department should be carried out beforehand to define a preselection.Based on the market analysis and user experience, a requirements catalog should be created to support the selection of suitable Office products among the various alternatives. The requirements can be divided into the two classes MUST requirements and DESIRED requirements. Mandatory requirements must be met by the Office product available for selection in order to get a closer look. TARGET requests are optional, but they are used to choose between several Office products in the nearer selection. TARGET requests may also be weighted to indicate the order of requirements. This allows the Office products to be selected that meet all the MUST requirements and score the most points in the TARGET requirements.

The following table shows an example analysis of the requirements analysis.

In the above example, Office Product 2 exits because a MUST requirement is not met. Office Product 1 and Office Product 3 meet all MUST requirements, with Office Product 1 getting the most extra points based on the DESIRED requirements.

The most common applications for working with PDF files are Adobe Reader and Adobe Acrobat. Malefactor developers are also oriented towards market leaders. Therefore, it may be useful to use less common PDF viewer or at least vorzuhalten to avoid acute warnings.

#### APP.1.1.M6 Testing new versions of Office products

For an orderly transfer of office products and in case of significant changes, a suitable procedure for testing and approval is required. The tests are designed to identify problems with new versions of Office products at an early stage. For the planning and implementation of tests and the approval based on them, the following levels are usually to be taken into account, in which other functionaries are to be included with their technical perspective:

* the professional level (represented by specialist responsible persons)
* the level of IT operations (represented by the IT manager)
* the level of information security (represented by the information security officer)
Test and review scenarios as well as criteria for the release have to be developed for all mentioned levels. Here should be considered:

* At the technical level, it must be checked if the new version of the Office product is compatible with the established work equipment (such as file formats, standard templates, forms and evaluation forms).
* IT operations should ensure that new versions of Office products can be integrated with IT infrastructure and IT operations.
* Design and operation of Office products must be compliant with the policy (guidelines, guidelines), concepts (eg crypto concept) and best practices for information security. It is especially important to ensure that the required safety functions have been implemented and are working properly.
Before performing tests, the way in which results are backed up and evaluated should be determined, in particular with regard to the repeatability of tests. It needs to be clarified what data should be recorded during and after the test.

For testing the Office products, the test cases should be defined before the test is performed. The following categories should be considered:

* Standard cases are cases with which the correct processing of the defined functionalities should be checked.
* Error cases are cases in which an attempt is made to provoke possible error messages of Office products.
* Exceptions are cases where office products exceptionally have to react differently than in standard cases. It must therefore be checked whether the program recognizes these cases as such and processes them correctly.At the technical level, test cases can be defined for each category to be tested for each category. For example, input data and expected evaluation results can be defined in advance as default cases for an evaluation sheet.

In order to carry out the test, the IT operation should provide a suitable test environment. The environment should be as close as possible to the working environment in which the Office products are used.

The tests must be carried out according to the test plan. Every action and the test results must be sufficiently documented and evaluated. In particular, when errors occur, they must be documented in such a way that they can be reproduced. The operating parameters that are suitable for later production operation must be determined and recorded for the later creation of an installation instruction.

If, during the processing of individual test contents, it becomes apparent that one or more requirements of the catalog of requirements were not concrete enough, they should be specified if necessary.

On the basis of the established decision criteria, the test results are to be evaluated, all results combined and presented with the test documentation to the test person responsible.

After completing the tests, a pilot operation of the new version of the Office products makes sense, ie use under real conditions. If real-world pilot operations in the production environment are used, a sufficient number of tests must confirm the correct and correct functioning of Office products in advance, so as not to jeopardize the integrity of the production environment. For example, the product can be installed by selected users, who then use it in real production for a certain period of time.

If incompatibilities with the institution's work equipment are detected during the test phase, it should be decided how this will be done. For this purpose, it makes sense to define error classes that can be used to determine whether the error prevents the widespread use of the new version of the Office products or whether the incompatibilities can be accepted for a transitional period. Troubleshooting should define what work item adjustments are required for the new version of the Office products. For the implementation of the changes, see Action APP.1.1.M10 End User Software Development.

#### APP.1.1.M7 Installation and configuration of Office products

To ensure a standardized installation of the Office products, an installation and configuration guide should be created, which also contains the necessary steps to adapt the configuration. The Office products should only be installed and configured according to the documented instructions on the dedicated IT systems. Ideally, the configuration is done through centralized procedures.

Deviations from the installation instructions and in particular the standard configuration specified there must always be approved and documented.

If users are to install the software themselves, at least the pilot installation should be accompanied by a selected typical user by the IT department to verify the understandability of the installation instructions. The installation instructions should be updated and improved based on the findings from the pilot installation as well as further feedback from the users.Both before and after installing software, a full backup should be performed. The first backup can be used to recover a consolidated touchdown point during subsequent installation problems. After the successful installation, a complete data backup should be carried out again so that it can be restored to the state after successful installation of the product in the event of later problems.

Since office products are usually installed in almost all workstations in an institution, it is recommended that the configuration be managed centrally. There are several options for this depending on the operating system used on the workstations:

* In the Windows environment, the uniform configuration of the Office products can generally be distributed to the workplaces by means of group policies.
* In the Mac OS and Unix environment, a single configuration can be managed with configuration management applications.
The default configuration of Office products should be periodically reviewed and adjusted as needed. The customized default configuration should then be rolled out on the institution's workstations.

#### APP.1.1.M8 Version Control of Office Products

It should be recorded which versions of Office products are installed in the institution and in which configuration they are installed. Using different versions of Office products can cause compatibility issues when editing documents and make maintenance difficult. Documenting the rolled-out versions and configurations of Office products can be very helpful in quick troubleshooting. For the overview of the configurations, a documentation of the standard configuration can be created (for example, in the Office Products Operating or Installation Guide). So only deviations from the standard configuration have to be documented separately. Each time you change the default or default configuration, the documentation should be customized. If a configuration is used that differs from the standard configuration, the deviating configuration, the reason for it and the workstation on which the deviating configuration exists should be documented.

Regular checks should be carried out to verify that the versions used correspond to the officially released standard version of the institution.

The specific design of the inventory management and controls depends on the size of the installations and the size of the institution. For example, for smaller organizations with fewer Office product installations, simple lists that are manually sampled against the actual installations of Office products can be sufficient. In larger institutions, an inventory management software makes sense, with which it is possible to carry out automated checks of the versions used.

#### APP.1.1.M9 Eliminate residual information before sharing documents [User]

Office documents can usually be enriched with a variety of meta-information. These include, for example, information about the author, the last release or the version of the document. But you can also include sensitive information. When publishing Office documents or passing them on to third parties, it is therefore necessary to remove unwanted residual information.It should be carefully considered which metadata the file should contain. Here it may be desirable, for example, to provide a file with a large number of metadata so that it can be found via search engines. But it may also make sense not to pass on metadata. For example, the name of the author should be removed if a document is to be forwarded anonymously.

Here it makes sense to provide users with a checklist that allows them to identify unwanted residual information and delete it according to a defined process.

Exemplary checklist:

Many Office products have features that make checking residual information as automated as possible, or to a certain extent, warn against existing information remaining. For more specialized reviews, additional software or in-house developments can also be used.

For example, LibreOffice can enable warnings about residual information in documents. The settings can be found under * Extras | Options | LibreOffice | Security | Security options and alerts *.

In Microsoft Office, residual information alerts can be enabled in the Security Center. Options are under * File | Options | Security Center | Settings for the security center * to find. Here you can enable alerts under Privacy Options in the Document Specific Settings area. In addition, Microsoft Office provides a review feature. This can be found under * File | Information | Check for problems | Check Document *. The review feature automatically checks for any residual information in the document and displays it in a report that also provides cleanup options. The test function should define which tests are meaningful and which adjustments can be made.

In addition, individual passages are often to be rendered unrecognizable in a document prior to its publication. Depending on the file format, appropriate methods should be used. A popular but extremely error prone method is to "blacken" text passages electronically. However, the over-painted information is easily readable in many cases. Therefore, this is absolutely necessary.

Another example of possible residual information is OLE (Object Linking And Embedding). OLE functions allow objects to be embedded in files. These are used in many Office products to provide information to other programs. For example, this can be used to embed a spreadsheet created in Excel in a Word document. This not only transfers the information shown in the table section, but also all the information contained in the Excel file to the Word file. If the Word file is then shared, the recipient can then view and even modify the Excel file, even if it was read-only or write-protected by a password. To prevent this, the table should be copied as text into the Word file in this example. Only if the source Excel file contains no information other than what you want to pass it should be embedded in another file. This can be z. B. by creating a new Excel file can be achieved.

Handling residual information in Office documents should be part of the user training. In particular, the handling of software for the automated removal of residual information should be trained, if used. Sensitization campaigns should also draw attention to the dangers of residual information.

#### APP.1.1.M10 End User Software Development [User]In Office documents, among other things, with macros in documents or calculations and cell references in spreadsheets, extensive and complex program logic can be implemented. There is a risk that such Office documents are always developed by users in specialist departments as tools, but neither a comprehensible documentation is created, nor functional tests are performed. In the worst case, self-developed macros or programs based on Office applications become indispensable tools in the department, but can no longer be maintained or even contain undetected errors.

To prevent this, management should decide to what extent such software developments are permitted by end users in the institution. The decision should include the protection needs of the data to be processed. So it may make sense to define a protection requirement limit up to which the data can be processed in self-development. If the protection requirement of the data exceeds this limit, in-house developments must be migrated to solutions managed centrally by the IT operation.

If in-house developments are allowed in principle, it should be defined how they are to be documented and tested and which quality requirements apply to in-house developments in the form of office documents or tools. For this purpose, it is advisable to record the in-house developments per department in a catalog or a list and to name a responsible person and representative for each application / office tool. This person responsible is responsible for the adherence to the quality requirements as well as care, documentation and testing of his tools. For more information about Office product testing, see APP.1.1.M6 Testing New Versions of Office Products.

#### APP.1.1.M11 Regulated use of extensions for Office products

Many office product can be customized with extensions to the needs of the institution. These extensions can not be used without the associated Office products, but due to their complexity, they are proprietary software products. Therefore, deployed extensions as well as the Office products themselves must be used in a controlled manner. Which includes:

* Regulated selection of suitable extensions
* Obtain extensions from official sources
* If possible check the checksums or the signatures of the extensions during the installation
* Patch management of the extensions
* Documentation of the configuration of the extensions
* Testing the extensions for compatibility with the deployed versions of Office products
Special focus is on testing the extensions for compatibility with the version used. It should be noted that the development cycles of Office products and their extensions differ, so new versions of the extensions may appear much more frequently than there are new versions of the Office products.

Extensions testing should be performed on isolated test systems, as for the Office products, on clearly documented test procedures with result documentation. Follow the instructions for testing the software from APP.1.1.M6 Testing new versions of Office products.

In Microsoft Office, it is possible to allow only signed extensions (add-ins) from trusted publishers. This function can be activated in the security center. The function can be found under * File | Options | Security Center | Settings for the security center ... | Add-ins *.

#### APP.1.1.M12 Waiver of Cloud Storage [User]Some Office products incorporate features that make it possible to store, synchronize and share documents directly online. These features can be comfortable for the home user, but more dangerous than good for business use. For example, sensitive data can be inadvertently published if the feature is used sparingly.

All features of Office cloud document storage products should therefore be disabled.

The need to share and collaborate on documents should not be completely ignored. This usually results in users helping themselves and using unreleased software or unauthorized cloud solutions. Therefore, in training, users should be advised of the institution's ability to back up documents, share data with external parties, and use cloud services. For example, to share documents with third parties for review or editing, appropriate collaboration platforms should be used that have security features such as encrypted data storage and distribution and a suitable user and rights management system.

Microsoft Office 2013 integrates the SkyDrive cloud storage option. To disable them, make sure that the component "Microsoft SkyDrive Pro" is disabled in the installation options during installation. In addition, under * File | Options | Save * the items * "Do not show backstage when opening or saving files" * and "* Save to computer by default" *. The item * "Show additional storage locations, even if a login is required" * should be disabled. Cloud storage can also be disabled through group policy. The option "* Show SkyDrive Sign In *" in * User Configuration | Administrative Templates | Microsoft Office 2013 | Miscellaneous * to be set to "* Disabled *".

#### APP.1.1.M13 Using Viewer Functions [User]

Documents from potentially insecure sources, such as the Internet or e-mail, can contain malicious software that runs on opening. These can be both macros, as well as exploiting code of the vulnerabilities of the used Office product versions. To reduce this risk, viewers should be used.

On the one hand, these may be separate applications designed specifically for the sole purpose of displaying Office documents. However, many Office products also include a so-called protected mode, in which only a small portion of the functionality of the Office product is enabled.

Depending on the application and protection requirements, consideration should be given to which alternative is appropriate. In areas with increased security requirements, it is always recommended to use separate viewer applications.

For example, Microsoft offers downloadable viewer programs for Word, Excel, PowerPoint, and Visio in the Download Center.

The settings for the integrated protected mode can be found in Microsoft Office under * File | Options | Security Center | Settings for the security center ... | Protected View * managed. The settings should be controlled as centrally as possible via GPO. Microsoft provides Administrative Template files for each Microsoft Office version for Group Policy.

In Adobe Reader version 10 or higher (Adobe Reader X), a sandbox (or "protected mode") is integrated to counteract attacks. Therefore, users who use Adobe Reader to view and edit PDF documents should use Adobe Reader X or later and use the "Protected Mode".

#### APP.1.1.M14 Protection against subsequent changes of information [User]Many application programs provide security mechanisms to limit further handling of the created files. Since the security mechanisms of the different application programs are very different and sometimes even vary from version to version, it is important to inform employees about how to use them and what steps to take before handing over electronic documents. It often makes sense to train one employee (plus representative) thoroughly. He should then process all documents to be forwarded according to the security requirements or be available as a contact person.

In the following, some such security mechanisms are presented using the example of PDF files.

 ** Protection of PDF documents **

With Adobe Acrobat, the most popular application for creating and editing PDF files, you can assign two types of passwords. Some are needed to open the document, the others are needed to change the security attributes. When assigning a password, it first asks which program versions the protection function should be compatible with. Up to the version "Adobe 5.0 and higher", only a 40-bit encryption with RC4 is possible, from "Adobe 5.0 and higher" is a 128-bit encryption with RC4 and from "Adobe 7.0 and higher" is a 128- Bit encryption with AES provided. Care should be taken to encrypt at least 128 bits, otherwise the document protection can easily be undone.

Among other things, the following attributes can be restricted via the security attributes:

* Open the document
* To press
* Change the document
* Copy texts, images or other content
* Access to metadata of a document
* Add or change notes and form fields
Thus, the rights can be very easily limited, so that no one can cut and paste the contents of a publication. If in extreme cases even printing is prevented, the file can only be read online.

Unfortunately, this only provides rudimentary protection, since PDF files (depending on the version of the program they were created with) can also be opened with programs that ignore these security attributes. As long as z. If, for example, printing is allowed, the document can even be converted back into a PDF file at any time without any restrictions.

PDF security policies can be created. Any user can create these for themselves or use security policies specified by the institution, which requires an Adobe Policy Server.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### APP.1.1.M15 Use of encryption and digital signatures (CI)

Increased demands on the authenticity, integrity and confidentiality of Office documents should use digital signatures to ensure authenticity and integrity. In addition, the documents should be encrypted to ensure confidentiality. Crucial to the security of the signature and encryption method is the quality of the algorithm used and the key selection.

 ** High integrity requirements: **If high demands are made on the integrity of Office documents, for example to guarantee non-repudiation, digital signatures can be used. When using digital signatures that are embedded in the Office documents, it should be noted that the method used for the crypto concept (see module CON.1 Crypto concept) fits the institution. It may be necessary to extend the crypto concept with the method for signing Office documents. As a rule, an institution-wide key management must be established in order to make meaningful use of the signature functions. In addition, if users work outside of the institution with the signed documents, it must also be noted that the solution used implemented an established standard that can be used easily by other institutions.

In Microsoft Office, documents can be signed with a built-in function. This can be found under * File | Information | Protect document | Add digital signature *. This assigns the document a digital signature that can be checked when opened in Microsoft Office. In addition, it is possible to insert a signature field visible in the document. This is about * insert | Signature line * possible. To sign the document, the signer must insert his signature by right-clicking on the respective signature line in the context menu at the point * "Sign ..." *.

In LibreOffice it is also possible to digitally sign a document. Here you can find the function under * File | Digital signatures *. The digital signatures are created according to the XML Signature specification and embedded in the LibreOffice documents.

 ** High confidentiality requirements: **

Office documents with high confidentiality requirements should be encrypted during transmission. In some cases, Office products offer built-in document encryption capabilities. However, built-in encryption of Office products should not be used without prior analysis. This should ensure that the offered encryption function also fulfills the requirements of the institution (see module CON.1 Crypto Concept). Care must be taken in the planning phase to ensure that algorithms and procedures that are currently state-of-the-art are in place and can provide adequate protection for the foreseeable future. It should also be noted that, depending on the Office products used, meta information is not encrypted. If the built-in encryption capabilities of Office products do not meet the institution's requirements, alternative options should be used.

Microsoft Office documents can be accessed via the function * File | Information | Protect document | Encrypt with password * to be encrypted. Microsoft Office has been using AES with a key length of 128 bits in CBC mode since version 2007. By default, versions prior to Microsoft Office 2007 use weaker algorithms with shorter key lengths. The built-in encryption feature of these versions should therefore not be used.

LibreOffice documents can be accessed via the function * File | Properties | Security | Protect * to be encrypted. Alternatively, the option "Save with password" can be checked in the Save dialog box. LibreOffice uses AES with a key length of 256 bits in CBC mode by default in the current version. Previous versions also used Blowfish and AES with key lengths of 128 and 192 bits.

#### APP.1.1.M16 Integrity check of documents (I)Documents that require a high degree of integrity should be protected during transmission using checksums (for example, CRC, MD5 hash, or SHA hash) or digital signatures (see action APP.5.2.M15 Using encryption and digital signatures). It is important to note that only digital signatures reliably detect intentional changes.

For unintentional changes (bit errors, etc.), many Office products provide automated repair functionality that can partially recover broken Office documents. It should be noted that the ability to recover documents depends on the file format of the Office document. For example, Office documents stored in the Office Open XML format (as of Office 2007) are more likely to recover from integrity loss.

3 Further information
------------------------------

### 3.1 Worth knowing

** ** License Management
 All of the institution's IT systems must use properly licensed Office products. Therefore, the licenses of the installations should be checked regularly. It makes sense to carry out the inventory management of the software licenses as part of the version control.

Using Office products without a valid license can, in the worst case, result in fines and re-licensing costs. Therefore, an overview must be created, showing how many licenses exist for the Office products used and how many licenses have already been used. This overview also helps to plan for future licenses.

### 3.2 Literature

Additional information on threats and security measures in the "Office Products" area can be found in the following publications, among others:

*

 #### [CS004] Using and Configuring Adobe Readers X and XI

  

 Alliance for Cyber ​​Security, BSI-CS 004, version 1.10, 10.2014
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_004.html](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_004.html)

  

 
*

 #### [KB2501584] Microsoft Security Advisory

  

 Microsoft Office File Validation for Office 2003, 2007 Office, and Office 2010, 04.2011
 <Https://support.microsoft.com/de-de/kb/2501584>

  

 
*

 #### [LODS] Apply digital signatures

  

 LibreOffice, (last accessed on 05.10.2017)
 [Https://help.libreoffice.org/Common/Applying\_Digital\_Signatures/de](https://help.libreoffice.org/Common/Applying_Digital_Signatures/de)

  

 
*

 #### [LORP] Libre Office Release Plan

  

 The Document Foundation, (last accessed on 05.10.2017)
 <Https://wiki.documentfoundation.org/ReleasePlan>

  

 
*

 #### [MS35554] Office 2013 Administrative Template files (ADMX / ADML) and Office Customization Tool

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://www.microsoft.com/en-us/download/details.aspx?id=35554>

  

 
*

 #### [MS49030] Office 2016 Administrative Template Files (ADMX / ADML) and Office Customization Tool

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://www.microsoft.com/en-us/download/details.aspx?id=49030>

  

 
*

 #### [MSD10] Excel Viewer

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://www.microsoft.com/en-us/download/details.aspx?id=10>

  

 
*

 #### [MSD13] PowerPoint Viewer

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://www.microsoft.com/en-us/download/details.aspx?id=13>

  

 
*

 #### [MSD35811] Visio Viewer

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://www.microsoft.com/en-us/download/details.aspx?id=35811>

  

 
*

 #### [MSD4] Word Viewer

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://www.microsoft.com/en-us/download/details.aspx?id=4>

  

 
*

 #### [MSDN338205] Introducing the Office (2007) Open XML File Formats

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://msdn.microsoft.com/en-us/library/aa338205.aspx>

  

 
*#### [MSDN368289] Digital Signatures and Windows Installer

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://msdn.microsoft.com/en-us/library/windows/desktop/aa368289.aspx>

  

 
*

 #### [MSDN380259] Cryptography Tools

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://msdn.microsoft.com/en-us/library/aa380259.aspx>

  

 
*

 #### [MSDN387764] SignTool

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://msdn.microsoft.com/en-us/library/aa387764.aspx>

  

 
*

 #### [MSFSD] Office 2013 - I can disable the "SkyDrive" save option under Word

  

 Microsoft, (last accessed on 05.10.2017)
 [http://answers.microsoft.com/en-us/office/forum/office\_2013\_release-word/office-2013-can-i-disable-the-skydrive-save-option/e358c2e0-0c10-4251 -b1b5-aabe59407ed7] (http://answers.microsoft.com/en-us/office/forum/office_2013_release-word/office-2013-can-i-disable-the-skydrive-save-option/e358c2e0-0c10- 4251-b1b5-aabe59407ed7)

  

 
*

 #### [MSODS] Add or remove a digital signature in Office files

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://support.office.com/de-de/article/Hinzuf%C3%BCgen-oder-Entfernen-einer-digitalen-Signatur-in-Office-Dateien-70d26dc9-be10-46f1-8efa-719c8b3f1a2d>

  

 
*

 #### [MSS2488] Microsoft Support Lifecycle Office 2003

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://support.microsoft.com/de-de/lifecycle?p1=2488>

  

 
*

 #### [MSS8753] Microsoft Support Lifecycle Office 2007

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://support.microsoft.com/de-de/lifecycle?p1=8753>

  

 
*

 #### [TN179125] Plan cryptography and encryption settings for Office 2013

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://technet.microsoft.com/de-de/library/cc179125.aspx>

  

 
*

 #### [TN194021] Guide to Office 2013 Security

  

 Microsoft, (last accessed on 05.10.2017)
 <Https://technet.microsoft.com/en-us/library/dn194021.aspx>

  

 
*

 #### [TN797428] File format reference for Word 2013, PowerPoint 2013, and Excel 2013

  

 Microsoft Technet, (last accessed on 05.10.2017)
 <Https://technet.microsoft.com/de-de/library/dd797428.aspx>

  

 
*

 #### [TN857087] Plan Protected View Settings for Office 2013

  

 Microsoft Technet, (last accessed on 05.10.2017)
 <Https://technet.microsoft.com/en-us/library/ee857087.aspx>

  

 
*

 #### [XMLDSIG] XML Signature Syntax and Processing (Second Edition)

  

 W3C, (last accessed on 05.10.2017)
 <Https://www.w3.org/TR/xmldsig-core/>