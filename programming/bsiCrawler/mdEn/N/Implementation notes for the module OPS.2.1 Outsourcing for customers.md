1 description
--------------

### 1.1 Introduction

Nowadays more and more institutions are deciding not to perform their own processes and activities themselves, but outsource them to a third party - an external service provider. This decision is usually made because of the many opportunities that such an outsourcing project can bring. Among other things, significant costs can be saved, external resources can be used flexibly, or resources can be relieved to concentrate more on one's own core competencies. However, these opportunities are always accompanied by considerable risks (high dependence on external service providers, loss of control and control, information security risks), which not only cause the outsourcing project to fail, but in the worst case, the existence of the outsourcing companies Endanger institution. An example of this would be the unauthorized publication of strictly confidential business strategies of the outsourcing institution by employees of the outsourcing services provider. This makes it all the more important to adequately address all risks associated with the outsourcing project. In order to achieve this goal, measures are described below which the outsourcing customer should consider or implement during each phase of an outsourcing project.

### 1.2 Life cycle

Starting with the preparation of a rough concept and a strategy for the outsourcing project, the choice of the right service provider and the subsequent contract design up to safe migration and regular operation, an outsourcing project has to face a large number of security risks. The steps that should be taken and the measures that must be followed in order to do so are described below.

** planning and conception **

In order for an outsourcing project to be successfully implemented, all necessary framework conditions for the project should be defined in advance of the actual outsourcing.

This includes strategic considerations, such as the consideration of opportunities and risks. In addition, a decision must be made regarding the outsourcing model, which supports the realization of the expectations of the outsourcing project (OPS.2.1.M5 definition of an outsourcing strategy). Furthermore, security standards are to be defined in advance which should apply to the outsourcing project. These become a potential outsourcing partner to security requirements (OPS.2.1.M1 establishing security requirements for outsourcing projects). Employees and their representatives must also be informed in good time about the outsourcing project (OPS.2.1.M2 Timely participation of the Staff Committee). In addition, regulations must already be defined in the planning as to how the secure deployment of external personnel is ensured in the course of cooperation with the service provider (see OPS.3 Outsourcing for service providers).

**Implementation**

In addition to the security requirements, all other requirements that an outsourcing partner must meet must be individually defined for each outsourcing project in order to enable objective comparisons and to identify an optimal outsourcing partner (OPS.2.1.M3 Selection of an appropriate outsourcing partner). service provider).In order to achieve the set outsourcing goals, all necessary services, which must be provided by the outsourcing service provider, should be contractually fixed (OPS.2.1.M4 contract design with the outsourcing service provider). For each outsourcing project, a security concept should be developed, which takes into account the individuality of the combination of customers, service providers and the outsourced process (OPS.2.1.M6 Creation of a security concept for the outsourcing project). Once the security concept has been established, it must be ensured that information security maintenance measures (OPS.2.1.M11 planning and maintenance of information security in ongoing outsourcing operations) are implemented so that a security concept actually works and is not outdated.

Likewise, the communication channels and the secure migration of processes and tasks are defined in this phase (OPS.2.1.M7 definition of possible communication partners, OPS.2.1.M13 Secure migration for outsourcing projects).

With regard to the network connection and the data exchange with the outsourcing service provider, regulations have to be made, since normally many processes are dependent on this. However, the service providers are independent and, as third parties, not directly in the sphere of influence of the customer (see OPS.2.1.M9 Agreements for the connection to networks of the outsourcing partners and OPS.2.1.M10 agreements on data exchange between the outsourcing partners).

** operation and separation **

During operation, all agreed parameters should be checked regularly. In addition to the monitoring of defined key performance indicators, this includes monitoring measures to maintain the information security of the outsourcing service provider (OPS.2.1.M11 planning and maintaining information security in ongoing outsourcing operations).

If a change is desired by one of the parties in the context of an outsourcing project, this should be implemented according to a defined process (OPS.2.1.M12 change management). A change in the outsourcing relationship can also be its termination. In this case, contractual arrangements and arrangements should be made. In particular, in the event of an unexpected end to the outsourcing project (eg due to the bankruptcy of the outsourcing service provider), the absence of such arrangements may result in significant economic damage (OPS.2.1.M15 Orderly Termination of Outsourcing Ratio).

** Emergency Preparedness **

As part of the emergency preparedness, the agreed parameters should also be checked (OPS.2.1.M14 emergency provision for outsourcing).

2 measures
-----------

The following are specific implementation notes in the Outsourcing for Customers section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### OPS.2.1.M1 Definition of security requirements for outsourcing projects [ISB outsourcing customer]

An outsourcing project must establish security requirements that are in line with the outsourcing strategy. These should serve as the basis for the selection of an outsourcing service provider and the subsequent contract design (OPS.2.1.M3 selection of a suitable outsourcing service provider, OPS.2.1.M4 contract design with the outsourcing service provider and OPS.2.1.M11 planning and maintenance of information security).

The security requirements can be determined, for example, based on IT-Grundschutz.

In order to achieve the required level of security, outsourcing customers and outsourcing service providers should jointly develop security goals and security requirements based on them, which take into account the individuality of the respective outsourcing project.In these considerations, all interfaces between outsourcing customers and outsourcing service providers with the respective security requirements must be included. All aspects of identity and entitlement management should be considered. For this purpose, z. For example, all participating users can be assigned to specific groups (administrator, controller, employee, etc.), whereby each group receives certain rights that it absolutely needs in the course of its activity. Another possibility is the definition of certain roles, i. H. the summary of certain rights. Users who complete one or more specific roles as part of their work in the outsourcing project will then be granted the necessary rights.

In any case, when granting rights, the * least privilege principle * should be observed. Thus, all users receive only the necessary rights. The risk of intentionally or negligently caused security incidents can thus be reduced (see also OPS.2.1.M6 Creation of a security concept for the outsourcing project).

In order to allocate access rights adequately, it is necessary to classify all data and information. The classification must be made according to the strategic importance.

It should be noted that setting security requirements is an iterative process:

* First, the desired security requirements are specified by the customer.
* Then, in the bidding phase, a comparison is made as to how and whether the required security requirements can be met by the offering service providers.
* If a service provider is selected, then this must be used to develop the further refinement of the security requirements (eg based on the operating systems or security mechanisms used). In the final phase of this coordination process, the security requirements for the concrete implementation must then also be defined.
In general, the following minimum security requirements arise for outsourcing scenarios:

* The implementation of IT-Grundschutz or a comparable level of protection is a minimum requirement for both outsourcing parties. In addition, both outsourcing service providers and outsourcing customers themselves must have a security concept and have implemented it.
* It is important to delineate the relevant IT networks exactly (for example, according to specialist task, business process, IT systems) so that all interfaces can be identified. Appropriate technical security requirements can then be set for the interfaces.
* There must be an actual structural analysis of IT systems and applications.
* There must be a need for protection (such as applications, systems, communication links, rooms) regarding confidentiality, integrity and availability.
Of course, relevant laws and regulations must be observed. This can be particularly costly in cases where customers or service providers operate transnationally or globally.

As part of the security requirements, it must be determined which rights (eg access rights, access rights to data and systems) are assigned to the outsourcing service provider by the customer.

The requirements for infrastructure, organization, personnel and technology must be described. It is often sufficient here to meet a security level that corresponds to IT-Grundschutz. If any additional requirements exist, these must be described in detail. This depends crucially on the security strategy and already existing systems and applications. For example, the following points could be detailed depending on the outsourcing project:

** Organizational regulations and processes **

* Requirements for safety-critical organizational processes (eg time restrictions for the alerting plan) can be specified.* Specific requirements for specific roles can be specified. For example, it may be required that an ISB with special knowledge (eg host knowledge) must be appointed to the outsourcing service provider.
** hardware / software **

* The use of certified products (eg according to Common Criteria or ITSEC) by the outsourcing service provider may be required.
* Requirements for the availability of services and IT systems can be provided. For example, in this context, the degree and method of load distribution (eg for web servers with customer access for very many customers) can be specified.
* Requirements for multi-client capability and the related separation of hardware and software can be formulated. For example, it can be stipulated that no IT systems of the customer may be accommodated in rooms in which systems of other clients of the service provider already exist.
**Communication**

* Special procedures for securing the communication between service provider and client, such as the use of encryption and signature procedures, can be specified.
** Controls and QS **

* General requirements for control and measurement of safety, quality or even procedures and organizational regulations can be specified, eg. B. Time intervals, responsibilities.
* Desired procedures or mechanisms for control and monitoring, such as unannounced on-site inspections, audits (possibly by independent third parties) may be specified.
* Requirements for logging and evaluation of log files can be specified.
In general, the defined IT security requirements form one of the foundations for choosing a suitable outsourcing service provider. However, specific IT security requirements may need to be adjusted to the IT security level that service providers can deliver.

In the case of tenders or the selection of an outsourcing service provider, a specification of services or a specification should always be created with the following contents:

* Description of the outsourcing project (task description and task sharing) as well as
* Descriptions of the required quality level, which does not necessarily have to correspond to the client's level,
* Information security requirements and
* Criteria for measuring service quality and safety.
In individual cases, it may be necessary to issue the detailed security requirements only against a non-disclosure agreement to service providers, since this can be used to derive indications of existing or planned security mechanisms.

Together with the basic measures, the following measures correspond to the state of the art in outsourcing for service providers.

Together with the basic measures, the following measures correspond to the state of the art in the field of outsourcing for customers.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of outsourcing for customers.

#### OPS.2.1.M2 Timely participation of the Staff Committee [Head of Organization]The timely and comprehensive information of the staff representatives is generally recommended for all projects that affect the operational interests of the employees. This generally includes outsourcing projects. An early involvement of the staff representation of the outsourcing customer is recommended, possibly already in the bidding phase. This can contribute to the success of the project. Early involvement can prevent time delays in implementing measures and increase acceptance for the outsourcing project. Employee willingness to change, motivation, job satisfaction and speedy project completion can all be positively influenced by cooperation between all parties involved. In addition, the expertise of those employees who later work in the context of the concrete processes surrounding the outsourcing project is a success factor that should not be underestimated during implementation.

The legal basis of the participation of the staff representation in Germany are the company constitution and personnel representation laws of the federal and state governments as well as individual provisions of the Civil Code (BGB).

Outsourcing projects are often accompanied by measures that, in principle, enable employee behavior or performance monitoring. This requires z. B. the co-determination of the Staff Committee.

The transfer of tasks or processes of an institution to a third party usually also leads to changes in the personnel structure, which also necessitates the involvement of the staff representatives. This can also mean that after the implementation of an outsourcing project, employees have to switch from the outsourcing customer to the service provider. For the customer, ie the original employer, there is an obligation to inform in this case. The employees are to be informed in writing before the transfer of the undertaking. Employees do not have to be individually trained, but it is advisable to address the specific impact on specific groups of workers individually. Contents of the information are specified in § 613a Abs. 5 BGB.

The consequences for the constitutional bodies themselves must also be examined as part of an outsourcing project. For this it is recommended to consult a professional legal advice.

#### OPS.2.1.M3 Selection of a suitable outsourcing service provider [ISB Outsourcing customer]

Since the selection of the outsourcing service provider is a far-reaching and risky decision, clear selection criteria should be defined for each outsourcing project. The following are examples of evaluation criteria that should be considered when deciding on an outsourcing service provider.

** Transparency of operation and safety precautions **

The outsourcing service provider should be able to present the processes that are fundamental to its service provision in such a transparent manner that it can be assumed that it fulfills the contract without any doubt. The outsourcing client should also be aware of the security arrangements that the outsourcing service provider has made for the specific outsourcing project, if necessary. In particular, this should enable a smooth interaction of the security mechanisms between the outsourcing partners.

** Security requirements check **

The outsourcing customer must consider the security requirements of the outsourcing service provider to the extent that the outsourcing service provider covers at least the desired security level of the outsourcing customer. For example, if the outsourcing customer demands a high protection requirement, the outsourcing service provider must at least meet the requirements for a high protection requirement.

**Reputation**The reputation of a service provider in the market can not be quantified. Reports from other customers, media reports and also the active public presence of the service provider can be considered qualitatively.

** References and certifications **

The service provider should have references for similar outsourcing projects. It is important to pay attention to conflicts of interest through business relationships with competitors of the customer.

The specified references should be questioned at least randomly. Thus, existing or former customers of the potential service provider can be interviewed about their project experience with the service provider.

Depending on requirements, the service provider should implement relevant safety standards, eg. Eg ISO 27001 based on BSI IT-Grundschutz. In the case of existing certifications, the outsourcing customer must ensure that the scope and protection requirements contained in the certificate include the area of ​​application required by the outsourcing customer. For this purpose, a test of the certified scope is required.

** Business Fit / Corporate Culture **

For foreign service providers special aspects must be considered. These include, for example: foreign legislation, other liability regulations, espionage risks, other security culture, security mechanisms that are permitted and usable in the partner company or by country-specific legislation.

In addition, the organization of the service provider should be considered, as these z. B. can affect the liability limits. Furthermore, the ownership structure should be researched to clarify potential influencing factors in advance.

Finally, it should be checked to what extent the described aspects are compatible with the customer's situation or ideas.

** requirements for employees **

Requirements are also to be made of the employees of an outsourcing service provider.

The outsourcing customer should check to what extent the outsourcing service provider has the required qualifications. In addition, the number of available qualified employees should be assessed. Representative arrangements and working hours should also be questioned.

When choosing foreign partners, a common language for communication between their own employees and those of the service provider must be established. It should also be questioned whether the existing language skills are sufficient for the clarification of detail problems. In addition, aspects such as different time zones or legal peculiarities must be taken into account.

Depending on the required level of security for the outsourcing project, it should be checked if necessary whether a security check of the employees is available or can be carried out without complications.

#### OPS.2.1.M4 Contract Design with the Outsourcing Service Provider [ISB Outsourcing Client]

Outsourcing contracts are not, as purchase, work or service contracts, in the Civil Code (BGB) regulated. It is therefore important to agree in writing all aspects of an outsourcing project when drafting the contract. The contract should stipulate both the required rights and obligations of the outsourcing partners. The type, scope and level of detail of the contractual arrangements should be individually adapted to the outsourcing project. Contractual arrangements in advance are particularly important because many risks can be reduced or avoided in advance for the outsourcing customer. The following aspects should therefore be taken into account in the view of the outsourcing customer in the course of each contract design.

** Clear specification and definition of performance **An inaccurate definition of service provision often leads to additional and unpredictable additional costs for the outsourcing customer, as he, for example, has to claim a supposed "additional service" from the outsourcing service provider. Claims by the service provider for compensation for additional services can be better assessed if the service to be provided has been clearly defined. Appropriate discussions or disagreements that could cause lasting damage to the business relationship between the contracting parties are thereby avoided in the best possible way. In addition, the risk of loss of control and control options can be counteracted if the outsourcing institution can more easily identify or prove deviations by means of a clear deferred income. In this context, the outsourcing customer also creates a contractual basis for possible sanctions or claims for damages in case of poor or non-performance.

