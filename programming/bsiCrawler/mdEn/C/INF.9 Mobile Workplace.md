description
-------------

### 1.1 Introduction

Good network coverage and powerful IT equipment, such as: For example, laptops, smartphones, or tablets allow employees to work almost anywhere, from anywhere. This means that official tasks are often performed not only in the rooms and buildings of the institution, but in changing workplaces in different environments, eg. In hotel rooms, trains or at customers. The information processed must be adequately protected.

On the one hand, mobile work changes the duration, location, and distribution of working hours, and on the other hand, it increases information security requirements because mobile workplace environments can not assume the security of an IT infrastructure found in an office environment.

### 1.2 Objective

The module describes security requirements for mobile workstations. The aim is to create a security situation comparable to an office space for such workplaces.

### 1.3 Delimitation

The module contains fundamental requirements that must be observed and fulfilled when employees often work not only within the premises of the institution, but at changing workplaces outside.

Above all, it depicts the organizational, technical and personnel requirements for wholly or partially mobile work. In order to secure IT systems, data carriers or documents used during mobile work, all relevant components must be used, such as SYS.3.1 * laptop *, SYS.3.2 * tablet and smartphone, * SYS.3.4 * mobile data carrier, * NET .3.3 * VPN, * SYS.2.1 * General Client, INF.1 Building or INF.8 Home Workplace * must be considered separately.

Likewise, the security requirements for VDU workplaces that are fixed by the employer (teleworking) are not the subject of this module, but are described in OPS.1.2.4 * Teleworking *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the * * mobile workspace area:

### 2 1 Lack of or inadequate regulations for mobile workplaces

If the mobile work is not or only insufficiently regulated, the institution may incur financial damages. If, for example, it is not regulated which information may be transported and processed outside of the institution and which safeguards must be adhered to, confidential information can get into the wrong hands. These may then be used by unauthorized persons to the serious disadvantage of the institution.

### 2 2 Impaired by changing operating environment

As mobile data carriers and end devices are used in very different environments, they are exposed to a variety of threats. These include, for example, damaging environmental influences (for example, high or too low temperatures), as well as dust, moisture or transport damage.

In addition to these influences, the operating environments with their different levels of security must be taken into account. Especially smartphones, tablets, laptops and similar mobile devices are not only mobile, but can also communicate with other IT systems. In this case, for example, malicious programs can be transmitted or sensitive information can be copied. In this way, tasks may no longer be fulfilled, customer appointments may not be performed, or IT systems may be damaged.

### 2 3 Manipulation or destruction of IT systems, accessories, information and software on the mobile workstation
It may be easier to manipulate or destroy IT systems, accessories, information and software that are used on a mobile device than in the institution. The mobile workstation is often accessible to third parties. Also here the central protective measures of the institution are not present, for example, porter services. If IT systems, accessories, information or software are manipulated or destroyed, the employee at the mobile workstation is often only able to work to a limited extent. In addition, destroyed IT components or software solutions may need to be replaced, which requires both financial and time resources.

### 2 4 Delays due to temporarily limited accessibility

Most employees at the mobile workstation have no fixed working hours and are sometimes difficult to reach on the way. This can significantly delay the flow of information. Even if the information is transmitted via e-mail, the response time is not necessarily shortened because it can not be guaranteed that the mobile employee reads the e-mail in a timely manner. Depending on the situation and institution, temporary accessibility has different effects, but it can severely limit the availability of information.

### 2 5 Unsecured file and disk transport

When documents, data carriers or files are transported between the institution and the mobile workstations, this information and data can be lost or stolen, read or manipulated by unauthorized third parties. As a result, the institution may incur greater financial damages. File and disk transport can be insufficiently secured in several ways:

* If unique items are transported (missing backup), goals and tasks can not be achieved as planned after loss.
* If unencrypted data carriers fall into the wrong hands, this can lead to serious confidentiality losses.
* If there is insufficient access protection on the way, files or data carriers can be copied or manipulated unnoticed.
### 2 6 Inappropriate disposal of data media and documents

