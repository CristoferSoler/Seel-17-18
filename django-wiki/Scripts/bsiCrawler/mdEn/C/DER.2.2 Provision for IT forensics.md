Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

IT forensics is the strictly methodical data analysis on data carriers and in computer networks for the clarification of incidents, taking into account the possibilities of strategic preparation, especially from the point of view of the plant operator of an IT system.

Forensically investigating IT security incidents is always necessary if damage is to be determined, attacks should be averted and avoided in the future, and attackers identified. Whether an IT security incident is investigated forensically is decided on during the incident. An IT forensic investigation in the sense of this module consists of the following phases:

* Strategic Preparation: In this phase, processes are planned and built to ensure that an institution can forensically analyze IT security incidents. It is also necessary if the institution does not have its own forensic experts.
* Initialization: After the responsible employees have decided to forensically investigate an IT security incident, the previously planned processes are triggered. Furthermore, the scope of the investigation will be determined and initial measures will be carried out.
* Forensics: Here, the evidence to be backed up is selected and the data forensically secured. A distinction is made between live forensics and post-mortem forensics: live forensics ensures that volatile data (eg network connections, RAM) is backed up by a running IT system. In the case of post-mortem forensics, however, forensic copies of data carriers are created.
* Analysis: The collected data is analyzed forensically. The data are considered both individually and in the overall context.
* Presentation of results: The relevant test results are prepared and taught according to the target group.
### 1.2 Objective

The module shows what precautionary measures are necessary to enable IT forensic investigations. The focus will be on how forensics can be prepared and carried out. If forensic service providers carry out forensics in whole or in part, the requirements also apply to the service providers. Through contractual agreements and examinations, it can be ensured that the service provider adheres to the same.

### 1.3 Delimitation

The module does not describe any requirements to ensure that attacks are detected. These are contained in the module DER.1 * Detection of safety-relevant events * and are assumed in the present block. Also, no criteria and processes are explained, by means of which the responsible persons can decide, whether an IT security incident must be examined forensisch or not. The decision is made while the incident is being handled (see DER.2.1 * Incident Management *).

Furthermore, the module deals only with precautionary measures, which are fundamental for later IT forensic investigations. How the actual forensic analysis is performed is therefore not the subject of this module.

Ultimately, the building block also does not address how IT infrastructures can be cleaned up after they have been attacked (see DER.2.3 * Clean Up Major Security Incidents *). However, the activities described there can be significantly supported by the results of IT forensic investigations.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance for provisioning for IT forensics:

### 2 1 Infringement of legal framework
For IT forensic investigations, all data deemed necessary are often copied, secured and evaluated. This usually includes personal data of employees or partners. Is it z. Unfounded and without the Privacy Commissioner is involved, accessed, the institution violates legal regulations, such. For example, if the earmarking is disregarded. It is also possible that, for example, it can be deduced from the collected data how employees behave, or a relationship to them can be established. As a result, there is a risk that internal regulations will also be violated.

### 2 2 Loss of evidence through incorrect or incomplete preservation of evidence

If evidence is backed up incorrectly or not fast enough, it may lose important data that can not be recovered later. At worst, this leads to a fruitless forensic investigation. At least, however, the probative value is limited.

The risk of losing important evidence increases when employees misuse forensic tools, back up data too slowly or practice too little. Often, evidence is lost if those responsible do not recognize and secure transient data as relevant.

