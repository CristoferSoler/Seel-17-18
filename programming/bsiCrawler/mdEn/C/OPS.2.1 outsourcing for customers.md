1 description
--------------

### 1.1 Introduction

In outsourcing, institutions (outsourcing customers) outsource all or part of their business processes and services (eg, security or cleaning staff) to external service providers (outsourcing service providers). The operation of hardware and software can also be outsourced as a service. Regardless of what is outsourced, every outsourcing requires close ties to the external service provider and their service quality and service quality. This ratio is particularly for the customer not only opportunities, but also associated with significant risks, such. As strong dependencies, loss of their own know-how and loss of control and control. Information security aspects must therefore be adequately considered during the entire life cycle of outsourcing.

This module focuses on requirements that outsourcing customers should adhere to or implement during each phase of an outsourcing project.

### 1.2 Objective

The aim of this module is to ensure that all security objectives of the outsourcing customer are met even after the outsourcing of business processes or services to an outsourcing service provider and that the agreed level of security is permanently maintained (or improved). Outsourcing should not result in any uncontrollable risks to the outsourcing institution regarding information security.

### 1.3 Delimitation

This building block contains hazards and security requirements from the point of view of outsourcing customers and is limited solely to the requirements of protection of information from the outsourcing institution.

Transmission paths to outsourcing service providers can not be secured by implementing the requirements.

The terms outsourcing and cloud have many parallels. For outsourcing customers, there are usually additional requirements for the use of cloud services.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in customer outsourcing:

### 2 1 Lack of or inadequate information security regulations

An outsourcing project typically transfers large amounts of information between the customer and the outsourcing service provider. Depending on the protection requirements of the information to be processed, missing or inadequate regulations can cause damage. This is the case, for example, if the regulations and instructions for controlling the service provider are not updated in the event of technical, organizational or personnel changes, for example, if contact persons change. The range of regulatory deficits ranges from ambiguity in responsibilities and control functions to incomprehensible or incoherent formulated regulations, up to completely missing regulations.

### 2 2 Inappropriate access, access and access rights management

Depending on the outsourcing plans, it may be necessary for the outsourcing customer's employees to have access, access and access rights to IT systems, information, buildings or rooms of the outsourcing service provider. If the granting, administration and control of these rights is poorly regulated and, in extreme cases, even unauthorized rights are granted, it is no longer possible to guarantee the necessary protection requirements for the outsourcer's information. For example, the uncontrolled assignment of administrative authorizations to employees of the outsourcing service provider can lead to serious security risks. These could exploit permissions and copy or manipulate sensitive information.

### 2 3 Missing or inadequate testing and approval process
If an outsourcing customer has not defined adequate requirements for testing and approval procedures for the outsourcing service provider, existing errors in the hardware and software or security gaps in the configuration may not be recognized or not detected in good time. This lack can lead to the fact that the necessary protection of the information of the outsourcing customer can not be guaranteed any longer. If testing reveals that new components or updates result in significant changes to workflows, or more resources (eg, memory, processor capacity) are required for acceptable processing speed, and this is not communicated to the customer, this can result in significant failure. or subsequent investments.

### 2 4 Inadequate contractual arrangements with an outsourcing service provider

Due to inadequate contractual arrangements with an outsourcing service provider, various and serious security problems can arise. If tasks, performance parameters or expenses have been described insufficiently or misleadingly, the consequence may be that security measures are not implemented due to ignorance or lack of resources. This can have a variety of negative consequences, such as non-compliance with regulatory requirements and obligations, failure to comply with disclosure obligations and laws, and failure to take responsibility for loss of control and control.

### 2 5 Inadequate regulations for the end of an outsourcing

Without sufficient and appropriate regulations for the resolution of an outsourcing contract by the outsourcing customer, there is the danger that the outsourcing customer will find it difficult to get rid of the outsourcing service provider. On the other hand, it can also happen that termination of the outsourcing service provider, which is possible too soon, forces the outsourcing customers to choose an inappropriate new outsourcing service provider. In either case, it may be difficult or even impossible to transfer the outsourced area to another service provider or reintegrate it into one's own institution. This can lead to a variety of security problems, for example, during the dissolution process, data and systems could no longer be adequately protected, since these are regarded as "old systems". Inadequate regulations for the deletion of data, including data backups, can lead to the disclosure of confidential data to third parties.

### 2 6 Dependence on an outsourcing service provider

