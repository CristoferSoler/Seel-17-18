1 description
--------------

### 1.1 Introduction

Buildings form the outer physical framework for the execution of business processes. A building comprises the stationary workstations, the processed information as well as the established information technology and thus ensures an external protection for them. In addition, the infrastructure of a building often enables the execution of business processes and IT operations. Therefore, not only the building itself, so walls, ceilings, floors, roof, windows and doors to look at, but also all building-wide infrastructure and utilities such as electricity, water, gas, heating and cooling.

Considered is a building that is used by one or more organizational units of an institution. These can have quite different security requirements. In addition, it must be taken into account in all considerations that a building can and should almost always be entered by non-institutional customers (citizens, customers, suppliers). If a building is used by different parties in such a way, the design and equipment of the building and the concept of use for the building must fit together. It is intended to ensure an optimal environment for people working in the building. Unauthorized persons should not be allowed access there, where they could impair safety, and the technology deployed in the building should be safe and efficient.

### 1.2 Objective

This module describes which requirements have to be met in order to optimally use a building from the point of view of information security. The measures resulting from the requirements depend on the type and size of the institution. Requirements from this module can also be transferred to large properties with several buildings or to the use of individual parts of buildings in multi-party buildings.

### 1.3 Delimitation

This module considers technical and non-technical safety aspects in the planning and use of typical buildings for companies and authorities. The entire lifecycle of buildings is considered, starting with the preparation of a catalog of requirements, over conception, installation, use to conversions or excerpt.

The cabling in a building is considered separately in the modules INF.3 Electrotechnical cabling and INF.4 IT cabling, special rooms such as server rooms or archive rooms in the respective building blocks of the INF layer.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the General Building area:

### 2 1 fire

Buildings and the people and facilities inside them can be severely damaged by fire. In addition to direct damage caused by the fire, consequential damage must also be considered. The biggest source of danger in a fire is the toxic fire smoke. Most personal injury in a fire is caused by smoke poisoning. Even at facilities and IT systems, fire smoke can cause serious damage.

For example, when PVC is burned, it produces chlorine gas, which together with the humidity and extinguishing water form hydrochloric acid. Distributing the hydrochloric acid vapors through the air conditioner can cause damage to sensitive electronic equipment located in a part of the building far from the fire.

### 2 2 FlashLightning is the essential hazard during a thunderstorm for buildings and the information technology contained therein. Lightning reaches currents of up to 200,000 amperes at voltages of several 100,000 volts. This enormous electrical energy is released and mined within 50-100 microseconds. A lightning strike with these values, which strikes at a distance of about 2 km, still causes power surges in the building in the building, which can lead to the destruction of sensitive electronic devices. These indirect damages increase with decreasing distance.

If the lightning strikes a building directly, the dynamic energy of the lightning causes damage. This can be damage to the building (roof and facade), damage caused by fires or overvoltage damage to electrical equipment.

### 2 3 water

Water can cause damage to a building and its facilities from outside, for example, from rain, flood or floods, or from the inside, for example from defects in water pipes.

### 2 4 Natural damage and natural disasters

Depending on the location of a building, it is exposed to varying degrees of risk from natural disasters and natural disasters. Causes of natural disasters can be seismic, climatic or volcanic phenomena such as earthquakes, floods, landslides, tsunamis, avalanches and volcanic eruptions. Examples of extreme meteorological phenomena are severe weather, hurricanes or cyclones.

### 2 5 Environmental hazards

Buildings may be damaged or impaired by events in the immediate area, such as the immediate emergence of toxic substances or, indirectly, rescues, road closures or evacuations.

### 2 6 Unauthorized access

If unauthorized persons enter a building or individual premises, this can result in various other security threats. Unauthorized persons can cause damage through intentional acts such as theft or manipulation of information or IT systems, but also through unintentional misconduct (eg due to lack of expertise).

The aim of a burglary may be the theft of IT components or other readily available goods, as well as the copying or manipulation of data or IT systems. Non-obvious manipulations can cause much higher damage than direct destruction. Even unauthorized intrusion can cause property damage. Windows and doors are forcibly opened and damaged, they must be repaired or replaced.

### 2 7 Violation of laws or regulations

