Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Today, almost all strategic and operational functions and tasks are significantly supported by information technology (IT) or can not be executed without IT. As a result, the demands on the performance and availability of the IT systems and their connection to the network environment are steadily increasing. To meet this need for power, maintain reserves, and run IT economically, government agencies and companies of all sizes are concentrating their data center IT landscape.

A data center (RZ) is defined as follows:

If a data center deviates from this definition, the considered IT operating area is referred to as a server room. This definition is based exclusively on the importance of the IT structure for the task fulfillment of the using institution and is thus in methodological harmony with DIN EN 50600.

If a server room is to be protected, the requirements of this module can be reduced accordingly. However, this must be substantiated reasonably and comprehensibly (according to 6.) and at least the basic requirements must be implemented.

### 1.2 Objective

On the one hand, the module addresses institutions that run a data center and want to check whether they have implemented appropriate security measures in the course of a revision. On the other hand, the building block can also be used to estimate the security measures that must be implemented when centralizing IT in a data center. The ultimate goal of the requirements described in this module is to maintain the secure operation of the data center.

### 1.3 Delimitation

The subject of this module are only data centers of medium type and quality. The security requirements described here are not sufficient to protect high-security data centers, such as those used in the banking sector. A high-security data center is different, especially in the points high availability, disaster tolerance, redundancy of components, resistance to natural hazards, energy efficiency and data security of the consideration here mean data centers.

Furthermore, the present module is not suitable for small information networks with z. B. only one or very few servers or IT systems. An example of this is a small, medium-sized enterprise (SME) with few IT workstations and a server that is located in a separate room. In such cases, it is often sufficient to implement the INF.6 * protective cabinet / technical room * module.

In order to keep the module manageable, it deliberately avoided technical details and planning parameters. Further information can be found in relevant standards, eg. Eg DIN EN 50600.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to data centers:

### 2 1 Incorrect planning

If a data center is designed and ignored to protect against elementary threats, there is a very high risk of failure. So z. For example, site risks such as air traffic, earthquakes, floods, or political issues may jeopardize operational safety and availability. It can also have a massive impact on the operation of a new data center if there is insufficient bandwidth available due to incorrect design or if the energy supply at the selected location is insufficient.

### 2 2 Unauthorized access
Lack of access controls or these are insufficient, increases the risk that unauthorized persons enter the data center and there negligent, z. B. due to lack of expertise, or intentionally cause damage. Attackers can so z. For example, stealing sensitive data, stealing devices or manipulating servers. Inadequate access controls thus have a particular impact on the availability, confidentiality and integrity of data or IT components.

### 2 3 Insufficient monitoring

If the IT and infrastructure operated in the data center are insufficiently monitored and maintained, components can go unnoticed. This may severely affect the availability and accuracy of the data center. In addition, failures often occur creepingly. Without active monitoring, they might be noticed too late. It is then often not possible to react in time.

### 2 4 Insufficient air conditioning in the data center

IT components require a certain operating temperature to function properly. They also convert their energy into additional heat. If a data center is not or insufficiently air-conditioned, the climatic conditions in the room can not be kept stable. If it is too cold or too hot, the devices may undercut or exceed their permissible operating temperature. The consequences are z. B. malfunctions and failures of technical components or damaged storage media.

### 2 5 fire

If a data center has no or only insufficient fire protection, there is a risk of a fire developing and spreading rapidly. Fire and smoke can cause great damage. Also, arcing may not prevent early.

### 2 6 water

Leakages in the data center infrastructure, floods, burst pipes, faulty sprinkler systems, sewer damage or even air conditioning faults can cause water to enter the data center. This can cause devices to become damaged or stop working. Also could be triggered such a short circuit, which leads to total failure or even causes a fire.

### 2 7 Missing or inadequate burglary protection

Missing or inadequate intruder protection makes it easy for unauthorized individuals to invade a data center. Offenders can so z. B. stealing or manipulating IT components and accessing confidential information. They could also destroy the devices or damage the data center as a whole.

### 2 8 Power failure

