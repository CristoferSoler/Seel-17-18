Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Standard software is understood to mean software that is offered on the market and is usually obtained from specialized dealers, for example via catalogs or online portals. It is characterized by the fact that the user can install it himself and adapt it with little effort.

These implementation notes for the relevant module show how institutions should deal with standard software in terms of security. For example, institutions must be able to create a standard software requirement catalog, select a suitable product, install it safely, manage licenses appropriately, and safely uninstall the product.

### 1.2 Life cycle

** planning and conception **

In the planning and design phase, an employee responsible for procuring the standard software should be named (see CON.4.M4 * Definition of responsibilities in the area of ​​standard software *). The requirements for the standard software to be procured should be analyzed and recorded in a requirements catalog (CON.4.M5 * Creation of a requirements catalog for standard software *). Then a suitable product can be selected (CON.4.M6 * Selection of a suitable software product *). In the case of increased protection requirements, it should also be decided whether and how an application to be procured should be certified in order to demonstrate a certain level of security (see CON.4.M11 * Use of certified standard software *).

**Procurement**

When procuring standard software, it should be defined how their deliveries are handled. For each delivery, it should be checked to see if it is complete (see CON.M7 * Verification of Delivery of Standard Software *).

**Implementation**

Before using standard software, ensure that the integrity of the installation software is guaranteed (see CON.4.M1 * Ensuring Integrity of Standard Software *). In addition, standard software should be securely installed and configured afterwards (see CON.4.M3 * Secure installation and configuration of standard software *). For each application an installation instruction has to be created (see CON.4.M2 * Development of the standard software installation instructions *).

**Business**

It should be ensured that only licensed standard software is used (see CON.4.M8 * License Management and Version Control of Standard Software *). In case of increased protection requirements, additional safety functions should be implemented if necessary (see CON.4.M10 * Implementation of additional safety functions *). Encryption, checksums or digital signatures should also be used (see CON.4.M12 * Use of encryption, checksums or digital signatures *).

** ** segregation

If standard software is uninstalled, it should be ensured that all (system) files of the application are deleted (see CON.4.M9 * Uninstallation of standard software *).

2 measures
-----------

The following are specific implementation notes in the section "Selection and Use of Standard Software".

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### CON.4.M1 Ensure the integrity of standard software

It is to be ensured that released standard software is only installed from the original data media or from verified identical copies of the original installation program. This is to prevent that intentional or unwanted changes can be made, for. Due to malware, bit errors due to technical errors or manipulated configuration files.
The installation must therefore be carried out exclusively from original data media or verified identical copies of the original installation program. Alternatively, a released version can be installed over a local area network. It should be ensured that only authorized persons can access it.

Backup copies should be made and checked from the original media. Original media and all copies must be kept secure from unauthorized access. The copies made should be numbered and included in inventories. Copies that are no longer needed should be deleted or destroyed. Also, original media and original installers must be checked for malicious software before first use.

Optionally, a checksum can be created via the original data carriers or via a reference version installed during the test. Based on this, the integrity of the media used for this or the versions stored in local networks or the correct installation can be checked prior to installation. In addition, installed programs can be provided with checksums in addition to protection against unauthorized changes to the shared configuration. In this way, even infections with previously unknown malware can be detected. It can also be determined if a virus infection occurred before or after installation.

#### CON.4.M2 Development of the installation instructions for standard software

After the institution has decided on a product, an installation instruction has to be created. During testing, the configuration of the product was determined that allows a safe and efficient production operation (see CON.4.M6 * Selection of suitable standard software *). This should ensure that the software works in a user-friendly, orderly and safe manner at the workplace.

In order to ensure the appropriate configuration of the product in productive operation, certain parameters must be specified. Partly this must be accompanied by organizational regulations.

For some properties of a product, the following example shows what can be specified in an installation instruction.

**Example:**

User friendliness:

* The product must be installed with the appropriate drivers to create a work environment acceptable to the user, such as: B. screen flicker-free, sufficient pressure preparation.
* Settings where the functions have the highest processing speed are preferable, unless other criteria such as security speak against it (example: a backup should be verified, although the verification requires extra time).
Safety:

