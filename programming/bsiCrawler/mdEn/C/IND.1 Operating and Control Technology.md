1 description
--------------

### 1.1 Introduction

Operational Technology (OT) is hardware and software that detects and effects change through the direct monitoring and / or control of physical devices, processes and events in the enterprise [GART1].

The industry, which includes Critical Infrastructures, includes industrial control systems (ICS) and automation solutions, which are responsible for all kinds of control functions. Further examples are laboratory equipment (eg automated microscope or analysis tools), logistics systems (barcode scanners with small computers) or building management systems.

The customary physical separation of OT from other IT systems and networks in office applications is nowadays only applicable in exceptional cases with increased protection requirements due to increasing integration requirements. Multi-level production steps and their overall control as well as regulatory requirements require an increasing opening across organizational boundaries. This trend is accelerated by the trend towards optimizing manufacturing processes to increase competitiveness in the context of Industry 4.0.

As IT components and technologies from office IT are increasingly being used in OT in addition to OT-specific components, they are now exposed to comparable hazards. At the same time, OTs differ significantly from traditional IT, making it difficult to apply established security procedures. For example, there may be restrictions based on manufacturer specifications or legal requirements that prevent or hinder changes to components. An example of this is the application of security updates or subsequent hardening measures. The OT is usually also subject to significantly longer lifecycles, even beyond the manufacturer support, so that the availability of security updates can not be consistently guaranteed.

Another major difference for OT is the high availability and integrity requirements, whereas confidentiality is often of secondary importance compared to office IT. Disturbances of these systems can cause risks to life, limb and environment and can usually not be remedied by restarting.

### 1.2 Objective

The goal of the module is to demonstrate suitable requirements for the information security of the OT. He addresses cross-component, conceptual and architectural security requirements.

The module is to be modeled and implemented across the board. In this case, multiple use in different areas of OT in an institution (operator within the meaning of VDI 2182) can not be ruled out since there are different requirements with regard to information security.

### 1.3 Delimitation

Depending on the purpose, industry, IT systems and technology used, as well as the long service life (sometimes without updates), the configuration of the OT can vary greatly, even with comparable applications. When designing the security measures based on the requirements of this module, the existing special features must therefore be taken into account. These can have a significant influence on the design of the security concept. For this reason, the risk analysis can already be of great importance when creating a security concept for the normal protection requirement. This may require multiple use of the device for different areas.

In addition, the surrounding infrastructure of the OT - ie locations, facilities, buildings, rooms, etc. - must be modeled by building blocks that are as specific as possible in order to complement the protective effect of this building block.

2 risk situation
-----------------
The following specific threats and vulnerabilities are of particular importance in the field of control technology:

### 2 1 Inappropriate integration of OT into the security organization

Different framework conditions, knowledge and procedures in the areas of office IT and ICS can lead to implementation problems with overarching security requirements. On the one hand, IT security requirements can not be implemented due to technical or process-specific features of ICS systems. On the other hand, ICS-specific information security and safety aspects (aspects of functional security) may not be known to the information security officer of Office IT. This can lead to friction losses in communication and implementation as well as to insufficiently treated or unrecognized risks.

### 2 2 Inappropriate integration of OT into operational processes

Despite the increasing convergence of OT and IT, there are peculiarities that make it difficult to transfer established business operations. Operational interventions in the context of change and (security) incident management for secure configuration, troubleshooting or the implementation of security updates, for example, can lead to a renewed official release or the loss of manufacturer's support. Unauthorized changes can affect the function of a component and potentially have an impact on its safety functions.

The OT is used to monitor, control and automate technical processes. Disruptions to these systems can lead to production losses, technical or personal damage and environmental damage. These potential effects must be taken into account during operational interventions.

### 2 3 Inadequate access protection

Industrial control systems are increasingly rarely operated completely independently from the outside world. Modern manufacturing and manufacturing processes require an information exchange with upstream and downstream production steps and are often linked to central production planning and control systems (Manifacturing Execution System / Enterprise Resource Planning) of an institution. The electronic exchange of information requires networking of production facilities with third party networks such as office IT or the networks of partners and service providers. Requirements for interactive access from office or mobile workstations as well as operational requirements for the electronic data exchange, such as the provision of software and updates, or for the realization of remote access for a call or service providers promote networking with the outside world.

If the necessary communication channels are too broad or insufficiently secured, attackers can use these access routes for network-based access and for compromising the automation system.

