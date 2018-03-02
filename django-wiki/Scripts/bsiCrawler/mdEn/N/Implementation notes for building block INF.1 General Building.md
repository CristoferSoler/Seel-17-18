[toc]
 
1 description
--------------

### 1.1 Introduction

Buildings form the outer physical framework for the execution of business processes. A building comprises the stationary workstations, the processed information as well as the established information technology and thus ensures an external protection for them. In addition, the infrastructure of a building often enables the execution of business processes and IT operations. Therefore, not only the building itself, so walls, ceilings, floors, roof, windows and doors to look at, but also all building-wide infrastructure and utilities such as electricity, water, gas, heating and cooling. Building on the protection goals, the various tasks and security measures must be coordinated.

Considered is a building that is used by one or more organizational units of an institution. These can have quite different security requirements. In addition, it must be taken into account in all considerations that a building can and should almost always be entered by non-institutional customers (citizens, customers, suppliers). If a building is used by different parties in such a way, then the design and equipment of the building and the usage concept for the building must fit together. It is intended to ensure an optimal environment for people working in the building. Unauthorized persons should not be allowed access there, where they could impair safety, and the technology deployed in the building should be safe and efficient.

### 1.2 Life cycle

When securing a building, technical and non-technical safety aspects must be implemented during planning and use. The entire lifecycle of buildings must be considered, starting with the creation of a catalog of requirements, through conception, installation, use, right through to conversions or extensions.

The cabling in a building is considered separately in the modules INF.3 Electrotechnical cabling and INF.4 IT cabling, special rooms such as server rooms or archive rooms in the respective building blocks of the INF layer.

In the use of buildings for the business operations of public authorities or companies, different approaches have to be followed with regard to information security for certain measures. In a new building required measures can be carried out to a large extent already in the planning phase.

On the other hand, when it comes to renting or using an existing building, which may involve expansion and conversion, the possibilities for realizing adequate information security are often much more limited.

** planning and conception **

The planned use of a building and the protection requirements of the business processes operated there determine how the building is to be designed and equipped with safety aspects. Starting with an assessment of the location and type of the property, it is necessary to consider whether the building is fit for purpose or can be appropriately designed.

The further planning or testing of an existing building is recommended for the creation of a zone model (see INF.1.M 23 Formation of Safety Zones), which can then be used to plan the use of the building based on protection requirements (see INF.1.M1 Planning the building use). From this, the organization of access authorizations, described in Chapter 3.1 Access control system and authorization management, the execution of doors and windows and the further measures for securing and monitoring are derived.
For room occupancy planning, INF.1.M 3 compliance with fire safety regulations and, in the case of use of an existing building, INF.1.M 34 layout of buildings worthy of protection shall be applied. It is also always necessary to determine the expected electrical connection values ​​according to the intended use of the room (see INF.1.M 2 Adjusting the Circuits).

**Procurement**

Both when selecting a location for a new building and when valuing an existing building, the measures INF.1.M 25 Suitable site selection and INF.1.M 31 Selection of a suitable building must be considered.

** Construction phase and preparation for use **

During the construction phase, all protective measures assessed as necessary in the planning phase must be implemented. During the construction phase the measures INF.1.M 10 Compliance with relevant standards and regulations and INF.1.M 3 Compliance with fire protection regulations must always be applied. INF.1.M 13 Arrangements for access to distribution boards and INF.1.M 12 key management must be defined at the latest when moving into a building. Likewise, an access control and an access control concept according to INF.1.M 7 access control and control is required.

** Building use **

During the use of the building, in particular the regular use of INF.1.M 18 fire inspections shall be provided, thus monitoring compliance with the prescribed fire safety regulations. Through the use and regular monitoring of the measure INF.1.M 6 Closed windows and doors shall ensure that only authorized persons are present in the building and that at least basic protection against burglary is taken.

** Emergency Preparedness **

In order to be prepared for emergencies, an alerting plan should be set up and emergency exercises should be carried out at regular intervals, as otherwise it may be expected that incorrect decisions will be made in the event of an emergency or if there is a lack of clarity about the necessary operations (see INF.1. M 20 alerting plan and fire drills).

2 measures
-----------

The following are specific implementation instructions in the "General Building" section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### INF.1.M1 Building Security Planning [Planner, Information Security Officer (ISB)]

In order to develop practicable and economical security measures for the use of a building, the protection requirements of the business processes operated there and the basic protection goals, which often result from the business activity, must be determined. The self-evident protection of persons in the building and the protection of the assets in the context of information security, in particular the protection of IT, so the hardware and the software to be observed. In addition to the classic IT hardware, the areas of the entire support technology, ie power supply, cooling / air-conditioning, etc., must be taken into account.

In a building, many different safety aspects have to be taken into account, from fire protection and electrics to access control. Depending on the size of the institution and the buildings, there may be different responsible persons. Therefore, the different roles and tasks have to be coordinated. Competent persons should coordinate with each other in order to select appropriate security measures for the different areas, building on the protection objectives.
It is good practice to first consider zones when planning buildings (see INF.1.M 23 Building Safety Zones). Many protection goals can be achieved by not having to go from a low-security zone directly to a higher-security one. Initially, the spatial layout should be coordinated with the intended use of the building (see INF.1.M 1.13 Arrangement of buildings worth protecting). Clearly identifiable and easy-to-secure transitions should be created between different security zones. Permissible transitions between the zones are then carried out according to the protection requirement. Impermissible transitions are either prevented or particularly secured. For example, escape doors from security zones with a higher level of security into the outside area must be secured in such a way that unauthorized access from outside to inside is prevented. Windows and entrances must be protected according to their protection requirements (see INF.1.M 22 Safe Doors and Windows).

#### INF.1.M2 Adapted distribution of circuits

In many cases, the initial installation already involves inaccurately that one of the three phase conductors in the 3-phase network is significantly more heavily loaded with loads and thus burdened with them than the other two (danger of neutral point shifting). Furthermore, according to experience, the room occupancy and the connection values ​​for which an electrical installation was designed no longer correspond with the actual conditions after some time. It is therefore essential to check the electrical installation and, if necessary, adapt it to changes in the use of the room and changes and additions to the technical equipment (IT, air conditioning units, lighting, etc.). This can be done in simple cases by relocation of lines. In some cases, however, it may be necessary to install additional or completely new infeeds, lines, distributors, etc.

Further information on IT cabling and electrotechnical cabling can be found in the corresponding building blocks of the INF layer.

#### INF.1.M3 Compliance with fire safety regulations

The existing fire protection regulations (eg according to the standard DIN 4102 Fire behavior of building materials and components) and the requirements of building supervision for buildings must be strictly adhered to. The local fire department should be involved in fire safety planning.

For rooms where important IT equipment and data carriers (servers, data backups, etc.) are housed, the regulations of standard EN 1047 Part 2 should also be observed. The aim here is to minimize the effect of a fire on the contents of such rooms by special measures such as the installation of doors with fire and smoke protection quality, the careful execution of closures and possibly even the upgrading of walls.

For meeting, training and event rooms, the appropriate regulations for fire safety in meeting places may have to be observed. Since there are different additional requirements depending on the type of use, for example with regard to the opening and width of doors in the course of escape and rescue routes and signage, the local fire brigade should also be consulted here during planning.

A person should be designated who is responsible for compliance with fire safety regulations. This may be a fire safety officer or a person entrusted with the task, who is also appropriately trained.

It is advisable to observe further instructions on fire protection, as can be found, for example, in the publications of VdS Schadenverhütung GmbH.
It is particularly important to describe the escape routes well. For this, the prescribed markings must be used and the regulations for their attachment must be adhered to. The escape routes must always be kept open, that is, in particular, that they must not be blocked, z. B. by the inventory parked in the corridor or by the escape doors are completed.

Fire and smoke protection doors offer protection only when closed and must therefore never be kept permanently open by wedges or other devices. No exceptions may be allowed.

So that the fire brigade can quickly start firefighting in case of fire, it is important that the fire alarm panel, the fire alarm panel and the entry points for extinguishing water can be found quickly by signage.

Achieving efficient fire protection requires the cooperation of all parties involved. This includes the functions of the fire protection officer (employer is responsible for compliance with fire safety regulations), the specialist for occupational safety (in Germany required by §§ 5, 6 Occupational Safety Act, this is responsible for the design of the company fire protection) and the safety officer (in Germany required according to § 22 SGB VII, this has executive activities, eg for the prevention of accidents at work and occupational diseases, and works for the occupational safety specialist).

