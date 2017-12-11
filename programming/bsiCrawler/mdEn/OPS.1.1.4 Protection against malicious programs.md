1 description
--------------

### 1.1 Introduction

Malicious programs are programs that typically perform malicious functions on the IT system without the knowledge and consent of the user or owner of an IT system. These capabilities can cover a wide range, from espionage to ransomware, to the sabotage and destruction of information or even devices.

Malicious programs can generally occur on all operating systems and IT systems. In addition to classic IT systems such as clients and servers, these also include mobile devices such as smartphones. Network components such as routers, industrial control systems and even IoT devices, such as networked cameras, are also frequently endangered by malicious programs.

Malicious software spreads on classic IT systems mostly via e-mail attachments, manipulated websites (drive-by downloads) or data carriers. Smartphones are usually infected via the installation of malicious apps, even drive-by downloads are possible. In addition, open network interfaces, faulty configurations, and software vulnerabilities are common entry points on all IT systems.

In this module, the term "virus protection program" is used. "Viruses" are synonymous with all types of malware. What is meant is a program to protect against any kind of malware.

### 1.2 Objective

This module describes the procedure for creating and implementing protection against malicious programs in order to effectively protect an institution against malicious programs.

### 1.3 Delimitation

This module describes the general requirements for protection against malicious programs. Specific requirements to protect certain IT systems of the institution against malicious programs can be found in the respective building blocks, in particular the layer SYS, for example in SYS.2.2.3 Client under Windows 10. If an identified malicious program leads to a security incident, the requirements of the Building block DER.2.1. Treatment of security incidents. The requirements of the DER.2.3 Cleanup block help to remove identified malware and restore a clean state.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​malware protection:

### 2 1 Software vulnerabilities and drive-by downloads

If IT systems are not adequately protected against malicious programs, which also requires, among other things, that patches are brought in quickly and the protection mechanisms of application programs such as browsers are correctly configured, software vulnerabilities can be exploited to execute malicious code. In the so-called drive-by downloads, for example, it is sufficient to visit a malicious website. A vulnerability in the browser or in an installed plug-in such as Java or Adobe Flash can then be exploited to infect the IT system and provide the attacker with extensive control and access to the network of an institution. Particularly at risk here are IT systems that are not regularly updated, such as many smartphones.

### 2 2 Blackmail by ransomware

A common type of malware is ransomware. This encrypts the data of the infected IT system as well as frequently other data that can be reached via network shares. As a rule, the attackers use encryption methods that can not be reversed without knowing the key, thus forcing their victims to spend large sums of money. If there is no effective protection against malicious programs and no additional precautions like data backups are made, there can be significant restrictions on the availability of information as well as massive financial and image damage.

### 2 3 Targeted Attacks and Social Engineering

Institutions are often attacked with customized malicious programs. This z. B. Leading executives through social engineering methods to open malicious email attachments. Tailor-made malicious programs often can not be detected directly by virus protection programs. The human resources department of an institution, for example, can be a target, for example by malicious application documents are sent by electronic means. If the attacker has been able to infect an IT system in this way, he can spread within the institution and, for example, steal, manipulate or destroy information.

### 2 4 Mobile media infectionsIf the users are not adequately sensitized, mobile data carriers can also serve as a gateway for malicious programs. An attacker can z. B. malicious USB sticks on the grounds of an institution, which are then connected by inexperienced users to IT systems. If there is insufficient protection against malicious programs, an attacker can also gain access to the network and the data of the institution in this way.

### 2 5 botnets

Through malicious programs, IT systems of an institution can become part of so-called botnets. An attacker who frequently controls thousands of systems in such a botnet can use them, for example, to send spam or launch distributed denial-of-service attacks (DDoS) on third parties. Even if your own institution may not be directly harmed, it can still have a negative impact on the availability and integrity of your own services and IT systems, and may even cause legal problems.

### 2 6 Infection of production systems and IoT devices

In addition to classic IT systems, devices are increasingly being attacked by malicious programs, which at first glance do not seem like obvious targets. For example, an attacker could infect a surveillance camera accessible via the Internet to spy on them. But even a networked light bulb or an app-controlled coffee machine can serve as an entry point into the institution's network or as part of a botnet if those devices are not adequately protected from malicious programs. Networked production systems or industrial controls can also be maliciously manipulated or even destroyed, which can result in downtime and many other threats to the institution and its employees, including fires.

3 requirements
---------------

The following are specific requirements for malicious program protection. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The ISB should at least be included in all strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the defined IT security concept.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### OPS.1.1.4.A1 Creation of a concept for protection against malicious programs

