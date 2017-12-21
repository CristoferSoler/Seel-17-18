1 description
--------------

### 1.1 Introduction

Web applications provide functions and dynamic content over the Internet protocol Hypertext Transfer Protocol (HTTP) or HTTPS (HTTP over SSL or TLS, that is protected by an encrypted connection). For this purpose, documents and user interfaces (eg input masks) are generated on a server and delivered to corresponding client programs (web browser). Web applications are usually developed on the basis of frameworks. These provide a framework for frequently recurring tasks (eg for security components).

To run a web application, several IT system components are usually required. These typically include a web server to deliver data, an application server to run the actual application, and additional background systems attached as data sources across different interfaces (eg, database or directory service).

Web applications are used in both public IT networks and corporate networks (intranets) to provide data and applications. Depending on the purpose of the web applications, they are typically used by users who need to authenticate in advance. Web applications must implement security mechanisms that protect the data and prevent its misuse. Typical security components or mechanisms are: authentication, authorization, input and output validation, session management, error handling, and logging.

### 1.2 Objective

The goal of the module is the secure operation of web applications and the protection of information that is processed by a web application.

### 1.3 Delimitation

This module considers the threats and requirements specific to web applications. While web servers deliver the web pages (see also APP.3.2 * web server *), web applications provide functions and prepare dynamic content delivered by the web server. The module APP.3.2 * Webserver * also contains the editorial planning of the website as well as the emergency management, these aspects are therefore not dealt with again in this module. The security-relevant aspects of a service-oriented architecture (SOA) (see APP.3.7 * Service-Oriented Architectures *) are not considered in this module.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in web applications:

### 2 1 Deficiencies in the development and enhancement of web applications

If a web application is developed or extended with missing or inadequate specifications and standards, this can lead to errors, quality losses or incompletely implemented functionality. Mistakes made in early stages of development are often only discovered at an advanced stage of development. In order to remedy these errors later, often the source code of the web application has to be extensively checked and corrected again. As a result, the development costs can increase significantly. In the case of basic architectural errors, the web application may even need to be completely redeveloped. In addition, if there are no requirements to implement security mechanisms, the required protection requirements of the data to be processed may possibly be violated.

### 2 2 Avoiding Web application authorization
Attackers often try to access features or data from web applications that are only available to a limited group of users. If the authorization is implemented incorrectly, an attacker can gain the privileges of another user with more extensive rights and access protected areas and data. This is usually done by an attacker manipulating his inputs in a targeted manner by typing (unscheduled) commands or statements in the text boxes.

### 2 3 Inadequate validation of input and output data

If a web application processes input data manipulated by an attacker, protection mechanisms can be bypassed. Also, the web application's output data is either delivered directly to the user's browser, the calling application, or to downstream systems. If the data is not sufficiently validated before output, it could contain malicious code that is interpreted or executed on the target systems.

### 2 4 Missing or poor web application error handling

If errors occur during the operation of a web application, the z. B. restrict the availability of the web application to unreachability. For example, actions may be performed incompletely, cached states and data may be lost, or security mechanisms may fail. If errors are not handled correctly, operation and protection of functions and data can no longer be guaranteed.

### 2 5 Inadequate logging of security-relevant events

If security-relevant events are insufficiently logged by the Web application, they can not be traced at a later time and the cause can no longer be determined. Critical errors and attacks, such as unauthorized configuration changes to the Web application, go unnoticed and a vulnerability can then be difficult to resolve.

### 2 6 Disclosure of security-related information in web applications

Web pages and data generated and delivered by a web application may include information about the background systems, e.g. For example, information about IT components and versions of frameworks. This information can give an attacker hints for a targeted attack on the web application.

### 2 7 Abuse of a web application through automated use

When an attacker automates a web application's capabilities, it can perform numerous operations in a short amount of time, effectively performing repetitive attacks against the web application. With the help of a repeated login process, eg B. valid combinations of user name and password systematically determined (brute force) or lists with valid user name generated (enumeration). In addition, repeated invocation of resource-intensive features (such as complex database queries) for application-level denial-of-service attacks may be abused.

