[toc]
 
1 description
--------------

### 1.1 Introduction

The implementation notes described in this document provide information and assistance on how to properly implement the requirements of the module * OPS.1.1.2 Proper IT administration *. They represent proposals that meet the typical conditions in an information network. They do not exclude that the requirements of the building block can also be achieved in other ways that may be more appropriate for an individual information network.

### 1.2 Life cycle

The module * OPS.1.1.2 * * Proper IT administration * describes IT processes. Therefore, he is mainly concerned with the lifecycle phase * implementation *, only individual aspects reach into other lifecycle phases.

** planning and conception **

In order to establish a proper IT administration process, several preliminary considerations are required. Tasks and authority in the IT-operation must be clear for the involved ones, important basic rules should be fixed in a guideline (see for this * OPS.1.1.2.M7 regulation of the IT-administration activity *). Because of the comprehensive permissions, administrative activities are particularly sensitive. This is due to corresponding requirements for the recruitment of personnel (see * OPS.1.1.2.M3 Regulated recruitment of IT administrators *) and for the release (see * OPS.1.1.2.M4 Termination of the activity as IT Administrator *).

If high availability requirements exist for the IT environment, it must be ensured that the components, architectures and processes used meet these requirements (see * OPS.1.1.2.M19 Consideration of High Availability Requirements *).

**Procurement**

Procurement processes are not affected by this module.

**Implementation**

When implementing a proper administration process, different security requirements must be taken into account. First of all, suitable persons must be selected to perform the defined administration roles (see * OPS.1.1.2.M1 Personnel Selection for Administrative Activities *). Appropriate administration accounts must be set up for these persons (see * OPS.1.1.2.M5 Administration Accessions *), whereby the administrative access to IT systems and components should be appropriately protected (see * OPS.1.1.2.M6 Protection of Administrative Access) Additions *). In the case of increased protection requirements, this should also include network-side shielding of administrative accesses and interfaces (see * OPS.1.1.2.M16 Access Restrictions for Administrative Accesses *).

Administrative access is not only at the system level, but often also within specialized applications. Such administrative tasks must also be suitably mapped during operation (see * OPS.1.1.2.M8 Administration of Specialist Applications *). If the size of the organization allows it, or if increased integrity requirements require it, different administrative tasks should be separated from one another (see * OPS.1.1.2.M15 Distribution of IT Administration Activities *). The human resources available for IT operations must be sufficient to maintain proper system operation even in the event of incidents or downtime (see * OPS.1.1.2.M9 Resource Planning *).

In the case of increased protection requirements, it may also be necessary to log administrative activities consistently (see * OPS.1.1.2.M18 Continuous Logging of Administrative Activities *) and / or to carry out a continuous four-eyes principle (see * OPS.1.1. 2.M17 IT administration in the four-eyes principle *).

 **Business**
In particular, it must be ensured during ongoing operations that administrative activities are suitably documented (see * OPS.1.1.2.M11 Documentation of IT Administration Activities *). In order for the deployed personnel to keep pace with developments that affect the security of their information network, appropriate measures for continuous qualification and information are required (see * OPS.1.1.2.M10 Training and Information *).

** ** segregation

This module contains no requirements for the sorting out.

** Emergency Preparedness **

In order to ensure the implementation of a proper IT administration even in emergency situations, suitable precautions must be taken (see * OPS.1.1.2.M2 Representation Regulations and Emergency Preparedness *).

2 measures
-----------

The following are specific implementation notes in the section "Proper IT Administration".

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### OPS.1.1.2.M1 Personnel Selection for Administrative Activities [Head of Personnel]

IT administrators must have the necessary professional qualifications to properly handle the tasks assigned to them. For administrators, this usually means an IT-related vocational training, a corresponding degree or many years of professional experience in the IT sector. In addition, internal training or further training can ensure the qualification of the corresponding employees. For example, if necessary, additional knowledge can be imparted that is needed for the respective task.

Employees who have an administrative role can not simultaneously assume a controlling role (for example, auditing). In addition, the role of administration is not compatible with all other roles in an institution, as conflicts of interest can occur here.

In order to take on administrative tasks, it must be ensured that every administrator and also the representatives are provided with the necessary time to perform their tasks carefully. It must also be taken into account that education and training are required.

In order to determine which specialized skills are required in the IT administration and how they can be covered, it is advisable to first of all outline the platforms, products and techniques used. It is important to distinguish which skills must be mastered by each individual IT administrator and which must be covered by the IT administration team as a whole. A matrix can then be used to identify the persons with the relevant knowledge and how they were acquired (study, training, professional practice or training). If no candidate with all the required qualifications can be found, it can be checked whether existing gaps can be closed in the context of qualification measures.