When constructing buildings, a large number of laws and regulations must be observed, for example relating to fire protection or other aspects of structural safety. If it is violated, it may not be noticeable for a long time, but it can have catastrophic consequences if, for example, fireboards were improperly installed.

### 2 8 Insufficient firing

Every building in which IT operates is criss-crossed by a multitude of wires and cables. Fresh and sewer pipes, heating pipes, energy supply and data transmission are mentioned as examples. It is inevitable that such pipe and cable routes must cross fire walls and floors. If suitable fire barriers are not installed in such places, fires and smoke may spread uncontrollably.The high dynamics of the IT also make it necessary to relocate, even beyond the firebox, in the pipeline network. In what form that can be done correctly depends directly on the existing bulkhead and can be very different. If changes to a firewall are not carried out in accordance with the requirements of the respective bulkhead manufacturer, there is a risk that it will fail in the event of a fire and the fire can thus expand into the area actually protected by the bulkhead.

### 2 9 Power failure

In the event of a power outage, entire buildings or parts of them may become unusable. Not only the obvious, direct power consumers such as IT or lighting are dependent on the power supply, also all infrastructure facilities are today directly or indirectly dependent on the electricity, eg. As elevators, air conditioning, security systems, security locks, automatic door locking systems, sprinkler systems, telephone extension systems. Even the water supply is dependent on electricity in high or low floors because of the pumps required to generate pressure.

3 requirements
---------------

The following are specific requirements for the General Building area. Basically, the building services is responsible for meeting the requirements, ie the organizational unit that is responsible for the facilities of the infrastructure in a building or in a property. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### INF.1.A1 Planning of building security [Planner, Information Security Officer (ISB)]

Based on the planned or existing use of a building and the protection requirements of the business processes operated there, it MUST be determined how the building is to be secured. For a building, many different aspects of security MUST be respected for the protection of people in the building, the protection of assets and the IT, from fire protection to electrical systems to access control. The safety requirements from the different areas MUST be coordinated with each other.

#### INF.1.A2 Adapted circuits

It MUST be checked regularly whether the protection and design of the circuits still meet the actual needs.

#### INF.1.A3 Compliance with fire safety regulations

The existing fire protection regulations as well as the requirements of the construction supervision MUST be complied with. The escape routes MUST be signposted and kept open in accordance with regulations. The local fire brigade SHOULD be called in during the fire protection planning. The regulations for fire protection resulting from the building regulations are not sufficient for the requirements of the fire protection of the IT. Therefore, an IT-related fire protection concept MUST be created and implemented.

Unnecessary fire loads MUST be avoided. This includes the regular disposal of waste paper and packaging waste.

There MUST be a fire safety officer or a person entrusted with the task, who is also properly trained.

#### INF.1.A4 fire detection in buildings [planner]Buildings MUST be equipped with a sufficient number of smoke detectors. For larger buildings, a fire alarm panel (BMZ) SHOULD be used, to which all detectors are connected. In the case of smoke detection, an alarm MUST be triggered in the building to ensure that all persons present in the building can perceive it. The functionality of all smoke detectors or all components of a fire alarm system MUST be checked regularly. It MUST be regularly checked that the escape routes are usable and free from obstructions, so that the building can be cleared quickly in a dangerous situation.

#### INF.1.A5 Hand Fire Extinguisher

For firefighting fires, manual fire extinguishers in the appropriate fire class (DIN EN 3 Portable Fire Extinguishers) MUST be available in sufficient numbers and sizes in the building. The hand fire extinguishers MUST be regularly checked and maintained. The employees SHOULD have been instructed in the use of hand fire extinguishers.

#### INF.1.A6 Closed Windows and Doors [Staff]

Windows and outward doors (balconies, terraces) MUST be closed in times when a room is not occupied. There must be a corresponding instruction for this. It MUST be checked regularly to see if the windows and doors are locked after leaving the rooms. Fire and smoke protection doors MUST NOT be kept permanently open.

#### INF.1.A7 Access Control and Control [Head of Organization]

Access to protected parts of buildings and rooms MUST be regulated and controlled. There SHOULD exist a concept for access control. The number of authorized persons SHOULD be kept to a minimum for each area. Additional persons may only be admitted after prior examination of the necessity. All issued access authorizations SHOULD be documented. The access control measures MUST be regularly checked for their effectiveness.