By opting for outsourcing, an institution always becomes dependent on the outsourcing service provider. This dependency involves the risk that know-how will be lost and that there will no longer be complete control over the outsourced processes and components. In addition, the protection needs of the outsourced business processes and information may vary, resulting in inadequate security measures. By having full control of business processes, sensitive information, resources, and IT systems, while reducing the knowledge of outsourcing customers, outsourcing service providers may no longer notice information security deficiencies.

This situation could be exploited by the outsourcing service provider, for example through drastic price increases and insufficient service quality.

### 2 7 Disruption of the working climate due to an outsourcing project
Outsourcing projects are often seen as negative changes from the point of view of the employees of the outsourcing institution. This often leads to a bad working environment. Employees of the outsourcing client often fear for them adverse task changes or even downsizing through outsourcing projects. In the event of a negative attitude towards the outsourcing project, employees could unintentionally or willfully neglect security measures, take a boycott position or even take acts of revenge. In addition, this could terminate know-how carriers (such as IT managers and the IT operation) during the introductory phase, so that the outsourcing project can not be implemented as planned.

### 2 8 Poor information security in the outsourcing implementation phase

The introductory phase of outsourcing projects is often characterized by tight deadlines and financial targets. This can lead to lack of security controls and audits or reviews and other quality assurance measures remain, for example, when creating security concepts. Transitional measures with security deficits will remain a habit over time and due to resource constraints over years. This creates the concrete danger that this will establish a "project climate" that will lead to further serious safety deficiencies.

### 2 9 Failure of the systems of an outsourcing service provider

In the case of an outsourcing service provider, the IT systems and processes operated there can partially or completely fail, which also affects the outsourcing customer. In the event of inadequate client separation, the failure of a system that is not assigned to the outsourcing customer may still result in the outsourcing customer being unable to retrieve its contractually guaranteed service. Similar problems arise when the connection between outsourcing service provider and customer fails.

### 2 10 Weaknesses when connecting to an outsourcing service provider

If the IT connection between the outsourcing service provider and the outsourcing customer is insufficiently secured in an outsourcing project, the confidentiality and integrity of the transmitted data may be jeopardized. However, open or poorly secured interfaces could also result in unauthorized access for outsiders to the systems of the participating institutions.

### 2 11 Lack of multi-client capability at the outsourcing service provider

Outsourcing service providers usually have many different customers who use the same resource base (eg IT systems, networks, personnel). If the IT systems and data of the different customers are not sufficiently separated from each other, there is a risk that one customer will be able to access the area of ​​another customer. In addition, there could be conflicts of interest with the outsourcing service provider if he has to meet parallel comparable resource requirements. If the respective customers are in a competitive situation, this can be particularly problematic.

3 requirements
---------------

The following are specific requirements for Outsourcing for Customers. Basically, the IT manager is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:
#### OPS.2.1.A1 Definition of security requirements for outsourcing projects [ISB outsourcing customer]

All security requirements for an outsourcing project MUST be based on the outsourcing strategy. Both outsourcing parties MUST be contractually bound to comply with IT-Grundschutz or a comparable level of protection. All interfaces between the outsourcing service provider and customers MUST be identified and corresponding security requirements defined. It must be specified in the security requirements which permissions (access rights, access rights, access rights) are set up mutually.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state of the art in outsourcing for customers. They SHOULD be implemented in principle.

#### OPS.2.1.A2 Timely participation of the Staff Committee [Head of Organization]

The staff representatives SHOULD be informed in time about an outsourcing project. The participation of the staff representatives SHOULD take place already in the bidding phase. Depending on the outsourcing project, the legal voice should be respected.

#### OPS.2.1.A3 Selection of a suitable outsourcing service provider [ISB Outsourcing customer]

To select the outsourcing service provider, a requirement profile with the security requirements for the outsourcing project SHOULD exist. There should be evaluation criteria for the outsourcing service provider and their personnel based on this requirement profile.

#### OPS.2.1.A4 Contract design with the outsourcing service provider [ISB Outsourcing customer]

All aspects of the outsourcing project with the outsourcing service provider SHOULD be regulated in writing. All roles and obligations to cooperate for the creation, review and modification (eg of persons) of the security concept with the outsourcing service provider SHOULD be regulated. The rights and obligations of the contracting parties SHOULD be regulated in writing. For the regular review of the requirements, the outsourcing service provider SHOULD provide the outsourcing customer with the possibility of audits.