If it is not possible to properly dispose of data carriers and documents at the mobile workstation, these usually go into the household waste. Even where work is being done on the move, employees often throw drafts and other supposedly useless documents directly into the next wastebasket or simply leave them lying in the hotel or on the train. However, if data carriers or documents are not properly disposed of, attackers can derive valuable information that can be deliberately misused for blackmail or industrial espionage. The consequences range from the loss of know-how to the threat to the existence of the institution, for example, if important orders fail to materialize or partnerships fail.

### 2 7 Confidentiality loss of sensitive information

At the mobile workstation, attackers can more easily access sensitive information stored on hard drives, removable media, or paper, especially if they are professional. They can also listen to communication links. However, if information is read or disclosed unauthorized, it will have serious consequences for the entire institution. Among other things, the loss of confidentiality may result in the institution violating laws or creating competitive disadvantages and financial loss.

### 2 8 Theft or loss of data carriers or documents

The mobile workstation is not as well secured as the workplace in a company or agency. During a train journey, from a hotel room or sometimes also from conference rooms to customers, it is easier to steal official IT and documents.
In addition, IT systems or components can be lost. In addition to the purely material damage caused by the immediate loss of the mobile device, the disclosure of sensitive data (eg e-mails, notes from meetings, addresses or other documents) may result in further (financial and / or reputational) damage.

### 2 9 Lack of security awareness and carelessness in handling information

Often it can be observed that organizational regulations and technical security measures for portable IT systems and mobile data carriers exist in institutions, but these are again undermined by the careless handling of specifications and technology. So z. B. repeatedly observed that brought along mobile data carriers are left unattended in the meeting room or in the train compartment during breaks.

In addition, gifts in the form of data carriers, such as. As USB sticks, accepted by employees and thoughtlessly connected to your own notebook. Here then the notebook can be infected with malware and thereby protected information can be stolen, manipulated or encrypted and thus made temporarily unusable.

In public transport or during business lunches, it can be observed again and again that people are having open discussions about business-critical information. These can then easily be overheard by outsiders and may be used to the grave disadvantage of the employee or his institution.

3 requirements
---------------

The following are specific requirements for the protection of mobile workstations. Basically, the Information Security Officer (ISB) is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### INF.9.A1 Appropriate selection and use of a mobile workstation [supervisor, user]

The institution MUST impose on its employees how mobile workplaces should be properly selected and used. It is necessary to define properties that are desirable for a mobile workstation, but also exclusion criteria that speak against a mobile workstation. At least MUST be regulated:

* under which workplace conditions sensitive information may be processed,
* how employees at the mobile workstation protect themselves from unwanted insights from third parties,
* whether a permanent mains and power supply must be given and
* which workplace environments are completely prohibited.
#### INF.9.A2 Arrangements for mobile workplaces [Head IT, users]

For all work on the way MUST be regulated, which information outside the company or the authority may be transported and processed and what safeguards must be taken. It also MUST be clarified under which conditions employees with mobile IT systems may access internal information of their institution.

In addition, the IT components and data carriers must be clearly regulated. It is therefore necessary to determine which IT systems and data carriers may be taken, who can take them with them and which basic security requirements must be observed. It also MUST be logged when and by whom, which mobile devices were used outside the home.
Mobile device users MUST be made aware of the value of mobile IT systems and the value of information stored on them. You MUST be informed about the specific hazards and measures of the equipment they use. In addition, they MUST be informed about what kind of information may be processed on mobile IT systems. All users MUST be advised of the applicable regulations that must be followed by them and trained accordingly.

#### INF.9.A3 Access and Access Protection [Staff]

The employees MUST be informed about the regulations and measures for burglar and access protection at the mobile workplace. MUST be advised to close windows and close doors when the mobile workstation is not occupied (this is possible, for example, in hotel rooms). If this is not possible (eg on the train), the employees MUST store all documentation and IT systems in a safe place if they are absent. It MUST be ensured that unauthorized persons can not access official IT and documents at any time.

If rooms are left only briefly, the clients used MUST be locked or shut down so that they can only be used again after successful authentication.

#### INF.9.A4 Working with external IT systems [supervisors, users]

