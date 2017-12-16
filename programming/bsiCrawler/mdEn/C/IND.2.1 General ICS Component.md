1 description
--------------

### 1.1 Introduction

An ICS component is an electronic component that controls or regulates a machine or plant. It is thus part of an industrial control system (English: Industrial Control System, ICS) or more generally an operational technology (English: Operational Technology, OT). Such components may be Programmable Logic Controllers (PLCs), sensors, actuators, a machine, or other parts of an ICS.

Due to the high availability requirements typical in the OT environment and the often extreme environmental conditions (climate, dust, vibration, corrosion), ICS components have always been designed as robust devices with high reliability and a long service life.

ICS components are usually configured or programmed using special software from the respective manufacturer. This is done either via so-called programming devices (eg as an application under Windows or Linux) or via an engineering station which loads the application programs into the programmable logic controllers.

The role of the Information Security Officer in the field of industrial automation varies according to the nature and direction of the institution. Another name besides ICS Information Security Officer (ICS-ISB) is also Industrial Security Officer.

### 1.2 Objective

The goal of the device is to protect all types of ICS components, regardless of manufacturer, type, purpose and location. It can be used for a single device or a multi-component modular device.

### 1.3 Delimitation

The requirements are developed for a generic component. For more specific ICS components, additional building blocks are available under IND.2 * ICS Components * that describe requirements that go beyond the generic requirements of this building block and may need to be implemented.

The module contains no organizational requirements for securing an ICS component. For this, the requirements of the block IND.1 * Operating and Control Technology * must be implemented.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the General ICS Component area:

### 2 1 Damage caused by harmful environmental influences

ICS components in industrial environments are often exposed to special conditions that may affect safe operation. Examples include extreme heat, cold, moisture, dust, vibration or corrosive or corrosive atmospheres. Frequently, several factors occur simultaneously. Such adverse environmental conditions can cause ICS components to wear faster and fail earlier.

### 2 2 Incomplete documentation

ICS components are often incompletely documented, so not all product features are known. Information about the services used, protocols and communication ports as well as authorization management are often particularly incomplete. This makes the hazard analysis more difficult because interfaces, functions and security-relevant mechanisms are overlooked. As a result, potential hazards can not be taken into account. In addition, there are no or limited responses to new vulnerabilities in an ICS component if the services and ports used are not fully captured.

### 2 3 Unsafe system configuration

The standard configuration of ICS components is often designed to allow the components to function properly and be easy to commission. Security mechanisms often do not play a sufficient role. By default, all services, protocols, and ports are often turned on and remain active even when they are not in use. Likewise, default permissions often remain unchanged.
It is easy for attackers to take over and manipulate such components. It is also possible for an attacker to exploit the insecure system configuration to use the ICS component as a starting point for further attacks. As a result, business-critical information can flow away or the entire operation of the institution can be affected.

### 2 4 Insufficient user and authorization management

Some ICS components have their own user and authorization management. If this is poorly designed, it can happen that employees share user accounts or that the permissions of departed employees or service providers are not deleted. Overall, unauthorized persons can access ICS components.

### 2 5 Insufficient logging

For ICS components, logging is often limited to process-related events. Information relevant to information security is often not recorded. As a result, security incidents are difficult to detect and can not be reconstructed afterwards.

### 2 6 Manipulation and sabotage of an ICS component

The multiple interfaces of ICS components lead to an increased risk of manipulation of systems, software and transmitted information. Depending on the motivation and knowledge of the perpetrator, this can have a local impact across locations. In addition, status and alarm messages or other measured values ​​can be suppressed or changed.

Manipulated readings can lead to incorrect decisions of ICS components or operating personnel. Manipulated systems can be used to attack other systems or sites or to cover up ongoing manipulation.

### 2 7 Use of unsafe protocols

Some of the protocols used in the field of industrial control systems offer no or only limited security mechanisms. Technical information such as measurement and control values ​​are often transmitted in plain text and without integrity assurance or authentication. An attacker with access to the transmission medium can then read out and modify the contents of the communication or introduce control commands, thereby provoking actions or directly influencing the operation. A protocol-level attack is possible even if the ICS component is otherwise securely configured and does not itself have vulnerabilities.

### 2 8 denial-of-service (DoS) attacks

An attacker could interfere with the operation of ICS components by DoS attacks. For processes running under real-time conditions, even a shorter disruption can lead to loss of information or control.

### 2 9 malware