** avoidance of unnecessary fire loads **

A fire load is caused by all flammable substances that are introduced into the building. It depends on the quantity and calorific value of the substances. IT equipment and cables are as much a fire load as furniture, floor coverings and curtains. Further explanations on the flammability or non-flammability of building materials (building material class A or B) can be found in DIN 4102 Part 1 and Part 4.

When placing IT equipment, data carriers, etc., prior notice should be given to the existing fire loads in the same room and in the adjacent rooms. For example, the volume library should not be located near or over a paper store.

Even during operation, care must be taken to avoid unnecessary fire loads. The regular disposal of waste, especially waste paper and packaging waste is active fire protection. Offices should be removed no longer needed files and stored in specially designated archives. One of the most common examples of unnecessary fire loads in rooms used for IT is packaging material such as cardboard or polystyrene. From the IT rooms, packaging material must be removed immediately and transported to designated storage rooms, if it is still needed.

For buildings, the reduction of unnecessary fire loads should already be taken into account in the planning phase. Non-flammable materials are to be preferred for the removal (building material class A). In order to ensure safe operation in terms of fire protection and to not exceed limit values, a rough calculation of the later fire loads should already be made in the planning phase of buildings. The fire classes of the facilities and the building material classes of the materials must be taken into account. As a result, later difficulties in the fire protection inspection by building inspectorate and fire department are avoided.

#### INF.1.M4 fire detection in buildings [planner]

Measures for structural and technical fire protection, fire detection and timely alerting in the event of fire are elementary measures to protect the health and life of all people who are in a building.
Which measures of the structural and technical fire protection are required for a building, give in Germany the respective valid building regulations. In order to standardize the various state building regulations, the model building code (MBO) was created as a reference framework. In addition, a fire protection concept appropriate to the size and use of the building must be set up.

It is always true that in buildings, depending on the type of use and construction, fires can occur for various reasons. In order to protect people and to be able to stem a fire in time, its formation must be detected as quickly as possible and the fire fought.

In order to be able to detect, alert and combat the occurrence of a fire as quickly as possible, sufficient smoke detectors must be installed in compliance with the applicable standards and manufacturer specifications.

Local detectors can be controlled and evaluated via a fire alarm panel (BMZ). Detectors of all kinds and a fire alarm system together form the fire alarm system (BMA).

Recommended is a minimum equipment consisting of

* Smoke detectors on the ceiling of all hallways as well
* Smoke detectors on the ceiling of all technical rooms and rooms of the electrical supply (distributions, UPS).
If a ventilation and air conditioning system (RLT) is available, its ventilation ducts must also be monitored. The HVAC system must be able to be switched off centrally by the BMZ in order to prevent the spread of smoke in the building.

It is important to ensure the correct installation of smoke detectors according to the manufacturer's specifications. Planning, construction and operation of a BMA are to be designed in accordance with DIN 14675 "Fire Alarm Systems - Construction and Operation" and agreed between the client, building supervisor, fire brigade and, if necessary, insurer.

If a fire alarm panel is present, all of its messages, including the fault messages on a constantly occupied place, eg. B. the porter's lodge, run up.

The functionality of all smoke detectors and all other components of a fire alarm system must be checked regularly. Sporadically, some of the detector lines should be manually tested for their functionality.

In the case of smoke detection, an alarm must be triggered in the building to ensure that all persons present in the building can perceive it.

In order to ensure a safe exit from the building, it must always be ensured that the intended escape and rescue routes are usable. They must not be restricted in their prescribed width by furniture or even electrical equipment such as copiers or printers which pose a significant fire load. The minimum width of escape routes in Germany is specified in the Technical Guideline for Workplaces ASR A2.3 "Escape Routes and Emergency Exits, Escape and Rescue Plan". It must be checked regularly that the escape routes are usable and free of obstacles.

#### INF.1.M5 Hand Fire Extinguisher

Most fires arise from small, at first still easily controllable fire herds. Especially in offices, the fire finds plenty of food and can spread very quickly. The immediate control of fires is therefore very important.

This immediate combat is only possible if hand-held fire extinguishers in the appropriate fire class (DIN EN 3 portable fire extinguishers) in sufficient number and size (advice from the local fire department) are available in the building.

All hand fire extinguishers must be regularly checked and maintained so that they work in case of emergency. A maintenance certificate must be kept about this. It is also important to ensure that fire extinguishers in areas with special access restrictions are not forgotten during such periodic inspections.
Powder extinguishers covering fire classes A (solids), B (flammable liquids) and C (gases) should not be used in areas with electrical and electronic equipment, as the damage caused by the damage is usually disproportionately high. It is therefore strongly recommended not to keep powder extinguishers in the immediate vicinity of server rooms, data carriers, rooms for technical infrastructure and data centers, but only suitable gas extinguishers. This is the only way to prevent a powder extinguisher from being mistakenly used in the outbreak of a fire. Incidentally, the appropriate manual fire extinguishers are to be defined in the fire protection concept, taking into account the predicted.

The fire extinguishers must be installed so that they are easily accessible in case of fire. Employees should memorize the location of the next fire extinguisher. The locations of extinguishers and hydrants must be marked by prescribed signs. Portable fire extinguishers are allowed up to a total weight of 20 kg. With the predominantly used devices of 6 and 12 kg, it is possible to extinguish larger sources of fire than are generally assumed by non-experts, but this is only possible if the extinguisher is used correctly. Only a few seconds pass until the extinguishing agent is completely discharged. Therefore, in appropriate fire safety exercises, the staff should be instructed in the use of hand fire extinguishers and the operation of the extinguisher also to practice.

#### INF.1.M6 Closed windows and doors [Staff]

Windows and outward-opening doors (balconies, terraces) must be closed in times when a room is not occupied. Exterior doors are to be completed. In the cellar and ground floor and, depending on the design of the façade, also on the higher floors, open windows and doors offer burglars ideal entry points, which are also used during the operating hours of an institution.

Employees should be advised that windows and doors should be closed when leaving rooms. If it is ensured during normal working hours that the rooms are only temporarily vacant, it is not necessary to have compulsory regulation of office space, meeting, event and training rooms.

No exception may be allowed for fire and smoke protection doors. These provide protection only when closed and must therefore never be kept permanently open by wedges or other devices (see INF.1.M3 Observance of fire protection regulations).

It makes sense if porters or employees of the building services regularly check whether the windows and doors were closed after leaving the rooms.

#### INF.1.M7 Access Control and Control [Head of Organization]

Access to parts and rooms requiring protection must be regulated and checked (see ORP.4 Identity and Permission Management). The measures range from simple key assignment to elaborate identification systems with individual separation.

For access control and control it is necessary that

* the scope of the regulation is clearly determined,
* the number of persons entitled to access is reduced to a minimum; these persons should know each other's authority in order to recognize unauthorized persons as such,
* the admission of other persons (visitors) takes place only after prior examination of the necessity,
* issued access authorizations are documented.
The granting of rights alone is not sufficient if their compliance or overrun is not controlled. The design of control mechanisms should be based on the principle that simple and workable solutions are often as efficient as expensive technology. Examples for this are:

* Information and awareness of the beneficiaries,
* Announcement of permission changes,
* visibly carrying house IDs, supplemented by the issue of visitor badges,
* Accompanying visitors,
* Behavioral rules when authorization violation is detected and
* Restriction of unrestricted access for non-authorized persons (eg door with blind knob, lock for authorized persons with key, bell for visitors).
Access control requires a variety of structural, organizational and personnel measures. Their interaction should be governed by an access control concept that defines the general guidelines for perimeter, building and equipment protection. This includes:

* Definition of security zonesProtected areas may include land, buildings, server rooms, peripherals, archives, communications equipment and home automation. Since these areas often have very different security requirements, it may be useful to divide them into different security zones (see INF.1.M 23 Formation of Security Zones).
* Assignment of access authorizations (see ORP.4 Identity and Authorization Management)
* Designation of a person responsible for access controlThis assigns the access rights to the individual persons according to the principles defined in the security policy.
* Definition of time dependencies It must be clarified whether time restrictions on access rights are required. Such time dependencies may be: access only during working hours, access once a day or temporary access until a fixed date.
* Specifying evidence retentionHere is to determine which data is logged when entering and leaving a protected area. It requires a careful balance between the security interests of the system operator and the protection interests of the individual's privacy.
* Handling of exceptional situationsAlso in exceptional situations, no unauthorized persons should be able to enter the building or the properties. However, the highest priority must be to ensure that all persons can leave the endangered zones as quickly as possible in case of fire.
In addition, the installation of card readers of various qualities, of locks and separating devices may be useful. For key management, see INF.1.M 12 Key Management.

