[toc]
 
1 description
--------------

### 1.1 Introduction

The "Implementation Plan for the Guarantee of IT Security in the Federal Administration" (UP Bund) stipulates that federal authorities must fully implement IT-Grundschutz. They are also required to carry out a comprehensive information security audit (IS audit) at least every 3 years. However, authorities are exempted if they have an ISO 27001 IT-Grundschutz-based certificate.

IS revisions are essential to any successful information security management. Only when established security measures and processes are regularly reviewed, are they effective, complete, adequate and up-to-date can the overall state of information security be assessed. IS revisions are thus a tool to identify, achieve, and maintain an appropriate level of security. Through them, it is possible to detect undesirable developments and existing security deficiencies and initiate appropriate countermeasures.

### 1.2 Objective

The module defines requirements for the IS audit for federal authorities with the aim of improving information security in an authority, avoiding undesirable developments in this area and optimizing security measures and processes.

### 1.3 Delimitation

The module describes how IS audits in federal agencies can be planned, carried out and followed up on the basis of the "* Information Security Audit Manual *". However, the module only compiles the obligations within the scope of the IS audit. The binding rules for the IS revision are the "* Guide for the Information Security Revision *" in the current version

Audits and revisions within the Information Security Management System (ISMS) are considered in the module DER.3.1 * Audit and Revision * and are therefore not part of this module. It also does not take into account how the IS audit can be integrated into an existing, higher-level audit organization of an authority (for example internal audit).

The module is aimed especially at federal authorities. In principle, however, the content may also be relevant to other authorities (eg state authorities), companies or other organizations. Unless these are also obliged by law, contract or other regulations to the IS audit, the contents of this module are to be regarded as recommendations. For example, an IS audit in the sense of this module could also be useful for institutions other than federal authorities for preparing ISO 27001 certification based on IT-Grundschutz.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the * IS audit for federal agencies *:

### 2 1 Violation of the requirements of the UP Bund

Among other things, the UP Bund envisages that all federal authorities that do not yet have full ISO 27001 certification based on IT-Grundschutz be subject to a regular IS audit. If federal authorities do not regularly carry out IS revisions, they violate these requirements.

### 2 2 Override security measures

The level of security of an authority depends on full and correct implementation of security measures. In particular, in the critical phase of projects or under certain circumstances, it may happen that security measures are temporarily suspended. However, it is sometimes forgotten to reactivate them, resulting in too low a level of security.

### 2 3 Ineffective or non-economic implementation of security measures
If security measures are implemented without taking into account certain practical aspects, the measures may be ineffective. For example, it is meaningless to lock the entrance area with turnstiles if the staff can easily enter the building through an open side entrance.

Likewise, individual measures can be taken that do not make economic sense. Thus, for the protection of information with a normal confidentiality, a cleanly implemented rights and role concept is more useful and economical than a certificate authority and the subsequent certificate-based encryption of the file server.

### 2 4 Insufficient implementation of the information security management system

In many agencies, the information security officer himself checks whether security measures have been implemented. Often it will forget about checking the actual ISMS. Especially as this should be done by an independent third party. As a result, there is a risk that the processes of an ISMS are inefficient or have not been adequately implemented. As a result, the security level of the institution is impaired.

### 2 5 Inadequate qualification of the examiner

If an IS auditor is not sufficiently qualified or prepares insufficiently for the audits, he may incorrectly assess the security status of an authority during the IS audit. As a result, he does not initiate the necessary or even the wrong corrective measures in his test report. In the worst case, this results in too high and thus not economic or too low and thus very risky securing of information.

### 2 6 Lack of long-term planning

If IS revisions are not planned on a long-term and centralized basis, it can happen that individual areas of one authority are checked very frequently and others not at all. As a result, it is very difficult or even impossible to assess the security status of the information network.

### 2 7 Lack of planning and coordination when performing IS revisions

If an IS audit is poorly scheduled and not voted on by all of the agency's concerned employees, the required or wrong contacts may not be available during the on-site audit. As a result, individual areas may not be tested at all. Even though the IS auditor has set the appointments too narrowly for the individual areas, there is a risk that the planned examination will be carried out only superficially because too little time is available.

### 2 8 Lack of coordination with the Staff Committee

IS revisions can also be used to check aspects that can be used to draw conclusions about the performance of employees. Thus, these exams could be considered performance appraisals. Failure to involve staff representatives may result in violations of the applicable codetermination law.

### 2 9 Intentional concealment of deviations or problems

Employees may fear that an IS Revison will detect bugs and try to conceal security issues and misrepresent the true status quo.

### 2 10 Confidentiality loss of sensitive information

During an IS audit, various confidential information is collected by the auditors. Deficits in the information security of the audited authority are also named. However, if these deficiencies become known to unauthorized third parties, they could be used to attack the authority.