It MUST be created a concept, which IT systems must be protected against malicious programs. It also MUST be noted how the protection has to be done. If no reliable protection is possible, then the identified IT systems SHOULD NOT be operated. The concept SHOULD be comprehensibly documented.

#### OPS.1.1.4.A2 Use of system-specific protection mechanisms

It MUST be examined which protections the IT systems used as well as the operating systems and applications used to provide protection against malicious programs. These mechanisms MUST be used unless there is at least equivalent substitution or good reason against it. If they are not used, this should be justified and documented.

#### OPS.1.1.4.A3 Selection of a virus protection program for terminal devices

Depending on the operating system used, other existing protection mechanisms and the availability of suitable virus protection programs, such a protection program MUST be selected and installed for the specific purpose. ONLY Enterprise Products may be used with service and support services tailored to the institution. Products for home users or products without manufacturer support MUST NOT be used in professional operation mode. It may ONLY be used cloud features of such products, where no serious, demonstrable data or privacy issues speak against it.

#### OPS.1.1.4.A4 Selection of a virus protection program for gateways and IT systems for data exchange [specialist responsible]

For gateways and IT systems used for data exchange, a suitable virus protection program MUST be selected and installed. ONLY Enterprise Products may be used with service and support services tailored to the institution. Products for home users or products without manufacturer support MUST NOT be used in professional operation. It may ONLY be used cloud features of such products, where no serious, demonstrable data or privacy issues speak against it.

#### OPS.1.1.4.A5 Operation of virus protection programsThe virus protection program MUST be configured for its environment of use. The recognition performance SHOULD be in the foreground unless data protection or performance reasons weigh more heavily in the respective individual case. If security-related functions of the virus protection program are not used, this should be justified and documented. For protection programs specifically optimized for desktop virtualization, it should be transparent whether to dispense with certain detection methods in favor of performance.

#### OPS.1.1.4.A6 Updating the used virus protection programs and signatures

On the IT systems equipped with this, the virus protection program scan engine and the malware signatures MUST be updated regularly. The frequency of quality-assured signature updates MUST conform to the recommendations of the manufacturer.

An update to new program versions SHOULD be done soon after publication. Each time the virus protection program is updated, the manufacturer's change documentation SHOULD check for any relevant changes. After the update has been installed, the configuration settings MUST be checked and reconciled with the documented presets.

#### OPS.1.1.4.A7 Awareness and Commitment of Users [Users]

Users MUST be regularly briefed on the threat of malware. You MUST follow the basic rules of conduct to reduce the risk of malware infection. Files from untrusted sources SHOULD NOT be opened.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state-of-the-art in the field of malware protection. They SHOULD be implemented in principle.

#### OPS.1.1.4.A8 Use of cloud services

Cloud services to improve the detection performance of virus protection programs SHOULD be used. The corresponding specifications from the requirements OPS.1.1.4.A3 Selection of a virus protection program for terminal devices and OPS.1.1.4.A4 selection of a virus protection program for gateways and IT systems for data exchange MUST be observed.

#### OPS.1.1.4.A9 Malware infection report [user]

Used virus protection program SHOULD automatically block and report an infection with a malicious program. The automatic message SHOULD be accepted at a central location. Depending on the circumstances, the responsible employees SHOULD decide on the further course of action. Regardless of an automatic message, however, the user SHOULD also turn to the designated contact person if there is a suspected infection with a malicious program. The procedure for messages and alarms of virus protection programs SHOULD be planned, documented and tested. It should be specifically regulated, what should happen in the case of a confirmed infection.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### OPS.1.1.4.A10 Use of special analysis environments (CIA)

Automated analysis in a specialized test environment (based on sandboxing or separate virtual or physical systems) SHOULD be used as a supplement to evaluate suspicious files.

#### OPS.1.1.4.A11 Using Multiple Scan Engines (CIA)

To improve detection performance, IT-protected IT systems such as gateways and data-sharing IT systems SHOULD use virus-protection programs with multiple alternative scanning engines.

#### OPS.1.1.4.A12 Use of Disk Locks (CIA)

Before, in particular, data carriers from third parties are to be connected to the IT systems of the institution, they SHOULD be checked by a data carrier lock.

#### OPS.1.1.4.A13 Handling Untrusted Files (CIA)

If it is necessary to open untrusted files, this should only happen on an isolated IT system. The affected files SHOULD be used there z. This can be converted to a non-hazardous format or printed out if it reduces the risk of malware infection.

#### OPS.1.1.4.A14 Selecting and Using Cyber ​​Security Products Against Targeted Attacks (CIA)