* The parameters for safety functions must be preset, eg For example, the minimum length of passwords or the daily creation of backups.
* If multiple security-related procedures are supported (eg encryption algorithm, hash functions), select those that will provide adequate levels of protection.
Function:

* Only the required program functions must be activated, unwanted or unneeded functions must be switched off.
* The automatic storage function is to be activated with the parameter "every x minutes".
Organization:

* Only an administrator is allowed to install the software.
* Regulations must be issued for the operation, eg. B. Data backups are to be carried out independently by the user, passwords must be changed after x days.
Boundary conditions:

* The configuration of the platform on which the standard software product is to be used must be described and specified, in particular, if system-related weaknesses of the platform are thereby eliminated.
#### CON.4.M3 Secure installation and configuration of standard software

The standard software should be installed on the intended IT systems according to the installation instructions (see CON.4.M2 * Development of Standard Software Installation Instructions *). In addition to the programs to be installed, the installation instructions also contain configuration parameters and the setup of the hardware and software environment.

Deviations from the installation instructions must be approved by the supervisor or the person responsible for the approval process.

Since standard software is developed for many fields of application, it usually contains more functions than are required for the specialized tasks. To reduce the number of problems and errors, only the functions actually required may be installed. Functions that can lead to security problems must not be released.

Both before and after installing software, a full backup should be performed. The first backup can be used if errors occur during installation. The second backup will restore the condition after successful installation of the product in case of later problems.

The successful installation must be reported to the responsible body for productive operation.

When using a new product, it may be necessary to migrate databases that were created with a predecessor product. If the tests have shown that this can lead to difficulties, assistance should be provided to the users. Alternatively, trained personnel can centrally migrate the old data.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "selection and use of standard software".

#### CON.4.M4 Definition of responsibilities in the area of ​​standard software [department]

Before the introduction of standard software, a number of responsibilities have to be B .:

* Who creates a requirements catalog?
* Who chooses products?
* Who tests? Who is responsible for the release?
* Who installs the software?
Below is shown how these responsibilities can be meaningfully distributed. However, because the terms in most institutions differ from each other, some instances are defined in advance according to their tasks, to which the individual responsibilities can then be assigned:

* The department is the user of the standard software. He expresses the need for new software and thus initiates the procurement process. He will be involved in pre-selection and testing to meet the needs of the users.
* The management of the institution is responsible for releasing standard software. This responsibility is usually delegated to the head of the department. After approval, responsibility for the correct use of the standard software is transferred to the specialist department.
* The task of IT is to provide IT solutions that enable departments to do their jobs. He also has to ensure the safe and reliable operation of IT.
* The procuring entity must ensure that the standard software is interoperable and compatible. She also has to ensure that house standards and legal regulations are adhered to. Often there are IT coordinators in the individual departments who consult parts of the tasks of the procurement office for the specialist department and possibly also coordinate the budget of the department.
* The budget is responsible for accounting, IT budget management and budget allocation.
* The IT security officer must check whether the products used or to be procured ensure an adequate level of security. As part of security management, he must ensure information security during ongoing operations.
* The data protection officer must ensure that the data protection regulations are adhered to and that personal data are sufficiently protected.
* In many cases, the Personnel / Works Council must be involved in the selection of new standard software, especially if there are major changes in the workflow or if the software to be procured is suitable for performance control.
In the overall process "standard software", it must be determined for each individual step which of the instances described above are responsible for the execution and which instances have to be involved. The following table shows how responsibility can be meaningfully distributed.

The assignments made are binding and it must be checked regularly whether they are complied with.

#### CON.4.M5 Creation of a requirement catalog for standard software [department]

The market usually offers many similar standard software products. Comparable in their basic function, however, they differ in criteria such as acquisition and operating costs, additional functions, compatibility, administration, ergonomics and information security.

** list of requirements **

For the selection of a suitable product, therefore, first a catalog of requirements should be created, the z. B. statements on the following points may contain statements:

* Functional requirements that the product must meet in order to properly support the specialist department. The functions relevant for the specialist task should be highlighted. Example:

 
+ Word processing with the additional functions: integration of graphics, macro programming, spell checking and hyphenation. Macro programming must be disabled, spell checking must be available in English, French and German. The specified text formats must be imported and exported.


 
* IT Deployment Environment: This is described on the one hand by the constraints imposed by the existing or planned IT deployment environment and, on the other, by the performance requirements that the product places on the deployment environment. Example:

 
+ Required IT deployment environment and performance requirements: Operating system, processor, memory, disk space, external disk interfaces, and networking.


 
* Compatibility requirements to other programs or IT systems, ie migration support and upwards and downwards compatibility. Example:

 
+ The functions A, B, C must be retained when changing versions.


 
* Performance requirements describe the required performance in terms of throughput and runtime behavior. For the required functions as accurate as possible information on the maximum allowable processing time should be taken. Example:

 
+ Other simultaneously processed processes may not be slowed down by more than 30% by the product.


 
* Interoperability requirements, d. H. Collaboration with other products across platforms must be possible. Example:

 
+ A word processor should be available for Windows, Unix, and macOS platforms. Documents should be able to be created on one operating system and further processed on another.


 
* Reliability requirements concern the stability of the product, ie fault detection and tolerance as well as failure and operational safety.

 
+ Incorrect entries of the user must be recognized and must not lead to program termination or system crash.
* Conformity to standards, which may be international standards, de facto standards or even house standards. Example:

 
+ The product must comply with the EU Screen Directive 90/270 / EEC.


 
* Compliance with internal regulations and legal regulations. Example:

 
+ Since personal data are processed, the provisions of the Federal Data Protection Act must be able to be fulfilled with the available functions.


 
* Usability requirements characterized by ease of use, comprehensibility and learnability, in particular the quality of the user interface and the quality of the user documentation and help functions. Example:

 
+ The user interface must be designed so that unskilled workers can be briefed on their use within two hours.


 
* Requirements for the maintenance arise for the user mainly from the error handling of the product. Example:

 
+ The administration effort must not exceed X hours per month.


 
* The upper limit for costs. Not only the direct procurement costs for the product itself must be included, but also follow-up costs, such. As an upgrade of the hardware, personnel costs or necessary training.
* Documentation requirements must state which documents are required in which quality (completeness, comprehensibility) .Examples:

 
+ User documentation must be easy to understand and self-paced. The entire functionality of the product has to be described.


 
* With regard to software quality, requirements can be set that range from manufacturer declarations to the quality assurance procedure used, ISO 9000 ff. Certificates and independent software tests in accordance with ISO / IEC 25051. Example:

 
+ The manufacturer's software manufacturing process must be ISO 9001 certified.


 
* If security tasks are to be fulfilled by the product itself, these must be formulated in the form of safety requirements. This will be explained below.
** ** safety requirements

Typical safety requirements that a product can fulfill are briefly explained below. Further details can be found in the Common Criteria (CC).

* Identification and Authentication: To many products, there will be requirements to identify and monitor those users who have access to the product. In addition to verifying the identity of the user, it is important to verify that the user is actually the person he claims to be. This is done by providing the product with information that is permanently linked to the user.
* Access Control: For many products, it will be necessary to ensure that users are prevented from accessing information that they do not have access to or do not want to access. It may also be necessary to prevent users from creating, modifying or deleting information without authorization.
* Preservation of evidence: For many products, it must be ensured that users' actions are recorded. Thus, the consequences can later be assigned to the user in question and the user can be made responsible for his actions.
* Log Evaluation: For many products, it will be necessary to ensure that sufficient information is recorded about both normal and exceptional occurrences so that it can later be determined whether security breaches actually occurred and what information or other equipment was affected.
* Unadulterability: For many products, it will be necessary to ensure that certain relationships between different data remain correct and that data is transferred between individual processes without modification. In addition, functions must also be provided which allow the transfer of data between individual processes, users and objects to detect or prevent losses, additions or changes, and which make it impossible to determine the alleged or actual origin or destination of the data Change data transfer.
Reliability: For many products, it will be necessary to ensure that time-critical tasks are performed at the exact time it is needed, not sooner or later. It will also be ensured that non-time-critical tasks can not be converted into time-critical ones. Similarly, for many products, it will be necessary to ensure that access is possible at the required moment and resources are not unnecessarily requested or retained.
* Transmission security: This term covers all functions intended to protect the data during transmission via communication channels: authentication, access control, data confidentiality, data integrity, transmission and receipt verification. Some of these functions are realized by means of cryptographic methods.
In addition, further security requirements for standard software can be specified.