If the power fails and there is no redundant power supply, this can lead to significant disruptions in the operation of a data center and thus the institution. For example, in the event of a power outage, all IT services provided by the data center are suddenly unreachable. Also, data can be lost. Furthermore, it is possible that a sudden power failure will damage IT systems, active network components, telecommunications systems or surveillance technology.

### 2 9 pollution

Dust and other contaminants in a data center can cause the technology to stop working. Due to contamination, it precipitates more often and wears out sooner.

### 2 10 Insufficient roadway dimensioning
If cable runs are not routed separately and minimum clearances are not met, data center IT disruptions can occur. Also extensions of the network can be problematic, so that the protection against fire and smoke developments may no longer be guaranteed. It should also be noted that holes for fire-rated cable glands may only be laid with cables at 60% of the cross-section. 40% must be filled with fire-retardant mortar or another material approved for firefighting. If this requirement is not observed, a fire from the adjacent room may easily spread to the RZ.

3 requirements
---------------

The following are specific requirements for data center protection. Basically, the IT manager is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### INF.2.A1 Definition of requirements [planner, IT operation, building services, information security officer (ISB)]

For a data center, appropriate technical and organizational requirements MUST be defined and implemented.

When planning a data center or selecting suitable premises, it is important to consider potential environmental hazards and the security level of the IT components (especially availability). Furthermore, safeguards against potential internal and external attacks MUST also be included in the overall assessment.

A data center MUST be designed overall as a closed security area. It MUST also have different security zones. For this purpose, administrative, logistics, technical and IT areas MUST be clearly separated. In the case of a server room SHOULD it be checked whether different security zones are feasible.

It MUST also be ensured that supply lines (eg for water or gas) do not run as far as possible in the immediate vicinity of technical components requiring protection. Existing supply lines MUST be checked at least at the critical points regularly, whether they are still tight.

#### INF.2.A2 Fire department formation [planner]

Appropriate fire compartments MUST be set for the premises of a data center. The protection target for the fire wall or the fire section MUST not only be personal and building protection, but also the protection of the inventory and its availability. Thus, not only must a fire be prevented from spreading by flames and hot flue gases, but also heat radiation and the spread of cold smoke MUST be blocked. In the case of a server room, it should be checked whether suitable fire compartments for the premises can be implemented.

#### INF.2.A3 Use of an Uninterruptible Power Supply [Building Services]

For all operational components of the data center, an uninterruptible power supply (UPS) MUST be installed. Since the power requirement of air conditioning systems is often too high for a UPS, however, at least the control of the equipment MUST be connected to the uninterruptible power supply. In the case of a server room, IT systems SHOULD check to see if the operation of a UPS is necessary, depending on the availability requirements of the IT systems.

The UPS MUST be adequately dimensioned so that all components are powered on in the event of a power failure, so that no data loss occurs.
In the case of relevant changes, it MUST be checked whether the existing UPS systems are still sufficiently dimensioned. The battery of the UPS MUST be maintained in the required temperature range and preferably placed in a separate area.

The UPS MUST be regularly maintained and tested for functionality. For this, the maintenance intervals provided by the manufacturer MUST be adhered to * (* see * INF.2.A10 Infrastructure Inspection and Maintenance) *. In order to ensure that the UPS provides the necessary support time, the actual support time MUST be determined on a regular basis and, in addition, if there is a change in the consumer.

If IT equipment is powered by a UPS, DO NOT connect it to other IT equipment using shielded wires.

#### INF.2.A4 emergency shutdown of power supply [building services]

In the event of an emergency, there must be suitable possibilities for disconnecting the data center from power. For example, an emergency stop button SHOULD be installed. Such a switch MUST not only disconnect the external power supply, but also switch off the entire UPS system. All emergency stop switches MUST be protected so that they can not be inadvertently actuated.

#### INF.2.A5 compliance with air temperature and humidity [building services]

In order to be able to operate IT systems reliably in accordance with the manufacturer's recommendations, it MUST be ensured that the air temperature and humidity in the IT operating range are within the prescribed limits.

The actual heat load in the refrigerated areas MUST be checked at regular intervals and after major modifications by calculation or measurement.