Language skills must also be taken into account when acquiring the necessary qualifications: to avoid misunderstandings, IT administrators need to know the language spoken by the users of their systems so that they can understand and work on their requirements or problem descriptions. In multinational institutions, an agreed group language, usually English, can also be used as a substitute.

Good English literacy, including technical terminology, is important to IT administrators because information from system documentation, guides, or forums is often available in English only.
If administrative tasks are outsourced to third parties (eg external service providers or freelancers), the necessary qualifications must also be taken into account when selecting the contractors and awarding the contract. For this purpose, appropriate agreements should be made as to which minimum qualifications the employed personnel must fulfill and which ongoing qualification measures are to be carried out.

IT administrators must have the right personality to do their jobs reliably and carefully. When filling positions with internal staff, the previous leadership of the persons concerned provides good information. For this purpose, appropriate information should be obtained from the previous superiors. In the case of external candidates, the examination of work certificates and other application documents provide important insights into the professional career and can give indications of the general suitability for the respective job and the reliability in general. Within the agreed probationary period, it must be checked whether the persons are actually suitable for the tasks entrusted to them.

For all employees in the IT administration, an examination of the personal background should be carried out within the framework of what is permitted by law. B. by obtaining a personal certificate of good conduct.

Also in the transfer of administrative tasks to third parties, the reliability of the staff employed to ensure. For this purpose, it must be agreed whether the examination is carried out by the contractor and is suitably demonstrated, or whether the contracting authority has appropriate powers for review. Furthermore, it is necessary to determine how to proceed if the client rejects the use of certain persons, if indications of personal or professional deficits make this necessary.

#### OPS.1.1.2.M2 Representation arrangements and emergency preparedness

For all administrative tasks and responsibilities, sufficient substitution arrangements must be made to ensure that the tasks can be performed properly, even if the responsible employee fails. In the event of the failure of an IT administrator, rules should exist to ensure the proper performance of administrative tasks. For all applications and systems, in addition to the main person responsible, additional persons should be named who are technically suitable for maintenance and administration and familiar with or trained in the respective systems. The names and contact details of these employees should be recorded in writing. A suitable procedure must ensure that representatives are aware of the failure of an IT administrator and take on pending tasks.

In emergency situations, implementing immediate actions may require short-term access to systems and applications without having an authorized IT administrator available. In this case, administrative emergency access should be established. The access data for these administration identifiers should be stored in such a way that only the authorized group of persons can access it. In addition, they should be able to be provided quickly if needed.

If possible, passwords should only be deposited if there is no other (technical) solution. It should always be noted that the deposit of passwords gives a false signal character for the safe handling of passwords. However, passwords should always be stored securely if they are the only way to access IT systems. This is often the case with administrator accounts.
One possibility is the storage of authentication means in a protective cabinet accessible only to the management level or to an emergency team. The output of the access data should be documented. By depositing the access data or means of access in sealed envelopes can be achieved that their use is recognizable and then z. B. a change of passwords and deposit is done in a new envelope. It should be checked regularly that current passwords and authentication means are stored.

#### OPS.1.1.2.M3 Regulated recruitment of IT administrators [Head of Human Resources]

When people in the institution take on administrative tasks, their tasks and responsibilities must be defined in writing, eg. B. in the form of a job description with tasks and competences.

If suitable internal or external staff members meet the relevant requirements (see * OPS.1.1.2.M1 Personnel Selection for Administrative Activities *), they must be introduced to their job in accordance with a regular procedure. At least the following aspects should be considered:

* The proof of fulfillment of professional and personal requirements must be systematically filed (eg in a personal file).
* Any existing skills gaps must be closed by suitable training before starting the related tasks.
* Obligations and instructions are to be carried out (usually at least one obligation on the data secrecy according to § 5 BDSG).
* Security guidelines and security regulations of the institutions as well as the structural and procedural organization in the ISMS must be communicated.
* Reporting channels and contact persons for security incidents must be made known.
* The structure and the procedures used for the documentation should be explained.
* Person-related administration accounts must be set up to the required extent. The means of access (passwords, smartcards, tokens ...) must be initialized and securely transferred.
* IT administrators must be briefed on the systems and networks they are responsible for.
In order to ensure full implementation of this and any other issues relevant to the institution, it is advisable to design checklists or leaflets to be processed by the new IT administrators while documenting the proper execution of all tasks.

#### OPS.1.1.2.M4 Termination as IT Administrator [Head of Human Resources]

If internal or external employees are relieved of an activity in the IT administration, it must also be ensured that all documents, work materials and authority are withdrawn. This includes z. B .:

* Disabling / blocking administration and user accounts
* Change passwords of non-personal administrative accounts whose passwords are known to the departing employee.
* Change passwords for Wi-Fi access
* Block VPN or remote access
* Blocking of user and device certificates whose associated keys are or were under the control of the employee
* Blocking access to external services (eg cloud applications)
* Submission of access cards or authentication means (smart cards, tokens)
* Return of mobile IT devices
* Examination and adaptation of alerting plans and representation arrangements
* Information of affected bodies about the departure of the employee (employee, security guard, gate, service provider, supplier, domain administrator).
The points listed here are examples that have to be examined for each institution and supplemented with additional points as required.
For the release of IT administrators, it is also advisable to use appropriate checklists or runnotes to ensure and document the complete execution of the required steps.

#### OPS.1.1.2.M5 Administration IDs

For administrative access to IT systems and applications, personal administration identifiers must be set up and used as far as technically possible. The use of a central administration ID by several persons means that operations can not be assigned to the executing person. Therefore, an additional administrative identifier must be provided for each administrative person.

If the use of general, non-personal administrative identifiers is unavoidable in individual cases, it should be ensured that the use of the identifier is comprehensibly documented. This can be z. B. on Unix systems can be achieved by first logging in with a personal identifier and from there with the command "su" to the overarching identifier (eg "root") is changed. A proof would also be possible through the use of so-called jump servers, on which administrative accesses are used out of a person-related session. If technical implementation is not possible at all due to special circumstances, the IT administrators should keep a record of the use of general administration IDs.

The rights of the administration access must always be adapted to the respective requirements. For example, an employee who only administers the database does not need any system administrator rights or access to configure the mail server. Any rights derived therefrom, such as the ability to start and stop the database service at the operating system level, must also be granted if necessary.

For routine activities, a personal, unprivileged identifier must be used. This includes all non-administrative activities, such as research activities or e-mail communication. This ensures that, on the one hand, there are no unintentional administrative changes to the information network, but on the other hand, attacks via external communication interfaces (e-mail, WWW) can not directly affect access with administrative authorizations.

For example, accidentally running an encryption trojan under an administrative handle as an e-mail attachment could allow the malware to quickly encrypt all documents in the file racks on the network. If the same scenario is used using a restricted user ID, the damage is limited to the files that are accessible under this ID in write access.

#### OPS.1.1.2.M6 Protection of administrative identifiers

Access to administration IDs must be adequately protected by appropriate authentication mechanisms. For administration identifications, a two-factor authentication should be used, in which, in addition to the password, a further factor is usually added, eg. B.

* Hardware tokens with dynamically generated codes,
* mobile devices to which dynamically generated logon codes are sent
* cryptographic certificates that are bound to a specific device or hardware (smart card / token),
* biometric authentication procedures provided they provide sufficient reliability and security.
With increased protection requirements, a two-factor authentication must be used.

This prevents a potential attacker from gaining access to protected systems simply by spying on passwords, since another factor, such As the possession of hardware or corresponding biometric properties, is required for a login.
A somewhat weaker protection is offered by cryptographic certificates that are stored in software and protected by a password. The use of such certificates may, for. For example, when using SSH. The storage of the certificates should take place in such a way that an unauthorized access is excluded. Compared to hardware-bound certificates, there is a fundamental risk that the certificate is copied by an attacker and the password is spied or guessed, but this method offers a clear gain in security over passwords alone.

When using usernames and passwords, a password policy with correspondingly high password complexity requirements must apply. Because long and complex passwords are difficult to remember, password management programs that store passwords in an encrypted database can be used. This database must itself be protected with a strong password.

Passwords for infrequently-used, privileged accesses (such as stored emergency users or technical users of services or databases) that require IT administrators to log in only in exceptional circumstances should be dialed much longer than the minimum password for user passwords in require the institution to increase the robustness against attacks.

For administrative access, secure protocols must be used to encrypt communication unless the local console is used. For example, SSH should be used for Unix derivatives and Windows RDP for Windows. Access to web interfaces must be secured using TLS.

Every logon procedure via administration ID must be logged. The logging must ideally take place in such a way that the logged in user has no possibility to change the protocol. This can be realized, for example, in which the logging via a protocol such. For example, syslog is done on a separate logging system. It must be ensured that the affected system and the logging system have a uniformly synchronized system time to facilitate the reconstruction of operations based on the log data.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "Proper IT administration".

#### OPS.1.1.2.M7 IT administration regulation [Head of Human Resources]

