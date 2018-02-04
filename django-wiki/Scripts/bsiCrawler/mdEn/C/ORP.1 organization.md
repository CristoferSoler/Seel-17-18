[toc]
 
1 description
--------------

### 1.1 Introduction

Every company and authority must have an organization that controls the interaction of the various roles and units with the business processes and resources in the institution. Most institutions have an organizational unit responsible for the regulation and control of the general operation as well as for the planning, organization and execution of all administrative services. Various information security tasks must be implemented or supported by this unit.

### 1.2 Objective

This module describes requirements for an organization that serve to enable, control and operate information security.

### 1.3 Delimitation

This module outlines general and overarching requirements in the area of ​​information security organization. For this purpose, information flows, processes, role allocation, the structure and process organization are to be regulated. The building block organization thus forms the framework for the implementation of information security by other building blocks. Special requirements of an organizational nature, which are directly related to requirements of other blocks (eg server administration), are listed in the corresponding blocks.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​organization:

### 2 1 Missing or inadequate regulations

The importance of overarching organizational regulations and targets for the goal of information security. As the responsibilities or the distribution of control tasks increases with the complexity of business processes and the extent of information processing, but also with the protection needs of the information to be processed.

Lack of regulations can lead to massive security gaps, for example because employees do not know how to react to incidents. Problems can also arise because regulations are outdated, impractical, or incomprehensible formulated.

### 2 2 Disregarded regulations

Just setting rules does not mean that they are respected. All employees must also be aware of the applicable regulations. Damage that arises because existing regulations are not known, may not be excused with the statements: "I did not know that I am responsible." or "I did not know how to handle it."

Examples of consequential damage caused by non-compliance with regulations are:

* Confidential information is discussed within earshot of other people, for example, during breaks in meetings or via mobile phones in public environments.
* Documents are published on a web server without any proof of whether they are actually intended for publication.
* Due to improperly managed access rights, an employee can change data without being able to assess the relevance of this breach of integrity.
### 2 3 Missing, unsuitable, incompatible resources

Insufficient supply of equipment can significantly affect operation. Faults may arise if the required resources are not available in sufficient quantity or are not made available in due time. It may also be the case that inappropriate or even incompatible equipment is procured which consequently can not be used.

** Example: ** The hard disk space of PCs and servers as well as the mobile data carriers is constantly increasing. Unfortunately, it is often forgotten to procure IT components and data carriers that provide sufficient capacity for regular data backup.
Likewise, the functionality of the equipment used must be guaranteed. If maintenance work is not carried out or only insufficiently carried out, it can cause great damage. Examples:

* The batteries of an uninterruptible power supply (UPS) have an insufficient capacity due to lack of maintenance (too low acid content). The UPS can not bridge a power outage for a sufficient amount of time.
* The fire extinguishers are due to lack of maintenance no longer sufficient pressure, so that their fire-fighting effect is no longer guaranteed.
### 2 4 Unauthorized access to vulnerable rooms

All rooms, including offices in the home or on the road, where sensitive information is stored or processed must be protected against unauthorized access by third parties. Unauthorized persons may cause damage in such areas through deliberate acts (manipulation or vandalism), but also through unintentional misconduct (due to a lack of specialist knowledge). Even if no direct damage can be detected, the operating procedure can be disturbed even if it must be investigated how such an incident was possible or whether damage occurred or tampering was carried out.

For example, intruders could reset passwords, access servers directly, or manipulate active network components. Also, they could have stolen or altered sensitive information on paper or disk.

### 2 5 Unauthorized exercise of rights

Rights such as access, access and access rights are used as organizational measures to protect information, business processes and IT systems from unauthorized access. If such rights are granted to the wrong person or if a right is exercised unauthorized, a variety of dangers can result. For example, unauthorized persons could gain access to personal data.

### 2 6 Endangerment by non-operating persons

In the case of outsiders, it can not be assumed that they will bypass information and information technology that are accessible to them in accordance with the requirements of the institution visited, especially since they rarely know it.

Visitors, cleaners, and third-party personnel can compromise internal information, business processes, and systems in a variety of ways, from inappropriate handling of technical equipment to attempting to "play" IT systems, or even stealing documents or IT components ,

** Examples **

* Visitors may, if they are unaccompanied, have access to documents, data carriers or equipment, damage them or gain unauthorized knowledge of sensitive information.
* Cleaning personnel may inadvertently disconnect a connector, water may get into equipment, documents may be misplaced or even removed with the waste.
### 2 7 Manipulation of information and devices

Outsiders, but also culprits, can use deficiencies in the organization and try to manipulate devices, accessories, documents and other data carriers. Tampering can range from falsely gathering data, changing access rights, to manipulating operating systems, data carriers, or IT systems. Attacks are all the more effective the later they are discovered, the broader the perpetrator's knowledge is, and the more profound the consequences are for a work process.

** Example: ** In a Swiss financial company, an employee manipulated the application software for certain financial services. This allowed him to illegally obtain larger sums of money.

### 2 8 Destruction, vandalism, sabotage
For various reasons (revenge, malice, frustration), people can try to disrupt business processes, manipulate or destroy devices or information.