* Data backup: The availability of the data processed with the product is subject to special requirements. This includes features integrated into the product that are designed to prevent data loss, such as: For example, automatically saving intermediate results or automatically creating backup copies before major changes are made.
* Encryption: For many products, it will be necessary to encrypt user data before transmission or after processing and to decrypt it after receipt or further processing. For this purpose, a recognized encryption method is to be used. It must be ensured that the parameters required for decryption (eg keys) are suitably protected.
* Data Integrity Features: Data that may cause loss of integrity can use features that detect or remediate errors through redundancy. In most cases, integrity checking methods are used that can reliably detect whether a product or the data created with it has been deliberately manipulated or data has been restored without authorization.
* Data protection requirements: If the product is intended to process personal data, additional special technical requirements must be made in addition to the aforementioned security functions in order to comply with data protection regulations.
Security functions are implemented by mechanisms. Depending on the intended use, these mechanisms must have different strengths, with which they can ward off attacks. The required strength of the mechanisms must be specified in the catalog of requirements. Applying the Common Criteria (CC) assesses the attack resistance of an IT product operating in a particular deployment environment. Criteria for the evaluation are the threats defined in the security specifications or in a protection profile of the data objects to be protected. The required test depth includes the specification of the attack resistance and depends on the protection requirement and the intended use of the product. The test depth is determined by means of a catalog (see CC, Part 3) mostly by means of predefined evaluation levels (EAL 1 to 7).
For attack resistance assessment, state-of-the-art attacks relevant to the mission scenario are analyzed to a certain strength, taking into account the attacking time required, technical expertise of the attacker, knowledge of the product, opportunity to attack, and resources required. The confirmation of the attack resistance in the course of the certification then takes place in the gradations low (basic), extended (enhanced basic), medium (moderate) and high (high). Basic means protection against publicly known attacks and against attackers with very limited capabilities and capabilities. High means that a successful attack requires very good expertise, product knowledge, opportunities and resources, and is therefore considered extremely burdensome overall.

#### CON.4.M6 Selection of suitable standard software [department, procurement office]

In order to be able to select a suitable software product, the IT department, in cooperation with the procuring entity, must first carry out a market analysis based on the requirements catalog (see CON.4.M5 * Creation of a requirements catalog for standard software *) and prepare it as tabular as possible. In this table statements must be made for the eligible products in the list of requirements.

The market overview should be compiled using product descriptions, manufacturer statements, trade journals or dealer information. Alternatively, an invitation to tender is possible and in some cases predetermined. The basis for this is the requirements catalog, so that a comparable market overview can be drawn up based on the incoming offers.

Subsequently, the products included in the market overview must be evaluated. For this purpose, a rating scale should be developed. Based on the available information it is now determined which of the required properties has the product. Lack of mandatory properties, it must be discarded. By evaluating the individual properties of each product, a sum is formed. As a result, there is now a ranking list of eligible software products.

The following table shows an example of such a procedure. The properties required and evaluated in the requirements catalog for a compression program are weighted as follows:

As a result, it shows that product 3 falls out because a necessary property is missing. Otherwise, the list is headed by Product 2, followed by Products 1 and 4.

The list drawn up must be presented together with the market overview of the procuring entity so that it can check to what extent the products listed there comply with internal regulations and legal requirements. In doing so, the procuring entity must also ensure that the other bodies whose specifications must be adhered to, such as the data protection officer, the IT security officer or the personnel or works council, are involved in good time.