3 requirements
---------------
The following are specific requirements for the area of ​​IS revision for federal authorities. In principle, the person responsible for the IS audit is responsible for fulfilling the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### DER.3.2.A1 Definition of responsibilities for the IS audit

The institution MUST appoint a responsible person to plan, initiate, and track the results of IS revisions.

#### DER.3.2.A2 Creation of an IS-Revision-Manual

An IS Revision Manual MUST be created. The manual MUST be adopted by the management.

#### DER.3.2.A3 Definition of the basis for the audit and a common rating scheme [IS audit team]

The audit basis for the IS audit MUST be the UP Bund, the Information Security Review Guide, the BSI Information Security Standards, and the IT Baseline Protection Compendium. This MUST also be known to all involved. For the assessment of the implementation of the measures, the evaluation scheme from * Information Security Revision - A Guide for the IS Revision Based on IT-Grundschutz * MUST be used (see 4. * Further Information *).

#### DER.3.2.A4 Preparation of a plan for the IS audit

Federal agencies that do not yet have ISO 27001 certification based on IT-Grundschutz MUST perform a comprehensive IS audit at least every 3 years. In addition, further revisions for critical business processes SHOULD be scheduled. The person responsible for the IS audit should therefore prepare a multi-year rough planning (meaningfully for at least 3 years) for the audit project based on the information security audit guideline. This SHOULD then be specified by an annual detailed plan.

#### DER.3.2.A5 Selection of a suitable IS audit team

For IS revisions, a suitable team MUST be compiled or commissioned. The IS audit team MUST be granted an unrestricted right to information and access to its activities.

#### DER.3.2.A6 Preparation of an IS revision [IS revision team]

The authority management MUST initiate the IS review process by placing an order with the IS audit team.

For document review, the authority to be audited MUST provide the necessary reference documents to the IS audit team in accordance with the information security audit guide.

#### DER.3.2.A7 Carrying out an IS audit [IS audit team]

In the case of an IS short revision, the mandatory inspection list from * Mandatory inspection topics for the IS short revision * (see 4. * Further Information *) MUST be used. All created basics must be updated during the IS revision and adapted if necessary.

As part of an IS audit, both a document review and an on-site inspection MUST be performed. All results of the two phases MUST be documented in writing and summarized in an IS audit report.

#### DER.3.2.A8 Retention of IS audit reports
The IS audit report and its underlying reference documents MUST be audited by the audited authority for at least 10 years from the date of notification of the report, unless otherwise required by law or regulation. It MUST be ensured that only authorized persons can access the IS audit reports and the reference documents.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​IS auditing for federal authorities. They SHOULD be implemented in principle.

#### DER.3.2.A9 Integration into the Information Security Process [Information Security Officer (ISB)]

It should be ensured that IS revisions are part of and initiated by the security process. In addition, the results of IS revisions SHOULD flow back into the ISMS and contribute to its improvement.

Furthermore, the IS revisions, the results as well as the activities for the elimination of deficiencies and quality improvement SHOULD be included in the regular report of the ISB to the authorities.

#### DER.3.2.A10 communication agreement

Clear regulations should be made on how to exchange information between the IS audit team and the federal agency to be audited. In this way, suitable measures should be taken to ensure that the information exchanged during an IS audit remains confidential and integrity.

#### DER.3.2.A11 Conducting a kick-off meeting for a cross-sectional revision [IS-Revision-Team]

For a cross-sectional revision, a start-up interview SHOULD be made between the IS audit team and the contact persons. The following contents SHOULD be discussed:

* Explanation and presentation of the IS revision procedure,
* Presentation of the institution: Explanation of the main tasks and overview of the IT used,
* Transfer of reference documents to the IS audit team.
#### DER.3.2.A12 Creation of a test plan [IS-Revision-Team]

Before an IS audit, the IS audit team SHOULD create an IS audit plan that coordinates and describes the entire time and organizational process of the audit, as well as all related activities and policies. If it is necessary during the IS audit to extend or otherwise adjust the planned procedures, the IS test plan should be adapted accordingly. The test plan SHOULD also be part of the final IS audit report.

During the IS short revision, the bindingly defined inspection list from * Binding inspection topics for the IS short revision * (see 4. * Further information *) SHOULD replace the inspection plan.

#### DER.3.2.A13 Inspection and Checking of Documents [IS Revision Team]

The document review SHOULD be done on the basis of the measures defined in the test plan. The IS audit team SHOULD verify that all relevant documents are current and complete. When checking the actuality, the granularity of the documents SHOULD be taken into account. When checking for completeness, care should be taken to ensure that all material aspects have been recorded and that the appropriate roles have been assigned.