#### OPS.2.1.A5 Definition of an Outsourcing Strategy [ISB Outsourcing Client]

An outsourcing strategy SHOULD be defined that takes into account not only the economic, technical, organizational and legal framework but also the relevant aspects of information security. It SHOULD clarify which business processes, tasks or applications are generally eligible for outsourcing. The outsourcing client SHOULD have sufficient skills, competencies and resources to determine and control information security requirements in each outsourcing project. The Outsourcing Strategy SHOULD describe the goals, opportunities and risks of the outsourcing project.

#### OPS.2.1.A6 Creation of a security concept for the outsourcing project [specialist responsible, ISB outsourcing customer]

The outsourcing customer SHOULD create a security concept for each outsourcing project based on the associated security requirements. Likewise, each outsourcing service provider SHOULD submit an individual security concept for the respective outsourcing project. Both security concepts SHOULD be coordinated with each other. The security concept of the outsourcing service provider and its implementation SHOULD be combined into an overall security concept and regularly checked for effectiveness by the outsourcing customer or independent third parties.

#### OPS.2.1.A7 Definition of possible communication partners [Head of Organization, ISB Outsourcing Customer]
It SHOULD be determined which internal and external communication partners may transmit and receive which information about the respective outsourcing project. There SHOULD exist a process that checks the function of the communication partners on both sides. The permitted communication partners with the respective authorizations MUST always be up to date.

#### OPS.2.1.A8 Regulations for the use of the staff of the outsourcing service [Head of Human Resources, ISB Outsourcing Customer]

The employees of the outsourcing service provider SHOULD be obliged in writing to comply with the relevant laws, regulations and regulations applicable to the outsourcing customer. The employees of the outsourcing service provider SHOULD be instructed in their tasks and informed about existing information security regulations. There SHOULD exist substitution arrangements for the employees of the outsourcing service provider. There SHOULD exist a regulated procedure for termination of the contract with the employees of the outsourcing service provider. Outsourcing service providers SHOULD be treated as visitors in the short term or once.

#### OPS.2.1.A9 Agreement on the connection to networks of outsourcing partners [ISB Outsourcing customer]

Before connecting the network of the outsourcing customer to the network of the outsourcing service provider, all security-relevant aspects in an agreement SHOULD be regulated in writing. The agreement SHOULD specify exactly which areas and services the outsourcing service provider may access in the outsourcing customer's network. The compliance with the agreements for the network connection SHOULD be checked and documented. On both sides, contact persons should be named for both organizational and technical issues of the network connection. The required level of security SHOULD be demonstrably demanded and checked by the outsourcing service provider before the network connection to the outsourcing service provider is activated. In case of security problems on one of the two sides SHOULD be determined who should be informed about it and which escalation steps are to be initiated.

#### OPS.2.1.A10 Agreement on data exchange between the outsourcing partners [ISB Outsourcing customer]

For the regular data exchange with fixed communication partners, the necessary security measures SHOULD be agreed. Data formats and procedures for secure data exchange SHOULD be specified. Contact persons for both organizational and technical problems and in particular for security-relevant events when exchanging data with third parties SHOULD be named. Availabilities and response times when exchanging data with third parties SHOULD be agreed. It SHOULD be determined which exchanged data may be used for which purposes.

#### OPS.2.1.A11 Planning and maintenance of information security in ongoing outsourcing operations [ISB Outsourcing customer]

The intention was to draw up an operational concept for the outsourcing project, which also considers the safety aspects. The security concepts of the outsourcing partners SHOULD regularly be checked for up-to-dateness and consistency. The status of the agreed security measures SHOULD be checked regularly. There should be regular communication between the outsourcing partners, including coordination on changes and improvements.
The outsourcing partners SHOULD regularly conduct joint exercises and tests to maintain safety levels. Information about security risks and how to deal with them SHOULD be exchanged on a regular basis between the outsourcing partners. There SHOULD exist a process that ensures the flow of information in dealing with security incidents affecting the respective contractors.

#### OPS.2.1.A12 Change Management [IT Operations, Change Manager]

The outsourcing customer SHOULD be informed about major changes in good time in advance. A documentation of all major changes in terms of planning, testing, approval and documentation SHOULD be regularly requested from the outsourcing customer. Before changes are made, relapse solutions should be worked out together with the outsourcing service provider.

#### OPS.2.1.A13 Secure migration for outsourcing projects

