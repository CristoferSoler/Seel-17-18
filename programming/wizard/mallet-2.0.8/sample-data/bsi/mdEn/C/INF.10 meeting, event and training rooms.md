1 description
--------------

### 1.1 Introduction

As a rule, each institution has one or more rooms in which meetings, trainings or other events can be held. For this purpose, specially equipped rooms are often provided. Meeting, event and training rooms are characterized by the fact that they are used by changing people or groups of people and visitors and usually only for a limited period of time. IT systems brought along are often operated in conjunction with devices of the institution, such as third-party laptops on permanently installed projectors. These different usage scenarios result in a risk situation that is hardly comparable with those of other rooms.

### 1.2 Objective

The aim of the module is to protect the information that is processed in meeting, event and training rooms, as well as the IT equipment that operates in these rooms. In addition, the proper handling of visitors who use appropriate spaces, treated.

### 1.3 Delimitation

This module considers all technical and non-technical safety aspects for the use of meeting, event and training rooms. Detailed recommendations on how to configure and secure the IT systems in these rooms are not covered in this module, which can be found in SYS.2.1 General Client and OS-specific system building blocks. Other typical for meeting rooms aspects such. B. WLAN or video conferencing systems are considered in the building blocks of the layers NET.2 radio networks or NET.4 telecommunications. The wiring in these rooms is in the module INF. 3 Electrotechnical cabling and INF.4 IT cabling considered separately. Requirements for fire protection can be found in building block INF.1 General building.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to the meeting, event, and training rooms:

### 2 1 Missing or inadequate regulations

If z. For example, if employees do not close the windows and doors when they leave the room, or confidential information is not removed from a whiteboard or flipchart, sensitive information can be viewed by unauthorized persons. In general, employees should therefore be provided with appropriate regulations so that corresponding security gaps can not occur. However, stipulating regulations does not yet ensure that they are also observed and the operation is trouble-free. Many problems also arise if the regulations are available but not known. Often z. For example, employees do not need to close windows and doors after meetings and how to handle a used flipchart.

### 2 2 Incompatibility between foreign and own IT

IT systems are becoming increasingly mobile and increasingly used in different environments. Mobile IT users often find scenarios in which the IT systems can not be used as planned due to incompatibility. For example, older devices do not have the same connectors and connectors as newer devices. In addition, devices are manufactured that are not compatible with other devices without a suitable adapter. So is z. For example, if a matching adapter is not available, a laptop that has been prepared with all the important data for a meeting can not be used on a projector. In addition, attempts to connect the IT systems may cause damage to the equipment or stored data.

### 2 3 Danger to visitorsIt is not always easy to sensitize and train your own employees to handle sensitive information and IT systems properly. Visitors can generally not be expected to handle the information and information technology available to them in accordance with the requirements of the institution visited, especially since they are often unaware of these requirements. Visitors can generally access confidential information by carelessness of their own employees. Likewise, this can happen out of ignorance, for example, when the visitors are on the way to the toilet in the door err and enter a staff office, on the whiteboard confidential information. Visitors may also intentionally destroy or damage equipment to obtain confidential information.

### 2 4 Flying wiring

In meeting, event, and training rooms, users often change as well as how the rooms are used. This will sometimes change the equipment and thus of course the wiring in such rooms permanently. Cables can thus, depending on the location of the connection points in the room (sockets of the power supply and the data network) transitionally across the room, even over traffic routes away, be laid. Not only people are endangered by these trip hazards, even IT equipment can be damaged if people tear the "flying" cables with them.

### 2 5 Theft

If the data carriers, IT systems, accessories, software or data that are partly stationary in a meeting room are stolen, there are costs for the replacement as well as for the restoration of a workable state. On the other hand, the meeting room can be used only limited then due to lack of availability of the devices. Thus, there may be bottlenecks regarding the occupancy of rooms. In addition, confidential information may be stolen, abused or disclosed.

In addition to expensive IT systems, mobile devices are often stolen, which are inconspicuous and easy to transport. If the meeting, event and training rooms are not closed or supervised or the IT systems are not adequately secured, the technology can be stolen quickly and inconspicuously. This is especially true if, for example, in meeting breaks, the premises are not closed.

