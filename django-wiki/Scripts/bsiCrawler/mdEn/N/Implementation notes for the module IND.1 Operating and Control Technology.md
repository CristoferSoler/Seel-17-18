Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Operational Technology (OT) is hardware and software that detects and effects change through the direct monitoring and / or control of physical devices, processes and events in the enterprise [GART1].

The industry, which includes Critical Infrastructures, includes industrial control systems (ICS) and automation solutions, which are responsible for all kinds of control functions. Further examples are laboratory equipment (eg automated microscope or analysis tools), logistics systems (barcode scanners with small computers) or building management systems.

The customary physical separation of OT from other IT systems and networks in office applications is nowadays only applicable in exceptional cases with increased protection requirements due to increasing integration requirements. Multi-level production steps and their overall control as well as regulatory requirements require an increasing opening across organizational boundaries. This trend is accelerated by the trend towards optimizing manufacturing processes to increase competitiveness in the context of Industry 4.0.

As IT components and technologies from office IT are increasingly being used in OT in addition to OT-specific components, they are now exposed to comparable hazards. At the same time, OTs differ significantly from traditional IT, making it difficult to apply established security procedures. For example, there may be restrictions based on manufacturer specifications or legal requirements that prevent or hinder changes to components. An example of this is the application of security updates or subsequent hardening measures. The OT is usually also subject to significantly longer lifecycles, even beyond the manufacturer support, so that the availability of security updates can not be consistently guaranteed.

This convergence of technologies between office IT and OT will demand increased cooperation between the know-how bearers of both functional areas in the future. The technological know-how for IT, communication and cyber defense is currently mostly in the Office IT departments. However, a successful solution must take into account the circumstances of the OT infrastructure as far as possible. However, this can only be done with the support of OT managers.

### 1.2 Life cycle

The life cycle of ICS results from the operating life of the respective production plant. This is always much longer than the usual time periods in office IT. The typical duration is ten to fifteen, sometimes even 20 years and longer. In the office IT, it is usually only three to five years.

** planning and conception **

Building a secure (in terms of information security) OT infrastructure requires appropriate planning. Already in the conception phase, aspects relevant to information security should be analyzed and considered. This serves to identify risks in the development process at an early stage and, as a rule, can then be treated more economically. As part of the planning, the inventory and the initial documentation should be created (see IND.1.M4 OT Infrastructure documentation).
The development of a suitable zone concept (see IND.1.M5 Development of a suitable zone concept) forms a central element of the conception phase which, depending on the protection requirements, may require a more or less pronounced partitioning (see IND.1.M16 Greater isolation of the zones). The design also includes the handling of removable media and mobile devices (see IND.1.M9 Restrictive use of removable media and mobile devices) and secure (remote) administration (see IND.1.M8 Secure (Remote) Administration) account. This should be additionally supported by concepts for protection against malicious programs (see IND.1.M3 protection against malicious programs).

** ** Procurement recommendations

Obtaining a secure ICS infrastructure is a complex process in which the necessary requirements must be meaningfully shared and communicated between the operator, integrator and manufacturer (see IND.1.M11 Secure Procurement and System Development).

**Implementation**

For the ICS infrastructure to operate safely, it must be integrated into the security organization (see IND.1.M1 Integration into the security organization). Employees who perform tasks within their framework must be sensitized and trained with regard to typical hazards (see IND.1.M2 Awareness and Training of Personnel). In order to be able to design and evaluate measures, in-depth infrastructure documentation is indispensable (see IND.1.M4 OT infrastructure documentation).

In addition, further process components are required to form the necessary framework in which safe operation is possible: IND.1.M6 Change management in OT and IND.1.M7 Establishment of authorization management, with additional protection requirements possibly also IND.1. M15 Checking and Monitoring Permissions and IND.1.M14 Strong Authentication to OT Components.

**Business**

The secure operation of an ICS infrastructure includes a bundle of processes and measures described in IND.1.M6 Change Management in OT. The basis of safe operation is the reliable detection of faults and anomalies and is highlighted with IND.1.M19 monitoring, logging and detection.

** Emergency Preparedness **

Also with regard to the emergency planning, there are some special features in the field of ICS. Appropriate concepts for infrastructure recovery following component failure or infrastructure compromise must be described and presented.

2 measures
-----------

The following are specific implementation instructions in the area "Operating and Control Technology".

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### IND.1.M1 Integration into the security organization

An information security management system (ISMS) for the OT infrastructure must be established. This OT ISMS can exist either as a stand-alone ISMS or as part of an overall ISMS and should explicitly include in its scope the definition of goals and values, processes, roles, responsibilities, and specifications for the OT infrastructure.

In particular, consideration should be given to the specific requirements of OTs, which derive from the specific conditions, such as B. Derive rules for warranty. Here, the alternative approaches to office IT should be outlined.

** Building a security organization **

The institution must set up a security organization that governs the roles and responsibilities for the information security of OT infrastructure and components. The safety organization should consider all parties involved in the operation of OT components (eg manufacturer, integrator / machine builder, outsourcing partner, third party vendor, physical security specialist, production and maintenance manager).
An overall information security officer in OT must be designated and known within the organization. In the following, this is referred to as ICS Information Security Officer. In larger institutions, an information security officer should also be designated for each installation, alternatively per component type / layer / zone.

In this case, both a security organization for the entire institution can be built and operated, which includes the areas of Office IT and OT, or separate security organizations for the two areas. To exploit synergies and avoid planning mistakes and risks, close cooperation between the OT and Office IT experts must take place. Which structure is suitable for an organization depends strongly on the existing structures and well-established processes in an institution. It is crucial that a flow of information and knowledge takes place in both directions and that those responsible in each area are taken seriously. For this, both sides have to be open to the particular peculiarities of the other area and, to avoid misunderstandings, consider the culture and language of the other side. A dual head (Information Security Officer / ICS Information Security Officer) can be a useful solution in some institutions, if the division of tasks and interfaces are clear and clarified in writing.

** Attention legal framework conditions **

Legal, regulatory and other specific requirements for the OT and the respective sector or sector must be known and interpreted in terms of their impact on the institution. This applies in particular to institutions that operate critical infrastructures, but increasingly also in other areas. In addition to the national requirements, European and international regulations may also have to be observed. Responsibilities and processes should be established to ensure that all relevant requirements are promptly communicated to the key bodies.

** Definition and compliance with specifications **

There should be a process of writing, communicating, updating, evaluating and implementing concrete guidelines for specific subject areas (guidelines / policies) in the ICS area. These can be partially taken from the field of office IT, where appropriate and available. Often, however, adjustments are needed to reflect the specifics of OT.

When selecting components, a check should be made of defined (functional and information security relevant) requirements. In this case, individual components can be the subject of the test up to the entire OT.

**Additional information**

Further information on the structure and design of the safety organization is documented in the ISMS Safety Management module.

#### IND.1.M2 Sensitization and training of personnel

The implementation of the necessary awareness-raising and knowledge-building of the staff can take place in different ways. These can be special training events or online training. Contents and frequency should be based on the tasks of the employees and the threat scenarios. A one-time information is to be carried out at least for all employees.

Operating personnel should be made aware of the threats or problems that are relevant to an OT-specific workplace. This can be z. As the handling of removable media or smartphones.

OT-Responsible and ICS Information Security officers should be trained more specifically on the threat situation and need for action.
For SMEs, it is usually advisable to have the training carried out by external experts, since they can always bring up-to-date practical knowledge. For larger institutions, it may be worthwhile. the establishment of an own course program.

Proposals for more detailed training plans may, for. For example, see the document "Recommendations for Further Training and Qualification Measures in the ICS Environment" [BSI-CS 123].

In addition, it is recommended that social engineering be promoted regularly and vigorously, for example through education campaigns or through careful tests coordinated with data protection and the works council, which must not personally expose anyone.

#### IND.1.M3 Protection against malicious programs

A malicious program must consider the threatened OT components and all possible routes of infection, assess risks and, where necessary, establish appropriate technical and organizational safeguards.

Among the possible routes of infection include:

* All external interfaces including connections to the office network, Internet and other extranets
* Removable disk
* Service station and programming devices, also from service providers
* as well as fundamentally newly procured components (hard drives, USB sticks, software with Trojans, etc.)
** ** virus scanner

