[toc]
 
1 description
--------------

### 1.1 Introduction

In emergency situations, access to information to restore a business process, an IT system or a specialist task is indispensable. To this end, the relevant processes for maintaining information security in an emergency should be planned, established and reviewed.

Only when planned and organized is an optimal emergency preparedness and emergency management possible. A professional emergency management process reduces their impact and thus ensures the operation and continued existence of the institution. Appropriate measures must be identified and implemented that make business processes and specialist tasks more robust and fail-safe, and that make it possible to handle the emergency quickly and purposefully.

The maintenance of information security must therefore be integrated into a comprehensive emergency management. However, emergency management has its own process manager (the emergency officer) with whom the information security officer coordinates.

### 1.2 Objective

The aim of the module emergency management is to describe requirements that ensure information security even in critical situations. To this end, the corresponding measures are to be embedded in a holistic continuity management and to consider all aspects that are necessary in order to be able to maintain information security even in the event of a damaging event. This ranges from planning to checking all processes.

### 1.3 Delimitation

When a damage event occurs, the right information must be complete and accurate. In the present module, neither criteria nor processes are explained, by means of which the responsible persons can decide, whether an emergency exists or not. The decision is made while the incident is being handled (see DER.2.1 * Handling Security Incidents *).

Crises are considered in the context of a separate crisis management and in this module only as an interface, eg. As part of the further escalation of emergencies. Further information on the individual phases of emergency management and the definition of emergency management for crisis management are contained in BSI Standard 100-4.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in *** *** emergency management:

### 2 1 Staff shortage

If employees fail, z. Eg by germs in the canteen, pandemic, death or strike, the own institution could no longer perform their specialized tasks and business processes and, moreover, relevant information for restarting the business process or the IT systems could no longer be accessible. In many cases, individuals have specific expertise (head monopolies), so that damage can occur even if the number of staff shortages is numerically very low.

### 2 2 Failure of IT systems

If components of an IT system fail, eg. B. by defective hardware or power failure, the entire IT operation can be disturbed. As a result, the availability of the respective information and thus of the respective business process is at risk. In addition, important information needed for recovery operations may not be available.

### 2 3 Failure of a Wide Area Network (WAN)
The causes of the failure of a wide area network (WAN) can be manifold. Therefore, it is possible that a network outage will affect only individual users, a vendor or a specific region. Frequently, such failures only last a short time and only affect the business processes and specialized tasks that require a correspondingly high availability of the WAN. But there are also always longer failures, which can cause massive problems in communication and accessibility.

### 2 4 Failure of a building

Buildings can become unusable unpredictably, eg. B. because they were partially or completely destroyed by fire, storm, flood, earthquake or explosion. However, a failure of a building can also be caused by the fact that due to blockades by police or fire brigade, the environment can no longer be entered or the building must be abandoned, because electricity, water, sewage, heating or air conditioning over a period of time no longer work.

### 2 5 Failure of a supplier or service provider

When organizational units depend on service providers, the partial or total failure of an outsourcing service provider or supplier can have a significant impact on business continuity, especially in critical business processes.

3 requirements
---------------

Specific requirements for emergency management are listed below. In principle, the emergency officer is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of emergency management. They SHOULD be implemented in principle.

#### DER.4.A1 Creation of an emergency manual [Information Security Officer (ISB)]

It SHOULD be created an emergency manual in which the most important information about

* Roll,
* Emergency measures,
* Alerting and escalation,
* Communication, general business continuity, recovery and
* Recovery plans
are included. Responsibilities and authority SHOULD be assigned, communicated and recorded in the emergency manual. It SHOULD be ensured that appropriately trained personnel are available in an emergency. It SHOULD regularly be checked by tests and exercises as to whether the measures described in the emergency manual also work as intended.

The emergency manual SHOULD be checked regularly and updated if necessary. It SHOULD also be accessible in an emergency. The emergency manual SHOULD be supplemented with rules of conduct for cases (eg fire) that should be communicated to all employees.

#### DER.4.A2 Integration of emergency management into organizational processes and processes [institutional management]

The processes in the security management SHOULD be coordinated with the emergency management (see DER.2.1 * Handling of security incidents *).

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that go beyond the level of protection afforded by the state of the art and should BE considered AT INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).
#### DER.4.A3 Definition of Scope and Emergency Management Strategy [Institutional Management] (CIA)

The scope of the emergency management system SHOULD be clearly defined. The institution's management SHOULD set out an emergency management strategy that sets out the goals and the level of risk acceptance.

#### DER.4.A4 Guideline for emergency management and assumption of overall responsibility by senior management [Institutional Management] (CIA)

A guideline for emergency management SHOULD be adopted by the management level. This SHOULD contain the essential cornerstones of emergency management. The guideline for emergency management SHOULD be regularly reviewed and, if necessary, revised. The guideline for emergency management SHOULD be announced to all employees.

#### DER.4.A5 Development of a suitable organizational structure for emergency management [Institutional Management] (CIA)

