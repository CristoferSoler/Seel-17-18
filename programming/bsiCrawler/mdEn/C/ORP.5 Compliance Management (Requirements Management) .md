1 description
--------------

### 1.1 Introduction

In every institution there are legal, contractual, structural and internal guidelines and guidelines that have to be observed from many different directions. Many of them have a direct or indirect impact on information security management.

The requirements vary depending on industry, country and other conditions. For example, an authority is subject to other external regulations than a stock corporation. The management level of the institution must ensure compliance with the requirements (New German: Compliance) and operate a compliance management system.

Depending on the size of an institution, it may have different management processes that deal with different aspects of risk management, such as: Security management, privacy management, compliance management, controlling. They should work together in a spirit of trust in order to exploit synergy effects and resolve conflicts at an early stage.

### 1.2 Objective

The aim of the module Compliance Management is to show how an overview of the various requirements of the individual areas of an institution can be created at any time. It describes how security requirements can be derived from legal, contractual, structural and internal guidelines and specifications.

### 1.3 Delimitation

This module looks at selected requirements that result from legal or contractual requirements and that have an impact on the design of information security in the institution. It does not address sectoral laws.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in compliance management:

### 2 1 Violation of legal requirements

The inadequate implementation of information security can lead to violations of legal regulations or contractual agreements. In addition, institutions must observe a multitude of sector-specific, national and international legal framework conditions. Since this can be very complex, it can happen that unintentional violates legal requirements or this is even deliberately accepted. Example:

* Many cloud service providers offer their services in an international environment. Thus, the providers are often subject to other national laws. Often cloud users only see at low costs and estimate the legal framework conditions to be respected, such as data protection, information requirements, insolvency law, liability, information access for third parties.
### 2 2 Improper disclosure of information

Due to the misconduct of persons, it may happen that information worth protecting is inadmissible. Examples for this are:

* Confidential information is discussed within earshot of other people, such as in a talk break from meetings or via mobile phones in public environments.
* The manager of a department suspects an employee to cooperate with the competition. To prove this to him, he asks the head of IT operations to give him "on the small way" insight into the emails of this employee. The IT operations manager instructs the mail administrator to set up access for this without obtaining the necessary consents.
### 2 3 Inadequate identification check of communication partners
In personal conversations, on the phone or in e-mails, many people are willing to divulge much more information than they would in writing or in large groups. Often the communication partner is tacitly expected to treat the conversation or e-mail content confidentially. In addition, there is a tendency not to question the identity of the communication partner, as this is perceived as rude. Likewise, permissions are often not checked sufficiently, but implicitly derived from the (claimed) role. Typical examples are:

* An employee receives an e-mail from an alleged friend of his supervisor, allegedly agreeing to the fast transfer of an outstanding amount.
* A man in a blue jacket with a mounting case gains access to the data center after mumbling something about "water pipes".
### 2 4 Accidental disclosure of internal information

When passing on information, it happens again and again that in addition to the desired information inadvertently also other information is transmitted. This may result in confidential, appropriate information falling into the wrong hands. examples for this are

* old files or residual information on shared media, transmission of data other than intended or sent to wrong recipients.
* In 2015, a French TV station was unable to broadcast a program for hours after hackers gained access to internal IT systems. In a press conference, after the station was able to work again, a notice board was transmitted in the background around the world, where passwords for all sorts of internal and external identifiers hung.
3 requirements
---------------

The following are specific requirements for * compliance management *. Basically, the Change Manager (Compliance Manager) is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### ORP.5.A1 Identification of the legal framework [Head of Organization, Head of Institution]

The institution MUST have a process in place to identify all relevant legal, contractual and other requirements. All legal frameworks that affect security management MUST be identified and documented.

The statutory and contractual requirements relevant to the individual areas of the institution SHOULD be worked out in a structured overview. The documentation MUST be kept up to date. The requirements identified as security-relevant MUST be incorporated in the planning and design of business processes, applications and IT systems, or in the procurement of new components.

#### ORP.5.A2 Observance of legal framework conditions [Supervisors, Head of Organization, Institution Management]

Managers who have the legal responsibility for the local institution MUST ensure compliance with legal requirements. The responsibilities and responsibilities for compliance with legal requirements MUST be defined.

