1 description
--------------

### 1.1 Introduction

In order to be able to protect IT systems, security-relevant events must be detected and dealt with in good time. For this purpose it is necessary that institutions plan, implement and regularly practice suitable organizational, personnel and technical measures in advance. For if a predefined and proven procedure can be used, reaction times can be shortened and existing processes optimized.

A security event is an event that affects information security and may affect confidentiality, integrity, and availability. Typical consequences of such events are spied out, manipulated or destroyed information. The reasons for this are manifold: Malware, obsolete system infrastructures or culprits play a role. Attackers often exploit zero-day exploits, which are security holes in programs, before there is a patch for them. Another growing threat is Advanced Persistent Threats (APT). These are targeted cyber attacks on selected institutions and facilities where an attacker gains permanent access to a network and extends it to other systems. The attacks are characterized by a very high use of resources and considerable technical capabilities on the part of the attackers and are often difficult to detect.

### 1.2 Objective

This module shows a systematic way in which information can be collected, correlated and evaluated in order to detect safety-related events as completely as possible and in a timely manner. The lessons learned from detection are designed to enhance the ability of institutions to identify and respond appropriately to security-related events.

### 1.3 Delimitation

The block contains basic requirements that must be observed and fulfilled when safety-relevant events are detected. The prerequisite for this, however, is that comprehensive logging is carried out. The necessary measures are not described in this module, but are included in OPS.1.1.5 * Logging *.

In addition, the block does not describe how to deal with security-related events after they have been detected. Recommendations are listed in DER.2.1 * Incident Management * and DER.2.2 * Forensics *. Likewise, the topics of data protection and archiving of log data will not be discussed, these will be dealt with in CON.2 * Privacy * and OPS.1.1.2 * Archiving *.

To detect security-related events, additional programs are often required, eg. Anti-virus programs, firewalls or intrusion detection / intrusion prevention systems (IDS / IPS). Safety aspects of these systems are likewise not the subject of the present module. They are z. These are discussed in, for example, NET.3.4 * IDS / IPS *, OPS.1.1.5 * Protection against malicious programs * and NET.3.2 * Firewall *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the detection of security-related events:

### 2 1 Disregard of legal regulations and company participation rights

Programs that detect security-related events and evaluate log data often gather much information about the network structure and internal processes of an institution. This can z. B. Protected data, such as personal data, classified information or work processes of employees be included. However, the fact that such data are stored may violate personal rights or co-determination rights of employees. Under certain circumstances, the institution may also violate the respective state data protection laws or the Federal Data Protection Act.### 2 2 Insufficient qualification of those responsible

In the daily IT operation of an institution, many errors and errors can occur (for example, a large increase in incoming protocol data). If the responsible employees are not adequately sensitized and trained, there is a risk that they will not identify security-relevant events as such and thus an attack remains undetected.

### 2 3 Missing or inadequate logging

If security-relevant events are recorded inadequately or not at all, it is not possible to determine sufficiently and quickly enough whether security requirements are violated or whether attempts to attack occur. Also, in the case of damage no error analysis can be performed and the gateway of an attack may remain. Also, protocol information is used to perform integrity checks. However, if the logs are missing, this is not possible.

### 2 4 Incorrect administration of the detection systems used

Incorrect configurations can cause the detection systems used to function incorrectly. If, for example, the alarm is set incorrectly, increased false alarms can occur. The responsible employees may then no longer be able to differentiate between a false alarm and a security-relevant event. Also, they may not catch the messages promptly, as too many alarms are generated. This may leave attacks undetected. Similarly, the effort increases greatly to evaluate the amount of messages.

### 2 5 Missing information about the protected information network

If there is no information or only insufficient information about the information network, there is a danger that essential areas of the information network will not be adequately protected by detection systems. As a result, attackers can easily penetrate the network of the institution and, for example, access information worthy of protection. It is also possible for them to stay in the system long unnoticed and to access the network permanently.

### 2 6 Inadequate use of detection systems

If detection systems are not used, and the security-related events detection functions used in IT systems and applications are not used, it is easier for attackers to penetrate the institution's network and gain unauthorized access to sensitive information. It is particularly critical if the transitions between network boundaries are insufficiently monitored.

### 2 7 Insufficient human resources

If there are not enough personnel to evaluate log data, safety-relevant events can not be completely detected. So attacks may remain hidden for a long time or are only discovered when z. B. have leaked a lot of information worth protecting. Even if no external sources of information are evaluated due to insufficient staff, security gaps may remain open for too long and can be exploited by attackers to illegally penetrate the IT systems of the institution.