#### INF.1.A8 smoking ban [staff]

For rooms with IT or data carriers (server room, data carrier archive but also document archive), in which fires or soiling can lead to high damage, a smoking ban MUST be issued. It MUST be regularly checked that the access protection is not undermined when establishing or tolerating smoking areas.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​general buildings. They SHOULD be implemented in principle.

#### INF.1.A9 Safety Concept for Building Use [Planner, Information Security Officer (ISB)]

It SHOULD give a security concept for the building use. The security concept for the building SHOULD be coordinated with the overall security concept of the institution. It SHOULD be updated regularly.

Protected rooms or parts of buildings SHOULD NOT be housed in exposed or endangered areas.

#### INF.1.A10 Compliance with relevant standards and regulations [installer company, site manager]

When planning, constructing and reconstructing buildings and installing technical equipment, all relevant standards and regulations SHOULD be taken into account.

#### INF.1.A11 Completed doors [Staff]

Employees SHOULD be instructed to close their office when absent or to close their work records. It SHOULD be checked sporadically if this is implemented.

#### INF.1.A12 key management

For all keys of the building (of floors, corridors and rooms) SHOULD have a locking plan. The production, storage, administration and issuing of keys SHOULD be centrally regulated. Reserve keys SHOULD be kept and secured, but kept handy for emergencies. Unissued keys SHOULD be stored safely. Each key issue SHOULD be documented.#### INF.1.A13 Regulations for access to distribution boards

The access to the distributors of all utilities in a building SHOULD be quickly possible if needed. The access to distributors SHOULD be limited to a narrow circle of beneficiaries.

#### INF.1.A14 Lightning protection devices

A lightning protection system should be installed according to the current standard. There SHOULD be a comprehensive lightning and surge protection concept. The interception systems in buildings with extensive IT equipment SHOULD comply at least with protection class II in accordance with DIN EN 62305 "Lightning protection". The lightning protection system SHOULD be checked and serviced regularly.

#### INF.1.A15 Location plans of utilities

There SHOULD have up-to-date maps of all supply lines. It SHOULD be regulated who keeps and updates the site plans of all utilities. The plans SHOULD be kept in such a way that only authorized persons can access them, but they are quickly available when needed.

#### INF.1.A16 Avoidance of position information on parts of buildings that are to be protected

Location references to areas worthy of protection SHOULD be avoided. Protective building areas SHOULD NOT be easily visible from the outside.

#### INF.1.A17 Structural smoke protection [Planner]

The structural smoke protection SHOULD be checked after installation and conversion work. The functionality of the smoke protection components SHOULD be checked regularly.

#### INF.1.A18 fire safety inspections

Fire safety inspections SHOULD take place regularly, at least once or twice a year. Deficiencies detected during fire safety inspections SHOULD be rectified immediately.

#### INF.1.A19 Early information of the fire protection officer

The fire protection officer SHOULD be informed about work on pipeline routes, corridors, escape and rescue routes. He SHOULD check the proper execution of fire protection measures.

#### INF.1.A20 Alerting plan and fire drills

An alerting plan should be drawn up for the measures to be taken in case of fire. He SHOULD be updated periodically. Fire safety exercises SHOULD be carried out regularly. The alert plan SHOULD be reviewed and updated periodically.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### INF.1.A21 Independent electrical supply strands (A)

The IT SHOULD be fed by two independent supply strings.

#### INF.1.A22 Safe Doors and Windows (CIA)

Doors and windows SHOULD be selected according to the protection goals of the area to be protected and the protection needs of the institution as well as the appropriate classification in the relevant standards. All room enclosing security measures through windows, doors and walls SHOULD be equivalent and appropriate in terms of burglary, fire and smoke. It SHOULD be checked regularly that the security doors and windows are functional.

#### INF.1.A23 Formation of Security Zones [Planner] (C)

Rooms with similar protection requirements SHOULD be zoned together to treat comparable risks consistently and to reduce the cost of required security measures. A security zone concept for buildings and land SHOULD be developed and documented.

#### INF.1.A24 Automatic drainage (A)All water hazard areas SHOULD be equipped with automatic drainage. The functionality of active and passive drainage systems SHOULD be checked regularly.

#### INF.1.A25 Suitable Location Selection [Institutional Management] (A)

