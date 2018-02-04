[toc]
 
1 description
--------------

### 1.1 Introduction

A web server is the core component of every web offer: It accepts requests from the clients (browsers) and, if possible, returns the corresponding content. The data is usually transported via the Hypertext Transfer Protocol (HTTP) or its version encrypted with Transport Layer Security (TLS) HTTP Secure (HTTPS). Because web servers provide a simple interface between server applications and users, they are also commonly used for internal information and applications in institutional networks (intranets).

Web servers are (mostly) available directly on the Internet and thus offer an exposed attack surface. Therefore, they must be protected by appropriate protective measures.

### 1.2 Objective

The goal of the module is to protect the web server and the information provided by the web server.

### 1.3 Delimitation

The term web server is used for both the software that answers the HTTP requests and the IT systems that run this software. This module primarily looks at the web server software. Security aspects of the IT system on which the web server software is installed are handled in the corresponding building blocks of the IT systems layer (see SYS.1.1 * General Server * and, for example, SYS.1.3 * Server under Linux or * SYS.1.2. 2 * Windows Server 2012 *).

Recommendations on how to integrate web servers into the network architecture and secure them with firewalls can be found in the building blocks NET.1.1 * Network Architecture and Design * or NET.3.2 * Firewall *.

Dynamic content and HTML-beyond functions are provided by web applications or web services. These are not the subject of this module, but are covered in the modules APP.3.1 * Web Applications * and APP.3.5 * Web Services *.

The module CON.1 * Crypto Concept * describes how cryptographic keys can be managed securely.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the web server area:

### 2 1 Reputational loss

If attackers manage to manipulate or redesign a website (defacement), the reputation of the institution can be damaged. Similarly, the publication of false information (such as misleading product descriptions) may result in the reputation of the institution being lost to the public or the institution being warned. Damage can also occur if the website is unavailable and potential customers switch to competitors.

### 2 2 Manipulation of the web server

An attacker can gain access to a web server to manipulate files. For example, he could change the configuration, start additional services, install malware, or modify web content. He could also replace files that are offered for download by files with malicious programs. Also, an attacker may use the compromised server, for example, to perform DDoS (Distributed Denial of Service) attacks. If your own server is used to distribute malicious software, it can happen that the web server is run on blacklists and is no longer accessible to visitors.

### 2 3 Distributed Denial of Service (DDoS)

Due to DDoS attacks, a web server can partially or completely fail. For users, the web site is then only very slow or no longer available. For many institutions, such a failure is quickly critical to business, eg. B. for an online store.
In addition to DDoS, other types of denial-of-service attacks can affect the availability of a website specifically for individual users by, for example, blocking individual accounts from incorrect logins. An attacker could z. For example, a user account lock could be triggered by invalid login attempts.

### 2 4 Loss of confidential data

Many web servers still use outdated cryptographic techniques, such as RC4 or SSL. Inadequate authentication or inappropriate encryption can lead to attackers being able to read or change the communication between the clients and the servers or between the servers.

### 2 5 Violation of laws or regulations

Violations of legal regulations, in particular against telemedia and data protection laws, can have legal consequences. Further, the web server contents may violate copyright, such as when using images for which no rights have been acquired.

### 2 6 Software vulnerabilities or errors

If updates and patches for web servers or used extensions are not imported or received too late, the web server can be successfully attacked. This allows attackers to manipulate files or services or misuse the web server for further attacks.

### 2 7 Missing or poor troubleshooting

If errors occur during the operation of a web server, this can, for example, affect the availability of the web server. Also, content may be displayed incompletely or security mechanisms fail. If errors are not handled correctly, the operation and protection of the functions and data of a web server is no longer guaranteed.

### 2 8 Insufficient logging of security-relevant events

If security-relevant events are insufficiently logged by the web server, they can not be reconstructed at a later time and the cause can no longer be determined. Critical errors and attacks, such as unauthorized configuration changes, will go unnoticed for so long.

3 requirements
---------------

The following are specific requirements for the Web server area. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### APP.3.2.A1 Secure configuration of a web server

After a web server has been installed, a secure basic configuration MUST be made. For example, the web server process MUST be assigned to a user account with minimal rights. Also, the web server MUST run in an encapsulated environment if supported by the operating system. The web server service MUST NOT have unnecessary write permissions. Unnecessary modules and functions of the web server MUST be deactivated.

#### APP.3.2.A2 Protection of web server files

All files on the web server, especially scripts and configuration files, MUST be protected so that they can not be read and changed without authorization.

It MUST be ensured that the web server application can only access files that are within a defined directory tree (WWW root directory). Resources outside the WWW directory MUST NOT be linked or linked from it.
Furthermore, functions that list directories MUST be disabled. Files that should not be changed MUST be read-only. Confidential data MUST be transmitted encrypted and stored.

#### APP.3.2.A3 Securing file uploads and downloads

All files published using the web server MUST be checked for malware beforehand. In addition, documents MUST be purged of residual information. Retrievable files MUST be stored on a separate hard disk partition.

There must be a maximum size specified for file uploads. For uploads enough space MUST be reserved. The storage location of the uploads MUST be generated randomly and MAY NOT be influenced by the user.

#### APP.3.2.A4 Logging events

The web server MUST log at least the following events:

* successful access to resources,
* Failed access to resources due to insufficient privileges, non-existent resources and server errors, as well as
* general error messages.
The logging data SHOULD be evaluated regularly.

#### APP.3.2.A5 authentication

If clients authenticate to the web server, an encrypted connection MUST be used for this (see APP.3.2.A11 * Encryption via TLS *). The password files on the web server MUST be stored cryptographically secured and protected against unauthorized access.

#### APP.3.2.A6 Timely import of security-relevant patches and updates

The responsible employees MUST inform themselves regularly at various sources about current weaknesses in the web server software used and import security-related updates in a timely manner. Software updates and patches for web servers, as well as additional applications and enhancements MUST be sourced from trusted sources only and must be sufficiently tested before they are installed or deployed. Before any updates or patches are installed, MUST always be sure that the original state of the web server can be restored.

#### APP.3.2.A7 Legal framework for web offers [Information Security Officer (ISB)]

If content is published or services offered to third parties via the web server, various legal framework conditions MUST be observed. Thus the respective Telemedien- and data protection laws as well as the copyright must be adhered to. Also, the accessibility requirements of the Disability Equality Act SHOULD be respected.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​web servers. They SHOULD be implemented in principle.

#### APP.3.2.A8 Planning the use of a web server

In order to select suitable security measures for the web server, it should be planned and documented, for which purpose it should be used and how the web server should be integrated into the existing IT infrastructure. The documentation SHOULD also describe the information or services of the website and the respective target groups. For the technical operation and the web contents, the responsible persons should be determined.

#### APP.3.2.A9 Defining a Security Policy for the Web Server [Information Security Officer (ISB)]

A security policy should be created that identifies the required actions and responsibilities. It should also regulate how to get information on current vulnerabilities, how security measures are implemented and how to proceed when security incidents occur.

#### APP.3.2.A10 Selection of a suitable web host [Information Security Officer (ISB), Head IT]
If the web server is not operated by the institutions themselves, but offers from external service providers are used (web hosting), the institution SHOULD pay attention to the following points when selecting a suitable web host:

* It SHOULD be contractually regulated how the services are to be provided. Security aspects should be recorded in writing in the contract in a Service Level Agreement (SLA).
* For all products offered, the basic installation should be made safe. The service provider SHOULD inform its customers about the risks of additional applications and extensions (plug-ins). In addition, he SHOULD commit himself to regularly refer to existing updates of the programs used.
* The IT systems used for the service provision SHOULD be regularly checked and maintained by the service provider. He SHOULD be required to promptly respond to technical problems or compromise customer systems.
* The service provider SHOULD implement basic technical and organizational measures to protect its information network.
#### APP.3.2.A11 Encryption over TLS

The web server SHOULD provide encryption for all connections via TLS (HTTPS). If an HTTPS connection is offered then all content SHOULD be available over HTTPS. So-called mixed content SHOULD NOT be used. Critical actions, such as logging in to a web application (login), SHOULD be done via HTTPS.

#### APP.3.2.A12 Appropriate handling of errors and error messages

The HTTP information and the error messages displayed SHOULD NOT show the name and version of the web server software. It should also be ensured that the web server only outputs application-specific error messages that serve the information of the user. For unexpected errors, the web server SHOULD go into a secure state.

#### APP.3.2.A13 Web crawler access control

Web crawler access SHOULD be governed by the robots exclusion standard. Content SHOULD be provided with access protection (see APP.3.2.A5 * Authentication *) to protect it from web crawlers that do not adhere to this standard.

#### APP.3.2.A14 Integrity Checks and Malware Protection

It SHOULD be checked regularly if the files and web content are still integer and not changed by attackers. Also, the files SHOULD regularly be checked for malware.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.3.2.A15 Redundancy (A)

Web servers SHOULD be configured redundantly. The Internet connection of the web server and other IT systems, such as the web application server, SHOULD be designed to be redundant.

#### APP.3.2.A16 Penetration Test and Revision [Information Security Officer (ISB), IT Leader] (CIA)
There should be regular penetration tests. The tests SHOULD only be done by reliable, trustworthy and qualified employees or service providers. In advance, all contractors for penetration testing SHOULD make detailed arrangements to conduct and evaluate the tests. Also the consent of all competent authorities SHOULD be obtained. For the test period the respective contact persons SHOULD be binding and reachable. After the penetration test, the results SHOULD be sufficiently protected and treated confidentially. The final report SHOULD be submitted to the ISB.

#### APP.3.2.A17 Advanced authentication methods for web servers (CI)

It SHOULD use advanced authentication methods, eg. Client certificates or multi-factor authentication.

#### APP.3.2.A18 Protection against denial of service attacks (A)

To detect denial-of-service attacks at an early stage, the web server SHOULD be constantly monitored. Furthermore, measures should be defined and implemented that prevent or at least mitigate such attacks.

#### APP.3.2.A19 Creation of an Internet Editorial Team [Specialist, Head of IT] (CIA)

To maintain web offers, a self-employed Internet editorial team should be set up. The Internet editorial team SHOULD include all the roles that were named in the concept for web offers. For extensive web offers, a contact person for web applications SHOULD also be determined. Likewise, processes, procedures, and people responsible should be named in case of problems or security incidents.
