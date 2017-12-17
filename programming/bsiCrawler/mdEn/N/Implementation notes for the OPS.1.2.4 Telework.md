1 description
--------------

### 1.1 Introduction

Teleworking is understood as any activity based on information and communication technology, which is carried out exclusively or occasionally outside the business premises and buildings of the employer.

There are various forms of teleworking: it can be provided, for example, as home-based teleworking in the employee's home or as mobile teleworking on the go. It is also possible that the employees are employed in the context of the on-site teleworking with customers or suppliers and work there with the equipment of the own employer. Another possibility is the teleworking in so-called telecenters or satellite or neighborhood offices.

Homebased telework distinguishes between home-based work and alternating teleworking. In the case of alternating teleworking, employees work alternately at their workplace at the employer and at home.

### 1.2 Life cycle

** planning and conception **

* A teleworking concept should be developed outlining the security objectives, the protection needs of teleworking information, and the risks and safety measures (see OPS.1.2.4.M6 Creating a Teleworking Security Policy). *

* Secure teleworking requires organizational regulations and personnel measures. Particular attention should be given to the special obligations of teleworkers and their instruction in the terms of use of communications. They are described, inter alia, in OPS.1.2.4.M1 Regulations for Teleworking and OPS.1.2.4.M5 Awareness and Training of Teleworkers. *

**Implementation**

After the organizational and planning preparatory work has been completed, the teleworkers and other IT systems can be installed. The following measures must be observed:

* Safety of the teleworking computer: The teleworking computer must be designed in such a way that safe use is possible in an unsafe operating environment. In particular, only authorized persons should use the teleworking computer offline and online (see OPS.1.2.4.M2 * Safety requirements for the teleworking computer *).
* Secure communication between the teleworking computer and the institution: As communication takes place via public networks, special security requirements for communication between the teleworking computer and the institution must be fulfilled (see OPS.1.2.4.M3 * Safety requirements for the communication link *).
**Business**

Users have a significant impact on telework safety. Teleworkers must therefore be trained to comply with security requirements and to use the IT systems (see * OPS.1.2.4.M5 Awareness and Training of Teleworkers *).

** Emergency Preparedness **

All relevant data created or modified during teleworking must be saved (see OPS.1.2.4.M4 * Teleworking data *).

2 measures
-----------

The following are specific implementation notes in the Teleworking section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### OPS.1.2.4.M1 Teleworking Regulations [Supervisor, Human Resources]

Institutions must set rules for telework. In doing so, various labor law and health and safety conditions must be observed. Controversial points should be clarified either by company agreements or by individual agreements between teleworker * and employer in addition to the employment contract. For example, these agreements should address the following issues:

* Voluntary participation in teleworking
* Overtime and surcharges
* Expenses for trips between company / customer and home
* Expenses for example for electricity, heating and rent
* Liability (in the case of theft or damage to IT, but also in case of accident at work or occupational disease)
* End teleworking
The security measures necessarily to be implemented for teleworking in the handling of information and information and communication technology should also be documented in a telework safety directive, unless it is appropriate to integrate the contents into already existing guidelines of the institution.

The following aspects, for example, should be considered in the teleworking regulations:

