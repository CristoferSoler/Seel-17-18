1 description
--------------

### 1.1 Introduction

Web browsers are application programs that retrieve, process, display, output and store (hypertext) documents, images, video, audio and other data formats from the Internet on local IT systems. Similarly, web browsers can also transfer data to the Internet. Stationary and mobile client systems are unimaginable today without a web browser, because many private and business applications use appropriate content.

At the same time, these contents are becoming ever more diverse on the internet. Fewer and fewer websites can do without embedded videos, animated elements, and other active content. Modern web browsers also cover a wide range of additional features by incorporating plug-ins and external libraries. There are also extensions for certain functions, data formats and content. The complexity of modern web browsers offers a high potential for serious conceptual errors and program weaknesses. Not only does it increase the potential threat of attacks from the Internet, it also poses additional risks due to programming and operating errors.

The consequences for the confidentiality and integrity of data are significant. Similarly, the availability of the entire IT system is threatened by such vulnerabilities. As a result, Internet content must, as a rule, be regarded as untrustworthy from the point of view of the Web browser.

### 1.2 Objective

This module describes security requirements for web browsers that are used on client systems, ie on stationary and mobile computers as well as partially on tablets and smartphones. Both centrally managed and individual operating environments are considered.

### 1.3 Delimitation

This module contains basic security requirements that must be observed and complied with when installing and operating web browsers for accessing data from the Internet. Browsers for access to all-local or data in internal data networks without Internet access are not covered in this module.

Web browsers are closely interlinked with the operating system of the client system and access the interfaces and functions provided there. In order to secure the operating systems, therefore, the requirements of the building blocks of the layers SYS.2.2 * desktop systems * and SYS.3.2 * tablet and smartphone * should be met.

Many plug-ins, such as Java, run through the Web browser instances and typically run in separate execution environments. Requirements for this can be found in the block SYS.2.7 * Internet-PC *.

Web applications used by browsers as well as responsible servers are handled in the blocks APP.3.1 * Web applications * and APP.3.2 * Web server *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​Web browsers:

### 2 1 Execution of malicious code by web browser

Web browsers can load data from untrusted or potentially compromised sources. Such data may contain executable code with malicious code that can exploit vulnerabilities and infect the user's device without his knowledge and thus unnoticed.
This can be code that can be directly executed by the web browser, such as JavaScript. Likewise, it may also be executable code of a plug-in or an extension in the context of the browser, such as Adobe Flash, Java or components of PDF documents. Finally, it can also be code that is loaded from the Web browser to the client and executed outside of the browser process. In many cases, additional malicious software will be reloaded by the malicious code, which will then be executed on the client with the rights of the user. Failure to adequately address the basic protections of modern web browsers threatens the confidentiality, integrity, or availability of information or services of the client or the potentially connected networks.

### 2 2 Exploit Kits

Vulnerability lists and so-called exploit kits greatly facilitate the development of individual malware. Cyber ​​attacks can be automated to easily use drive-by downloads or other distribution channels without expert knowledge. Attackers can exploit known web browser vulnerabilities or any associated resource or extension to prepare for follow-up attacks or to download and install malicious code on the client.

### 2 3 Reading the Internet communication

The basic security of communication on the Internet depends very much on the authentication method used and the encryption of the data in transit. The necessary procedures are often poorly implemented.

Weak implementations of the necessary procedures are widespread and prevent effective authentication and encryption. Many web services still use outdated encryption techniques. Thus, an attacker can undermine the authentication of servers or the communication or the data is not encrypted effectively. This information can be read or changed on the transmission path. In the past, CAs were also compromised, allowing attackers to obtain certificates for third-party sites.

### 2 4 Loss of integrity in web browsers

If browsers, plug-ins or extensions are taken from untrusted sources, malicious functions can be carried out unintentionally and unnoticed. For example, attackers can spoof components such as toolbars on web browsers to trick users into manipulated copies of web pages that cause phishing attacks. Malicious extensions can manipulate the content of the websites in question or spy on data and send it to the attacker.