### 2 6 Confidentiality loss of sensitive information

By technical failure, carelessness, ignorance also by intentional acts confidential information can be disclosed. This confidential information may be available in different places, such. For example, on storage media within computers (such as hard drives), on removable storage media (such as USB sticks or optical media), in printed form on paper and on whiteboards or flipcharts. If information is read or disclosed unjustifiably, it can have serious consequences for the institution, such as violations of law, competitive disadvantages or financial repercussions.

3 requirements
---------------

Specific requirements for the protection of meeting, event and training rooms * are listed below. In principle, the head of organization is responsible for the fulfillment of the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:#### INF.10.A1 Secure use of meeting, event and training rooms [Head of IT, Building Services]

Equipment in the rooms MUST be adequately secured against theft. In addition, it MUST be determined who administers the permanently existing IT and other systems in the rooms. It MUST also be determined if and under what conditions visitors may use IT systems brought along. Furthermore, it must be determined whether and to which network access and TK interfaces visitors may access.

#### INF.10.A2 Supervision of visitors [Staff]

Visitors MUST be supervised outside of spaces specifically designated for access by visitors. Employees MUST be advised not to leave unmanned persons unattended.

#### INF.10.A3 Closed windows and doors [Staff]

The windows of the meeting, event and training rooms MUST be locked when leaving. For premises with IT systems or sensitive information, the doors MUST be locked when leaving. In addition MUST be checked regularly, if the windows and doors were closed after leaving the rooms. Likewise MUST be taken to ensure that fire and smoke protection doors are actually closed.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​meeting, event and training rooms. They SHOULD be implemented in principle.

#### INF.10.A4 Planning of meeting, event and training rooms

When planning meeting, event and training rooms, the location of the rooms SHOULD be taken into account. In particular, premises that are often used by visitors SHOULD NOT be located in parts of the building where confidential information is regularly processed. It should be determined for each room how confidential the information may be, which may be discussed or processed in the premises.

#### INF.10.A5 Flying Wiring

To avoid flying cabling, the power connectors SHOULD be located where projectors, laptops or other consumers are placed. In addition, cabling that goes over the floor should be covered with a cable duct.

#### INF.10.A6 Setting up secure network access [Head IT]

It should be ensured that IT systems brought along can not be connected to internal IT systems via the data network. Only dedicated IT systems should be able to access the institution's LAN. A data network for visitors SHOULD be separated from the LAN of the institution. Network access SHOULD be set up so that it is prevented that third parties can read the internal data exchange. Power connections in meeting, event or training rooms SHOULD be secured. It SHOULD prevent IT systems in meeting, event, and training rooms from connecting to the intranet and the Internet at the same time.

In addition, the power supply SHOULD be built out of a subdivision separate from other rooms.

#### INF.10.A7 Secure Configuration of Training and Presentation Computers [IT Leader]

Dedicated training and presentation calculators SHOULD be provided with a minimal configuration. It should be determined which applications can be used on training and presentation computers in the respective event. The training and presentation computers SHOULD only be connected to a separate network separate from the institution's LAN. Other networks SHOULD only be accessible restrictively.

#### INF.10.A8 Creation of a proof of use for roomsDepending on the type of use of the meeting, event and training rooms, it should be clear who used the rooms at what time. For premises where training on IT systems or particularly confidential meetings are carried out, proof of use should also be provided. It SHOULD be considered to introduce evidence of use for premises accessible to each employee.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### INF.10.A9 Resetting Training and Presentation Computers [IT Leader] (CA)

A procedure SHOULD be set to reset training and presentation computers to a predefined state after use. User made changes SHOULD be completely removed.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and security measures in the area of ​​"meeting, event and training rooms" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [DIN1627] DIN EN 1627: 2011-09

  

 Doors, windows, curtain walls, grilles and shutters - Burglar resistance - Requirements and classification, 2011

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the building block "meeting, event and training rooms".

* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.16 Theft of devices, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.21 Manipulation of hardware or software
* G 0.24 Destruction of equipment or data media
* G 0.41 Sabotage
* G 0.44 Unauthorized intrusion into premises
* G 0.45 data loss
The cross reference tables can be found in the download area due to their size.