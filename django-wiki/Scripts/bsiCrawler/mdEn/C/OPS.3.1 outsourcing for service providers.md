[toc]
 
1 description
--------------

### 1.1 Introduction

In outsourcing, outsourcing service providers take over business processes and services (eg security or cleaning staff) in whole or in part from outsourcing institutions (outsourcing customers). The operation of hardware and software can also be taken over as a service. Regardless of which services are taken over, this requires a close bond between the outsourcing service provider and the outsourcing customer. The outsourcing service provider is not spared the risks associated with the outsourcing relationship. He must implement the risk-reducing security requirements that are generally defined by the outsourcing customer (see the OPS.2.1 Outsourcing for Customers module). It is not only in the interest of the outsourcing customer, but also that of the outsourcing service provider, to provide the agreed service and to comply with the agreed security level. In case of failure to meet the requirements imposed on him sometimes threatened high penalties and, where appropriate, other legal consequences, which not only have financial implications, but also damage the reputation sustainable. The focus of this module is therefore on requirements that deal with the planning, implementation, control and management of information security aspects in the context of outsourcing from the point of view of the service provider.

### 1.2 Objective

The module describes the requirements for the outsourcing service provider so that he can meet the security level of the outsourcing institution or avoid uncontrollable risks resulting from the business relationship.

### 1.3 Delimitation

The building block contains security requirements for outsourcing that service providers have to meet. It complements the requirements of protection for information of the outsourcing institution from the point of view of the outsourcing service provider.

Securing the transmission paths between the service provider and the customer of outsourcing services is not considered in this module.

The terms outsourcing and cloud have many parallels. For providers of outsourcing, requirements regarding the use of cloud services are generally also to be considered.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in outsourcing service providers:

### 2 1 Failure of a Wide Area Network (WAN)

Outsourced service providers whose services are not provided locally by the customer are highly dependent on the availability of wide area networks (WANs). For economic reasons, services are usually provided from a few central locations. The connection to the outsourcing customer takes place via wide area networks. The failure of a long-distance network can therefore lead to the outsourced service can no longer be provided.

### 2 2 Missing or inadequate information security regulations

As part of an outsourcing, outsourcing service providers receive and process large amounts of information from outsourcing customers. Depending on the protection requirements of the information to be processed, missing or inadequate regulations can cause damage, for example if responsibilities are unclear. This is the case, for example, if the regulations and instructions are not updated in the event of technical, organizational or personnel changes, such as when contact persons change. The spectrum of regulatory deficits ranges from ambiguity in responsibilities and control functions to incomprehensible or incoherent formulated regulations, up to completely missing regulations.

### 2 3 Inappropriate access, access and access rights management
Depending on the outsourcing plans, it may be necessary for the outsourcing customer's employees to have access, access and access rights to IT systems, information, buildings or rooms of the outsourcing service provider. If the outsourcing service provider's outsourcing services are poorly managed, managed and controlled, this can lead to far-reaching security issues. If the processes for granting the rights are too complex, it may take too long for the employees of the outsourcing customer to receive the urgently needed rights. If IT operations grant clients too many rights, they could also gain access to areas of other clients.

### 2 4 Missing or inadequate testing and approval process

If an outsourcing service provider has not established a sufficient test and release procedure for hardware and software, this represents a considerable threat to IT operations. Existing hardware and software failures or security gaps in the configuration may not be able to do so on time recognized. Introducing new components into the operating environment without first testing them sufficiently can also result in errors or security holes from one tenant area having a negative impact on other customers.

If inadequate testing and release procedures lead to security incidents, the necessary protection of the customer's data is no longer guaranteed and penalties or contract terminations can occur and thus have financial consequences.

### 2 5 Unsecured file and disk transport

Outsourcing service providers often process large amounts of data from the outsourcing institution. If the transport of files, documents and data carriers is not suitably secured in accordance with the protection requirements of the information to be transported, loss, unauthorized notice or manipulation can cause considerable damage to the outsourcing service provider as well as to the outsourcing service provider. This can lead to significant problems in the outsourcing business relationship. Damage can occur if files or data carriers are transported on an insecure route to the outsourcing customer and these are tapped, manipulated or lost on the way.

### 2 6 Insufficient information security management at the outsourcing service provider

Insufficiently established or inadequately implemented information security management by the outsourcing service provider entails significant risks. The issues range from a lack of overall accountability for information security to a lack of senior management support and inadequate strategic and conceptual guidance towards an intransparent security process. For outsourcing service providers, there is now the risk that the requirements of the outsourcing institution will not be met if the entire organization is deficient in terms of information security.

### 2 7 Inadequate contractual arrangements with an outsourcing customer

It may happen that, due to inadequate contractual arrangements, an outsourcing service provider does not provide a service as required to maintain the customer's security level. If the need for protection and the resulting requirements for the security of outsourced data or systems are unknown to the outsourcing service provider, they can not be adequately protected.