Also, any existing air conditioning MUST be maintained regularly. If the two parameters "temperature" and "humidity" deviate from the standard value, they MUST be recorded over a representative period in a time interval adapted to the situation.

#### INF.2.A6 Access control [IT operation, information security officer (ISB), building services]

There must be an access control to protect against unauthorized access to a data center.

An access regulation tailored to the respective requirements MUST ensure for own employees and for temporary employees that they are not allowed to access IT systems outside their area of ​​activity.

In addition, it MUST be ensured that visitors and external personnel are individually recorded and supervised by the access control during all work in the data center.

In addition, all access to a data center MUST be monitored. The institution's requirements for an access control system MUST be documented in sufficient detail in a concept. In the case of a server room, it should be checked whether it makes sense to monitor all access options.

Furthermore, it MUST be regulated which internal and external persons are allowed access for which period. It MUST be ensured that no unnecessary or too extensive access rights are granted. It MUST be checked regularly whether the regulations for the use of an access control are adhered to.

#### INF.2.A7 Closing and securing [staff, building services]

All data center doors MUST always be kept locked. Windows should be avoided as early as possible during planning. If they do exist, they MUST be kept locked as well as the doors. Doors and windows MUST provide adequate protection against attack and environmental influences (eg fire and smoke). It should be noted that the structural design of all space-forming elements in terms of safety, especially in terms of security zones, must be equivalent.

#### INF.2.A8 Use of a fire alarm system [planner]
A fire alarm system MUST be installed in a data center. This MUST monitor all surfaces. All messages from the fire alarm system MUST be forwarded appropriately (see also INF.2.A13 * Planning and installation of hazard alarm systems *). The fire alarm system MUST be maintained regularly. It MUST be ensured that no special fire loads are present in rooms located in the fire compartment of the data center.

#### INF.2.A9 Use of extinguishing or fire prevention system [Planner]

In a data center, a state-of-the-art extinguishing or fire prevention system MUST be installed.

In server rooms, manual fire extinguishers in sufficient numbers and sizes SHOULD be used. The fire extinguishers MUST be installed so that they are easily accessible in case of fire. Each extinguisher MUST be regularly inspected and maintained to ensure proper functioning in the event of an emergency. All employees MUST be instructed in the use of hand fire extinguishers.

#### INF.2.A10 Inspection and maintenance of the infrastructure [IT operation, building services, maintenance personnel]

All components of the technical infrastructure MUST comply with at least the recommended or standard intervals and requirements for inspection and maintenance. In order to understand when which work has been carried out, inspections and maintenance MUST be logged.

Cable and pipe penetrations through fire walls MUST be checked regularly to ensure that the bulkheads are in conformity with standards and intact. The results MUST be documented.

#### INF.2.A11 Automated monitoring of the infrastructure [IT operation, building services]

All fault messages of the infrastructure, eg. As leakage monitoring, air conditioning, electricity and UPS systems MUST be automatically monitored and forwarded as quickly as possible, z. B. via a monitoring system.

In the case of a server room, IT and support equipment that is rarely or rarely operated by one person SHOULD be equipped with a remote annunciator. The responsible employees MUST be alerted promptly.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​data center and server room. They SHOULD be implemented in principle.

#### INF.2.A12 Design and implementation of a perimeter protection for the data center [planner, building services]

The security measures for perimeter protection SHOULD be equivalent to those of the security concept for the building and its environment. Depending on the specified protection requirements for the data center and depending on the terrain, the perimeter protection SHOULD consist of the following components:

* outer enclosure or enclosure,
* Precautionary measures against unintentional crossing of a property boundary,
* Precautionary measures against intentional non-violent overcoming of the property boundary,
* Precautionary measures against intentional violent overcoming of the property boundary,
* Field-level safeguards as well
* outside person and vehicle identification.
#### INF.2.A13 Planning and installation of alarm systems [planner]