It has to be decided how many and which candidates should be tested. It makes sense to select the first two or three candidates and then test whether they actually meet the key criteria of the catalog of requirements. This is especially important for the necessary requirements. Test licenses should be obtained for this purpose and tests should be carried out as described in module * * OPS.1.1.7 * Software tests and approvals *.

In addition to the criteria of the catalog of requirements, the following points should also be taken into account for the decision:

**Credentials**

If the manufacturer or distributor can provide reference installations for his product, the experiences made there can be questioned and included in the product assessment.
If external test results or quality statements are available for the software product being tested (eg test results in professional journals, conformity tests according to proprietary standards, tests and certificates according to relevant standards and standards such as ISO 9001), these results should also be taken into account in the selection.

** Dissemination rate of the product **

With a high level of penetration, the individual user usually has little or no influence on the manufacturer of the product when it comes to troubleshooting or implementing certain functions. But he can rather assume that such a product will be developed continuously. In some cases there are external tests commissioned by the manufacturer or carried out by specialist journals. For high-penetration products, there is generally more knowledge about vulnerabilities, so the user can assume that the major vulnerabilities are already known, or that knowledge about vulnerabilities is quickly disseminated and closed soon after they become known.

With a low penetration rate, a user may have more influence on the manufacturer. However, external tests are often not available because they are too expensive and too expensive for products from small manufacturers. Low-penetration products usually contain no more or less vulnerabilities than those with high levels of prevalence. Disadvantage here is that they may not be known so quickly and thus can be fixed. When it comes to security holes, they are unlikely to be known to potential attackers or worthwhile targets.

** Cost-effectiveness / costs for purchase, operation, maintenance, training **

Before deciding on a product, the question should always be whether the cost of the product is commensurate with the benefits that can be achieved. In addition to direct acquisition costs, all subsequent costs for operation, maintenance and training are to be included in the bill. For example, it must be clarified whether the IT infrastructure needs to be upgraded or whether training is required for installation and operation.

After completion of all tests, the test results must be presented to the procuring entity. The decision on a product should be made by the procuring entity with the participation of the requesting department and the IT department based on the test results. Also, the purchase price and additional features of the products that were not listed in the catalog of requirements, but still make sense for the use, should be taken into account in the decision.

#### CON.4.M7 Verification of Delivery of Standard Software [Department]

Upon receipt of a delivery, it shall be verified on the basis of the available documentation,

* whether the delivery was ordered,
* for whom she is destined
* whether transport damage can be detected and
* whether it is complete, that is, whether on the one hand all ordered components and on the other hand all components belonging to the scope of delivery of the product according to the product description are present.
The results of these tests are to be documented in a goods receiving directory together with:

* Product name and version,
* Product Type,
* Scope of delivery, ie description of the individual components including number and delivery form (for example book, data carrier),
* Delivery date,
* Delivery type,
* who received it,
* Repository and
* to whom it was passed.
After that, the delivered products must be passed on to the IT department to perform functional testing and formally release, install, and configure the product.
If the products are used only temporarily or made available (for example, for a test), at least the serial number and other product-specific identification features must be noted in corresponding inventories. If the delivered products are to be used permanently, they must be marked with unique identification features (eg grouped consecutive inventory numbers). Then they have to be added to an inventory. This must be able to provide information about:

* Identification features,
* Procurement sources, delivery times,
* Stay,
* Release date,
* Installation date and configuration specifics and
* Maintenance contracts, maintenance intervals.
#### CON.4.M8 License management and version control of standard software

Without proper version and license control, experience has shown that an IT system or within an organizational unit quickly uses different software versions, some of which may be used without a license.

All IT systems of an institution may only use licensed software. This regulation must be communicated to all employees. The administrators of the various IT systems must ensure that only licensed software is used. To do this, they must be equipped with suitable tools for license control and trained in dealing with them.

Often, an institution uses different versions of an application. Through a license check it must be possible to get an overview of all used software versions. This should ensure that old versions are replaced with newer ones as soon as necessary and that all versions are deleted when licenses are returned.