If the installation and unrestricted operation of anti-virus programs on OT components is possible and approved by the manufacturer / integrator, these systems should be automatically supplied with up-to-date virus signatures.

** Secure configuration of anti-virus programs **

Due to the high availability requirements in OT, critical systems may require custom configuration for antivirus programs. Settings should be deactivated that could lead to an unintentional impairment of the production (eg due to a heavy system load due to a virus scan). Often, manufacturers only release such limited configurations for running anti-virus programs on the OT components.

Antivirus programs can usually operate in two different modes. First, before accessing applications or files, a scan generally takes place, or the scan is initiated manually or timed. Usually the antivirus program should automatically scan for all accesses.

The selection should be based on the recommendation of the manufacturer of the virus protection program and the OT component. If continuous testing (eg for performance reasons) is not possible, alternative protective measures should be taken.

In addition, a complete scan of all data should be performed periodically. An additional, complete scan with up-to-date signatures should be performed after initial installation and after changes to the system.

Basically, the following settings should be taken into account when configuring the virus protection programs:

* Manual scans should only be performed and documented at standstill of production.
* Only local media should be checked. Network drives should not be scanned to avoid parallel scanning by multiple machines.
* Only administrators may have the authority to configure or disable the anti-virus program.
* The antivirus program should report finds to a central location. An automatic termination of the processes / programs can lead to a failure of the OT component with a False Positive Fund and must therefore be critically examined.
The installation process and configuration should be documented for each OT component.

** Central viruses **
As far as possible, the OT network should be operated autonomously and only allow compulsory connections to other networks. If connections to other networks are necessary, this should not be done directly, but always be routed through a proxy server.

Therefore, the signatures for the anti-virus program should not be obtained directly from the Internet, but via a central virus signature distribution service in the DMZ. It loads the current signatures on behalf of the Internet and makes them available to the OT components. Thus, no direct connections to the OT in the Internet are required.

** Timely update of virus signatures **

Often timely updates of virus signatures and virus protection programs on OT components are not possible. Therefore the following aspects have to be considered.

The OT components should be grouped according to their possible update interval. In addition, redundantly configured OT components should be assigned to different groups in order, for example, to be able to react immediately to the distribution of incorrect virus signatures in the production environment (eg false positives).

The distribution of virus signatures into the groups with redundant ICS should be done with a time delay (eg, 12 hours) to continue operating with the second system if problems persist.

Due to the high availability requirements, only signatures released by the manufacturer / integrator of the OT component and classified as noncritical should be distributed.

** Virus protection program on the firewall (virus wall) **

A virus wall examines the traffic between two networks for malicious programs. In this way, it can test data transmitted by OT components with no or limited antivirus software. For this purpose, these OT components are placed in a separate network segment and the traffic to and from this network is filtered by an application level gateway (ALG) with anti-virus program installed and examined for malicious programs. See also IND.1.M16 Greater foreclosure of the zones.

** Alternatives for virus scanners **

However, anti-virus programs typically can not be installed on all components. Possible limitations may be a lack of manufacturer release, unsupported operating platforms (eg field systems or PLCs), lack of updating of virus signatures or potential availability risks, so that in most cases complementary or alternative technical or organizational safeguards must be implemented , Alternative technical protective measures can be:

* Securing external interfaces of an OT component (site connections, access by service providers, interfaces to the office network and the Internet)
* Outlaw endangered systems into secured network segments (with a filtering component if needed to connect to other zones (see Virus Protection Program section above)
* Restricting removable media (such as USB media)

 
+ Disable system interfaces
+ Use of a removable disk sluice


 
* Establishment of network-based access controls in the user area (avoidance of third-party devices)
* Use of network-based protection systems

 
+ Application Layer Gateways (ALG)


 
* Application whitelisting (restriction of executable programs to ICS)
* If possible, periodically scan the OT components from a boot media or USB device with the latest antivirus software and current signatures, for example, during a scheduled maintenance window (in this way, an infection can be detected, at least retroactively, and then eliminated).
Alternative organizational protection measures can be:

* Regulations for data exchange and use of removable media
* Prohibition of connecting third-party devices
* Manual virus scanning with special offline antivirus solutions in maintenance windows
In order to effectively protect the OT from malicious programs, coordinated and appropriate security measures must be selected and implemented, taking into account the environmental characteristics. On this basis, an anti-virus concept has to be developed, which shows how the protection against malicious programs is achieved.

** Application Whitelisting **

It is possible to monitor and restrict the execution of programs by means of special application control software. Unlike common anti-virus programs, it does not attempt to block unwanted software, but rather attempts to allow only desirable programs to execute.

As a result, two different approaches can be distinguished to detect and prevent applications and unwanted behavior of a system (eg in the case of malicious programs). In the blacklist approach of common anti-virus programs, this is done on the basis of known signatures and heuristics of unwanted applications. This approach has some weaknesses, such as: B. that new malicious programs can change automatically with each new copy and thus have a new, yet unknown signature. Thus, the successful protection depends on the timeliness and availability of the signatures.

With application whitelisting, only such applications and behaviors are allowed that have been explicitly released. Everything else is forbidden. This way, there is no dependency on current signatures. In particular, in systems such as in the OT environment, which are subject to only minor changes due to software installations, this method is suitable. Therefore, as far as possible, an application control should always follow the whitelist approach.

For example, to prevent the execution of unauthorized software, such protection software can resort to the following different attributes:

* Certificates (signing of trusted software eg by a central office),
* File system path (certain areas are declared trusted),
* Hashes (the applications and possibly unauthorized changes are identified by a hash of the files),
* System and user behavior (eg use of certain TCP ports, operation only at certain times).
### 2.2 Standard measures

Together with the basic measures, the following measures are in line with the state of the art in the area of ​​"Operating and Control Technology".

#### IND.1.M4 Documentation of the OT infrastructure

A complete, up-to-date and practically usable documentation of the OT is essential for proper operation.

This is all the more true for information security, since it is only on this basis that it is possible to determine the necessity, adequacy and degree of implementation of many other measures and to systematically identify possible weak points and attack vectors.

The depth of the documentation may differ. For example, a PLS that is a closed system may be limited to the outside interface. As a rule, the PLS itself has an internal administration or a uniform software / hardware version depending on the system version. In other cases, all components can be documented.

** Creating and Maintaining the Documentation **
The form of documentation management should be geared to the needs of the target group and should be as practicable as possible. Documentation may take the form of one or more documents embedded in a web site or specific IT tools. However, the existing requirements for the availability of the documentation, which must be accessible, in particular, in fault and emergency situations, must be observed. This can be done, for example, by replication on emergency systems or as a hard copy on the respective workstation and / or at the emergency location. At the same time, the filing should also take into account the sensitivity of the documentation in order to prevent unauthorized access.

The operator must ensure that changes relevant to the operation are recorded in the system documentation. Through regular checks on up-to-dateness, failures in daily business can be identified and made up for.

** Request exchange with integrator and manufacturer **

Wherever essential parts of an OT infrastructure are set up and maintained by service providers (integrators or machine / plant builders), requirements, evidence and documentation must be passed on in both directions: safety requirements should, if possible, be included in the tendering process, but at the latest during the Implementation of the project to be communicated to the contractor.

It should include or provide up-to-date and comprehensive documentation containing information on security features, vulnerabilities, configurations, and necessary safeguards.

** ** Inventory

To avoid incompatibilities and inconsistencies of software in specific versions as well as configurations (eg IP address conflicts), the configuration of the individual OT components should be documented in a list. In addition, OT components can be quickly identified in this way when new updates become available or configuration changes are required. Even if updates are not possible, such a list can be used to evaluate the potential impact on a timely basis.

The list can, for example, document the following properties:

* Functional name,
* Computer name,
* Responsible administration staff with stored contact details (possibly also service times),
* Physical site,
* MAC address (es),
* IP address (es),
* DNS name,
* FQDN,
* Manufacturer,
* Model / product type
* Operating system,
* installed applications and services, including ports and protocols used,
* Patch level of each software with the patch import date (for IT systems such as PLCs and related devices, it is important to have firmware levels of each CUPU and each module),
* Date of the last virus scan (or automatic repeat interval) and
* Backup interval (full and incremental), extent of backup and last performed backup.
** Network or network structure plan **

The structure of the network should be documented in a physical and a logical network. If it makes sense for the environment, the physical plan should include the locations and OT infrastructure, eg. As cables, buildings and wireless connections represent. The plan could include:

* Name / description and functionality of the systems,
* at least one technical feature by which the respective system / network segment is identifiable, eg. B.

 
+ IP network addresses and netmasks z. 192.168.1.0/24,
+ IP addresses of all connected network interfaces z. Eg 192.168.1.54
+ MAC addresses (at least if and where IP communication is not the primary issue),


 
* (if available) DNS name, resp.
* (if available) FQDN (Fully Qualified Domain Name).
The logical network does not represent the physical realities and focuses on the structural view and the security zones.
In addition to the communication possibilities represented by the network, the communication relationships between the components should also be recorded. This means which components need to communicate with each other. This is necessary to be able to identify and prevent unauthorized data traffic.

Redundancies (similar systems with analog function, configuration and the same protection requirement) can be summarized in the network structure plan, as this serves for readability. However, if the availability requirement is high, the redundancies (number, type (eg, hot standby, failover, load balancing, etc.)) should emerge from the network structure plan. This can be done by annotating the objects so as not to inflate the plan itself.

** Administration and user manuals **

For safe and uninterrupted operation it is necessary that the service and maintenance personnel as well as administrators know all the functions of the OT and can operate them. If staff failures occur (eg due to illness or termination), it should be ensured that the information required remains available in the institution and accessible to the representatives.

Therefore, an administration and user manual should be available for the OT and each application (possibly also a document covering both topics). In addition to operational controls and procedures, documents should also cover information security aspects, including:

* Necessary firewall rules (with service, protocol and port),
* Instructions for curing specific applications,
* Instructions for secure configuration,
* Specific risks (eg when activating a specific configuration),
* System recovery (for emergency preparedness).
The documentation should enable the continuation of operations by third parties.

** Energy industry and other KRITIS sectors **

Additional requirements apply to the energy industry due to the IT security law. In accordance with §11 (1a) of the German Energy Industry Act (EnWG), the Federal Network Agency's IT security catalog requires not only the establishment of an ISMS that meets the requirements of DIN ISO / IEC 27001, as amended, but also the implementation of DIN ISO / IEC 27002 standards and DIN ISO / IEC TR 27019 (DIN SPEC 27019) as amended, including the creation of a specific form of the network structure plan. The network operator must provide an overview of the applications, systems and components affected by the scope of the IT security catalog with the main technologies to be found and their connections. The overview must be differentiated according to the technology categories "Control System / System Operation", "Transmission Technology / Communication" and "Secondary, Automation and Telecontrol Technology". Chapter E.IV Table 2 of the IT Security Catalog contains a brief description of the technology categories as well as a few examples, which usually have to be adapted to the concrete OT. In the scope of the ISMS as well as in the network structure plan, at least the telecommunication and EDP systems must be included, which are "necessary for a safe network operation". The definition of the latter category is to be made and justified by the institution.

Other KRITIS sectors will also have special requirements in the future. Here the respective regulation and implementation practice must be observed.

It is important to make a well-founded definition of which systems are necessary for the safe operation of the industrial or KRITIS functions. This can be z. In the network and should be compatible with the zone model (see IND.1.M5 Developing an Appropriate Zone Concept).

#### IND.1.M5 Development of a suitable zone concept [IT operation]
The OT network should consist of several network segments with individual protection requirements. The data traffic between the different levels (see figure: levels of the automation pyramid) should be regulated by a data flow control (eg by means of a firewall) to the necessary operational level.

Figure: Levels of the automation pyramid

In addition to the separation of networks with different functionalities at the same level, multi-site networks or generally organizationally independent machines / plants should be segmented among each other (horizontal segmentation). So z. B. prevents malicious programs from spreading to all machines without hindrance.

The establishment of a connection should basically be established from the network segment with the higher protection requirement into the network segment with the lower protection requirement.

A bypass of the network separation by undocumented connections must not take place. In particular, no uncontrolled connections to network segments with different protection requirements should be allowed.

** ** consideration

In the conception and implementation of the zone model, operational dependencies must be determined and their effects examined. Thus, the operational stability is ensured within the framework of existing requirements and appropriately designed taking into account the requirements of the OT environment. For the assessment, the availability requirements of each zone must be determined according to the requirements of the technical processes according to the maximum principle across all systems in the zone.

#### IND.1.M6 Change management in OT operation

Over the lifetime of the OT, the changes to the system and the potential new hazards must be taken into account on an ongoing basis and taken into account accordingly.

**Documentation**

When operating the system, it is important to incorporate changes and adjustments in the existing documentation. The goal is to always have up-to-date documentation that reflects the actual state of the systems. Continuous updating eliminates the need for complex inventory analyzes.

** Change Management **

Administrative changes to the existing infrastructure or OT components can influence the information security of the environment and should be planned, checked, adequately tested, performed and documented through a binding change process. The nature of the process depends heavily on the respective organization or OT and should be comprehensibly documented. In less complex environments with a small administration team, the change process can essentially be based on procedural requirements (planning, information requirements for maintenance, procurement of software and updates, execution of tests (test concept), regulations on the use of service providers) as well as documentation obligations (eg. comprehensive or system-bound administration journal). In larger organizations, there may be a more complex change process consisting of application, review, testing, and approval procedures, and the use of supporting tools (forms, technically supported workflows, CMDB, etc.).

** time synchronization **

A large number of processes, but also administrative activities, are based on a precise and coordinated time (eg the traceability of distributed protocol data, the addition of additives in production at the right time, etc.). It has to be considered based on the application requirements, how the time synchronization takes place.

For synchronization, the Network Time Protocol (NTP) or IEEE 1588 can be used.
The time signal for the systems should come from a trusted source. For example, zones of high criticality should not move their time from a less protected zone if the signal could possibly be tampered with. The clients on the OT components should interpret the time in a consistent, standardized format (for example, considering time zones, winter and summer time).

#### IND.1.M7 Establish Permission Management

Under permissions are privileges of persons to

* Access (physical access to IT systems),
* Access (accessibility of a system via network) or
* Access (executability of programs and functions as well as usability of data)
to understand.

Incorrectly set permissions can significantly affect the security of an IT environment. Excessively or illegally assigned rights can lead to disruption through misuse or malfunctioning, while rights that are too low can make regular procedures difficult and in critical situations can hinder the effective handling of malfunctions.

Authorizations must therefore be assigned according to the needs of the minimum principle and actively maintained with regard to changes. For this a continuous process (authorization management) is required.

Permission Management must meet the following basic requirements:

** Providing an application, review and approval process **

Authorizations must be formally requested and successfully verified before they can be awarded. An authorization request should be checked by at least two persons. The examination could be carried out by the respective supervisor and by the respective application or system manager.

** Audit-proof maintenance of an inventory overview and history **

Authorization management must have a complete overview of the authorizations assigned to a person. This overview must also include the authorization history of a person as well as information about the respective authorization request and the test and release process carried out.

The inventory management of user accounts and authorizations must be presented in usable form and used as the basis for a target / actual comparison.

** Verification of existing access **

Authorization management requires an interface to the HR process, so that status changes in employee employment relationships can be taken into account in a timely manner. Additions and authorizations of fixed-term and external employees should always be limited in time for the duration of the employment or commissioning relationship.

In addition, a manual verification of the configured user access should be carried out in a defined cycle (eg annually).

In the case of IT authorizations, special requirements for authorization management must also be taken into account.

** Use of personal user access **

If supported by the system, user access for interactive system usage should be created by users and administrators as personal accounts and assigned to the owner. If the use of personal access is not technically possible or not feasible in the existing environment, the allocation of group access must remain comprehensible.

** Role-based authorization for personal access **

Authorizations should always be assigned to personal user accesses via groups. To perform a user role, a user account may be a member of one or more groups. The authorization groups available for a system are specified by the respective systems and applications.

** Assignment of special access rights **
Special network-side access permissions, such as those set up by firewall or Access Control Lists (ACL) on screening routers, are typically set up for the workstations of specific individuals. Such an access rule is thus to be understood as user authorization and should be managed in the authorization management and checked in the context of the regular verification.

The management of authorizations can be done independently for the OT by the institution, or be integrated into an institution-wide authorization management.

**Groups**

Basically, the use of personal user access due to the higher traceability and user responsibility is preferable. In certain cases, however, the use of functional group access can be represented, if this can achieve operational advantages or improved availability, which would otherwise be difficult to achieve by other means. Each group access must be documented separately. Persons who have access to the access to persons must, for example, be organized. B. be documented comprehensibly on shift schedules. An example could be the use of an "operator" access in a control room, which is staffed around the clock and in which all persons with access know each other. The functional accesses, as well as other accesses, must be integrated into the proper process of managing entitlements. It is especially important to ensure that only the minimum required rights are granted. In case of doubt, different tasks can be distributed to different accesses, so that ideally as much of the staff as possible needs read-only access. Each access must be assigned to a responsible person.

** Responsibility for functional and technical user access **

Functional accesses should be assigned to the person responsible for the application. Technical user and service accesses (for example for machine-to-machine communication or integration with other applications) should be assigned to the person responsible for the operation of a component.

** Password distribution and management, password **

A password policy should be implemented that takes into account the following points. Technical solutions as well as organizational measures can be defined.

* The user should be prevented from selecting weak passwords (eg length, alphabet with numbers and special characters) by complexity requirements.
* The password should only be valid for a predefined period of time. The user should then be prompted to choose a new, non-old password.
* The number of failed login attempts should be limited (for example, temporary blocking of user access).
When selecting the measures, it must be ensured that the system always remains operable and dangerous conditions are excluded.

A possible alternative to passwords are smart cards.

** avoidance of abuse **

Unauthorized access to systems should be prevented. It should be recognizable and documentable which user was active (see IND.1.M10 Monitoring, Logging and Detection).

There are certain operating situations that require immediate operator access to the OT. A logout or screen lock is not acceptable. In these cases, the systems should be protected from unauthorized access by compensating protective measures (eg occupied control room).

In less critical areas, the operation should be locked and only a display of the current information. In this way, observation is still possible, but hinders unhindered access.
For authentication, solutions using chip or RFID cards with user PIN can be used to avoid the entry of complex passwords.

#### IND.1.M8 Secure Administration [IT Operations]

The management of active system components, such as server systems, network or OT components, is performed either locally at the local console, via a serial interface or, in the case of networked components, after the initial setup, typically via network-based remote access.

** startup **

For the initial configuration of a component, a guide or checklist should be created to ensure that security-related settings are enforced independently of the person. The respective settings to be made are component-dependent. For example, they may include (enumeration not complete):

* Disable

 
+ unnecessary or unsafe administrative interfaces (SNMP, HTTP, service ports, etc.)
+ dispensable standard user accounts
+ or uninstalling unnecessary functions


 
* Enable security features:

 
+ Configuration of secure remote administration interfaces (SSH, HTTPS)
+ Logon banner
+ Session timeouts or session time limits
+ Minimum password security
+ Limitation of administrative access to administration networks (Access Control Lists)
+ Encrypted storage of passwords
+ Time synchronization
+ Enable system logging / configuration of logging servers
+ Check for and change potentially existing default passwords
+ Integration into central administration or authentication systems
+ Secure storage of administration passwords
+ possibly local firewall or integrity checks


 
The initial configuration can also be performed on the basis of an initially created reference configuration. The initial configuration should, if possible, be done in a secure environment and should always include the application of the available security patches before a component is put into service. Before integration into the OT network, it is recommended to check the authenticity of the component and to test for compromising behavior.

** Configurations on the local console **

Configuring OT components on the local console for many components is limited to the initial configuration at startup, so that management can be done in operation via network-based remote access. Non-networked components continue to be configured through the local console. In addition, the local console is often maintained as an alternate configuration option in case of network infrastructure failure and is not disabled.

Physical access to enabled system consoles must therefore be appropriately restricted, such as secure premises or lockable server cabinets. Furthermore, access to the console should be password protected and limited to authorized access.

**Remote maintenance**

Remote maintenance should always be done using secure protocols such as TLS-secured connections, SSH or SNMPv3. Clear text protocols should be avoided. If possible, the establishment of a dedicated administration network or access restrictions (ACLs) should protect against unauthorized access.
The security of the maintenance computer is indispensable for the safe operation of the system. These must therefore be adequately protected against compromise or abuse. The basis for this should be the relevant building blocks of the IT-Grundschutz for the maintenance computers. Particular attention should be paid in this context to the aspects of access, network-based access, use of the system and external interfaces such as Internet, e-mail or the use of removable media. The operation of an up-to-date virus scanner may be necessary or avoidable depending on the threat situation.

** Support Hits **

Externally accessible remote maintenance access must be planned appropriately and effectively secured against misuse. Suitable measures for this are:

* Access Restrictions Access to remote maintenance access should be restricted to known, predefined network areas where possible.
* Secure authentication External connection setup should be securely authenticated. This can be achieved, for example, by means of an additional token or client certificate. With dial-up connections, a call-back procedure can be set up for a stored telephone number.
* Use of secure protocols External access to OT environments must be via encrypted and integrity-assured protocols only.
* Use of jump servers External remote maintenance access to OT components should not be done directly, but via hardened jump servers in a DMZ infrastructure (see IND.1.M16 Greater isolation of the zones). The bounce server can be protected against attacks as well as being up-to-date while the OT component is still out of date due to availability requests or missing updates. This protects the component from unauthorized or malicious access, prevents data transfers, enforces checks for malicious programs, and enforces session time limits or disconnections during inactivity.
* Demand-dependent activation If remote access is required only occasionally, the external access should be deactivated by default and activated only when required.
* Access logging should be traceable by appropriate logging. In the case of very high protection needs, consideration should be given to recording the administration session by appropriate procedures.
When designing the remote access, care should be taken to prevent the use of unwanted tunnels (TLS, SSH, IPsec) to circumvent security measures. Such tunnels could make components and services of the OT components undesirably accessible.

#### IND.1.M9 Restrictive use of removable media and mobile devices

Removable media on the one hand (eg USB stick) and mobile devices on the other hand (eg service laptop) have become main entry points for attacks, as these components often cross the carefully constructed zone boundaries and can be exploited to prevent malicious software or Move orders into or send out sensitive information.

** Regulations on removable media and mobile devices **

The regulation should address the scope and document possible defined exceptions and deviating regulations. It should be documented procedures in which removable drives are used.

Use of private removable data carriers or other mobile devices for data transport or connection to OT components should generally be ruled out.

** Restriction of use **

On the OT components the use should be restricted to certain devices (device control). This is usually possible with functions of the operating system or via additional software.
If it is necessary to transport media or devices between different zones, there must be a process with which the media or devices are protected and checked. For service providers, an equivalent process should apply.

In the new planning of plants and systems should be dispensed with the use or restrictive handling and safe use of removable media are forced.

** Removable Disk (Quarantine PC) **

A quarantine PC can test for malware on behalf of OT storage media. For this purpose, employees must be instructed to check storage media from an untrustworthy source (eg USB sticks) for malicious programs by means of the quarantine PC before such data carriers are transferred to the OT network or to OT components with no or limited access Antivirus program can be connected.

The quarantine PC should have a current patch level of virus protection programs and be recorded with current malware signatures. Therefore, the signatures of quarantine PCs must always be up to date.

In addition to a possibly automated review of the storage media by the quarantine PC, a manual check for the volume should always be performed.

** Use of mobile devices **

On service laptops, programming devices and similar devices, which are used especially in the field of OT, can not be waived in the rule. Therefore, special considerations are necessary here, so that the security of the OT infrastructure is not endangered by weak points in these clients or in their use.

Smartphones, tablets and other mobile devices that are not exclusively managed in the OT network should generally not be connected to the OT network. If this is desired, these must be adequately secured. To secure these devices, the relevant IT-Grundschutz modules should also be used.

** Use of notebooks for maintenance purposes **

In applications, notebooks are often used as mobile maintenance devices. In principle, it is important to define the work to be carried out before each mission and the employee must be able to do so due to his training and knowledge. When working on systems with high protection requirements (SIL, GMP etc.), additional measures must be taken to ensure that no unintentional changes are made.

Technical safety measures (eg protection of the configuration data of the field device by means of appropriate bridge) or alternatively organizational measures (four-eye principle) are to be applied.

** Internal devices **

Organizational measures must be taken to ensure that only maintenance-requiring software is installed on these maintenance devices. It should be done a system hardening. In addition, these devices should be patched regularly and checked for malware (malicious programs).

** External devices **

For the use of external maintenance devices, it is recommended to first conclude a corresponding contract with the external provider in which the information security-relevant topics (especially rules of conduct for the external employees) are contractually regulated.

Before using an external maintenance device, an inventory is required. To clarify in this context is:

* Which software is installed (including operating system and patches)
* Which interfaces are available and active (eg UMTS / GPRS / GSM)
* Which malware protection is installed (are current signatures available?)
Once this inventory has been completed and has not yielded any negative findings, the next step is to investigate malicious programs using anti-virus protection that complies with institutional requirements. If successfully completed, OT access can be granted.
In this context, the use of individual firewalls (USB-operated compact devices) has proven itself with different users. These are switched between the respective OT component and the maintenance device and are intended to prevent unwanted activities.

#### IND.1.M10 Monitoring, Logging and Detection [Area Safety Officer]

By early detection of security-relevant events can react to these promptly and thus a possible damage is limited. Therefore, a strategy should be developed in advance in a Security Incident Response Plan as to how security-relevant events are detected and identified, which reactions are required and how a safe state can be restored. The Security Incident Response Plan should take into account the phases of planning, reaction and recovery. For example, to classify the events, notify, document, investigate the event and the actions derived from it.

In particular, the responsibilities and roles as well as the further course of action (eg notification to authorities or publication) should be defined. Here also the data protection officer is to be involved.

The plan should be tested at regular intervals and at least once a year, checked for up-to-dateness and revised if necessary.

** ** logging

Logging is used for early detection of errors and security-related incidents such as unauthorized access attempts to data or identification of transmission bottlenecks.

The logging data should be stored on a central server. This allows logging data from distributed systems and components to be centrally collected, analyzed, and correlated.

In an OT, at least the following events should be logged and centrally collected, as far as they are available:

* local events, eg. The operating systems,

 
+ Restart of services,
+ System starts and reboots,
+ Successful and unsuccessful logins to the system (operating system and application software),
+ Failed authorization checks,


 
* Events from domain controllers, such as

 
+ Setup or changes of users, groups and permissions,


 
* Firewall / Router / Switch / Server events, especially

 
+ Blocked data streams (violations of ACLs or firewall rules),


 
* Anti-virus program events,
* other safety-relevant error messages (eg hardware defects, exceeding of capacity limits),
* IDS / IPS events.
In addition, the following data should be recorded for the aforementioned events:

* Date and time (It is to use a common time source for all systems see IND.1.M6 change management in the OT - time synchronization),
* Description of the event,
* Criticality,
* Source of the event, eg B. Application, operating system.
In addition, attention must be paid to the applicable data protection regulations.

** Monitoring and evaluation **

To ensure safe operation, a suitable infrastructure for operational monitoring of system operation should be designed, implemented and operated. The monitoring should include not only the operational availability and utilization monitoring of services, systems and networks but also the evaluation of security-relevant events.

This will usually not happen if the logs are spread across a variety of systems. Therefore, a central log server should be set up. This must be suitably embedded in the zone concept (see IND.1.M5 Development of a suitable zone concept). If necessary, multiple log servers are required to maintain the separation of the zones.
The incoming logs must be systematically evaluated so that the appropriate response can be triggered if necessary. In the case of a manageable number of systems, this can be done on a random basis, with at least one (role) responsibility and one frequency (depending on the protection requirement, eg weekly) to be determined. With a larger OT infrastructure, only an at least partially automated evaluation will allow the detection of critical events.

Based on events that occur and limits on monitored values, an alarm should be raised to inform the component's IT operations about the event.

The following list illustrates possible examples of such events and patterns:

* Conspicuous behavior that is typical of malicious programs (eg increased network traffic, decrease in performance, increasing application errors and integrity violations),
* Hardware defects such as bad sectors in data storage (eg hard disk) or failing components due to hardware errors,
* Loss of network connection,
* Unusual increase in CPU load and memory usage.
** Implementation of intrusion detection or intrusion prevention systems **

Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) can be used to detect attempts to attack at an early stage, so that IT operations can be alerted at an early stage (IDS) or an automated response to the attack is initiated (IPS) ,