For the migration phase, a security management team of qualified employees of the outsourcing customer and the outsourcing service provider SHOULD be set up. A preliminary safety concept should be drawn up for the migration phase, which also considers the test and implementation phase. It SHOULD be ensured that productive data in the migration phase are not used unprotected as test data. All changes should be documented. After completing the migration, the security concept SHOULD be updated. It SHOULD be ensured that all exemptions are lifted at the end of the migration phase. For changes in the migration phase SHOULD be examined to what extent there is a need for adjustment to the contractual basis.

#### OPS.2.1.A14 Emergency Preparedness for Outsourcing [Emergency Response Officer]

There SHOULD exist an emergency preparedness concept for outsourcing, which includes the components of the outsourcing customer, the outsourcing service provider and the associated interfaces. In the emergency preparedness concept for outsourcing, the responsibilities, contact persons and processes between the outsourcing customer and the outsourcing service provider SHOULD be regulated. The outsourcing customer SHOULD control the implementation of the outsourcing service provider's emergency measures. It should be done to common emergency exercises of outsourcing customers and outsourcing service providers.

#### OPS.2.1.A15 Orderly termination of an outsourcing relationship [Head of Procurement]

The contract with the outsourcing service provider SHOULD regulate all aspects of the termination of the service relationship, both for a planned and an unplanned termination of the contract. It SHOULD be ensured that termination of the service relationship with the outsourcing service provider does not affect the outsourcing client's business.

The outsourcing customer SHOULD receive all information and data after the completion. The outsourcing service provider SHOULD safely delete all data after the return.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### OPS.2.1.A16 Security check of employees (CI)

With external outsourcing service providers SHOULD be contractually agreed that the trustworthiness of the employed personnel is suitably checked. For this, criteria should be defined together.

4 Further Information
------------------------------

### 4.1 Literature
Further information on risks and security measures in the area of ​​outsourcing for customers can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [BVIT2005] Buisiness Process Outsourcing Guide

  

 Business Process Outsourcing Guidelines - BPO as Opportunity for the Location Germany, Federal Association for Information Technology Telecommunications and New Media, Version 10.1, 2005
 <Https://www.bitkom.org/Bitkom/Publikationen/Leitfaden-Business-Process-Outsourcing.html>

 
* #### [BVIT2008] Guide Legal Aspects of Outsourcing in Practice

  

 Legal Aspects of Outsourcing in Practice, Bundesverband Informationswirtschaft Telekommunikation und neue Medien e.V., 2008
 <Https://www.bitkom.org/Bitkom/Publikationen/Rechtliche-Aspekte-von-Outsourcing-in-der-Praxis.html>

 
* #### [DIN37500] DIN ISO 37500: 2015-08

  

 Guide Outsourcing, DIN German Institute for Standardization e.V., 08.2015

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the module "Outsourcing for customers".

* G 0.11 Failure or disruption of service providers
* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.17 Loss of equipment, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.22 Manipulation of information
* G 0.25 Failure of devices or systems
* G 0.29 Violation of laws or regulations
* G 0.35 coercion, blackmail or corruption
* G 0.42 Social engineering
The cross reference tables can be found in the download area due to their size.
* G 0.11 Failure or disruption of service providers
  * OPS.2.1.A3 Selection of a suitable outsourcing service provider [ISB Outsourcing customer]
  * OPS.2.1.A5 Definition of an Outsourcing Strategy [ISB Outsourcing Client]
  * OPS.2.1.A9 Agreement on the connection to networks of outsourcing partners [ISB Outsourcing customer]
  * OPS.2.1.A14 Emergency Preparedness for Outsourcing [Emergency Representative]
  * OPS.2.1.A15 Orderly termination of an outsourcing relationship [Head of Procurement]
* G 0.14 Spying out information (spying)
  * OPS.2.1.A7 Definition of possible communication partners [Head of Organization, ISB Outsourcing Customer]
  * OPS.2.1.A10 Agreement on data exchange between the outsourcing partners [ISB Outsourcing customer]
* G 0.15 Listening
  * OPS.2.1.A9 Agreement on the connection to networks of outsourcing partners [ISB Outsourcing customer]
  * OPS.2.1.A10 Agreement on data exchange between the outsourcing partners [ISB Outsourcing customer]