Furthermore, it should be checked whether the documents available and the decisions made therein are comprehensible. The results of the document review SHOULD be documented and, where appropriate, incorporated into the on-site inspection.

#### DER.3.2.A14 Selection of target objects and measures [IS-Revision-Team]
In an IS cross-sectional revision or IS partial revision, the IS audit team SHOULD use the results of the document review to select the POU target objects for on-site inspection. The module for information security management (see ISMS.1 * Security Management *) including all related requirements SHOULD always be fully tested. Further building block target objects SHOULD be selected in a risk-oriented manner according to the procedure defined in the * Information Security Revision Guide *. The selection SHOULD be documented comprehensibly in writing.

In addition, the selection SHOULD consider the criticized requirements from previous IS revisions. All actions with serious security deficiencies from previous IS revisions SHOULD be considered.

#### DER.3.2.A15 Selection of suitable test methods [IS revision team]

It SHOULD be ensured that appropriate methods are used to identify the relevant issues. In addition, all tests should be proportionate.

#### DER.3.2.A16 On-Site Review Schedule [IS Revision Team]

Together with the point of contact of the authority to be audited, the IS audit team SHOULD develop a schedule for the on-site inspection. The results SHOULD be documented in the IS test plan.

#### DER.3.2.A17 On-site inspection [IS-Revision-Team]

The on-the-spot check SHOULD ensure that the selected measures ensure information security in an appropriate and practicable way. The exam SHOULD start with an opening interview.

Thereafter, all measures of the test plan or all topics of the test topic list SHOULD be tested. If so, the intended test methods SHOULD be used. If the IS audit team identifies deviations from the documented status for a selected sample, the sample SHOULD be extended as needed until the issue is resolved.

During on-the-spot audits, IS auditors should never actively intervene in systems themselves or give instructions for changes to the subject of the review.

All essential facts and information about source, information and submission requests as well as conducted meetings SHOULD be recorded in writing.

The IS audit team SHOULD briefly present the findings to the contact persons of the audited authority in a final discussion. There should be no concrete assessment, but an indication of any shortcomings and the further procedure. This final discussion must also be recorded.

#### DER.3.2.A18 Conducting Interviews [IS Revision Team]

Interviews SHOULD be structured. Questions SHOULD be concise, precise and easy to understand. In addition, suitable questioning techniques SHOULD be used.

#### DER.3.2.A19 Review of the risk treatment plan [IS audit team]

The IS audit team SHOULD verify that the remaining residual risks to the information network are adequate and sustainable and are bindingly borne by the authorities. Measures that fundamentally contribute to the information security of the entire federal authority must NOT be included in the risk assumption.

The IS audit team was asked to randomly verify whether or to what extent the measures specified in the risk treatment plan have been implemented.

#### DER.3.2.A20 Follow-up of the on-site inspection [IS-Revision-Team]

After the on-site inspection, the information collected SHOULD be further consolidated and evaluated. After the eventually requested documentation and additional information have been evaluated, the audited measures SHOULD be definitively evaluated.
To provide the requested documentation, a sufficient time window SHOULD be granted. Documents that have not been received by the agreed end date SHOULD be considered non-existent.

#### DER.3.2.A21 Creation of an IS audit report [IS audit team]

The IS audit team SHOULD transfer the results obtained to an IS audit report and document it comprehensibly.

A draft version of the report SHOULD be submitted to the audited federal authority in advance to verify that the issues identified by the audit team were properly recorded. It SHOULD be considered that the IS audit team explains the results of the IS audit in a presentation to those responsible.

The audited federal authority SHOULD make sure that all relevant bodies in the federal authority receive within a reasonable time the passages of the IS auditing report that are important and necessary for them. In particular, the content SHOULD be communicated to the authorities, to those responsible for the IS audit and to the ISB.

IS audit reports SHOULD at least be classified as classified for "for business use only" (VS-NfD).

#### DER.3.2.A22 Follow-up and initiation of follow-up [Information Security Officer (ISB)]

The deviations noted in the IS audit report SHOULD be remedied within a reasonable time. The corrective actions to be performed SHOULD be documented with responsibilities, date of implementation and the respective status. The implementation SHOULD be tracked continuously and the implementation status should be updated.

In principle, it should be checked whether additional IS revisions are necessary. The person responsible for the IS audit SHOULD adapt the rough and detailed planning to the IS audit.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### DER.3.2.A23 Security Review of IS Auditors (CI)

Insofar as the IS auditors access sensitive information, they should be required to provide evidence of their integrity and reputation, such as a police certificate of good conduct or references.

If classified information classified according to secrecy is concerned, the IS auditors SHOULD undergo a security check according to the Security Review Act (SÜG). In this regard, the ISB SHOULD include the intelligence officer or security officer of its authority.
