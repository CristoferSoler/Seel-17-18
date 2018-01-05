1 description
--------------

### 1.1 Introduction

Web applications provide functions and dynamic content over the Internet Protocol Hypertext Transfer Protocol (HTTP) or HTTPS (HTTP over SSL / TLS, that is protected by an encrypted connection). For this purpose, documents and user interfaces (eg operating elements and input masks) are generated on a server and delivered to corresponding client programs (web browsers).

Web applications are usually developed on the basis of frameworks. These provide a framework for frequently recurring tasks (eg for security components). For a web application, several frameworks are often used for different areas (eg access to databases, formatting of the outputs) and components (eg authentication, session management).

To run a web application, several IT system components are usually required. These usually include a web server for delivering the data, an application server for operating the application and additional background systems that are connected as data sources via different interfaces (eg database or directory service).

Web applications provide data and applications in both public IT networks (such as the Internet) and corporate networks (intranets). Web applications need to implement security mechanisms that protect data and prevent abuse.

Typical security components or mechanisms of a web application are:

* Authentication
 To access protected resources of the web application, the users must identify themselves to the authentication component (eg through access data).
* Authorization
 Before accessing protected resources and features, you must verify that users have sufficient rights.
* Input and output validation
 Input and output data must be checked and filtered to avoid processing of harmful data (such as executable malicious code).
* Session Management
 Since the Internet Protocol HTTP does not support mating related requests to a user, this mapping is done through session management of the web application.
* Error handling
 Errors that occur must be treated in such a way that the data of the web application is protected even in the case of an error.
* Logging
 Events must be recorded by the web application in such a way that actions taken and security-related incidents can also be reconstructed at a later date.
### 1.2 Life cycle

** planning and conception **

When planning a web application, it usually has to be decided whether the requirements for the web application can be covered by standard products or an in-house development is necessary. When a web application is implemented based on standard software, customizations are usually required that go beyond mere configuration changes and often include development work. As a result, standard software-based web applications often have to comply with Web application development and extension requirements (see APP.3.1.M9 * Web Application Procurement, Development, and Extension *).

Already in the design phase of a web application, security aspects must be taken into account to protect the data to be processed (see APP.3.1.M8 * System architecture of a web application *). Here, the integration of the background systems (eg database) and their secure connection must be included (see APP.3.1.M11 * Secure connection of background systems *).

If personal data are processed, recorded or evaluated by web applications (eg user behavior), the legal framework must be taken into account when planning technical solutions (see APP.3.1.M17 * Control of the log files *).

**Procurement**
If a web application with available standard software is to be realized, a suitable product must be selected (see * APP.3.1.M9 Procurement, Development and Extension of Web Applications *).

**Implementation**

Before a web application is taken over into active operation, the safety functions must be configured. The components to be deployed must protect the web application from known threats and attack techniques (see, for example, APP.3.1.M18 * SQL Injection Protection *).

In addition, context-sensitive validation and filtering of the data (see APP.3.1.M1 * Authentication for web applications *) and the protection of user sessions through session management (see APP.3.1.M3 * Secure Session Management *) are essential Security components of a web application.

**Business**

After a web application has passed through the acceptance and release procedure successfully and has been configured ready for operation, normal operation can be started.

In particular, when using a web application over public networks (eg Internet) there is a risk that exploited vulnerabilities will be exploited. Therefore, processes must be defined in order to be able to permanently maintain the desired security level of the web application (see APP.3.1.M6 * Timely Import of Security-Relevant Patches and Updates *).

It must be ensured that data transmitted by web applications does not contain any security-related information that gives an attacker information about bypassing security mechanisms (see APP.3.1.M14 * Confidential Data Protection *).

For the high protection requirement, penetration tests have to be carried out on the web application in order to check the security level of the web application and to quickly eliminate possible weaknesses (APP.3.1.M21 * Carrying out of penetration tests *).

2 measures
-----------

The following are specific implementation notes in the Web Applications section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### APP.3.1.M1 Web Application Authentication [Developer]

If a web application or parts thereof are to be used exclusively by a limited group of users, the users must authenticate themselves to the application. Different methods can be used for this purpose, which are described for example in the section * Selection of an Authentication Method *.

When implementing authentication mechanisms for web applications, the following points should be considered:

** Requirements for the authentication component **

The authentication logic should only be implemented in one place and not multiple times in the program code. If errors occur during authentication, the requested action should be aborted and the request rejected.

The authentication component should be able to force secure passwords according to a password policy. Requirements for secure passwords can be found in the section * Password Usage *.

In addition, it is recommended to show the estimated strength of the entered password (eg, weak, medium, secure). This assists the user in choosing secure passwords.

In order to avoid errors in the development of the authentication component, it is recommended to implement them on the basis of established standard components (libraries or frameworks) (eg * Enterprise Security API * of the OWASP).

If there is an increased need for protection of the web application, a two-factor authentication should be used.

In order for a user to detect the misuse of their user account, the web application should display the date and time of the last unsuccessful and successful login attempts after a user has logged in as a warning.

** Selection of an authentication method **

The HTTP / 1.1 protocol provides two different methods for user authentication.
The first method is the so-called basic access authentication. The client sends the user name and the password Base64-coded in the so-called authorization header of the HTTP request to the server. Base64 is a method for encoding binary data in 7-bit ASCII, which is used here for transmitting special characters via the HTTP interface. The password is therefore not readable at first glance, but can be easily determined by a potential "eavesdropper" because it is unencrypted. Therefore, this type of authentication can be used at most for very low confidentiality requirements.

The second method for HTTP authentication is the digest authentication. With this type of authentication, the user's password must be in plain text on the server. The client receives a random string from the server, the so-called Challenge. From this challenge and the password of the user, the client calculates a so-called digest according to a standardized procedure, which is then sent to the server for authentication. Since the server has both the random string generated by him and the password of the user, he can also calculate the digest and thus perform the authentication. Since the password is not sent via the network during digest authentication, this method is suitable for a somewhat higher protection requirement.

A problem with the use of the above-mentioned authentication methods is the security of the password data on the server: In the case of the digest authentication, the authentication data of the users must be present on the web server in plain text. Basic authentication usually saves a hash value of the password. Securing the password files on the server against unauthorized access is therefore particularly important.

In addition to HTTP authentication, there is another way to control access via the HTTP protocol: Authentication is not carried out via the web server itself but via a server-side application. Username and password are entered via normal HTML forms and checked by the application. However, it should always be noted that passwords or PINs transmitted in plain text over the Internet can be easily read. In addition, of course, all data, even if they are delivered on authenticated requests, transmitted unencrypted.

Some web offers identify users through special cookies stored in the browser. Since cookies are also transmitted in plain text when using HTTP, this method is also unsuitable for authentication when accessing sensitive information. Since there are other security issues with cookies, this method should generally not be used.

** User authentication via SSL / TLS **

The authentication data should always be encrypted, see APP.3.1.A14 * Protection of confidential data *. A commonly used method of user authentication for web offers is the combination of forms-based authentication and SSL / TLS-encrypted data transmission. If the chosen SSL / TLS encryption is sufficiently strong, this method offers a level of security that is appropriate for higher security requirements at a reasonable cost (user administration in the web application and implementation of SSL / TLS-protected access to the web server).

The following table summarizes the various ways in which users authenticate to Web servers.

Table: User Authentication on Web Servers

The Microsoft Internet Information Server also provides another method that uses Windows user logon. However, this method works only with the Microsoft Internet Explorer as a client.
** Remember Me function **

To improve user-friendliness, web application authentication data is sometimes stored permanently on the users' clients (eg within a cookie in the web browser). This option is often referred to as the Remember Me feature. If authentication data has been saved on the client as part of the Remember Me function, it will be automatically transferred during later use of the web application. The user no longer needs to enter access data.

If an attacker gains access to the web browser or malicious code is executed on the client, this stored authentication data can be read out. For this reason, this feature should be avoided. However, if the Remember Me function can not be dispensed with, then the user should explicitly agree to an activation (opt-in). In addition, the user should be made aware of the risks of the function.

In addition to authentication data in cookies, current browsers can often save form fields (eg username / password or address data) for later reuse. If a web form for which the entered data was previously saved is called again, the data is automatically entered in the fields by the browser. Therefore, the * autocomplete = off * option should be set for all form fields containing sensitive data. This instructs the browsers not to save the data of the corresponding form fields.

** Additional authentication for critical functions **

If a user has successfully authenticated, the web application usually assigns him a unique session (using a session ID). The web application can use this session ID to map the incoming requests to the logged in users. Thus, the session ID can be considered as a kind of temporary logon date that can be used to access the logged-in user sessions (see also APP.3.1.M3 * Secure Session Management *).

Since the session ID is often attacked, it can not be completely ruled out that an attacker has not already adopted it. Therefore, in the case of safety-critical actions (eg changing the password or deleting the entire database), the user should be authenticated again (eg by entering the old password when changing the password).

** Limits for failed logon attempts **

If a user tries to log in to the web application several times at short intervals, these authentication attempts should be considered as an attack. If the number of failed attempts exceeds a specified value (for example, five failed attempts), the user account should be locked for a defined time interval (for example, 10 seconds). In addition, the time intervals for blocking the user account may progressively increase with the number of failed attempts. This is to prevent users from guessing passwords of other users without authorization.

When choosing the limit and time intervals, it should be noted that this mechanism can be misused for denial-of-service attacks. An attacker could deliberately provoke the blocking of many user accounts and thus exclude these users from using the web application.

** Automated resetting of authentication data **
Since web applications are often used by a large group of users, they often offer functions for automatically resetting the authentication information (password reset). So the administrative effort should be kept as low as possible, if z. B. a user has forgotten his password. If the authentication data can be reset without authorization, the authentication mechanism can be bypassed in this way. Therefore, it must be ensured that all functions of a web application for changing the authentication data are at least as secure as the primary authentication.

For example, in the process of resetting the password, if the user is authenticated by a secret question with an appropriate answer, the features should be formulated by the user. It should be noted that they should not include data that is publicly available or easy to guess. To increase the level of protection, several questions and answers can be included in the registration process (eg five, of which at least three questions need to be answered correctly for successful authentication).

In addition, another security feature can be used by sending a link to a previously specified by the user e-mail address after correct answering the questions or sent another security token (eg a PIN) via SMS to a stored phone number becomes. Only after the user clicks on the link or enters the PIN can he log in.

Since the authentication procedure is usually difficult to bring to the same level of security when resetting credentials as in primary authentication, an automated reset by the web application should be avoided. In the case of limited user groups of the web application (eg in the case of a web application on the intranet), the password can instead be manually reset, for example, via a hotline with secure authentication features and a corresponding release procedure. Especially with a high protection requirement, this method is preferable.

** Password usage control **

For web applications that use passwords for authentication, a password usage policy must be introduced. The users must be notified. Specifications for password design can be found in ORP.4 Identity and Permission Management. For web applications, the following rules for password design have proven successful:

A password should consist of uppercase letters, lowercase letters, special characters, and numbers. At least two of these types of characters should be used.

* If alphanumeric characters can be selected for the password, it should be at least 8 characters long.
* Users should be regularly stopped to change the password, eg. B. every 180 days.
* The repetition of old passwords when changing the password should be prevented by the IT system (password history).
* The choice of trivial passwords (eg * BBBBBBBB *, * 123456, name, date of birth *) should be avoided.
* Each user must be able to change their own password at any time.
* Users should be assisted in changing passwords by entropy measurement (password-quality display).
* Initial login of new users should be assigned initial passwords that need to be changed after a single use.
* Unsuccessful login attempts should be rejected with a brief error message without giving details. In particular, in the case of unsuccessful login attempts, it must not be possible to determine whether the user name entered or the entered password (or both) are incorrect. After five consecutive incorrect password entries for the same identifier, the authentication system should block the access for this (for a certain period of time or permanently). If the web application blocks an identifier, it may not be visible on subsequent unsuccessful login attempts, but should be communicated to the user in a separate way.
* When authenticating in networked systems, passwords should not be transmitted unencrypted, even on the intranet. If the authentication is carried out over an unsecured network, passwords must under no circumstances be transmitted unencrypted.
* When entering the password, the password should not be displayed on the screen.
** Reset passwords **

It happens regularly that users forget or lose their authentication information or tokens. Therefore, every web application must have an adequate mechanism to give users access again quickly, but without opening any security holes. Depending on the type of authentication procedure selected and the need for protection, there are various options for resetting passwords or enabling tokens, see ORP.4 Identity and Authorization Management.

#### APP.3.1.M2 Web Application Access Control [Developer]

An access control has to be implemented at all levels of a web application (eg through the web application, the application server, the web server and the operating system). As a result, in addition to web-application-level access protection, the requirement of APP.3.1.M11 Secure Back-End System Attachment * should be considered for back-up protection of data in background systems.

The following points should be considered for secure access control at the web application level:

** General aspects **

If you work with a Web application that has multiple users, you must properly manage and manage the access rights.

Every access to protected content and features must be controlled before it is executed. This is true even if, for example, the same user repeatedly accesses a protected resource. Automated client requests through web technologies (such as Ajax) should also be treated as independent requests and controlled accordingly.

** Granting of access rights **

Access rights control which person is empowered to use web applications as part of their role. The access rights (for example, read, write, execute) to web applications, subapplications, or data depend on the function that the person perceives. At the same time, only as many access rights may be assigned as are necessary for the task perception (* need-to-know principle *). The access rights must be implemented by the rights management of the application.

Many web applications allow different rights to be defined as group rights or rights profiles (eg group * data collection *). This definition corresponds to the technical implementation of the rights assigned to a function. In order to manage access rights efficiently, it is advantageous to create such groups or profiles.

The specification and modification of access rights must be initiated and documented by the responsible person (see also ORP.4 Identity and Authorization Management).

** Documentation of authorized users and rights profiles **

There must be documentation of the users approved for the web application, created user groups and rights profiles (see also ORP.4 Identity and Permission Management).
The documentation of the authorized users and rights profiles must be checked regularly (at least every 6 months) to see whether they reflect the actual status of the assignment of rights and whether the assignment of rights still complies with the security requirements and the current tasks of the users. The complete documentation is a prerequisite for checking the assigned user rights.

** Authorization Component Requirements **

Web applications typically use a generic client that is not under the control of the web application. This allows an attacker to arbitrarily manipulate the request as a matter of course and bypass security mechanisms implemented on the client side. For this reason, the authorization must be implemented server-side on a trusted IT system.

The authorization component must consider all managed resources of a web application. These include z. For example, URLs, files, object references, business functions, application data, configuration data, and log data.

The authorization routines should be implemented centrally in one place and not distributed in the program code of the web application. In this way, the code of the authorization component is separated from the business logic of the web application and a redundant and error-prone implementation is avoided. When developing the authorization component, you should use functions from existing frameworks.