To do this, IDS / IPS works on the basis of heuristics to distinguish attack attempts from common, desired behaviors and data. Accordingly, these heuristics must be updated regularly. When updating the heuristics, the instructions for updating virus signatures should be taken into account. In addition, the heuristics must be adapted to the OT and its individual circumstances. Typical incidents and events that can be detected by such a system are e.g. B. unauthorized access to systems and the unauthorized installation of software or manipulation of data. In addition, unintentional and accidental changes (eg in configuration files) can also be detected.

An IDS / IPS can monitor individual servers (host-based IDS / IPS, HIDS / HIPS) or monitor the traffic through sensors in the network (network-based IDS / IPS, NIDS / NIPS).

If a NIDS / NIPS is used, the sensors should be placed in the network for monitoring the data traffic, in particular for external interfaces (eg DMZ). External interfaces are usually more vulnerable to attacks (eg, the Internet). Likewise, a HIDS should be installed on all OT components. The log data of the HIDS should be integrated into a central logging.

IDS / IPS should be considered as an additional safeguard and do not replace system and network monitoring (eg through a Security Information Event Management (SIEM) system).

The use and operation of an IDS can only be recommended for larger institutions, as the set-up, maintenance and review of the notifications (especially in the initial phase) are not inconsiderable. In smaller plants the effort and the benefit must be checked in advance and alternative curing and protective measures may have to be implemented.