### 2 8 Insufficient Session Management of Web Applications
If an unauthorized person detects a user's session ID due to inadequate session management, it can use the web application in the context of that session. As a result, z. For example, an attacker could interact with the web application as a legitimate authenticated user without knowing the actual credentials. For example, in a session fixation attack, an attacker can first assign a session ID from the web application and submit it to the victim (for example, via a link in an email). If the victim follows this link and subsequently authenticates himself to the web application with the session ID transmitted by the attacker, the attacker can then use the application with the session ID known to him. In this way, it is possible for him to access the web application in the security context of the attacked user and thus to use functions.

3 requirements
---------------

The following are specific requirements for Web application protection. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### APP.3.1.A1 Web Application Authentication [Developer]

In order to access protected resources of a web application, users MUST authenticate themselves to the application. For this, a suitable authentication method MUST be selected and the selection process documented. If the so-called digest authentication method is used, the password files on the web server MUST be sufficiently protected.

A central authentication component MUST be used, which has been implemented as far as possible with established standard components. The component MUST force users to use secure passwords according to a password policy. If a web application stores authentication data on a client, the user MUST explicitly consent ("opt-in") and be alerted to the risks of the function.

To ensure that a valid session (session ID) was not inherited by an attacker, users must re-authenticate to critical features. Also, the web application MUST set limits for failed login attempts. All offered authentication methods of the web application MUST have the same security level. In addition, users MUST be informed immediately when the password has been reset.

#### APP.3.1.A2 Web Application Access Control [Developer]

If only a limited number of users are allowed to use the web application, an authorization component MUST be used to ensure that users can only perform actions for which they are authorized. Any access to protected content and features MUST be controlled before it is executed.

All users MUST be assigned restrictive access rights properly. If employees receive access rights to or change any of the web applications, those responsible MUST check, confirm, and document in a traceable way. The documentation of the granted access rights MUST always be up to date. Also, there must be a regular procedure to deprive users of access rights. Should it not be possible to assign access rights, an additional security product MUST be used for this purpose.
All resources managed by the web application MUST be considered by the authorization component. Users MUST be server-side and centrally authorized on a trusted IT system. If the access control is faulty, requests MUST be rejected. Also, there must be an access control on URL calls and object references. Likewise, access to files must be restricted by the users with restrictive file system permissions, and secure handling of temporary files MUST be provided.

#### APP.3.1.A3 Secure Session Management [Developer]

Session IDs MUST be properly protected. They MUST be generated randomly (with sufficient entropy). If the web application's underlying framework can generate session IDs, then the framework's functionality MUST be used. If session IDs are managed and created using a framework, then the framework MUST be configured securely. Also, the session ID MUST be sufficiently protected when it is transmitted and stored on the client side.

A web application MUST allow users to explicitly end an existing session. After the user has logged in, an existing session ID MUST be replaced with a new one. The duration of the session MUST be limited, eg For example, inactive sessions automatically become invalid after a certain time and a maximum validity period is given (timeout). After the session is invalid, all session data (both server-side and client-side) MUST be invalid and deleted.

#### APP.3.1.A4 Controlled integration of data and content in web applications [developer]

It MUST be ensured that a web application integrates and delivers exclusively intended data and content to the user. If a web application offers a file upload feature, this feature MUST be restricted (for example, to necessary file types). Also, access and execution rights MUST be set restrictive in this case. In addition, it MUST be ensured that a user can save files only in the specified path.

The goals of the redirect feature of a web application MUST be sufficiently limited so that users are redirected to trusted web pages only. If a user leaves the trust domain, he MUST be informed.

#### APP.3.1.A5 Logging Security Events of Web Applications [Developer]

A web application MUST record security-relevant events with the required characteristics in a comprehensible way. Access to the log data MUST be limited to a few authorized persons. When evaluating the log data, it MUST be ensured that malicious code in log entries is not interpreted by the evaluation program. More detailed information can be found in OPS.1.1.5 Logging.

#### APP.3.1.A6 Timely import of security-relevant patches and updates

System administrators MUST regularly inform themselves about current vulnerabilities and import security-related updates in a timely manner. Software updates and patches for web applications MUST be obtained from trusted sources only. You MUST be tested sufficiently before the roll-out. Before any updates or patches are installed, MUST always be sure that the original state of the web application can be restored. The current patch level MUST be documented.

#### APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
Web applications MUST be protected against automated access by appropriate protection mechanisms, such as: For example, by setting limits on the number of access attempts in a given amount of time. However, it MUST be taken into account how the limits affect the web application, e.g. For example, functional restrictions might occur for authorized users.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state of the art in web applications. They SHOULD be implemented in principle.

#### APP.3.1.A8 System architecture of a web application

Already in the design phase of a web application security aspects should be considered. Also, care should be taken that the architecture of the web application accurately captures and correctly implements the business logic of the institution.

In the system architecture SHOULD be provided to separate the server services by separate IT systems from each other. Also, each user account SHOULD be used for the different server processes of the system components. The rights of these service accounts SHOULD be limited to the operating system level, so that only the required resources and files of the operating system can be accessed.

The network architecture SHOULD pursue a multi-tiered approach (multi-tier architecture). At least the security zones Web Layer, Application Layer and Data Layer SHOULD be considered. From these zones SHOULD NOT be able to access systems on the intranet.

The software architecture of the web application SHOULD be documented with all components and dependencies. The documentation SHOULD already be updated and adapted during the course of the project, so that it can be used right from the development phase and that decision-making processes are comprehensible. The documentation should identify all components necessary for operation that are not part of the web application as such. Likewise SHOULD emerge from which components implement which security mechanisms, how the web application is integrated into an existing infrastructure and which cryptographic functions and procedures are used.

#### APP.3.1.A9 Web Application Procurement, Development and Extension [Tester, Development Manager, Procurer, Developer]

When purchasing products for web applications, a requirements catalog SHOULD be created. To be able to compare different products, a rating scale SHOULD be developed.

If the actual web application or an extension is developed in-house, a suitable procedural model SHOULD be used. In doing so, all phases of the model SHOULD be run through before commissioning. For the development, programming guidelines SHOULD be specified, which help to establish a uniform security level.

If the security mechanisms of a web application are designed and developed, they SHOULD consider the most future standards and attack techniques. In application development, the development, test, and production systems SHOULD be separated.

If the web application is developed by a service provider, it should be ensured that this service provider implements the necessary security requirements during development and that the client can access the source text at any time.

#### APP.3.1.A10 Acceptance and release of web applications [Head IT]
Before web applications or extensions that have been developed either on their own or on behalf of them, are to be taken over into live operation, they SHOULD be accepted. This also applies to standard software that is adapted for the specific application. The results of the software acceptance procedure SHOULD be documented. After acceptance, the web application SHOULD be formally released. If errors are detected during operation, there should be a troubleshooting procedure.

#### APP.3.1.A11 Secure connection of background systems

Background systems of web applications where functionality and data are outsourced SHOULD be sufficiently protected. Access to background systems SHOULD only be possible via defined interfaces and defined systems. The traffic between the users and the web application (s) and other services and the background systems SHOULD be regulated by security gateways (firewalls). In addition, the traffic SHOULD be encrypted. Web application access to background systems SHOULD also be done with minimal rights.

When using an Enterprise Service Bus (ESB), ensure that all services authenticate to the ESB before they are allowed access. There SHOULD be a separate logical network segment for the ESB. Access to the ESB SHOULD only be possible through the connected applications and services. All access to the ESB SHOULD be authenticated and encrypted when communicating across site and network boundaries.

#### APP.3.1.A12 Secure Configuration of Web Applications [Developer]

A web application SHOULD be configured so that its resources and capabilities can be accessed only through the designated secure communication paths. Access to unneeded resources and functions SHOULD be restricted. The following should be considered when configuring web applications:

* Disabling unneeded HTTP methods
* Character encoding configuration
* Definition of limit values
* Restrictive file system permissions
* Administration of a web application
#### APP.3.1.A13 Restrictive Release of Security Information [Developer]

Web pages and Web application responses SHOULD NOT contain information that could give an attacker hints that he or she can use to bypass security mechanisms. This should at least include:

* neutral error messages
* no safety-relevant comments or product and version information
* limited access to security-related documentation
* regular deletion of unneeded files
* secure registration by external search engines as well as the renunciation of absolute path information
The web application SHOULD NOT be administered from insecure networks. Administration accesses SHOULD address trusted network segments and IT systems, such as: B. from the administration network. Configuration files of the web application SHOULD be stored outside the web root directory.

#### APP.3.1.A14 Protection of confidential data [developer]

Confidential data of a web application SHOULD be protected by secure, cryptographic algorithms. If such data is transmitted, for example, SSL / TLS encryption should be used. In addition, the HTTP post method SHOULD be used. In the case of connection errors SHOULD NOT change to an unencrypted channel on an encrypted channel.
Also, the web application SHOULD guarantee by directives that client-side no sensitive data is cached. Furthermore, forms should not display confidential form data in plain text and should not be saved by the browser. Access data of the web application SHOULD be protected on the server side with cryptographic algorithms against unauthorized access (Salted Hash). Likewise, files with source code from the web application SHOULD NOT be retrievable. Also, web application configuration files SHOULD only be stored outside of the web root directory.

#### APP.3.1.A15 Verification of essential changes

If important entries are to be changed, such as passwords and configurations, the entry SHOULD be re-verified by a password. Users SHOULD be notified of changes via communication paths outside the web application, for example by e-mail.

#### APP.3.1.A16 Comprehensive input and output validation [Developer]

All data submitted to a web application SHOULD be treated as potentially dangerous and filtered accordingly. All input and output data as well as data streams and secondary data (eg session IDs) SHOULD be validated. On the server side, the data SHOULD be checked on a trustworthy IT system. Incorrect entries SHOULD NOT be treated automatically if possible (English * sanitizing *). However, if it is unavoidable, * SANitizing * SHOULD be implemented safely to prevent abuse.

#### APP.3.1.A17 Error Handling [Developer]

If errors occur during the operation of a web application, they SHOULD be treated so that the web application remains in a consistent state. The following points should be considered when troubleshooting:

* confidential information in error messages should be avoided
* Error messages must be logged
* an initiated action must be canceled in the event of an error and
* subsequently rejecting access to the requested resource or function.
Previously reserved resources SHOULD be released again during error handling. Also, the bug SHOULD be treated as much as possible by the web application itself.

#### APP.3.1.A18 Control of log files

For each web application, a concept SHOULD be created that determines how extensive the logging should be and how the data is to be evaluated. In addition, a responsible person who evaluates the protocols SHOULD be named. The results SHOULD be submitted to ISB or another designated employee. Furthermore, existing legal requirements with regard to the protocol data SHOULD be adhered to, such as data protection aspects.

#### APP.3.1.A19 Protection against SQL injection

Web applications SHOULD carefully review and filter all inputs and parameters before they are passed to the database system. In addition, stored procedures or prepared SQL statements SHOULD be used. If prepared SQL statements can not be used, the SQL queries SHOULD be separately secured. In order to provide potential attackers with no evidence of attacks, web applications SHOULD issue neutral error messages to the outside world.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.3.1.A20 Use of Web Application Firewalls (CIA)
To filter data at higher protocol levels, institutions SHOULD use Web Application Firewalls (WAF). If a WAF is used, the configuration SHOULD be adapted to the web application to be protected. The configuration of the WAF SHOULD be checked after every update of the web application.

#### APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)

To avoid clickjacking attacks, make sure that the content on all Web application web pages is displayed only at the top level of the browser window. In addition, the Web application HTTP response headers SHOULD set the * X-FRAME-OPTIONS * directive.

#### APP.3.1.A22 Performing Penetration Tests (CIA)

Web applications SHOULD undergo regular penetration testing. Penetration tests SHOULD only be carried out by reliable, trustworthy and qualified personnel or service providers. In advance, all contractors for penetration testing SHOULD make detailed arrangements to conduct and evaluate the tests. Also the consent of all competent authorities SHOULD be obtained. For the test period the respective contact persons SHOULD be binding and reachable. After the penetration test, the results SHOULD be sufficiently protected and treated confidentially. The final report SHOULD be submitted to the ISB and the responsible executives.

#### APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)