If errors occur during access control (eg because insufficient information is used for authorization), access must be denied. In the event of an error, no requested resources may be transmitted or functions performed uncontrolled.

** Control of all resources involved in an action **

A user may not be able to perform an action on a resource for which he does not have sufficient rights. If z. For example, if an authenticated user changes a URL parameter to be assigned to a bank account, he / she may not gain access to a foreign bank account. If the rights to carry out an action are checked, all resources involved in the action should therefore also be checked.

This also applies to the implementation and configuration of the search function of a web application. Care should be taken to ensure that access-protected resources are not presented to an unauthorized user as a search result. For example, before the Web application returns the search results, it should be checked if the user has sufficient rights to view them.

** Access control for URL calls and object references **

Websites and other Web application resources are usually identified and retrieved via the URL. In this case, a user usually invokes web pages or functions of the web application via the displayed links on an already displayed web page of the application.

If resources of the web application are to be protected, it is not sufficient to remove the link to the resource from the displayed web pages (eg a link to the administration page), but also the direct call of the resource via the URL must be protected ,

Web application pages are often created dynamically based on references to objects, such as the ID of a database entry. If these references are passed by the users of the web application (eg as parameters in the URL), the parameter and thus the reference can be changed as desired by a user.
Since these are not direct references (eg to files) but indirect references (references to objects), access control should be based on the reference values ​​(eg IDs). Furthermore, an additional access control for the requested objects in the background systems should be carried out if possible. This can be achieved, for example, by passing user authentication to the background systems (see also APP.3.1.M11 * Secure Connection of Background Systems *).

** Restrictive file system permissions on upload function **

Basically, access to files by users of the web application must be restricted by restrictive file system permissions (see APP.3.1.M12 * Secure Configuration of Web Applications *).

If the web application provides functionality for uploading files, after the upload has been completed, only the owner may have the file system authority to access the created files. In a further step, the access to the files can be explicitly released for other users. In general, it should be ensured that uploaded files have no execution rights, so that an attacker can not execute any malicious code (see also APP.3.1.M4 * Controlled integration of data and content in web applications *).

** protection of temporary files **

Dynamic web pages often generate temporary data (such as summary charts, reports). If this is sensitive data, it should not be cached in the file system. Instead, the data should be delivered directly to the user. If the data to be protected must be stored in temporary files, the following points should be considered:

* Access permissions in the file system must be restrictive so that only authorized users and services can access it.
* Filenames should be made up of random values ​​(such as a Globally Unique Identifier (GUID)), so they are not easy to guess.
* Once the data is no longer needed, it should be deleted promptly.
* It is recommended to save the files in a directory that can not be reached via the web server (eg outside the root directory of the web server).
* Access to the files should be possible only through those web application interfaces that implement sufficient security mechanisms for access control and logging.
#### APP.3.1.M3 Secure Session Management [Developer]

Web applications typically use the stateless HTTP protocol to transfer data. Requests generated by a user are not associated with them, such as individual page views to populate a virtual shopping cart. In order to recognize a user's associated requests and assign them to a session, a session ID is assigned (for example, after successful log-on), which is then transmitted at each page request. The session ID is typically generated by the web application itself.

If the user has logged into the web application, the session ID is similar to his credentials. The web application identifies the user with each page or service call and associates it with a session (privileged if necessary). If unauthorized users use the session ID, they are identified as legitimate users and can use the application or service on behalf of the victim.

The session management of a web application has the task of managing the sessions and assigning new session IDs. The following requirements and aspects should be taken into consideration.

** Session ID requirements **
It should be noted that the period of validity of a session ID (see also section "Limited Session Duration") should be significantly smaller than the time it takes for an attacker to guess the session ID. This can be individually assessed using a formula for a web application (see [GSSID]).

The session ID should meet at least the following requirements:

* The session ID must be generated randomly using cryptographic random number generators and should have an entropy of at least 64 bits so that it can not be guessed by a potential attacker. To increase the entropy of the session ID, the length can be increased (for example, 128 bits) and the character space of the session ID (for example, alphanumeric characters and special characters) can be increased. As a guideline, the length of the session ID should be at least twice the number of bits as the number of session ID entropy bits. As a result, the session ID should be at least 128 bits long. Assuming that a character is represented by 8 bits, such a session ID would consist of at least 16 characters (128 bits / 8 = 16 bytes).
* No externally known or erratable data (for example IP address, time) should be included in the calculation of the session ID, as long as this does not tolerate entropy.
* If the framework underlying the web application supports the generation of session IDs, the function of the framework should preferably be used. The functionality of leading frameworks is usually tested and supports the secure generation of session IDs. An error-prone new development should therefore be avoided.
* If session IDs are managed and created with a framework, it is important to ensure secure configuration of the framework so that the above-mentioned requirements for the session ID are met.
** Protection against unauthorized access to the session ID **

The session ID can be transferred both in the URL of a request (GET method), in the body of the request (POST method) or as a cookie in the header of the request. When data is submitted using the GET method, it can be stored by participating IT systems and viewed by third parties (for example, in the browser history, on screenshots, page copies, or printouts). Therefore, the session ID should not be transferred via the GET method (ie in the URL). For web applications with high protection requirements, this is not allowed. Instead, the session ID should preferably be transferred in cookies.

If the application requires the GET method (for example, because some clients can not process cookies), the following points should be noted:

* Users should be advised of the dangers mentioned and, when leaving the computer, terminate the session or lock the computer.
* Users should be advised not to send any saved pages or screenshots from web pages where the session ID is visible in the URL.
* When using the web application through a public machine, a message should indicate that the browser history should be deleted after the session.
* Very long session IDs make it difficult for unauthorized persons to write off or read along randomly.
* When linking to external sites, the session ID must not be transferred. This applies both to the transmission in the URL and to the referrer field. Therefore, for links to external pages, a forced redirect should take place, which clears the referrer field.
To protect against unauthorized reading of the session ID, the communication should take place via a secure connection after a successful login. This can be encrypted via a transport security, for example by means of SSL / TLS. The session ID can be transferred over an unsecured connection if the existing session can not use access-protected areas of the web application. Usually the user is not yet authenticated in this case.

Access to the session ID as an authentication feature should be strictly regulated. If the session ID is transferred in a cookie, the client-side access to this cookie should be limited as far as possible with the following flags (for a detailed description of the cookie flags see APP.3.1.M14 * Protection of confidential data *): Path (for example * / webapp / *), Secure and HttpOnly.

** Limited time of meeting **

A web application must allow users to explicitly end an existing session after they have been used. Therefore, a clearly visible logout option must exist on all web pages for which an authentication of the user is necessary. After logging off, the session should be completely terminated and the session ID no longer valid. In addition, the user should be sensitized to the following behaviors:

* If the user is logged in, he should log out of the web application after completing the activities.
* If there was no logout on the last visit, the user should be advised to log out in the future on the next logon to the web application.
Unused existing sessions provide an attack surface for session ID brute force attacks. Therefore, sessions should no longer be valid after an idle time interval (idletime). In addition, a maximum validity period should be assigned (timeout), so that the session IDs of active sessions have a limited validity. This should be chosen as low as possible for the sessions, so that brute-force attacks are difficult, whereby the usability of the web application should not be unnecessarily limited. The formula in the "Session ID requirements" section can be used to determine an appropriate validity period.

If serious errors occur while using the web application, requested actions should be aborted and, in addition, the session terminated. Fatal errors are, for example, exceptions and detected attempts to attack. In the case of high protection requirements, even narrower criteria should be considered, which invalidate the session (for example, invalid entries, invocation of missing pages).

During invalidation, the session data should be completely deleted on the server and client side, so that the session will no longer be accepted on the server side and client-side information about previously established sessions will remain. This can be achieved, for example, by deleting the cookie with the session ID.

In addition, multiple parallel sessions under the same user account can be prevented. An existing session can be invalidated when you log in again so that only the new session remains valid. Alternatively, for example, it is possible to maintain the first session for a limited period of time (for example, 15 minutes) before it is invalidated. When logging in, the user should see a message about the expiring first session via a parallel, second session. In this way, existing but no longer used sessions after re-logon can not be used by third parties or only partially unauthorized.
To protect against session fixation attacks, an existing session ID should be replaced by a new one after logging in.

Likewise, after a change from an unsecured communication channel (HTTP) to a secure communication channel (HTTPS), a new session ID should be assigned, since the session ID could have been read during the transmission over an unsecured channel.

** Protection of session data **

Resulting session data (for example shopping cart) may only be stored on the server side on a trustworthy IT system. In addition, data must be protected against unauthorized access by other users through access control. If the web application requires client-side storage of session data, then APP.3.1.M14 * Confidential Data Protection * should also be considered for storing data on the client.

** Assignment of a session using additional attributes **

In addition to the session ID, additional features can be used to link users and sessions together (for example, the IP address). This makes it even more difficult for an attacker to take over a session, as he would need to know the additional features in addition to a valid session ID. The use of additional attributes to associate a session should be considered, at least for high-security Web applications.

If the IP address is used as an additional feature for the session assignment, it must be stored and checked on the server side. If the IP address changes during the course of a session, this should be considered an attack attempt in applications with high protection requirements and, consequently, the session should be invalidated. However, it should be noted that the IP address can not always be uniquely assigned to a user. If some users of the web application are connected via a proxy with the same (for example reverse proxy) or changing IP address (for example, changing, outgoing proxies), there is a risk that the IP addresses of these users will not be uniquely assigned to a session can. Thus, it should be kept in mind that the security measure may result in some users having limited or no use of the web application.

If the referrer is used as the identity feature, it can be checked for a fixed part of the referrer path that remains the same for all accesses (for example, the domain of the web application). The users must therefore have a web page of the web application in the referrer. It should be noted that some browsers allow deactivation or user manipulation of referrer submission, and content filtering may filter this field.

The identity features can be distributed to multiple properties of the HTTP header to protect against unauthorized use of the session. Conceivable, for example, HTTP header information such

* the browser type name (user agent header),
* Supported client formats and languages ​​(Accept and Accept-Language headers) and
* the referrer (referrer header).
Due to the sometimes small range of variation of the mentioned features of the HTTP header, the additionally achieved protection is limited. In contrast, the implementation effort and possibly the complexity of troubleshooting increases. For this reason, it should be considered in individual cases whether the additionally achieved protection justifies the implementation effort.

** avoid self-implementation **

If the session management of a web application can be based on a proven implementation in a framework or a common standard, then this is preferable to a self-implementation, since self-implementations of this security-critical, complex function very often prove to be vulnerable.
#### APP.3.1.M4 Controlled integration of data and content in web applications [developer]

A web application creates web pages at runtime whose contents can be composed of different sources. This content is z. B. in the form of files dynamically incorporated when creating the web page or generated by the web application. Since a user is delivered to the finished website, it is often not clear to him from which source the displayed content originated. Therefore, the web application must ensure that only intended data and content are included and delivered to the user.

The contents can be integrated by means of different techniques. Therefore, the following sections summarize guidance for the safe use of common techniques.

** Including Files (File Inclusion) **

When web pages are generated by a web application, it often dynamically incorporates portions of the delivered Internet page from disparate files (such as a navigation bar). This reduces the maintenance required for changes to the website (eg a new navigation entry). The content and path of the files to be included should be changed only by the administrator or privileged users of the web application. On the other hand, ordinary users should not be able to freely choose or modify the files for inclusion (eg via changed parameters). For this reason, the web application should not process user input to embed files.

However, if the web application requires user input as a source for embedding files, the intended paths to the source files should not be arbitrary. Users should not be able to specify the entire path, but instead user input should be encapsulated in predefined path statements.

Attacks, such as Path Traversal, try to convert the path to sensitive files by relative references (eg * /../../../etc/passwd*) and thus break out of the given paths. To prevent such attacks, user input should be filtered for unwanted characters for manipulation of the path (eg * / .. * and * \ .. *) (see also APP.3.1.M15 * Comprehensive input and output validation *) ,

When selecting the source files, indexes can be used instead of file names to which filenames stored on the server side are assigned. Thus, an attacker has no direct influence on the file name and can not directly incorporate any content by manipulating the index.

Web applications can, in addition to files on the server system, remotely stored resources via the network connection via URL (Remote File Inclusion). That should be stopped as completely as possible. However, if this can not be waived, the trustworthy source of these files must be ensured (eg on the basis of a whitelist with the limitation to a server or a list of absolute URLs).

** Use of file uploads **

For many web applications, users can submit content using an upload feature. A typical use case is the upload of a profile photo. The uploaded data should be limited to the required file formats (eg only image files should be allowed for the profile photo). This should include both the file extension and the contents of the file, eg. B. by an evaluation of the file header to be checked.
Uploaded files should be stored in a directory that can not be reached via the web interface (eg outside the root directory of the web server). This prevents a user from accessing their uploaded files directly (for example, to harmful scripts). If the uploaded files are initially stored in a temporary directory, it must be ensured that other users can not access the file without permission.

If a web application provides the user with an upload function of files, the following points should be noted:

* The functionality should only be available to registered users.
* Uploaded files must not be stored in the root directory of the web server service. Either fixed directory structures should be specified in which folders and files can be created or stored in another context (such as in a database or a fixed path). A user should not be able to break out of the given context.
* The default path to save the uploaded files must not be changed by the users.
* To protect against denial of service attacks, the file size should be limited.
* The permissions of uploaded files should be set restrictive to prevent unauthorized access. This is to prevent that uploaded files of an attacker are executed.
* An antivirus should scan the uploaded files for malware.
* The choice of file name should be restricted as follows:
* The file name with the file extension should be limited to a fixed number of characters (eg 200 characters).
* All non-visible characters (eg control characters) and all coded variants of these characters should be removed from the file name (eg Unicode).
* All characters with a specific meaning for interpreters should be removed (eg *;:> </ \. *% $ *).
* If possible, only alphanumeric characters and the file ending point should be allowed.
** Include content from passed parameters **

Web applications often accept input in the form of parameters (such as from forms), process them, and re-represent them in the response (for example, the search term in a web search). An attacker can exploit this in order to manipulate the presentation of the website via selected inputs. Therefore, all parameters used by the web application to display web pages must be validated in accordance with APP.3.1.M15 * Comprehensive Input and Output Validation *.

** Secure forwarding of requests (redirect) **

The redirect feature of a web application must not allow any web page to serve as a redirect target so that users are redirected to only trusted intended web pages. For example, it should be avoided that users are led to a phishing site via a prepared link to the forwarding function of the web application.

The following points provide guidance on restrictions on forwarding destinations.

* Restriction to local pages
 If there is no need to redirect to external websites, the forwarding destination can be checked for external addresses and only local pages allowed. Here, only relative paths to targets within the web application should be allowed as input and the necessary host part should be subsequently added statically.