* ** Working time regulation: ** It should be regulated how the working hours are distributed among activities between the institution and the teleworker. Fixed times must also be set at which the employee can be reached at the teleworkstation.
* ** Response times: ** It should be regulated at what intervals the teleworkers are to retrieve current information (for example, how often emails are read) and in which period of time they have to respond.
* ** Handling of confidential information: ** In teleworking, confidential information is processed both analogously, for example on paper, as well as digitally. Regardless of the form in which information is available, it must be protected from unauthorized access and other security risks. Therefore, the entire life cycle of confidential information is adequately secured.
* ** Tools: ** It should be specified which tools the teleworker may use and which should not be used (for example, not released software). Thus, an e-mail connection can be provided, but the use of other Internet services are prohibited. Furthermore, it could be prohibited to use data carriers such as DVDs or USB sticks, if the teleworkstation does not require this.
* ** Data backup: ** Teleworkers must be obliged to back up locally stored data on a regular basis. In addition, it should be agreed that one generation of data backups will be deposited in each institution. If the data backup via the remote access to the institution is already sufficiently secured and there is no increased need for protection, a local data backup can be waived.
* ** Synchronization of data stocks: ** Data sets that are processed both in the institution and at remote workstations must be synchronized appropriately. The synchronization procedure must be planned precisely so that no conflicts arise and no data loss occurs. The conflicts occur, for. For example, if two users have changed the same record in mirrored datasets. It is advisable to synchronize the data using appropriate software.
* ** Privacy Policy: ** Privacy Policy: Teleworkers are required to comply with applicable privacy laws.
* ** Data communication: ** It must be determined which data is transmitted by which means or which data may not be transmitted electronically or only encrypted. It should also be determined which documents can be transported between the institution and the teleworkstation and how they should be protected.
* ** Transport of documents and data carriers: ** The nature and security of the transport of documents and data carriers, between the teleworkplace and the institution, must be regulated. Confidential data on digital media should always be transported encrypted.
* ** Registration: ** Teleworkers are to be obliged to report security-related incidents immediately to an institution to be designated in advance. For this it is necessary to instruct the teleworkers in accordance with the applicable guidelines. For example, the Incident Management Guideline is suitable for this.
* ** Access right teleworking place: ** An access right to the teleworking place should be agreed, if necessary after previous registration. This is important in the first place, so that in case of substitution files and data for the assistant employee are available.
* ** Substitution scheme: ** For each teleworker, a representative should be appointed who must be informed about the current activities, so that he can take over the representation at short notice. For this, the work results by the teleworkers must always be carefully documented. Maybe sporadic or regular meetings between the teleworker and his representative make sense. In addition, it must be regulated how the representative can access the data, the teleworking computer or the teleworkstation in the event of an unexpected substitution. This substitution case should be tested on a trial basis and the test then be evaluated by the teleworker and his representative. This makes it possible to constantly optimize the substitution process.
The rules for teleworking are to be handed out to every teleworker. Corresponding leaflets must be updated regularly.

#### OPS.1.2.4.M2 Safety requirements for the teleworking computer [Head IT, IT operation]

The safety requirements for the telework computers are based on the protection requirements of the data to be processed at the teleworkstation and the data that teleworkers can access via the institution's communication computer. The higher the need for protection, the more measures must be taken to ensure this protection.

General security goals for teleworkers are:

* Telework computers may only be used by authorized persons. This ensures that only authorized persons can access data and programs stored on a teleworking computer. The same applies to information and data that could be reached via the teleworking computer (for example, via VPN). Authorized persons are the administrator of the teleworking computer and the teleworker and his deputy.
* Telework computers may only be used for authorized purposes. For example, the user should not be allowed to install unauthorized programs. This prevents damage caused by misuse and misuse.
* Damage due to theft or malfunction of a teleworking computer must be tolerable. Teleworkers are typically deployed in a low-security environment so that theft or malfunction is more likely than in the protected operating environment of an institution. This can not only affect the availability but also the confidentiality of the stored data. For example, to minimize damage from theft, data should only be stored in encrypted form. To limit damage caused by defects, for example, regularly performed backups are suitable.
* Teleworkers should be able to detect at least obvious attempted or made manipulations on the teleworking computer. This ensures that the teleworking computer remains in an integrity state, even if manipulation attempts are not excluded.
From the protection requirement of the data to be processed at the teleworking station * *, the safety objectives and thus the safety requirements for the teleworking computers are derived. It must be documented which of the safety-relevant functionalities described below must have a teleworking computer and how these are to be implemented.

The following functionalities are useful for a teleworking computer:

* The teleworking computer must have an identification and authentication mechanism **. In particular, the following points must be ensured:

 
+ Security-critical parameters such as passwords or user ID must be securely managed. Passwords must never be stored unencrypted on the teleworking computer.
+ The access procedure must respond to incorrect entries in a defined manner. If, for example, faulty authentication occurs three times in succession, access to the teleworking computer is to be blocked or the time intervals must be successively increased, after which a further access attempt is permitted.
+ It must be possible to specify minimum specifications for the safety-critical parameters.
+ After a temporary inactivity of the keyboard or mouse, a screen lock must be activated automatically, which is only deactivated after re-identification and authentication.


 
* The teleworking computer must have ** access control **. In particular, the following requirements have to be implemented:

 
+ The teleworking computer must be able to differentiate between different users. It must be possible to set up at least two separate roles on the teleworker, namely Administrator and Teleworker.
+ By means of a differentiated legal structure (for example, reading, writing, executing), access to files and programs must be controllable. For mobile devices, a differentiated legal structure is not always possible. Especially smartphones and tablets often have no such differentiation. It should therefore be checked whether the devices are suitable for the present protection needs.


 
* Teleworking computers should have ** logging **. It makes sense to implement the following requirements:

 
+ The minimum amount that the teleworker should log should be configurable. For example, the following actions including the occurred error cases should be logged:


- for authentication: for example, user ID, date and time, result of access control logon attempt, type of access, what was changed, read, written
- carrying out administrative activities,
- Occurrence of functional errors.



+ for unauthorized persons there must be no possibility to disable logging. The protocols themselves may not be readable or modified by unauthorized persons.
+ The logging must be clear, complete and correct.


 
* If the teleworking computer should have a ** protocol evaluation **, the following requirements may be useful:

 
+ An evaluation function must be able to distinguish between the types of data required during logging (for example, filtering of all unauthorized access to all resources in a given period).
+ The evaluation function must generate reportable (readable) reports so that no safety-critical activities are overlooked.


 
* Teleworking computers should have ** data backup ** features. These should fulfill the following requirements, among others:
 

 
+ Data protection for teleworking should comply with the framework conditions for data protection of the institution and comply with them
+ The backup program must be user-friendly and fast. It should be automatable.
+ It must be configurable, which dates are backed up when.
+ There must be an option to restore any backups.
+ The function must allow to secure several generations.
+ Backup of intermediate results from the running application should be possible.


 
* Teleworking computers should have a ** encryption component **. For this purpose, it is important to first consider which functionality is required:

 
+ the encryption of selected data (offline) or
+ automatically the entire hard drive (online).
In principle, the automatic encryption of all data carriers should be preferred because this is more user-friendly and efficient. This requires that a suitable encryption product is used and that data loss in case of malfunction (power failure, abortion of the encryption) is intercepted by the system. In addition, the following requirements are useful:
 

 
+ The implemented encryption algorithm should meet the requirements of the institution.
+ The key management must harmonize with the functionality of the teleworking computer. In particular, fundamental differences of the algorithms are to be considered: Symmetric methods use a secret key for encryption and decryption, asymmetric methods use a public key for encryption and a private (secret) for decryption.
+ The teleworking computer must securely manage the safety-critical parameters such as keys. Thus, keys (even those that are no longer used) must never be stored unprotected, that is, readable on the teleworking computer.


 
* If the teleworking computer should have ** Integrity Check ** mechanisms, the following requirements are useful:

 
+ Integrity checking procedures should be used which can reliably detect intentional manipulations on the teleworking computer or on the data.
+ Data transfer mechanisms must be used to detect intentional manipulation of address fields and user data. In addition, the mere knowledge of the algorithms used without special additional knowledge may not be sufficient to make unrecognized manipulations of the above data.


 
* The telework calculator should have ** boot protection ** to prevent unauthorized booting from removable media.
* It should be possible to restrict the ** user environment ** of the teleworking computer ** **. The administrator should be able to specify which programs the teleworker can execute, which peripheral devices can be used and which changes the teleworker may make to the system. In addition, the teleworker settings that are necessary for safe operation should not change unauthorized and not allowed to play third-party software without permission.
* Depending on the operating system installed and other existing protection mechanisms of the teleworking computer, it must be checked whether virus protection programs should be used. If this is the case, a virus check must be carried out before importing data from removable media, before transferring data media or when sending and receiving data.
* If the teleworking computer should be administered via ** Remote Administration **, it must be ensured that remote administration can only be carried out in an authorized way. In the remote maintenance, authentication of the remote maintenance personnel, the encryption of the transmitted data and a logging of the administration processes must be ensured.
From the above functionalities, it is necessary to select those which are required due to the security requirements of the teleworking computers and which are possible according to the protection requirement. Based on these functionalities then a suitable operating system must be selected as a platform. If this does not support all the required functionalities, additional products must be used. In this case, as far as possible all telework computers of an institution should be equipped in the same way in order to facilitate care and maintenance and to be able to bring similar systems together as client groups. The overall system must be configured by the administrators so that maximum security can be achieved.

Additional requirements for the individual client systems are listed in the block layer SYS.2 * Desktop Systems *. These should be implemented according to the client solution used for the teleworking computer.

#### OPS.1.2.4.M3 Safety requirements for the communication connection [Teleworker, IT Manager, IT Operations]

If teleworking involves data transmission between a teleworking computer and a computer of the institution, official information is usually transmitted via public communication networks. Since neither the institution nor the teleworkers have any influence on whether the confidentiality, integrity and availability are maintained in a public communications network, additional security measures are required.

In general, data transfer between the teleworking computer and the institution must meet the following security requirements:

* ** Securing the confidentiality of the transmitted data: ** A sufficiently secure encryption must ensure that even if attackers intercept the communication between the telework computer and the institution's computer, no conclusions can be drawn about the contents of the data. In order to ensure the confidentiality of the transmitted data, in addition to a suitable encryption method, an adapted key management with periodic key change is also required.
* ** Ensuring the integrity of transmitted data: ** The transmission protocols used must detect and correct a random change in transmitted data. To be able to detect intentional manipulations during data transmission, the data should be signed and / or encrypted.
* ** Ensuring the availability of data transmission: ** If time delays in teleworking are difficult to tolerate, a redundant public communication network should be selected as the transmission path so that failure of individual links does not mean total communication failure. On a redundant network connection to the teleworking computer and the interface of the institution may be waived if necessary.
* ** Ensuring the authenticity of the data: ** When transferring data between the teleworking computer and the institution, it must be ensured that communication takes place between the right participants. This means to ensure that data with sender telework computer actually come from there. Similarly, the origin of institutional data must be undoubtedly traceable back to the institution.
* ** Ensuring the traceability of data transmission: ** Logging functions can be used to make communication comprehensible.
* ** Ensuring data reception: ** If it is important for teleworking that data has been received correctly, acknowledgment mechanisms can be used to determine whether the recipient has received the data correctly.
#### OPS.1.2.4.M4 Data Protection in Teleworking [Teleworker, IT Operations]
In teleworking, data can be processed on different IT systems and in different places. For example, the processing can take place on servers and clients in the institution, but also on telework clients. To ensure the availability of data, they must be backed up regularly.

A backup of all relevant data at the teleworkstation must generally take place and comply with the general rules for data backup of the institution. The institution's data protection concept must also include teleworking. In general, the following methods for data backup at the teleworkstation are available:

* Data backup on external data carriersHere, the teleworkstation must have the necessary technical equipment. In addition to the necessary external data carriers, this includes the necessary hardware and software of the computer. In addition, the teleworker must be trained to make the backups independently.
* Data backup via network The backup of the local data can also be done via the connection to the network of the institution. The advantage here is that on the one hand, the backup does not have to be done independently by the teleworkers and on the other hand, the teleworkers have to manage any media. Decisive in the data backup over a network connection is that their transmission capacity for the volume of data to be backed up is sufficient. Depending on the backup program, it is possible to transfer only changes to the database since the last backup (incremental backup). In many cases, this can greatly reduce the volume of data to be transported. An important requirement of the backup program is that unexpected disconnects are detected and handled properly.
In both methods of data protection, it is desirable to minimize the volume of data to be backed up. In addition to lossless compression methods, which are integrated into many backup programs, incremental or differential backup methods can also be used. However, this may increase the overhead of restoring a backup.

The backup should be as automated as possible, so that the teleworkers have to perform only a few actions themselves. If user collaboration is required, they should be required to perform the backup regularly. Finally, it should be sporadically checked whether created backups can be restored.

** Storage of backup volumes **

If data backups are carried out at the teleworkstation, backup data carriers must be kept locked there. It must be ensured that only the teleworker and his representative can access it.

However, one generation of the backup volumes should always be kept in the institution so that the representative can access the backup volumes in the event of a disaster.

#### OPS.1.2.4.M5 Awareness and Training of Teleworkers [Supervisors, Head of IT]

A teleworking memorandum must be used to instruct the teleworkers in the appropriate security measures of the institution. In particular, the following points should be considered:

* Official documents must be stored securely at the teleworkstation, eg locked away in cabinets.
* Windows and outward doors (balconies, terraces) are to be locked when the teleworkstation is left.
* Structural and security changes to teleworking IT may only be made by the institution's administrators.
* The teleworking computer may only be connected via the appropriate connection to public communication networks.
* When exchanging data between data carriers between the IT systems of the institution and the workstation PC at the teleworkstation, only the data carriers procured by the institution may be used. Media should only be transported encrypted. Service and private IT systems or media should be kept separate.
* Unauthorized access to the teleworker's IT is prevented by access locks, such as boot and screen locks. Passwords are generally kept secret.
In addition, the teleworkers are to be trained in dealing with the telework computers so far, that they can make simple error corrections (for example, change printer cartridges) or solve simple problems independently.

The requirements of the module ORP.3 * Sensitization and Information Security Training * should also be taken into account for the orderly and structured approach to teleworker safety instructions.

### 2.2 Standard measures

Together with the basic measures, the following measures are in line with the state of the art in teleworking.