### 2 5 Loss of privacy

If browsers are configured insecure, trusted data can be made available to unauthorized third parties at random or maliciously. Also passwords can be passed on unintentionally. If cookies, passwords, histories, input data and search queries are stored or unnecessary extensions are activated, data from third parties or malicious programs can be more easily misused.

### 2 6 Error during administration and operation

Errors in the administration of the web browser can lead to unsafe configuration and unsafe operation. An essential threat potential arises in the lack of timeliness and maintenance of the web browser used. In addition, browser manufacturers often do not provide security updates in a timely manner. This significantly increases the spread of exploitable vulnerabilities.

3 requirements
---------------
The following are the specific requirements for Web browsers. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer should always be involved in strategic decisions. In addition, the Information Security Officer is responsible for ensuring that all requirements are met and verified in accordance with the security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### APP.1.2.A1 Using sandboxing

The web browser MUST use to ensure that each instance and each processing process can only access its own resources (sandboxing). Web pages MUST be isolated as stand-alone processes or at least as separate threads. Plug-ins and extensions MUST also run in isolated areas. The web browser used SHOULD implement the content security policy according to the W3C specifications.

#### APP.1.2.A2 Encryption of communication

The web browser MUST support Transport Layer Security (TLS) in a secure version. Unsafe versions of TLS version SHOULD be disabled. The web browser MUST support the HTTP Strict Transport Security (HSTS) security mechanism as per RFC 6797. For all major public TLS encrypted web services, the domains SHOULD be inserted in the HSTS preload list of the browser.

#### APP.1.2.A3 Use of certificates [user]

The web browser MUST provide a list of trusted root certificate issuers and accept the certificates provided by the institution itself. The web browser MUST support extended validation certificates. Root certificates MAY only be added, changed, or deleted with administrative rights. Certificates MUST be revoked by the web browser (locally).

The web browser MUST fully validate the validity of server certificates using the public key and the validity period. The revocation status of the server certificates MUST be checked by the web browser. The certificate chain including the root certificate MUST be verified.

The web browser MUST clearly and clearly show the user whether the communication is in plain text or encrypted. The web browser SHOULD enable the user to view the server certificate used on request. The web browser MUST signal the user if any certificates are missing, invalid, or revoked. The encrypted connection may in such a case be made ONLY after express confirmation by the user.

#### APP.1.2.A4 Version check and update of the web browser

The web browser MUST have a mechanism that can reliably detect and display its own version as well as those of all loaded or enabled extensions and plug-ins.

Updates for the web browser, plug-ins and extensions MUST be installed immediately. The web browser should be able to import updates automatically. If no update is available for a known critical vulnerability, measures for mitigation MUST be taken in a timely manner.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state of the art in the field of web browsers. They SHOULD be implemented in principle.

#### APP.1.2.A5 basic configuration

The browser SHOULD be able to be centrally configured. Central settings may NOT be changed by users. The web browser SHOULD NOT run permanently with extended privileges.

#### APP.1.2.A6 Password Management in Web Browser [User]
When a password manager is used in the browser, it SHOULD establish a direct and unique relationship between the web page and the password stored therefor. The password store SHOULD be protected. The passwords stored in the password manager SHOULD only be accessible after entering a master password. Authentication for password protected access SHOULD only be valid for the current session. The password manager SHOULD set the quality of the passwords according to the security policy of the institution. The stored passwords SHOULD be erasable by the user.

#### APP.1.2.A7 Protection of data [user]

Third party cookies SHOULD BE REJECTED. Saved cookies SHOULD be erasable by the user.

The autocomplete feature SHOULD be disabled. If the function is used, the user should be able to delete the completion data. The user SHOULD also be able to delete the history data of the browser.

If available, a synchronization of the browser with cloud services should be disabled. Telemetry functions as well as the automatic transmission of crash reports to the manufacturer SHOULD be deactivated as far as possible.