When implementing an IPS, it should also be borne in mind that planning also takes into account very specific situations, so that these legitimate transmissions are not prevented. Before activating these functions, therefore, a very thorough trial phase must be completed.
The effectiveness of an IDS / IPS strongly depends on a customized and individual configuration. For example, the effectiveness can be affected by a high number of recurring false positives. In particular, IPS should be used wisely. Priority here is the ongoing operation, which could be disturbed by a faulty intervention of the IPS.

Therefore, not only the initial configuration of the IDS / IPS requires a trained specialist staff, but also in operation at least one person must be able to distinguish a reported attempted attack from a False Positive in an emergency. This person should be constantly available so that appropriate countermeasures can be taken after classifying the notification.

#### IND.1.M11 Secure Procurement and System Development

** Development and Integration **

OT components are delivered as a combination of hardware and software. The adaptation to the individual circumstances and needs is realized by the configuration. In some cases it may be necessary to develop your own software (eg scripts, batch files for batch processing) to integrate certain automatisms or functions later. If own programs or also scripts are developed, then the secure creation (Secure Coding Guidelines) of the programs as well as the safe integration in the existing environment should be regulated by an internal software development guideline.

** Confidentiality agreement with manufacturers, suppliers and external operators **

The institution should establish confidentiality agreements with contractors (manufacturers, suppliers or external operators). These should, in particular, consider employees of the contracting party with relevant information and information security knowledge about the OT of the institution (eg in the event that employees of the contracting partner change position or company).

In addition, it should be regulated how the availability of the OT can be maintained if the contracting party no longer offers maintenance services or services (eg due to insolvency of the contracting party). For example, the institution should continue to have the necessary access to these systems and sufficient documentation to maintain and operate the OT.

In the case of a contractor's business, it should be contractually agreed that confidential information handed over be returned to the institution.

** Long-term information security guarantee **

The institution, system integrators and manufacturers should develop a strategy already at the planning stage how to ensure the long-term information security of the system. This applies to the entire duration of the investment. This also includes the continued use of discontinued software. Therefore, alternative protective measures should be considered early on.

**Compatibility**

The OT and its components to be procured should implement common standards of the respective technology and be compatible with other systems in accordance with these standards. To this end, these should support, if possible, established, commercially available information security mechanisms.

** Abandon superfluous product features **

If OT components have services or interfaces that are not required for operation, they should be removed if possible or at least deactivated. The changes made to the OT should be documented comprehensibly.

** Communication of information security requirements to the system integrator and manufacturer **

The information security requirements of the institution for the OT resulting from the risk analysis should be communicated to the manufacturer and system integrator implementing the equipment. This should be done as part of the specifications.
The requirements should be formulated on the basis of the specific applications. So they can relate to required properties or information. It should be described not solutions, but requirements. The degree of fulfillment of the requirements should be taken into account when choosing the solution and the integrator.

** Consideration of information security specifications of the manufacturer and system integrator **

