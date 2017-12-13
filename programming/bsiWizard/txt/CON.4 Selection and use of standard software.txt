1 description
--------------

### 1.1 Introduction

Standard software is understood to mean software that is offered on the market and is usually obtained from specialized dealers, for example via catalogs or online portals. It is characterized by the fact that institutions can install them themselves and adapt them with little effort.

This module shows how institutions should deal with standard software from a security point of view. For example, institutions must be able to create a standard software requirement catalog, select a suitable product, install it safely, manage licenses appropriately, and safely uninstall the product.

### 1.2 Objective

The module systematically identifies the protective measures to be taken so that standard software can be safely planned, procured, operated and rejected. The ultimate goal is to protect the information processed with the standard software.

### 1.3 Delimitation

This module deals exclusively with standardized programs, which are designed so that they can be used and adapted by the user independently without the support of the manufacturer or external service providers.

This module does not deal with software tests and releases. Requirements are listed in * * OPS.1.1.6 * Software Tests and Permissions *. The software development is not discussed. For this purpose, the requirements of the module CON.4 * Software Development * should be considered separately *. *

Details of the sorting out are considered in more detail in the module * OPS.1.2.7 Sale / Disposal of IT *. Further requirements for cloud applications are regulated in the blocks OPS.2.2 * Cloud usage * and * * APP.5.3 * Cloud applications from the client point of view *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the * standard software * area:

### 2 1 Lack of adaptation of the standard software to the needs of the institution

If purchased standard software is not adapted to the requirements of the institution, the internal operation can be significantly disturbed. Formats could z. B. not be compatible with already used programs or new product could have too little functionality. This can lead to performance losses, disruptions or errors within the business processes.

### 2 2 Disclosure of information worthy of protection due to incorrect configuration

Is a standard software configured incorrectly, eg. If, for example, unneeded functions are still activated, unintentionally information worthy of protection can be disclosed. This can lead to financial losses or reputational damage. In addition, the institution could also violate applicable law, eg. For example, if personal information is disclosed.

### 2 3 Obtaining standard software and updates from unreliable sources

If standard software or related updates are obtained from unreliable sources, the integrity and functionality of the software can not be assured. This also applies to extensions (* plug-ins * or * add-ons *). The installation of compromised software may result in malicious code being distributed in the institution and that the software may not work as intended. In addition, the integrity and availability of IT systems may be compromised.

### 2 4 Manipulation of data by users

The data used in standard software can be manipulated in a variety of ways by users, e.g. For example, if you incorrectly or incorrectly record data incorrectly, change the content or simply delete data. As a result, all specialized processes in which the corresponding application is used are affected. Failure to detect the manipulated data will result in processing of corrupted information. In addition, security holes can be created that attackers can exploit.### 2 5 Software vulnerabilities in standard software

Despite intensive testing, not all vulnerabilities and defects in standard software are usually discovered before they are delivered to customers. If these are not detected in time, resulting crashes or errors can lead to far-reaching consequences. In addition, the confidentiality and integrity of the stored data and the availability of affected IT systems may be affected. Software vulnerabilities or errors can also lead to serious security vulnerabilities in standard software. These can sometimes be exploited by attackers to inject malicious code.

### 2 6 Use of non-licensed standard software

If standard software without a valid software license is used, because, for example, the license volume has been exceeded unnoticed, this can result in contractual penalties. Conversely, if standard software is installed on workstations where it is not needed, the license fee may be overpaid.

### 2 7 Unauthorized exercise of rights in standard software

Access, access and access rights are used as organizational measures to protect information, business processes and IT systems from unauthorized access. If unauthorized persons use standard software or certain functions, this may endanger the confidentiality and integrity of the information by altering, deleting or creating it improperly. Such vulnerabilities arise, for example, through incorrect rights. Affected business processes can be corrupted, inadvertently process erroneous information or disclose sensitive information.

### 2 8 Data loss due to incorrect use of standard software

Incorrect use of standard software may allow employees to accidentally delete or modify data in a way that makes it unusable. This can block entire business processes. Incorrect use of encryption features may result in the data still being available but no longer being decrypted. In this case, the data can no longer or only with increased effort to be restored, which can lead to an additional financial burden on the institution.

3 requirements
---------------

Specific requirements for the protection of * standard software * are listed below. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### CON.4.A1 Ensure the integrity of standard software

When installing standard software, you MUST ensure that it is an original unmodified software program. It MUST be installed either from original media or from verified identical copies of the original installation program. Access to the installation routines MUST be restricted to authorized employees. The original media or installer MUST be scanned for malware. Backup files SHOULD be created and checked.

#### CON.4.A2 Development of the installation instructions for standard software