**Data protection and data safety**

Furthermore, regulations for compliance with data protection regulations should be specified. These include u. a. Safety precautions that the outsourcing service provider must follow in the course of data processing. This is to ensure that the outsourcing partners comply with the statutory provisions of the Federal Data Protection Act (BDSG) and protect the confidentiality, integrity and availability of data and information. The contract should specify the necessary organizational measures that must be taken by the outsourcing service provider to prevent unauthorized access to the data of the outsourcing customer. In particular, the focus should be on protecting the systems against unauthorized or accidental destruction, accidental loss, technical errors, counterfeiting, theft, misappropriation, unauthorized modification, copying or access. In addition, it should be specified how the confidentiality of data should be protected by technical, human and organizational measures. If necessary, additional agreements to safeguard the business secrecy of the customer must be contractually regulated.

** Infrastructure (see eg building block INF.2 data center) **

* Scope of the shared infrastructure
* Requirements of the outsourcing customer to secure the shared infrastructure
* The property rights of all components of the infrastructure
** Organizational regulations / processes (see, for example, module ORP.1 Organization) **

* Non-Disclosure Agreements must be contractually agreed. This should already be taken into account during the contract design phase itself, as security requirements of the outsourcing customer may allow conclusions to be drawn about existing security systems.
* Definition of communication channels and contact persons
* Definition of processes, work processes and responsibilities
* Integration of the service into the value added process of the outsourcing customer
* Division of labor during service provision / cooperation obligations of the outsourcing customer
* Procedures for solving problems, naming contact persons with the necessary authority in both contracting parties
* Regular voting rounds
* How to adjust performance
* Archiving and deletion of data (especially at termination of the contract)
* Accessibility of the outsourcing service provider to IT resources of the outsourcing customer: who accesses which system? What are the responsibilities and rights?
* Access and access rights for outsourcing service provider staff to the Outsourcing customer's premises and IT systems* Access and access rights for employees of the outsourcing customer to the premises and IT systems of the outsourcing service provider
* physical repository of data
** Personnel (see, for example, module ORP.2 Personnel) **

* Designing the workplaces of outsourcing service personnel that are deployed to the outsourcing customer (eg compliance with the VDU workplace policy)
* Definition and coordination of representation arrangements with both contracting parties
* Commitment to training
** Regulations in the context of emergency preparedness **

In the context of emergency preparedness, at least the following aspects should be regulated to ensure continuous business continuity:

Categories to classify errors and incidents by type, severity and urgency
* Required measures when an accident occurs
* Response times and escalation levels
* Obligation of the outsourcing service provider to cooperate in the resolution of emergencies
* Type of involvement and timing of emergency exercises at the outsourcing service provider
* Requirements of the outsourcing customer on the type and extent of data backup
* Agreement on whether or which systems must be designed redundantly
Of particular importance may be regulations in case of force majeure. Furthermore, it should be clarified, for example, how a strike of the staff of the outsourcing service provider ensures the availability of data and systems. Especially when outsourcing service providers and outsourcing customers belong to different industries or are located in different countries, the customer can be completely surprised by such occurrences.

 ** Next relocations **

 ** client separation **

In the context of client separation, the outsourcing service provider must ensure that disruptions or emergencies in outsourcing customers do not affect the processes and systems of other customers. In addition, under no circumstances may the data of the outsourcing customers be made available to other customers.

The outsourcing service provider should therefore be contractually obliged to create a client concept that describes how the IT systems and applications run in a client-capable manner. If necessary, a physical separation, i. H. dedicated hardware, to be agreed. Furthermore, it can be specified that the employees employed by the outsourcing service provider are not used for other outsourcing customers.

** Change Management and Testing **

Contractual arrangements must be established that allow the outsourcing customer at any time to adapt to new requirements. This applies in particular if, for example, legal requirements change. It is necessary to determine how to react to system extensions, increased requirements or scarce resources.

In this context, the supervision and further development of already existing systems must be regulated. It is not uncommon for the outsourcing service provider to take over proprietary systems or software from the outsourcing customer, which is no longer able to develop it in his or her own right. The evolutionary path of systems should therefore also be regulated by contract.

A continuous improvement of the service quality and the security level should be as precise as possible in the Service / Security Level Agreements (SLA). This applies both to the respective time frame for the correction of errors and to the tracking of security requirements.

Furthermore, test procedures for new hardware and software should be defined. The following points should be included:

* Regulations for updates and system adjustments
* Separation of test and production systems
* Responsibilities in the creation of test concepts
* Specify test models to use* Responsibilities of outsourcing customers and outsourcing service providers in the performance of tests (eg cooperation or assistance of the outsourcing customer, acceptance and approval procedures)
* Duty to Inform and Agree on Major Interference with a System (Negative Example: The outsourcing service provider is installing a new version of the operating system on the server.) Unexpected errors disrupt important applications without the outsourcing customer being able to prepare.)
* Approval procedure for conducting tests
* Determination of reasonable quality losses during the test phase (eg availability and capacity)
** Control and Examination Rights **

The quality of the service provision must be checked regularly. The outsourcing customer must be contractually guaranteed the necessary information, access, access and access rights to the premises used by him. If independent third parties are to carry out audits or benchmark tests, this must also be regulated in the contract.

All institutions which have to carry out examinations with the outsourcing customer (eg supervisory authorities) must also be able to exercise the corresponding control options (eg access rights, data access) with the outsourcing service provider.

In order to ensure audit and control capabilities, the outsourcing agreement should include a statement from the outsourcing service provider specifying an unannounced, if unannounced, audit of the outsourced outsourcer scope.

** Information requirements and communication **

The service provider should be contractually obliged to report on any developments that could affect service delivery. This should enable the outsourcing customer to react in a timely manner. It should also be ensured that the outsourcing service provider regularly reports on current (security) incidents or problems with internal workflows. In this regard, z. B. Results of revisions relevant.

In order to ensure an adequate flow of information, z. For example, the type of information, the communication paths to be used and the respective contact persons (roles) to which certain information should be forwarded, are contractually established.

Rules should be specified for the end of the outsourcing relationship. In any case, periods of notice should be agreed and sufficiently dimensioned. With regard to the dimensioning of notice periods, care must be taken to ensure that the outsourcing customer has sufficient time to re-integrate the outsourced activities and processes or to transfer them to another outsourcing service provider.

In addition, if necessary, the outsourcing service provider may be required to provide assistance in the course of a re-integration or transfer of service provision to another outsourcing service provider even after the end of the outsourcing relationship.

Furthermore, the outsourcing service provider is contractually obligated to return or destroy all hardware and software, including the data stored on it, which were originally in the possession of the outsourcing customer after the end of the outsourcing relationship.

#### OPS.2.1.M5 Defining an Outsourcing Strategy [ISB Outsourcing Client]

Outsourcing projects often have many advantages. However, these benefits are offset by a number of risks that can result in the desired goals being missed. In addition, the commitment to an outsourcing service is usually for a long time. Strategic planning of the outsourcing project is therefore of great importance.Economic, technical and organizational aspects should be considered here. In addition, security-relevant aspects play an important role. Information security has to be taken into consideration right from the beginning of planning, as it plays a key role in outsourcing projects.