In addition, the different configurations of the installed software should be documented. Thus, it must be possible to get an overview of which IT system which security-relevant settings of a product specified by the release and which were actually installed. This can be used, for example, to quickly clarify to which clients macro-programming has been installed for a particular product and which not.

In order to prevent licenses from being invalidated in case of hardware defects, hardware-independent licenses should be used. This allows an IT system to be replaced with less effort if the hardware fails. If this is not possible, appropriate precautions must be taken for failure, such as agreements with the manufacturer regarding a license transfer.

If it is necessary to activate a product online through a manufacturer's licensing server, the license may subsequently expire and the product may be deactivated. If possible, products should be chosen that do not have to be activated online. Again, precautions are to be taken for a failure.

If feasible and economically viable, perpetual licenses should be preferred. This can be used to prevent a functional restriction if the license has expired or the system time deviates significantly.

#### CON.4.M9 Uninstalling standard software

When uninstalling standard software, the specifications of block OPS.1.1.8 * Deleting and destroying data * must always be observed. In addition, there are some special features.

When uninstalling software, remove all files created to operate the software on the IT system. Also, all entries in system files made with respect to the product must be deleted. Many software products create files or modify existing files in various directories on the IT system during installation. As a rule, the user is not informed about all changes made to the IT system.
In order to completely uninstall standard software, it is helpful to document the system changes made during installation either manually or using special tools. Otherwise, a product may not be completely uninstalled.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### CON.4.M10 Implementation of Additional Security Features (CIA)

Sometimes it is necessary to use and possibly implement security functions such as access control, access rights management and verification or logging in addition to the standard software itself:

* If the logging options of the IT system including additional security products are not sufficient to ensure sufficient evidence, they must be implemented appropriately.
* If the granularity of the access rights of the IT system including additional security products is insufficient to ensure proper operation, access rights management and control must be implemented.
* If the IT system, including any added security products, does not allow the administrator to access certain data, or at least to log and control that access, additional security features must be implemented as needed. For example, encryption of the data can prevent the administrator from reading this data in plain text if he does not have the associated key.
These additional requirements for standard software must be taken into account in the planning and the selection, as subsequent implementation is usually uneconomical or not easily possible.

#### CON.4.M11 Use of certified standard software (CIA)

In the case of a high protection requirement, the trustworthiness of standard software with regard to information security can only be ensured by independent testing institutes examining and evaluating the products. Based on this, a certificate can then be issued.

** Certification of products **

A generally accepted basis for the evaluation and certification of products has been the harmonized "Criteria for the Assessment of the Security of Information Technology Systems (ITSEC)" since 1991, and since 1998 the "Common Criteria for the Assessment and Assessment of the Security of Information Technology" adopted worldwide, shortly Common Criteria (CC). In Germany, the BSI carries out such certifications. If the evaluation result is positive and the ITSEC framework or the Common Criteria are complied with, the BSI will issue a safety certificate for the product under investigation.
The associated certification document indicates which function was examined with which test depth and which evaluation was performed. The test depth ranges from evaluation level E 1 (lowest test depth) to evaluation level E 6 (highest test depth) for the ITSEC or from trustworthiness level EAL 1 (lowest test depth) to trustworthiness level EAL 7 (highest test depth) for the CC. In this case, the evaluation level E 1 of the ITSEC roughly corresponds to the trustworthiness level EAL 2 of the CC, etc. In addition, the tested mechanism strength of the implementation of the security functions is specified, which represents a measure of the effort required to overcome the security functions. ITSEC and CC distinguish here the mechanism strengths low, medium and high. In addition, instructions are given as to which boundary conditions must be observed when using the product.

If several products with a reasonable price / performance ratio are available for IT procurement, only those with a security certificate should be considered. In this case, security certificates should be taken into account, in particular, if the evaluated scope of functions includes (as far as possible) the minimum functionality and the mechanism strength meets the protection requirement. The higher the level of verification specified in the certificate, the more confidence in the effectiveness and correctness of the security functions can be placed on the product.

** Overviews of certified products **

The certification bodies regularly issue overviews of which products have received a certificate. A compilation of BSI-certified IT products can be found on the BSI website. The BSI also publishes newly issued certificates in the journal <kes> - The Journal for Information Security. This information can also be retrieved from the BSI website.

