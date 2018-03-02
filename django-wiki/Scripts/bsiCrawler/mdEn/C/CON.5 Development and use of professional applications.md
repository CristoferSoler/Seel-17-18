[toc]
 
1 description
--------------

### 1.1 Introduction

Specialized applications are complex applications that are designed for individual and specific technical tasks and are generally not purchased and used as standard solutions. Instead, base solutions are customized for individual use by institutions, or applications are developed entirely by third parties or the institution itself. These specialized applications include, for example, human resources management software, social data management techniques, or financial reporting. Careful planning of safety measures prior to selection and commissioning of an application is essential for the level of safety achieved, as errors in planning, such as B. missing security functions during operation can not be compensated or only with high additional expenses.

### 1.2 Objective

The aim of this module is to show which basic safety requirements must be taken into account in the planning, procurement, commissioning, regular operation and decommissioning of a specialized application.

### 1.3 Delimitation

The focus of this module is on organizational and conceptual aspects of information security of specialized applications. Selection, configuration and safe operation of safety functions in applications are only described generally and fundamentally in this module. A concrete description for widely used standard applications can be found in the other building blocks of the layer APP * Applications * as well as in the building block CON.4 * Selection and Use of Standard Software *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the field of *** *** specialist applications:

### 2 1 Loss of confidentiality or integrity in specialized applications

Specialist applications typically process sensitive information, such as all types of personal information or trade secrets. If these data are disclosed or changed unintentionally, this can result in contractual or legal violations (including data protection law violations). In particular, in the event of loss of integrity, legal violations may arise due to process or procedural errors. If the information is no longer available, business or specialist tasks can no longer be fulfilled. The loss of confidentiality, integrity and availability can have significant consequences, such as: As criminal and financial consequences, or in individual cases even personal injury.

### 2 2 Inappropriate access and access rights management

If the allocation of access and access rights is poorly regulated, this will quickly lead to serious security vulnerabilities, eg. B. by wild growth in the rights allocation. This quickly causes users to receive permissions on demand, or vice versa, only through unnecessarily complicated ways to get them. Thus, on the one hand, missing authorizations can hinder the daily work, on the other hand, authorizations can be granted without requirement and thus pose a security risk.

### 2 3 Inaccessible contractual arrangements with an external service provider
Due to inadequate contractual arrangements with an external service provider, especially in the creation, support of the implementation and maintenance of the application, various and serious security problems can occur. If tasks, performance parameters or expenses have been described insufficiently or misleadingly, the result may be that security measures are not implemented due to ignorance, lack of qualification or lack of resources. This can have a variety of negative consequences, such as non-compliance with regulatory requirements and obligations, failure to comply with disclosure obligations and laws, and the lack of ownership due to the loss of control and oversight.

### 2 4 Software designation error

When planning applications, programs and protocols, security-relevant design errors can arise. These often result from the reuse of dedicated application modules and protocols in other deployment scenarios. If other security requirements are relevant here, for example, if application modules and protocols intended for isolated operating environments are connected to the Internet, this can lead to massive security gaps.

### 2 5 Software vulnerabilities

Software vulnerabilities are errors that pose a security risk to the data processed by the application. These security risks arise from the fact that planned security mechanisms are ineffective or are due to technical progress, or if security mechanisms can be deliberately bypassed as a result. In addition, software errors can also result in poor processing performance (performance deficiencies) or failure of the application. Possible consequences of a breakdown include loss of work, lost sales or breaches of contractual agreements or legal requirements.

### 2 6 Undocumented functions

Many applications often include built-in undocumented features for development or support purposes by the manufacturer. These are mostly unknown to the users. Undocumented functions are problematic when they are bypassing essential security mechanisms, such as: B. such for access protection allow. This can significantly affect the confidentiality and integrity of the processed data.

### 2 7 Missing or inadequate security measures in applications

Security mechanisms or security functions are designed to ensure that the processing of information ensures confidentiality, integrity and availability to the required extent. Frequently, however, the development of an application focuses on functional functionality or the time and cost framework, so that important security mechanisms are too weak, so that they can easily be bypassed, or even completely lacking.

3 requirements
---------------

The following are specific requirements for planning, selection, procurement, commissioning, operation and separation of specialized applications. Basically, the department that uses the application is responsible for fulfilling these requirements. In practice, these requirements can only be fulfilled if the IT operations managers (eg IT managers) and the information security officer (ISB) are involved or involved.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### CON.5.A1 Definition of required security functions of the specialist application [IT operation]
For the specialist application, the necessary security functions MUST be taken into account in the professional selection and integration into the IT infrastructures and operating processes. The selection and implementation of appropriate security features in the specialized application MUST be based on the data processed in the application and, where appropriate, a complementary risk analysis. The safety functions MUST be suitably documented.