A consistent protection concept for the considered building SHOULD be developed. Only then should it be planned which alarm systems are needed and installed for which building areas of the data center and how to deal with alarm messages. The concept SHOULD always be adapted as the use of the building areas changes.
A suitable alarm system (GMA) should be installed for the respective field of application. The messages of the GMA SHOULD be connected to an alarm receiving station in compliance with the applicable Technical Connection Conditions (TAB). The alarm receiving station SHOULD be reachable at all times and technically as well as personnel able to respond in a suitable manner to the reported hazard. The transmission path between the inserted GMA and the auxiliary service SHOULD be configured redundantly. All transmission paths SHOULD be tested regularly.

#### INF.2.A14 Use of a network replacement system [planner, building services]

The energy supply from the network of a power supply company () SHOULD be supplemented by a power supply system (NEA). The resources of a NEA SHOULD be checked regularly. In order to maintain the protective effect of an NEA, it SHOULD be regularly maintained (see INF.2.A10 * Infrastructure Inspection and Maintenance *). During these services, load and function tests as well as test runs under load should also be carried out.

#### INF.2.A15 Surge protection device [Planner, building services]

On the basis of the currently valid standard, a lightning and surge protection concept based on the principle of energetic coordination (Annex C of DIN EN 62305-4) SHOULD be created and implemented. The energetic coordination of the overvoltage protection devices SHOULD be documented and approved in a concept.

Lightning and overvoltage protection devices SHOULD be periodically and after known events checked and replaced if necessary. Regardless of the scope and expansion of the overvoltage protection SHOULD be noted that a comprehensive and continuous equipotential bonding of all electrical equipment included in the surge protection is required. For subsequent installations, care should be taken that the equipotential bonding is carried along.

#### INF.2.A16 Air conditioning in the data center [Building Services]

It SHOULD be ensured that the climatic conditions for air temperature and humidity in the data center (see INF.2.A5 * Compliance with Air Temperature and Humidity *) as well as for fresh air and suspended solids are created and maintained. The air conditioning SHOULD be sufficiently dimensioned for the data center. All relevant values ​​SHOULD be constantly monitored. If a value deviates from the norm, an automatic alerting should take place.

The air conditioning systems SHOULD be as fail-safe as possible in computer room areas, z. B. by redundant designed components.

#### INF.2.A17 Early fire detection [planner, building services]

To detect fires in data centers at a very early stage, a system for early fire detection should be installed.

To prevent incipient fires from spreading further, the early fire detection SHOULD be used to automatically disconnect the power. The monitoring areas of the early fire detection as well as the areas of action of the voltage disconnection SHOULD be designed sufficiently small-scale in order to achieve a balanced relationship between the fire protection on the one hand and the DC availability on the other hand.

The system for early fire detection SHOULD comply with the current state of the art. Also it SHOULD be operated according to the specifications of the manufacturer and regularly maintained.

#### INF.2.A18 Protection against water leakage [Building Services]

In areas where IT equipment with central functions is located, water-bearing pipes should be avoided. For example, there should be no radiators in the data center.
If water-carrying lines (eg for cooling directly on the RZ surface) are unavoidable, SHOULD it be ensured that water leaks are detected as early as possible and the effects are minimized. By visual inspection, the existing water pipes should be checked regularly to see if they are still tight. Messages from a detection system SHOULD be reported to responsible employees so that they can intervene quickly based on reaction plans and current documentation (see * INF.2.A13 Planning and Installation of Alarm Systems *).

#### INF.2.A19 Conducting functional tests of the technical infrastructure [building services]

The technical infrastructure of a data center SHOULD be tested regularly (at least once or twice a year) as well as after system modifications and extensive repairs. The results SHOULD be documented. In particular, entire reaction chains SHOULD be subjected to a real functional test.

#### INF.2.A20 Regular updates of infrastructure and construction plans [planner]

Construction plans, route plans, circuit diagrams, escape route plans, fire brigade maps, etc. SHOULD be updated immediately after each conversion or when the infrastructure or security technology has been expanded. In addition, the employees SHOULD be informed accordingly. It SHOULD be checked at least once within three years, if all relevant plans are still current and correct.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### INF.2.A21 Dodge Data Center (A)

A geographically separated alternative data center SHOULD be set up and used. The backup data center SHOULD be sized to maintain all processes of the institution. Also SHOULD it be always ready to use. All data of the institution SHOULD be regularly mirrored in the alternative data center.