If peripherals such as microphone or webcam are connected, they SHOULD be disabled in the browser. The browser SHOULD provide a way to configure or disable WebRTC, HSTS, and JavaScript.

#### APP.1.2.A8 Using plug-ins and extensions [User]

It SHOULD only essential plug-ins and extensions are installed. Plug-ins and extensions for the browser SHOULD only be installed with administration rights. The execution of plug-ins SHOULD always be confirmed by the user. The browser SHOULD provide the ability to configure and disable extensions.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### APP.1.2.A9 Use of an isolated browser environment

With increased protection needs, web browsers should be deployed running in an isolated environment (such as ReCoBS) or on dedicated IT systems.

#### APP.1.2.A10 Using private mode [user]

The browser SHOULD be executed in the so-called private mode with increased confidentiality requirements, so that no information or content is stored persistently on the user's IT system. The browser SHOULD be configured to delete local content on exit.

#### APP.1.2.A11 Check for harmful content

Called Internet addresses SHOULD be checked by the browser for potentially harmful content. The browser SHOULD alert the user appropriately if there is information about malicious content. A connection classified as malicious should NOT be able to be called. The verification procedure used must NOT violate any privacy or privacy policy.

#### APP.1.2.A12 two-browser strategy

In the event of unresolved security problems with the web browser used, an alternative browser from another manufacturer SHOULD be installed to serve as an alternative.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the "Web Browser" area can be found in the following publications, among others:
* #### [AbWeB] Hedging options when using web browsers

  

 Federal Office for Security in Information Technology, Version 1.0, 2013
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_047.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_047.pdf)

 
* #### [ACSDB] SSL Cipher Suite Details of Your Browser

  

 Active Cipher Suites Detais of the Browser, Check Options, (last accessed on 28.09.2017)
 <Https://cc.dcsec.uni-hannover.de/>

 
* #### [CSP] Content Security Polic W3C

  

 W3, Version 1.0, 2012
 <Https://www.w3.org/TR/2012/CR-CSP-20121115/>

 
* #### [HSTS] HTTP Strict Security Policy (HSTS), RFC 6797

  

 IETF, 2012
 <Https://tools.ietf.org/html/rfc6797>

 
