Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

To limit damage and prevent further damage, detected security incidents must be dealt with quickly and efficiently. Therefore, it is necessary to establish a predetermined and proven procedure for the handling of security incidents (* Security Incident Handling or Security Incident Response) *.

A security incident can have a strong impact on an institution and cause major damage. For example, such incidents are misconfigurations that cause confidential information to be disclosed or criminal acts such Hacking of servers, theft of confidential information, sabotage or IT-related blackmail.

The causes of security incidents are manifold: Malware, obsolete system infrastructures, or perpetrators play a role. Attackers often exploit zero-day exploits. Another growing threat is Advanced Persistent Threats (APT).

In addition, users, administrators, or external service providers may not behave properly, causing system parameters to change security-critical or violate internal policies. Furthermore, the cause may be that access rights are violated, that software, hardware, or rooms and buildings in need of protection are insufficiently secured.

### 1.2 Objective

The aim of this module is to show a systematic way how a concept for the treatment of security incidents can be created.

### 1.3 Delimitation

The focus of this module is on the handling of security incidents from the point of view of information technology. However, before security incidents can be handled, they must be detected. Safety requirements for this are contained in block DER.1 * Detection of safety-relevant events * and are assumed in the present block. The initial forensic investigation is dealt with in the module DER.2.2 * Forensics * and the correction after an APT incident in the module DER.2.3 * Clearance of far-reaching security incidents (APT responders) *. A special area of ​​the treatment of security incidents is the emergency management, which is discussed in the module DER.4 * emergency management * and will not be considered further here. However, it should be noted that the decision as to whether an emergency exists or not, is made in the present module.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the handling of security incidents:

### 2 1 Inappropriate handling of security incidents

In practice, it can never be ruled out that security incidents will occur. This also applies if a large number of security measures have been implemented. Responding to acute security incidents either unresponsive or inadequate will result in major damage, including catastrophes. Examples are:

* In the log files of a firewall are noticeable entries. Failure to promptly assess whether the first sign of a break-in attempt is to allow attackers to pass the firewall unnoticed and penetrate the internal network of the institution with a successful attack.
* Vulnerabilities in the IT systems or applications used are known. If this information is not obtained on time and necessary countermeasures are not promptly initiated and implemented, these vulnerabilities can be exploited by attackers.
Failure to take appropriate action to handle security incidents can result in wrong decisions in a hurry and under stress. These can be z. For example, misleading the press and causing a negative external impact, harming third parties with their own IT systems and claiming damages, or foreseeing no evasion or recovery measures will significantly increase the damage to the institution ,

### 2 2 Unrecognized security incidents

In the daily operation of an institution many errors and errors can occur. It may happen that security incidents are not identified as such by the personnel and an attack or attempted attack remains unrecognized. Even though the employees are sufficiently sensitized or trained for the interests of information security, it can not be ruled out that they do not recognize security incidents. Examples for this are:

* A user who has not been logged into their institution's local area network for a long time thinks that their laptop's significant slowdown in Internet access for one week has been normal and does not realize that a malicious program is running in the background. He was not or insufficiently trained to inform the security officer in case of suspicious abnormalities.
* A production manager does not notice that the data in the production systems and also the control display systems have been secretly changed. He does not suspect, as the SCADA control of the production plant shows strange values, since this was only for a short time. The incident is not reported because all values ​​are back to the expected display values. Nobody is struck by the fact that a malicious software has manipulated the display values.
* A burglary in a store is considered a case of procuring crime as notebooks and flat screens have been stolen. The fact that the notebooks contained confidential information and access data for IT systems on the intranet is given no greater importance and the ISB is not informed. Therefore, the institution is not prepared for the subsequent attacks on the IT systems of other locations and the company headquarters. The attack uses the data found on the stolen notebooks.
### 2 3 Destruction of evidence traces in the handling of security incidents

Careless or non-compliant handling of security incidents may result in the inadvertent destruction or non-judicialization of important evidence traces for the investigation or subsequent legal prosecution.

Examples for this are:

* An attacker placed malicious software on a workstation, whose operation and target can only be analyzed while it is still running. For this, information about the active processes and the contents of the main memory would have to be backed up and evaluated. If the workstation is now shut down prematurely, the information from the current state can no longer be used to analyze and clarify the security incident.
* An administrator finds a running process on a server that causes an above-average CPU usage. In addition, this process creates temporary files and sends unknown information over the Internet. If the process is terminated prematurely and the temporary files are simply deleted, it can not be determined if confidential information has been successfully stolen.
* An important server is compromised because the administrator could not bring in the latest security updates as planned due to the heavy workload and a lack of maintenance window. In order to avoid possible disciplinary consequences, the administrator enters the missing updates before a security team can analyze the reason for the break-in and the damage incurred. Lack of error culture has thus prevented an analysis of the problem.
