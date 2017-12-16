1 description
--------------

### 1.1 Introduction

Users or even IT components that access the resources of an institution must be unequivocally identified and authenticated. The management of the necessary information is called identity management.

Authorization management is about whether and how users or IT components are allowed to access and use information or services, that is, grant or deny them access, access or access based on the user profile. Authorization Management refers to the processes required to assign, revoke, and control rights.

The transitions between the two terms are fluid, so the term Identity and Access Management (IAM) is used in this module.

### 1.2 Objective

The goal of the building block is for users or even IT components to be able to access only the IT resources and information they need for their work and for which they are authorized and to deny access to unauthorized users or IT components. For this purpose, requirements are formulated with which institutions should establish secure identity and authorization management.

### 1.3 Delimitation

This module describes basic requirements for the development of identity and authorization management.

Requirements concerning components of an identity and authorization management, such as operating systems or directory services, can be found in the corresponding blocks (eg SYS.1.3 Unix server, SYS.1.2.2 Windows Server 2012, APP.2.1 General directory service, APP.2.2 Active Directory).

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​*** *** identity and authorization management:

### 2 1 Lack of or insufficient processes for identity and entitlement management

If identity and authorization management processes are inadequately defined or not followed, the administrator responsible may not receive information about personnel changes. This can mean, for example, that a user account of a departed employee is not deleted. He can thus continue to access sensitive information or cloud applications.

Also, it is possible that employees who have been moved to a new department retain their old permissions and thereby accumulate extensive overall permissions over time.

### 2 2 Lack of central deactivation of user access

In institutions, employees often have user access to various IT systems such as production, test, quality assurance or project systems. These are usually in different areas of responsibility and are managed by different administrators. As a result, an identical and unique user ID is not used on all IT systems and there is usually no central overview of the user access on the individual IT systems. In such a scenario, it is not possible to immediately disable all user accesses of an employee in the event of an attack or password theft. Also, when an employee leaves the institution, all receipts can not be blocked immediately.

### 2 3 Inappropriate access, access and access rights management
If the allocation of access, access and access rights is poorly regulated, this will quickly lead to serious security vulnerabilities, eg. B. by wild growth in the rights allocation. When introducing identity management systems or revisions, it often turns out that different people in different organizational units are responsible for assigning authorizations. This quickly causes users to get permissions on demand or, conversely, get them over unnecessarily complicated ways. Thus, on the one hand, missing authorizations can hamper the daily work, on the other hand, authorizations can be granted without requirement and thus pose a security risk.

3 requirements
---------------

The following are specific requirements for identity and entitlement management. Basically, the ISB is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### ORP.4.A1 Regulation for the creation of users and user groups [Administrator, IT Leader]

It must be governed by how users and user groups are to be set up. All users and user groups MAY ONLY be set up via separate administrative roles.

#### ORP.4.A2 Regulation for setting up, changing, and revoking privileges [Administrator, Head of IT]

User IDs and permissions MAY ONLY be assigned based on actual needs. Personnel changes MUST remove the user IDs and permissions that are no longer required. Applying Employees Authorizations that go beyond the standard may ONLY be assigned after further justification. All permissions MUST be set up via separate administrative roles.

#### ORP.4.A3 Authorized User and Rights Profile Documentation [Administrator, IT Leader]

There must be a documentation of the authorized users, created user groups and rights profiles. The documentation of the authorized users, created user groups and rights profiles MUST be regularly checked for up-to-dateness. The documentation MUST be protected against unauthorized access. If done electronically, SHOULD be involved in the data protection process.

#### ORP.4.A4 Task distribution and separation of functions [Head IT]

It is necessary to define the tasks and functions that are relevant for the IT deployment. It MUST also be determined which tasks and functions are incompatible. These separations MUST be implemented. They SHOULD be documented.

#### ORP.4.A5 Assignment of access authorizations [Head IT]

It MUST be specified which access rights are assigned to which persons within their function. If access means such as chip cards are used, the issue or withdrawal MUST be documented. The authorized persons SHOULD be trained in the correct handling of the access equipment. For longer absences authorized persons SHOULD be temporarily suspended.

#### ORP.4.A6 Assignment of access authorizations [Head IT]

It MUST be determined which access rights are assigned or withdrawn to which persons within their function. If means of access such as chip cards are used, the issue or withdrawal MUST be documented. The authorized users SHOULD be trained on the correct handling of the means of access. For longer absences authorized persons SHOULD be temporarily suspended.
#### ORP.4.A7 Assignment of access rights [Head IT]

It MUST be determined which access rights are assigned or withdrawn to which persons within their function. If means of access such as chip cards are used, the issue or withdrawal MUST be documented. The access rights SHOULD be trained on the correct handling of the means of access. For longer absences authorized persons SHOULD be temporarily suspended.

#### ORP.4.A8 Password Usage Control [User, IT Leader]

