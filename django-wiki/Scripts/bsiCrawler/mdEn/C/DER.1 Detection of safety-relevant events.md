Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

In order to be able to protect IT systems, security-relevant events must be detected and dealt with in good time. For this purpose it is necessary that institutions plan, implement and regularly practice suitable organizational, personnel and technical measures in advance. For if a predefined and proven procedure can be used, reaction times can be shortened and existing processes optimized.

As a security incident an event is called, has an impact on information security and may adversely affect the confidentiality, integrity and availability. Typical consequences of such events are spied out, manipulated or destroyed information. The reasons for this are manifold: Malware, obsolete system infrastructures or culprits play a role. Attackers often exploit zero-day exploits, which are security holes in programs, before there is a patch for them. Another growing threat is Advanced Persistent Threats (APT). It is targeted cyber attacks to selected institutions and organizations in which an attacker is permanent access to a network and this spreads to other systems. The attacks are characterized by a very high use of resources and considerable technical capabilities on the part of the attackers and are often difficult to detect.

### 1.2 Objective

This block shows a systematic way information is collected, correlated and can be evaluated to detect security events as completely and promptly. The lessons learned from detection are designed to enhance the ability of institutions to identify and respond to security-related events.

### 1.3 Delimitation

The block contains basic requirements that must be observed and fulfilled when safety-relevant events are detected. The prerequisite for this, however, is that comprehensive logging is carried out. The necessary measures are not described in this module, but are included in OPS.1.1.5 * Logging *.

In addition, the block does not describe how to deal with security-related events after they have been detected. Recommendations are listed in DER.2.1 * Incident Management * and DER.2.2 * Forensics *. Likewise, the topics of data protection and archiving of log data will not be discussed, these will be dealt with in CON.2 * Privacy * and OPS.1.1.2 * Archiving *.

To detect security-related events, additional programs are often required, eg. Anti-virus programs, firewalls or intrusion detection / intrusion prevention systems (IDS / IPS). Safety aspects of these systems are likewise not the subject of the present module. They are z. These are discussed in, for example, NET.3.4 * IDS / IPS *, OPS.1.1.5 * Protection against malicious programs * and NET.3.2 * Firewall *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the detection of security-related events:

### 2 1 Disregard of legal regulations and company participation rights

Programs that detect security-related events and evaluate log data often gather much information about the network structure and internal processes of an institution. This can z. B. Protected data, such as personal data, classified information or work processes of employees be included. However, the fact that such data are stored may violate personal rights or co-determination rights of employees. Under certain circumstances, the institution may also violate the respective state data protection laws or the Federal Data Protection Act.
### 2 2 Insufficient qualification of those responsible

In the daily IT operation of an institution, many errors and errors can occur (for example, a large increase in incoming protocol data). If the responsible employees are not adequately sensitized and trained, there is a risk that they will not identify security-relevant events as such and thus an attack remains undetected.

### 2 3 Missing or inadequate logging

If security-relevant events are recorded inadequately or not at all, it is not possible to determine sufficiently and quickly enough whether security requirements are violated or whether attempts to attack occur. Also, in the case of damage no error analysis can be performed and the gateway of an attack may remain. Also, protocol information is used to perform integrity checks. However, if the logs are missing, this is not possible.

### 2 4 Incorrect administration of the detection systems used

Incorrect configurations can cause the detection systems used to function incorrectly. If, for example, the alarm is set incorrectly, increased false alarms can occur. The responsible employees may then no longer be able to distinguish between a false alarm and a security-relevant event. Also, they may not catch the messages promptly because too many alarms are generated. This may leave attacks undetected. Similarly, the effort increases greatly to evaluate the amount of messages.

### 2 5 Missing information about the protected information network

If there is no information or only insufficient information about the information network, there is a danger that essential areas of the information network will not be adequately protected by detection systems. As a result, attackers can easily penetrate the network of the institution and, for example, access information worthy of protection. It is also possible for them to stay in the system long unnoticed and to access the network permanently.

### 2 6 Inadequate use of detection systems

If detection systems are not used, and the security-related events detection functions used in IT systems and applications are not used, it is easier for attackers to penetrate the institution's network unnoticed and access unauthorized sensitive information. It is particularly critical if the transitions between network boundaries are insufficiently monitored.

### 2 7 Insufficient human resources

If there are not enough personnel to evaluate log data, safety-relevant events can not be completely detected. So attacks may remain hidden for a long time or are only discovered when z. B. have leaked a lot of information worth protecting. Even if no external sources of information are evaluated due to insufficient staff, security gaps may remain open for too long and can be exploited by attackers to illegally penetrate the IT systems of the institution.