#### CON.4.M12 Use of encryption, checksums or digital signatures (CI)

When confidential or high-integrity information is transferred, a cryptographic process should be used to protect the data for transport or transmission.

** Confidentiality protection by encryption **

The decisive feature of an encryption method is the quality of the algorithm as well as the key selection. A recognized algorithm is, for example, the Advanced Encryption Standard (AES).

In order to ensure the confidentiality of the information to be transmitted, the sender's and the recipient's IT systems must adequately protect access to the encryption program. If necessary, this program should be stored on a removable medium, usually kept locked and only played back when needed and used.

** Integrity protection through checksums, encryption or digital signature formation **
If only the integrity of the data to be transmitted is to be ensured for the exchange of data, a distinction must be made as to whether protection should be provided only against accidental changes, such as: B. by transmission errors, or against manipulation should be realized. If only random changes are to be detected, checksum methods (eg Cyclic Redundancy Checks) or error-correcting codes can be used. In addition, protection against manipulation is provided by methods which generate a so-called Message Authentication Code (MAC) from the information to be transmitted by using a symmetric encryption algorithm (eg Triple-DES). Other methods use an asymmetric encryption algorithm (eg RSA) in combination with a hash function and generate a digital signature. The respective generated fingerprints (checksum, error-correcting codes, MAC, digital signature) are transmitted together with the information to the receiver and can be checked by the latter.

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Further information on hazards and safety measures in the area "selection and use of standard software" can be found in the following publications, among others:

*

 #### [27001A12.1.1] ISO / IEC 27001: 2013 - Annex A.12.1.1 Documented operating procedures

  

 In particular Annex A, A.12.1.1 Documented operating procedures, (last accessed 05.10.2017)
 <Https://www.iso.org/home.html>

  

 
*

 #### [27001A12.1.2] ISO / IEC 27001: 2013 - Annex A.12.1.2 Change management

  

 In particular Annex A, A.12.1.2 Change management, (last accessed 05.10.2017)
 [Www.iso.org/home.html](www.iso.org/iso/home/standards/management-standards/iso27001.htm)

  

 
*

 #### [27001A12.6.2] ISO / IEC 27001: 2013 - Annex A.12.6.2 Restriction of software installation

  

 In particular Annex A, A.12.6.2 Restriction of software installation, (last accessed 05.10.2017)
 <Https://www.iso.org/home.html>

  

 
*

 #### [27001A8.1.1.] ISO / IEC 27001: 2013 - Annex A.8.1.1. Inventory of assets

  

 In particular Annex A, A.8.1.1 Inventory of assets, (last accessed 05.10.2017)
 [Www.iso.org/home.html](www.iso.org/iso/home/standards/management-standards/iso27001.htm)

  

 
*

 #### [27001A8.1.3] ISO / IEC 27001: 2013 - Annex A.8.1.3 Acceptable use of assets

  

 In particular Annex A, A.8.1.3 Acceptable use of assets, (last accessed 05.10.2017)
 <Www.iso.org/iso/home/standards/management-standards/iso27001.htm>

  

 
*

 #### [27001A8.1.4] ISO / IEC 27001: 2013 - Annex A.8.1.4 Return of assets

  

 In particular, Annex A.8.1.4 Return of assets, (last accessed 05.10.2017)
 <Https://www.iso.org/home.html>

  

 
*

 #### [CC] Common Criteria for Information Technology Security Evaluation (CC)

  

 published in the series of standards ISO 15408: Information technology- Security techniques- Evaluation criteria for IT security, Version 3.1, (last accessed on 28.09.2017)
 <Www.commoncriteriaportal.org>

  

 
*

 #### [ISFBA] The Standard of Good Practice - Area BA - Business Application Management

  

 in particular Area BA - Business Application Management, Information Security Forum (ISF), 06.2016

  

 
*

 #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

  

 
*

 #### [TR02102] Cryptographic Procedures - Recommendations and Key Lengths

  

 BSI, (last accessed on 27.09.2017)
[Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)
