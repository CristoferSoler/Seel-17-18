Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

The use of IT for task management requires that machine data processing work as smoothly as possible, since the individual results can not be controlled in most cases. As part of the software tests, it is therefore checked whether the software in question works without errors. To do this, the software must reliably provide the required functionality and, in addition, must not have any unwanted side effects. With the subsequent release of the software by the responsible organizational unit, the basic permission is given to use the software productively in the institution. At the same time, this organizational unit assumes responsibility for the IT process, which is supported by the software.

Software can be tested at different points in the life cycle of a software. Thus, software tests may already be necessary during development, before release for productive operation or in the course of patch and change management. The software tests and releases are to be carried out for self-development as well as for the use of standard software.

This module describes the test and approval process for self-developed or customized software as well as for standard software. The test and release process is characterized by the fact that it can be run several times depending on the result.

### 1.2 Objective

By implementing this module, the institution ensures that the software used meets the technical and organizational requirements as well as the existing protection requirements of the entire institution or individual organizational units. A key aspect of this is that safety-critical software is systematically and methodically checked for existing weak points.

### 1.3 Delimitation

While the module CON.3 * Software Development * covers the software development process and the software tests that are required during the development process, this module describes the special requirements that are placed on test and release management. This test and release management does not exclusively refer to self-developed or customer-supplied software, but also to the testing and release of CON.4 * Selection and use of state-of-the-art software * and APP.1.1 * Office products *.

Different technical methods are used for the software tests. The procedure for penetration tests is described in more detail in the module DER.3.3 * Penetration Tests *.

Software testing can also be part of patch or change management. This is specified in more detail in the module OPS.1.1.3 * Patch and Change Management *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in software testing and release:

### 2 1 Incomplete implementation of client's requirements

If the requirements are incompletely or incorrectly incorporated or if the parties involved in the software development or procurement (eg client and contractor) communicate inadequately with each other, the requirements of the client could only be fulfilled incompletely. This can lead to weaknesses in the software. If, for example, the requirements of the contractor have to be incorporated retroactively, software development projects may be delayed and thus cause financial damage.

### 2 2 Inadequate training of developers and software testers
It is often assumed that trained developers and software testers have sufficient knowledge to test and share software because of their training. Accordingly, developers and software testers are often trained too little to innovations in their field or the field of application of the software. This ignorance can lead to serious security problems when z. For example, functions or methods may be used in programming that are already considered unsafe, but are not yet known to developers.

### 2 3 Software test with productive data

Software tests with productive data or in productive operation are necessary, because only with the productive data can the function and the performance of the product be assessed. Often, developers also have a different view of the product being developed; for example, they have a different level of security awareness, they trust the software they are developing too much, and they can not correctly interpret the potential impact of problems.

Although software tests with productive data are necessary, this can lead to security problems. In particular confidential productive data can be viewed for the software tests by unauthorized employees or third parties who have been commissioned with the respective software test.

Through software tests in productive operation, the operation could be massively disrupted. Malfunctions of the software under test may affect other applications and IT systems that are severely disrupted. If you are using the "original" production data in production mode and not with copies of the data, they could be changed or deleted unintentionally.

### 2 4 Missing or inadequate test procedure

If new software is not or insufficiently tested and released without installation instructions, errors in the software may go undetected. It is also possible that thereby required and observed installation parameters are not recognized or observed.

These software or installation errors resulting from a lack of or inadequate software testing procedures pose a significant threat to the institution's IT operations. For example, data may be lost if an update to a database management system is run without prior testing.

### 2 5 Missing or inadequate clearance procedure

A missing or inadequate release procedure can lead to the use of software that was not accepted by the technical side. Thus, the software may have functionalities that it should not have, or functionalities may be missing. In addition, the software may be incompatible with other applications.

### 2 6 Missing or inadequate documentation of tests and test results

A software release can usually be issued once all tests have been performed and no deviations have been found. However, if the documentation of the software tests is incomplete, it will not be possible to detect what has been tested afterwards. If identifiable software errors or missing functions were insufficiently documented and thus not taken into account during the release, these deviations may unintentionally delete or modify the productive data to be processed and disturb other IT systems and applications.

### 2 7 Missing or inadequate documentation of the approval criteria

If approval criteria are not clearly communicated, it may result in premature release or no release, although it could be granted. As a result, versions with unrecognized software errors can be released, which can interfere with productive operation, and secondly, this can lead to a project delay with financial losses.