Appropriate measures MUST be identified and implemented to avoid violations of relevant requirements. If violations of relevant requirements are identified, appropriate corrective actions MUST be taken to correct the deviations.

#### ORP.5.A3 Employee commitment to comply with applicable laws, regulations and regulations [Supervisor, Human Resources]
All employees MUST be trained in and required to comply with applicable laws (such as privacy), regulations and internal regulations. Employees MUST know which legal framework determines their activity.

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​compliance management. They SHOULD be implemented in principle.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are in line with the state of the art in the area of ​​compliance management (requirements management). They SHOULD be implemented in principle.

#### ORP.5.A4 Conception and Organization of Compliance Management [Institutional Management]

Appropriate processes and organizational structures SHOULD be established to provide an overview of the different legal requirements for each area of ​​the institution. For this purpose, responsible persons SHOULD be named and their duties in relation to compliance management determined.

Compliance Managers and ISB SHOULD collaborate regularly. Together, they SHOULD integrate security requirements into compliance management, translate security-relevant requirements into security measures and monitor their implementation.

#### ORP.5.A5 Exemptions [Supervisors, Information Security Officer (ISB)]

In individual cases, it may be necessary to deviate from the provisions made. However, justified exceptions SHOULD in any case be approved by an authorized body after a risk assessment. It SHOULD give an approval procedure for exemptions. It SHOULD give an overview of all issued exemptions. An appropriate procedure for documentation and a review process SHOULD be established. All exemptions SHOULD be temporary.

#### ORP.5.A6 Instructing the staff in the safe handling of IT [Supervisors, Human Resources]

All employees and all external IT users SHOULD be instructed in the safe handling of the IT of the institution. In addition, they should be given a binding, understandable, up-to-date and available IT use policy. This policy SHOULD describe what rights and obligations you have in IT use and what security measures you should take. Changes SHOULD be announced to employees in good time.

#### ORP.5.A7 Maintaining Information Security [Information Security Officer (ISB)]

In order to maintain and continuously improve the existing security level, all security measures of the security concept should be regularly checked for compliance and improvement. The tests SHOULD be carried out by independent, qualified, internal or external persons. The results of the checks SHOULD be comprehensibly documented and announced to the management. Defects found SHOULD be corrected promptly.

#### ORP.5.A8 Regular reviews of Compliance Management

The aim was to establish a procedure for regularly checking compliance management and the resulting requirements and measures for efficiency and effectiveness (see also DER.1.3 Audits and Revisions). It SHOULD regularly be checked if the organizational structure and the processes of compliance management are still appropriate.

### 3.3 Requirements for increased protection requirements
Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### ORP.5.A9 Protection against subsequent changes to information [Information Security Officer (ISB), user] (I)

In order to prevent files from being altered unnoticed, sufficient security measures should be taken. Depending on the data format and protection requirements, suitable methods SHOULD be selected. These include, for example, digital signatures and other cryptographic methods, copyright notices or the use of file formats that make subsequent changes or partial further processing more difficult. Employees SHOULD be informed about which security mechanisms should be used and how they should be used.

#### ORP.5.A10 Classification of Information (CIA)

There are in many areas of an institution information that has a higher need for protection or special restrictions, such. Personal, financial, confidential or copyrighted information. Depending on their categorization, they are subject to different restrictions when dealing with them. Therefore, if possible, all information should be classified according to its protection needs and, if possible, marked. Employees SHOULD regularly be advised of the careful handling of information and of the restrictions on the handling of classified data.

#### ORP.5.A11 Survey of the legal framework for cryptographic processes and products [IT operation, person responsible for the individual applications] (CI)

When using cryptographic products, various legal conditions must be observed. The legal framework for the use of cryptographic procedures and products SHOULD be determined and documented for all countries in which they are to be used.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the area of ​​compliance management can be found in the following publications:

* #### [19600] ISO 19600: 2014

  

 ISO, compliance management systems, 2014

 
* #### [27002K18] ISO / IEC 27002: 2013 Chapter 18 Compliance

  

 ISO, Information Technology-Security Technique- Code of Practice for Information on Security Controls, especially Chapter 18 "Compliance", 2013

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "Compliance Management".

* G 0.29 Violation of laws or regulations
The cross reference tables can be found in the download area due to their size.