### 2 4 Insufficient protection against malicious programs for OT

Industrial control equipment can be affected by both targeted malicious software attacks and by chance malicious programs aimed at compromising office IT. Possible infection routes result from data transfers, the use of removable media and mobile devices, or the lack of segmentation or control of data traffic.

On the other hand, the use of anti-virus software can also pose risks to OT if there is no manufacturer release for the environment or if fault detection and active system interventions endanger the operation. A similar disruption potential (due to the disruption of connections) can also result from the operation of network-based Intrusion Prevention Systems (IPS).
In addition, the use of anti-virus software requires regular updates. If this is not guaranteed, new attacks by malicious software can not be detected. This also applies generally to attacks for which the antivirus software has no signatures.

### 2 5 Unsafe projecting process / application development process

Adaptations and advancements of IT systems, applications and control programs represent a critical intervention in the control system. Malfunctions can arise from functional errors in the case of inadequate test and validation steps, faulty or manipulated configuration data or weak points in the software, if important safety functions such as on- and off-hook Issuance or authorization checks are implemented inadequately.

Further dangers may arise from unsafe development environments, improper storage of program code, documentation or project data, as well as from the data transfer interfaces.

### 2 6 Insecure administration concept and remote administration

The management of industrial control systems takes place in certain cases remotely via network access. Here are different public and private networks such. As telephone networks, wireless networks, mobile networks and increasingly the Internet. If these accesses are inadequately planned, configured insecure or are not monitored, attackers may be able to access individual OT components or the infrastructure unauthorized and thus circumvent the security mechanisms at the perimeter.

Local administrators also have privileged rights that make abusive intrusion or compromised accounts attractive to attackers.

### 2 7 Insufficient monitoring and detection procedures

The monitoring of operating states of the process to be automated is an essential function of industrial control systems. For example, warnings that are relevant to the process (eg if levels are exceeded) and technical parameters (eg temperatures, valve positions) are displayed. In contrast, there is often a lack of adequate monitoring of the supporting IT infrastructure.

If unusual or security-relevant events of such operating environments are not or only insufficiently monitored, attempts to attack, network bottlenecks or foreseeable failures can not be detected early.

In addition, a poor evaluation or confusing presentation of events can lead to warnings and errors being detected late.

### 2 8 Inadequate test concept

Industrial control systems are often subject to high availability requirements. Malfunctions or technical failures may result in serious damage and high follow-up costs. For this reason, systems are often designed to be fail-safe and redundant.

If changes to such an environment are not carefully planned, tuned, and tested in a realistic environment, there is a risk that logical or software engineering failures will be overlooked and system malfunctions will occur. Even updates released by the manufacturer can cause disruptions when modifying or adjusting parameters on the system.

### 2 9 Lack of life cycle concepts

In addition to specific OT components, components, technologies and software from office IT, so-called commercial-off-the-shelf (COTS) products, are increasingly being used. Due to the very long lifecycles in OT, these components are generally operated much longer than usual in office IT, sometimes even beyond the manufacturer support cycles.
As a result, after the manufacturer support expires, updates for vulnerabilities will no longer be available. In contrast, there are often publicly documented vulnerabilities, as well as tools that exploit these vulnerabilities. This also allows unexperienced attackers to successfully penetrate the systems. This also applies if updates are not recorded or only with great delay.

The long operating times can also lead to problems in the procurement of spare parts, if they are no longer produced by the manufacturer. This also applies to possible know-how for the care and maintenance of legacy systems that no longer exists with new employees

### 2 10 Use of unsafe protocols

The OT components communicate with each other via various network protocols and technologies. In addition to protocols and technologies from office IT (eg Ethernet, TCP / IP, WLAN, GSM), ICS-specific protocols are used. These have not always been developed from the point of view of information security and accordingly provide, in part, no or only limited security mechanisms. Information is often transmitted in plain text and without integrity assurance or authentication.

An attacker with access to the network could read or modify the contents of the communication and thus influence the processes, for example by feigning sensor data or falsifying control commands. This applies in particular to protocols used for communication over freely accessible areas, such as radio protocols or in the context of site networking (telecontrol).

### 2 11 Unsafe configurations

In the default configuration of OT components, security measures are not always enabled, which makes it much easier for unauthorized access. Operating insecurely configured components can also threaten the security of other components of the environment, such as when credentials can be retrieved or in trust with other systems.