** Definition of outsourcing goals **

In each outsourcing strategy, the goals of the project should be defined precisely. At the same time, compliance with the safety guideline should always be ensured. For example, the outsourcing goals must not contradict the overarching goals of the institution and the security objectives derived from it. The following aspects should be considered:

* Security guideline (flexibility, dependencies, future plans),
* Feasibility study with compilation of framework conditions and
* Business aspects with cost-benefit assessment.
After initial strategic considerations, it must first be clarified which business processes, tasks or applications are generally eligible for outsourcing.

The importance of the legal framework should not be underestimated. For example, laws could generally prohibit the outsourcing of certain core tasks of an institution, or at least impose far-reaching requirements and require the involvement of regulators. As a rule, the client remains fully accountable to his customers or government agencies for services or products, regardless of whether individual areas of responsibility have been outsourced.

Unfortunately, information security is often neglected at the beginning of planning, although it is of central importance. This applies both to technical and organizational security aspects, which play a decisive role in the outsourcing scenario. In general, one has to keep in mind:

* The decision to outsource is usually not easy to revise. The commitment to the service provider may be very long term.
* A service provider often has access to customer data and IT resources. The outsourcing customer loses sole and complete control over data and resources. Depending on the outsourcing project, this then also concerns data with high protection requirements.
* For the technical implementation of the outsourcing project, it is necessary that data is transferred between the customer and the service provider. This automatically results in an increased risk potential.
* As a rule, it is necessary that employees or subcontractors of the outsourcing service provider (and therefore outsiders) have to work temporarily in the customer's premises. This also results in an increased risk potential.
* As part of an outsourcing project, new processes and workflows need to be designed, implemented and implemented. The consequences of the necessary changes must be clarified and estimated.* For each outsourcing service provider there is a conflict of interest that should not be underestimated: on the one hand, it has to provide the service as cost-effectively as possible in order to maximize its profit; on the other hand, the outsourcing customer expects high service quality, flexibility and customer-friendly behavior. Experience has shown that this point is the most underrated. While IT managers tend to be very critical and cost-conscious, and are very skeptical about promises made by manufacturers and consultants, outsourcing is often the opposite. All too easily, the customer forfeits the advertising slogans of the service providers in the expectation that they will be able to significantly reduce their IT costs. However, practice teaches that at most the services provided in the future, which have been contracted from the beginning, will be provided. If it turns out that the service quality is inadequate because the customer expects services that he takes for granted - in contrast to the outsourcing service provider - improvements are generally not expected without high additional costs. Any IT manager who thinks about outsourcing should take the trouble to figure out at what cost a service provider must deliver the agreed service, so that both the customer and the service provider benefit from the contract. With this calculation, it may turn out that a serious service delivery at the promised low cost is highly unlikely.
In order to define the outsourcing strategy, an individual security analysis must always be carried out. Only in this way can it finally be determined how existing business processes or information networks can be delimited and separated so that parts of them can be outsourced. Naturally, in this early phase of the project, the security concept will only describe general conditions and will not contain any detailed measures. The safety analysis should be carried out according to the methodology described in the IT-Grundschutz approach:

* A structural analysis should first be carried out to determine the current status.
* Thereafter, a determination of protection is required.
* Building on this, appropriate security measures must be selected and adapted to the respective framework conditions of the outsourcing project. At the same time, the need for action, the priorities and the costs of the measures to be implemented must be identified. The results can then be included in particular in the consideration of the profitability of the outsourcing project.
If the protection requirements of important systems or applications are high or if the modeling of the information network according to IT-Grundschutz is not possible, a supplementary safety analysis (eg risk analysis) must be carried out. Once the safety-related hazards have been analyzed, it can be determined whether and how this should be addressed.

Ultimately, however, a certain residual risk will be borne by the outsourcing customer. The results of the safety analysis are directly included in the cost-benefit assessment.

When developing a promising long-term outsourcing strategy, management must not focus solely on cost savings. The impact of an outsourcing project on task fulfillment, business model and service or product portfolio must also be considered. Should standard processes or core business processes be outsourced? It is important in this context that the ability to determine and control requirements for IT itself is sufficiently maintained. In particular, the further development and maintenance of self-developed IT systems and applications should be considered.The following opportunities, which are generally associated with an outsourcing project, can be formulated as goals for the outsourcing customer:

* Cost Benefits: Reducing the cost of service delivery and the associated increase in productivity continue to be the main motive for outsourcing customers. B. be achieved by staff savings. Both wages and salaries, as well as costs for qualification and further training are allocated to the outsourcing service provider. Fixed staff costs can thus be converted into variable service costs, which can be adapted as needed in a timely manner. Also needs of resources such. For example, the IT infrastructure can be quickly adapted without increasing the investment risk.
* Focus on core competencies: Outsourcing certain processes can relieve management, IT operations or other departments of expertise so that they can focus on their core competencies. This frees up staff capacities that can be used elsewhere.
* Improvement of the security level: Ideally, the outsourcing project can achieve a better level of security. The outsourcing service provider is usually characterized by a high degree of specialization in his area of ​​expertise. Particularly in information security, relevant know-how is required in order to regularly evaluate current security notices, security bulletins, update notifications and bug reports, to recognize their relevance and, if necessary, to take the right steps quickly. In addition, outsourcing service providers can adapt the implementation of security patches or security-relevant system configurations to the production of the outsourcing customer, so that operations are not disturbed by these processes.
Competency Islands: Internal IT departments often do not grow to the same extent as the organization they are responsible for. A patchwork of workarounds and other temporary security solutions can be the result. In addition, few, if not one, employee will be able to survey the entire IT infrastructure. If these employees fail or leave the organization of the outsourcing customer, serious security deficiencies result since the IT infrastructure maintenance expertise no longer exists. By contrast, the outsourcing service providers can usually rely on several equally qualified experts who can represent each other. In addition, they have a homogenous IT infrastructure, which, due to its high degree of standardization, is easier to maintain, especially from a safety point of view, and has a higher resilience.* Utilization of external know-how and improvement of the range of services: Another outsourcing motive can be the use of external know-how, without having to own it or develop it yourself. This in turn results in cost savings potential. In addition, the quality of service provision can be increased by using the specialist knowledge of the outsourcing service provider. More efficient process design and low-risk diversification can also be achieved by reducing vertical integration. Outsourcing clients can focus their skills on lean value-added processes that are supported by specialized outsourcing service providers. Also in this context, supporting an outsourcing service provider can potentially help improve overall security levels. Due to their specialization, outsourcing service providers will often be better equipped to evaluate dynamic security situations and initiate immediately necessary steps. Especially with regard to new IT solutions and the associated increasing complexity, a specialized service provider can be useful, which can keep the balance between security and an extended range of services or more functionality.
* Risk transfer: In addition to the transfer of investment risks already mentioned, another advantage is the outsourcing of additional risks, such as: Eg misconduct of employees, software errors or the occurrence of disasters. However, failures of this kind do not only affect the outsourcing service provider but can always fall back on the outsourcing customers. Even with a contractually agreed complete transfer of risks to the outsourcing service provider, it remains questionable to what extent this can be paid in the event of liability.
** Risks and Challenges **

The outsourcing goals are offset by a number of versatile outsourcing risks. These risks should be described in the outsourcing strategy and, as a result, taken into account in each outsourcing project. The following describes possible risks of an outsourcing project.