In order to implement a more comprehensive concept, to maintain flexibility in use and to ensure transparency and verifiability, the use of an IT-based system for authorization management is recommended (see chapter 3.1 Access Control System and Authorization Management).

The access control terminals must be protected against manipulation. To do this, they must be placed in such a way as to guarantee confidentiality when entering data. In addition, all units required for data entry should be combined in one device, such as a keypad for PIN entry.

If not all units are in one device, the data transmission between them must be encrypted. So if z. B. non-contact card reader used, the data transfer between card and reader must be encrypted.

In operation, the effectiveness of all technical and organizational measures must be constantly monitored. It is advisable, especially at known problematic place to regularly check whether no opportunities have arisen to circumvent access control, z. B. in delivery or smoking areas.

#### INF.1.M8 smoking ban [employee]
First and foremost, a general smoking ban in buildings naturally serves non-smoker protection. In addition, it also has relevance in information security. Thus, tobacco smoke can damage sensitive IT equipment as well as the smoke of a fire. Therefore, and because of the additional risk of fire, a strict smoking ban should be observed in all IT operating rooms (server room, data carrier archive but also document archive etc.). This also serves the preventive fire protection as well as the operational safety of IT with mechanical functional units.

Unfortunately, the smoking ban in buildings creates a different risk from the outdoor smoking areas to be provided. It is common to find that external doors in areas that are sometimes difficult to see are always open, because the area close to the door forms the smoking area and the door is never closed during work hours for reasons of convenience.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "general building".

#### INF.1.M9 Safety Concept for Building Use [Planner, Information Security Officer (ISB)]

The prerequisite for the development of an effective security concept is the determination of the protection requirements of the business processes operated in a building and the definition of the fundamental protection goals, which often result from the business activity. Subsequently, a practicable and economical security concept for the use of a building will be developed. Taking into account the various safety aspects of a building, building on the protection objectives, appropriate safety measures should be established for the various areas while maintaining a defined safety level. It should be ensured that all accesses are so controlled and secured that no unauthorized persons can enter the areas to be protected.

This consideration must almost always be supplemented by further measures against unauthorized intrusion or creeping. An overview of this is the measure INF.1.M 27 Burglary Protection.

If the building has public or semi-public areas or if z. If, for example, it is possible to inspect the building through window fronts in the street area, the INF.1.M 16 must be checked to avoid damage to parts of the building.

Wherever the protection of the contents of the building, be it goods, be it the technical infrastructure, is particularly required, the security concept must consider the protection against water. Information on this can be found in measure INF.1.M 24 Automatic drainage.

All precautionary or damage-reducing measures coordinated with the protection objectives must be supplemented by measures to be taken (see S 1.18 Hazard warning system). The building protection concept is only complete if the relevant hazards are counteracted by planning and execution and if surveillance measures are taken to ensure that damage-causing events or accidental or intentional attempts to overcome protection and security measures are noticed as early as possible. Only then is it possible to take countermeasures.

The security concept for the building should be in line with the overall security concept of the institution. It should be regularly updated, especially if there are changes in the use of the building, such as organizational changes in the institution.

#### INF.1.M10 Compliance with relevant standards and regulations [installer company, site manager]
There are guidelines, standards and regulations for almost all areas of technology. These may have been issued by standardization organizations, industry associations, user groups or government institutions, eg. B. DIN (German Institute for Standardization), ISO (International Standards Organization), VDE (Association of Electrical Engineering, Electronics and Information Technology), VDMA (Verband Deutscher Maschinen- und Anlagenbau), VdS (Association of Property Insurers). These rules help ensure that technical equipment provides a sufficient level of protection for users and safety during operation.

The letter-faithful observance of standards alone does not lead to a significant improvement of the information security. The intelligent implementation of normative specifications, however, is an indispensable basis for all other safety measures. In the planning and construction of buildings, in their operation and conversion as well as in the installation of technical building equipment (eg internal supply networks such as telephone or data networks) and in procurement and operation of equipment, the corresponding standards and regulations must therefore be observed.

#### INF.1.M11 Completed doors [Staff]

The doors of unoccupied rooms should be locked. This prevents unauthorized persons from gaining access to the documents and IT equipment they contain. The completion of individual offices is particularly important if they are in areas with public access or access is not controlled by other measures.

It is not necessary to lock the doors if they have a blind knob on the side of the corridor. The prerequisite for this, however, is that the authorized employees always carry their keys with them.

Interior doors can also be escape doors. Escape doors must allow the doors to be opened by anyone at any time from the inside, as long as there are people on the inside. They must be secured in such a way as to prevent unauthorized access from outside to inside.

In some cases, for. For example, in open-plan offices, offices can not be completed. Then, as an alternative, each employee should close off his documents ("Clear Desk Policy") and the personal workspace before his absence: desk, cabinet and PC (activate access protection), telephone.

In meeting, event and training rooms, there is usually no way to include documents, IT systems and the like separately. Therefore, it should be possible to have such rooms, at least when all participants of an event leave the room, or have them supervised by an internal employee.

When the computer is running can be dispensed with the completion of the doors, if access is possible only after successful authentication, ie z. For example, a password-assisted screen saver is enabled. When the computer is switched off, it is possible to dispense with closing the office when booting the computer requires the entry of a password. The same function is fulfilled by access mechanisms based on tokens or smart cards.

It makes sense to have sporadic employees, such as gatekeepers or employees of the building services, check that the requirements for closing rooms and safe storage of confidential documents are adhered to.

#### INF.1.M12 key management

For all keys of the building (of floors, corridors and rooms) a locking plan has to be finished. The production, storage, administration and issuing of keys must be centrally regulated. Reserve keys are to be kept and stored securely. The same applies to all means of identification such as magnetic stripe or chip cards. Please note:
* If a locking system is available, separate locking groups must be set up for areas requiring protection. Depending on the requirements, individual rooms are to be taken out of the locking group and provided with individual locking.
* Unissued keys and the reserve keys are to be protected against unauthorized access.
* The keys are issued only in justified and comprehensible cases to authorized persons against receipt and must be documented. Even in the case of substitution, a key may not simply be passed on, but must be made via the key issue. Only through this detour can a complete documentation be provided as proof of the whereabouts of the key.
* Precautions are to be taken on how to respond to loss of individual keys (notification, replacement, reimbursement, possibly recourse due to lack of due diligence), replacement of the lock, replacement of locking groups, etc.).
* If roles or responsibilities of employees change, check their locking permissions and collect keys that are no longer needed.
* When leaving employees, all keys must be collected (inclusion of the key management in the slip of the stations to be done before departure).
* Locks and keys to vulnerable areas (where very few keys should be issued) can also be exchanged, if necessary, without prior notice in case of suspicion, in order to prevent the use of unauthorized keys / locking devices.
#### INF.1.M13 Regulations for access to distribution boards

Wherever possible, the distribution boards (eg for energy supply, data networks, telephony) must be accommodated in rooms for technical infrastructure (see building block INF.5 Room for technical infrastructure). The safety requirements listed there must be taken into account.

Access to the distributors of all utilities (electricity, water, gas, telephone, hazard notification, district heating / cooling, etc.) in a building must be possible and orderly. By possible is meant

* that distributors are not glued with paints or wallpapers so that they can only be opened with tools or can not be found,
* that distributors are not delivered with furniture, equipment, pallets, etc.
* that for locked distributors the keys are available and the locks work.
By ordered is meant that it is defined who may open which distributor. Distributors should be closed and may only be opened by the persons responsible for the respective utility. The access options can be regulated by different locks and a corresponding key management (see INF.1.M 12 Key Management and Chapter 3.1 Access Control System and Authorization Management).

If fuses are installed in distributors of the power supply network, appropriate spare fuses (in the distributor) should be available. A documentation of the distributors must be carried out according to INF.3 Electrotechnical cabling.

All devices installed in the distributor must be labeled exactly and permanently. This label must be affixed in such a way that even with removed covers, each installation element can be identified with immediate safety.

#### INF.1.M14 Lightning protection devices

The direct effects of a lightning strike on a building (damage to the building structure, fire, etc.) can be prevented as far as possible by installing a suitable lightning protection system. However, since it is not the task and function of "external lightning protection" to protect the electrical equipment in the building, an "internal lightning protection", ie the overvoltage protection, is also required (see INF.3 Electrotechnical cabling).