#### OPS.1.2.4.M6 Creating a security concept for teleworking [Supervisor, Head of Organization, Head of IT]

A teleworking security concept should be developed outlining the security objectives, the protection needs of teleworking information, and the risks and security measures.

Teleworking usually processes information outside of the protected operating environment. It is therefore necessary to establish in advance the protection of the information, business processes, applications, IT systems, communication links and rooms (especially teleworking) regarding confidentiality, integrity and availability. From the protection requirements of the data to be processed at the teleworkstation, the security objectives and thus the safety requirements for the teleworkers, the teleworkers and the teleworking workplaces are derived.

In addition to an overview of the threat situation and the organizational, infrastructural and personnel security measures, measures from the following areas may be useful:

* Dealing with data and resources that are worth protecting, such as documents and storage media, in particular regulations for making copies and for deleting or destroying data carriers.
* Securing communication (for example by encryption, electronic signature) between institution and teleworkplace,
* Authentication mechanisms,
* Regulations for further network connections,
* Regulations for data exchange,
* Data backup.
In addition, various laws and regulations must be observed when designing teleworking (see OPS.1.2.4.M1 * Teleworking regulations *).

The requirements, objectives and measures to be taken for telework safety must be documented. The security concept for teleworking has to be harmonized and harmonized with the overarching security concept of the institution. It also needs to be regularly updated and adapted to changes in the institution or technology.

The security measures to be implemented by the teleworkers are to be grouped together in a security guideline for telework.

#### OPS.1.2.4.M7 Regulated use of communication options for teleworking [teleworker, IT operation]

For teleworking typically various communication options, such as telephone, fax and Internet connection, but also mail exchange and file and data carrier transport is required.
It must be regulated how the existing communication possibilities may be used. The exchange of mail as well as the file and data carrier transport between institution and teleworkplace must also be considered. Similarly, the private use of communication options should be clearly regulated, eg. B. the Internet connection. All regulations must be fixed in writing (see * OPS.1.2.4. * M1 * Teleworking regulations *) and handed over to the teleworkers.

To clarify are at least the following points:

** flow control **

The exchange of information between the teleworking center and the institution must be regulated in such a way as to ensure the security of the information.

* Which services may be used for information exchange and data transmission?
* What information may be given to whom?
* Which services may not be used explicitly?
* Which correspondence may be processed by e-mail? Is there a signature regulation for communication?
* Which authentication methods are used for correspondence and data exchange?
* Are digital signatures used?
** Access Permissions ** If the teleworker needs access to the IT of the institution (for example, a server), it should first be determined which objects (eg data or IT) are actually needed for his tasks. The required access and access rights should be assigned according to the stipulated requirements of the institution.

** Security measures for information exchange ** Information exchange in teleworking must be adequately secured. Confidential information must be transported safely. At least the following questions have to be answered:

* For which media should which shipping method be used (for example, courier service)? What type of transport security is appropriate (for example, envelopes with security labels)?
* For which data should which encryption methods be used? As far as possible, data should be encrypted during data transmission and on data carriers so that transport losses endanger their availability at best and not their confidentiality.
* Are backup copies of data to be transferred, which were created or compiled solely for the purpose of data transmission?
* For which data is a deletion necessary after a successful transfer? This can for example apply to personal data.
* From which data should a copy of the data remain on the teleworking computer despite the successful transmission?
* Is a malware check of the data performed prior to shipping and receiving data?
* For which data transfers should logging be carried out? If automatic logging of data transmissions should not be possible, it should be determined whether and to what extent handwritten logging should be provided for.
** Internet use ** It is to be regulated whether Internet services can be used via the telework computer. It should also be clarified whether a private use is allowed. Questions to be clarified:

* Is the use of Internet services generally prohibited?
* Which internet services may be used?
* May I download data from the internet? Data from third-party servers may be in danger of malicious software.
* Which framework conditions and technical security measures must be observed when using the internet? Which security mechanisms should be activated in the browser, for example?
* Can teleworkers participate in the exchange of information via Internet platforms, newsgroups, blogs or similar? Is this a pseudonym required?
#### OPS.1.2.4.M8 Flow of information between teleworker and institution [supervisor, teleworker]
To ensure that teleworkers are not excluded from the workplace, a regular exchange of information between the teleworkers and the work colleagues of the institution must take place. Both supervisors and teleworkers are responsible for this. The respective supervisors must ensure that teleworkers * * receive all necessary information for their work areas. Teleworkers, however, must also independently ask for information and news. The regular exchange of information is important so that teleworkers are aware of plans and objectives in their field of work.