Employees with IT administration tasks require extensive access to systems, applications, and databases for their work. Administrative accesses are often just not the authorization control because z. For example, troubleshooting requires extensive accessibility, or because the systems and applications do not provide administrator privilege restrictions. But not everything that employees can do with their privileges, they are allowed to do - otherwise a proper and traceable IT operation would no longer exist. Access to personal data or telecommunications content is subject to legal restrictions, which must also be implemented in the IT administration.

The institution should therefore make arrangements for the IT administration and commit these bindingly in a work instruction or guideline. The following contents should be considered:
* The organization of IT operations should be described. This includes in particular the division of tasks in the IT administration, including the corresponding representation regulations. For each IT component or application, it must be clear who has the administrative responsibility. In larger institutions it may be useful to delineate the responsibility for planning, procurement and introduction, operation and further development as well as separation.
* The role of administration is not compatible with all other roles in an institution. For example, when using logging, you must pay attention to the role separation of administration and revision. In areas with increased security requirements, additional role exclusions may be required (see OPS.1.1.2.M14).
* For larger institutions with a variety of different IT systems and subnets, it must also be ensured that the tasks are distributed among the various administrators in such a way that no responsibility problems arise, that is to say neither overlaps nor gaps in the distribution of tasks. In addition, the communication between the various administrators should run as smoothly as possible. For this purpose, for. For example, regular administrators meetings will be held to discuss typical problems and solutions in their daily work.
* Rules for dealing with administrative access should be defined (see OPS.1.1.2.M4).
* Authorities and duties of administrators should be described. This includes, in particular, a ban on access to sensitive data (eg e-mail inboxes, log data) if there is no operational necessity for access.
* Application and approval procedures should be established for changes to the information network. IT administrators must not make changes that do not have an order and clearance, or are required for immediate security.
* Documentation requirements of IT administrators should be described. This includes the form of the documentation, its location and obligations for an appropriate update check.
* The duties and powers of the IT administrators in the context of the investigation and defense against security incidents should be regulated.
The policy or work instruction should be put into effect by an authorized senior management and made known to all IT administrators. It must be accessible in the current version at a defined storage location for all affected employees. Appropriate intervals should be used to check and adapt and confirm the regulations.

#### OPS.1.1.2.M8 Administration of Specialist Applications [IT Operations]

Often employees in departments of an institution also perform administrative tasks for individuals in specialist applications. These can overlap with the administrative tasks of the IT operations administrators. In order to avoid mutual interference and ambiguity about the areas of responsibility, the specific tasks of the application administrators and system administrators should be documented in writing. In addition, fixed contact persons and communication interfaces should be defined in order to facilitate the technical exchange.

If administrative intervention in the operation of the application is necessary, the specialist administrators of the respective department should be informed beforehand of the upcoming maintenance and the associated impairment or changes. This can be the case, for example, with version changes or maintenance windows. In addition, a consultation with the department should be sought in order to lay the date of the maintenance window as low as possible and to consider user requirements.
The requirements of this module are also to be implemented for the application administrators, as far as this is possible within the applications. For example, administrative tasks should only be carried out with dedicated, specially authorized administration accounts. Access to administration interfaces should be properly protected. Appropriate rules should be established for access to databases (such as application protocols) with administrative rights. Appropriate documentation requirements should be agreed.

#### OPS.1.1.2.M9 Sufficient resources for IT operations

All administrative activities should be provided with sufficient physical and human resources to properly manage them. These should take into account the routine tasks as well as unforeseeable activities. In particular for the treatment and clarification of security-relevant events suitable reserves should be available to handle such incidents in a timely manner. Maintaining proper IT operations must also be ensured when IT administrators are unavailable due to vacations, illness or training. Correspondingly trained persons as well as the necessary technical equipment should therefore be taken into account in resource planning.

As a rule, a lack of human resources leads to the elimination of documentation activities and an increase in the error rate.

In regular cycles, such as annually, resource planning should be reviewed. The collection of actual resources used and an analysis of all factors helps to adapt the planning to current requirements. It should also take into account the evolution of the threat situation, eg. For example, by incorporating appropriate studies from security companies or situational pictures from agencies such as the Federal Office for Information Security.

Resource planning should also take into account resources required for IT operations. This includes, for example, sufficient crypto-tokens to enable secure authentication of administrators or simple encryption of confidential data.

#### OPS.1.1.2.M10 Training and Information [Head of Staff]

Administrators should continually expand their knowledge in line with technical progress. Therefore, they should be enabled to participate in appropriate continuing education and training. These should be recorded in a training plan for the entire IT administration team. The aim is to keep the knowledge of IT administrators up-to-date with state-of-the-art technology and to inform them of new developments that may or may not be relevant to the institution. It should also be agreed within the team that relevant qualifications are each covered by several employees, so that representations are possible.