The institution MUST fix the password usage. It MUST be specified that only passwords with sufficient length and complexity are used. The passwords SHOULD be changed at appropriate intervals. The passwords MUST be changed immediately as soon as they become known or suspected to unauthorized persons. Passwords MUST be kept secret. Standard passwords MUST be replaced with strong passwords and predefined logins must be changed. It SHOULD be checked that the possible password length is also fully checked by the IT system. In the case of unsuccessful login attempts, the system SHOULD NOT give any indication as to whether the password or user ID is incorrect.

#### ORP.4.A9 Identification and Authentication [Head IT]

Access to all IT systems and services MUST be secured through appropriate identification and authentication of accessing users, services or IT systems. Preconfigured access means MUST be changed prior to productive use.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​identity and authorization management. They SHOULD be implemented in principle.

#### ORP.4.A10 Protection of User Accounts with Extended Privileges [IT Leader]

User accounts with far-reaching permissions SHOULD be protected with at least two authentication features.

#### ORP.4.A11 Reset Passwords [IT Manager]

For resetting passwords, an appropriate secure procedure SHOULD be defined and implemented. Support staff who can reset passwords SHOULD be trained accordingly. If the password requires more protection, a strategy SHOULD be defined if the support staff can not take responsibility due to a lack of secure means of transmitting the password.

#### ORP.4.A12 Development of an authentication concept for IT systems and applications [Head IT]

An authentication concept SHOULD be created. In it, it should be defined for each IT system and each application which functional and security requirements are placed on the authentication. Authentication information SHOULD be cryptographically securely transmitted and stored.

#### ORP.4.A13 Appropriate selection of authentication mechanisms [Head IT]

SHOULD use identification and authentication mechanisms appropriate to the protection needs. Authentication data SHOULD be protected by the IT system or IT applications during processing against spying, alteration and destruction at any time.

#### ORP.4.A14 Checking the effectiveness of user separation on the IT system [Administrator]

At appropriate intervals, it should be checked whether the users of IT systems regularly log off after task fulfillment and not several users work under the same ID.

#### ORP.4.A15 Approach and conception of processes for identity and authorization management [Head of IT]

For identity and authorization management, the following processes SHOULD be defined and implemented:

* Manage policies,
* Manage identity profiles,
* Manage user IDs
* Manage permission profiles,
* Manage roles.
#### ORP.4.A16 Access and Access Control Policy [Administrator]

A guideline should be created for the access and access control of IT systems, IT components and networks. You should use standard rights profiles that correspond to the functions and tasks of the employees. For each IT system and IT application, a written access policy SHOULD exist. In addition, all established users and assigned rights SHOULD be documented. It SHOULD be regulated that users can only access IT systems and services if they have been appropriately identified and authenticated beforehand.

#### ORP.4.A17 Appropriate Selection of Identity and Entitlement Management Systems [IT Leader]

When using an identity and authorization management system, it SHOULD be appropriate for the institution and its respective business processes, organizational structures and processes as well as their protection needs. The Identity and Entitlement Management System SHOULD map the institution's existing requirements for dealing with identities and permissions. The selected identity and authorization management system SHOULD be able to realize the principle of separation of functions. The identity and entitlement management system SHOULD be adequately protected against attacks.

#### ORP.4.A18 Use of a central authentication service [Head IT]

In order to establish a central identity and authorization management, a central network-based authentication service SHOULD be used. The use of a central network-based authentication service SHOULD be carefully planned. For this purpose, the security requirements that are relevant for the selection of such a service SHOULD be documented.

#### ORP.4.A19 Training of all employees in the handling of authentication procedures and mechanisms [user, IT manager]

All employees SHOULD be instructed in the correct handling of the authentication procedures. It SHOULD give clear guidelines for handling authentication procedures. The employees SHOULD be informed about relevant regulations.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### ORP.4.A20 Emergency Prevention for the Identity and Entitlement Management System [IT Leader] (CIA)

It SHOULD be examined to what extent a failed identity and authorization management system is critical to security for the business processes. For emergencies, an authorization concept SHOULD be present and emergency authorizations should exist.

#### ORP.4.A21 Multi-Factor Authentication [IT Leader] (C)

With a higher protection requirement, a secure two- or more-factor authentication, eg. As with cryptographic certificates, smart cards or tokens, are used for authentication.

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the area of ​​"identity and authorization management" can be found in the following publications, among others:

* #### [29146] ISO / IEC 29146: 2016

  

 Information technology - Security techniques - A framework for access management, 06.2016

 
* #### [ISFTS14] The Standard of Good Practices Area TS1.4 Identity and Access Management

  

 ISF, especially Area TS1.4 Identity and Access Management, June 2016

 
* #### [NIST80053A] NIST Special Publication 800-53A
Assessing Security and Privacy Controls at Federal Information Systems, especially Areas AC and IA, 12.2014

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the module "identity and authorization management".

* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.16 Theft of devices, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.36 Identity theft
* G 0.37 denying actions
* G 0.44 Unauthorized intrusion into premises
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