The threat posed by malicious programs is also becoming increasingly severe in industrial control systems. Infection opportunities arise through interfaces to the outside world and office IT (vertical integration) but also through mobile devices such as service notebooks or removable storage devices in the programming and maintenance of ICS components. By the latter malicious programs can also be introduced into isolated environments (overcoming the "air gap").

### 2 10 Spying on information

ICS components often contain detailed information about the controlled or monitored process or process. Also from other transmitted values, such as measurement or control data, this information can be partially reconstructed. The same applies to control programs or parameters.

Attackers could get business secrets here (industrial espionage), eg. Recipes, procedures or other intellectual property. They can also gain information about the functioning of an ICS component and its security mechanisms, which can be used for further attacks.

### 2 11 Insufficient security requirements for procurement
Due to a lack of awareness of the risks and cost reasons, procurement often does not take information security into account. As a result, ICS components can sometimes contain serious vulnerabilities that can only be remedied later on.

### 2 12 Manipulated firmware

For ICS components, the operating system (firmware) can be changed in addition to the application program. This allows manipulated software to enter the system. The internal memory could be altered by a compromised programmer, through a local data interface (eg, USB), or through another existing network connection by an attacker. Similarly, a software update could have been manipulated on the way from the manufacturer to the operator. Finally, a component with already compromised firmware could arrive at the operator, such as a manipulated supply chain or purchasing from insecure sources. This gives an attacker the opportunity to change or distort processes and procedures.

3 requirements
---------------

The following are specific requirements for the General ICS Component area. Basically, the ICS Information Security Officer (ICS-ISB) is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the defined security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### IND.2.1.A1 Restricting Access to Configuration and Maintenance Interfaces [ICS Administrator]

It MUST be ensured that only authorized employees can access the configuration and maintenance interfaces of ICS components. The configuration MUST be changed ONLY after a release on the ICS component or authentication.

Default or factory-set passwords MUST be changed. The change MUST be documented and the password securely stored. SHOULD be changed as default or factory set user accounts.

#### IND.2.1.A2 Use of Secure Configuration and Maintenance Protocols [ICS Administrator, Maintenance Staff]

Secure protocols MUST be used to configure and maintain ICS components. The data MUST NOT be transmitted unprotected.

#### IND.2.1.A3 Logging [ICS Administrator]

It MUST be specified:

* which data / events should be logged,
* how long the log data are stored and
* who is allowed to see this.
In general, all safety-relevant system events MUST be logged and evaluated if necessary.

#### IND.2.1.A4 Deactivation of unused services, functions and interfaces [ICS administrator, maintenance personnel]

All unused services, functions and interfaces of ICS components MUST be disabled or uninstalled.

#### IND.2.1.A5 Deactivation of unused user accounts [ICS Administrator]

Unused and unnecessary user accounts MUST be disabled.

#### IND.2.1.A6 Network Segmentation [ICS Administrator]

ICS components MUST be disconnected from the office IT. If ICS components are dependent on other services in the network, this should be sufficiently documented. ICS components SHOULD communicate as little as possible with other ICS components.

### 3.2 Standard requirements
Together with the basic requirements, the following requirements correspond to the state of the art in the field of general ICS components. They SHOULD be implemented in principle.

#### IND.2.1.A7 Backups [Control Center Operator]

Programs and data MUST be backed up regularly and after system changes.

#### IND.2.1.A8 Malware Protection [ICS Administrator]

ICS components SHOULD be protected from malicious programs by appropriate mechanisms. If an anti-virus program is used for this, the program and the virus signatures SHOULD always be up to date. If resources on the ICS component could not be sufficient or the real-time requirement could be jeopardized by the use of antivirus software, alternative measures, such as: As the foreclosure of the component or the production network, be taken.

#### IND.2.1.A9 Communication Relationship [ICS Administrator]

It SHOULD document with which systems an ICS component exchanges which data. In addition, the communication links of newly integrated ICS components SHOULD be documented.

#### IND.2.1.A10 System Documentation [Control Center Operator, ICS Administrator]

It SHOULD be created an extended system documentation. These should include specific features of the operation (eg backup, routine maintenance, replacement and restoration of components, third-party services) and the system administration options (eg remote access). In addition SHOULD be documented if ICS components were changed. It SHOULD be ensured that only authorized employees can access the system documentation. Also, the documentation SHOULD still be available in the event of a malfunction.

#### IND.2.1.A11 ICS Component Maintenance [Maintenance Personnel, Control Center Operator, ICS Administrator]