* Hidden costs: An outsourcing project is not just about cost savings. The associated costs should be carefully analyzed and weighed in advance. So z. For example, to include costs for controlling the outsourcing project and contract management. During an outsourcing relationship, there may be unexpected communication and coordination costs on the outsourcing client side. If the scope of the outsourcing project is underperformed, any adjustments will be necessary during the contract relationship. Such contract changes can sometimes entail substantial additional costs. In addition, one-time costs may arise. These include, for example, severance payments or costs for new hires incurred in the course of personnel restructuring.* Loss of know-how: The benefits of using external know-how also entail risks. Thus, the permanent use of the expertise of third parties usually causes the loss of their own know-how. Employees of the outsourcing customer often give up their expertise in the course of an outsourcing project, or do not maintain it. The competence for outsourced functions is ultimately no longer in the hands of the outsourcing customer. Particularly critical is such a situation when the know-how of the employees of the outsourcing service provider is no longer adequate and thus serious security vulnerabilities arise, but these are not discovered because the required expertise is no longer available at the outsourcing customer. The loss of one's own know-how inevitably increases dependence on the outsourcing service provider.
* Dependence on the outsourcing service provider: The dependence of the outsourcing customer on the outsourcing service provider increases in particular with the complexity of the outsourced process and with the duration of the outsourcing relationship. For the outsourcing customer, there is always the risk of a price increase by the outsourcing service provider after the outsourcing project is well advanced and backward integration would not be economical or too risky. As a result, cost increases often need to be accepted, which can greatly affect the profitability of the outsourcing project in retrospect. The resulting cost savings, in turn, often lead to savings in the security area and have a corresponding impact on the security level.
* Reputation and loss of trust: The impact on outsourcing customers resulting from performance shortcomings of the outsourcing service provider can lead to far-reaching consequences. Corresponding consequences, such. Regardless of whether the debt originally lies with the outsourcing service provider, for example, a loss of reputation or trust occurs to outsourcing customers themselves.
* Loss of control and oversight: The outsourcing customer generally has limited authority over the outsourcing service provider. This results in limited control options and an increased need for coordination in comparison with self-provision. The control options of the outsourcing customer are also limited. Despite agreed access rights, the outsourcing customer will not have all the information regarding the organization and processes of the outsourcing service provider.
* Third party insight into internal operations and data: Depending on the nature of the outsourcing project, the outsourcing service provider may receive information about internal operations and possibly also business relationships of the outsourcing customer. Thus, for the latter, a sole control over this information is no longer ensured. It may also be necessary for outsourcing service providers to work, at least temporarily, on the premises of outsourcing clients, thereby facilitating their access to data and resources. If disclosure of information is personal data, the relevant data protection laws must also be observed.Data security risks: Security of data is an essential aspect of outsourcing. Especially risks resulting from the loss of the availability of systems and data, eg. For example, in case of a system failure of an IT outsourcing, are considered. In general, the involvement of an outsourcing service provider increases the number of transmission paths and thus also the potential dangers. Typical threats include hacker attacks, malicious programs, hardware and software failure failures, and other damage scenarios, such as: B. by power or air conditioning failures. The IT risks of the service provider have a direct impact on the outsourcing customers. Even minor or partial failures lead to inconsistent or incorrect data processing.
** Description of the procedure for the outsourcing project **

After outlining the outsourcing objectives as well as the outsourcing risks to be considered in the outsourcing strategy, a structured approach to managing an outsourcing project should be outlined. Detailed guidelines for implementation can be described in downstream documents (eg a framework instruction for outsourcing). The approach described is intended to cover the outsourcing risks and thus ensure the achievement of the set goals. As part of the described approach, the following phases of the outsourcing project should be considered:

* Selection of possible outsourcing areas: Which processes and / or activities should not be outsourced due to legal requirements or for strategic reasons (core competencies)? In addition, a cost-benefit analysis must be carried out during this phase, on the basis of which the profitability of the planned outsourcing project can be assessed.
* Recording and assessing the outsourcing issue: What are the individual risks for the situation under consideration, how should they be dealt with and what requirements should be placed on a potential outsourcing service provider?
* Selection of a suitable outsourcing service provider: The selection should be made on the basis of the previously identified risks and the (security) requirements derived from them.
* Contract design: Which aspects have to be regulated by contract?
* Transfer to regular operation: What (safety) measures should be taken in the course of the transfer of service provision to the outsourcing service provider?
* Regular operation and termination: What control, monitoring, control and coordination measures are to be taken during ongoing operation and what precautions must be taken to anticipate or unexpected termination of the outsourcing project?
#### OPS.2.1.M6 Creation of a security concept for the outsourcing project [specialist responsible, ISB outsourcing customer]

For each outsourcing project, there must be a security concept based on the security requirements of the outsourcing client (OPS.2.1.M1 Definition of Security Requirements for Outsourcing Projects).

The overall security concept should be created after commissioning an outsourcing service provider. Outsourcing projects are characterized by the fact that many technical and organizational details only emerge in the course of planning and migration of the systems. Therefore, the safety concept will in most cases not be complete and final right from the start and must be continuously developed and made concrete by all those involved during the migration and operational phases. Special requirements for the security concept for the migration phase (as part of the overall security concept) are described in OPS.2.1.M13 Secure migration for outsourcing projects.In general, security concepts for outsourcing projects differ only slightly from security concepts for self-operated IT systems. However, it has to be considered that additional parties may be involved in an outsourcing project. In addition to the outsourcing service provider, this can be, for example, network providers and subcontractors of the service provider. These, too, must not affect the agreed security objectives. The required security requirements for their areas of responsibility must either be integrated in the security concept of the service provider or be described in independent security concepts, which must be submitted to the outsourcing customer.

Each party involved in the outsourcing project must create and implement its own security concept, which also includes the specific outsourcing project. This requires security concepts:

* for the sphere of influence of the outsourcing customer,
* for the sphere of influence of the outsourcing service provider as well
* for the interfaces and communication between these areas.
Based on this, the outsourcing customer was to create a security concept for the entire system, which considers the security in the interaction of the individual systems.

The various sub-concepts must be coordinated between outsourcing customers and outsourcing service providers. The outsourcing customer is not directly involved in the security concept of the outsourcing service provider, but should check in an audit whether it is available and sufficient. The outsourcing customer can also rely on external third parties for the audit. In the course of the project, all sub-concepts should be continuously checked for up-to-dateness and correctness.

The overall security concept should consider all relevant risks associated with the outsourcing project. Potential risks are described in OPS.2.1.M5 Definition of an Outsourcing Strategy.

The security requirements specified in OPS.2.1.M1 Definition of security requirements for outsourcing projects and OPS.2.1.M4 contract design with the outsourcing service provider form the basis for the overall security concept. Based on the basic requirements described there, the detailed design must take place in the security concept, whereby, for example, the measures are specified and contact persons are specified by name.

Experience has shown that the transition (migration) of tasks and IT systems from the customer to the outsourcing service provider is a project phase in which security incidents are increasingly likely. For this reason, the security concept must deal with migration regulations and measures, which are dealt with in more detail in OPS.2.1.M13 Secure migration for outsourcing projects.

Below are some aspects and topics that should be described in detail in the security concept. Since the details of a security concept depend directly on the outsourcing project, the list is to be understood as a suggestion and makes no claim to completeness. In addition to an overview of the threat situation, which serves to motivate the security measures, and the infrastructural and personnel security measures, measures from the following areas may be useful:

**Organization**