Both outside perpetrators (eg, disappointed burglars, out-of-control demonstrators) and culprits (eg, frustrated or mentally unstable staff) can destroy or damage someone else's property through vandalism. While vandalism is usually an expression of spontaneous, blind destructiveness, sabotage is the willful manipulation or damage of things with the aim to harm the victim. Particularly attractive targets of sabotage can be data centers or communication links of authorities or companies, since a relatively small amount of funds can make a big impact.

### 2 9 Theft and loss of information and equipment

The theft or loss of data carriers, IT systems or data can lead to various consequential damages in addition to the immediate material losses, if no appropriate organizational precautions have been taken.

3 requirements
---------------

The following are specific requirements for protection in the organization. Basically, the Information Security Officer (ISB) is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### ORP.1.A1 Definition of Responsibilities and Regulations [Institutional Management]

For all security-related tasks, both responsibilities and authority MUST be defined. Binding information security regulations for the various operational aspects MUST be defined across the board. It also MUST be clear which information can be exchanged with whom and how they should be protected. The regulations MUST be revised on a regular basis. They MUST be announced to all employees.

#### ORP.1.A2 Assignment of responsibility for information, applications and IT components [Head of IT, Information Security Officer (ISB), Head of Institution]

All information, business processes, applications and IT components MUST be defined as who is responsible for them and their security. All employees MUST be aware of what they are responsible for and in what ways.

#### ORP.1.A3 Supervision or assistance of third parties [employees]

Employees MUST be urged not to leave unrelated persons unattended.

#### ORP.1.A4 Function separation between operational and controlling tasks

Within an institution, all relevant tasks and functions SHOULD be defined and clearly delineated. The tasks and the required roles and functions MUST be structured in such a way that operational and controlling functions are distributed to different persons. For incompatible functions, a separation of functions MUST be defined and documented. Representatives MUST also be subject to separation of functions.

#### ORP.1.A5 Authorization [Head IT]

It MUST be determined which access, access and access rights are assigned to which persons within their tasks and functions. Only as many rights may be assigned as are necessary for the task perception. There must be a regulated procedure for granting, managing and revoking privileges (see also ORP.4 Identity and Entitlement Management). The documentation of the permissions MUST be current and complete.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of organization. They SHOULD be implemented in principle.
#### ORP.1.A6 The tidy workplace [employee]

All employees SHOULD be advised that neither sensitive information nor IT systems should be freely accessible at unattended workplaces. Workplaces SHOULD be randomly checked to see if vulnerable information is open to the public.

#### ORP.1.A7 Device Management [Head of IT, Head of Production and Production, Head of Building Services]

It SHOULD have an overview of all devices that are used in the institution and that can have an impact on information security. In addition to IT systems and ICS components, these also include Internet of Things. It SHOULD give appropriate testing and approval procedures before using the equipment.

#### ORP.1.A8 Resource Management [IT Leader]

The resources required to perform the task and meet safety requirements SHOULD be in sufficient quantity. It SHOULD give appropriate test procedures before use of the equipment. For inventory management, the resources SHOULD be listed in inventories. In order to prevent the misuse of data, the reliable deletion or destruction of resources SHOULD be regulated.

#### ORP.1.A9 Proper Disposal of Protected Equipment [Staff, Information Security Officer (ISB)]

Operating and material resources SHOULD be disposed of in such a way that no conclusions can be drawn as to their use or contents. The disposal of protective materials SHOULD be regulated. All employees SHOULD know these regulations. To dispose of sensitive material, appropriate disposal facilities, such as: B. shredder available. Protective material collected for disposal SHOULD be protected against unauthorized access.

#### ORP.1.A10 Responding to security breaches [Information Security Officer (ISB)]

It SHOULD be regulated, which reactions take place in case of suspected violations of the security specifications. Only then is a targeted and timely response possible.

#### ORP.1.A11 Timely participation of the Staff Committee [Head of IT]

The staff representatives (employees 'representatives, employees' representatives) SHOULD be informed in due time about any procedures and projects that affect them.

#### ORP.1.A12 Regulations for maintenance and repair work [IT operation, building services, ICS information security officer]

Technical devices SHOULD be maintained regularly. It should be regulated which safety aspects are to be observed during maintenance and repair work and who is responsible for the maintenance or repair of equipment. Employees SHOULD know that maintenance personnel must be supervised while working in the house. Performed maintenance work SHOULD be documented.

#### ORP.1.A13 Relocation Security [Head of IT, Head of Domestic Engineering, Information Security Officer (ISB)]

Before a planned move, security guidelines for this purpose SHOULD be developed or updated in good time. All employees SHOULD be informed about the security measures to be followed before, during and after the move. During the move a minimum level of access and access control SHOULD be present. It should SHOULD be checked after the move that the moving goods to be transported has arrived completely undamaged or unchanged.

### 3.3 Requirements for increased protection requirements
Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### ORP.1.A14 Inspections [Building Services, Information Security Officer (ISB)] (CIA)

Checks should be carried out to check the extent to which security requirements are implemented. Easy to correct negligence SHOULD be rectified immediately (eg Close window). In addition, causes should be questioned and eliminated.
