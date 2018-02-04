Table of content

[toc]
 
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
If the allocation of access, access and access rights is poorly regulated, this will quickly lead to serious security vulnerabilities, eg. B. by wild growth in the rights allocation. When introducing identity management systems or revisions, it often turns out that different people in different organizational units are responsible for assigning authorizations. This quickly causes users to receive permissions on demand, or conversely, only through unnecessarily complicated ways to get them. Thus, on the one hand, missing authorizations can hinder the daily work, on the other hand, authorizations can be granted without requirement and thus pose a security risk.