* #### [MDST8SSL] Minimum standard of the BSI according to § 8 paragraph 1 sentence 1 BSIG for the use of the SSL / TLS protocol in the federal administration

  

 Federal Office for Information Security, Version 1.0, 2015
 [Https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard\_BSI\_TLS\_1\_2\_Version\_1\_0.pdf](https://www.bsi. bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard_BSI_TLS_1_2_Version_1_0.pdf)

 
* #### [MDST8Web] Minimum standard of the BSI according to § 8 paragraph 1 sentence 1 BSIG for the secure use of web browsers in the federal administration

  

 Federal Office for Information Security, Version 1.0, 2017
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard\_Sichere\_Web-Browser.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/ DE / BSI / minimum standards / Mindeststandard_Sichere_Web-Browser.pdf)

 
* #### [OWASPList] OWASP List of the 10 Most Critical Web Application Security Risks

  

 OWASP, (last accessed on 28.09.2017)
 [Https://www.owasp.org/index.php/Category:OWASP\_Top\_Ten\_Project](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)

 
* #### [ReCoBS] Common Criteria Protection Profile for Remote Controlled Browsers System (ReCoBS)

  

 BSI, BSI-PP-0040; Version 1.0, 2008
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/recobslanginfo\_pdf.pdf?\_blob=publicationBundesamt](https://www.bsi.bund.de/SharedDocs/Downloads /DE/BSI/Internetsicherheit/recobslanginfo_pdf.pdf?_blob=publicationBundesamt)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Web Browser" building block.

* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.28 Software vulnerabilities or errors
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
* G 0.14 Spying out information (spying)
  * APP.1.2.A2 Encryption of communication
  * APP.1.2.A3 Use of certificates [user]
  * APP.1.2.A7 Protection of data [user]
  * APP.1.2.A10 Using private mode [user]
* G 0.15 Listening
  * APP.1.2.A7 Protection of data [user]
* G 0.18 Missing planning or missing adjustment
  * APP.1.2.A2 Encryption of communication
  * APP.1.2.A3 Use of certificates [user]
  * APP.1.2.A5 basic configuration
  * APP.1.2.A6 Password Management in Web Browser [User]
  * APP.1.2.A8 Using plug-ins and extensions [User]
  * APP.1.2.A12 two-browser strategy
* G 0.19 Disclosure of information worthy of protection
  * APP.1.2.A1 Using sandboxing
  * APP.1.2.A10 Using private mode [user]
  * APP.1.2.A11 Check for harmful content
  * APP.1.2.A12 two-browser strategy
  * APP.1.2.A2 Encryption of communication
  * APP.1.2.A6 Password Management in Web Browser [User]
  * APP.1.2.A7 Protection of data [user]
  * APP.1.2.A10 Using private mode [user]
* G 0.20 Information or products from unreliable sources
  * APP.1.2.A3 Use of certificates [user]
  * APP.1.2.A4 Version check and update of the web browser
* G 0.21 Manipulation of hardware or software
  * APP.1.2.A4 Version check and update of the web browser
  * APP.1.2.A5 basic configuration
* G 0.22 Manipulation of information
  * APP.1.2.A2 Encryption of communication
  * APP.1.2.A3 Use of certificates [user]
  * APP.1.2.A8 Using plug-ins and extensions [User]
* G 0.23 Unauthorized intrusion into IT systems
  * APP.1.2.A1 Using sandboxing
  * APP.1.2.A10 Using private mode [user]
  * APP.1.2.A11 Check for harmful content
  * APP.1.2.A12 two-browser strategy
  * APP.1.2.A4 Version check and update of the web browser
  * APP.1.2.A9 Use of an isolated browser environment
  * APP.1.2.A11 Check for harmful content
* G 0.25 Failure of devices or systems
  * APP.1.2.A12 two-browser strategy
* G 0.26 Malfunction of equipment or systems
  * APP.1.2.A4 Version check and update of the web browser
  * APP.1.2.A9 Use of an isolated browser environment
  * APP.1.2.A12 two-browser strategy
* G 0.28 Software vulnerabilities or errors
  * APP.1.2.A1 Using sandboxing
  * APP.1.2.A10 Using private mode [user]
  * APP.1.2.A11 Check for harmful content
  * APP.1.2.A12 two-browser strategy
  * APP.1.2.A4 Version check and update of the web browser
  * APP.1.2.A8 Using plug-ins and extensions [User]
  * APP.1.2.A9 Use of an isolated browser environment
  * APP.1.2.A11 Check for harmful content
  * APP.1.2.A12 two-browser strategy
* G 0.30 Unauthorized use or administration of devices and systems
  * APP.1.2.A5 basic configuration
  * APP.1.2.A6 Password Management in Web Browser [User]
  * APP.1.2.A7 Protection of data [user]
  * APP.1.2.A8 Using plug-ins and extensions [User]
* G 0.31 Incorrect use or administration of devices and systems
  * APP.1.2.A5 basic configuration
  * APP.1.2.A6 Password Management in Web Browser [User]
  * APP.1.2.A7 Protection of data [user]
  * APP.1.2.A8 Using plug-ins and extensions [User]
* G 0.39 Malware
  * APP.1.2.A1 Using sandboxing
  * APP.1.2.A10 Using private mode [user]
  * APP.1.2.A11 Check for harmful content
  * APP.1.2.A12 two-browser strategy
  * APP.1.2.A4 Version check and update of the web browser
  * APP.1.2.A9 Use of an isolated browser environment
* G 0.40 Denial of Service
  * APP.1.2.A12 two-browser strategy
* G 0.45 data loss
  * APP.1.2.A7 Protection of data [user]
* G 0.46 Loss of integrity of sensitive information
  * APP.1.2.A2 Encryption of communication
  * APP.1.2.A3 Use of certificates [user]
