[toc]
 
1 description
--------------

### 1.1 Introduction

The ongoing administration of IT systems and components is fundamental to IT operations. The system administrators set up IT systems and applications, observe the operation and react with measures that preserve the function and performance of the systems, or adapt the systems to the changing needs. They also perform a number of security tasks: not only do they make the systems available, they also implement security measures and verify their effectiveness. For this they have very extensive authorizations, so that it is also very important for the security of the information network to protect the system administration against unauthorized access.

### 1.2 Objective

The goal of this module is to demonstrate how proper IT administration meets the security requirements of IT applications, systems, and networks.

On the one hand, with the implementation of this module, the institution ensures that the activities required in the system administration for the security of the information network are carried out properly and systematically. On the other hand, the institution also reacts to the special threats that inevitably arise from dealing with administration privileges and from gaining access to areas worthy of protection in the institution.

### 1.3 Delimitation

The module describes general security requirements for proper IT administration. It considers ongoing administrative activities carried out by designated personnel at the institution's sites. It must be distinguished from remote administration of IT systems via external interfaces, as well as remote maintenance of devices and components by the respective manufacturers or suppliers, which is considered in the module * OPS.2.4 Remote maintenance *.

The subject of the module are general requirements for the administration process as such. Specific requirements for the management of individual IT systems and components are dealt with in the module * OPS.1.1.2 Network and System Management *. There are corresponding requirements, such as systems installed and put into operation, such as changes and maintenance performed or systems are singled out.

The other building blocks of the area * OPS.1.1 core IT operation * describe aspects of IT operation that are relevant in addition to the present building block. They should therefore additionally be considered and modeled in addition to this module.

A particular security relevance in an institution is the proper administration of users and rights. Therefore, this topic is also covered in a separate building block * * (see * ORP.4 Identity and Permission Management) *.

The requirements described in this module must also be applied if administrative tasks are performed by third parties. Special requirements for such cases are additionally described in the modules * OPS.2.1 Outsourcing for Customers and OPS.3.1 Outsourcing for Service Providers *.

Furthermore, the module Proper IT Administration refers to the regular operation. In exceptional situations, especially in the event of a potential IT attack and the compromising of systems, different requirements must be observed, which are described in the relevant building blocks from the area of ​​* DER.2 Security Incident Management *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​proper IT administration:

### 2 1 Failures due to unregulated responsibilities
If the IT organization has the administrative responsibilities, eg. If, for example, planning, installation, documentation, patch management and monitoring are not clearly regulated or the regulations are not known and understood to the involved employees, this may mean that security-relevant tasks from these areas are not or not systematically carried out , Typical examples are an unclear definition of the responsibilities between IT and telecommunications technology, between office IT and production facilities or between application and platform operation.

### 2 2 Staff shortages of core competencies

Even administrators can be unplanned or long-term. Without trained representatives, there is no guarantee that the systems and applications they are looking after will continue to operate properly and safely. Administrators sometimes build up a great deal of detailed knowledge of the systems and applications they are looking after, which includes the products and solutions used on the one hand, and the specifics of the deployment environment and the specific configuration on the other hand. With this knowledge, they can quickly recognize error situations and implement requirements more easily, which often leads to the administration of individual persons, especially in complex systems. If this person fails, the knowledge for the institution is no longer available.

### 2 3 Abuse of administrative permissions

Administrative permissions allow extensive access to documents, communication content and databases. Administrators can use these far-reaching permissions not only to perform the tasks assigned to them, but also for their own purposes or in the sense of third parties. So they could z. B. View personnel records or read communications from colleagues. Third, pressure or other incentives could also be used by administrators to misappropriately access data or systems.

### 2 4 Relief from attacks

The privileged system access of the administrators is often the focus of attackers. If administrative tasks are not properly performed, attacks on the information network can be made considerably easier. Negligence may result in errors in the configuration, protective measures provided may not or only insufficiently implemented or suspicions that arise can not be tracked. Causes are z. For example, a lack of security awareness, high time pressure or lack of processes and procedures. This can lead to vulnerabilities that could be exploited by attackers.

### 2 5 Disturbance of operation

Administrative activities directly influence the operation of IT systems and applications. For example, ongoing user sessions can be aborted when IT systems are restarted or legitimate access is prevented when a firewall policy is customized. If such operations are performed without considering how they affect the users and without coordinating them with the affected areas, the operation can be significantly disrupted.

### 2 6 Lack of information on incidents
Deficiencies in the documentation of the IT operation or missing records can lead to the fact that IT security incidents can not be clarified or tracked. Since security incidents are often not easily recognizable, such. If the attack has expired, what extent it has had or how it has been manipulated, this must first be determined by means of suitable investigations. However, this assumes, for example, that the target state of systems prior to the incident is documented and verifiable, or that proper unauthorized changes to systems can be distinguished on the basis of appropriate records. If such information is lacking, incidents are difficult or impossible to resolve. Even a judicial proof against the perpetrators is no longer possible in such cases.