* G 0.17 Loss of equipment, data carriers or documents
  * OPS.2.1.A6 Creation of a security concept for the outsourcing project [specialist responsible, ISB outsourcing customer]
  * OPS.2.1.A10 Agreement on data exchange between the outsourcing partners [ISB Outsourcing customer]
* G 0.18 Missing planning or missing adjustment
  * OPS.2.1.A1 Definition of security requirements for outsourcing projects [ISB outsourcing customer]
  * OPS.2.1.A10 Agreement on data exchange between the outsourcing partners [ISB Outsourcing customer]
  * OPS.2.1.A11 Planning and maintenance of information security in ongoing outsourcing operations [ISB Outsourcing customer]
  * OPS.2.1.A12 Change Management [IT Operations, Change Manager]
  * OPS.2.1.A13 Secure migration for outsourcing projects
  * OPS.2.1.A14 Emergency Preparedness for Outsourcing [Emergency Representative]
  * OPS.2.1.A15 Orderly termination of an outsourcing relationship [Head of Procurement]
  * OPS.2.1.A16 Security check of employees (CI)
  * OPS.2.1.A5 Definition of an Outsourcing Strategy [ISB Outsourcing Client]
  * OPS.2.1.A6 Creation of a security concept for the outsourcing project [specialist responsible, ISB outsourcing customer]
  * OPS.2.1.A9 Agreement on the connection to networks of outsourcing partners [ISB Outsourcing customer]
  * OPS.2.1.A12 Change Management [IT Operations, Change Manager]
  * OPS.2.1.A13 Secure migration for outsourcing projects
* G 0.19 Disclosure of information worthy of protection
  * OPS.2.1.A6 Creation of a security concept for the outsourcing project [specialist responsible, ISB outsourcing customer]
  * OPS.2.1.A7 Definition of possible communication partners [Head of Organization, ISB Outsourcing Customer]
  * OPS.2.1.A8 Regulations for the use of the staff of the outsourcing service [Head of Human Resources, ISB Outsourcing Customer]
  * OPS.2.1.A10 Agreement on data exchange between the outsourcing partners [ISB Outsourcing customer]
  * OPS.2.1.A11 Planning and maintenance of information security in ongoing outsourcing operations [ISB Outsourcing customer]
  * OPS.2.1.A13 Secure migration for outsourcing projects
* G 0.22 Manipulation of information
  * OPS.2.1.A6 Creation of a security concept for the outsourcing project [specialist responsible, ISB outsourcing customer]
  * OPS.2.1.A10 Agreement on data exchange between the outsourcing partners [ISB Outsourcing customer]
* G 0.25 Failure of devices or systems
  * OPS.2.1.A6 Creation of a security concept for the outsourcing project [specialist responsible, ISB outsourcing customer]
  * OPS.2.1.A14 Emergency Preparedness for Outsourcing [Emergency Representative]
* G 0.29 Violation of laws or regulations
  * OPS.2.1.A1 Definition of security requirements for outsourcing projects [ISB outsourcing customer]
  * OPS.2.1.A10 Agreement on data exchange between the outsourcing partners [ISB Outsourcing customer]
  * OPS.2.1.A11 Planning and maintenance of information security in ongoing outsourcing operations [ISB Outsourcing customer]
  * OPS.2.1.A12 Change Management [IT Operations, Change Manager]
  * OPS.2.1.A13 Secure migration for outsourcing projects
  * OPS.2.1.A14 Emergency Preparedness for Outsourcing [Emergency Representative]
  * OPS.2.1.A15 Orderly termination of an outsourcing relationship [Head of Procurement]
  * OPS.2.1.A16 Security check of employees (CI)
  * OPS.2.1.A2 Timely participation of the Staff Committee [Head of Organization]
  * OPS.2.1.A4 Contract design with the outsourcing service provider [ISB Outsourcing customer]
  * OPS.2.1.A5 Definition of an Outsourcing Strategy [ISB Outsourcing Client]
  * OPS.2.1.A6 Creation of a security concept for the outsourcing project [specialist responsible, ISB outsourcing customer]
  * OPS.2.1.A8 Regulations for the use of the staff of the outsourcing service [Head of Human Resources, ISB Outsourcing Customer]
  * OPS.2.1.A16 Security check of employees (CI)
* G 0.35 coercion, blackmail or corruption
  * OPS.2.1.A16 Security check of employees (CI)
* G 0.42 Social engineering
  * OPS.2.1.A7 Definition of possible communication partners [Head of Organization, ISB Outsourcing Customer]