* Dealing with data and resources worthy of protection such as printer paper and storage media, in particular regulations for making copies and deleting / destroying
* Defining actions for which the "four eyes principle" applies
** hardware / software **

* Use hardened operating systems to make attacks as difficult as possible
* Use intrusion detection systems (IDS) to detect attacks early
* Use file integrity checking systems to handle changes such as: B. to detect after successful attacks
* Use of syslog and time servers to enable the most comprehensive logging possible* Use of cascaded firewall systems to increase the perimeter protection on the part of the service provider
* careful assignment of user identifiers, ban on group IDs for the service provider's staff
**Communication**

* Secure communication (eg by encryption, electronic signature) between service provider and customer to protect sensitive data
* Authentication mechanisms
* Detailed regulations for further network connections
* Detailed regulations for data exchange
** Controls and QS **

* Detailed regulations (eg unannounced on-site inspections, time intervals, responsibilities, level of detail) for controls and measurement of safety, quality of service, procedures and organizational arrangements
** Emergency Preparedness **

* Outsourcing customers and service providers must have coordinated emergency concepts, see also OPS.2.1.M14 Control of emergency preparedness in outsourcing.
#### OPS.2.1.M7 Definition of possible communication partners [Head of Organization, ISB Outsourcing Customer]

As part of an outsourcing project, the outsourcing customer transfers much information to external communication partners. It must be ensured that the respective recipients have the necessary authorizations to process this information. If information is exchanged between several communicating bodies, it should be clear to all those involved who also received or will receive this information.

In order to meet the above criteria, it must be determined which communication partners are allowed to receive which information, both on the part of the outsourcing customer and on the part of the outsourcing service provider, as well as for all other parties involved. This requires that all information is classified according to its strategic importance for the outsourcing institution (OPS.2.1 M1 Definition of security requirements for outsourcing? Projects).

Recipients are to be informed that the data transmitted may only be used for the purpose for which they were passed on. For reasons of data protection (see, for example, BDSG, transfer control), an overview should be drawn up as to which recipients are entitled to receive information, in particular personal data, via data transmission or data medium exchange. This overview must be current and correct.

For this purpose, responsibilities have to be assigned specific roles, which assume these tasks and regularly check compliance with the provisions made by both the Outsoucing customer and the outsourcing service provider.

#### OPS.2.1.M8 Regulations for the use of the staff of the outsourcing service provider [Head of Human Resources, ISB Outsourcing Customer]

In the context of outsourcing projects, the outsourcing service provider's employees may also be deployed in the outsourcing customer's premises. In the long term, this can lead to employees of the outsourcing customer not always knowing exactly whether they are their own or external employees.

Outsourced Service Personnel who operate for an extended period of time within the Outsourcing Client's premises, and who may have access to confidential records and data, must make a written commitment to comply with applicable applicable laws, regulations and internal regulations.

Furthermore, it should be ensured that the employees of the outsourcing service provider - similar to their own employees - are instructed in their tasks. To the extent necessary to fulfill their duties and obligations, they must be informed of in-house rules and regulations on information security and the institution-wide security requirements. This is particularly true when working in the premises of the outsourcing customer.In addition, it should be ensured that adequate representation arrangements also exist for the employees of the outsourcing service provider. The respective representatives must also be properly briefed and committed to compliance with applicable laws, regulations and internal regulations.

In addition, it must be regulated how to handle personnel changes at the outsourcing service provider. These must be communicated to the outsourcing customer in good time.

Upon termination of the outsourcing relationship, a controlled handover of the work results and the documents and resources received must take place. The employees of the outsourcing service provider are also to be deprived of all access rights and access rights.

If employees of the outsourcing service provider are only used at short notice or once on site, they should be treated like visitors and accordingly, for example, should only be allowed to stay in their premises accompanied by employees of the outsourcing customer.

#### OPS.2.1.M9 Agreement on the connection to networks of outsourcing partners [ISB Outsourcing customer]

Before connecting the outsourcing customer's network to the outsourcing service provider's network, a detailed agreement (Data Connection Agreement, DCA) should be made. In this must be precisely defined who gets access to the network of the outsourcing customer and under what conditions this should happen. Analogously, it must be regulated who should receive access to the network of the outsourcing service provider from the network of the outsourcing customer with which access rights and under what conditions. Such an agreement should include the following components:

* A description of what the agreement as a whole includes, including a description of the information networks involved
* A vote on the protection needs and the classification of data (a common understanding must be reached)
* A determination of those responsible (Who is responsible for compliance with the terms of the contract?)
* The naming of contact persons for both organizational and technical problems and in particular for safety-related events
* The information required to classify organizational and technical issues as such as well as security-related events
* Information and specifications for network-internal encryption
* Which services (eg SSH, HTTPS) are provided and which are not
* Which IT platforms, applications and data formats are used
* Whether the network connection results in requirements for the availability of network or IT components at the respective partner (performance, maximum failure rate)
* Who is allowed to log what has to be logged or where the log data are stored and who may access the log data (this may be particularly important in emergency situations)
* To what extent a regular exchange of log data should take place
* What security measures must be taken and how compliance is checked
* A Non-Disclosure Agreement, d. H. an agreement that information obtained by one of the parties involved in the collaboration will not be disclosed to outsiders
* A liability or compensation regulation (this should include the conditions for the separation of the network connection, liability for malicious programs or hacker attacks, penalties for non-performance or liability for use of third-party content to be clarified)
* A regulation on obligations to provide information in the event of security breaches
* A specification of which data may be used for which purposes (eg in the case of further use of work results)* A description of the extent to which other contractors are involved in the agreement, eg B. by sharing applications or as a service provider for one of the contractors
* The duration and possibilities of adaptation of the agreement (technology is developing fast, ie the agreements on their use have to be constantly adapted)
The agreement should be concluded by those persons who are responsible for compliance with the agreements. First of all, it has to be clarified who should take the responsibility for the grid connection, as usually different areas of an institution are involved here. It makes sense to set up a team to which belong at least the information security officer, the IT manager, the specialists in the affected areas and the data protection officer. In the case of critical decisions, all the persons mentioned should be involved, as their interests may vary greatly according to experience.

Before a network connection is activated, all safety deficiencies on both sides should have been eliminated. Here also a way should be found, how the outsourcing customer can convince himself of the security level of the outsourcing service provider or other third parties, for example by basic safety checks or spot checks. In no case should the removal of security vulnerabilities be put into real operation, as experience has shown that this is prioritized lower than mere problems with regard to availability.

The outsourcing service provider should only be provided with the services that have been contractually agreed and absolutely necessary. For foreign outsourcing service providers, their national laws must be taken into account. In the areas of cryptography, privacy and copyright.

If security incidents occur due to the network connection, it must be clearly defined who is allowed to disconnect and when, who is to be informed and which escalation steps are to be provided.

#### OPS.2.1.M10 Agreement on data exchange between the outsourcing partners [ISB Outsourcing customer]

Data exchange between the outsourcing customer and the outsourcing service provider can take place in various ways, in addition to network connection (see OPS.2.1.M9 agreement on the connection to networks of third parties) z. Via data medium exchange or by e-mail. In addition to the security measures that must be taken into account when sporadically exchanging data, agreements should be made with regular communication with fixed communication partners in order to make them as smooth as possible. Such an agreement should include the following components:

* Appointment of contact persons for both organizational and technical problems, and in particular for security-related events
* The required technical information, ie specifications about it

 
+ which applications and data formats are supported
+ what availability is guaranteed, how often, for example, to read e-mails and how fast they can be answered


 
* which security measures must be ensured during the data exchange, thus z. B.

 
+ that data should be checked for malware before and after the exchange
+ how the data should be protected against damage during transport and unauthorized access (sealed containers, checksums, encryption)
+ how the key management is regulated
+ that the data on the transmitter side may be deleted at the earliest after confirmation of the correct reception, if a deletion is required


 
* a confidentiality agreement
* a determination of which data may be used for which purposes (eg in the further use of work results)* an obligation to comply with relevant laws, regulations and regulations, eg. B. Privacy and copyright laws or licensing regulationsOther points that should be included in such an agreement can be found in block OPS.1.2.3 disk replacement and module APP.1 E-mail / Groupware / Communication.
#### OPS.2.1.M11 Planning and maintenance of information security in ongoing outsourcing operations [ISB Outsourcing customer]

After the transfer of the service provision to the outsourcing service provider has taken place, the information security must also be ensured during ongoing operation. In general, the IT-related individual tasks do not differ from those that have to be planned and carried out if no outsourcing is carried out. However, special features arise from the fact that the tasks are spread over several parties and therefore additional coordination and control measures are required. In this context, the following aspects should be considered:

* Documentation and policies must be updated regularly.
* The applicable security concepts of all involved must be checked to see if they are still coordinated and guarantee the desired level of security. In particular, the outsourcing service provider should inform outsourcing customers about important changes in their sphere of influence.
* The client concept of the outsourcing service provider should be checked to see if it meets the customer's security requirements.
* Regular checks should be carried out on the following aspects:

 
+ Implementation of the agreed audits
+ Implementation status of the agreed security measures
+ Maintenance status of systems and applications
+ Rights assignment by the outsourcing service provider (misuse of rights)
+ Use of employees who have not been reported to the outsourcing customer (eg at agencies)
+ Compliance with requirements in terms of performance, availability, quality level
+ Compliance with data protection requirements


 
* Regular rounds of voting on the following points are to be held:

 
+ Exchange of information (eg personnel news, organizational regulations, changes to the law, planned projects, planned tests and system changes that can lead to impairment of the quality of service)
+ Information about security risks and dealing with them
+ Identification and analysis of problems
+ mutual feedback and identification of potential for improvement
+ Change management: Change requests (hardware, software, expansion of the service portfolio, increased resource requirements, etc.) should be discussed at an early stage


 
* Regular exercises and tests should be conducted on the following topics:

 
+ Reaction to system failures (partial failure, total failure)
+ Restoring backups
+ Control of security incidents


 
#### OPS.2.1.M12 Change Management [IT Operations, Change Manager]

With the complexity of today's IT systems, even minor changes to running systems can lead to security issues, such as: Due to unexpected system behavior or system failures.

In terms of information security, change management is responsible for identifying new security requirements that result from changes to IT systems. If significant hardware or software changes are planned on an IT system, the implications for overall system security must be investigated. Changes to an IT system must not lead to a reduction in the efficiency of individual security measures and thus to a threat to overall security.Changes made to the outsourcing service provider during an outsourcing project should also be considered through the outsourcing client's change management. Therefore, it should be contractually agreed with the outsourcing service provider that security aspects are taken into account when planning and executing changes to IT components, software or configuration data. Any changes to IT components, software or configuration data should be planned, tested, approved and documented by the outsourcing service provider. The outsourcing service provider must ensure that all security-relevant changes are appropriately addressed. These include, for example:

* Changes to IT systems (new applications, new hardware, new network connections, modifications to the software used, installation of security patches, hardware upgrade, etc.)
* Changes in the task or the importance of the task for the outsourcing customer
* Changes in the user structure (new, eg external or anonymous user groups)
* spatial changes, eg. B. after a move
Before changes are approved and implemented, testing and testing the planned actions must ensure that the level of security is maintained during and after the change. If risks, in particular for availability, can not be ruled out, the planning must also provide for a fallback solution and specify criteria as to when this should take effect.

All changes and the corresponding decision-making principles must be documented. This applies both in the operating and in a test environment.

In change management, the authorization concept for making changes is an important issue:

* Only those who are allowed to make changes should have access privileges to the relevant system areas.
* There should be mechanisms to ensure that all significant changes have been agreed in advance.
** Note: ** When making changes, always pay attention to changes in an IT system or its operating conditions

* Changes in the implementation of individual security measures,
* the creation of a new security concept or
* require the revision of the institution-wide information security guideline.
* In the case of major changes, it should be agreed that the information security management of the outsourcing customer must be involved in advance by the outsourcing service provider. A fallback solution should be worked out together.
#### OPS.2.1.M13 Secure migration for outsourcing projects

After commissioning the outsourcing service provider, a preliminary security concept for the migration phase must first be developed, which also considers the test and implementation phase as a sub-aspect of the outsourcing project (see OPS.2.1 M6 Development of a security concept for the outsourcing project). On the one hand, a large number of non-employees are involved in this phase, on the other hand processes must be established, tasks transferred and systems newly set up or adapted. Careful testing is therefore extremely important. Especially for test purposes and in phases of heavy workload, "flexible" and "uncomplicated" solutions are often chosen, which are rarely very safe. It is therefore important, for example, to ensure that productive data is not used as test data without special protection. This must be excluded by the security concept.Before creating a migration plan as part of the outsourced security concept, an information security management team should be set up specifically for the migration phase at the outsourcing client. This must pay attention to security issues during the migration phase and ensure by suitable measures even before the migration that a secure IT operation is guaranteed during the migration. The size of the information security management team depends on the type and size of the outsourcing project, as a minimum it can consist of one security expert from each outsourcing partner.

The information security management team is assigned the following tasks from which rules and specifications are derived that must be included in the migration concept:

* It is a mixed team of employees of the outsourcing customer and the outsourcing service provider to form. This can also be reinforced by external experts to make special know-how available.
* An information security concept must be created for the migration phase.
* The responsibilities and hierarchies for the migration phase are to be defined. It is important that clear management structures are created and that clear contacts are defined on both sides. In addition, it must be ensured that responsibilities are defined on both sides, even at high levels. This is the only way to ensure that, if in doubt, action can be taken with appropriate emphasis.
* The required tests have to be planned and carried out, approval procedures have to be prepared and the commissioning of the service has to be planned.
* Select suitable employees on both sides of the outsourcing partners for the test and implementation phase and for later operation. Contractually, an outsourcing customer can of course also have a say in the personnel selection of the outsourcing service provider.
* Employees of the outsourcing customer are to be trained on behavior during and after the migration phase. As a rule, employees are confronted with new and unknown contact persons. This carries the danger of social engineering (eg call of a supposed employee of the security team of the outsourcing service provider).
* The outsourcing service provider must get to know exactly the relevant processes, applications and IT systems of the outsourcing customer and be instructed accordingly.
* Trouble-free operation must be ensured through accurate resource planning and testing. The productive systems must not be neglected. For this purpose, it must be checked in advance whether the planned employees are available. In addition, interference must be calculated by necessary tests.
* Applications and IT systems that the outsourcing service provider should take over should be sufficiently documented. The examination of the documentation for completeness should be considered as well as the adaptation of the existing documentation to the changed conditions by the outsourcing project. The documentation of new systems or subsystems should also be ensured.
* During the migration it should be constantly checked if the SLAs or the security level agreements have to be adapted.
In the introductory phase of the outsourcing project and the first period of operation, special attention must be given to the emergency approach. Until the necessary routine, for example in the handling of malfunctions and security-related incidents, has set in with all those involved, more and more employees are required to undertake on-call services.Once the migration is complete, it must be ensured that the information security concept is updated, as experience shows that there are always changes during the migration phase. This means in particular:

* All security measures must be specified.
* Contacts and responsibilities are documented with names and necessary contact details (telephone, times of availability, possibly required assignment terms such as customer numbers).
* The system configurations must be documented, whereby the set safety-relevant parameters must also be recorded.
* The staff must be prepared for regular operations by means of training.
* As a final task, the outsourcing project must be transferred to safe operation after the migration phase. It is particularly important to ensure that all necessary exceptions during the migration phase, eg. Extended access rights.
#### OPS.2.1.M14 Emergency Preparedness for Outsourcing [Emergency Representative]

The same requirements apply to emergency preparedness for outsourcing as for the non-outsourced operation of business processes or IT systems. However, special features arise from the fact that emergency preparedness must be guaranteed by different parties and thus also for differently distributed systems.

In general, emergency preparedness concepts for the systems must exist at the outsourcing customer and at the outsourcing service provider as well as at the interfaces between outsourcing customers and outsourcing service providers (eg network connection, routers, telecommunication providers). In OPS.2.1.M4 contract design with the outsourcing service provider is described which aspects should already be regulated in the context of contract design. In the emergency preparedness concept, these requirements must be described in detail. In the context of emergency preparedness, particular consideration should be given to the following aspects:

* Responsibilities, contacts and processes should be clearly regulated and fully documented.
* Detailed work instructions should be prepared for specific error situations.
* A concept for conducting regular emergency exercises should be developed.
In an emergency, information security crucially depends on the quality of the work instructions for the staff of the outsourcing service provider. Often outsourcing customers' systems are operated by outsourcing service personnel who have no detailed knowledge of the applications running on the IT systems. Nevertheless, the responsibility for the application lies exclusively with the outsourcing customer. If an application error occurs, the outsourcing service provider may need to troubleshoot without having extensive knowledge of the overall system. The emergency preparedness concept therefore requires the outsourcing service provider to receive accurate instructions. In the course of this, it may also be useful to define actions that are explicitly forbidden (eg reboot of an IT system).Misbehavior of an application may be technical (eg full disk, network problems) or application specific causes (eg processing of a wrong record, program error, wrong parameter setting). In the event of technical errors without any impact on other applications, the outsourcing service provider will be able to correct the error itself, but cooperation with the outsourcing customer is usually necessary to prevent undesirable side effects at the application level. If there are application-specific problems, the outsourcing service provider will need detailed and comprehensive instructions as well as lists of contact persons on the part of the outsourcing customer so that they can react properly. Especially with problems with complicated applications or with extensive patching processes, often knowledge is required that is only available to the customer.

It is also important to provide the outsourcing service provider with information about the protection needs of the data and systems involved so that it can act appropriately.

#### OPS.2.1.M15 Orderly termination of an outsourcing relationship [Head of Procurement]

An outsourcing relationship ends either intentionally and expecting (eg after reaching a defined goal after the end of the project or due to a transfer of the service to another service provider) or unintentionally and unexpectedly (eg due to the insolvency of the outsourcing service provider ).

In order to have sufficient time for the re-integration or transfer of the outsourced processes and activities to another outsourcing service provider in the course of an intended termination, sufficient notice periods must be agreed (see OPS.2.1.M4 Contract Design with the outsourcing service provider). However, compliance with the agreed notice periods can not always be guaranteed. Due to insolvencies, technical faults or natural disasters, the provision of services by the outsourcing service provider may be canceled at short notice. To counteract this risk and to maintain continuity and quality of service delivery in such cases, the outsourcing customer should have adequate contingency plans (see OPS.2.1.M14 Outsourcing Emergency Response Control). This applies in particular to outsourcing projects that affect time-critical processes and activities.

If, following the termination of the outsourcing relationship, a transfer of service provision to another outsourcing service provider takes place, this must be regarded as a new outsourcing project. Accordingly, all the requirements of the module have to be implemented again. In insourcing, ie the re-storage of service provision in one's own institution, this applies analogously. The same requirements apply to strategy, security concept for insourcing, migration and emergency preparedness as with a "classic" outsourcing project.

The following aspects should be considered:

* Property rights to hardware and software (interface programs, tools, batch processes, macros, licenses, backups) must be regulated.
* The re-use of the tools, procedures, scripts and other software used by the service provider must be regulated in the event of termination of the service relationship.
* The IT systems, applications and workflows of the outsourcing service provider must be sufficiently documented.
* All necessary data must be transferred or handed over by the service provider to the customer.
* All data stocks at the service provider must be securely deleted. The deletion of the databases should be confirmed in writing by the outsourcing customer.
* All permissions that have been set up as part of the outsourcing project should be reviewed. The outsourcing customer should delete all permissions that have been set up for the outsourcing service provider or third parties.* Internal or external employees who take on the duties of the service provider must be instructed and trained.
* It is advisable to contractually agree on a transitional period in which the former service provider is still available for queries and assistance.
* Upon termination of the outsourcing relationship, a controlled handover of the work results and the documents and resources received must take place. The employees of the outsourcing service provider are also to be deprived of all access rights and access rights.

 
### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### OPS.2.1.M16 Employee Security Check (CI)

The outsourcing customer should be able to prove the qualification as well as the trustworthiness of the employees of the outsourcing service provider.

The possibilities to check the trustworthiness of personnel are legally very limited in Germany, but also in many other countries. In addition, the results are usually not very meaningful, z. B. in police certificates. In principle, however, should be checked before the takeover of new or external employees in projects, whether

* These have sufficient references, eg. From other, similar projects
* the submitted curriculum vitae of the candidate is meaningful and complete
In addition, it may be useful to have academic and professional qualifications certified, for example by inquiring at the university or from previous employers or clients. The identity of the candidate should also be verified. B. by presentation of identity documents.

If outsourcing service personnel use staff internally at the customer's site or access internal applications and data in projects, collaborations or outsourcing projects, comparable checks should be carried out as for own employees. When drafting contracts with outsourcing service providers, it should be contractually stipulated which side has to carry out such checks and to what extent.

3 Further information
------------------------------

### 3.1 Worth knowing

Note on the footer: The "last checked" can also be omitted as long as the two data "last updated" and "last checked" match.

### 3.2 Literature

Further information on risks and security measures in the area of ​​outsourcing for customers can be found in the following publications, among others:

*

 #### [27001] ISO / IEC 27001

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

  

 
*

 #### [BVIT2005] Buisiness Process Outsourcing Guide

  

 Business Process Outsourcing Guidelines - BPO as Opportunity for the Location Germany, Federal Association for Information Technology Telecommunications and New Media, Version 10.1, 2005
 <Https://www.bitkom.org/Bitkom/Publikationen/Leitfaden-Business-Process-Outsourcing.html>

  

 
*

 #### [BVIT2008] Guide Legal Aspects of Outsourcing in Practice

  

 Legal Aspects of Outsourcing in Practice, Bundesverband Informationswirtschaft Telekommunikation und neue Medien e.V., 2008
 <Https://www.bitkom.org/Bitkom/Publikationen/Rechtliche-Aspekte-von-Outsourcing-in-der-Praxis.html>

  

 
*

 #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

  

 
*

 #### [NIST80053] NIST Special Publication 800-53Security and Privacy Controls for Federal Information Systems and Organizations, Revision 4, NIST, 04.2013
 <Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>