3 requirements
---------------

The following are specific requirements for the detection of safety-related events. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### DER.1.A1 Creation of a security policy for the detection of security-relevant events [Information Security Officer (ISB)]On the basis of the institution's general security policy, a specific security policy MUST be drawn up in which comprehensible requirements and specifications are described, how the detection of security-relevant events can be planned, constructed and operated safely. The policy MUST be known to all employees responsible for detection and fundamental to their work. If the policy is changed or deviated from the requirements, this MUST be coordinated and documented with the responsible ISB. It MUST be checked on a regular basis to see if the directive is still correctly implemented. The results MUST be documented in a meaningful way.

#### DER.1.A2 Compliance with legal conditions when evaluating log data [Information Security Officer (ISB)]

If log data is evaluated, the legal provisions from the current federal / state data protection laws MUST be adhered to. In addition, the personal rights or co-determination rights of employee representatives MUST be respected when using detection systems. Likewise MUST be ensured that all other relevant legal provisions are observed, for. B. Telemedia Act (TMG), Works Constitution Act and Telecommunications Act.

#### DER.1.A3 Definition of reporting routes for safety-related events

Appropriate reporting and alerting channels MUST be defined and documented. It MUST be determined which bodies should be informed when. Also MUST be listed, how the respective persons can be reached. Depending on the urgency, a security-relevant event MUST be reported via various communication channels.

The reporting and alerting channels MUST be printed out to the employees. All persons relevant for the notification or alarm MUST be informed about their tasks. All the steps of the reporting and alerting process MUST be described in detail. The established reporting and alerting channels SHOULD be regularly reviewed, tested and, if necessary, updated.

#### DER.1.A4 Awareness of employees [supervisors, IT managers, users]

In order for employees to quickly identify possible security incidents, they MUST be sensitized accordingly. Regular training sessions SHOULD be held to highlight current and current threats and cybercrime practices.

Employees MUST also be made aware that they will not simply ignore or close client event messages, but pass the messages on to the responsible incident management team according to the alerting pathways (see DER.2.1 * Incident Management *).

Each employee MUST report a detected incident immediately to Incident Management.

#### DER.1.A5 Use of supplied system functions for detection [specialist responsible]

If IT systems or applications have functions that can be used to detect safety-related events, they MUST be activated and used.

Logging must be activated on all components used (see OPS.1.1.5 * Logging *). If a security-relevant incident occurs, the messages MUST be evaluated at least locally. In addition, the logged events of other IT systems MUST be checked. Also the collected messages SHOULD be checked punctually in binding fixed periods.It MUST be checked whether additional malicious code scanners should be installed on central IT systems (see also SYS.1.1 * General Server *). If so, they MUST allow them to centrally access their messages and logs. In addition, they MUST be updated regularly. It MUST be ensured that the malicious code scanners automatically report safety-relevant events to the persons responsible and that the messages are also evaluated and examined.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of detection of safety-relevant events. They SHOULD be implemented in principle.

#### DER.1.A6 Continuous monitoring and evaluation of log data [user]

All log data SHOULD be actively monitored and evaluated as permanently as possible. It SHOULD name employees who are responsible.

Do the responsible employees have to actively search for security-related events? For example, if they control or test IT systems, such tasks SHOULD be documented in appropriate procedures.

Sufficient human resources SHOULD be provided for the detection of security-related events.

#### DER.1.A7 Training of managers [supervisors, IT managers]

All those responsible for controlling event reports SHOULD receive further training and qualifications. When procuring IT components, a budget for training should be scheduled and a training concept designed for the responsible staff.

#### DER.1.A8 Definition of segments to be protected [specialist responsible persons]

The network plan (see NET.1.1 * Network architecture and design *) SHOULD specify which network segments must be protected by additional detection systems (see DER.1.A9 * Use of additional detection systems *).

#### DER.1.A9 Use of Additional Detection Systems [Specialists]

In order to better recognize safety-relevant events, the information network SHOULD be supplemented by additional detection systems and sensors. For example, malicious code detection systems should be deployed and managed centrally. The transitions between internal and external networks defined in the network SHOULD also be supplemented by network-based intrusion detection systems (NIDS).

#### DER.1.A10 Using TLS / SSH Proxies [Specialists]