To complicate cross-site request forgery (CSFR) attacks, the web application SHOULD support security mechanisms that allow users to distinguish intentional page views from unintentionally redirected third-party commands. At a minimum, it should be checked whether, in addition to the session ID, a secret token is required to access protected resources and functions. Also, in web applications, the referrer field in the HTTP request SHOULD be checked as an additional feature to identify an intended call by a user.

#### APP.3.1.A24 Preventing Blockage of Resources [Developer] (A)

To protect against denial-of-service (DoS) attacks, resource intensive operations SHOULD be avoided and particularly secured. Likewise, a possible overflow of log data in web applications SHOULD be monitored and prevented. SOAP messages SHOULD be validated against a corresponding XML schema. For critical services and applications SHOULD be tested to work with anti-DoS service providers.

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the area of ​​"web applications" can be found in the following publications, among others:

* #### [HILWEB] Help for using the web application module

  

 BSI, (last accessed on 29.09.2017)
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Download/Vorabversionen/Baustein\_Webanwendungen\_Hilfsmittel.pdf](https://www.bsi.bund.de/SharedDocs/ Downloads / DE / BSI / Grundschutz / download / pre-release / Baustein_Webanwendungen_Hilfsmittel.pdf)

 
* #### [OWASP] Open Web Application Security Project

  

 OWASP, (last accessed on 28.09.2017)
 <Https://www.owasp.org>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Web applications" building block.

* G 0.14 Spying out information (spying)
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.28 Software vulnerabilities or errors
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.36 Identity theft
* G 0.38 Abuse of personal data
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.43 Importing messages
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
* G 0.14 Spying out information (spying)
  * APP.3.1.A1 Web Application Authentication [Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A2 Web Application Access Control [Developer]
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
  * APP.3.1.A24 Preventing Blockage of Resources [Developer] (A)
  * APP.3.1.A3 Secure Session Management [Developer]
  * APP.3.1.A4 Controlled integration of data and content in web applications [developer]
  * APP.3.1.A6 Timely import of security-relevant patches and updates
  * APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
* G 0.18 Missing planning or missing adjustment
  * APP.3.1.A5 Logging Security Events of Web Applications [Developer]
  * APP.3.1.A8 System architecture of a web application
  * APP.3.1.A9 Web Application Procurement, Development and Extension [Tester, Development Manager, Procurator, Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A18 Control of log files
* G 0.19 Disclosure of information worthy of protection
  * APP.3.1.A1 Web Application Authentication [Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A2 Web Application Access Control [Developer]
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
  * APP.3.1.A24 Preventing Blockage of Resources [Developer] (A)
  * APP.3.1.A3 Secure Session Management [Developer]
  * APP.3.1.A4 Controlled integration of data and content in web applications [developer]
  * APP.3.1.A6 Timely import of security-relevant patches and updates
  * APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
* G 0.20 Information or products from unreliable sources
  * APP.3.1.A6 Timely import of security-relevant patches and updates
  * APP.3.1.A9 Web Application Procurement, Development and Extension [Tester, Development Manager, Procurator, Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
* G 0.21 Manipulation of hardware or software
  * APP.3.1.A4 Controlled integration of data and content in web applications [developer]
  * APP.3.1.A6 Timely import of security-relevant patches and updates
  * APP.3.1.A9 Web Application Procurement, Development and Extension [Tester, Development Manager, Procurator, Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
* G 0.22 Manipulation of information
  * APP.3.1.A1 Web Application Authentication [Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A2 Web Application Access Control [Developer]
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
  * APP.3.1.A24 Preventing Blockage of Resources [Developer] (A)
  * APP.3.1.A3 Secure Session Management [Developer]
  * APP.3.1.A4 Controlled integration of data and content in web applications [developer]
  * APP.3.1.A6 Timely import of security-relevant patches and updates
  * APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
* G 0.23 Unauthorized intrusion into IT systems
  * APP.3.1.A1 Web Application Authentication [Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A2 Web Application Access Control [Developer]
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
  * APP.3.1.A24 Preventing Blockage of Resources [Developer] (A)
  * APP.3.1.A3 Secure Session Management [Developer]
  * APP.3.1.A4 Controlled integration of data and content in web applications [developer]
  * APP.3.1.A5 Logging Security Events of Web Applications [Developer]
  * APP.3.1.A6 Timely import of security-relevant patches and updates
  * APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
  * APP.3.1.A8 System architecture of a web application
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
* G 0.28 Software vulnerabilities or errors
  * APP.3.1.A6 Timely import of security-relevant patches and updates
  * APP.3.1.A8 System architecture of a web application
  * APP.3.1.A9 Web Application Procurement, Development and Extension [Tester, Development Manager, Procurator, Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A22 Performing Penetration Tests (CIA)
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.3.1.A1 Web Application Authentication [Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A2 Web Application Access Control [Developer]
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
  * APP.3.1.A24 Preventing Blockage of Resources [Developer] (A)
  * APP.3.1.A3 Secure Session Management [Developer]
  * APP.3.1.A4 Controlled integration of data and content in web applications [developer]
  * APP.3.1.A5 Logging Security Events of Web Applications [Developer]
  * APP.3.1.A6 Timely import of security-relevant patches and updates
  * APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
* G 0.32 Abuse of permissions
  * APP.3.1.A1 Web Application Authentication [Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A2 Web Application Access Control [Developer]
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
  * APP.3.1.A24 Preventing Blockage of Resources [Developer] (A)
  * APP.3.1.A3 Secure Session Management [Developer]
  * APP.3.1.A4 Controlled integration of data and content in web applications [developer]
  * APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
* G 0.36 Identity theft
  * APP.3.1.A1 Web Application Authentication [Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A2 Web Application Access Control [Developer]
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
  * APP.3.1.A24 Preventing Blockage of Resources [Developer] (A)
  * APP.3.1.A3 Secure Session Management [Developer]
  * APP.3.1.A4 Controlled integration of data and content in web applications [developer]
  * APP.3.1.A5 Logging Security Events of Web Applications [Developer]
  * APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
* G 0.38 Abuse of personal data
  * APP.3.1.A1 Web Application Authentication [Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A2 Web Application Access Control [Developer]
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
  * APP.3.1.A24 Preventing Blockage of Resources [Developer] (A)
  * APP.3.1.A3 Secure Session Management [Developer]
  * APP.3.1.A4 Controlled integration of data and content in web applications [developer]
  * APP.3.1.A6 Timely import of security-relevant patches and updates
  * APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
* G 0.39 Malware
  * APP.3.1.A6 Timely import of security-relevant patches and updates
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
* G 0.40 Denial of Service
  * APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A24 Preventing Blockage of Resources [Developer] (A)
* G 0.43 Importing messages
  * APP.3.1.A3 Secure Session Management [Developer]
  * APP.3.1.A4 Controlled integration of data and content in web applications [developer]
  * APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
* G 0.46 Loss of integrity of sensitive information
  * APP.3.1.A1 Web Application Authentication [Developer]
  * APP.3.1.A10 Acceptance and release of web applications [Head IT]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A17 Error Handling [Developer]
  * APP.3.1.A18 Control of log files
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A2 Web Application Access Control [Developer]
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
  * APP.3.1.A24 Preventing Blockage of Resources [Developer] (A)
  * APP.3.1.A3 Secure Session Management [Developer]
  * APP.3.1.A4 Controlled integration of data and content in web applications [developer]
  * APP.3.1.A6 Timely import of security-relevant patches and updates
  * APP.3.1.A7 Protection against unauthorized automated use of web applications [Developer]
  * APP.3.1.A11 Secure connection of background systems
  * APP.3.1.A12 Secure Configuration of Web Applications [Developer]
  * APP.3.1.A13 Restrictive Release of Security Information [Developer]
  * APP.3.1.A14 Protection of confidential data [developer]
  * APP.3.1.A15 Verification of essential changes
  * APP.3.1.A16 Comprehensive input and output validation [Developer]
  * APP.3.1.A19 Protection against SQL injection
  * APP.3.1.A20 Use of Web Application Firewalls (CIA)
  * APP.3.1.A21 Prevention of Clickjacking [Developer] (CI)
  * APP.3.1.A22 Performing Penetration Tests (CIA)
  * APP.3.1.A23 Prevention of Cross-Site Request Forgery [Developer] (CI)