IT administrators should be provided with appropriate opportunities to learn about changes in the solutions they manage. Many vendors send out newsletters or notifications about security vulnerabilities and product updates, or host user forums to share news. In the case of major changes, appropriate training should be provided or opportunities exist for research and literature studies.

Administrators should be regularly aware of the security of the systems, services and protocols they service, especially current threats, known vulnerabilities and required security measures. Sources of information on this topic include:

* The Federal Office for Security in Information Technology (BSI) (see http://www.bsi.bund.de/)
* Manufacturers or distributors of programs and operating systems. These often inform registered customers about known vulnerabilities in their systems and provide corrected versions of the system or patches to address the vulnerabilities.
* Computer Emergency Response Teams (CERTs). These are computer emergency teams that serve as a single point of contact for preventive and reactive action on security incidents in computer systems. CERTs provide information in so-called advisories on current vulnerabilities in hardware and software products and provide recommendations for remedying them. Various organizations or associations maintain their own CERTs.
* CERT-Bund, Federal Office for Security in Information Technology, PO Box 20 03 63, D-53133 Bonn, Telephone: 0228 99-9582-222, Fax: 022899-9582-5427, E-Mail: certbund@bsi.bund.de , WWW: https://www.bsi.bund.de/certbund/
* DFN-CERT, Center for Secure Network Services GmbH, DFN-CERT, DFNCERT Services GmbH, Sachsenstrasse 5, D-20097 Hamburg, Telephone: 040-808077-555, Fax: -556, E-Mail: info @ dfn-cert. de, WWW: http://www.dfn-cert.de.
* There are CERTs at various universities that also provide information publicly. An example is the RUS-CERT of the University of Stuttgart (see http://cert.uni-stuttgart.de).
* Manufacturer and system-specific as well as security-specific discussion groups or mailing lists. In such forums, references to existing or suspected security vulnerabilities or errors in various operating systems and other software products are discussed. Most current are usually the English-language mailing lists such as Bugtraq, of which there are publicly available archives in many places, for example, at http://www.securityfocus.com.
* Some IT journals also regularly post articles that outline new vulnerabilities in different products.
Ideally, administrators and security officers should be aware of security vulnerabilities in at least two different locations. It is advisable, in addition to the manufacturer's information, to use an "independent" source of information.

In any case, administrators should also use product-specific sources of information from the manufacturer, for example, to know whether patches or updates are ever made available to a specific product when security vulnerabilities are discovered. For products for which the manufacturer no longer provides security patches, it must be checked in good time whether an application under these circumstances is still responsible and by what additional measures a protection of the affected systems can still be guaranteed.

#### OPS.1.1.2.M11 Documentation of IT Administration Activities [IT Operations]

Changes made to systems or specialized applications should be documented in an appropriate form. A traceable documentation is necessary in order to have an overview of the IT systems of the information network at all times and to be able to guarantee a smooth operation. This must also be possible for representatives if an administrator fails unexpectedly. A comprehensible documentation is also a prerequisite for being able to carry out system checks (eg on problematic settings, consistency in case of changes). Therefore, the changes that administrators make to the system should be documented, automated if possible. This applies in particular to changes to system directories and files. Existing logging mechanisms of systems and applications should be activated to an appropriate extent.
For all changes, it should also be documented who has hired the change, who is performing it, and what should be the purpose. Corresponding system-related documents (system logbooks) can be used for this, as well as central ticket systems in which, among other things, the executing employee, the cause, the time and the description of the changes themselves are recorded. If the ticket system is connected to a CMDB (Configuration Management Database), all changes can be directly assigned to systems, employees and categories and tracked.

#### OPS.1.1.2.M12 Regulations for maintenance and repair work [IT operation]

In order to protect the IT against disturbances, maintenance work must be carried out regularly. The timely initiation of maintenance and the review of its implementation should be carried out by a central body (eg procuring entity). The maintenance should be carried out by trustworthy persons or companies, if they can not be carried out by own personnel. The instructions of the manufacturer must be strictly observed. In the case of regular maintenance by external persons, the conclusion of a maintenance contract may be advantageous.

For each IT system, it should be documented when it was maintained and what errors were fixed (eg device pass or device or configuration management system). It is also advisable to set up an information system for maintenance and repair work. With such a system, upcoming work can be planned and documented work can be documented and the successful course can be controlled.

It should also document who is responsible for the maintenance or repair of equipment.

** Regular cleaning of IT equipment **

All types of IT equipment should be cleaned regularly. The recommended intervals depend on the type of device or the environment of use. However, cleaning should be done at least once a year, not only because it is unpleasant to work with soiled equipment, but also because soiling may affect their functionality.

Examples: Keyboards should be cleaned at the latest when they become sticky or pinch individual keys. A workstation PC should occasionally (eg once a year) also be dust-cleaned inside, unless the manufacturer's instructions suggest otherwise. For printers, negligent cleaning may compromise print quality, or limit or even damage components. Typical issues are printer rolls, printheads and toner dust accumulations.

Too much dust in IT systems can lead to heat build-up. Impurities on circuit boards (particularly effective are combinations of dust and tar and nicotine deposits) can cause leakage currents.

Deposits should therefore be removed carefully on a regular basis. In particular, effective ventilation of all IT systems should be ensured. All aerators and ventilation components must be kept free from interfering contaminants.

When cleaning IT equipment, it is imperative that the manufacturer's instructions are followed, both with regard to the procedure and the choice of tools as well as the minimum maintenance intervals.

** Maintenance and repair work in the house **

For maintenance and repair work in the home, especially when carried out by external parties, regulations should be made concerning their supervision: during the work, a competent person should supervise the work to the extent that they can judge whether unauthorized actions are performed during the work , Furthermore, it must be checked whether the maintenance order has been carried out to the agreed extent.

As measures before and after maintenance and repair work are to be planned:
* Maintenance and repair work must be announced to the affected employees in good time.
* Maintenance technicians must identify themselves on request.
* Access to data by the service technician should be avoided as much as possible. If necessary, storage media must first be removed or deleted (after a complete backup), especially if the work has to be done externally. If deletion is not possible (eg due to a defect), the work must also be observed externally or special contractual agreements must be made and trusted companies selected.
* The access, access and access rights granted to the maintenance technician must be limited to the necessary minimum and be revoked or deleted after the work.
* After performing maintenance or repair work, password changes are required, depending on the "depth of penetration" of the maintenance personnel. In the IT area, a check for malicious software should be carried out.
* The maintenance work carried out must be documented (scope, results, time, company name and possibly the name of the service technician).
* Represented companies should confirm in writing that they comply with relevant safety regulations and guidelines (eg VdS 2008 Flammable Work, Fire Protection Guidelines). This applies to all activities in which there may be a direct or indirect danger to buildings or people. Ultimately, it is important that the on-site personnel are familiar with these rules.
* After maintenance or repair work, check the proper functioning of the maintained system. In particular, the withdrawal of the interventions for testing purposes must be checked.
** External maintenance and repair work **

If IT systems are outsourced for maintenance or repair, all sensitive data stored on data media must be physically cleared beforehand. If this is not possible because the data carriers can no longer be accessed due to a defect, the companies responsible for the repair must undertake to comply with the required information security measures. With these, contractual rules on the confidentiality of data must be taken (confidentiality agreements, see also ORP.1 organization). In particular, it should be stipulated that data stored externally during maintenance should be carefully deleted after completion of the work. Likewise, the duties and responsibilities of the external maintenance staff must be carefully defined.

When carrying out external maintenance work, it must be recorded which IT systems or components have been given to whom for repair, who caused this, what the maintenance or repair order includes, when the repair should be completed and when the device should be back was returned. In order to keep up with this, it is necessary to identify the IT systems or components that identify which organization they belong to and how they can be clearly assigned within the organization.

When shipping or transporting the components to be repaired care should be taken to prevent damage and theft. If there is still sensitive information on the IT systems, they must be transported protected accordingly, eg. B. in sealed containers or by couriers. Furthermore, evidence of the shipping (repair order, accompanying note, dispatch notes) and receipt at the recipient (receipt confirmation) must be kept and archived.
For IT systems protected by passwords, depending on the scope of the repair work and the type of password protection, all or some passwords must be either announced or set to specified settings such as "REPAIR" so that the service technicians can access the devices.

After the return of the IT systems or components, these must be checked for completeness. All passwords have to be changed. Data carriers are to be checked for computer viruses after being returned using a current virus search program. All data or programs residing on the repaired device should be checked for integrity.

Remote maintenance regulations can be found in OPS.2.4 Remote Maintenance.

#### OPS.1.1.2.M13 Securing Remote Maintenance [IT Operations, Information Security Officer (ISB)]

Remote maintenance of IT systems involves special security risks. For remote maintenance, it must be distinguished whether internal or external maintenance personnel access the IT systems. In order for administrators to be able to help IT users quickly without having to go to the installation site of the respective IT systems, IT support often uses remote access access. For safety reasons, it makes sense to do without external remote maintenance. If this is not possible, then additional security measures are unavoidable.

The IT system to be maintained must implement the following security functions:

* The connection setup for remote maintenance should always be initiated by the local IT system. This can be realized by calling the IT system to be serviced at the remote maintenance center or using an automatic callback.
* The user of the IT system must explicitly agree to the remote access, eg. B. via an appropriate confirmation on the system. He should watch all activities during remote access.
* The external maintenance personnel must authenticate themselves at the beginning of the maintenance. If passwords are transmitted unencrypted, one-time passwords should be used.
* The execution of a remote maintenance must be logged. At least the beginning and the end of the remote maintenance as well as the participants are to be noted. If no one can observe the remote access on the maintained IT system, all activities involved in performing the remote maintenance must be recorded on the IT system to be maintained.
In addition, additional functions can be implemented on the IT system to be maintained:

* Impose a timeout on incorrect access attempts
* Disabling remote maintenance during normal operation and explicit release for a precisely defined period of time
* Restriction of Maintenance Personnel: Maintenance personnel should not have full administrator rights. A graded rights administration should be realized. A division of the administrative activities should also be considered (see OPS.1.1.2.M15 Distribution of administrative activities). Maintenance personnel should only have access to the data and directories that are currently affected by maintenance.
* There should be a separate user ID for maintenance personnel on the IT system. It makes sense to do without external remote maintenance. If this is not possible, the following points must be observed in addition to the above-mentioned safety measures:
* For remote maintenance via external communication connections, the accesses and the connections must be secured. The remote maintenance personnel must authenticate themselves and the transmitted data must be encrypted. For example, the connection via VPN or exclusively used connections can be realized.
* If technically possible, all activities should be monitored by third-party IT experts during administration. For example, remote administration of a client via a graphical user interface often allows all inputs and outputs to be displayed and recorded on the IT system to be maintained (see OPS.1.1.2.M18 Consistent logging of administrative activities). Even if remote maintenance is used by third parties because the know-how or capacity is not available internally, the external maintenance personnel must not be left unattended. In case of ambiguity about the operations, the local IT expert should ask immediately. It must always be possible to cancel the remote maintenance locally.
* If data or programs are created on the local IT system during maintenance, this must be clearly recognizable and comprehensible. For example, this may only be done in specially marked directories or under certain user identifiers.
* All remote administration operations must be recorded. At least the beginning and the end of the remote maintenance as well as the participants are to be noted. If no one can observe the remote access on the maintained IT system, all activities involved in performing the remote maintenance must be recorded on the IT system to be maintained.
External maintenance personnel should be subject to contractual confidentiality provisions (confidentiality agreements, see also ORP.1 Organization). In particular, it should be stipulated that data stored externally during maintenance should be carefully deleted after completion of the work. Likewise, the duties and responsibilities of the external maintenance personnel must be carefully defined.

More on this topic can be found in OPS.2.4 remote maintenance.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### OPS.1.1.2.M14 Administrators Security Check (CIA)

The possibilities to have the trustworthiness of new or external personnel checked are legally very limited in Germany, but also in many other countries. In addition, the results are usually not very meaningful, such. B. in police certificates. In principle, however, should be checked before the acquisition of new or external employees in projects, whether

* These have sufficient references, eg. From other, similar projects, and
* the submitted curriculum vitae of the candidate is meaningful and complete.
In addition, it may be useful to have academic and professional qualifications certified, for example, by inquiring at the university or from previous employers or clients. The identity of the candidate should also be verified. B. by presentation of identity documents.

If external personnel are deployed internally or if internal applications and data can be accessed through projects, cooperations or outsourcing projects, comparable checks should be carried out as for own employees. When drafting contracts with external service providers, it should be contractually stipulated which side has to carry out such checks and to what extent these are carried out.

#### OPS.1.1.2.M15 Distribution of administrative activities (CI)
Many operating systems, applications, and IT components provide the ability to split the administration role and distribute administrative activities to different users. If there are special task administration roles, it should be used. In particular, when multiple people need to be assigned administrative tasks in large systems, the risk of over-relinquishing administrator roles can be reduced by sharing tasks so that administrators can not uncontrollably make unauthorized or unintentional changes to the system.

However, even if administrative activities are split, many systems automatically create an administrator account that is not restricted (depending on the system, root, superuser, or supervisor.) Access should be as restrictive as possible he is protected by a multi-factor authentication.

If there are increased requirements for protection against tampering by or with the assistance of IT administrators, different administration roles should be defined in larger institutions, each staffed by different people. The division is best based on the attack scenarios against which protection is to be achieved. Conceivable z. As the following divisions, which can also be combined with each other.

It should be noted that a finer division means that more staff must be available to cover all relevant activities throughout - even on vacation and illness.

With limited human resources, the division of administrative activities can also be limited to particularly vulnerable systems and applications.

#### OPS.1.1.2.M16 Access restriction for administrative access (CIA)

The protection of administrative access to IT systems and components can be significantly increased if the access is not only protected by an authentication mechanism for the administrators (see OPS.1.1.2.M5), but is also limited on the network side. Administrative accesses and interfaces can then only be accessed from a network segment that is separate from the networks in which the system offers its services.

So z. For example, SSH accesses or web interfaces for administration can be linked to a separate network card, which is integrated in a separate administration network. A user who addresses the system via a different network card and a different network can then not call these accesses. It should be noted that a segmentation of the network in different protection zones must then be reflected in the administration network - otherwise there is a risk that an attacker abused after the successful adoption of a system, the administration network to bypass security gateways.

Then selected client systems can be integrated into the administration network, from which the administrative accesses of the systems can be achieved. Even better is the establishment of a jump server, on which the IT administrators must log in to get from there into the administration network. All administrative accesses can be controlled, logged and, if necessary, recorded.

With firewall and DMZ systems in particular, it must be ensured that administrative interfaces can not be reached via external connections.

#### OPS.1.1.2.M17 IT Administration in the Four Eyes Principle (CI)

For particularly critical systems or for certain critical activities, it may be desirable for administrative activities to be conducted on a four-for-one basis. One administrator then carries out the work while another administrator is present and observes the activities.
This requirement can be implemented by an organizational specification (eg a work instruction). Ideally, it is supported by technical measures, eg. For example, by dividing the administrative password into two halves, each known to only one administrator. This allows you to log in with administrative rights only if both administrators are present.

In some cases, systems also provide built-in functions for implementing a four-eye principle, such as: For example, setting up and enabling firewall rules on a security gateway.

The implementation of a four-eyes principle requires more staff and can delay the availability of administrators in an emergency. It should therefore be carefully weighed and is usually implemented in the case of very high security requirements (eg for the key servers of qualified trust services).

#### OPS.1.1.2.M18 Consistent logging of administrative activities (CI)

Administrative activities should be logged as much as possible. On systems with high security requirements, they should be consistently logged.

Not only the logon to the system (see OPS.1.1.2.M5 Administration IDs), but also all commands issued by the administrator or called functions should be logged. Because the logging should not be shut down or bypassed by the administrator, ideally it does not take place on the administered system itself, but in an environment that is not under the control of the implementing administrators.

This can be realized, in which administrative access to IT systems and components is only possible on the network side via the use of a jump server, on which a complete logging of the executed activities takes place. For this application scenario, ready-made solutions are available on the market that can record both console-based access and access via graphical user interfaces. For console-based access, there are also various free solutions.

In order to achieve the purpose of protection, the recorded logs may not be changed or deleted by the administrators themselves. The logged data should be evaluated at regular intervals by an independent third party (eg auditor).

#### OPS.1.1.2.M19 Consideration of High Availability Requirements [Information Security Officer (ISB)] (A)

If high availability requirements exist in the IT environment to be administered, suitable concepts and measures must be implemented to meet these requirements. As a rule, this requires an overarching approach. In its High Availability Compendium ("HV Compendium"), the BSI has compiled a suitable methodology and numerous assistance in the analysis, planning and implementation of highly available IT environments. The compendium is available free of charge on the BSI website and is divided into several volumes and sections:

High availability planning should be documented with the underlying methods, assumptions and outcomes. Responsibility for the preparation and updating of the high availability concept must be transferred to a suitable body within the institution, eg. B. an IT architect.

High availability planning and security management must mesh. Thus, the HV requirements for the determination of protection requirements in the information security process with regard to the protection goal availability must be considered. Conversely, findings from security incidents that affect this protection objective must be fed back into the HV planning.
The realization of high availability requirements should also be taken into account during audits and revisions. This can be z. These include, for example, carrying out load tests or testing the intended high availability measures (eg pivoting data centers).

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Additional information on hazards and security measures in the area of ​​"Proper IT administration" can be found in the following publications, among others:

*

 #### [27001A12] ISO / IEC 27001: 2013 - Annex A.12 Operations security

  

 Information technology- Security techniques- Information security management systems- Requirements, especially Annex A, A.12 Operations security, ISO, 2013

  

 
*

 #### [HVK] High Availability Compendium

  

 BSI, (last accessed on 28.09.2017)
 [https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/HVKompendium/hvkompendium\_node.html](https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/ HVKompendium / hvkompendium_node.html)

  

 
*

 #### [ISFSY] The Standard of Good Practice - Area SY System Management

  

 especially Area SY System Management, Information Security Forum (ISF), 06.2016

  

 
*

 #### [NIST80053] NIST Special Publication 800-53

  

 Security and Privacy Controls for Federal Information Systems and Organizations, Revision 4, NIST, 04.2013
 <Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>