Examples of insecure configurations include the use of standard passwords, the use of system administration plaintext protocols, the operation of unneeded services, unsecured interfaces, such as: USB or Firewire ports, or disabled security features.

### 2 12 Dependencies of the TDC of IT networks

The OT is now operated less and less self-sufficient. If there are dependencies on other systems, networks or services, failures or security incidents in the IT network also affect the OT.

In particular, if these systems and networks are not under the control of the institution (the operator of the ICS infrastructure), this can severely affect the availability of OTs and processes. In addition, the incident or error can usually only be remedied with external support.

Examples of dependencies on other systems and networks include Internet connectivity (both wired and wireless), shared infrastructure components, operations management and monitoring by service providers, or the use of cloud services.

3 requirements
---------------
The following are specific requirements for the area of ​​operating and control technology. Basically, ICS Information Security Officer (ICS-ISB) is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### IND.1.A1 Integration into the security organization

An Information Security Management System (ISMS) for Operating the OT Infrastructure MUST exist either as an independent ISMS or as part of an overall ISMS, and MUST explicitly specify within its scope the definition of goals and values, processes, roles, responsibilities, and specifications for the OT include.

The management level of the institution MUST initiate, control and control the security process. The institution MUST establish a security organization that governs the roles and responsibilities for the information security of the OT infrastructure and components.

There is a need to appoint an overall information security officer in OT and to announce it within the institution. Legal, regulatory and other specific requirements for the OT sector and the sector or sector MUST be known and their impact on the institution evaluated.

There MUST exist a process of writing, communicating, implementing, updating, evaluating and improving concrete guidelines for specific topics in the process area.

Further information is described in the ISMS Security Management module.

#### IND.1.A2 Awareness and training of staff

Operating staff MUST be regularly informed and sensitized to relevant IT security threats in the field of OT. OT managers MUST be regularly informed or trained about the threat situation and need for action.

Additional information is described in the ORP.3 Sensitization and Training module.

#### IND.1.A3 Protection against malicious programs

In order to prevent risks from malicious programs, a concept for the protection against malicious programs MUST be created and implemented. It must consider the threatened IT systems as well as the possible infection pathways (external interfaces, removable media, service and parameterization / programming devices) and determine appropriate technical and organizational protective measures.

When using anti-virus software on OT components, it must be considered whether and in what configuration the operation of anti-virus software is supported by the manufacturer. If this is not the case, the need for alternative protection procedures MUST be considered in a risk analysis.

Used virus protection software MUST be supplied with current signatures. The antivirus concept MUST set the update strategy. This includes the reference to signatures, their distribution methods and the frequency of updating. The reference and distribution of signatures can be automated. The receipt of virus signatures by OT systems MUST NOT take place directly from the Internet, but must be done indirectly via a proxy or virus signature distribution service. The interface systems MUST be operated separately from the OT environment in a standalone zone (eg, DMZ).

### 3.2 Standard requirements
Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​operating and control technology. They SHOULD be implemented in principle.

#### IND.1.A4 Documentation of the OT infrastructure

The safety-relevant parameters of the OT infrastructure SHOULD be documented. All software and system components SHOULD be kept in an inventory. From this, the product and protocol versions used as well as the responsibilities should emerge. The components used SHOULD include any manufacturer restrictions or regulatory requirements such as certifications. This documentation and a system inventory SHOULD be kept in a control system, for example.

In addition, a current network SHOULD document zones, zone transitions, established communication protocols and procedures, and external interfaces. The interfaces SHOULD consider active network components as well as manual data transfer methods (eg using removable data carriers). The documentation SHOULD capture redundancies, IP addresses or ranges, and the assignment to physical security zones.

Since the documentation contains confidential information, all documents must be stored securely and given a classification regarding protection requirements.

#### IND.1.A5 Development of a suitable zone concept [IT operation]

There SHOULD be a zone concept that defines different levels with different protection requirements and includes the complete OT infrastructure and at least the transition to Office IT. The network SHOULD be segmented according to the zones and the flow of data between the zones should be properly controlled to make attacks more complex, unlikely and easier to detect.

It should also be a horizontal segmentation in independent functional areas (such as plants) done. The individual zones SHOULD be independent of each other as much as possible during operation. In particular, the zones in which the technical process is controlled SHOULD continue to be operable for a predetermined period of time in the event of failure of the other zones or their intentional decoupling following compromise. This period SHOULD be defined and documented as part of the risk analysis or alternatively in the context of emergency planning. The network SHOULD therefore be designed stably in the sense of manipulation- and error-resistant.

