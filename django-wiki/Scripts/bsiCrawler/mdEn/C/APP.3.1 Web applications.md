[toc]
 
1 description
--------------

### 1.1 Introduction

Web applications provide functions and dynamic content over the Internet protocol Hypertext Transfer Protocol (HTTP) or HTTPS (HTTP over SSL or TLS, that is protected by an encrypted connection). For this purpose, documents and user interfaces (eg input masks) are generated on a server and delivered to corresponding client programs (web browser). Web applications are usually developed on the basis of frameworks. These provide a framework for frequently recurring tasks (eg for security components).

To run a web application, several IT system components are usually required. These typically include a web server to deliver data, an application server to run the actual application, and additional background systems attached as data sources across different interfaces (eg, database or directory service).

Web applications are used in both public IT networks and corporate networks (intranets) to provide data and applications. Depending on the purpose of the web applications, these are typically used by users who need to authenticate in advance. Web applications must implement security mechanisms that protect the data and prevent its misuse. Typical security components or mechanisms are: authentication, authorization, input and output validation, session management, error handling, and logging.

### 1.2 Objective

The goal of the module is the secure operation of web applications and the protection of information that is processed by a web application.

### 1.3 Delimitation

This module considers the threats and requirements specific to web applications. While web servers deliver the web pages (see also APP.3.2 * web server *), web applications provide functions and prepare dynamic content delivered by the web server. The module APP.3.2 * Webserver * also contains the editorial planning of the website as well as the emergency management, these aspects are therefore not treated again in this module. The security-relevant aspects of a service-oriented architecture (SOA) (see APP.3.7 * Service-Oriented Architectures *) are not considered in this module.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in web applications:

### 2 1 Deficiencies in the development and enhancement of web applications

If a web application is developed or extended with missing or inadequate specifications and standards, this can lead to errors, quality losses or incompletely implemented functionality. Mistakes made in early stages of development are often only discovered at an advanced stage of development. In order to remedy these errors later, often the source code of the web application has to be extensively checked and corrected again. As a result, the development costs can increase significantly. In the case of basic architectural errors, the web application may even need to be completely redeveloped. In addition, if there are no requirements to implement security mechanisms, the necessary protection requirements of the data to be processed may possibly be violated.

### 2 2 Avoiding Web application authorization
Attackers often try to access features or data from web applications that are only available to a limited group of users. If the authorization is implemented incorrectly, an attacker can gain the privileges of another user with more extensive rights and access protected areas and data. This is usually done by an attacker manipulating his inputs in a targeted manner by typing (unscheduled) commands or statements in the text boxes.

### 2 3 Inadequate validation of input and output data

If a web application processes input data manipulated by an attacker, protection mechanisms can be bypassed. Also, the web application's output data is either delivered directly to the user's browser, the calling application, or to downstream systems. If the data is not sufficiently validated before output, it could contain malicious code that is interpreted or executed on the target systems.

### 2 4 Missing or poor web application error handling

If errors occur during the operation of a web application, the z. B. restrict the availability of the web application to unreachability. For example, actions may be performed incompletely, cached states and data may be lost, or security mechanisms may fail. If errors are not handled correctly, operation and protection of functions and data can no longer be guaranteed.

### 2 5 Inadequate logging of security-relevant events

If security-relevant events are insufficiently logged by the web application, they can not be traced at a later time and the cause can no longer be determined. Critical errors and attacks, such as unauthorized configuration changes to the Web application, go unnoticed and a vulnerability can then be difficult to resolve.

### 2 6 Disclosure of security-related information in web applications

Web pages and data generated and delivered by a web application may include information about the background systems, e.g. For example, information about IT components and versions of frameworks. This information can give an attacker hints for a targeted attack on the web application.

### 2 7 Abuse of a web application through automated use

When an attacker automates a web application's capabilities, it can perform numerous operations in a short amount of time, effectively performing repetitive attacks against the web application. With the help of a repeated login process, eg B. valid combinations of user name and password systematically determined (brute force) or lists with valid user name generated (enumeration). In addition, repeated invocation of resource-intensive features (such as complex database queries) for application-level denial-of-service attacks may be abused.

### 2 8 Insufficient Session Management of Web Applications
If an unauthorized person detects a user's session ID due to inadequate session management, it can use the web application in the context of that session. As a result, z. For example, an attacker could interact with the web application as a legitimate authenticated user without knowing the actual credentials. For example, in a session fixation attack, an attacker can first assign a session ID from the web application and submit it to the victim (for example, via a link in an email). If the victim follows this link and subsequently authenticates himself to the web application with the session ID transmitted by the attacker, the attacker can then use the application with the session ID known to him. In this way, it is possible for him to access the web application in the security context of the attacked user and thus to use functions.