When selecting or planning a building location, it should be examined which environmental conditions could influence the information security. It SHOULD give an overview of location-related hazards. These threats SHOULD be countered with additional compensatory measures.

#### INF.1.A26 porter or security service (CIA)

The duties of the porter or security service SHOULD be clearly documented. The gatekeepers SHOULD observe and control all movement of persons at the gate and at all other entrances. All employees and visitors SHOULD legitimize themselves at the gatekeepers. Visitors SHOULD be accompanied to the visitors or picked up at the gate. The gatekeepers SHOULD be informed in good time if access authorizations change.

#### INF.1.A27 Burglary Protection (CIA)

It was intended to implement adequate anti-burglary measures adapted to local conditions. Equivalence and continuity of burglary protection during planning, implementation and operation SHOULD be assessed regularly by a competent person. The regulations for burglary protection SHOULD be known to the employees.

#### INF.1.A28 Air conditioning for people (IA)

In larger buildings the air supply SHOULD be provided by ventilation and air conditioning (RLT) systems. The RLT systems SHOULD be designed for the actual use of the building. You SHOULD maintain RLT systems regularly.

#### INF.1.A29 Organizational requirements for the cleaning of buildings (CIA)

It SHOULD be checked whether the employees of the commissioned cleaning company use the issued keys or ID cards according to the contract. The cleaning staff SHOULD be sufficiently informed about the handling of the IT. Cleaners SHOULD be supervised in the most sensitive areas at work.

#### INF.1.A30 Selection of a suitable building (CIA)

When selecting a suitable building, it should be checked whether all safety requirements relevant for later use can also be implemented. For each building, the existing hazards and the necessary damage prevention or reduction measures SHOULD be documented in advance.

#### INF.1.A31 Extract from Buildings [Inner Service] (C)

In the run-up to the excerpt, an inventory of all things relevant to information security (hardware, software, data carriers, folders, documents, etc.) SHOULD be compiled. After moving out, all rooms SHOULD be searched for left behind things.

#### INF.1.A32 firewall cadastre (A)

A firewall cadastre was to be run. In this, all types of bulkhead SHOULD be individually recorded. After working on firebox, the changes in the cadastre SHOULD be entered at the latest after 4 weeks.

#### INF.1.A33 Arrangement of protected buildings (CIA)

Protected rooms or parts of buildings SHOULD NOT be housed in exposed or endangered areas. If there are exposed rooms in an exposed position, sufficient measures should be taken to secure them. This SHOULD be documented.

#### INF.1.A34 Alarm system (A)

It SHOULD provide a hazard warning system appropriate to the premises and the risks. The alarm system SHOULD be regularly serviced or tested. It SHOULD be checked whether the recipients of hazard reports are able to respond appropriately to the alarm technically and personally.

4 Further Information
------------------------------

### 4.1 LiteratureFurther information about hazards and safety measures in the area of ​​"General Building" can be found in the following publications, among others:

* #### [27001A11] ISO / IEC 27001: 2013 - Annex A.11 Physical and envionmental security

  

 ISO, Information technology - Security techniques - Information security management systems - Requirements, in particular Annex A, A.11 Physical and environmental security, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [ISFCF19] The Standard of Good Practice - AREA CF19 Physical and Environmental Security

  

 especially AREA CF19 Physical and Environmental Security, ISF, 06.2014

 
* #### [NIST80053PEP] NIST Special Publication 800-53 Revision 4 - APPENDIX PAGE F-213

  

 Assesing Security and Privacy Controls for Federal Information Systems and Organizations, in particular APPENDIX F-PS PAGE F-213, FAMILY: PHYSICAL AND ENVIRONMENTAL PROTECTION, NIST, 2013
 <Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "General Building".

* G 0.1 fire
* G 0.2 Unfavorable climatic conditions
* G 0.3 water
* G 0.4 Pollution, dust, corrosion
* G 0.5 natural disasters
* G 0.6 disasters in the environment
* G 0.7 Major events in the environment
* G 0.8 Failure or malfunction of the power supply
* G 0.10 Failure or malfunction of supply networks
* G 0.16 Theft of devices, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.29 Violation of laws or regulations
* G 0.34 stop
* G 0.44 Unauthorized intrusion into premises
The cross reference tables can be found in the download area due to their size.