* Predefined forwarding destinations
If forwarding is intended exclusively for known, static destinations, these should be stored in a predefined list with indexes on the server side. The targets are thus assigned static index values. Instead of the destination address, the client passes an index value (for example, from a selection list of a form) that is assigned to a destination address from the list on the server side.
* Manual confirmation
 Before forwarding, the user must check and confirm the destination address and thus the trustworthiness of the forwarding destination (eg via a forwarding page). This warns the user before he leaves the web application and thus the security context.
* Referrer test
 The reefer field of the HTTP request can be checked by the forwarding function as an additional feature for its intended use. Redirection should only occur if the referrer field contains the address to a Web application web page with a reference to the redirect destination.
** Integration of third party content **

Partner-embedded data and content (eg, commercials) should generally be considered less trustworthy. Therefore, a strong control of this content is recommended because of the risk of embedding malicious code or untrusted content.

#### APP.3.1.M5 Logging Security Events of Web Applications [Developer]

Security-relevant events (for example, accesses to resources, authentication attempts) must be logged in a comprehensible manner so that the log data can be used to determine the causes in the event of a fault, error or attempted attack. More detailed information can be found in OPS.1.1.6 * Logging *.

The following points should be noted when logging security-related events of web applications.

** Events to log for web applications **

In addition to logging on the server and background systems (for example, operating system, web and application server, database), the application must also log security-relevant events. At least the following events should be recorded at the application level:

* successful and unsuccessful login attempts to the web application,
* failed authorization attempts when accessing resources (for example, database access) and Web application features;
* failed validation of input and output data,
* failed XML schema validations,
* XML parser error,
* errors that have occurred (for example, exceptions),
* Changes to permissions for users or user groups of the web application (for example, access rights),
* Changes to user accounts (eg password change),
* Deleting the web application (for example, contributions),
* detected manipulation attempts and unexpected changes (for example, login attempts with invalid or expired session IDs),
* administrative function calls and changes to the configuration (for example, retrieval of user data, activation and deactivation of logging),
* Starting and stopping services.
** Characteristics of events to be logged **

In order to understand security-related events using historical data, basic characteristics of the events must be available. Therefore, at least the following features should be logged:

* Date,
* Time with time zone,
* associated username,
* affected object (for example, user account, file, data source),
* Status of the action (for example, failed, successful),
* Place of occurrence (for example component),
* Action (for example, authentication, authorization),
* Severity (for example, information, warning, error).
In addition, it may be helpful to log the following characteristics:

* Source IP address,
* References to the session ID (not the session ID itself),
* IT system where the error occurred
* Software version (version) of the web application.
Confidential and security-relevant data (eg session ID, access data) should not be logged.

** Suitable data formats and mechanisms **

The logged data should be stored in a uniform format for efficient evaluation. The web application logging component should therefore use a data format that integrates with existing solutions. If, for example, a central component is used for the evaluation of the log data, data formats should be selected that support this component.

** Server-side logging by a central component **

The logging of the web application is to be carried out on the server side only, since only in this way the log data can be evaluated centrally. The log data should be collected from a single, central logging component of the web application, not from different logging components.

An error-prone redevelopment of the logging component should be avoided. Instead, use the functionality of established frameworks that typically support a centralized logging approach and logging in common protocol data formats (see section * Appropriate Data Formats and Mechanisms *).

** Protection against unauthorized access and manipulation of log data **

Since the log data may contain sensitive information (for example, about the user behavior and the configuration or configuration of the web application), access to the log data must be regulated and made available only to authorized users. Access to log data should not be possible via public interfaces. Log data should therefore be stored in dedicated log directories (for example, outside the web root directory of the web server).

If the log data is stored in a database, the log data should be separated from the actual payload. This separation can be achieved by means of a separate database table. In addition, a separate database user for logging can increase the protection of log data. In this case, the database user must not have access rights to the log data for the user data.

Alternatively, the high protection logging data may also be stored in a separate database instance.

** Secure protocol evaluation **

An attacker can deliberately provoke log entries (for example, if input fields are logged) that contain malicious code. Therefore, when evaluating the log data, it must be ensured that malicious code in log entries is not interpreted by the evaluator, for example, by viewing in a browser and interpreting JavaScript code in the log data.

Since no changes to the log data may be made during log evaluation, the log data should only be analyzed in a read-only mode.

** time synchronization **

The log data of various components of a web application (for example, application server, web server, database server) usually have to be correlated in order to fully understand cross-component processes. For this purpose, the time should be synchronized on the systems in order to be able to consistently track processes in the logs based on the times.

#### APP.3.1.M6 Timely import of security-relevant patches and updates
Often, errors in products become known, which can lead to the information security of the information network in which they are operated, is affected. Corresponding errors can affect hardware, firmware, operating systems, and applications. These vulnerabilities need to be addressed as soon as possible so that they can not be exploited by internal or external attackers. This is especially important when the systems are connected to the Internet. Operating system or software component manufacturers typically release patches or updates that must be installed on their IT system to correct the error (s).

The system administrators should therefore regularly inform themselves about known vulnerabilities (see also section * Gathering information about system vulnerabilities *).

It is important that patches and updates, like any other software, can only be obtained from trustworthy sources. For each system or software product deployed, it must be known where security updates and patches are available. It is also important to verify the integrity and authenticity of the products already installed or the security updates and patches to be applied before installing an update or patch. They should also be scanned using an anti-virus program before installation. This should also be done for packages whose integrity and authenticity have been verified.

However, security updates or patches should not be prematurely downloaded, but must be tested before. Otherwise, if a conflict arises with other critical components or programs, such an update may cause the system to fail. If necessary, an affected system must be protected by other means until the tests are completed.

Before installing an update or patch, you should always back up the system, which will allow it to recover to its original state if problems occur. This is especially true if detailed tests can not be performed due to time constraints or due to a lack of a suitable test system.

In any case, it must be documented when, by whom and for what reason patches and updates were recorded. From the documentation the current patch level of the system must be able to be determined quickly at any time, in order to gain clarity as soon as the weaknesses become known as to whether the system is at risk.

If it is determined that a security update or patch is incompatible with another major component or program or is causing problems, it is important to consider how to proceed. If it is decided that a patch will not be installed due to the problems that have arisen, this decision must be documented in any case. In addition, it must be clear in this case what measures have been taken to ensure safety. Such a decision must not be made by the administrators alone, but must be agreed with the supervisor and the security officer.

** Gathering information about system vulnerabilities **

It is very important that system administrators keep up to date with newly discovered vulnerabilities. Sources of information on this topic include:

* The Federal Office for Security in Information Technology (BSI) (see http://www.bsi.bund.de/)
* Manufacturers or distributors of programs and operating systems. These often inform registered customers about known vulnerabilities in their systems and provide corrected versions of the system or patches to address the vulnerabilities.
* Computer Emergency Response Teams (CERTs).
These are computer emergency teams that serve as a single point of contact for preventive and reactive action on security incidents in computer systems. CERTs provide information in so-called advisories on current vulnerabilities in hardware and software products and provide recommendations for remedying them. Various organizations or associations maintain their own CERTs.
 The original CERT of Carnegie Mellon University served as a role model for many more such teams and is today a kind of "roof cert":
 Computer Emergency Response Team / Coordination Center (CERT / CC), Software Engineering Institute, Carnegie Mellon University, Pittsburgh, PA 15213-3890
 Telephone: + 1-412-268-7090 (24-hour hotline), email: cert@cert.org, WWW: http://www.cert.org
 The CERT messages are published in newsgroups (comp.security.announce and info.nsfnet.cert) and via mailing lists (inclusion by e-mail to: cert-advisory-request@cert.org).
 In Germany, among others, the following CERTs exist:
* CERT-Bund, Federal Office for Security in Information Technology, PO Box 20 03 63, D-53133 Bonn, Telephone: 0228 99-9582-222, Fax: 022899-9582-5427, E-Mail: certbund@bsi.bund.de , WWW: https://www.bsi.bund.de/certbund/
* DFN-CERT, Center for Secure Network Services GmbH, DFN-CERT, DFN-CERT Services GmbH, Sachsenstrasse 5, D-20097 Hamburg, Telephone: 040-808077-555, Fax: -556, E-Mail: info @ dfn- cert.de, WWW: http://www.dfn-cert.de.
* There are CERTs at various universities that also provide information publicly. An example is the RUS-CERT of the University of Stuttgart (see http://cert.uni-stuttgart.de).
* Manufacturer and system-specific as well as security-specific newsgroups or mailing lists. In such forums, references to existing or suspected security vulnerabilities or errors in various operating systems and other software products are discussed. Most current are usually the English-language mailing lists such as Bugtraq, of which there are publicly available archives in many places, for example, at http://www.securityfocus.com.
* Some IT journals also regularly post articles that outline new vulnerabilities in different products.
Ideally, administrators and security officers should be aware of security vulnerabilities in at least two different locations. It is advisable, in addition to the manufacturer's information, to use an "independent" source of information.

In any case, administrators should also use product-specific sources of information from the manufacturer, for example, to know whether patches or updates are ever made available to a specific product when security vulnerabilities are discovered. For products for which the manufacturer no longer provides security patches, it must be checked in good time whether an application under these circumstances is still responsible and by what additional measures a protection of the affected systems can still be guaranteed.

#### APP.3.1.M7 Protection against unauthorized automated use of web applications [Developer]

A web application is commonly used by humans and thus does not require automated usage (eg through scripts). Brute-force attacks (eg guessing credentials) and enumeration attacks (eg automated detection of valid login names) rely on the automated control of a web application (automation). These attacks typically attempt to collect sensitive data through repetitive, slightly varying queries (such as changed usernames).
To prevent such attacks, the web application must be able to distinguish automated from manual access. Automated attacks are characterized by a high number of access attempts within a short period of time, which clearly exceeds the usual level.

Therefore, a tolerance threshold for repeatedly retrieved resources can make such attacks more difficult (tar pit). If limits are set against automated queries, it must be ensured that legitimate users are as little restricted as possible in the functionality and operation of the web application. If Web application primitive limits are too tight, attackers can abuse it at the Web application level for denial-of-service attacks. For example, if user accounts are blocked for a certain amount of time after a specified number of unsuccessful login attempts, targeted incorrect entries can result in a long-term lockdown of many user accounts. As a result, legitimate users will no longer be able to log in to the web application during this time.

In addition, the efficiency of automated attacks is usually highly dependent on the level of detail of the information in the web application responses (see * APP.3.1.M13 Restrictive Release of Security-Related Information *).

The following examples show possible protection mechanisms:

* An artificial delay between entering user authentication credentials and reporting a failed login attempt can make brute-force attacks more difficult due to the increased time required. The effectiveness of this method can be increased by a progressive increase in the delay after each failed attempt.
* If submissions are rejected, information about the cause should be generic. For example, an attacker may not be able to log in to a valid user account based on messages such as "Invalid Password" instead of "Invalid Access Data" (see also APP.3.1.M16 * Error Handling *).
Attack attempts are often characterized by multiple failed attempts to perform an action. Therefore, the session should be ended in this case. Subsequently, a new registration should be required.
* Automated attacks can be fended off by temporarily blocking the IP address if an attack is suspected. It should be kept in mind that this recommendation may also affect bystanders who are not involved (eg if multiple users use the same proxy).
* Frequently called CAPTCHAs (Completely Automated Public Turing Test To Tell Computer and Humans Apart) are used to distinguish automated and manual access. In this case, tasks have to be solved by the user of the web application (for example, the characters in a picture must be recognized and tapped or puzzles answered), which is not easily possible for a computer program. Depending on the technology used and the task, the web application may only be used to a limited extent for people with disabilities. So should As an alternative to fading in the task they are also provided acoustically to allow people with visual impairment, the use of the web application. It should be noted that the use of CAPTCHAs for reasons of discrimination is regulated or prohibited by law in many countries. In Germany, the federal administration is obliged to design its publicly accessible internet and intranet services according to the Barrier-Free Information Technology Ordinance (BITV).
### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "web applications".

#### APP.3.1.M8 System architecture of a web application
Web applications generally use multiple IT system components; Web servers, web application servers, and background systems. The basis for the secure operation of a web application must be a suitable system architecture.

When designing the system architecture of the web application and networking the IT systems involved, the following points should be considered.

** Secure design of logic **

Web applications can map complex business processes that go beyond just displaying individual web pages. In the technical design of these processes, care must be taken that the implemented application logic can not be misused. For example, it should not break out of a designated process of the web application and thus the process of the process can be controlled from the outside.

The requirements for the depicted business logic must be precisely recorded and implemented correctly so that only intended and planned actions can be carried out. Deviant behavior must be rejected. If, for example, only recommended articles are to be sent by means of a recommendation function of the web application, it must be taken into consideration that this function can also be abused in order to send spam e-mails. If the recommendation text is specified in this example, spam emails can no longer be sent via this function. Furthermore, it must also be checked whether errors in the business logic can occur through two concurrent sessions (race conditions).

When designing the web application, all functions should therefore be documented based on use cases. It should be recorded for which purposes the functions should be used and how misuse can be avoided.

If the web application is aborted for any reason, the logic must ensure that the web application returns to a consistent state (roll back).

Interactive features in web offerings can also be implemented through active content running on the client system (eg via JavaScript). Often it is also possible to provide these functions with dynamic or static content. Because the use of active content on the client systems is often disabled for security reasons, it is recommended to design the web application as far as possible without active content and to implement the application logic purely on the server side.

Interactive functions in web applications can be realized in different ways: server-side or client-side. Since the client is not under the control of the web application, it can not be ruled out that it will be misused. Active content such as JavaScript or ActiveX has been and still is exploited to attack web applications and the information they manage. For safety reasons, it is therefore advisable to implement active content on the server side or, if possible, to do without it.

If active content is to be used, the following points should be noted:

* It should be ensured that the web application can be used even if the execution of active content in the browser is disabled.
* For active content should be as comprehensible as possible, from which source they come, so that an effective check can be made in the client. This can be achieved, for example, by the signature of ActiveX components.
* If using Ajax makes it inevitable to serialize and dynamically generate XML data, frameworks should be used.
* If JavaScript is used, the function call * eval () * should be omitted.
* If the web application JSON is used for data exchange, only objects are to be used as top-level elements.
Examples:
* A web application authenticates users in multiple, sequential steps. The users have to use user name and password in the first step and an authentication token in the second step. The first step should not be skipped to ensure that all authentication features are entered. In the final step for the final authentication, all authentication features must then be checked again.
* Even in the conception phase of a banking application, it must be considered that a user can also enter negative amounts in a transfer form. The web application must ensure that this does not reverse the logic of the remittance form and that no unanticipated credit is triggered.
** separation according to server roles **

The server services of the web application (eg web server, application server, database server) should each be operated on separate IT systems. If this approach exploits a vulnerability in the system of an exposed component (eg in the web server), the data stored on other system components (eg the database) is not directly affected.

A separation of the server roles can also be implemented by a server virtualization. If a server virtualization is needed, the module SYS.1.5 * Server Virtualization * must be taken into account during implementation.

** Restricted accounts for server processes of system components **

You should use separate accounts for the different server processes of the system components (for example, a separate system user for the web server process). At the same time, the rights of these service accounts at the operating system level must be limited so that only the necessary resources and files of the operating system can be accessed. In this way, even after a successful server compromise, an attacker has limited privileges, making access at the operating system level more difficult.

** Multilayer network architecture **

The Web application IT system components should be decoupled in the security gateway in demilitarized zones (DMZs) according to protection needs.

The network architecture should follow a multi-tiered approach (multi-tier architecture). At least the following security zones should be considered:

* Web layer
 This layer is adjacent to the untrusted network (eg, Internet) and represents the exposed layer with direct access by users. Packet filters between adjacent networks (e.g., application layer and Internet) should filter the traffic so that there is no direct access the untrusted network beyond the mesh limits of the Web layer. In this layer systems such as the web server should be placed, which occupy an exposed position and z. B. require direct access by users.
* Application layer
 The application layer should be adjacent to the Web layer and to the data layer. The network traffic to the adjacent networks should be filtered by packet filters, so that no direct access between the adjacent networks is possible. In this network segment, systems and servers should be placed with the application logic (eg the application server with the web application). The systems access data from the adjacent data layer (eg, databases), process it, and make it available to systems in the Web layer (eg, the Web server).
* Data Layer
The data layer is the most trusted zone of the multi-layered architecture. Packet filters between the adjacent networks should regulate the traffic. In this layer, the background applications of the web application, such as Databases, directory service and legacy systems. Access to these systems should only be possible from adjacent networks (eg application layer). The data layer is to be implemented as a separate zone and should not be integrated into other zones (eg Intranet).
It should not be possible to access systems on the intranet from the above zones. If z. For example, if a directory service is used for the authentication on the web application, a dedicated domain on dedicated hardware should be used for this purpose.

Filtering of the traffic should be done by separate filter components (eg packet filter). If the protection requirement is high, the filter components should be replaced or supplemented by systems with filter functions at higher protocol levels (eg Application Level Gateway). The application level gateway should be integrated into a separate security zone, which receives the requests of the users before the systems of the web layer.

** documentation of the architecture **

Understanding the software architecture of a web application is necessary to maintain, develop and extend it efficiently and error-free. When documenting web applications, there are some peculiarities to consider.

The documentation must take all components into account. At least the following points should be covered by the specific documentation:

* All dependencies (for example on frameworks, libraries, operating systems, hardware) and interfaces (for example on background systems) should be documented.
* Components required for operation that are not part of the web application must be labeled as such, for example, background systems such as a database.
* Documentation must identify which components implement security mechanisms. The following are the security features of Web applications that should be considered at least:

 
+ User management,
+ Role and authorization concept,
+ Authentication,
+ Authorization,
+ Session management,
+ Logging and
+ Transport safety.


 
* The documentation must describe how the web application integrates with an existing network infrastructure. Here the requirement APP.3.1.M8 * System architecture of a web application * has to be considered.
* The used cryptographic functions and procedures must be documented, see module CON.1 * Crypto Concept *.
Documentation should be updated and adjusted throughout the project so that it can be used during development and documented decision-making.

#### APP.3.1.M9 Procurement, Development and Extension of Web Applications [Tester, Development Manager, Procurer, Developer]

If institutions want to use web applications, they can buy them in whole or in part on the market. In order to find a suitable product, suitable criteria must be defined. But institutions can also develop or extend a web application themselves. Again, rules need to be defined and adhered to (see section Development and Enlargement).

** Creation of a requirements catalog for standard software **

To solve a task that is handled with a web application, the market usually offers a variety of similar standard software products. Comparable in terms of their basic functionality, however, they differ in criteria such as acquisition and operating costs, additional functionalities, compatibility, administration, ergonomics and information security.
In order to be able to select a suitable web application, a catalog of requirements must first be created (see the module CON.5 standard software). The catalog of requirements should contain statements on, inter alia, the following points:

* Functional requirements
* IT deployment environment
* Compatibility and interoperability requirements
* Performance requirements
* Reliability requirements
* Conformity to standards
* Usability requirements
The security properties required for the product should also be listed in the requirements catalog. Typical security functions are for example

* Identification and authentication
* Access control
* Logging and log evaluation
* Data backup
* Encryption
* Data integrity features
In order to be able to compare different web applications from the market in the sense of a benefit analysis, a rating scale should be developed in which suitable criteria exist as to how the fulfillment of the individual requirements is assessed. For this purpose, it is necessary to assess quantitatively or qualitatively the significance of the individual requirements for the desired IT-based task fulfillment beforehand.

** development and expansion **

The following points should be considered when developing and extending web applications.

It should be developed according to a suitable process model (eg V-Modell XT, waterfall model, spiral model). An application has to go through all development phases of the procedure model before commissioning. The procedure model used should cover at least the following or comparable phases.

** ** Requirements Analysis

Enterprise security policies and company-specific requirements should be considered in the requirements analysis and made available to the development teams (eg meeting industry standards such as PCI DSS or accessibility requirements). These include z. For example, guidelines and requirements for the use of cryptographic algorithms and secure programming guidelines (see also section Implementation of Programming Guidelines).

At this stage, all data to be processed by the web application should be identified and classified according to protection needs. Appropriate protection mechanisms of the application must be established to protect the data according to their protection needs.

** Concept and design **

The design and architecture of the application should be defined and documented. Here development techniques (eg programming languages, frameworks) should be selected. Also the knowledge and the experience of the developers has to be considered for cost and security reasons.

The architecture should provide that components (eg for authorization, authentication) are preferably implemented in modules that can be reused. The central availability and use of modules avoids redundancies and makes maintenance easier.

For web applications, the central security mechanisms should be implemented at least server-side if possible.

Care should be taken to ensure that security requirements are fully met by security mechanisms and recorded for the creation of test cases.

Decisions taken should be documented, so that efficient further development of the application is ensured by sufficient documentation later on.

**Development**

When implementing the application, programming guidelines (see also section Implementation of Programming Guidelines) for the safe development of the components should be observed.
Care should be taken to ensure that the documentation is continued during the development work (eg by comments in the source code and tools for generating the documentation). Thus, the source code at a later date for third parties is traceable.

To protect against the loss of already developed and rejected solutions as well as for documentation purposes, the history of the changes should be recorded (eg by a revision system).

**Testing**

Test cases should not only consider the business functions but also the security functionality. These include z. B. Security components such as authorization, authentication and filtering components. Whenever possible, penetration tests and, for high protection needs, source code analysis should be performed to control the implemented security mechanisms (APP.3.1.M21 * Performing Penetration Tests *).

Before an application is operated, not only the functionality, but also a possible abuse of the offered functionality should be checked. This can be achieved by penetration tests. In order to be tested on a four-eye basis, the tests should not be performed by persons who were previously involved in the design or development of the application.

During the tests, it must be ensured that they are performed only with test data and not with live data or customer data.

For web applications, web pages should be tested for compliance with the standard used (eg HTML standard). This avoids unforeseen side effects due to browser misinterpretation. A review with different browsers can be very helpful here.

When planning and performing the tests, consideration should be given to the requirement APP.3.1.M10 * Software Acceptance and Release Procedure *.

** Integration and Software Distribution (Deployment) **

Before the productive commissioning, the web applications and necessary background systems must be configured securely. Here, the connection of possible background systems (eg identity memory, databases) to the application should be considered. Before putting the application into operation, it must also be ensured that the transport channel is protected.

Protective data of the web application are often stored in background systems. Therefore, the security level of the application and possible background systems should be consistent. Access to the background systems should only be possible for users through the defined interfaces of the application.

In addition, it should be ensured that the data can not be manipulated by third parties when distributing the application.

** Maintenance **

A process for maintaining the application needs to be defined, which also includes periodically checking the security of the application for vulnerabilities or available patches.

When adapting or extending the application, care must be taken not to compromise the security mechanisms. In addition, tests in a separate test environment should recheck whether the security mechanisms are still working properly.

** Implementation of programming guidelines **

A programming policy helps to define a common programming style and to establish a uniform level of security (eg through the use of security libraries). The quality and comprehensibility of the source code can thereby be improved and made more comprehensible. As a result, errors and vulnerabilities can be found easier and a later extension of the application can be implemented cost-effectively.

Programming guidelines should be implemented not only in-house development but also outsourcing of development activity.

** Future-proof development of security mechanisms **
When designing and developing security mechanisms, future developments in attack techniques as well as standards (eg, new HTML standard) should also be considered. For example, a filter component that filters harmful-classified <script> tags should also filter unknown tags. At the time of development, unknown tags may be used in the future (for example, with the introduction of a new HTML standard) to bypass web application security mechanisms.

** Product-specific security functionality **

If a web application is used exclusively with a specific browser, the use of product-specific security features of the browser should be taken into account.

** Application Development Outsourcing **

In the case of outsourcing, it must be ensured that the contractor meets the necessary security requirements when developing the application. This can be achieved, for example, by specifying a procedure model or by programming guidelines.

If a service provider is commissioned to develop an application with a high protection requirement, the source code (eg the project archive) should be under the administrative control of the client. At the same time, the client should be able to access the source code of the application at any time and be able to follow changes to the source code.

** Definition of the development environment **

The production, test and development environments are operated on separate systems. Different access data should be selected in the environments. Test accounts should not receive privileged rights where possible. Basically, successful attacks on the development or test environment should not affect the production environment.

#### APP.3.1.M10 Acceptance and release of web applications [Head IT]

As part of a software acceptance process, it is checked whether the considered software, for example a web application, reliably provides the required functionality and, moreover, whether it has no unwanted side effects. The subsequent release of the software by the competent authority grants permission to use the software. At the same time, this position also assumes responsibility for the IT process that is implemented by the software.

In the case of software acceptance, it makes sense to distinguish between software that was developed by itself or on assignment, and standard software that is adapted only for the specific application.

** Acceptance of self-developed or commissioned software **

Before the order for software development is awarded internally or externally, the requirement definition for the software must be created, from which the rough and detailed concept for the realization is developed. On the basis of these documents, the responsible body draws up an inspection plan.

Usually, test cases and the expected results for the software are developed. On the basis of these test cases, the software is tested and the comparison between the calculated and the expected result is used as an indication of the correctness of the software.

To develop the test cases and to carry out the tests, the following should be noted:

* the test cases are developed by the competent authority,
* for test cases no data of the active operation is used,
* Test data, in particular if the active data are copied for this purpose, must not contain any confidential information and personal data must be anonymised or simulated,
* The test must not affect the current operation. If possible, a logically or physically isolated test computer should be used.
A decrease is to be refused if:

* serious errors are detected in the software
* Test cases occur where expected results do not match those calculated
* User manuals or manuals are not available or of inadequate quality and
* The software, including the source code and processes, is not or not sufficiently documented.
The results of the acceptance must be recorded in writing. The documentation of the acceptance result should include:

* Name and version number of the software and if necessary the IT-procedure,
* Description of the test environment,
* Test cases and test results and
* Declaration of acceptance.
** decrease of standard software **

If standard software is procured, it should also be accepted and released. In the decrease should be checked whether

* the software is free of computer viruses,
* the software is compatible with the other products used,
* the software is executable in the desired operating environment and which parameters are to be set,
* The software was delivered complete including the required documentation and
* the required functionality is fulfilled.
** Release procedure **

If the software has been approved, it must then be released for use. To do this, first determine who is authorized to release software. The release of the software must be specified in writing and suitably filed.

The release statement should include:

* Name and version number of the software and if necessary the IT-procedure,
* Confirmation that the acceptance has been made properly,
* Restrictions on use (parameter setting, user group ...),
* Release date, from when the software may be used and
* the actual release.
If IT technically possible, it must be prevented that software can be changed or manipulated unnoticed after release, for example by means of suitable integrity protection methods. Otherwise, appropriate organizational rules must be established to prevent or promptly detect changes to the software.

Even after intensive acceptance tests, errors in the software may be detected during ongoing use. In this case, it is necessary to determine how to proceed in such an error case (contact person, troubleshooting process, involvement of the responsible authority, repetition of acceptance and release, version control).

Further explanations can be found in the module CON.5 * standard software * *. *

#### APP.3.1.M11 Secure connection of background systems

Web applications often use background systems, such as database maintenance or directory services user management. The data must also be adequately protected during transmission and storage in background systems. To do this, the background systems must be securely connected to the web application.

Typical background systems of web applications are: databases, directory services, middleware, web services, and legacy systems.

For the secure connection of background systems the following points should be considered:

** Placement of and access to the background systems **

Users of the web application should not be able to directly access the background systems as this may circumvent protection measures. Instead, they should be allowed to access it only through pre-defined interfaces and features of the web application.

In addition, the connection to the background systems should be additionally protected. For this purpose, the systems should authenticate themselves before the data transmission and encrypt the transmitted data so that they can not be read or changed unnoticed (for example by means of SSL / TLS).

If the IT systems involved are connected via insecure channels, a cryptographically secured tunnel with appropriate encryption and authentication should always be used.
Access to background systems should be done with minimal rights. For this purpose, service accounts should be set up on the respective background system.

If a single service account is used to access a background system, all requests in the security context of that service account are processed. This then applies both to access by users with restricted access authorizations and to access by administrative users. To prevent this, several service accounts with different access rights should be used for a background system.

In a suitable system environment, the user accounts may be forwarded to the background system, for example when using a directory service that both the web application and the background system manage the users. In this way, the privileges can be limited to the necessary rights of the user logged on to the web application.

It is important to ensure that unauthorized access to the web application uses its own service account in the directory service with restricted permissions.

** Enterprise Service Bus **

In the context of so-called service-oriented architectures (SOA), web applications are often connected to background systems via an enterprise service bus (ESB) as a central communication infrastructure. This ensures that only the interface to the ESB needs to be defined and implemented for each application, and not many separate interfaces to other applications and services. In a separate directory (* Repository *) the ESB stores metadata about the connected services.

In addition, the ESB can also implement central safety functions to further protect the connected applications. Such security features can, for example, detect and prevent replay attacks or check XML data for potentially harmful content, but also log message exchange centrally and audit-proof.

When using an ESB, ensure that all services authenticate to the ESB before they are allowed access. This also applies to access to the ESB repository. The ESB must be integrated into the network architecture so that access is only possible from the servers of the connected applications and services and external access to the ESB is excluded. For this purpose, the ESB should have its own logical network segment. The ESB must perform its own authorization check to verify that access to the requested service is permitted by the requesting service or requesting application. In particular, it must be ensured that applications or services with external contact do not access internal services that are not intended for this purpose. Such applications must not gain knowledge of internal services and their interfaces through the ESB repository. If the service-oriented architecture encompasses several security domains, for example a DMZ with externally invocable services and an internal network with backend systems, the ESB must also be divided into appropriate security domains with controlled transitions, or several ESBs must be implemented for the individual security zones ,

If the ESB does not communicate exclusively locally in a protected data center network, the communication between the ESB and the connected applications must be adequately secured (authentication and encryption).

By bundling the communication of many applications and services, the availability of the ESB is of particular importance. This must be taken into account in the implementation and operation of the ESB by redundancies and appropriate monitoring of the service.

#### APP.3.1.M12 Secure Configuration of Web Applications [Developer]
If a web application is poorly configured, an attacker may be able to overcome existing security mechanisms. Therefore, the following points should be considered when configuring the web application:

** Disabling unnecessary HTTP methods **

A web application can be accessed using HTTP methods using different HTTP methods (for example, * GET, POST, PUT, DELETE *, or * TRACE *). Typically, however, a web application requires only a very limited set of these HTTP methods (for example, * GET * and * POST *).

In addition, a web application can respond differently to a request, depending on the HTTP method used. For example, if the input data filtering is performed only on a GET or POST request, this security function could be bypassed by calling an unintended HTTP method.

Some HTTP methods (such as * PUT *) provide access to security-critical functionality (such as uploading arbitrary files), allowing you to bypass Web application restrictions (for example, file type checking for an upload function). ,

Therefore, unneeded HTTP methods should be disabled and not edited by the web application. This also applies to fictitious HTTP methods that are not defined in the corresponding standard RFC 2616. Even if the HTTP methods have already been deactivated in the configuration of the web server, the web application should not process unneeded HTTP requests.

** character encoding configuration **

The transmitted data between the user's client and the web application may be in different encodings. Depending on the expected encoding, the data is interpreted differently by clients, the Web application, or the background systems. In order for clients to send data to the Web application in the desired encoding, the Web application should specify the character encoding scheme (for example, UTF-8) when delivering Web pages in the header fields of the HTTP response.

If the web application is used internationally, care should be taken to ensure that all international character sets are supported at all logical levels of the web application and the attached background systems.

** setting of limits **

Some protections include the use of limit values ​​(see eg APP.3.1.M7 * Protection against unauthorized automated use of web applications *). If a limit value is exceeded, the temporary blocking of an affected function or resource is often carried out. For example, failed login attempts can result in the user account being blocked (for example, to prevent brute force attacks).

However, such measures can affect the operation of the web application and thus also affect uninvolved users. For example, these users will not be able to log in to the web application if their user account has been suspended.

These effects should therefore also be taken into account when setting limit values.

** Restrictive file system permissions **

Web applications often provide users with direct or indirect access to the underlying file system (for example, via retrievable files or an upload feature). In order for an attacker to be able to read or manipulate unauthorized files that are worthy of protection, they should be protected by restrictive file system permissions in addition to the web application-level access restrictions. The server running the web application must be started with restricted privileges and not as administrator (root).

** Administration of a web application **
The web application should primarily be administered via a system decoupled from the application. For example, in the case of an ecommerce application, article maintenance may be via a separate system with access to the database of the web application. Ideally, the system should be designed solely for this purpose and not directly connected to the web application. Accordingly, the web application should retrieve the item data exclusively from the database.

Often web administration applications offer a web interface on the same server. This feature should be avoided and instead the web application should be administered via a separate system. If administration is required on the same server, the administration interface should only be accessible from the administration network and access by ordinary users of the web application should not be possible. Ways to administer the web application that are not used (eg console) should be disabled.

#### APP.3.1.M13 Restrictive release of security relevant information [developer]

Websites and Web application responses can include security-related information that helps attackers bypass security mechanisms and exploit vulnerabilities. Therefore, no security-related information should be displayed that is not necessarily required for the operation and use of the web application.

The following examples illustrate what information can contain security-related information and how it can be prevented from being disclosed.

** No security-related information in error messages **

If an error occurs during the operation of the web application (for example, access errors), neutral error messages should be sent to the user. The error messages must not allow any direct conclusions about techniques, security mechanisms and conditions of the web application. Examples of information that should not be included in error messages:

* Stack traces and debugging information,
* Messages such as * username invalid * or * password invalid * (invalid instead of general error messages such as * username or password *),
* error messages passed on by background systems, for example SQL error messages of a database instead of a message * error in checking the access data *,
* Error codes instead of, for example, the message * An error has occurred *.
In the case of a failed authentication, for example, regardless of the validity of the user name, a general message such as * Incorrect or invalid access data * should always be output so that an attacker can not infer the existence of user accounts (user enumeration).

Basically, different HTML code can lead to the same output in the web browser. For example, two HTML pages with a different number of spaces in the browser are displayed the same, although they differ in HTML code. It is therefore important to ensure that the error messages are identical not only in the representation in the browser, but also in the HTML code. This is to prevent an attacker from being able to conclude the validity of partial entries (for example, a valid user name with an incorrect password) due to a changed HTML code.

Further information on error handling can be found in APP.3.1.M16 * Error Handling *.

** Prevention of "WS-Interface Probing" **
When generating Web Services Description Language (WSDL) files, make sure that the tools or frameworks used do not write additional and possibly safety-critical information into the files. Therefore, the files are to be examined first before they are published. If necessary, the tools or frameworks must then be reconfigured so that they no longer write any security-critical information to the WSDL files, or the files must be subsequently cleaned up.

XML transport containers should generally not pass error messages with detailed information to users (potential attackers). The messages should be general or generic in such a way that they do not contain any information about the applications, frameworks and version numbers used and also do not allow them to be inferred.

If services can only be searched and called by certain users known to the service provider, it is a good idea to protect the WSDL files or their repositories from direct and unauthorized access by means of a previous user authentication.

** Prevention of security-related comments in delivered websites **

When developing web applications, comments may be written to the HTML code. These comments may contain security-related information (for example, to-do lists, version numbers, credentials, or uninterpreted source code) that can be easily viewed by the user as HTML comments in the web page. For this reason, care must be taken to ensure that no safety-relevant information is contained in the comments. Ideally, no comments should be used in the delivered web pages or responses from a live web application.

** Limited access to documentation **

Information in the documentation of a web application can alert an attacker to potential vulnerabilities (for example, default users after installation). They can be abused to prepare for attacks. Therefore, unnecessary documentation about the web application and its components (for example, database) should be deleted. If the documentation is available online, only the appropriate addressee group should be able to access it. For example, the documentation for administering a web application should not be accessible from the Internet.

** Delete unneeded files **

Running a web application often results in files that are not needed for production (for example, temporary files, or backup files). These files may contain security-critical information (for example, test results) or offer functions (for example, test tools for determining version numbers of the libraries used) that can be used for attacks on the web application.

In addition, it should be noted that especially with temporary files or backup files often other file extensions (for example, * .bak files as backup copies of an editor) are used. If these files are retrieved from the web server, it would be possible that the files are no longer interpreted due to the unknown file extension and instead the source code of the web application is delivered.
Versioning systems usually create files or folder structures for the objects they manage (for example, folders such as * .svn * or * .git *). These files or folders often contain detailed information about the managed projects and may allow complete access to the source code. For this reason, applications or application components should not be applied to production systems via versioning. At a minimum, access to files and folders created by the versioning software should be blocked.

For the above reasons, all files that are not needed for productive operation must be deleted. In addition, you should check regularly whether new files have been created and whether they can be deleted. If this is not possible, access to these files can be blocked.

** Secure registration by external search engines **

Search engines use so-called agents (also called robots or crawlers) to index new or changed content in the network. These agents can be instructed by the * robots.txt * file in the Web application root directory to ignore designated resources (for example, paths) of the Web application. In this way, sensitive information can be excluded from indexing in the search engine. The confidential resources (for example, directory paths) should be listed in the * robots.txt * file under the * Disallow * directive. This causes the agents not to index the listed resources.

So that the entries in the file * robots.txt * do not give an attacker an indication of security-critical resources of the web application, all directories to be protected should, if possible, be grouped together in a separate directory of the web application. Only this directory should be entered in the file * robots.txt * so that it does not contain any internal directory structures with security-relevant information.

** Protection against directory traversal attacks **

Access to resources may only take place with the rights required for this purpose and after prior authentication. Consequently, suitable authentication mechanisms have to be implemented as well as strict access rules (policies) to be defined and implemented. In addition, an intrusion detection system can be used to detect directory traversal attacks.

** Avoidance of product and version information **

Frequently, responses and output from each component of the web application include product name and version number information. This information may be contained, for example, in HTTP headers or in comments in the HTML source text of the delivered web pages. Based on this information, an attacker can search for known vulnerabilities of the product and use them to attack the web application. Therefore, information about products and versions used should be avoided (for example, application framework, web server).

** waiver of absolute path information **

Absolute paths often allow conclusions about the internal structure and structure of the web application. For example, the location of information worth protecting can be determined. Therefore, if possible, no absolute paths of the web application should be published.

#### APP.3.1.M14 Protection of confidential data [developer]

The following measures should be taken to protect sensitive data in web applications.

** General aspects **

When sensitive data is processed, transmitted, or stored by the web application (both server-side and client-side), it should be protected by cryptographic techniques. Even if the web application is compromised, the cryptographic methods used should continue to protect that data.

Confidential data of a web application are e.g. B .:

* Access data (eg user, password),
* Authentication data (eg session ID),
* critical data processed by the web application (eg payment information or health data).
Cryptographic methods can be used in the processing, transmission and storage of this data by the web application and by the clients. You can z. B. be used as follows:

* Encryption of data,
* secure storage of access data,
* Protection of the transport channel.
Care must be taken to select cryptographic algorithms for the respective application which correspond to the state of the art and have no known weak points. The cryptographic algorithms should be implemented on the server side.

A special meaning with the cryptography comes to the used keys. Depending on the field of application, these must have a certain minimum length and satisfy various mathematical requirements (eg complexity). In addition, a correspondingly secure transport or exchange of keys must be ensured. The same applies to their storage. When designing a web application, these points should be regulated and summarized in a crypto concept (see CON.1 * crypto concept *).

For web applications with a high protection requirement, it may additionally be necessary to secure the user data. For example, if social data with high confidentiality requirements is being processed by the web application, this data may be encrypted by the web application prior to storage. This ensures that even with direct access to the database (eg by database administrators) no usable data can be read out.

** Secure handling of SSL / TLS **

If confidential data is transmitted, it can be protected against unauthorized knowledge or manipulation by means of a secure transport channel. Therefore, before transferring confidential data, you should switch to a secure connection. Even after a user has logged in, the transmitted data should continue to be protected by a secure connection. The transport channel is usually secured by the use of SSL / TLS. Further information can be found in the module APP.3.2 * Webserver *.

In addition, care must be taken to ensure that no errors occur during the SSL / TLS connection setup or during the transmission of data over an encrypted channel to an unencrypted connection. Instead, the connection should be renewed or rejected. It must be prevented that confidential data is transmitted over an unsecured connection (eg by setting the secure flag for cookies).

When establishing an SSL / TLS connection, the encryption mode to be used is negotiated between client and server. Among the available algorithms are those that can no longer be considered safe. In particular, there is also the so-called zero-encryption mode, in which no encryption takes place. When configuring the web server to use SSL / TLS, care must be taken that the server does not accept any of the weak algorithms, and in particular, not the null-encryption mode. Otherwise, it might happen that a secure connection appears to be established (using https), which is in fact too weak or not encrypted at all. Such a situation could be deliberately brought about by an attacker to intercept authentication information and other data. Therefore, in the SSL / TLS configuration of the Web server, the use of the Null Encryption mode and the weak algorithms should be disabled.

** Force the HTTP POST method **
When operating a web application, typically, data (eg, form data or the session ID) is transmitted to the web application. This data can be transferred as parameters in the URL (GET method) and in the body of the HTTP request (POST method).

When using the GET method, sensitive data such as form data is visible in the URL (for example, in the browser history) and can be logged and stored by intermediate systems.

Therefore, sensitive data should only be transferred via the POST method. It should be noted that frameworks often abstract the HTTP request method. Incorrect configuration of the framework may still allow both methods to be allowed, even though the web application is forcibly constrained to the POST method (for example, by forwarding an HTTP GET request to an HTTP POST request through the framework ).

** Protection of client-side stored data **

The data exchanged between the client and the web application can be cached by the client in the local browser cache. If the browser caches the data beyond the session duration, it can be retrieved from people with access to the user's machine and from scripts and browser plug-ins without additional access control.

The client-side caching of Web application sensitive data can be prevented by the following directives in the HTTP headers of the Web application:

* Cache-Control: * no-cache, no-store *
* Pragma: * no-cache *
* Expires: * -1 *
Since the web browser is usually not under the control of the operator of the web application, thus can not be completely ruled out that data is still cached. Therefore, for high-security Web applications, it may additionally be necessary for the user to deactivate or delete the browser cache during operation of the web application once it has completed its activities on the web application. In this case, for example, after the user has logged out, the user can be informed that the browser cache should be deleted. This particularly applies to web applications used by public IT systems. Alternatively, the user may be advised to use the browser's private mode, which does not cache data about the session.

Often, when operating a web application, data is stored in cookies on the client. Each time you access the web application, these cookies are transmitted transparently to the user to the web application. This can also be sensitive data such as the session ID. The access to cookies with confidential data should therefore be limited as much as possible. When cookies are created by the web application, the following cookie flags should be set:

* Domain
 The cookie flag should not be set, because then by default only queries of the domain that set the cookie are answered. Should it be necessary to allow this to be shared with other (sub-) domains as well, the domain should be restricted as much as possible without restricting the functionality of the web application (eg * webapp.domain.tld * instead of * domain.tld *).
* Path
 The Path attribute limits the validity of the cookie to a specified path of the web application. Also, the path attribute should be restricted as much as possible without restricting the functionality of the web application (for example, * / webapp / * instead of * / *).
* Secure
 If the directive Secure is set, the cookie will only be transmitted via encrypted communication channels, such as: Over SSL / TLS.
* HttpOnly
 This directive prevents client-side scripts from accessing the cookie (for example, JavaScript). It should be noted that this attribute is not supported by all browsers.
The following example shows the statement that creates a cookie using these directives:

* Set-Cookie: SESSIONID = sl342kdfjslaal39skdj; path = / webapp; secure; HTTPOnly *

When authenticating the user to a web application, an HTML form is usually used in which the user name and password are entered. If the user types his password into the password field, it should not be rendered in clear text, but replaced by so-called wildcards (eg stars or dots). To do this, the password field type must be selected in the form definition (* type = "password" *).

In addition, the web browser can be instructed not to cache sensitive form data (eg, username and password) and suggest as a selection the next time the form is invoked. The option * autocomplete = "Off" * should be set when defining the form in the form header.

During a user's session with a web application, user-specific data typically needs to be stored (for example, the items in the shopping cart). This data can be stored not only on the server side, but also on the client side in a cookie or in the web storage of the browser. In principle, it should be avoided to transfer confidential data to the client or to save it on the client, since the web application has no influence on the protection of client-side stored data. For example, security mechanisms used by the browser on the client to protect data can often be bypassed (for example, by direct access to the file system by local users or through cross-site scripting). Instead, confidential data should in principle be stored on the server side and only the identification feature of the user (eg the session ID) should be stored on the client side.

If it is unavoidable to store the session data on the client side, that data should be encrypted and checked for integrity before being processed by the web application. This ensures that the data can not be viewed without authorization during the transfer or that it can be manipulated unnoticed.

In addition, the data should preferably be stored only over the period of the session and not persistently. The Web storage mechanism should therefore prefer the sessionStorage object before the localStorage object.

** Protection of server-side data **

If users can log on to the web application, access data must be stored on the web application. In order to protect the access data even after a possible compromise of the web application by an attacker, they must not be stored in plain text. Instead, they should be deposited as * salted hashes * using timely cryptographic algorithms that append a random string to the plaintext. Here, a different, random salt should be used for each password.

In addition, the access data should be stored on the server side on a trustworthy IT system (eg on the web application) and in a protected area (eg outside the web root directory or in separate database tables). The access data should not be stored in the source code of the web application (hardcoded passwords).

In addition, only the web application should be able to access the access data with write access. The access data should only be able to be changed by the user and via the intended interfaces and functions of the web application, so that it is not possible for users to access access data without authorization. For example, to read, modify or delete through direct access to the file system.
When a user calls a Web page from the Web application, the page is typically created by the application at runtime. The called file contains code that is interpreted by the web application before delivery and returns a web page. This website is sent to the user.

Usually, file extensions are used to associate these file types with an interpreter or parser. If the file extension changes, it may be transmitted to the user without first being interpreted. When such files are retrieved, the user is given access to the program logic and sensitive information that may be stored in the code. This can affect any file whose file extension is not associated with an interpreter or parser. Examples of vulnerable files are:

* temporary files (eg * temp.tmp *),
* Backup data (eg * backup.bak *),
* Configuration files (eg * config.conf *),
* files to include (for example, * include.inc *).
The files may contain sensitive information such as access data that can be retrieved in the event of insufficient access restriction.

Therefore, files that are not intended for interpretation and direct retrieval by the user should not be served by the web application. In addition, the file system permissions on these files should be restrictive. Unnecessary files should be deleted in a timely manner (see also APP.3.1.M12 * Secure Configuration of Web Applications *, section Deleting Unnecessary Files).

** Storage of configuration files outside of web root **

Web application configuration files often contain sensitive information, such as: B. access data. Therefore, users of the web application should not be able to access the configuration files.

For this reason, configuration files should only be stored outside of the web server root directory. Outside this directory, data is typically not delivered by the web application.

Basically, configuration data outside the source code must be stored in separate configuration files. Configuration settings that contain sensitive data should also be encrypted.

#### APP.3.1.M15 Verification of essential changes

If important entries are to be changed, such as passwords and configurations, the password entry should be re-verified. Users should be notified of changes via communication paths outside the web application, for example by e-mail.

#### APP.3.1.M16 Comprehensive input and output validation [developer]

By reliably and thoroughly filtering the input and output data of web applications using a validation component, effective protection against common attacks can be achieved. Here, both the input data from users to the web application and the output data of the web application to the clients or to downstream systems, such as databases, should be filtered and output (output). This ensures that only expected and no corrupted data is processed or output.

If it is necessary for individual functions to set the data filter to be less restrictive, this must be explicitly defined and documented when accessing the data. In addition, it is possible to use context-sensitive filters in the business logic of the application or in the background systems.

For a secure processing of the data, the following points should be taken into account during the implementation and configuration of the validation component:

** Identification of the data **
In order for the input and output data to be comprehensively validated, all data structures to be processed (for example, the e-mail address) and the values ​​permitted therein must first be identified. For each data structure a corresponding validation routine should be implemented. In addition to the data structure, the type of data processing should also be recorded, for example forwarding to an interpreter, return to the client, storage in a database.

** Consideration of all data and data formats **

The validation component should take into account all data formats and interpreters to be processed. Typical data formats for web applications are, for example, personal data (name, telephone number, postal code), images, PDF files and formatted texts. Typical interpreters for data processed or output by web applications include HTML renderers, SQL, XML, JSON, LDAP interpreters, and the operating system.

Data can be validated by different techniques. Thus, the validation component can check the value range of the inputs or, for example, regular expressions can be used to validate allowed characters and the length of the expected data. Among other things, the validity of XML data can be verified using the appropriate XML schema. In addition, frameworks and libraries provide validation capabilities for common data formats.

The following characters are usually interpreted by programs used in web applications and can therefore be used by potential attackers to inject malicious code. For this reason, they should be considered in the filtering:

NULL, linefeed, carriage return, single quotes, commas, slashes, spaces, tab characters, greater than and less than, XML and HTML tags. (The list is not complete.)

In addition, the interpreter character sets (for example, SQL syntax) may vary for different products. Examples of critical characters are listed in the section * Potentially dangerous characters for interpreters * in * Tools for the Web applications module [GSSID].

In addition to the actual user data (for example, form parameters in GET or POST variables), data of other sources (secondary data) must also be validated. These include, for example:

* Names of form variables (they can be arbitrarily manipulated as well as the value of the form variable),
* HTTP header fields (header fields in HTTP requests and responses should contain only ASCII characters and, for example, no newline characters like * \ r \ n *),
* Session IDs (for example, cookies).
Automated calls by the client, for example through Ajax or Flash scripts or JSON requests, must also be checked.

The background systems should be validated (if necessary, renewed). This also applies if, for example, data is read out again after a successful write to the database since the data in the database may have been changed in the meantime.

However, malicious code can also be transmitted through a way that can not be controlled by the web application (for example, FTP, NFS). If an attacker can use these services to modify or create files that are integrated by the web application, he can embed malicious code via this detour. In the so-called cross-channel scripting JavaScript code is inserted in this way, which is executed by the browser similar to persistent cross-site scripting. Therefore, regardless of the source, all data should always be validated prior to output to the user or further processing by the application.

** Server-side validation **
Typically, users access the web application with generic clients (for example, web browsers). These clients are not in the security context of the web application, but are under the control of the users. Data validation should therefore be implemented as a server-side security mechanism on a trustworthy IT system.

If additional data is processed by the web application on the client side (for example, JavaScript code), this data should also be validated on the client. The supplied scripts of the web application should provide the corresponding validation routines. If the data is sent to the server in the downstream processing process, it should be noted that the client-side check can not replace the server-side validation.

** ** validation approach

Data validation distinguishes between the white list approach and the black list approach.

A white-list approach only allows for data that is included in the list. Starting with as small a set of characters as possible, rules are created that allow data in a defined character space and reject data that contains different characters. Complex rules should be mapped by using simple rules sequentially.

On the other hand, in a black list approach, those data that are included in the list are rejected as inadmissible. Any data that is not explicitly prohibited will be accepted in this approach.

With the black list approach, however, there is a risk that not all variations of inadmissible data are taken into account and thus recognized. Therefore, the White List approach should be preferred to the Black List approach.

** Canonization before validation **

Data can be in different encodings (for example UTF-8, ISO 8859-1) and notations (for example UTF-8 is * "." = "2E" = "C0 AE" *). Depending on the coding scheme used, the same value can therefore be interpreted differently. If the data is validated without regard to coding and notation, potentially damaging data will not be detected and filtered. Therefore, all data should be converted to a consistent, normalized form before validation. This process is called canonization of the data. The data presented in this way are then processed further. If AJAX is used, it should also be reloaded using the * textContent * property instead of * innerHTML *, as * textContent * automatically encrypts.

In addition, the web application should explicitly set the encoding scheme when delivering data (for example, via the Content-Type header: * charset = ISO-8859-1 *).

** Context sensitive data masking **

If potentially harmful data needs to be processed by a web application (for example, characters that are meaningful to interpreters), and thus filtering can not be performed, then that data must be masked and converted into a different representation. In this masked form, the data is no longer interpreted as executable code. Since the masking is interpreter-specific, all interpreters used must be taken into account (for example, SQL, LDAP). Accordingly, context-sensitive must be masked for the expected input and output format and the interpreter language. Due to the complexity and specific requirements of different interpreter languages, it is recommended to use specialized libraries for masking.

In principle, all characters classified as unsafe for the intended interpreter should be masked. These include, for example:

* unexpected JavaScript and HTML for delivery to the client (for example, the web browser),
* illegally inserted SQL statements to the database (for example, from entries in form fields),
* Commands to the operating system (for example, in manipulated HTTP variables).
Masking is performed by converting the affected data or metacharacters of the respective interpreter language into so-called character references. The following example shows selected HTML characters with the corresponding character references (HTML entities):

* * & * => * & amp; *
* * <* => * & lt; *
* *> * => * & gt; *
* * "* => *" *
* * '* => *' *
Make sure that * & * characters are replaced in the first pass and that no multiple masking is used, as this character is reused in character references other than metacharacters.

** Using a custom markup to filter HTML tags **

If the web application requires HTML formatting tags in user input (for example, to format user posts), allowed HTML tags should be distinguished from and filtered by problem tags (see also section Context sensitive masking of data).

With this approach, there is a high risk of overlooking problematic tags (for example, * <script> *). Even apparently harmless tags can be partially misused via attributes like * onMouseOver * to execute code. Therefore, the alternative approach of defining the user's markup with custom markup tags (BBCode, for example) should be preferred. These markup tags are then translated by the application into its HTML tags. Traditional tags or problematic characters are still filtered.

One possible technique for allowing simple markup is to use * {* and *} * instead of * <* and *> *. Fat would then be written as * {F} ** This is bold ** {/ F} * and an image could be placed this way: * {img src = / images / img.gif width = 1 height = 1 img} *.

Here, the conversion into HTML must not simply replace curly braces with angle brackets, but must look at each day as a whole:

* * {img * after * <img *,
* * img} * after *> *,
* * src = file * after * src = "file" * (where file is to be additionally filtered).
When HTML tags are allowed, always make sure that at least the following tags are not allowed:

* Applet
* base
* iframe
* link
* object
* script
* style
These tags allow any content to be included in the web page. These may therefore not be used.

** Preventing Code Injections in SOAP Messages **

Generally, submissions should never be passed without prior checking. In order to avoid injection attacks, it is necessary to filter input parameters from the interface description (WSDL file) for harmful code and, for example, to allow only system-compliant strings via a whitelist. It is also recommended to avoid strings as complete as possible and to check integer values ​​for their length.

** Treatment of incorrect entries (sanitizing) **

Instead of rejecting data due to an unexpected data format or character, incorrect entries can be corrected and automatically transformed (sanitize). This should allow a user-friendly input of the data in different spellings. For further processing, the data can be cleaned of unexpected characters (for example, the telephone number * (0049) -201-12345678 * can be converted into the number-only format * 004920112345678 *).

A cleanup may consist of deleting, replacing, or masking characters (see also section Context-Sensitive Data Masking).

When sanitizing, there is a risk that changes to the data lead to new complexity, new vectors of attack or misinterpretation. Sanitizing should therefore be avoided as far as possible and should only be used in cases where abuse of sanitizing can be ruled out.
If the web application detects bad data, errors that indicate intentional manipulation (for example, a changed session ID) should not be automatically corrected, but rejected. In addition, input data that can not occur with the intended browser or client operation should always be rejected. These include, for example:

* additional or missing form parameters,
* Session cookies with unexpected characters or invalid length,
* unexpected values ​​when transferring form parameters from predefined HIDDEN, SELECT or CHECKBOX fields,
* different or unwanted transmission path of the parameters (for example, GET, POST, Cookie).
When purging the data, the nested input of attack vectors should be considered. For example, the seemingly reasonable filter * s / <script> // g; * (written here in Perl RegEx syntax) is problematic for deleting <script> tags in the input stream. However, this can be bypassed with a nested input (for example, * <sc <script> ript> *). It is therefore recursive to filter. In case of doubt, the input data should be rejected.

Basically, if the data is rejected, the requested action should also be aborted and a neutral error message should be output (see also APP.3.1.M13 * Restrictive Release of Security-Relevant Information *). For Web applications with high protection requirements, the session should also be aborted.

#### APP.3.1.M17 Error Handling [Developer]

If an error occurs during the operation of a web application, it should be treated so as to ensure a consistent state of the web application and to maintain the protection of the data. A web application is in an inconsistent state when it transitions to an unexpected state due to an error, causing data to be processed uncontrollably (for example, no error message if data is stored unsuccessfully).

The consistent state of a web application can be jeopardized by, among other things, the following events:

* the application crashes,
* a transaction is performed incompletely at the application level,
* an action is performed despite an error (for example, in case of incomplete checks by safety components),
* Services are prevented (denial of service),
* Rights are extended (privilege escalation),
* Malicious code is executed (code execution).
The following points should be considered when troubleshooting:

* ** Avoiding Confidential Information in Error Messages: ** The web application must provide the user with neutral, customized error pages in the event of an error that do not contain confidential information. See also * APP.3.1. * M13 * Restrictive release of safety-relevant information *.
* ** Error logging: ** In order to fully understand any errors that have occurred, they must be logged as an event in accordance with APP.3.1.M5 * Logging of security-relevant events by web applications *.
* ** Aborting the operation after an error occurs: ** If errors occur with web application security components (for example, during authorization or authentication), the action initiated must be aborted and access to the requested resource or function must be rejected. It must be ensured that provoked errors can not circumvent security mechanisms. For Web applications with a high protection requirement, consideration should also be given to forcibly terminating an existing session (see also APP.3.1.M3 * Secure Session Management *).
* ** Released Reserved Resources: ** On-the-fly, web applications use resources, such as network or file streams, to access background systems, cached states, or other data. As long as the web application accesses these resources, they are usually reserved for their exclusive access and can not be used by other processes. If an error occurs, previously reserved resources (for example, a file handle to a temporary file) should be released as part of the error handling. In addition, cached data must be deleted during error handling.
* ** Immediate handling of errors: ** Internal errors should be handled by the web application itself. Forwarding an unhandled error to other components (for example, application servers or downstream web services) may result in a loss of information necessary to handle the error (for example, release bound resources). Therefore, unhandled errors should not be forwarded.
* ** Avoidance of excessive fault tolerance: ** If causes of fault conditions are not fully understood, the fault should not be tolerated with regard to ease of use. In case of doubt, cancel the action. In case of serious errors should always be canceled.
The goal is to build robust and fault-tolerant Web applications that can distinguish user-directed usage from obvious abuse attempts and fatal errors, and then respond appropriately.

#### APP.3.1.M18 Control of log files

The logging of security-relevant events is only effective as a security measure if the logged data is evaluated at regular intervals by an auditor. If it is not possible in terms of personnel or technology to establish the role of an independent auditor for log files, it can also be evaluated by the administrator. In this case, it should be noted that this makes the activities of the administrator difficult to control. The result of the evaluation should therefore be submitted to the safety officer, the IT manager or another specially designated employee.

The regular check also serves the purpose of preventing the excessive deletion of the log files by the subsequent deletion of the log data. Depending on the type of log data, it may be useful to archive them on external data carriers.

Since log files contain personal data in most cases, it must be ensured that these data are used only for the purpose of data protection control, data backup or to ensure proper operation (see § 14 Abs. 4 BDSG and section * Data protection aspects during logging *). The scope of the logging and the criteria for its evaluation should be documented and agreed within the organization.

On the one hand, the minimum legal retention periods on the one hand and the maximum retention periods for log data on the other can result from various legal regulations. For example, data protection regulations may require a deletion (see also section * Data protection aspects during logging *).

For certain protocol data, however, legal minimum retention periods may apply. For example, if they provide information about business transactions. These deadlines must be met in any case. Before log data is deleted, it is therefore necessary to carefully check whether the relevant legal provisions have to be observed and what retention periods result from this. Here, the legal department should be involved.
The following evaluation criteria serve as examples that indicate indications of possible security gaps, manipulation attempts and irregularities:

* Are the times of check-in and check-out outside working hours (reference to manipulation attempts)?
* Are there incorrect attempts to log in (an indication of an attempt to guess passwords)?
* Are there any unauthorized access attempts (indication of attempts to manipulate)?
* Are there noticeably large time intervals in which no log data was recorded (reference to possibly deleted log records)?
* Is the amount of logged data too large (a large log file makes it difficult to find any irregularities)?
* Are there noticeably large time intervals in which there seems to have been no change of user (indication that users do not consistently log out after the end of work)?
* Are there noticeably long connection times in public networks?
* Has a noticeable high network load or interruption in network operation been detected in individual network segments or in the entire network (reference to attempts to prevent or impair the services of the network or to an inappropriate conception or configuration of the network)?
When analyzing the log files, special attention should be paid to all accesses made under administrator IDs.

If extensive log files are to be evaluated regularly, a tool should be used for this purpose. This tool should allow selectable evaluation criteria and highlight particularly critical entries (eg multiple failed login attempt).

** Data protection aspects during logging **

In the sense of data protection law, logging in the operation of IT systems means the creation of manual or automated records, from which the questions can be answered: "Who initiated and accessed what by what means and when?" In addition, system states must be derived: "Who had access rights from when to when?"

The nature and extent of logging depends on general data protection law and also on sector-specific regulations.

The logging of the administration activities corresponds to a system monitoring, while the logging of the user activities essentially serves the process monitoring. Accordingly, the requirements for the type and scope of system-oriented logging are mainly found in general data protection law, while procedural logging is often defined by sector-specific regulations. Examples of procedural logging are Meldegesetze, police laws, constitutional protection laws.

** Minimum logging requirements **

When administering web applications, the following activities must be fully logged:

* ** system generation and modification of system parameters **
 Since no system-controlled protocols are usually generated at this level, corresponding, more detailed, manual records are required which should correspond to the system documentation.
* ** Setting up users **
 Who from when to when who has been granted the right to use the web application in question, must be fully logged. Longer-term retention periods should be provided for these protocols since they are the basis of virtually every revision.
* ** creation of rights profiles **
 In the context of user management logging, it is particularly important to record who issued the instruction to set up specific user rights.
* ** Application and modification of application software **
 The logs represent the result of the program and process releases.
* ** Changes to the file organization **
In view of the manifold possibilities of manipulation that already arise when using the "standard file management systems", complete logging is of particular importance (see, for example, database management).
* ** Implementation of data protection measures **
 Since such measures (backup, restore) are associated with the production of copies or the overwriting of databases and are often carried out in "exceptional situations", there is an increased need for logging.
* ** Other call of administration tools **
 The use of all administration tools should be logged to determine if unauthorized persons have obtained system administrator rights.
* ** attempting unauthorized logging in and exceeding authority **
 The complete logging of all abnormalities when logging in and using components is of central importance. User in this sense is also the system administrator.
If personal data is processed, the following user activities must be completely or selectively logged depending on the protection requirements of the procedures or data:

* ** Input of data **
 Even if authority violations are otherwise logged, full logging of data entry should be considered as a rule.
* ** data transmissions **
 Only if a complete logging is not required by law, selective logging can be considered sufficient.
* ** Use of automated retrieval method **
 In general, a complete logging of the calls and the reasons of the calls (process, file number, etc.) may be required in order to uncover unauthorized knowledge within the scope of the granted access rights.
* ** Deletion of data **
 If data is deleted, this is to be logged.
* ** calling programs **
 This may be necessary for web applications that need to be protected. B. may only be used at certain times or occasions. Therefore, complete logging is indicated in these cases. The logging also serves to relieve the authorized user (proof of exclusively authorized call of the programs).
** Purpose of using protocol data **

Due to the almost identical regulations in the data protection law of the federal and state governments, protocol data is subject to a special strict purpose limitation. They may only be used for the purposes that led to their storage. These are generally the general controls defined in a security plan, the monitoring required in most data protection laws, the proper application of the data processing programs used to process personal data, and controls by internal or external data protection officers. Only in exceptional cases, the sector-specific regulations allow the use of this data for other purposes, such. For law enforcement, too.

** Storage life **

Unless domain-specific regulations provide otherwise, the retention period of the protocols is governed by the general deletion rules of the data protection laws. Log data must be deleted immediately if it is no longer necessary to achieve the purpose. If there is no compelling reason for the further holding of log files, there is a deletion obligation.

As clues can serve:

* the likelihood that irregularities may (still) become apparent and
* the ability to detect the causes of irregularities based on the logs and other documents.
Experience has shown that a period of one year should not be exceeded.
As far as protocols are prepared for the purpose of targeted controls, shorter retention periods may be considered. In general, a storage is sufficient to the actual control. Here, too, the area-specific regulations must be observed.

** Technical and organizational conditions **

The effectiveness of logging and its evaluation in the context of controls depends crucially on the technical and organizational framework conditions. Therefore the following aspects have to be considered:

* A concept should be drawn up that clearly defines the purpose of the protocols and their controls as well as safeguards for the rights of employees and other data subjects (see also OPS.1.1.6 * Logging *).
* The inevitability and thus the completeness of the protocols must be ensured as well as the tamper-proofness of the entries in log files.
* Effective access restrictions must be realized in line with the earmarking of data.
* The protocols must be designed so that they can be effectively checked. This also includes IT support for the evaluation.
* The evaluation options should be agreed in advance and determined.
* Controls should be timely so that damage can be averted and consequences can be taken if breaches are detected. Checks must take place in good time before log file deletion deadlines expire.
* Controls should be done on a four-eye basis.
* Employees should be aware that controls are in progress, if necessary unannounced.
* Automated procedures (eg * watch dogs *) should be used for routine checks.
* Personnel and works councils should be involved in the development of the logging concept and in defining the evaluation options of the protocols.
#### APP.3.1.M19 Protection against SQL injection

A number of measures have to be taken to prevent or at least aggravate SQL injections. These extend over all components of an application, from the application itself via the server to the database management system (DBMS).

** Application programming **

One of the most important measures to avoid SQL injection is the careful review and filtering of inputs and parameters by the web application. It should be checked whether the transferred data corresponds to the expected data type. If z. For example, if a numeric parameter is expected, it can be checked in PHP (PHP: Hypertext Preprocessor) with the function * is \ _numeric () *. The filtering, on the other hand, must ensure that special characters such as the quote character ('), the semicolon (;) and double hyphens (-) are ignored.

It is safer to use stored procedures or prepared SQL statements. These are offered by many database management systems (DBMS) and are originally intended to optimize more frequently occurring queries. The advantage of these parameterized statements is that parameters are no longer directly integrated into an SQL statement. Rather, they are transferred separately from the SQL statement to the database. The DBMS then combines its own statement and parameters, whereby the special characters mentioned above ** are automatically masked.

In order to provide potential attackers with no evidence of attacks, special attention should be paid to ensure that applications do not issue any external error messages that allow conclusions to be drawn about the system used or the structure of the underlying database.

** Server-side measures **

The most important security measure on the server is to harden the operating system. In order to provide as few attack points as possible, the following measures are taken for example:

* disable unnecessary services,
* delete unneeded user accounts,
* import relevant patches and
* delete all unnecessary components for the function of the server.
In addition, the use of an application-level gateway (ALG) should be considered. At the application level, ALGs can monitor the data being exchanged between the web browser and the application and prevent malicious data from reaching the server.

Another additional security measure is the use of Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS). IDS analyze the traffic transmitted over a network and detect potentially dangerous data. The analysis techniques used are divided into misuse and anomaly detection. Misuse Detection attempts to detect known attack patterns. Anomaly Detection follows the approach of learning the permissible patterns of behavior and identifying deviations from them as an attack. While an IDS is capable of detecting attacks and issuing alerts, an IPS is able to perform appropriate responses. For example, the response may be to block the connection, discard or change data.

In the case of increased security requirements, it should be checked whether the use of IDS or IPS is expedient.

** Database-side measures **

As well as the operating system, the database should also be hardened. In the case of the database, this means z. B .:

* remove unneeded stored procedures
* disable unneeded services,
* delete unneeded user accounts and default accounts and
* import relevant patches.
In this context, an account specially designed for database access should also be created, which should have as few access rights as possible.

In addition, confidential data, such as As passwords are stored in the database as far as possible only encrypted.

Many manufacturers now offer so-called vulnerability scanners, which can check both applications and databases for security vulnerabilities, such as possible SQL injections.

** Example of basic procedure for creating secure code using PHP and MySQL: **

In PHP, the function * mysql \ _real \ _escape \ _sting () prevents * special characters from being passed to a MySQL database. The function masks the special characters contained in the passed string, such as For example, quotes and thus prevents SQL injections.

Instead of the following syntax:

* $ query = "SELECT * FROM users
 WHERE username =
 ''. $ \ _ POST ['username']. '' '
 AND password =
 ''. $ \ _ POST ['password']. "'";
So this syntax should be used:

* $ query = "SELECT * FROM users
 WHERE username =
 mysql \ _real \ _escape \ _string ($ \ _ POST ['username']). '' '
 AND password =
 mysql \ _real \ _escape \ _string ($ \ _ POST ['password']). '' ";
** Example of secure code when using ASP with ADO and SQL Server: **

A prepared statement for the example above looks like this:

* $ query = "SELECT * FROM users WHERE username =?
 AND password =? "
 Set cmd = Server.CreateObject ("ADODB.Command")
 cmd.CommandText = query
 cmd.CommandType = adCmdText
 Set param = cmd.CreateParameter ("", adVarChar, adParamInput,
 nMaxUsernameLength, strUsername)
 cmd.Parameters.Append
 Set param = cmd.CreateParameter ("", adVarChar, adParamInput,
 nMaxUsernameLength, strPassword)
 cmd.Parameters.Append
 Set rs = cmd.Execute ()
It should be noted that the above code examples are only intended to illustrate the basic approach to avoid SQL injection.

### 2.3 Measures for increased protection requirements
The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### APP.3.1.M20 Use of Web Application Firewalls (CIA)

For filtering data at higher protocol levels, Web Application Firewalls (WAF) can be used. Since a WAF analyzes the HTTP protocol and the data transmitted over it, application-level attack patterns can already be filtered on the WAF. In this way, attempts to attack are detected early and no longer forwarded to the web application.

The filtering on the WAF can usually be done in two ways.

* Data sent to a web application is examined for known attack patterns. The attack patterns are provided by the manufacturer of the WAF and include both typical strings used in general attacks against web applications (eg SQL injection) and specific attack patterns that affect standard software products. In order for known attacks to be reliably detected, the attack signatures must be updated regularly, similar to a virus scanner.
* If no standard software is used or additional protection is to be achieved, customary filter rules can also be created for WAF. For example, it defines which input data will be allowed for the web application. This method requires a lot of configuration and knowledge of the data processed by the web application.
#### APP.3.1.M21 Prevention of Clickjacking [Developer] (CI)

To avoid clickjacking attacks, the following countermeasures should be implemented:

* Embedded code (eg JavaScript) in the web pages should check on the client and make sure that the contents of the web application are displayed at the top level of the browser window. This is to ensure that no other levels above the original content of the website can be stored. If this is not possible, then the display of the web application should be prevented (see script for avoiding clickjacking in tools for the module Web application [GSSID]).
* When web pages are delivered by the web application, the * X-FRAME-OPTIONS * directive should also be set in the HTTP response headers. * X-FRAME-OPTIONS DENY * prevents contents of the web page from being displayed in a frame. Alternatively, this restriction can be limited to pages that are not from the same domain (* X-FRAME-OPTIONS SAMEORIGIN *).
#### APP.3.1.M22 Performing Penetration Tests (CIA)

Penetration testing is proven and appropriate to determine the current security of IT systems and IT applications.

The BSI uses two test methods, IS penetration tests and IS Webchecks. The IS Penetration Test is the procedure for investigating the current security level of IT systems and networks. An IS web check is used to determine the current security level of the website or web services of an institution.

Penetration tests serve to assess the chances of success of a deliberate attack on an information network, a single IT system or a website and to derive the necessary additional security measures or to check whether the already implemented security measures are effective. For safety-critical networks and systems, penetration tests should be carried out regularly.

In detail, the installed applications (web application, mail server, web service) or the underlying carrier systems (operating system, database, etc.) are checked.
Typical starting points for a penetration test are:

* Network coupling elements (routers, switches, gateways),
* Security gateway (packet filter, intrusion detection system, virus scanner),
* Server (database server, web server, file server, storage systems),
* Telecommunications equipment,
* Web applications (for example web presence, transaction processing, webshop),
* Web services (for example REST interface, SOAP API, SOA),
* Clients,
* wireless networks (for example, WLAN, Bluetooth) and
* Infrastructure facilities (access control mechanisms).
Usually, penetration tests are divided into black box tests and whitebox tests. In a black box test, only the address information of the target is available to the penetration testers; further information is not provided to them. By means of the procedure "black box test" the attack of a typical outsider with incomplete knowledge about the target system should be simulated. On the other hand, the penetration testers in a Whitebox test have extensive, helpful information about the systems to be tested. This includes, for example, information about IP addresses, the internal network, the software and hardware used. These details will be communicated to you in advance by the client.

However, it is questionable whether the distinction between the procedures "black box test" and "Whitebox test" still makes sense today. For example, in a black box test due to lack of information there is a higher, entirely avoidable risk of causing unintentional damage. Furthermore, vulnerabilities due to undisclosed information could be overlooked.

In addition, there is a risk that the attack of an informed interior detective will not be taken into account during a black box test.

Penetration testers should nowadays be provided with all the information necessary for the test to be performed on the systems under test in order to be able to minimize any risks associated with the test and to enable as complete a vulnerability search as possible.

The classification of penetration tests in a largely automated vulnerability scan ("Vulnerability Scan") and a largely manual security audit therefore seems more practical and success-oriented according to current knowledge.

** Personnel and technical requirements for a penetration tester **

Penetration tests are demanding and difficult tasks that can also affect the ongoing IT operation. Therefore, only adequately qualified and reliable staff with cross-cutting knowledge should be employed in the following areas:

* Administration of operating systems and applications
* Network protocols and evaluation of network traffic
* Security products (for example, security gateways, intrusion detection systems)
* Programming languages
* Vulnerability scanner
* Audit and administration software
If external service providers are commissioned to carry out penetration tests, care should be taken to select a qualified and trusted service provider who can provide suitably qualified and reliable staff.

Furthermore, suppliers of penetration tests should be able to present to the client a structured methodology for their implementation on the basis of which the respective individual procedure can be worked out.

** Structuring and Procedure for a Penetration Test **

In a preparatory phase, the objectives and the scope of the penetration test must first be defined as precisely as possible between the client and the contractor. The penetration tester should present to the client a structured procedure that is to be agreed between the parties.
During the voting process, it should be noted that, under certain circumstances, third parties may need to be informed or involved in the planned penetration test.

In general, for example, the staff representation and the data protection officer, often external, such as the Internet service provider or web host, must be included in the project.

Certain conditions should be agreed in advance between the client and the service provider. These include in particular:

* Agreements on the confidentiality obligations
* Agreements on the use of hardware and software
* Agreements on the IT systems and IT applications to be tested
* Determination of permitted and unauthorized activities of penetration testers in order to avoid damage as far as possible
* Agreements on handling media before, during and after the completion of the penetration test, as the media may contain, for example, sensitive information about the test results
* Determination of the place of execution and evaluation and reporting for the penetration test
* Determination of a schedule including maintenance windows for the execution of the tests
* Detailed agreements on access to the Internet or the connection of test systems to the Internet during the implementation and evaluation of penetration tests
* Agreements on responsibilities and accessibility of contact persons as well as emergency preparedness
In the subsequent information phase, the penetration testers collect as much information as possible about the object to be tested. In preparation for the tests, the information obtained is then evaluated for potential vulnerabilities.

In the actual testing phase of a penetration test, if possible, the test procedures should be avoided, which could lead to a destructive result for the examined IT systems or IT applications.

For example, Denial of Service (DoS) attacks are designed to prevent access to individual services, systems, or network segments. Determining whether such attacks are possible, however, can often be clarified in advance by a system analysis, so that such attacks during a penetration test are superfluous.

Nevertheless, if DoS attacks or similar destructive attacks are to be conducted as part of a penetration test, this should be done outside the system's productive lifetime. Eventually, such an attack can also be simulated using a test system. These procedures should be expressly agreed.

Only then are active attempts to penetrate. The agreed maintenance windows and the schedule must be strictly adhered to. If changes to the time schedule are required, this must be agreed with the client in any case.

Otherwise, there is an increased risk that on the side of the client certain activities of the penetration tester are confused with real attacks. We recommend the complete recording and documentation of the penetration test.

In order to obtain as meaningful results as possible, it should be ensured that the penetration tests are carried out directly on the IT system to be tested and bypassing upstream components such as packet filters, Web Application Firewall. If there are special reasons to carry out the test with active upstream safety components, it should be noted that any safety problems in the application itself remain undetected because the upstream components intercept the attack attempts in the penetration test. However, such undiscovered vulnerabilities pose a relevant risk, as a modified attack can often override the protection systems and exploit the vulnerabilities.
** Typical Attack Techniques **

Network and port scanning: Network and port scanning are used to locate the IT systems active in a network and to identify the services (ports) offered there.

On the part of the IT administration, such queries are used to query the current status of the IT systems used. However, an attacker might use this information to identify vulnerabilities on each IT system and attack them based on that information.

* Improper input validation: Input validation is the process by which the user input (data) passed to an application for further processing is filtered, cleaned, or rejected in advance. This filtering is designed to prevent the application from passing malicious code whose processing leads to misconduct, such as the disclosure of confidential information.
* Attack methods that can cause such misconduct include: Cross-Site Scripting (XSS), Cross-Site Request Forgery (XSRF), Injection, OS Injection, Fuzzing *.
* Partly exploit vulnerabilities of the protocols and other techniques used to cause damage, for example by attacks on outdated SSL / TLS versions.
* Denial of Service (DoS) Attacks: These attacks are designed to disable one or more of the services provided. Among other things, this can be done by means of a load increased by increased inquiries, by a massively increased data volume (for example e-mails), but also by targeted exploitation of possible software errors. A well-known example of a DoS attack is the * Ping of Death *.
* Information Gathering: * Gathering * is the collection of all information that could be useful for an attack. Examples of such information include the numbering scheme used for directories or servers, as well as insights into web service interfaces gained through WSDL scanning.
* Social engineering: * Social engineering *, for example, calls fake calls or other contact with people who operate the IT system considered. The goal is usually to get confidential information, such as passwords.
* Password attacks: Here, the security or strength of passwords is tested by means of so-called dictionary attacks, brute force attacks or by decryption attempts.
* Exploiting Software Vulnerabilities: These attacks test, for example, whether the installed software is vulnerable to certain exploits, is configured incorrectly, has vulnerabilities, or is outdated. Frequently it is also examined whether known weaknesses of the standard installation of the respective product can be exploited in the present case.
* Cryptographic attacks: For example, the strength and implementation of the encryption mechanisms and protocols used, as well as key management, are examined.
* Infrastructure investigations: As part of infrastructure investigations, structural safety measures, access and closure facilities, as well as the disposal of materials, are examined. A variant of this is the so-called * Dumpster Diving *, here attackers are looking for useful documents or data carriers in the waste (for example, waste baskets, waste containers).
In the evaluation and reporting phase, the results are collected, evaluated and compiled in the form of a report. All information gained during the penetration test must be stored accordingly. The client should oblige the contractor in advance to hand over or destroy all records of the penetration test in full to the client.

The report must list the vulnerabilities found and also contain action recommendations on how to deal with the vulnerabilities discovered. It is also advisable to draw up an implementation plan for the recommended measures included in the report, including a prioritization. For management, the final report should also include a summary detailing the key audit findings and a review of the recommended course of action. The final report must be presented to the ISB and the responsible executives.

Accompanying all phases of a penetration test, a joint documentation of the individual agreements and results by the client and the contractor is recommended.

#### APP.3.1.M23 Prevention of Cross-Site Request Forgery [Developer] (CI)

In a cross-site request forgery (CSRF) attack, a user is given a command for a web application (eg, in the form of a link in a guest book) by an attacker. If he follows this link, the command will be sent to the web application and executed in the context of that user. If the user is logged on to the web application, their trust against the web application is exploited and the command is executed with the user's rights.

To make such attacks more difficult, the web application should support security mechanisms that make it possible to distinguish intended user page views from unintentionally redirected third-party commands. The following security measures are designed to prevent critical actions from CSRF attacks from being inadvertently executed.

** Use of an additional token **

In a CSRF attack, a valid HTTP request must be readjusted and sent to the victim. Such an HTTP request can z. For example, a URL may be mapped to the web application (eg, * http: //webapp.tld/addUser? Name = user *). For this, the attacker has the required request parameters, such. GET and POST variables, for the call. These parameters are generally easy to determine.

As a safeguard against a CSRF attack, a secret token can be introduced which an attacker can hardly guess. Each time the web application views the page, that token is passed as a parameter in URLs or as a hidden field on forms (double submit cookies). For each client request, the web application checks whether the transmitted token matches the value stored for the session. If an error occurs, the requested call is rejected. Without knowledge of this token an attacker can not adjust a valid HTTP request.

Although the session ID is confidential and therefore could be used as a token to protect against CSRF attacks, preferably a separate token should be generated. The token should have similar requirements that are also applied to the session ID.

If a CSRF protection is implemented, it is recommended to use the function from already used frameworks, if they offer a corresponding implementation.

For high-security web applications, consider creating the token for each request so that each time the web application is called, a new token is sent to the client, which must then be used in the subsequent request.
Before critical actions are performed (for example, state-changing requests such as a password change), the user should be re-authenticated by the web application. As a result, these functions can not be performed unnoticed, but an interaction with the user is required. Web applications with a high protection requirement should use an authentication method with multiple authentication factors (eg TAN, chip card).

Alternatively, when critical actions are invoked, the user may be redirected to a page that requires user interaction before the action is executed (eg, entering a random string). Only after the user has performed the interaction (eg, entered correct string) will it be redirected and the original request will be processed. Instead of the string, other mechanisms may be used that require user interaction (eg CAPTCHAs or puzzles, see also APP.3.1.M23 * Preventing Blocking of Resources (DoS) in Web Applications *).

The referrer field in the HTTP request (the URL of the web page from which the user came to the current page) can be used as another security feature. A Web application user's request is often valid only if the referrer field contains a URL of their own web application. So it can be assumed that the request was generated by clicking on a link of the web application.

It should be noted that the referrer field can be deactivated or filtered (eg for reasons of data protection) and therefore the measure can not be implemented for all web applications.

** Bypassing of protection mechanisms **

Security mechanisms to protect against CSRF attacks based on the referrer field or additional tokens (see section * Using an Additional Token *) can be bypassed through cross-site scripting attacks. Correct filtering of user data (see APP.3.1.M15 * Comprehensive Input and Output Validation *) is therefore critical to the effectiveness of CSRF security measures.

#### APP.3.1.M24 Preventing Blockage of Resources [Developer] (A)

Web applications often offer resource-intensive features that trigger complex database queries or data submissions, for example. If these compute-intensive operations are deliberately called up frequently or the web applications are flooded with inquiries, resources can be overcommitted and the operation can be restricted to unavailability. This procedure is known as Denial of Service (DoS) attack.

In most cases, DoS attacks are based on both brute-force and enumeration attacks on automation (see APP.3.1.M7 * Protection against unauthorized automated use of web applications *). Therefore, similar protections should be implemented to prevent DoS attacks. These include, for example, the following measures:

* Set limits (for example, the temporary blocking of a resource or the user account after repeated mishaps),
* artificially delay the time between request and processing by the web application (for example, in case of repeated unsuccessful login),
* temporarily disable the calling IP address if an attack is suspected,
* Use CAPTCHAs,
* Verify inputs to input fields before initiating compute-intensive operations,
* Use XML filtering mechanisms and XML validation checks.
In addition, the following examples provide pointers to specific safeguards to complicate web application denial-of-service attacks:
* Resource intensive operations are especially vulnerable to DoS attacks. Therefore, the resource usage per user can be limited to a maximum. In addition, certain operations can only be made available to logged-in users (for example, complex database calls).
* Only one request should be processed per user at the same time. Multiple requests from the same user should be processed sequentially.
* The load of DoS requests can be reduced in part by buffering ("caching") the web page views. Thus, the requested, computationally intensive operation is not executed on each call, but only the cached result is returned. Highly resource-intensive inquiries can be precalculated even in low-load periods (pre-aggregation).
* The web application's architecture and flow control should be designed to avoid compute-intensive operations (for example, resource-intensive operations should be avoided when creating session IDs or other cryptographic mechanisms). Load tests can be performed to detect compute-intensive operations.
* An overflow of memory space, for example during logging, can lead to write accesses to the data carrier being no longer possible. Storage operations performed by the web application can jeopardize operations. Therefore, access to data storage should be limited and the capacity of data storage should be checked regularly. Similarly, the consumption of random access memory (RAM) per thread should also be limited.
* SOAP messages must be validated according to the appropriate XML schema. If the validation is unsuccessful, for example because it contains an undefined number of elements, the SOAP message must not be further processed, as otherwise this can lead to problems with the processing by the XML parser.
* Similarly, web applications should be protected from SOAP flooding attacks. These are comparable to conventional flooding attacks (eg SYN flooding) and can therefore be fought with similar protective measures. For example, an intrusion detection system can detect and block messages that are sent repeatedly, for example by blocking messages. By using heuristics.
In the case of web applications where targeted, for example politically motivated DoS attacks from the Internet can be expected due to their nature, cooperation with a service provider specializing in the prevention of DoS attacks may be useful. Such service providers direct the IP traffic in the event of an attack via their own systems, which filter access and / or relieve the target systems by other measures, such as caching. It is important to consider in advance whether the diversion of the data streams via the systems of third parties will result in additional hazards or requirements. For example, a popular attack method for cached Web pages is that the attacker calls non-existent subpages. If the service provider does not intercept this and forwards the request for the supposedly new subpage to the original page, an inadvertent DoS attack of the service provider occurs. Such new attack vectors must be addressed in the selection of the anti-DoS service provider.

3 Further information
------------------------------

### 3.1 Worth knowing
Web tracking refers to the evaluation of user data, eg. To track the activities of users of a website. On the basis of these evaluations, user-tailored advertising can be displayed, for example, or the popularity of articles can be measured by means of statistics and the web presence can then be optimized. For this purpose, personal information, such as the user's location, the status of a transaction (eg transaction completion on a purchasing platform) and retrieval statistics via web pages, can be logged and used.

If external service providers are commissioned to evaluate this user data, it should be noted that these service providers may be able to correlate user data with the data of other customers and web applications. On this basis, detailed user profiles can be created across applications.

Possible techniques for collecting user data are for. B.

* (persistent) cookies,
Web bugs (pixel-sized image elements),

* Browser fingerprints (eg attributes such as installed plugins, screen resolution, time zone, user agent, HTTP headers),
* Logging the IP address.
The techniques can also be combined to more reliably identify users.

If user data, in particular personal data, are to be evaluated, the legal basis must be examined.

### 3.2 Literature

Further information about threats and security measures in the area of ​​"web applications" can be found in the following publications, among others:

* #### [BSICC] Common Criteria for Testing and Assessing the Security of Information Technology (Common Criteria)

  

 BSI, (last accessed on 05.10.2017)
 <Https://www.bsi.bund.de/DE/Themen/ZertifizierungundAnerkennung/Produktzertifizierung/ZertifizierungnachCC/ITSicherheitskriterien/CommonCriteria/cc.html>

 
* #### [GSKHM] Tools for using the IT-Grundschutz catalogs

  

 BSI, (last accessed on 05.10.2017)
 [https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Hilfsmittel/Bausteine/bausteine\_node.html](https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ ITGrundschutzKataloge / resources / blocks / bausteine_node.html)

 
* #### [OWASP] Open Web Application Security Project

  

 OWASP, (last accessed on 28.09.2017)
 <Https://www.owasp.org>

 
* #### [TR21022] BSI Technical Guideline, Cryptographic Procedures

  

 Use of Transport Layer Security (TLS), Federal Office for Information Security (BSI), 2017
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)
