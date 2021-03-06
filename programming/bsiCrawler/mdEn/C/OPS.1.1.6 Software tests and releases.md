1 description
--------------

### 1.1 Introduction

The use of IT for task management requires that machine data processing work as smoothly as possible, since the individual results can not be controlled in most cases. As part of the software tests, it is therefore checked whether the software in question works without errors. To do this, the software must reliably provide the required functionality and, in addition, must not have any unwanted side effects. With the subsequent release of the software by the responsible organizational unit, the basic permission is given to use the software productively in the institution. At the same time, this organizational unit assumes responsibility for the IT process that is supported by the software.

Software can be tested at different points in the life cycle of a software. Thus, software tests may already be necessary during development, before release for productive operation or in the course of patch and change management. The software tests and releases are to be carried out for in-house developments as well as for the use of standard software.

This module describes the test and release process for self-developed or customized software as well as for standard software. The test and release process is characterized by the fact that it can be run several times depending on the result.

### 1.2 Objective

By implementing this module, the institution ensures that the software used meets the technical and organizational requirements as well as the existing protection requirements of the entire institution or individual organizational units. A key aspect of this is that safety-critical software is systematically and methodically checked for existing weak points.

### 1.3 Delimitation

While the module CON.3 * Software Development * covers the software development process and the software tests that are required during the development process, this module describes the special requirements that are placed on test and release management. This test and release management does not only refer to self-developed or customer-developed software, but also to the testing and release of CON.4 * selection and use of state-of-the-art software * and APP.1.1 * Office products *.

Different technical methods are used for the software tests. The procedure for penetration tests is described in more detail in the module DER.3.3 * Penetration Tests *.

Software testing can also be part of patch or change management. This is specified in more detail in the module OPS.1.1.3 * Patch and Change Management *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in software testing and release:

### 2 1 Incomplete implementation of client's requirements

If the requirements are incompletely or incorrectly incorporated or if the parties involved in the software development or procurement (eg client and contractor) communicate inadequately with each other, the requirements of the client could only be fulfilled incompletely. This can lead to weaknesses in the software. If, for example, the requirements of the contractor have to be incorporated retroactively, software development projects may be delayed and thus cause financial damage.

### 2 2 Inadequate training of developers and software testersIt is often assumed that trained developers and software testers have sufficient knowledge to test and share software because of their training. Accordingly, developers and software testers are often trained too little to innovations in their subject area or the application of the software. This ignorance can lead to serious security problems when z. For example, functions or methods may be used in programming that are already considered unsafe, but are not yet known to developers.

### 2 3 Software test with productive data

Software tests with productive data or in productive operation are necessary, because only with the productive data can the function and the performance of the product be assessed. Often, developers also have a different view of the product being developed; for example, they have a different level of security awareness, they trust the software they are developing too much, and they can not correctly interpret the potential impact of problems.

Although software tests with productive data are necessary, this can lead to security problems. In particular confidential productive data can be viewed for the software tests by unauthorized employees or third parties who have been commissioned with the respective software test.

Through software tests in productive operation, the operation could be massively disrupted. Malfunctions of the software under test may affect other applications and IT systems that are severely disrupted. If you are using the "original" productive data in production mode and not with copies of the data, they could be changed or deleted unintentionally.

### 2 4 Missing or inadequate test procedure

If new software is not or insufficiently tested and released without installation instructions, errors in the software may go undetected. It is also possible that thereby required and observed installation parameters are not recognized or observed.

These software or installation errors resulting from a lack of or inadequate software testing procedures present a significant threat to the institution's IT operations. For example, data may be lost if an update to a database management system is run without prior testing.

### 2 5 Missing or inadequate clearance procedure

A missing or inadequate release procedure can lead to the use of software that was not accepted by the technical side. So the software can have functionalities that it should not have, or functionalities may be missing. In addition, the software may be incompatible with other applications.

### 2 6 Missing or inadequate documentation of tests and test results

A software release can usually be issued once all tests have been performed and no deviations have been found. However, if the documentation of the software tests is incomplete, it will not be possible to detect what has been tested afterwards. If identifiable software errors or missing functions were insufficiently documented and thus not taken into account during the release, these deviations may unintentionally delete or modify the productive data to be processed and disturb other IT systems and applications.

### 2 7 Missing or inadequate documentation of the approval criteria

If approval criteria are not clearly communicated, this may result in premature release or no release, although it could be granted. As a result, versions with unrecognized software errors can be released, which can interfere with productive operation, and secondly, this can lead to a project delay with financial losses.

3 requirements
---------------The following are specific requirements for software testing and clearance. Basically, the IT manager is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### OPS.1.1.6.A1 Planning the software tests

Before the software tests can be carried out, the framework conditions within the institution MUST be determined according to the protection requirements, organizational units, technical possibilities and test environments. The software tests MUST be based on the specifications of the specifications.

When selecting the test cases MUST be taken to ensure that they are as representative as possible of the functions to be tested.

#### OPS.1.1.6.A2 Performing Functional Software Tests [Tester]

Functional software tests MUST be performed to verify the proper and complete operation of the software. The functional software tests MUST be performed in such a way that they do not affect the productive operation.