All interfaces / connections between the zones SHOULD be risk assessed. The outside interfaces SHOULD use authenticated users and integrity-protected protocols.

#### IND.1.A6 Change management in OT operation

For changes to the OT, a change process (change management) SHOULD be defined, documented and lived. The change process SHOULD ensure that changes are planned, documented, adequately tested for undesirable side effects and functionality, objectively evaluated and approved for safety or operational impact.

There SHOULD be a concept for the safe testing of changes. The system time of the OT infrastructure SHOULD be kept synchronous. This SHOULD be done with an external reference.

Further information is described in the module OPS.1.2.1 Change Management.

#### IND.1.A7 Establish Permission Management

The institution SHOULD establish a process for managing user access and associated permissions to access the OT. Permission management SHOULD include the process, execution, and documentation for requesting, establishing, and revoking privileges.
The authorization management SHOULD ensure that authorizations are granted according to the minimum principle and regularly checked. Permission management SHOULD regulate access to IT systems for employees, administrators and third parties. Each participant SHOULD regularly be trained on the regulations to be observed. Compliance SHOULD be reviewed and sanctioned misconduct.

Further information is described in the module ORP.4 Identity and Authorization Management.

#### IND.1.A8 Secure Administration [IT Operations]

For initial configuration, administration and remote maintenance in OT, either secure protocols or separate administration networks with the corresponding protection requirements SHOULD be used. Access to these interfaces SHOULD be restricted to the authorized persons. It SHOULD only be granted access to the systems and functions required for the respective administration task.

The systems and communication channels used for administration or remote maintenance should have the same level of protection as the managed OT components. All remote maintenance and monitoring SHOULD be authorized, monitored and controlled by the institution. For this, the remote maintenance access SHOULD only be activated for use and then deactivated again. This SHOULD be documented

It should be ensured that it is not possible to build up unwanted tunnels to bypass security measures. In the case of higher protection requirements, a four-eye principle SHOULD also apply to critical administrative steps.

#### IND.1.A9 Restrictive use of removable media and mobile devices

For the use of removable media and mobile devices SHOULD regulations for handling be set up and publicized. Basically, the use of removable media and mobile devices in ICS environments SHOULD be limited. For media and devices of service providers SHOULD an approval process and a request list exist. The specifications SHOULD be known to each service provider and confirmed by them in writing.

On the OT components, all unnecessary interfaces SHOULD be disabled. At the active interfaces, the use of certain devices or media can be restricted.

Further information is described in the block SYS.3.4 Mobile data carrier.

#### IND.1.A10 Monitoring, Logging and Detection [Area Safety Officer]

To limit the potential impact of security incidents, business and security-related events SHOULD be identified promptly. For this, a suitable log and event management SHOULD be developed and implemented. Log and event management SHOULD include appropriate measures for the collection and detection of security-related events and a response plan (security incident response).

The response plan SHOULD set procedures for incident handling. It should cover the classification of events, reporting channels and the definition of the organizational units to be included, damage limitation reaction plans, analysis and restoration of systems and services, and the documentation and follow-up of incidents. The reaction plan SHOULD be tested regularly and checked for up-to-dateness.

#### IND.1.A11 Secure Procurement and System Development

For procurements, planning or developments of ICS, information security regulations SHOULD be made and documented. The documents SHOULD be part of the invitation to tender.
In procurement, planning or development, information security SHOULD be considered throughout the lifecycle. Requirements and implementation instructions for safe operation of OT components from manufacturers or integrators SHOULD be planned and implemented early. Compliance and implementation SHOULD be documented

The institution SHOULD document how the system fits in with the concepts of zoning, entitlement, vulnerability management, and antivirus protection, and adjust it if necessary. It should be regulated how the operation can be maintained if one of the partners stops providing services.

Further information is described in the module OPS.2.1 Outsourcing Usage.

#### IND.1.A12 Establish Vulnerability Management

For the secure operation of an ICS environment, the institution SHOULD establish a vulnerability management. Vulnerability Management SHOULD identify gaps in the software, components, protocols, and external interfaces of the environment, and identify, evaluate, and implement potential action requirements and capabilities (such as patch management).