The institution shall take into account the information security specification provided by the manufacturer and the system integrator in the risk analysis cycle. Building on the information provided by the manufacturer and system integrator, further measures can be defined by the institution.

** Robustness of the products **

In addition to the hardware (eg industrial computers), the software (eg protocol stack, OT applications) should also react robustly to invalid entries. For example, invalid network packets should not cause the software to crash or fail, but should be ignored by the protocol stack and logged as needed.

The robustness of the components should already be ensured by the manufacturers. This requirement should already be required when acquiring new components by the institution.

** Support for anti-virus solutions **

If necessary, the OT components to be procured should be equipped with a malware protection program or at least support the operation of malware programs. As a rule, the manufacturer supports selected products (see also IND.1.M3 protection against malicious programs).

** acceptance and integration tests **

As part of the acceptance and integration tests, the implementation of security requirements and interoperability should be examined and verified.

Special focus should be placed on the handling and effectiveness of backup and recovery measures.

#### IND.1.M12 Establish a Vulnerability Management

Errors in the software pose a problem. The resulting vulnerabilities could allow an attacker to gain access to the system or disrupt the software. Therefore, in principle, these errors should be corrected or their negative effects otherwise limited.

** ** vulnerabilities

As with all IT systems, OT components, systems, applications, and protocols contain vulnerabilities. As these fundamentally threaten security, a process for dealing with them is necessary.

There are several different cases: For one component (product, system, application)

* no vulnerabilities publicly known. This can change at any time.

 
+ In addition, vulnerabilities can only be known to certain parties who do not want to publish them for different reasons.1The exploitation of a vulnerability before the vulnerability was publicly disclosed is a so-called zero-day ("exploit").


 
* Vulnerabilities known and the manufacturer has

 
+ Patches provided. These were provided by the integrator / machine / plant builder for the OT


- Approved
- not released



+ no patches provided. The manufacturer plans:


- provide patches
- do not provide patches. In this case, the risk of continued operation must be considered and appropriate technical or organizational measures taken. Otherwise, such components (hardware and software) must be replaced.





 
** target of vulnerability - **

For all applicable cases, vulnerability management should be able to provide procedures. This should in principle be integrated into the other procedures for safe operation of the operating and control technology (see IND.1.M16 Change Management in OT).
The vulnerability management must identify gaps in the software, components, protocols and external interfaces of the environment and derive, evaluate and implement possible need for action and possibilities (eg patch management).

** ** Inventory Analysis

During the initial implementation of the vulnerability management, a weak point analysis of the initial situation must be carried out once to derive the need for action. On the basis of the existing infrastructure, the institution must identify all existing vulnerabilities of all installed components (products, applications, systems, protocols, external interfaces). This should be based on manufacturers' vulnerability advisories and publicly available CERTs. In addition, organizational and technical weak point analysis audits can be performed. This is especially recommended for higher protection requirements and for special exposure (eg interfaces to the Internet).

Importing security-relevant updates as part of a systematic patch management can be a way to close certain vulnerabilities. For this, a suitable procedure for the respective environment must be determined, whether, how and when patches can be applied.

** Evaluation of vulnerabilities **

In order to assess relevant weaknesses in a timely, systematic, technically appropriate and cost-effective manner and draw the right conclusions, it is necessary to establish a procedure for assessing vulnerabilities. It should be defined who (which role (s)) when (in which frequency) which information sources (news, advisories, e-mail distributors, databases, etc.) are subscribed to, viewed and evaluated. In smaller organizations, it is a good idea to bundle these tasks with the ICS Information Security Officer. In larger structures with many system and application types, a task sharing will be necessary. From the potential impact of a vulnerability (inferred from the need for protection) and the exposure (ease of exploitation), a criticality should be inferred, which sets the priority for further action. A standardized rating scale such as CVSS can be used. For smaller organizations, a two- or three-level qualitative scale is usually sufficient:

* uncritical (low impact or negligible exposure): Continue to observe.
* medium (maximum mean impact or exposure): treatment as part of the next regular software maintenance
* critical (critical impact or high exposure): priority unscheduled treatment (Information Security Officer decides what to do next)
A procedure for software maintenance should be attached to the evaluation process: Depending on the area (eg by zone), different specifications can be defined when, how often and how vulnerabilities are patched above a certain criticality or which alternative measures are in force must be so that can be dispensed with the patching. For each new type of vulnerability and evolution of attack techniques, it is important to assess whether the established replacement measures are still sufficient or need to be supplemented.

** ** patching

Where patching is possible, the risks of which are estimated and considered acceptable, a patch process with role-specific responsibilities should be defined which, in addition to the patches and updates released by the manufacturer, also considers additional third-party software (eg office applications, PDF readers). The process should contain at least the following elements:

* Regular check for new vulnerability reports from the manufacturers of OT components or third-party software
* Criticality assessment of patches, for example with Common Vulnerability Scoring System (CVSS),
Obtaining the patches and updates
* Testing (this should be done on a test environment (identical component)),
* Approval process,
* Handling manufacturer releases of patches and
* Dealing with the patching of additional software.
Sources of vulnerability reporting are manufacturers or CERTs.

CVSS is a methodology for assessing and classifying vulnerabilities depending on the individual risk of each operation. Among other things, the baseline score includes how the vulnerability can be exploited (eg locally or remotely) and what the consequences are (eg denial of service or code execution). A second value (temporal score) assesses changeable conditions over time. This includes z. For example, the availability of exploit code. A third component establishes the reference to the local environment of the user. He has to judge by his environment, which means a weak point for him. The first two pieces of information are made available on various Web sites for vulnerabilities (such as CVE MITER).

Installing patches and updates usually requires approval from the manufacturer of the OT component. Therefore, z. For example, patches and updates already available on the Internet can not be recorded by the institution, since a loss of functionality would be possible and the manufacturer would not assume any guarantee.

For this reason, the institution should contractually agree with the manufacturer to release and provide patches and updates or alternative workarounds for vulnerabilities, especially if such interference may affect the approval of a system. The time periods should be chosen as short as possible, because in this time window the affected system is exposed to an increased risk due to the vulnerability.

If possible, the institution can perform tests independently before installation. Alternatively, the updates should be installed and tested sequentially. Here, first redundant systems should be recorded. Before applying patches and updates, it is recommended to backup each system. This applies in particular to OT systems that are necessary for production. OT with no or little importance for production can also be patched without prior backup and extensive testing.

In addition, it should be checked whether a restart after the patch is performed or required. This must be taken into account in the planning.

Overall, the import of patches should be integrated into the operating cycles of the system. Maintenance windows on the system can be used to install patches. With redundantly designed components, a step-by-step procedure can be selected so that the time of installation is not delayed too long.

** Alternatives to patching **

If no patch is available, alternative measures should be considered and taken in a security consideration to prevent exploitation of the vulnerability. For example, solutions can be additional tools that prevent exploitation of vulnerabilities or prevent changes. As an alternative measure, it is possible, for example, to place the affected OT in a separate network segment and to filter the data traffic to this network segment by means of a firewall (see IND.1.M5 Development of a suitable zone concept).

** Handling End-Of-Support / End Of Life (EOS / EOL) **
If end-of-support is attained for OT components or software used in them, these components increase the operational risk. This applies in particular to software from the IT environment (eg operating systems). In these cases it is possible that weaknesses will continue to be discovered but will not be closed. In this case, additional protective measures may be necessary, eg. For example, migration to a new software or firmware version or hardware revision.

A safety assessment should be carried out for this purpose and based on this, appropriate information security measures should be identified, depending on the function of the OT and importance for production. For example, separating the OT with unpatched vulnerabilities into its own network segment and a restrictive firewall to filter traffic can protect the systems.

The long-term goal should be to replace the affected OT components with components supported by the manufacturer. Without support from the manufacturer, future errors and failures can severely affect production, as the development of solutions without the help of the manufacturer is more expensive.

In particular, it should be ensured when purchasing that no components are used that have already been discontinued by the manufacturer.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### IND.1.M13 Emergency Planning for OT (A)

** Emergency management **

Many organizations already have emergency management based on different requirements, which covers specific scenarios. In the area of ​​OT, these should be supplemented with contingency plans for at least the following scenarios:

* Complete failure of the Internet connection including remote maintenance for a longer period of time (> 1 week)
* Complete failure of Office IT for a certain period of time (eg 2 days)
* Temporary failure of critical IT components in the OT area for a period that is not traceable with standard operating processes
Compromise of critical IT components in the OT area by an unknown attacker or by malicious programs
If business continuity management (BCM) already exists, emergency management for the OT infrastructure can be integrated into it. Otherwise, a BCM should be set up, for example according to IT-Grundschutz (module DER.4 emergency management or BSI standard 100-4), which includes the OT infrastructure.

** System Backup and Recovery **

For the OT, a backup and recovery concept should be created. The basis for this can be the proven methods of Office IT (see module OPS.1.1.5 Data Backup). In addition, additional system or component-specific security procedures may be required for systems that can not be integrated into traditional security solutions.

The security infrastructure of the OT should be operated as independent as possible from the infrastructure of the Office IT solution. When using a common infrastructure, the risks arising from the dependencies should be considered and adequately taken into account. This applies in particular to the storage of system backups or project data on file servers of the office IT.

** Recovery Plan **
A recovery plan should specify how basic OT functions can be resumed after a significant failure. Actions should be derived in advance to ensure the restart of production in a reasonable time after a production or safety incident has occurred. These include, for example, backup processes, recovery and periodic backup testing, system recovery procedures, defective component repair and inventory of spare parts, as well as alternative communication and control capabilities for outages.

The plan should be reviewed at regular intervals and at least annually for topicality and revised if necessary.

Emergency plans and procedures must be compatible with applicable laws and other regulatory requirements. The emergency planning for the OT infrastructure can either be integrated into an existing emergency management or be established as an independent emergency management for the OT. In the latter case, OT emergency management can also be part of existing OT crisis management.

The organization must develop contingency plans for defining categories of failures and other crises. In the event of failure of all or part of the OT or critical communication links, pre-defined actions must be taken (eg, safely shut down the controlled process or maintain the last operational state prior to the event).

Restoring the OT infrastructure to a safe state means all system parameters (default parameters such as organization-specific) are set to safe values, safety-critical updates are (re) installed, security-related settings are restored, system documentation and operating instructions are available, and current, verified backups are restored and the whole system is fully tested and functional.

** Evaluation of the emergency management **

OT emergency management must be evaluated regularly (eg once a year). To do this, the organization should select a test procedure (eg full-scale simulation or table-top excercise) whose test depth and coverage is appropriate to the criticality of the OT infrastructure.

**Redundancy**

With regard to redundancy as an important measure of business continuity, the same applies in the OT area as it does for Office IT. The design and dimensioning of the redundancies always has to comply with the protection requirements and must cover all mission-critical elements of the OT environment, including power supply, supply lines, data cables, active network components, etc.

If there is a high demand for availability, an alternative control center (control room, control room, etc.) should be set up which is ready for action in the event of a failure of the main control center within a certain time frame to be defined by the organization with the help of the protection requirement (so-called emergency location). This emergency location should

* be geographically separated so that exposure to a natural disaster on both sites is unlikely
* reachable in case of emergency (even in case of regional outages of electricity and other services),
* Be covered by necessary service contracts with the appropriate priority and
* constantly configured to be operational within the set timeframe.
#### IND.1.M14 Strong Authentication to OT Components (CIA)

As far as possible, the use of all OT components should require authentication of the users and services, so that operation of the systems is only possible in the authenticated state. These include not only ordinary computers but also routers, switches and PLCs.
Different methods and features can be used for authentication. A distinction is made between the authentication features knowledge (eg password, PIN), ownership (eg token, smartcard, certificate) and physical features (eg fingerprint, iris recognition). The whereabouts of the person accessing can also indirectly be regarded as a feature if it is ensured that it could only reach this place by means of one or more further features. An example is a control room that can only be accessed by a key or by a (casual) facial inspection by colleagues.

** ** Mehrfaktorauthenti

With increased protection requirements, several features should be used for authentication and thus establish a higher level of information security (eg two-factor authentication using a token and password). Here, features from different classes (knowledge, possession, biometrics, location) should be combined.

When selecting the authentication methods, a security consideration must be carried out. This must be compared with other requirements (eg accident regulations) and organizational framework conditions (eg access restrictions) in order to arrive at a suitable selection.

** Central management of Authenti **

The management of these requirements should preferably be implemented via a central management solution (eg in a directory service). There should be no additional dependency on other zones. This can be achieved by operating the directory service within the zone for which it is needed. Information from a directory service in another zone can be replicated as needed.

Not all of the measures mentioned here are fully applicable to all OT components useful. For example, an attacker could block user access through provoked, failed login attempts. Thus, access to the affected system by the legitimate user would no longer be possible. Therefore, the gain in security due to the particular measure and possible restrictions on other requirements for the OT components (eg required, immediate access) must be weighed against each other. There should always be an emergency process that can maintain operation in the event of authentication failure. In this context, the technical user and service access required for automated operation should as far as possible not be dependent on a directory service.

#### IND.1.M15 Permission Checking and Monitoring (CIA)

Necessary The basis for this measure is that IND.1.M7 establishment of an authorization management has been implemented correctly. In the case of increased protection requirements, the requirements for authorization management are increased as follows. The goal is to make it easier and faster to prevent or at least identify abuse.

** Audit-proof maintenance of an inventory overview and history **

According to IND.1.M7 Establishment of an Authorization Management applies: Authorization Management must have a complete overview of the authorizations assigned to a person. This overview must also include the authorization history of a person as well as information about the respective authorization request and the test and release process carried out.
This therefore represents an assignment of users to (sets of) rights. In addition, however, the stock overview should conversely be able to provide information about which access rights apply to certain systems and applications, ie the assignment of application or system to users and rights. At least for all critical systems this should be present and up to date. Ideally, the effective authorizations are displayed here - that is, those actually set in the system technically instead of those derivable from the historical setting and deletion. This has the advantage that there is a chance to recognize illegitimate permissions added to the authorization process.

** Automated evaluation **

It makes sense to automate the compilation of the effective authorizations while carrying out an evaluation. Thus, changes (deltas) could be reported or deviations from a standard or target state can be specially represented.

** Logging of critical activities **

Critical permissions can be abused in different ways:

In the first case, the likelihood of reducing the likelihood of others improving at least the traceability and elucidation when logging critical administrative activities. This should be done centrally and needs a systematic evaluation (see IND.1.M10 Monitoring, Logging and Detection). In order to be effective in cases 1 and possibly also 4, the logs should not simply be deleted or manipulated by the same role whose action was logged. At a minimum, deletion or manipulation should be reported to another independent role. Even better is to prevent the deletion or manipulation technically and to automatically report attempts of erasure or manipulation to an independent role.

#### IND.1.M16 Greater Foreclosure of Zones (IA)

Interfaces to zones with high or very high protection requirements may require more isolation than is possible with Layer-4 firewall systems or the often limited scope for securing OT components. In particular for external interfaces of the OT and Office network, the interfaces should be subject to a security assessment.

The safety assessment should be carried out taking into account the design of the respective interface on the basis of elementary hazards. In this procedure, the relevant elementary hazards must first be determined and the respective interface must be examined for adequate protection. From this point of view, it may be necessary to discard interfaces or additionally protect them against the identified threats if the established security measures do not adequately cover the identified threats.

The protection measures required in each case result from the risk assessment and may also require adjustments to the communicating OT components such as hardening, antivirus protection, patch management or the awarding of minimum legal requirements. Due to the often limited possibilities of action there, such protective measures can also be implemented on an interface system. For this purpose, the construction of a DMZ can be considered.
The communication between the security areas considered (such as external access to the OT) is terminated in this DMZ by application layer gateways (ALG) such as proxy or data transfer server. Specific content checks on the gateway, such as checking for malicious programs or data format checks (eg XML checking through a web application firewall or protocol checks by industrial firewalls), can be performed on the gateway desired communication direction of the connection structure is observed. The ALGs can be specially hardened and enforce the safety requirements for the zone without the need for adjustments to the OT components. Such a DMZ infrastructure can be used depending on the environmental requirements per interface or for multiple interfaces.

#### IND.1.M17 Regular Security Check (I)

** revision **

OT infrastructures are often even less frequently audited than Office IT systems. In addition to a lack of security awareness, this is often due to the high availability requirements of such environments.