**Example:**
Due to lightning, a damage to IT equipment (PCs, servers, laser printers) in the amount of approx. 10,000 euros arose in the southern German branch of a service company. Due to this event, the building was equipped with external lightning protection without internal lightning protection (surge protection). A renewed lightning strike led to damage in almost the same height despite external lightning protection.

Since 2006, the standard DIN EN 62305 "Lightning Protection" (corresponds to the standards VDE 0185-305 and IEC 62305) has reorganized the entire lightning and surge protection since 2006.

Each institution should create a lightning and surge protection concept based on the new standard DIN EN 62305. In Part 2 "Risk Management", this standard describes for the first time generally binding the way to a risk-oriented lightning and surge protection. Part 3 deals with the "protection of structures and persons", ie external lightning protection.

The external lightning protection, the catching device (vulgo lightning conductor), is divided into four protection classes (also known as Lightning Protection Level, LPL for short) in terms of their effectiveness. The protection class IV (LPL IV) has the lowest protection value, while the protection class I offers the best protection. Easily distinguishable difference between the 4 protection classes is the mesh size of the capture devices. This ranges from 20 x 20 m for the protection class IV in 5 m steps down to 5 x 5 m for the protection class I. For buildings with extensive IT equipment, the catcher should at least comply with the protection class II, better protection class I.

The impressed lightning current that flows out through the catching device for grounding causes a voltage decreasing along the catching device from the point of impact of the lightning to the grounding point. At the highest point of the catching device, this voltage can be a few 100,000 volts. It should therefore be noted that especially in the upper floors of a building galvanic installations (data, electricity, water, etc.) must have a sufficient distance from the capture devices. Also this aspect is considered under the designation separation distance in the new standard. With considerations to protect against compromising coupling that has nothing to do, even if the aspect of the separation distance has often been wrongly equated with the protection against coupling of the lying close to the lightning arrester data lines on the lightning rod.

Since the voltage drop along the arrester at the grounding point never drops to 0 V due to the remaining earth contact resistance and the base of the arrester must be connected to the main equipotential bonding of the building, the entire PE system of the building and thus also the N conductor will be at this residual voltage raised. Here are voltages in the range of at least well over 10,000 volts expected. Thus, voltages between N / PE conductors and the conductors L1 / L2 / L3 are achieved, which significantly exceed the usual operating level of 230/400 V. In order for these voltages not to damage the electrical equipment operated within the building, the internal lightning protection, ie the overvoltage protection, must be built as an indispensable consequence of the structure of the external lightning protection (see INF.3 Electrical wiring).

The entire lightning protection system must be checked regularly. Safety equipment of protection classes I and II shall be subjected to a visual inspection every year and to a full inspection every 2 years. For protection classes III and IV, 2 or 4 years are planned here. For critical systems, such as those for the protection of highly available or highly available facilities, a comprehensive audit must be carried out annually. Detected defects must be remedied immediately. It goes without saying that the execution of the test, the findings made as well as any remedial work carried out must be documented in writing.
#### INF.1.M15 Location plans of utilities

Site plans identify the supply lines (electricity, water, gas, telephone, hazard notification, air conditioning, etc.) of a building and of buildings in a visual form, ideally with an explanatory written part. Up-to-date and well-maintained plans make it possible to prepare work in the area of ​​pipelines so that they are not damaged and, in the event of damage, to quickly and simply get an accurate picture of the situation, to quickly locate damaged areas so that faults can be remedied more quickly. Therefore, accurate and up-to-date maps of all supply lines, including all issues concerning the pipelines, should be kept in the building and on the associated property. This includes:

* precise guidance of the lines (marking in dimensioned floor plans and site plans),
* exact technical data (type and dimensions),
* possibly existing marking,
* Use of the lines, naming the connected network participants,
* Danger points and
* existing and tested security measures.
All work on pipes should be fully and promptly documented. The plans should be kept secure and stored in such a way that only authorized persons can access them, but at the same time they are quickly available when needed.

#### INF.1.M16 Avoidance of position information on parts of buildings that are to be protected

In each building there are areas with different usage scenarios and different protection needs. Protective building parts are z. Eg server room, data center, data carrier archive, climate control center, distribution of power supply, switch and maneuvering rooms, spare parts warehouse.

Such areas should not bear any indication of their use. Door signs such. B. DATA CENTER or ARCHIVE give a potential attacker, who has access to the building, hints, in order to be able to prepare his activities more purposefully and thus more successfully.

If it is unavoidable to store business-relevant information or IT in rooms or building areas that are easily visible to outsiders (see also INF.1.M 34 Arrangement of buildings worth protecting), appropriate measures must be taken to prevent the glimpse or so to make sure that the use is not revealed. It is important to ensure that z. B. not only a window of an entire floor is provided with a privacy.

#### INF.1.M17 Structural smoke protection [Planner]

In fires, smoke is the greatest risk to people. More than 90% of the deaths are due to smoke (poisoning). But also the IT hardware can be significantly affected by smoke. Therefore, value should be attached to comprehensive smoke protection.

The following recommendations should be considered for smoke protection:

* Fire doors should be smoke-proof, recognizable by the abbreviation "RS" in the type designation of the door.
* Smoke doors in corridors should be controlled by smoke switches. Such doors can always be open, as they close automatically when smoke is detected.
* Rapid smoke extraction from IT rooms must be possible.
* In air ducts (supply and exhaust air), duct detectors should be installed. In the fresh air intake, detectors should be installed, which automatically lock them when disturbances (smoke) are detected.
After installation and alteration work, it must be ensured that smoke protection measures have remained effective or have been restored.

Employees must be informed of the warning signals the smoke protection components have and how to react.

The functionality of all smoke protection components must be checked regularly. This also includes checking that breakthroughs have been effectively sealed to make wiring in raised floors and in suspended ceilings.

#### INF.1.M18 fire safety inspections
Fire safety inspections are intended to reveal weak points in preventive fire protection and they help raise awareness of how to establish preventive measures.

On-site visits should focus on typical vulnerabilities, such as the accumulation of flammable or explosive substances outside designated warehouses and containers, or storage of paper supplies or furniture within engineering and server rooms (not infrequently, these accumulations exceed allowable fire loads or obscure escape routes). It checks to see if smoke detectors are functioning, fire compartment or smoke control doors are kept open by wedges, fire barriers have been opened and / or even damaged during work, and have not been properly restored. In addition to announced unannounced inspections should also be made, findings recorded and defects rectified immediately.

Since the actions of the employees are usually determined not by malicious intent, but by the operational necessity or convenience, it can not be a sense of fire prevention, to find and punish perpetrators. Rather, the defects found should give rise to promptly correct the conditions and their causes.

#### INF.1.M19 Early information from the fire safety officer

For all work on pipe and cable ducts which in any way touch wall penetrations as well as necessary corridors, escape and rescue routes, the fire protection officer must be informed. This information must be given so clearly in advance of the actual work that the fire protection officer has ample opportunity to incorporate all aspects of constructive preventive fire protection in the planning and execution of the intended work.

The fire safety officer must be given the opportunity, even while the work is in progress, to provide timely information to monitor the proper execution of fire protection measures or to arrange for such control before they become inaccessible as a result of the construction progress, eg. B. because a suspended ceiling has already been closed.

The involvement of the fire protection officer is to be ensured by appropriate organizational instructions and documented in the planning and acceptance documents of the construction measure (see also INF.1.M 3 Compliance with fire protection regulations).

#### INF.1.M20 Alerting plan and fire drills

It is necessary to draw up plans for the measures to be taken in case of fire. In such a plan is z. B. to lay down,

* which measures have to be taken at which events,
* if and how parts of the building may need to be cleared (persons and equipment),
* who is to inform and
* which helping forces are to be informed.
The alerting plan can be supplemented with behavioral rules for the case of fire, to be announced to all employees. See also module DER.4 Emergency Management.

However, the best alerting plan is of little use if there is no assurance that the measures listed therein are correct and workable. It is therefore necessary to regularly check and update the alerting plan. One of these test measures is the performance of fire safety exercises.

**Example:**

