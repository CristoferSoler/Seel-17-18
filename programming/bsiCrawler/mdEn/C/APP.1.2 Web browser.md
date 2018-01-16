Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Web browsers are application programs that retrieve, process, display, output and store (hypertext) documents, images, video, audio and other data formats from the Internet on local IT systems. Similarly, web browsers can also transfer data to the Internet. Stationary and mobile client systems are unimaginable today without a web browser, because many private and business applications use appropriate content.

At the same time, these contents are becoming ever more diverse on the internet. Fewer and fewer websites can do without embedded videos, animated elements, and other active content. Modern web browsers also cover a wide range of additional features by incorporating plug-ins and external libraries. There are also extensions for certain functions, data formats and content. The complexity of modern web browsers offers a high potential for serious conceptual errors and program weaknesses. Not only does it increase the potential threat of attacks from the Internet, it also poses additional risks due to programming and operating errors.

The consequences for the confidentiality and integrity of data are significant. Similarly, the availability of the entire IT system is threatened by such vulnerabilities. As a result, Internet content must, as a rule, be regarded as untrustworthy from the point of view of the Web browser.

### 1.2 Objective

This module describes security requirements for web browsers that are used on client systems, ie on stationary and mobile computers as well as partly also on tablets and smartphones. Both centrally managed and individual operating environments are considered.

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

Vulnerability lists and so-called exploit kits greatly facilitate the development of individual malware. Cyber ​​attacks can be automated to easily use drive-by downloads or other distribution channels without expert knowledge. Attackers can exploit known Web browser vulnerabilities or any associated resource or extension to prepare for follow-up attacks or to download and install malicious code on the client.

### 2 3 Reading the Internet communication

The basic security of communication on the Internet depends very much on the authentication method used and the encryption of the data in transit. The necessary procedures are often poorly implemented.

Weak implementations of the necessary procedures are widespread and prevent effective authentication and encryption. Many web services still use outdated encryption techniques. Thus, an attacker can undermine the authentication of servers or the communication or data is not encrypted effectively. This information can be read or changed on the transmission path. In the past, CAs were also compromised, allowing attackers to obtain certificates for third-party sites.

### 2 4 Loss of integrity in web browsers

If browsers, plug-ins or extensions are taken from untrustworthy sources, malicious functions can be carried out unintentionally and unnoticed. For example, attackers can spoof components such as toolbars on web browsers to trick users into manipulated copies of web pages that cause phishing attacks. Malicious extensions can manipulate the content of the websites in question or spy on data and send it to the attacker.

### 2 5 Loss of privacy

If browsers are configured insecure, trusted data can be made available to unauthorized third parties at random or maliciously. Also passwords can be passed on unintentionally. If cookies, passwords, histories, input data and search queries are stored or unnecessary extensions are activated, data from third parties or malicious programs can be more easily misused.

### 2 6 Error during administration and operation

Errors in the administration of the web browser can lead to unsafe configuration and unsafe operation. An essential threat potential arises in the lack of timeliness and maintenance of the web browser used. In addition, browser manufacturers often do not provide security updates in a timely manner. This significantly increases the spread of exploitable vulnerabilities.

3 requirements
---------------
The following are the specific requirements for Web browsers. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer should always be involved in strategic decisions. In addition, the Information Security Officer is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.