With this in mind, an appropriate environmental review process should be developed, including appropriate review procedures based on manual or automated policy compliance checks (configuration and policy reviews). Special attention should be given to exposed systems with external interfaces as well as to systems with direct user access, since these are exposed to an increased threat situation.

When planning, it should also be borne in mind that certain weak points can in principle only be detected economically through practical vulnerability tests (often referred to as penetration tests). By such a measure, in principle, the availability of the environment can be temporarily reduced.

Audits should always be carried out in consultation with the responsible administrators during the operating hours.

The tests require extensive skills and experience, which can be obtained externally if required. In larger institutions it may be worthwhile to build up your own competence. Depending on the need for protection, it is advisable to have an audit per system and year down to an audit before going live and for major changes in the environment. This may include, but is not limited to:

- Extensions of equipment (hardware and software)

- Establishment of new external connections

- replacement installations

- Substantial upgrade processes and system or software migrations

3 Further information
------------------------------

### 3.1 Worth knowing

Different national and international special standards and specifications exist for different sectors, which can be used in addition to this module in order to further sharpen and supplement the measures. Some are mentioned in the bibliography; for further references, see the ICS Security Compendium.

** definitions **

For a detailed description of typical OT infrastructures, see chapter 2.3 * Hierarchical structure of ICS * and chapter 2.5 * Communication processes * of the ICS Security Compendium. There, in particular, the levels (zones) 1-5 (see IND.1.M5 development of a suitable zone concept) are shown in more detail.

* OT (Operational Technology): Operational Technology (OT) is hardware and software that detects and effects change through the direct monitoring and / or control of physical devices, processes, and events within the enterprise [GART1].
* ICS (Industrial Control System): ICS is a generic term for automation solutions for the control of technical processes in the industrial environment and part of the OT.
* PLC (programmable logic controller), PLC (programmable logic controller), PNK (process-related component); MTU (Main Terminal Unit), Controller: These terms designate an automation component with processing capability, depending on the industry. These are used for control or regulation in a machine or plant and programmed on a digital basis.
* Sensor transducer, limit switch, button / switch, initiator, limit switch: These are components for the acquisition of physical quantities and their conversion into a standard signal. Interfaces include analog standard interfaces such as 4 ... 20 mA current interface, 0-10V, 24V DC voltage, etc. but also digital communication protocols such as fieldbuses (eg PROFIBUS PA) or digital point-to-point connections (eg. B. IO-Link) are used
* Actuator, actuator: An actuator converts a control variable (eg electrical, hydraulic or pneumatic signal) into the manipulated variable for influencing the process. With regard to the connection, the same techniques are used as with sensors.
* HMI (Human Machine Interface); BUB (control and monitoring components), ABK (display and control component): These components serve to realize display and operating functions. Typical applications are z. This includes, for example, the representation and operation of the process via process flow diagrams, standard operating images (faceplates), trend images, sequence language images, group images. In addition, there are functions for alarm management, data archiving and evaluation as well as system diagnostics and documentation.
* Programming and testing device, service computer, engineering workstation: These components enable the configuration and commissioning of automation components.
* DCS (Digital Control System), PLS (Process Control System): DCS are mostly used for larger process plants. You can have a variety of features, such as alarm systems, plant visualization (waveform logging of measurements), user management, centralized data storage, and maintenance and development tools.
IS-Management (Information Security Management): The planning, control, and control task required to build and continuously implement a well-thought-out and effective process to produce information security is referred to as information security management. It is a continuous process whose strategies and concepts need to be constantly reviewed for performance and effectiveness, and updated as needed. The goal of IS management is not only to protect the information, but also the systems themselves. Cyber ​​security is synonymous in the sense of the document.
** Basic characteristics of the OT **

The OT covers all the technology involved in production processes and interaction with the physical world. Part of it is ICS. These are used wherever technical processes are automated. They are used for measuring, controlling, regulating and operating industrial processes. Examples include process and process technology, factory automation, supply and disposal networks (eg electricity, water, sewage, gas, district heating), operating technology (eg rail and road transport) and building automation. The OT also includes laboratory and analytical equipment.

The individual requirements are determined directly by the operational requirements of the production processes.

** Guaranteed response times **
Control circuits ensure defined reaction times with regard to their time behavior. If changes to the time behavior of the OT occur due to (temporary) modifications in the software, this can lead to disruptions in the production process and, for example, result in an increased reject rate.

** Legal requirements / restrictions **

There are many applications in which the operation of the equipment is subject to regulatory requirements (eg CE certification of equipment, safety guidelines, guidelines for the production of pharmaceutical products). In these cases, significant changes, including software changes to the OT components used, may require a dedicated approval process. Due to the prescribed test process, for example, the possibilities for timely import of security updates are limited or not given here.

**Software**

For OT components, a distinction must be made between firmware, application software and parameterization.

The firmware is updated by the manufacturers only when malfunctions occur; Changes to the user programs only occur if the systems are changed or extended; Parameterization takes place during normal operation.

** Changes and Updates **

Changing system configurations or applying updates often causes major problems, unlike Office IT. Before the action, possible effects on timing or other effects on the systems should be considered. During execution, availability may be restricted (eg due to a necessary restart). After the completion of the measure, a decrease (eg with regard to safety aspects) must be renewed. As a result, changes and updates are generally only introduced as part of planned plant shutdowns.

**Hardware**

In contrast to office IT, the OT runs for longer periods with the same hardware (device types). As a result, current software, firmware, or protocols may not be supported.

** ** standards

In the area of ​​OT, there are a large number of standards, standards and guidelines which contain stringent requirements (eg IEC 61508-3 in the area of ​​software development). Further sources are provided by the ICS Security Compendium in Chapter 4 Organizations, Associations and Their Standards.

### 3.2 Literature

Further information on hazards and safety measures in the area of ​​"control technology" can be found in the following publications, among others:

* #### [27019] ISO / IEC TR 27019: 2013

  

 Information technology- Security techniques- Information security management guidelines based on ISO / IEC 27002 for process control systems specific to the energy utility industry, International Organization for Standardization, 07.2013
 <Https://www.iso.org/standard/43759.html>

 
* #### [AHWAST] How to Use the White Paper - Requirements for Secure Control and Telecommunication Systems (Version 1.1, 2014)

  

 BDEW Federal Association of Energy and Water Management e.V. and Austria's e-Economy, Version 1.1, 2014
 [Https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge](https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge?open&ccm)

 
* #### [CSE] Recommendations for training and qualification measures in the ICS environment

  

 BSI publications on cyber security (BSI-CS 123), Federal Office for Information Security, 11.2015
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_123.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_123.pdf)

 
* #### [GART1] Gartner IT Glossary, Operational Technology (OT)

  

 <Http://www.gartner.com/it-glossary/operational-technology-ot/>

 
* #### [ICSSK] ICS Security Compendium

  

 Federal Office for Information Security (BSI), 2016
[https://www.bsi.bund.de/DE/Themen/Industrie\_KRITIS/Empfehlungen/ICS/empfehlungen\_node.html](https://www.bsi.bund.de/DE/Themen/Industrie_KRITIS/ recommendations / ICS / empfehlungen_node.html)

 
* #### [ICSSKfH] ICS Security Compendium for Manufacturers and Integrators

  

 Federal Office for Information Security (BSI), 2014
 <Https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ICS/ICS-Security-Kompendium-Hersteller.html>

 
* #### [IEC62443] IEC 62443-2-1: 2010 Industrial communication networks - Network and system security - Part 2-1:

  

 Establishing an industrial automation and control system security program, International Electrotechnical Commission (IEC), 2010
 <Https://webstore.iec.ch/publication/7030>

 
* #### [NIST80082] NIST Special Publication 800-82, Revision 2

  

 Guide to Industrial Control Systems (ICS) Security, National Institute of Standards and Technology (NIST), 2015
 [Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r2.pdf](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-81-2. pdf)

 
* #### [VDI2182.1] Guideline VDI / VDE 22182

  

 Page 1.

 
* #### [VDI2182.2.3] Guideline VDI / VDE 2182

 Page 2.

 
* #### [VDI2182.3.3] Guideline VDI / VDE 2182

 Sheet 3.

 
* #### [WAST] Whitepaper Requirements for secure control and telecommunication systems

  

 BDEW Federal Association of the Energy and Water Industry e.V, Version 1.1, 01.2015
 [Https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge](https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge?open&ccm)