* A fire drill conducted in a 21st floor Bonn office building showed that many employees did not know where a fire extinguisher or where the nearest stairwell is. In an emergency, this ignorance can lead to disaster. Partly the exercise was ignored, one did not leave the room for convenience.
Especially in fire safety exercises the correct behavior in case of fire should be trained and practiced to protect human life and damage u. a. for the IT to avoid. The execution of such exercises must first be agreed with the authorities or company management.
### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### INF.1.M21 Independent electrical supply strands (A)

As soon as high or very high demands are placed on the availability of IT, it is sensible and appropriate for IT to be supplied via two independent electrical supply lines and for the use of IT devices with two power supplies.

The important consumers (central storage components, network nodes or servers) are connected to the independent supplies "grid 1" and "grid 2" (also called "A-B supply") (see figure). Other IT components, to which only a few high demands are made, are evenly distributed to the supply lines.

Independent electrical supply lines

In this case, it must be ensured, especially with devices that are simply connected, that devices that provide each other with redundancy are not connected to the same supply. In addition, the devices must be distributed evenly according to their power consumption on both strands.

#### INF.1.M22 Safe Doors and Windows (CIA)

If doors and windows form a transition between security zones, they must provide adequate protection. An outside door must z. B. protect against burglaries, as well as the achievable windows must be secured. In the interior, doors that form the boundary of a fire compartment must themselves be fire-resistant, and they or other interior doors can form a second line of burglary protection.

Security doors and windows are classified in standards. The protection objective of the area to be protected and the need for protection of the institution make it possible to select the appropriate design of doors and windows:

* In the standard DIN EN 1627: 2011-09 "Doors, windows, curtain walls, grid elements and terminations - burglary resistance - requirements and classification", the components have been classified in resistance classes (RC, English Resistance Class). Due to their stability, doors according to the classifications RC1 to RC4 offer a higher protection against burglary (eg in server rooms, rooms with technical infrastructure as well as in cellar and supplier entrances). The resistance classes RC5 and RC6 are usually appropriate only for very specific requirements and therefore play no role in IT-Grundschutzbetrachtungen.
* Self-closing fire-retardant and possibly smoke-tight doors (eg fire doors T30 or T30-RS, according to DIN 18082 "fire protection shutters") delay the spread of fire and in the RS version smoke.
In the design as a self-closing smoke protection door (DIN 18095-1 "Doors; Smoke protection doors; Terms and requirements") they protect the spread of fire smoke. Fire smoke is so fine-grained that it easily passes through pressure equalization and ventilation holes of hard drives. However, it is still too big for the low altitudes of hard disk read heads and causes enormous damage there.

It can also be combined several protective properties in a door, there are, for example, smoke-tight fire doors, which also provide protection against burglary.

The safety measures of all room enclosing components must be equivalent:

* When using burglary-resistant doors, the use of burglar-resistant windows or facade elements (see DIN EN1627-1630: 2011 "Doors, windows, curtain walls, grille elements and barriers - Burglar resistance") must be considered in the façade area.
* Furthermore, it is z. B. not appropriate to install a burglar-resistant door of the highest resistance class in a plasterboard wall.
* When installing a fire-retardant or smoke-tight door, make sure that the surrounding wall is equally fire-retardant and smoke-proof, and that there is no bypass through open skylights or un-sealed cable glands.
Requirements for the execution of security doors can be found in INF.2 Rechenzentrum and INF.1.M 27 Burglary Protection.

The use of security doors in terms of fire protection beyond the area prescribed by the building inspectorate and the fire department (see INF.1.M 3 compliance with fire protection regulations) especially in vulnerable areas such as server room, document or data carrier archive makes sense. In the case of rooms requiring a high level of protection, a balanced protection concept must be created, which takes into account the installation of security doors and the notification of danger and alerting for checking and intervention. If a potential attacker has time for a break-in attempt over a whole weekend, even a high-quality burglar-resistant door will not prevent him from stealing or destroying data or equipment.

For the equipment of data centers, the resistance class RC3 according to DIN EN 1627-1630: 2011 should be used as the minimum value for the doors including their installation situation. Only if there is a particularly favorable condition for safety, especially if the intervention time of assisting forces is short (maximum 2 minutes), can an RC2 door be sufficient in exceptional cases. On the other hand, if the intervention time of assistants is 5 minutes or more, even an RC3 door can be considered inadequate and the installation of RC4 doors is recommended. Naturally, the same considerations also apply to all other components forming the RZ shell.

** Note: ** A burglary could also be to manipulate data or IT systems. For this reason, central IT systems should be checked for their integrity after break-ins (see also S 6.60 Definition of reporting procedures for security incidents).

It must be ensured that fire and smoke protection doors are actually closed and not (inadmissibly) z. B. be kept open by wedges. Alternatively, doors with an automatic locking mechanism activated in case of alarm can be used.

In addition, check regularly that the security doors and windows are functional. They must be in a proper mechanical condition, safely open and close, and monitoring installations such as make contacts must operate.

#### INF.1.M23 Formation of Security Zones [Planner] (C)

The need for protection of rooms in a building depends on their use. The required security measures must be adapted to this protection requirement. Accordingly, the structural design of walls, windows and doors must be and the complementary equipment with security and surveillance technology. Therefore, when planning a new building or evaluating an existing building, rooms with similar protection needs should be zoned together. This means that comparable risks can be treated uniformly and the costs of implementing measures are reduced.
To z. For example, if you do not need to permanently lock or monitor every single room in the building, areas with visitor traffic should be separated from areas that need to be protected. Public spaces such as a canteen that attracts external audiences, or semi-public spaces such as meeting, training, or function rooms should be located near the building entrance. Access to parts of buildings with internal areas such as the offices can then z. B. be easily monitored by a gatekeeper. Particularly sensitive areas such as a development department, rooms of building technology or IT rooms should be secured with an additional access control.

For physically securing a building and, if applicable, the surrounding property, it has proven useful to plan and implement a security concept with depth-restricted security measures (onion shell principle). Proven is a division into four security zones, outdoor area, controlled indoor area, internal area and high security area:

Figure: Formation of security zones

The security zone 0, ie the outdoor area, is encompassed by the property boundary. If the situation permits, this legal limit should be clearly indicated by an enclosure. The first access and access control can already be done here. Public building areas belong to this zone.

The security zone 1 is the controlled interior area. Through an appropriate access control, z. As a janitor or an access control system, only authorized persons (employees, invited visitors) gain access to this zone. If there is a high need for protection, there should already be an obligation in this zone to always carry visible badges. The outer skin of zone 1 (external building skin) should be protected against sabotage and burglary by structural and technical measures.

Zone 2 as an internal area can only be accessed by a restricted circle of authorized persons. There are defined access authorizations here. Zones or sections of buildings in zone 2 should have only one access at a time. Further access roads serve exclusively as escape and rescue routes and must always be kept closed during operation. They must be permanently monitored and secured against misuse by electromechanical safety devices (emergency exit systems).

Zone 3 forms the high-security area (eg board areas, critical IT rooms). The circle of authorized access is very limited. The security measures should be correspondingly high. Example: Access is only possible via a security gate with two-factor authentication and separation, exit with one-factor authentication and separation. There is an accounting of the access, as soon as no persons are reported more than present, the automatic arming of the burglar alarm system takes place.

Post offices, delivery and loading zones should be in security zone 1. They should be designed so that deliveries can be accepted without the suppliers having to enter further areas of the building. The doors in these areas should not be left open for a long time. For higher protection needs, either only the outer door or the door should open to the inner areas. Incoming deliveries should be examined in the delivery zone to determine whether or not they could be associated with risks. The type and depth of the reviews depends on the respective hazard potential (eg letter bombs). Incoming and outgoing deliveries should be kept as separate as possible.

#### INF.1.M24 Automatic drainage (A)
All areas within buildings where water can collect and accumulate, or where running or stagnant water is not detected, or discovered late, and where the water can cause damage, should be equipped with automatic drainage and water detectors. These areas include u. a .:

* Basement, cellar,
* Airspaces under raised floors,
* Light wells,
* Heating system.
If the drainage is passive, ie through floor drains directly into the sewage system of the building, backflow flaps are essential. Without such flaps, this drainage becomes the water inlet when the sewage system becomes overloaded. After extreme precipitation, in the majority of cases, water penetrates this way into cellars. The backflow valves must be checked regularly for their proper functioning.

If passive drainage is not possible because the level of the sewage system is too high, pumps can be used which are automatically switched on via float switches or water sensors. When using this technique, the following points should be noted in particular:

* The pump capacity must be sufficient.
* The pressure line of the pump must be equipped with a backflow valve.
* Precautions must be taken so that the pump can not be blocked by objects washed in with it (suction filter, etc.).
* Starting the pump should be indicated automatically (eg by the caretaker or the building service).
* The function of pump and switch should be tested regularly.
* The pressure line of the pump must not be connected to a sewage pipe in the immediate vicinity. In the event of a leak in this line, the pump would only pump the water "in a circle".
To prevent water z. If, for example, heavy rain enters the building from the outside, the condition of the site drainage must also be checked and, if necessary, repaired. If the location or profile of the property involves special risks to the building due to surface water, the installation of special water protection doors may be considered.

#### INF.1.M25 Suitable location selection [Institutional Management] (A)

When selecting and planning the location where a building is to be rented or created, it is advisable to take account not only of the usual aspects such as space requirements and costs, but also of environmental conditions that have an impact on information security:

* In connection with weaknesses in the building fabric, it can come to disruptions of the IT by shaking close traffic routes (road, rail, subway).
* Buildings located directly on major traffic routes (railways, motorways, main roads, airports) can be damaged by accidents.
* The proximity to optimal traffic and therefore escape routes can facilitate the execution of a stop.
* There may be disruptions to IT near broadcasting equipment.
* IT can be disrupted near railway lines.
* Flooding is likely near rivers and in lowlands.
* In the vicinity of power plants or factories, the availability of the building (eg by evacuation or large-scale shut-off) may be affected by accidents or breakdowns (explosion, discharge of harmful substances).
It may also be possible to avoid hazards from the neighborhood z. B. to compensate by appropriate arrangement worth protecting building parts. This should be taken into account in the selection and planning.

The location-related hazards and the necessary damage prevention or reduction measures should be documented in the safety concept. In addition, they should be included in the emergency concept.

#### INF.1.M26 porter or security service (CIA)
The establishment of a porter or security service has far-reaching positive effects against a whole series of threats. However, a prerequisite is that some basic principles are observed when carrying out the porter or security service. Naturally, the focus of the porter service is to control access during business hours, while security services monitor and secure the property, especially outside business hours.

* The gatekeepers should observe and control all movement of persons at the gate and at all other entrances.
* Supported by video surveillance, remote doors and gates can be monitored and controlled by the gatekeepers (see chapter 3.2 Video surveillance).
* The gatekeepers must be familiar with the employees. It is recommended that well-known persons legitimize the gatekeepers, so z. B. show a house card. If an employee leaves the institution or changes his / her position within the institution, the gatekeepers must also be informed as of when this employee is to be refused admission or if access authorizations change.
* Unknown persons ("even the new boss") have to identify themselves with the gatekeepers.
* In a visitor's book the access of foreign persons to the building can be documented. Issuance of visitor badges or visitor tickets is to be considered.
* Visitors should be accompanied to the visitors or picked up at the gate. If visitors are allowed to enter the building unaccompanied, it must first be verified that this is possible without any security concerns. The respective framework conditions must be documented in advance. For example, a list could be kept of trustworthy long-stay visitors who are allowed to enter the building unaccompanied after receiving a visitor's badge.
* When the gate is open 24 hours a day, alarming and supervising technology may always or only outside normal working hours accumulate. On the basis of alarm lists for the messages, the gatehouse forwards the messages to responsible employees or external authorities in charge.
The working conditions of the gatekeepers and the security personnel are to be designed for the task perception. The task description must stipulate bindingly what tasks the janitors or employees of the security service play in conjunction with other protective measures (eg building security after business or office hours, arming of the alarm system, control of exterior doors and windows).

When defining the tasks, it must be taken into account that the assigned tasks do not open any security gaps. If a gate is occupied by only one gatekeeper and he has no opportunity to temporarily close the gate, he may not be instructed or allowed to accompany visitors to certain visitors.

In many institutions, porter and guard services are provided by external security service providers, see OPS 4.2 Other Services.

#### INF.1.M27 Burglary Protection (CIA)

According to experience, burglars select their goals according to how high the risk and effort in relation to the expected profit. Therefore, all anti-intrusion measures should aim at minimizing perpetrators' chances of success. The usual anti-burglary measures should be adapted to the local conditions. This includes:

* burglary-resistant doors and windows, for example with resistance class RC2 (according to DIN EN 1627: 2011-09 "Doors, windows, curtain walls, grille elements and closures - burglar resistance - requirements and classification") or higher, if the risk situation makes it necessary
* Blinds on entry-level doors or windows,
* special lock cylinders, additional locks and latches,
* Securing basement light shafts,
* Closure of unused side entrances,
* burglar-proof emergency exits,
* Closure of passenger and goods lifts outside of service.
Recommendations are given by the local counseling centers of the Kriminalpolizei.

All anti-burglary measures should meaningfully form an end-to-end cover around the area that is to be protected against unauthorized access. Doors should be installed in sufficiently solid walls. Ventilation openings are to be barred in suitable form (maximum grid width 10x20 cm). Measures for access protection are also to be implemented in raised floor areas and above suspended ceilings. The equivalence and consistency of protection against burglary should be assessed regularly by a competent person during planning, during implementation and later during operation.

When planning material security measures, it must be ensured that provisions of the fire and personal protection, eg. As the usability of escape routes, not be violated. This applies in particular to changes to fire protection elements subject to type approval.

Employees must be informed about which regulations and measures for burglary protection must be observed, for example, that doors, windows or shutters must be locked in the evening.

Even within a building, the installation of anti-burglary elements may be useful. Hedging should be considered for special access-controlled areas such as executive offices, server rooms or the core units of a data center.

#### INF.1.M28 Air conditioning for people (IA)

In larger buildings, the air supply should be provided by ventilation and air conditioning (RLT) systems. HVAC systems provide for the transport (ventilation) and the conditioning (air conditioning) of the air. RLT systems should create a climate favorable to people. In addition, they must ensure a hygienically perfect quality of the indoor air. This means that the air treated by an air-conditioning system does not endanger the health or disturbances of the condition, it does not cause odor nuisance and the thermal comfort is maintained.

A good air quality can not be generated exclusively by the air conditioning system. When choosing construction materials, floor coverings and furniture, attention must also be paid to the use of materials that do not additionally and unnecessarily pollute the room air with pollutants.

The planning of state-of-the-art ventilation and air conditioning systems for non-residential buildings is described in DIN EN 13779 "Ventilation of non-residential buildings - General principles and requirements for ventilation and air conditioning systems and room cooling systems". Together with the workplaces ordinance, it determines in which rooms of the building which air quality requirements are to be met. DIN EN 13779 contains detailed specifications for

* the operative temperature
* the draft risk
* the relative humidity of the room
* the weighted sound pressure levels
* and other factors relevant to humans.
While there are high demands on air quality for offices and other permanently occupied rooms, the demand in rooms that are not always occupied is lower. It is therefore all the more important that, as required by the standard, the specifications for climate planning are specified by the client or the future user.

While cold is almost never a problem in creating a comfortable indoor climate, summer heat can be a bigger problem. The Workplace Ordinance calls for health-friendly room temperatures and protection against excessive sunlight for work rooms. To maintain a tolerable indoor climate on warm summer days, the RLT system must be supported by an effective shading of the windows.
RLT systems must be regularly maintained. Maintenance of HVAC systems not only helps to ensure reliable operation, but also to guarantee hygiene and thus the health of all users of the building. The maintenance of maintenance intervals and the careful execution of cleaning and filter changes must be controlled and documented.

RLT systems must not be accessible to everyone and may need to be protected against sabotage. The ventilation and air conditioning systems must also be taken into account in emergency planning (see building block DER.4 Emergency Management), especially during shutdown and restart planning.

#### INF.1.M29 Organizational requirements for the cleaning of buildings (CIA)

The execution of cleaning work is almost exclusively entrusted to external companies, see also OPS.4.2 Other services. The cleaning personnel, who are not part of their own institution, must enter all rooms and areas of the building, including parts of buildings such as technical rooms or boardrooms, to which only certain employee groups have access. Furthermore, the external cleaners often use their own equipment and bring depending on the contract also with detergents and other consumables. This creates weaknesses, as for example internal material could be taken on the way back.

In addition to the general characteristics of a service specification for cleaning work such as type, name and location of the object, room usage groups, current room directories as well as the individual service types are to be described in detail. Activity types can be z. As the cleaning of non-textile and textile coverings, the cleaning and care of objects of interior design and furnishings as well as disposal tasks. Building on this, the individual requirements are described with details of the scope in the individual rooms.

