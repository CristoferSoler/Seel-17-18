1 description
--------------

### 1.1 Introduction

Teleworking is understood to mean any activity based on information and communication technology, which is carried out exclusively outside the business premises and buildings of the employer. There are different forms of teleworking. It can, for example, be provided as home-based teleworking in the employee's home. It is also possible that the employees are employed in the context of the on-site teleworking with customers or suppliers and work there with the equipment of the own employer. Another possibility is teleworking in so-called telecentres, satellite or neighborhood offices.

Homebased telework distinguishes between home-based work and alternating teleworking. In the case of alternating teleworking, employees work alternately at their workplace at the employer's workplace and at home.

### 1.2 Objective

The aim of the module is to protect the information stored, processed and transmitted during teleworking. For this purpose, typical hazards are identified and specific requirements for teleworking are defined.

### 1.3 Delimitation

This building block focuses on the forms of telework that are carried out partly or wholly in the home environment. It is assumed that there is a telecommunications link between the teleworkstation and the institution that makes it possible to exchange information and if necessary access data in the institution. The requirements of this module cover three different areas:

* the organization of telework,
* teleworker's teleworker and
* the communication link between teleworker and institution.
Safety requirements for the teleworking center infrastructure are not taken into account in this module, but are described in module INF.8 * Domestic workstation *. The requirements of the topic-overlapping module INF.10 * Mobile workstation * must be observed.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the *** *** teleworking area:

### 2 1 Missing or inadequate regulations for the teleworking station

Since a teleworking station is located outside the institution, it requires individually adapted organizational arrangements. If such regulations do not exist, employees may not know that they B. independently have to perform backups. Also, they may not know how to handle security-related incidents at the teleworkstation. For example, if confidential information gets into someone else's hands, it may be used by unauthorized persons as a serious disadvantage of the institution.

### 2 2 Lack of or insufficient training of teleworkers

Teleworkers are largely on their own at work. If the teleworker not sufficiently trained in the use of IT, which may cause problems to increased downtime, as for example, an IT supervisor from the institution must first drive to the telework place, there to eliminate the problems.

### 2 3 Unauthorized private use of the official teleworking computer

In the home, it is easier to use the official teleworking computer privately, because controls by the employer are only partially possible. Therefore, it can happen that unchecked and released software is used and by careless action malicious software reaches the teleworking computer. This could, for example, compromise confidential information.
But not only teleworkers can use their computer improperly, but also relatives or visitors. Damage such as deleted hard drives can result in reinstallation costs or re-capture work.

### 2 4 Delays due to temporarily limited availability of teleworkers

Usually, a teleworker has no fixed working hours at the teleworkstation. Only fixed times are agreed on when he must be reachable. In the case of alternating teleworking, his working hours are also distributed between the teleworkstation and the in-house workplace.

If it is necessary for information to be obtained from the teleworker at short notice or for information to be passed on to the teleworker, delays may occur due to the difficult accessibility. Even if the information is sent via e-mail, it does not necessarily shorten the response time since it can not be guaranteed that the teleworker will read the e-mail in a timely manner.

Delays due to temporarily limited accessibility of teleworkers can have different effects depending on the situation and institution and limit the availability.

### 2 5 Poor integration of the teleworker in the flow of information

Since teleworkers are not in the institution on a daily basis, they have less opportunity to participate in the direct exchange of information with supervisors and work colleagues. As a result, they can be isolated from operational events and thereby z. B. identify less with the institution. Lack of information can also result in errors in workflows and operational processes that limit the teleworker's productivity. If the flow of information to the teleworker is not guaranteed, important news on information security may not reach him in time.

### 2 6 Insufficient representation rules for teleworking

The tasks of the teleworker are usually designed so that he can work independently for the most part. This can make it difficult in the case of illness to provide a representation for the teleworker. In particular, there may be problems in providing the requisite documentation or teleworker data to the representative when there are no access to the teleworker's home office.

### 2 7 Non-compliance with safety measures

Especially at the teleworkplace, due to a lack of control options, employees may not or not fully implement recommended or ordered security measures. It may cause damage that would otherwise be prevented or at least reduced. Depending on the function of the employee and the importance of the disregarded measure even serious damage can occur, eg. For example, confidential information can fall into the wrong hands. These may then be used to the serious disadvantage of the institution.

3 requirements
---------------