The roles for emergency management should be set appropriately to the circumstances of the institution. This SHOULD be documented in writing with the roles, duties and responsibilities of the roles. It SHOULD be named Qualified Personnel for all roles in Emergency Management. The organizational structure in emergency management SHOULD regularly be checked to determine whether it is practicable, effective and efficient.

#### DER.4.A6 Provision of adequate resources for emergency management [Institutional Management] (CIA)

The financial, technical and human resources for the intended goals of emergency management SHOULD be appropriate. The emergency officer or emergency management team SHOULD have enough time for emergency management tasks.

#### DER.4.A7 Creation of an emergency concept [institutional management] (CIA)

All critical business processes and resources SHOULD be identified (for example, with a Business Impact Analysis (BIA)). It SHOULD identify the most relevant, relevant risks to critical business processes and resources. For each identified risk SHOULD decide which risk strategies should be used for risk treatment. Continuity strategies should be developed that enable a recovery and recovery of critical business processes in the required time. An emergency concept SHOULD be created. Emergency plans and measures SHOULD be developed and implemented to enable effective emergency response and rapid resumption of critical business processes. In the emergency concept, information security SHOULD be considered and appropriate security concepts for emergency solutions developed.

#### DER.4.A8 Integration of Employees in the Emergency Management Process [Supervisors, Head of Human Resources] (CIA)

All employees SHOULD be sensitized regularly to the topic of emergency management. For emergency management, there should be a training and awareness-raising concept. The employees in the emergency management team SHOULD regularly be trained according to the required competences.

#### DER.4.A9 Integration of emergency management into organizational processes and processes [institutional management] (CIA)

It SHOULD be ensured that aspects of emergency management are taken into account in all business processes of the institution. The processes, specifications and responsibilities in emergency management SHOULD be coordinated with risk management and crisis management.

#### DER.4.A10 Tests and Emergency Exercises [Head of Institution] (CIA)

An exercise plan SHOULD be created so that all major emergency management plans and measures are tested and practiced regularly and on an ad hoc basis. In emergency management, sufficient resources should be provided for the planning, design, implementation and evaluation of the tests and exercises.
#### DER.4.A11 Review and maintenance of emergency preparedness and response (CIA) measures

The identified measures for emergency preparedness and response SHOULD be reviewed regularly and on an ad hoc basis. The checks SHOULD be planned so that no relevant part is left out. The results of the reviews SHOULD be evaluated and, where appropriate, implemented in corrective actions. The corrective measures SHOULD be planned and the implementation monitored.

#### DER.4.A12 Documentation in the Emergency Management Process (CIA)

The course of the emergency management process, the work results of the individual phases and important decisions SHOULD be documented. A procedure should be established to ensure that regular documents are updated. In addition, access to the documentation SHOULD only be restricted to authorized persons.

#### DER.4.A13 Review and Management of the Emergency Management System [Institutional Management] (CIA)

The management level SHOULD carry out its task of regularly reviewing, evaluating and, if necessary, correcting the emergency management system. The management level SHOULD regularly be informed about the state of emergency management through management reports.

#### DER.4.A14 Regular review and improvement of emergency response [Institutional Management] (IA)

All emergency measures should be reviewed regularly or in the case of major changes to ensure that they are still respected and correctly implemented and that they are still capable of achieving the defined goals.

It should be investigated whether technical measures were correctly implemented and configured and whether organizational measures are implemented effectively and efficiently. In case of deviations, the causes of defects SHOULD be determined and improvement measures initiated. This summary of results SHOULD be released by the management level. In addition, a process should be initiated that controls and monitors whether and how the improvement measures are implemented. In case of default, this SHOULD be escalated to the management level at an early stage.

It should be determined in the institution's management how the review activities are coordinated. In particular, reviews carried out in the area of ​​auditing, IT, security management, information security management and emergency management SHOULD be coordinated. For this purpose, it should be regulated which measures are to be checked when and by whom.

#### DER.4.A15 Assessment of the Efficiency of the Emergency Management System [Institutional Management] (IA)

It SHOULD regularly be assessed how powerful and effective the emergency management system is. As a basis SHOULD measure and evaluation criteria, such. B. Key performance indicators (Key Performance Indicators) are defined. These measured values ​​SHOULD be determined regularly and compared with the previous year's values. If the values ​​deviate negatively, the causes SHOULD be determined and improvement measures defined. The results of the evaluation SHOULD be reported to the management.

The management SOLLTE decide with which measures the emergency management should be further developed. All decisions of the management level SHOULD be documented and the previous records updated.

#### DER.4.A16 Emergency preparedness and emergency response planning for outsourced components [Institutional Management] (IA)

In emergency preparedness and response planning for outsourced components, the contractor's emergency management SHOULD check the supplier's or service provider's emergency management. This examination SHOULD be performed regularly by a person in charge of the institution's management. Also, the procedures in emergency tests and exercises SHOULD be coordinated with the supplier or outsourcing service provider and possibly carried out together.
The results and evaluations SHOULD be exchanged regularly between the institution's management and the supplier or service provider. This should include any improvement measures.