When servicing an ICS component, the latest and released security updates SHOULD always be loaded. Updates to the operating system SHOULD NOT be installed until approved by the manufacturer of a component, or the update SHOULD be tested in a test environment before it is used in a production component. For critical security updates, maintenance should be performed at short notice.

#### IND.2.1.A12 Acquisition of ICS Components [Control Center Operator, ICS Administrator]

For ICS components, uniform information security requirements appropriate to protection needs SHOULD be defined. These SHOULD be taken into account when procuring new ICS components.

#### IND.2.1.A13 Suitable commissioning of the ICS components [ICS Administrator]

Before ICS components are commissioned, they SHOULD comply with the current internally released firmware, software, and patch release.

New ICS components SHOULD be integrated into existing operations, monitoring and information security management processes. That should in particular

* the change and authorization management,
* the vulnerability management,
* protection against malware,
* the operational monitoring as well as contingency planning and
* Regular security check of the systems
include.

#### IND.2.1.A14 Disposal of ICS Components [ICS Administrator]

When eliminating old or defective ICS components, all sensitive data SHOULD be safely deleted. In particular, it should be ensured that all access data has been permanently removed.

#### IND.2.1.A15 Central System Logging and Monitoring [ICS Administrator]

All ICS components SHOULD transmit their logging data to a central system. The logged data SHOULD be evaluated regularly. For security-critical events, an automatic alerting SHOULD be made.

#### IND.2.1.A16 External Interface Protection [ICS Administrator]
Externally accessible interfaces, eg. Network interfaces, USB ports or serial ports SHOULD be protected from misuse.

#### IND.2.1.A17 Using Secure Protocols for Information Transfer [ICS Administrator]

Measurement or control data SHOULD be protected against unauthorized access or modification. For applications with real-time requirements SHOULD check if this is necessary and feasible. If measurement or control data is transmitted over public networks, they SHOULD be adequately protected.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### IND.2.1.A18 Communication in the event of a fault [Control Center Operator, ICS Administrator] (A)

It SHOULD provide alternative and independent means of communication that can be used in the event of a malfunction in order to remain able to act.

#### IND.2.1.A19 Security Tests [ICS Administrator] (CIA)

Regular security tests SHOULD check to see if the technical security measures have been implemented effectively. The security tests SHOULD NOT be done while the plant is in operation. The tests SHOULD be scheduled for maintenance times. The results SHOULD be documented. Identified risks SHOULD be evaluated and treated.

#### IND.2.1.A20 Trusted Code [ICS Administrator] (IA)

Firmware updates or new control programs SHOULD only be played if their integrity and authenticity has been checked beforehand.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and safety measures in the area "General ICS component" can be found in the following publications, among others:

* #### [AHWAST] How to Use the White Paper - Requirements for Secure Control and Telecommunication Systems (Version 1.1, 2014)

  

 BDEW Federal Association of Energy and Water Management e.V. and Austria's e-Economy, Version 1.1, 2014
 [Https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge](https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge?open&ccm)

 
* #### [ICSSK] ICS Security Compendium

  

 Federal Office for Information Security (BSI), 2016
 [https://www.bsi.bund.de/DE/Themen/Industrie\_KRITIS/Empfehlungen/ICS/empfehlungen\_node.html](https://www.bsi.bund.de/DE/Themen/Industrie_KRITIS/ recommendations / ICS / empfehlungen_node.html)

 
* #### [ICSSKfH] ICS Security Compendium for Manufacturers and Integrators

  

 Federal Office for Information Security (BSI), 2014
 <Https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ICS/ICS-Security-Kompendium-Hersteller.html>

 
* #### [NIST80082] NIST Special Publication 800-82, Revision 2

  

 Guide to Industrial Control Systems (ICS) Security, National Institute of Standards and Technology (NIST), 2015
 [Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r2.pdf](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-81-2. pdf)

 
* #### [WAST] Whitepaper Requirements for secure control and telecommunication systems

  

 BDEW Federal Association of the Energy and Water Industry e.V, Version 1.1, 01.2015
 [Https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge](https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge?open&ccm)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the "General ICS component" block.

* G 0.2 Unfavorable climatic conditions
* G 0.4 Pollution, dust, corrosion
* G 0.8 Failure or malfunction of the power supply
* G 0.9 Failure or malfunction of communication networks
* G 0.10 Failure or malfunction of supply networks
* G 0.12 Electromagnetic interference
* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.28 Software vulnerabilities or errors
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.37 denying actions
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.41 Sabotage
* G 0.43 Importing messages
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