The basis for this should be manufacturer vulnerability advisories or publicly available CERT reports. In addition, organizational and technical weak point analysis audits can be performed.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### IND.1.A13 Emergency Planning for OT (A)

With high availability, contingency plans for the failure and compromise of each zone SHOULD be defined, documented, tested after each major change, and regularly practiced (see also BSI Standard 100-4).

In addition, an effective replacement procedure for the failure of the (remote) administration option SHOULD be defined, documented and tested.

#### IND.1.A14 Strong Authentication to OT Components (CIA)

For secure authentication of privileged users in control systems, a central directory service SHOULD be set up. The authentication SHOULD be additionally secured by the use of several factors (knowledge, possession, biometrics).

When planning, it should be ensured that any resulting dependencies in the user authentication are known and taken into account during the implementation of the solution.

The central directory service SHOULD NOT serve to authenticate operational technical accounts. When using a directory service, local system and application identifiers for emergency situations SHOULD be set up and securely stored.

Authentication systems that manage sensitive authentication data SHOULD be adequately secured against unauthorized access, changes must be documented in a comprehensible manner and monitored for abnormalities.

#### IND.1.A15 Permission Checking and Monitoring (CIA)

To enable effective verification of privileges, the institution SHOULD maintain an inventory that includes all assigned access, access and access rights to critical systems. The directory SHOULD answer on the one hand, which rights a certain user has effectively, and on the other hand, who has rights on a certain system.

All critical administrative activities SHOULD be logged. The IT operation SHOULD NOT be able to erase or manipulate the logs.

#### IND.1.A16 Greater foreclosure of zones (IA)
For ICS environments that are highly vulnerable or difficult to protect at the system and network level, preventative use of interface systems with safety testing functions is required to prevent risks from external connections.

As required in IND.1.A5 development of a suitable zone concept, all external interfaces of the environment should be risk assessed. From the risks identified, specific individual security measures SHOULD be derived.

By implementing one or more connection zones (DMZs) in a PAP structure (firewall-encapsulated Application Layer Gateways), end-to-end external connections can be terminated and required security checks (virus protection, formatting of data, checking and filtering of content, media breaks) can be carried out without any adjustments the ICS system are necessary.

The implementation of this requirement increases perimeter security. Supplementary organizational and technical measures SHOULD be identified and implemented to further reduce the risks of intentional and accidental circumvention of the perimeter, such as the use of removable media or mobile devices.

#### IND.1.A17 Regular Security Check (I)

The safety configuration of OT components SHOULD be checked in an appropriate cycle and / or as needed for sudden, new and unknown hazards. The security check SHOULD include at least the exposed systems with outside interfaces or user interaction.

The realized security concept SHOULD be checked regularly.

The security check SHOULD be done as a configuration check or through automated conformance checks.

4 Further Information
------------------------------

### 4.1 Literature

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

 
* #### [ICSSK] ICS Security Compendium

  

 Federal Office for Information Security (BSI), 2016
 [https://www.bsi.bund.de/DE/Themen/Industrie\_KRITIS/Empfehlungen/ICS/empfehlungen\_node.html](https://www.bsi.bund.de/DE/Themen/Industrie_KRITIS/ recommendations / ICS / empfehlungen_node.html)

 
* #### [ICSSKfH] ICS Security Compendium for Manufacturers and Integrators

  

 Federal Office for Information Security (BSI), 2014
 <Https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ICS/ICS-Security-Kompendium-Hersteller.html>

 
* #### [IEC62443] IEC 62443-2-1: 2010 Industrial communication networks - Network and system security - Part 2-1:

  

 Establishing an industrial automation and control system security program, International Electrotechnical Commission (IEC), 2010
 <Https://webstore.iec.ch/publication/7030>
* #### [WAST] Whitepaper Requirements for secure control and telecommunication systems

  

 BDEW Federal Association of the Energy and Water Industry e.V, Version 1.1, 01.2015
 [Https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge](https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge?open&ccm)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the block "Operating and Control Technology".

* G 0.5 natural disasters
* G 0.6 disasters in the environment
* G 0.9 Failure or malfunction of communication networks
* G 0.11 Failure or disruption of service providers
* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.23 Unauthorized intrusion into IT systems
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.36 Identity theft
* G 0.37 denying actions
* G 0.39 Malware
* G 0.41 Sabotage
* G 0.42 Social engineering
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