In order not to disturb the work process, cleaning work is often moved to non-working hours. But this also has to clarify whether the cleaning staff should be supervised. Ideas for the cleaning times as well as the special treatment of individual particularly vulnerable and not uncontrollably accessible areas are to be listed in the service description.

Cleaning staff should be briefed on the tasks before starting their work. This includes, above all, instruction on which areas may be accessed under what conditions, how IT systems are to be cleaned and what needs to be observed in the environment of IT systems and how they deal with confidential information that they receive during their work , This can z. For example, documents found on desks or in baskets, or conversations overheard.

The entry of cleaning personnel can be particularly problematic in areas with higher security requirements such as data centers, server rooms, technical rooms or communication centers and therefore require additional security measures. In such areas, it may be useful to check the trustworthiness of the cleaning staff or to supervise them during their work.

If there is confidence in the cleaning company, the access of the cleaning staff should be regulated via the existing access control or the locking system. However, this can only be an effective safeguard if z. B. ID card or key against signature and only temporarily issued to named and known employees of the cleaning company. In the agreement on the use of permanent staff, the identification system can provide effective control of compliance.
For the coordination, but also in the case of occurring problems, the contractor must name an object manager who can be addressed at any time. He must have decision-making authority over the to be used (above all also about not more to be used, because unwanted) personnel.

The special treatment of sensitive areas should already be included in the invitation to tender and the contract formulation. For example, at data centers, random checks of bags or cargo in the access or access area for non-farm personnel should be included in the contracts.

As cleaning staff can not be expected to be IT savvy, they should therefore be trained in all areas of business-critical IT systems to determine which activities could damage IT equipment or IT operations. Examples of such problem areas are:

* When cleaning keyboards, unintentional input to servers or other key components can interfere with IT operations.
* IT systems can be turned off accidentally.
* Power or communication cables may be damaged by vacuum cleaners or torn from the endpoints.
* Water or cleaning fluid can cause short circuits in hardware components.
Areas with an increased need for backup such as machine room or data carrier archive are only in the presence of persons responsible of the client or in some cases also in the presence of a trusted person of the contractor, eg. B. in the four-eyes principle to clean.

#### INF.1.M30 Selection of a suitable building (CIA)

In addition to site planning (see INF.1.M 25 Site Selection), which looks at the environment of a building, a building must be assessed for its internal suitability. In principle, of course, it must be checked already during the building selection whether all measures relevant for the subsequent use can then also be implemented.

For some of these measures, however, the prerequisite can only be created later with great effort or not at all. Therefore, this measure should help in the selection of an existing building, typically to avoid problems occurring later in advance as far as possible. But it can also be helpful when planning a new building.

Individual aspects vary depending on whether the building is purchased or rented. From the point of view of information security, the following must be considered, among other things, with regard to the condition of the building fabric:

* Does statics (maximum ceiling load, load-bearing walls) enable the installation of high-load space (server room, DC, UPS, etc.) where they would be useful in terms of work economy and information security (see also INF.1.34 Arrangement of buildings worth protecting) ?
* Can the existing or additionally required access routes (corridors, staircases, elevators) be used and set up so that measures such as: B. INF.1.M7 access control and control are also meaningful implementation?
* Is it possible due to the development paths to separate areas with high security requirements from those with low, so that z. B. Training rooms outside of sensitive areas like product development?
* Can existing or additionally required access routes (corridors, staircases, elevators) be used at any time to transport even larger IT components? If this is not guaranteed, the restart after a hardware damage can possibly be delayed considerably.
* Are there (construction) conditions (rights of way, monument protection, etc.) that can hinder a needs-based use of the building? Particular attention must be paid to third-party rights of way, as these can collide with the necessary access-protected areas.
* Is a distribution of space possible, so that the INF.1.M 3 compliance with fire protection regulations can be implemented?
* Can INF.1.M 2 be adapted to circuit layout and INF.4 IT cabling?
Is there an external lightning protection? If so, it affects the details of the implementation of the requirements INF.3 Electrotechnical cabling and INF.4 IT cabling.
For rental properties, the following additional aspects must be considered:

* Does the tenant receive all the rights necessary for the proper construction of the building? Which rights and opposition options does the landlord reserve?
* Do safety devices have to be dismantled after the end of the lease? It must be ensured in the planning phase that due to such additional costs no necessary safety measures are waived.
* If the building is used by third parties at the same time, it must be clarified to what extent the implementation of measures is hindered or even prevented.
* As a tenant, do you get a say in a later re-letting of third-used parts of the building? It may well be that a new co-user of the building must be considered more safety-critical than the previous example. The human resources department of a small textbook publisher is moving out and as a tenant a politically or socially highly controversial organization is setting up an office there.
It should be documented, which safety requirements were considered in the building selection. In particular, any potential security risks and the measures taken to prevent or mitigate them should be noted.

#### INF.1.M31 Extract from Buildings [Inner Service] (C)

If a building is cleared in whole or in part because of moving out, the following things should be noted:

* In the run-up to the extract, an inventory of all things relevant to information security (hardware, software, data media, folders, documents, etc.) must be compiled.
* Each employee must be informed in writing of the things he is responsible for. This avoids that an employee cares about his own things well, things for the supposedly someone else is responsible, however, remain lying.
* Old equipment, data carriers, etc., which are no longer required, must be disposed of in accordance with OPS.1.1.8 Erasure and destruction prior to removal. Under no circumstances may old equipment be left behind, even if the landlord, tenant or buyer requests their further use or promises disposal.
After completing the excerpt, all rooms must be checked to ensure that no safety-critical items have actually been left behind. Things are often forgotten, especially in remote storage areas such as cellars and attics. All objects of professional use must be collected, removed and, if necessary, subsequently disposed of safely.
The safety recommendations for removals from ORP.1 organization should be considered.

#### INF.1.M32 firewall cadastre (A)

There should be a firewall cadastre that meets at least the following requirements:

* In the cadastre, all bulkheads are to be included, that is, pure cable ducts, pipe bulkheads, combination bulkheads, etc.
* Each firewall in the building or in the property must be managed individually in the cadastre (the inclusion of bulkheads in the cadastre can be dispensed with for those bulkheads whose failure demonstrably has no detrimental effect on the IT operation of the building or the property. )
* Each firewall is listed in the cadastre under an individual unique identification. This identification must be affixed in the immediate vicinity of the relevant bulkhead (as far as possible on both sides) in a legible manner.
* In the cadastre for each bulkhead individually the proof of at least annual visual inspection with the resulting findings is to lead.
* In the cadastre are for Schotts, which are already installed at the time of the creation of the cadastre, all available information structured, so at least:
* Installation location
* Manufacturer of the bulkhead
* Product name
* the general building inspectorate approvals (AbZ) valid at the time of construction or the general building inspectorate test certificates (AbP). These AbZ and AbP are usually valid for only 5 years and will either be extended or canceled. Often it is very difficult to find references to expired AbZ or AbP on the Internet.
* Installation date
* Installation company and a current photo of both sides of the built-in bulkhead.
In the case of existing bulkheads, it may be imperative in individual cases in the case of unclear circumstances to replace it with a new one. The following specifications apply to such a bulkhead:

* For all newly installed or altered bulkheads after the first compilation of the land registry, at least the following additional information must be included in the land register:
* Complete photo documentation of all essential single steps of the installation or conversion, reason of the conversion,
* Proof that the materials used in the conversion are approved by the manufacturer of the bulkhead for the conversion.
* All entries in the cadastre must be made immediately, at the latest 4 weeks after completion of the work.
After a conversion, the old certificate at the place of installation must be clearly marked as invalid but so that you can still read all the relevant technical information and supplement it with a new certificate that takes into account the conversion.

#### INF.1.M33 Arrangement of protected buildings (CIA)

Protected rooms or parts of buildings should not be located in exposed or endangered areas:

* Basements may be endangered by water.
* Rooms on the ground floor - towards public traffic areas - are endangered by attacks, vandalism and force majeure (traffic accidents near buildings).
* Rooms on the ground floor with poorly visible courtyards are at risk of burglary and sabotage.
* Well-visible rooms on the ground floor or in public areas are at risk as it may allow for spontaneous theft or unwanted insights into business-related information.
* Rooms below flat roofs are endangered by the ingress of rainwater.
* Underground parking can bring with it a whole range of risks: poorly visible rear entrances, open access supply lines or IT cabling, but they also often offer unauthorized persons access to insufficiently secured WLANs from their cars. From the point of view of fire protection, areas in underground garages are also problematic, which are misused as storage space.
As a rule of thumb, one may say that vulnerable rooms or areas are better located in the center of a building than in its exterior.