#### OPS.1.1.6.A3 Evaluation of test results [Tester]

The results of the software tests MUST be evaluated. A nominal and actual comparison SHOULD be carried out via the comparison with defined specifications. The evaluation MUST be documented.

#### OPS.1.1.6.A4 Sharing the Software [Specialists]

The functional unit MUST release the software as soon as the software tests have been successfully completed. The release MUST be documented in the form of a release declaration.

The releasing organizational unit MUST verify that the software has been tested as required. The results of the software tests MUST match the predefined expectations. It MUST also be checked whether compliance with legal or organizational requirements is ensured.

#### OPS.1.1.6.A5 Performing Non-Functional Software Tests [Tester]

Non-functional tests MUST be performed. In particular, security-specific software tests SHOULD be performed if the application has security-critical features. The test cases as well as the test results SHOULD be documented.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state of the art in software testing and clearance. They SHOULD be implemented in principle.

#### OPS.1.1.6.A6 Orderly briefing of the software testers [IT-Betrieb, Fachverantwortliche]

A software tester SHOULD be informed about the types of tests to be performed and the areas of software to be tested by IT operations. In addition, the software tester SHOULD be informed about the use cases and possible further requirements of the software.

#### OPS.1.1.6.A7 Software Tester Personal Selection [Human Resources]

When selecting software testers, separate selection criteria SHOULD be taken into account. The persons SHOULD have the required professional qualifications. There should be sufficient knowledge of the programming language to be tested, the development environment and the test methods to be used.

In public institutions and institutions protected by copyright, SHOULD check if a security clearance is required.

#### OPS.1.1.6.A8 Continuing Education of the Software Tester [Head of Human Resources]The software testers SHOULD be trained according to the module OPS.3 Sensitization and Training. Procedures should be established to inform the software testers about innovations that are relevant to their particular task.

#### OPS.1.1.6.A9 Procurement of test software [tester, IT operation]

The test software SHOULD be procured according to a catalog of requirements. It SHOULD also undergo the testing and approval process. It should be checked whether the assistance and support services of the software manufacturer are sufficient.

#### OPS.1.1.6.A10 Creation of an acceptance plan

The acceptance plan SHOULD document the test types, test cases and expected results to be performed. In addition, the acceptance plan SHOULD include the approval criteria. The procedure for rejecting a release SHOULD be defined.

#### OPS.1.1.6.A11 Use of anonymised or pseudonymised test data [Tester, Data Protection Officer]

Only anonymized or pseudonymized test data should be used for software testing. Insofar as the productive data have a personal reference, institutions SHOULD use only anonymized test data. If a personal reference could be derived from the test data, the data protection officer and possibly the staff representatives should be consulted.

#### OPS.1.1.6.A12 Performing Regression Tests [Tester]

If software tests are to be performed after a change in the software, regression tests should be performed. Regression tests SHOULD be completed. The omission of test cases SHOULD be substantiated and documented. The test cases and the test results SHOULD be documented.

#### OPS.1.1.6.A13 Separation of Test and Quality Management Environment from the Production Environment [IT Operations]

Software SHOULD only be tested in a dedicated test and quality management environment. The test and quality management environments SHOULD be operated separately from the production environment. The architectures and mechanisms used in the test landscape SHOULD be documented. The quality management environment SHOULD be adapted to the production environment. Procedures should be documented on how to handle the test landscape after the software test has been completed.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### OPS.1.1.6.A14 Performing Penetration Tests [Tester] (CIA)

It should be carried out for applications or IT systems with increased protection required penetration tests as a test method. It SHOULD be created a penetration test concept. In the penetration test concept, the criteria of success SHOULD be documented in addition to the test methods to be used.

The penetration test SHOULD be based on the framework conditions of the penetration test concept. The vulnerabilities identified by the penetration test SHOULD be classified and documented.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the area of ​​"Software tests and releases" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>* #### [29119] ISO / IEC 29119-2: 2013-09

  

 Software and systems engineering - Software testing, ISO, 09.2013
 [Http://www.iso.org/iso/catalogue\_detail.htm?csnumber=56736](http://www.iso.org/iso/catalogue_detail.htm?csnumber=56736)

 
* #### [BSIPEN] BSI Study "Implementation Concept for Penetration Testing

  

 Federal Office for Security in Information Technology, 11.2013
 [Https://www.bsi.bund.de/DE/Publikationen/Studien/Pentest/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/Studien/Pentest/index_htm. html)

 
* #### [BSIWEB] BSI Guides for Building Secure Web Applications

  

 Federal Office for Security in Information Technology, 2013
 [Https://www.bsi.bund.de/DE/Publikationen/Studien/Webanwendungen/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/Studien/Webanwendungen/index_htm. html)

 
* #### [CVSS] Common Vulnerability Scoring System

  

 CVSS, (last accessed on 28.09.2017)
 <Https://www.first.org/cvss>

 
* #### [GLEN] The Art of Software Testing

  

 Glenford J. Myers, Corey Sandler, Tom Badgett, Todd M. Thomas John Wiley & Sons, 2004

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the "Software tests and releases" block.

* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.38 Abuse of personal data
* G 0.42 Social engineering
* G 0.43 Importing messages
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.