An installation instruction MUST be created for the selected standard software. Also suitable parameters for the configuration as well as organizational conditions for the installation of the software MUST be specified.#### CON.4.A3 Secure installation and configuration of standard software

Approved standard software MUST be installed and configured to adhere to the appropriate installation instructions (see CON.4.A2 * Development of standard software installation instructions *). If these instructions are deviated, this MUST be approved by the supervisor. All installations MUST be performed by IT operations. It MUST be ensured that only the required program functions are installed.

The software MUST be configured to comply with the institution's security policies. Unnecessary services and features MUST be uninstalled. If this is not possible, they MUST be turned off. Before and after standard software has been installed, data backups should be performed by all participating IT systems.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​selection and use of standard software. They SHOULD be implemented in principle.

#### CON.4.A4 Definition of responsibilities in the area of ​​standard software [department]

For the introduction of a standard software, the responsible persons SHOULD be named. It should at least be determined who creates a requirements catalog, selects the product, tests and releases it and who is ultimately responsible for the installation. In addition, an introduction and approval process SHOULD be defined. For the operation of standard software, technical and technical product managers SHOULD be named.

#### CON.4.A5 Creation of a requirement catalog for standard software [department]

Before purchasing a standard software, a catalog of requirements SHOULD be created, which includes not only functional but also safety requirements. In addition, the program requirements of the technical and IT departments SHOULD be raised. The finished catalog of requirements SHOULD be coordinated with all affected specialist departments.

#### CON.4.A6 Selection of suitable standard software [department, procurement office]

Based on the requirements catalog (see CON4.1.A5 * Creation of a standard software catalog *), the products available on the market SHOULD be viewed and compared using a rating scale. Thereafter SHOULD investigate whether the shortlisted products really meet the institution's requirements. If there are several product alternatives, additional costs should also be taken into account, eg. For training or migration. Ultimately, the procuring entity, together with the head of the requesting department and IT operations, should select a suitable software product based on the ratings and test results.

#### CON.4.A7 Verification of Delivery of Standard Software [Department]

It SHOULD be checked if new software products were delivered completely and correctly. It should at least be checked whether the delivery was ordered, for whom it is intended and whether all the necessary components are present. Also pure download software including associated license files or keys SHOULD be checked accordingly. The results of the review SHOULD be documented. Thereafter, all delivered products and licensing information SHOULD be provided with unique identifiers and included in an inventory.

#### CON.4.A8 License management and version control of standard softwareLicensed standard software products used on the institution's IT systems SHOULD be licensed. To ensure this, the installed program versions and the licenses SHOULD be checked regularly. For this purpose, appropriate lists, databases or special license management programs should be used. The stock lists for the licenses SHOULD always be up to date. In addition, the different configurations of the installed standard software SHOULD be documented.

#### CON.4.A9 Uninstalling standard software

When uninstalling standard software, all files created to run the software on the IT system SHOULD BE removed. Also, all entries in system files made for the product SHOULD be deleted. In order to be able to completely uninstall standard software, the system changes made during installation SHOULD be documented either manually or with appropriate programs.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### CON.4.A10 Implementation of Additional Security Features (CIA)

It SHOULD be checked whether the safety functions of the operated standard software are suitable for increased protection requirements. If this is not the case, suitable functions SHOULD be implemented to ensure operation.

In principle, however, an increased protection requirement should already be considered when the requirements are defined and the product is selected.

#### CON.4.A11 Use of certified standard software (CIA)

When procuring standard software, it should be determined whether an assurance of the manufacturer, distributor or supplier can be recognized as sufficiently trustworthy via implemented security functions. If this is not the case, certification of the Common Criteria application should be considered as a decision criterion. If several products are available for selection, security certificates SHOULD be taken into account, in particular, if the evaluated scope of functions includes the minimum functionality (as far as possible) and the mechanism strength meets the protection requirements. If there is no suitable and certified product on the market, the application environment of the standard software SHOULD be protected according to a high protection requirement.

#### CON.4.A12 Use of encryption, checksums or digital signatures (CI)

If data with increased protection requirements are transmitted or stored, they SHOULD be encrypted beforehand. Is there a built-in encryption function in a standard software, SHOULD it be checked if it is sufficiently secure. This SHOULD be checked especially for older product versions. Users SHOULD be trained and sensitized in handling the encryption functions.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and safety measures in the area "selection and use of standard software" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [CC] Common Criteria for Information Technology Security Evaluation (CC)published in the series of standards ISO 15408: Information technology- Security techniques- Evaluation criteria for IT security, Version 3.1, (last accessed on 28.09.2017)
 <Www.commoncriteriaportal.org>

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
* #### [TR02102] Cryptographic method recommendations and key lengths

  

 BSI, (last accessed on 27.09.2017)
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "Selection and Use of Standard Software".

* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.22 Manipulation of information
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.