At transitions to external networks, TLS / SSH proxies SHOULD be used to break the encrypted connection, allowing it to check the transmitted data for malware. All TLS / SSH proxies SHOULD be protected against unauthorized access. In addition, security-related events on the TLS / SSH proxies SHOULD be automatically detected. An organizational regulation SHOULD be created under which data protection requirements the log data may be evaluated manually.

#### DER.1.A11 Use of a central logging infrastructure for the evaluation of security-relevant events [responsible persons]

The collected event messages of the IT systems and application systems SHOULD be stored on a central protocol infrastructure (see OPS1.1.5 * Logging *). The delivered event messages SHOULD be centrally stored, evaluated and retrieved using a tool. In order for the data to be correlated and reconciled, they SHOULD all be synchronized in time. The collected event messages SHOULD be regularly checked for abnormalities. So that safety-related events can also be detected retrospectively, the signatures of the detection systems SHOULD be up to date and up-to-date.#### DER.1.A12 Evaluation of information from external sources [Information Security Officer (ISB), specialist responsible]

In order to gain new insights into security-relevant events for their own information network, external sources SHOULD be consulted and evaluated. Since messages are delivered to an institution via different channels, it should be ensured that these messages are also recognized by the employees as being relevant and forwarded to the right place. If information comes from qualified sources, they SHOULD be evaluated in principle. All submitted information SHOULD be evaluated as to whether it is relevant to its own information network. If this is the case, the information SHOULD be escalated according to the incident handling procedure (see DER.2.1. * Incident Management *).

#### DER.1.A13 Regular audits of the detection systems

The existing detection systems and the measures taken SHOULD regularly be checked to see if they are still up-to-date and effective. It SHOULD evaluate the measured variables, which occur, for example, when safety-relevant events are recorded, reported and escalated. The audit results SHOULD be traceable documented and compared with the target state. Deviations SHOULD be investigated.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### DER.1.A14 Evaluation of log data by specialized personnel [Head IT] (CI)

Employees SHOULD primarily be assigned to monitor all log data. The seconded staff SHOULD receive specialized advanced training and qualifications. A group of persons SHOULD be named, who are exclusively responsible for the topic of evaluation of log data, such. B. from the field of forensics, is responsible.

#### DER.1.A15 Central detection and real-time event reporting (CIA)

Central components SHOULD be used to detect and evaluate safety-related events. Central Automated Analyzes with software tools SHOULD be used to record, correlate, and visualize all events occurring in the system environment. All submitted data SHOULD be completely visible and evaluable in the log management. The actual data SHOULD be evaluated as permanently as possible. If defined thresholds are exceeded, SHOULD automatically be alerted. Personnel SHOULD make sure that in the event of an alarm, a qualified and responsive response is initiated immediately. In this context, the affected employee SHOULD be informed immediately.

The system managers should regularly audit the analysis parameters and, if necessary, adjust them. In addition, already reviewed data SHOULD be automatically examined for safety-relevant events.

#### DER.1.A16 Use of detection systems according to protection requirements (CIA)

Applications with increased protection requirements SHOULD be protected by additional detection measures. For this purpose, for. B. such detection systems are used, with which the increased protection requirements can be technically ensured.

#### DER.1.A17 Automatic response to security events (CI)In a safety-relevant event, the detection systems used should automatically report the event and react with suitable protective measures. In doing so, procedures should be used that automatically detect possible attacks, attempted abuse or security breaches. It SHOULD be possible to automatically intervene in the data stream to prevent a possible security incident.

#### DER.1.A18 Conduct regular integrity checks (CI)

All detection systems SHOULD regularly be checked to see if they are still integer. Also, the user rights SHOULD be controlled. In addition, the sensors SHOULD perform integrity checks on files and trigger automatic alerts as the values ​​change.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on hazards and safety measures in the area "Detection of safety-relevant events" can be found in the following publications, among others:

* #### [BSILeit1] BSI Guide to Introducing Intrusion Detection Systems,

  

 IDS, BSI, Version 1.0, 10.2002
 [Https://www.bsi.bund.de/DE/Publikationen/Studien/IDS02/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/Studien/IDS02/index_htm. html)

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008
 <Https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "Detection of safety-relevant events".

* G 0.9 Failure or malfunction of communication networks
* G 0.11 Failure or disruption of service providers
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.27 Resource shortage
* G 0.28 Software vulnerabilities or errors
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.33 Personnel loss
* G 0.37 denying actions
* G 0.38 Abuse of personal data
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.41 Sabotage
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.