It is best to include these aspects in the construction planning for a new building or in the occupancy planning when moving into an existing one. For existing buildings, a corresponding usage arrangement will often be associated with internal moves. As a substitute, the opportunities arising from already required changes of the room occupancy should be used consistently.
If spaces requiring protection can not be arranged differently than in an exposed position, this should be documented explicitly in the security concept. In addition, additional compensatory measures must be taken to counteract the particular risk. So z. For example, in electrical basements or IT rooms in the basement an existing risk of water can be controlled by comprehensive water detection, threshold formation and preparation of drainage measures.

#### INF.1.M34 Hazard Alarm System (A)

A hazard warning system (GMA) consists of a large number of local detectors that communicate with a control center that also triggers the alarm. If a security alarm system for burglary, fire, water or even gas is available and can be expanded with reasonable effort accordingly, at least the core areas of IT (server rooms, data storage archives, rooms for technical infrastructure, etc.) should be included in the monitoring of this system be involved. In this way, hazards such as fire, burglary, theft can be detected at an early stage and countermeasures initiated.

To ensure this, the forwarding of messages to a permanently staffed office (porter, security and security, fire brigade, etc.) is inevitable. It must be ensured that this body is also able to respond technically and personally to the alarm. In this case, the switch-on guidelines of the respective institutions and the requirements of DIN EN 50518 "Emergency call and service control centers" must be observed.

A concept for hazard identification, forwarding and alerting should be established for the different areas of the building. This must be adapted to changes in usage. A hazard detection system is a complex overall system that must be planned and installed according to the building and the risk. Planning, installation and maintenance of a hazard detection system should therefore be carried out by experts. If these are not available in-house, external support should be used. For example, there are a variety of different reporting systems, which must be selected according to the security requirements and the environment. For burglary detection z. As motion detectors, glass breakage sensors, opening contacts, video cameras u. a. be used.

The detectors can be interconnected in different ways. Depending on the type and size of the areas to be protected and the applicable guidelines, suitable systems must be selected and installed. When planning or extending a GMA, care should be taken to ensure that the routes for networking have sufficient dimensions and as few changes as possible should be made to the route assignment.

In order to maintain the protective effect of the GMA, regular maintenance and functional testing (see DIN VDE 0833 Part 1-3 "Hazard Alarm Systems for Fire, Burglary and Raid") must be provided for.

If no GMA is available or if the existing one can not be used, local hazard detectors can be considered as a minimal solution. These work completely independently, without connection to a central office. The alerting takes place on site or by means of a simple two-wire line (possibly telephone line) elsewhere.

There are rooms like server room, data carrier archive, which have an increased need for protection. If there is no central GMA, local hazard alarms should be installed there. When using local hazard detection systems for early detection, it must be ensured that an alarm is also perceived outside the affected areas. The message can be sent through various channels and should be forwarded to a location that is staffed around the clock. For example, there are solutions that can alarm employees via the PBX or radio via a mobile phone.
Before planning a GMA, a consistent protection concept for the considered building must be developed. When planning security systems for private or commercial properties, it should be clarified with the property insurer whether a reduction in the insurance premium, in particular for burglary theft insurance, is possible.

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Further information about hazards and safety measures in the area of ​​"General Building" can be found in the following publications, among others:

* #### [27001A11] ISO / IEC 27001: 2013 - Annex A.11 Physical and envionmental security

  

 ISO, Information technology - Security techniques - Information security management systems - Requirements, in particular Annex A, A.11 Physical and environmental security, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [DIN0185-3] DIN V ENV 0185-3: Lightning protection, protection of structures and persons

 
* #### [DIN0298-4] DIN VDE 0298-4: Use of cables and insulated cables for power installations

  

 Part 4: Recommended values ​​for the current carrying capacity of cables and wires for fixed installation in and on buildings and flexible cables.

 
* #### [DIN0833-2] DIN VDE 0833-2: Alarm systems for fire, burglary and assault

  

 Part 2: Specifications for fire alarm systems

 
* #### [DIN0833-4] DIN VDE 0833-4: Alarm systems for fire, burglary and assault

  

  Part 4: Specifications for equipment for voice alarm in case of fire

 
* #### [DIN100-444] DIN VDE 0100-444: Installation of low-voltage systems

  

 Part 4-444: Protection measures - Protection against interference voltages and electromagnetic disturbances

 
* #### [DIN100-520] DIN VDE 0100-520: Installation of low-voltage systems

  

 Part 5-52: Selection and erection of electrical equipment - Cable and wire systems

 
* #### [DIN1047-1] DIN EN 1047-2: Secure storage units - Classification and methods of resistance to fire

  

 Part 1: Backup cabinets and diskette inserts

 
* #### [DIN1047-2] DIN EN 1047-2: Secure storage units - Classification and methods of resistance to fire

  

 Part 2: Data backup rooms and data backup containers

 
* #### [DIN1143-1] DIN EN 1143-1: Secure storage units - Requirements, classification and methods of resistance to burglary - Part 1

  

 Safes, safes for ATMs, strongroom doors and safes

 
* #### [DIN12056] DIN EN 12056-1 to 4: Gravity drainage systems inside buildings

 
* #### [DIN12101-1] DIN EN 12101-1: Smoke and heat storage

 
* #### [DIN13779] DIN EN 13779: Ventilation of non-residential buildings - General principles and requirements for ventilation and air conditioning systems and room cooling systems

 
* #### [DIN14073-2] DIN EN 14073-2: Office furniture - Office cabinets - Part 2: Safety requirements

 
* #### [DIN14096] DIN 14096: Fire protection regulations

 
* #### [DIN15602] DIN EN 15602: Security service providers / security service providers - terminology

 
* #### [DIN1627] DIN EN 1627: 2011-09

  

 Doors, windows, curtain walls, grilles and shutters - Burglar resistance - Requirements and classification, 2011

 
* #### [DIN18082] DIN 18082: Fire protection finishes

 
* #### [DIN18095-1] DIN 18095-1: Doors; Smoke doors; Terms and requirements

 
* #### [DIN1986-100] DIN1986-100: Drainage for buildings and land

 
* #### [DIN1991] DIN EN 1991: Eurocode 1: Actions on structures

 
* #### [DIN1992] DIN EN 1992: Eurocode 2: Design of reinforced concrete and prestressed concrete structures
* #### [DIN1993] DIN EN 1993: Eurocode 3: Design of steel structures

 
* #### [DIN1994] DIN EN 1994: Eurocode 4: Design and construction of composite steel and concrete structures

 
* #### [DIN1995] DIN EN 1995: Eurocode 5: Design of timber structures

 
* #### [DIN1996] DIN EN 1996: Eurocode 6: Design of masonry structures

 
* #### [DIN2425-1] DIN 2425-1: Planning for the utility industry, the water industry and for transmission lines; Pipe network plans of the public gas and water supply

 
* #### [DIN3] DIN EN 3: Portable fire extinguishers

 
* #### [DIN4102] DIN 4102: 2016-05

  

 Fire behavior of building materials and components, Beuth Verlag

 
* #### [DIN54] DIN EN 54: Fire alarm systems

 
* #### [DIN60839-11-1] DIN EN 60839-11-1 / VDE 0830-8-11-1: 2013-12: Alarm systems

  

 Part 11-1: Electronic access control systems - Requirements for plants and appliances

 
* #### [DIN62305-1] DIN EN 62305-1: Lightning protection

  

 2015-12 / VDE 0185-305-1: 2015-12: Lightning Protection - Part 1: General principles (IEC 81/472 / CD: 2015)

 
* #### [DIN77200] DIN 77200: 2008-05: Backup services - Requirements

 
* #### [ISFCF19] The Standard of Good Practice - AREA CF19 Physical and Environmental Security

  

 especially AREA CF19 Physical and Environmental Security, ISF, 06.2014

 
* #### [NIST80053PEP] NIST Special Publication 800-53 Revision 4 - APPENDIX PAGE F-213

  

 Assesing Security and Privacy Controls for Federal Information Systems and Organizations, in particular APPENDIX F-PS PAGE F-213, FAMILY: PHYSICAL AND ENVIRONMENTAL PROTECTION, NIST, 2013
 <Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
* #### [VDI3551] VDI 3551: Electromagnetic compatibility (EMC) in technical building equipment