### 2 8 Insufficient regulations for the end of an outsourcing
Without sufficient and appropriate regulation for the termination of the outsourcing contract, there is a risk that the business relationship will not be dissolved without conflict. Thus it could happen that information of the customer is irrevocably deleted at the outsourcing service provider, before they were completely and correctly transferred to the customer. A premature cancellation of customer information may result in penalties for the service provider.

### 2 9 Inadequate emergency preparedness concept for outsourcing

If an outsourcing service provider has only an inadequate emergency preparedness concept, under certain circumstances the contractually agreed IT systems and applications may not be available or only to a limited extent in an emergency. As a result, the business processes based on this are not available and the contractually agreed service is not provided.

### 2 10 Failure of the systems of an outsourcing service provider

In the case of an outsourcing service provider, the IT systems and processes operated there can partially or completely fail, which also affects the outsourcing customer. In the case of inadequate client separation, the failure of a system that is not assigned to the outsourcing customer may mean that it can no longer call up its contractually guaranteed service. Similar problems arise when the connection between outsourcing service providers and customers fails.

This may mean for the outsourcing service provider that, if contractually agreed, the outsourcing customer can assert claims for damages.

### 2 11 Weaknesses in the connection to an outsourcing service provider

If the IT connection between the outsourcing service provider and the outsourcing customer is insufficiently secured in an outsourcing project, the confidentiality and integrity of the transmitted data may be jeopardized. However, open or poorly secured interfaces could also result in unauthorized access for outsiders to the systems of the participating institutions.

### 2 12 Social Engineering

Social engineering is a way to gain unauthorized access to information or IT systems by "listening" to employees. This allows employees to be manipulated to act improperly. Employees of outsourcing service providers can make a particularly worthwhile goal here, since they have access to a great deal of data from different companies.

### 2 13 Lack of multi-client capability at the outsourcing service provider

Outsourcing service providers usually have many different customers who use the same resource base (IT systems, networks, personnel). If the IT systems and data of the different customers are not sufficiently separated from each other, there is a risk that one customer will be able to access the area of ​​another customer. In addition, there could be conflicts of interest with the outsourcing customer if the service provider has to meet parallel comparable resource requirements. If the respective customers are in a competitive situation, this can be particularly problematic.

3 requirements
---------------

The following are specific requirements for Outsourcing for Service Providers. Basically, the IT manager is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements
The following requirements MUST be implemented as a priority:

#### OPS.3.1.A1 Creation of a rough concept for the outsourcing service

A rough concept for the offered outsourcing service MUST be created. This rough concept MUST take into account the conditions of outsourcing (eg special requests) and answer basic questions about the security level and the security requirements of the outsourcing customer.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in outsourcing for service providers. They SHOULD be implemented in principle.

#### OPS.3.1.A2 Contract Design with Outsourcing Clients [ISB Outsourcing Service Provider]

All aspects of the outsourcing project with the outsourcing customer SHOULD be settled in writing in order to fulfill the order as desired and to ensure the required level of security. All responsibilities and obligations to cooperate for the preparation, testing and modification (eg of persons) within the framework of the contract or directly in the security concept between the outsourcing service provider and the outsourcing customer SHOULD be regulated.

#### OPS.3.1.A3 Creation of a security concept for the outsourcing project [ISB outsourcing service provider]

The outsourcing service provider SHOULD own a security concept for its services. For individual outsourcing projects, he SHOULD also create specific security concepts based on the associated security requirements of the outsourcing customer. Between outsourcing service providers and outsourcing customers SHOULD develop common security goals and a common classification for all vulnerable information. The implementation of the security concept SHOULD be checked regularly.

#### OPS.3.1.A4 Definition of possible communication partners [Head of Organization, Data Protection Officer, ISB Outsourcing Service Provider]

It should be determined between outsourcing service providers and customers which internal and external communication partners may transmit and receive which information about the respective outsourcing project. It SHOULD be checked regularly whether the communication partners are still currently employed in their function. The permissions SHOULD be adjusted for changes. Between the outsourcing partners it SHOULD be regulated according to which criteria which communication partners are allowed to receive which information.

#### OPS.3.1.A5 Regulations for the use of the staff of the outsourcing service provider [Head of Human Resources, ISB Outsourcing Service Provider]

Employees of the outsourcing service provider SHOULD be instructed in their tasks and informed about existing information security regulations of the outsourcing customer. Employees of the outsourcing service provider SHOULD be bound in writing to comply with relevant laws, regulations, confidentiality agreements and internal regulations. It SHOULD give representation arrangements in all areas.

#### OPS.3.1.A6 Regulations for the Use of External Personnel [Head of Personnel, ISB Outsourcing Service Provider]

If the outsourcing service provider uses external personnel, the outsourcing customer SHOULD be informed about this. External employees with outsourcing responsibilities SHOULD be required to be bound by the relevant laws, regulations and internal regulations in writing. They SHOULD be instructed in their tasks and especially in the safety requirements. Short-term or one-time deployed foreign personnel SHOULD be treated like visitors.