The following are specific requirements for the protection of teleworking. Basically, the Information Security Officer (ISB) is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### OPS.1.2.4.A1 Teleworking Regulations [Supervisor, Human Resources]
All relevant aspects of teleworking MUST be regulated. For information purposes, teleworkers MUST be given the applicable rules or a leaflet intended to explain the security measures to be followed. All points in dispute MUST be settled either by company agreements or by individual agreements between the teleworker and the employer in addition to the employment contract. For each teleworker, a representative MUST be named. The substitution case SHOULD be rehearsed regularly. The regulations MUST be updated regularly.

#### OPS.1.2.4.A2 Safety requirements for the teleworking computer [Head IT, IT operation]

All safety requirements that a telework computer must meet must be specified. All access and access to the institution's communication computers MUST be kept to the minimum necessary.

It MUST be ensured that only authorized persons are allowed to access the telework computers. In addition, the teleworking computer MUST be secured so that it can be used only for authorized purposes.

#### OPS.1.2.4.A3 Safety requirements for the communication connection [Teleworker, IT Manager, IT Operations]

It is necessary to define safety requirements for the communication link between the teleworking computer and the institution. It MUST be ensured that the confidentiality, integrity and authenticity of the transmitted data is guaranteed.

All communication protocols and security mechanisms MUST meet the defined requirements of the institution. The strength of the required security mechanisms SHOULD be based on the protection needs of the transmitted data. In addition, the authenticity of the communication partners MUST be guaranteed.

#### OPS.1.2.4.A4 Data protection in teleworking [Teleworker, IT operation]

All data processed during teleworking MUST be saved in a timely manner. For this purpose, data backups MUST be carried out either locally on external data carriers or centrally via the connection to the network of the institution.

The selected backup method MUST be appropriate and sufficient for the volume of data. In order to ensure a smooth process, as few backup actions as possible have to be made by the teleworker. There SHOULD be deposited a generation of backup volumes in the institution.

#### OPS.1.2.4.A5 Awareness and Training of Teleworkers [Supervisors, Head of IT]

Using a memo, teleworkers MUST be made aware of the dangers associated with teleworking. In addition, they MUST be trained in the appropriate security measures of the institution and trained in their handling. Training and awareness raising for teleworkers SHOULD be repeated regularly.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in teleworking. They SHOULD be implemented in principle.

#### OPS.1.2.4.A6 Creating a security concept for teleworking [Supervisor, Head of Organization, Head of IT]

A teleworking security concept SHOULD be created describing security objectives, protection needs, security requirements and risks. The concept SHOULD be regularly updated and revised. The security concept for telework SHOULD be coordinated with the overarching security concept of the institution.

#### OPS.1.2.4.A7 Regulated use of communication options for teleworking [teleworkers, IT operations]
It SHOULD be clearly defined which communication options may be used for teleworking under which conditions. The official and private use of Internet services in telework SHOULD be regulated. It should also be clarified whether a private use is generally allowed or prevented.

#### OPS.1.2.4.A8 Flow of information between teleworker and institution [supervisor, teleworker]

A regular in-house exchange of information between teleworkers, work colleagues and the institution SHOULD be ensured. All teleworkers SHOULD receive timely information about changed security requirements and other security-related aspects. All colleagues of the respective teleworker SHOULD know when and where this can be achieved. Technical and organizational teleworking arrangements for task management, security incidents and other problems SHOULD be regulated and communicated to teleworkers.

#### OPS.1.2.4.A9 Care and Maintenance Concept for Teleworking Places [Teleworker, IT Manager, IT Operations]

For teleworking places, a special care and maintenance concept SHOULD be created. The following aspects SHOULD be regulated: contact person for the user service, maintenance appointments, remote maintenance, transport of the IT equipment and introduction of standard teleworking computers. In order for the teleworkers to remain operational, they should be named contact persons for hardware and software problems.

#### OPS.1.2.4.A10 Implementation of a requirement analysis for the teleworking station [Head IT, IT operation]

Before a teleworkstation is set up, a requirement analysis SHOULD be performed. From this SHOULD z. For example, you can see which hardware and software components are needed for the teleworkstation. The requirements for the respective teleworkplace SHOULD be coordinated with the IT managers. It SHOULD ALWAYS BE DETERMINED AND documented, which protection requirements the information processed at the teleworkstation has.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and security measures in the field of telework can be found in the following publications:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NIST80046] NIST Special Publication 800-46 Revision 2

  

 Guide to Enterprise Telework, Remote Access and Bring Your Own Device (BYOD) Security, NIST, 07.2016
 <Http://dx.doi.org/10.6028/NIST.SP.800-46r2>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the "teleworking" building block.

* G 0.14 Spying out information (spying)
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.24 Destruction of equipment or data media
* G 0.25 Failure of devices or systems
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.33 Personnel loss
* G 0.40 Denial of Service
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