The institution MUST regulate how employees should work with external IT systems. Because the level of protection afforded by such IT systems can vary widely from that of one's own institution, each mobile employee MUST be aware of the dangers of using third-party IT systems. The regulations MUST specify whether and how sensitive information may be processed on external IT systems and how it prevents unauthorized persons from viewing the information. When employees work with third-party IT systems, it is essential to ensure that all temporary data created during this process is deleted.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of mobile workstation. They SHOULD be implemented in principle.

#### INF.9.A5 Timely loss report [employee]

Employees SHOULD immediately report to their institution if any information, IT systems or data media were lost or stolen. For this purpose, there should be clear reporting channels and contact persons within the institution.

#### INF.9.A6 Disposal of confidential information [staff, building services]

Confidential information SHOULD be safely disposed of, so do not just throw it in the trash. Before disposing of used or defective data carriers and documents, it MUST be checked whether they contain sensitive information. If this is the case, the data carriers and documents MUST be transported back with them and disposed of or destroyed by the institute.

#### INF.9.A7 Legal framework for mobile work [Head of Human Resources, Human Resources]

For mobile work, labor law and labor protection framework conditions SHOULD be observed and regulated. All relevant points SHOULD be governed either by company agreements or by individual agreements made between the mobile employee and the employer in addition to the employment contract.

#### INF.9.A8 Mobile Workplace Security Policy [IT Leader]
All relevant security requirements for mobile workstations SHOULD be documented in a mandatory security policy for mobile workers. In addition, it SHOULD be coordinated with the existing security guidelines of the institution as well as with all relevant specialist departments. Also, the security policy for mobile workstations SHOULD be updated on a regular basis. Likewise, it SHOULD specify that a representative be named for each mobile employee and that the substitution process be rehearsed on a regular basis. The staff of the institution SHOULD be sensitized and trained with regard to the current security policy.

#### INF.9.A9 Encryption of Portable IT Systems and Media [User]

To ensure that information worthy of protection can not be viewed by unauthorized third parties, SHOULD it be ensured that they are protected in accordance with the internal guidelines. Mobile data carriers and clients SHOULD be encrypted. The cryptographic keys SHOULD be kept separate from the encrypted device.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### INF.9.A10 Using anti-theft devices (CIA)

If the IT system used offers an anti-theft device, SHOULD it be used. The theft deterrents SHOULD always be used where there is an increased public traffic or the fluctuation of users is very high. In doing so, the employees SHOULD ALWAYS keep in mind that the protection of the information stored on the IT systems usually has a higher value than the re-acquisition costs of the IT system. The procurement and deployment criteria for anti-theft devices SHOULD be adapted to the processes of the institution and documented.

#### INF.9.A11 Ban on the use of unsafe environments (CIA)

It SHOULD set criteria for the work environment that must be met at least so that information with increased protection requirements can be handled on the go. The criteria should cover at least the following topics:

* Access and access by third parties,
* closed and, if necessary, lockable or guarded rooms,
* secure communication options and
* adequate power supply.
4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and security measures in the area of ​​mobile workplaces can be found in the following publications, among others:

* #### [27001A11.2] ISO / IEC 27001: 2013 - Annex A.11.2 Equipment

  

 Information technology- Security techniques- Information security management systems- Requirements, in particular A.11.2 Equipment, ISO, 2013

 
* #### [27001A6.2.1] ISO / IEC 27001: 2013 - Annex A.6.2.1 Mobile device policy

  

 Information technology- Security techniques- Information security management system - Requirements, in particular Annex A, A.6.2.1 Mobile device policy, ISO, 2013

 
* #### [ISFPA2] Information Security Forum (ISF), June 2016, specifically Area PA2 Mobile Computing

  

 Information Security Forum, in particular Area PA2 Mobile Computing, ISF, 06.2016

 
* #### [NIST80046] NIST Special Publication 800-46 Revision 2

  

 Guide to Enterprise Telework, Remote Access and Bring Your Own Device (BYOD) Security, NIST, 07.2016
 <Http://dx.doi.org/10.6028/NIST.SP.800-46r2>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------
The following elementary hazards are important for the "Mobile Workplace" building block.

* G 0.14 Spying out information (spying)
* G 0.16 Theft of devices, data carriers or documents
* G 0.17 Loss of equipment, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.24 Destruction of equipment or data media
* G 0.25 Failure of devices or systems
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.44 Unauthorized intrusion into premises
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