#### CON.5.A2 Testing and approval of specialized applications [Head of IT, Data Protection Officer]

For an orderly transfer of an application as well as for significant changes, a suitable procedure for testing and approval MUST be developed. It MUST be considered:

* the professional level (represented by the responsible persons),
* the level of IT operations (represented by the IT manager),
* the level of information security (represented by the information security officer),
* the level of data protection (represented by the Data Protection Officer) as well
* depending on the nature and complexity of an application other function carriers such. the staff representation.
#### CON.5.A3 Secure installation of a specialist application [IT operation]

An INSTALLATION MUST be created containing all the required application modules (libraries), installation order, and application module configuration. The installation instructions SHOULD consider the necessary aspects regarding the installation environment. The tray application MUST be installed according to the installation instructions.

For changes in the application and functional updates, the installation instructions MUST be updated.

#### CON.5.A4 Introducing users to the application

Users and administrators MUST be guided to the proper use and administration of the application, including its security features. This should include policies and procedures for using and administering the application, training and briefing, manuals and online help, and key user support.

#### CON.5.A5 Secure operation of a specialized application [IT operation]

Authorizations for the use and administration of a specialist application MUST be given correctly and regularly checked for correctness. Authorizations no longer required MUST be revoked again.

It MUST be ensured that log data is regularly evaluated and legally prescribed storage periods for log data are adhered to.

Security-critical patches and updates MUST be provided by the vendor of the application based on appropriate contractual agreements and timely. It MUST be ensured that patches and updates have previously been properly tested and approved.

There must be regular backups and restoring exercises.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​development and application of specialized applications. They SHOULD be implemented in principle.

#### CON.5.A6 Comprehensive documentation of application requirements

The e relevant requirements for the application SHOULD be documented. This documentation SHOULD be updated for changes to the application and functional updates.

#### CON.5.A7 Creation of a client concept [Head IT]

It was intended to ensure, with a client concept, that applications and data of different customers are operated in a cleanly separated manner. This SHOULD be created by the operator of the multi-tenant application and made available to the using institutions. The required mechanisms for client separation at the service provider SHOULD be implemented sufficiently.

#### CON.5.A8 Appropriate application development control [IT chief]
In developing an individual application, a suitable control and project management model SHOULD be used. In particular, the required qualifications of the personnel, the coverage of all relevant phases during the life cycle of the software, a suitable development model, risk management and quality objectives SHOULD be considered.

#### CON.5.A9 Decommissioning Applications [IT Manager]

The decommissioning of applications SHOULD be planned. It SHOULD clarify for all data which data is migrated, archived or deleted. Data that is no longer needed SHOULD be deleted safely. The decommissioning of applications and the associated IT systems and data carriers SHOULD be comprehensibly documented.

#### CON.5.A10 Emergency Prevention for Applications [IT Leader]

The specialist applications SHOULD be included in the planning for emergency preparedness.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### CON.5.A11 Appropriate and legally compliant procurement

When procuring a specialized application, the existing legal and organizational requirements SHOULD be implemented. If service providers are involved in the procurement, development or operation of an application, the relevant safety aspects of the contracts SHOULD be taken into account.

The institution SHOULD have defined processes and defined contacts, which ensure the consideration of the respective framework conditions. It SHOULD clarify what role certifications play in the award decision.

#### CON.5.A12 Fiduciary deposit

For business-critical applications, SHOULD it be checked if it is necessary to protect them against failure of the manufacturer of the application. The fiduciary deposit of materials not included with the application SHOULD be considered by an escrow agency, such as: Documented code, construction plans, keys, passwords. In this case, the duties of the escrow agency in storage and release (when may the deposit be issued to whom?) SHOULD be contractually regulated.

#### CON.5.A13 Development of a redundancy concept for applications [Head IT]

If there is a high or very high protection requirement with regard to the availability of an application, then a redundancy concept SHOULD be created. This SHOULD include the following aspects:

* Planning a limited IT operation and disaster recovery (emergency preparedness concept)
* Application-level redundancy through load balancing or application clusters / cloud services
* Possibilities to pan the applications to other systems
In addition, it should be ensured that the redundancy concept also includes the buildings and rooms, systems and communication connections required for the operation of the application. The redundancy concept SHOULD be coordinated with the emergency concept. The measures from the redundancy concept SHOULD be regularly tested and practiced.