#### OPS.3.1.A7 Creation of a client concept by the outsourcing service provider [ISB outsourcing service provider]
A suitable client concept SHOULD ensure that application and data contexts of different customers are clearly separated. The client concept SHOULD be created by the outsourcing service provider and made available to the outsourcing customer. The client concept SHOULD provide adequate security for the protection needs of the outsourcing customer. The required mechanisms for client separation at the outsourcing service provider SHOULD be implemented sufficiently.

#### OPS.3.1.A8 Agreement on the connection to networks of outsourcing partners [ISB outsourcing service provider]

Before the connection of a separate network to the network of the outsourcing service provider, all security-relevant aspects in an agreement SHOULD be determined in writing. It SHOULD be defined who is allowed to access the areas and services of the other network from one network. There should be a contact person on each side for both organizational and technical issues of the network connection. On both sides, all identified vulnerabilities SHOULD be eliminated and the required security level demonstrably achieved before the network connection is activated. In case of security problems on one of the two sides SHOULD be determined who should be informed about it and which escalation steps are to be initiated.

#### OPS.3.1.A9 Agreement on Data Exchange between the Outsourcing Partners [ISB Outsourcing Service Provider]

For the regular data exchange with fixed communication partners of the outsourcing partners, the necessary security measures SHOULD be agreed. Data formats and the secure form of data exchange SHOULD be specified. Contact persons for both organizational and technical problems and in particular for security-relevant events when exchanging data with third parties SHOULD be named. Availabilities and response times when exchanging data with third parties SHOULD be agreed. It SHOULD be determined which exchanged data may be used for which purposes.

#### OPS.3.1.A10 Planning and maintaining information security in ongoing outsourcing operations [ISB Outsourcing Service Provider]

The outsourcing customer SHOULD create an operating concept that takes all relevant safety aspects into account. The security concepts of the outsourcing partners SHOULD regularly be checked for up-to-dateness and consistency. The status of the agreed security measures SHOULD be checked regularly. There should be regular communication between the outsourcing partners, including coordination on changes and improvements.

The outsourcing partners SHOULD regularly conduct joint exercises and tests to maintain safety levels. Information about security risks and their handling SHOULD be exchanged between the outsourcing partners on a regular basis. There SHOULD exist a process that ensures the flow of information in dealing with security incidents affecting the respective contractors.

#### OPS.3.1.A11 Access, Access and Access Control [Head of Organization, ISB Outsourcing Service Provider]

Access, access and access rights SHOULD be regulated, both for outsourcing service personnel and outsourcing customers. It should also be regulated which permissions auditors and other examiners receive. It should always be awarded only as many rights as it is necessary for the task perception. It SHOULD provide a regulated procedure for the allocation, management and withdrawal of entitlements.

#### OPS.3.1.A12 Change Management [IT Operations, Change Manager]
There should be guidelines for making changes to IT components, software or configuration data. It SHOULD be stipulated that security aspects should also be taken into account when making changes. All changes SHOULD be planned, tested, approved and documented. The nature and extent of the documentation on the changes SHOULD be coordinated and provided with the outsourcing customer. SHOOTING solutions should be worked out before changes are made. For larger, security-relevant changes, the information security management of the outsourcing institution SHOULD be involved in advance.

#### OPS.3.1.A13 Secure migration for outsourcing projects

For the migration phase, a security management team of qualified employees of the outsourcing customer and the outsourcing service provider SHOULD be set up. For the migration phase, a security concept SHOULD be created. After completing the migration, the security concept SHOULD be updated. It SHOULD be ensured that all exemptions are lifted at the end of the migration phase. In the case of changes during the migration phase, the extent to which there is a need to adapt to the contractual basis and existing documents should be examined.

#### OPS.3.1.A14 Emergency Preparedness for Outsourcing [Emergency Response Officer]

There SHOULD exist an outsourcing contingency plan that includes the components of the outsourcing customer, the outsourcing service provider and the associated interfaces. In the emergency precautionary concept for outsourcing, the responsibilities, contact persons and processes between outsourcing customers and outsourcing service providers SHOULD be regulated. Regular emergency exercises should be carried out by outsourcing clients and outsourcing service providers.

#### OPS.3.1.A15 Orderly termination of an outsourcing relationship [Institutional Management]

It SHOULD be ensured that termination of the contractual relationship with the outsourcer does not affect his or her own business. The Outsourcing Contract with the Outsourcing Client SHOULD govern all aspects of the termination of the service relationship, both for a planned and an unplanned termination of the contractual relationship. The outsourcing service provider SHOULD hand over all information and data of the outsourcing customer to them. At the outsourcing service provider, all data stocks of the customer SHOULD then be securely deleted. All permissions set up as part of the outsourcing project SHOULD be reviewed and, if necessary, deleted.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### OPS.3.1.A16 Security check of employees [Head of Personnel] (CI)

The trustworthiness of new employees and external personnel at the outsourcing service provider SHOULD be verified by appropriate evidence. For this purpose criteria should be contractually agreed together with the outsourcing customer.