Teleworkers should be involved in the circulation procedure for house communications, pertinent information and journals. This poses a problem when teleworkers work exclusively at home. One solution is to scan important documents to send to teleworkers by e-mail. In any case, teleworkers must be informed promptly about changes in security measures and other security-related aspects.

The co-workers in the institution must be informed about the presence and availability of teleworkers. The corresponding e-mail addresses and telephone numbers should be known to all colleagues. In addition, a call forwarding from the telephone connection of the employee in the institution to the telephone at the teleworkstation should be established.

The following points must also be clarified in teleworking:

* Who is the contact person for technical and / or organizational problems with teleworking?
* Who must be notified of security incidents?
* How is the task assignment?
* How is the transfer of the work results carried out?
If technical-organizational problems arise, these must be reported immediately by the teleworker to the institution.

#### OPS.1.2.4.M9 Care and maintenance concept for teleworking jobs [teleworker, IT manager, IT operations]

For teleworking a special care and maintenance concept should be created, which provides the following points:

* ** Name User Service Contacts: ** This is where teleworkers can contact for software and hardware issues. The user service tries to provide help (also by telephone) at short notice or initiates maintenance and repair work. For this, the user service should know the configuration of the telework computers.
* ** Maintenance Dates: ** The dates of maintenance on the teleservices should be announced early, so that the teleworkers at these times the maintenance technicians access to the teleworkplace or access to teleworking computer grant or bring to IT equipment waiting to be brought into the institution.
* ** Introduction of standard teleworkers: ** The IT equipment of all teleworkers in an institution should be standardized so that the user service can quickly help with problems. It also reduces the conceptual and administrative effort required to set up a secure teleworking computer.
* ** Remote maintenance: ** If the teleworking computer can be administered and maintained via remote maintenance, the necessary security measures must be clarified. In addition, the time for on-line maintenance access must be agreed with the teleworkers concerned. To ensure that remote access can not be abused, appropriate safeguards must be established.
* ** Transportation of the IT: ** It should be determined for reasons of liability who is authorized to transport IT equipment and other equipment for teleworking between the institution and the teleworking stations. At the same time the protection of the devices must be considered. For example, a laptop can be transported by the teleworker personally, but should be equipped with an anti-theft device. The information should be encrypted.
#### OPS.1.2.4.M10 Implementation of a requirement analysis for the teleworking station [Head IT, IT Operations]

Before a teleworkstation is set up, a requirements analysis should be carried out. The purpose of this requirement analysis is to determine all possible application scenarios in order to derive the required hardware and software components. The results of such a requirement analysis must be documented and agreed with the IT managers.

Among other things, the following questions must be clarified in the scope of this requirement analysis:

* Up to which confidentiality claim may data be processed at the teleworkstation?
* For what purpose is access to the institution used (querying information, posting information, using the program)?
* How high is the traffic between the teleworkplace and the institution?
* Does the teleworker need to access the intranet of the institution? If so, does it have to be able to access the entire intranet, ie all available data and services or only parts of the intranet?
* Is the use of the internet intended for teleworkers? If so, does the teleworker have their own Internet access or is this access realized via the intranet of the institution?
Depending on the confidentiality of the data, it may be necessary to specify certain transmission paths from the institution to the teleworkstation. It may make sense to exclude individual transmission paths or set minimum requirements for it. For example, it might be compulsory to transport paper documents containing confidential information only directly from the institution to the teleworkstation in sealed transport containers. Likewise, different encryption methods for data transmission could be provided for different degrees of confidentiality.

Similar considerations should be made when the information to be processed by teleworking needs to be specially protected against manipulation.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Further information on hazards and security measures in the field of telework can be found in the following publications, among others:

* #### [27001A6.2.1] ISO / IEC 27001: 2013 - Annex A.6.2.1 Mobile device policy

  

 Information technology- Security techniques- Information security management system - Requirements, in particular Annex A, A.6.2.1 Mobile device policy, ISO, 2013

 
* #### [NIST80046] NIST Special Publication 800-46 Revision 2

  

 Guide to Enterprise Telework, Remote Access and Bring Your Own Device (BYOD) Security, NIST, 07.2016
 <Http://dx.doi.org/10.6028/NIST.SP.800-46r2>
* #### [NISTPA2] Area PA2 Mobile Computing

  

 especially Area PA2 Mobile Computing, Information Security Forum (ISF), 06.2016