#### INF.2.A22 Implementation of dust control measures [Building Services] (IA)

When an existing data center is expanded, appropriate dust control measures should be defined, planned and implemented. Persons who themselves are not involved in the construction measures should check at sufficiently close intervals whether the dust protection measures are working properly and the regulations on dust protection are complied with.

#### INF.2.A23 Secure Structured Cabling in the Data Center [Building Services] (A)

Cable trays SHOULD be carefully planned and executed. All cables SHOULD be protected against accidental mechanical stress, manipulation, eavesdropping or fire. For different types of networks, eg. As data network, network for alarm systems and power grid, separate cables should be used. If cables are routed together for different networks, it should be ensured that mutual interference is minimized. In addition, a redundant route should be sought.

#### INF.2.A24 Use of video surveillance systems [planners, building services, data protection officer] (IA)

The access control and the burglary message SHOULD be supplemented by video surveillance systems. For this purpose, the areas that make sense for video surveillance systems SHOULD be identified.

A planned video surveillance SHOULD be consistently embedded in the entire security concept. Also SHOULD be involved in the planning, conception and eventual evaluation of video recordings always the data protection officer.
The central technical components required for video surveillance SHOULD be set up and protected in a suitable environment. It SHOULD be checked regularly to see if the video surveillance system is working properly.

#### INF.2.A25 Redundant design of uninterruptible power supplies [Planner]

To ensure the availability of a data center, the UPS systems SHOULD be redundant. After a power outage, all components necessary for proper operation of the data center SHOULD be able to be powered on until an alternative power source can be connected.

#### INF.2.A26 Redundant design of emergency power systems (A)

In case of increased protection requirements, emergency power supply systems SHOULD be designed redundantly. It SHOULD be ensured that these systems are also regularly maintained (see INF.2.A10 * Infrastructure Inspection and Maintenance *).

#### INF.2.A27 Conducting alerting and fire prevention exercises (CA)

The staff of the institution SHOULD have regular alerting and fire safety exercises. These SHOULD be based on an alerting plan that documents the actions to be taken. It SHOULD be checked regularly to see if the measures are still correct, current and workable.

#### INF.2.A28 Use of higher-level alarm systems (IA)

For data center areas with increased protection requirements, only danger signaling systems of the VDS Class C should be used.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the area "data center and server room" can be found in the following publications, among others:

* #### [BKRZ] Guide Reliable Data Center

  

 Federal Association for Information Technology, Telecommunications and New Media e.V. (BITKOM), 2013 (last accessed 04.10.2017)
 <Http://www.bitkom.org/Bitkom/Publikationen/Betriebssicheres-Rechenzentrum.html>

 
* #### [DIN50600-1] DIN EN 50600-1, Information technology - Data center facilities and infrastructures

  

 Part 1: General Concepts, DIN, 2012

 
* #### [DIN62305-4] IEC 62305-4 (VDE 0185-305 / DIN EN 62305) - Lightning protection

  

 Part 4: Electrical and Electronic Systems in Structural Installations, DIN, 2011

 
* #### [VdSPeri] Safety Guide Perimeter

  

 VdS Schadenverhütung GmbH, 2012 (last accessed 04.10.2017)
 [Http://vds.de/fileadmin/vds\_publikationen/vds\_3143\_web.pdf](http://vds.de/fileadmin/vds_publikationen/vds_3143_web.pdf)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the building block "data center and server room".

* G 0.5 natural disasters
* G 0.6 disasters in the environment
* G 0.4 Pollution, dust, corrosion
* G 0.2 Unfavorable climatic conditions
* G 0.3 water
* G 0.1 fire
* G 0.7 Major events in the environment
* G 0.8 Failure or malfunction of the power supply
* G 0.10 Failure or malfunction of supply networks
* G 0.11 Failure or disruption of service providers
* G 0.15 Listening
* G 0.16 Theft of devices, data carriers or documents
* G 0.24 Destruction of equipment or data media
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.33 Personnel loss
* G 0.34 stop
* G 0.41 Sabotage
* G 0.44 Unauthorized intrusion into premises
The cross reference tables can be found in the download area due to their size.
