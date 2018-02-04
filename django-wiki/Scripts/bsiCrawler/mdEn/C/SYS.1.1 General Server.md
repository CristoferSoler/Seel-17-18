Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

This module covers general security requirements for all IT systems that provide services to other IT systems, such as clients or other servers. These services may be basic services for the local or external network, but also allow e-mail exchange or offer databases and print services. Servers are of central importance to information technology and thus to the functioning work processes of an institution. Often, servers perform tasks without any direct interactive use by a user. In addition, there are server services that interact directly with the users and are not perceived at first glance as a server service, for example, X servers under Unix.

### 1.2 Objective

The goal of this module is to protect information that is processed, offered or transmitted on servers, as well as the related services.

### 1.3 Delimitation

Usually, server systems are run under operating systems that have specific security requirements in each case. For common server operating systems, the IT-Grundschutz Compendium has its own modules that specify this module. The module "general server" forms the basis for the concrete building blocks on which they are based. If a specific block exists for a considered system, it must be used in addition to the module General Server. If no specific module exists for server systems used, the requirements of this module must be suitably specified.

The specific services offered by the server are not part of this module. For these server services, additional blocks must be implemented in addition to this block, according to the results of the modeling according to IT-Grundschutz. Insofar as an interactive use by users is provided for a server system in individual cases (eg terminal server), the associated security aspects are likewise to be considered separately, for example by applying the corresponding concretized components.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to General Servers.

### 2 1 Software vulnerabilities or errors

The more complex the software, the more frequently programming or design errors occur. Software vulnerabilities are unintentional program errors that are not or not yet known to the user and that pose a security risk to the IT system. There are constantly new security vulnerabilities found in existing, even in widespread or completely new software.

If software errors are not detected and corrected promptly, the errors that arise during the application can have far-reaching consequences. With widespread standard software, software vulnerabilities can quickly lead to serious security problems for all types of institutions.

In particular, errors in server services can have serious consequences. In the case of a vulnerability or an error in a network service, local access rights are not required to exploit them; it is often enough for the attacker to be able to access the network. If the server offers the server service with the vulnerability or error on the Internet, it could potentially exploit this error or vulnerability from any IT system worldwide.

### 2 2 Data loss

The loss of data can have a significant impact on business processes and thus on the entire institution, especially for servers. Many IT systems, such as clients or other servers, often rely on the central data stored there being available.
If business-relevant information of any kind is destroyed or falsified, business processes and specialized tasks can be delayed or even prevented from running. Overall, the loss of stored data, in addition to the loss and cost of recovering the data, especially long-term consequences, such as loss of trust among customers and partners, legal effects and a negative impact on the public lead. In many institutions regulations exist that no data may be stored on the local clients, but centralized storage on the servers must be used for this purpose. Data loss of this data then has serious consequences; the direct and indirect damage caused may even threaten the existence of institutions.

### 2 3 Prevention of services

One type of availability attack called "denial of service" aims to prevent users from using features or devices normally available to them. This attack is often associated with distributed resources by an attacker consuming these resources to the extent that other users are prevented from working and can no longer access the resources they depend on. In general, IT systems are also highly dependent on each other, the scarcity of resources of a server are quickly affected more servers. For example, CPU time, memory or bandwidth may be artificially curtailed, which may result in the service or resource being unusable at all.

### 2 4 Provision of unused operating system components and applications

Even with the installation of the server operating system, it is possible to install all supplied applications and services. Even in operation often software is installed, which is briefly tested, but then no longer needed. Often it is not known that these unused applications and services exist on the servers. In this way, there are numerous applications and services on the server, which are not used, thus unnecessarily burdening the server.

Such unused applications and services can contain vulnerabilities. If the applications are no longer updated then they can be an attack gate for attackers. If the installed applications and services are unknown, the IT operation is unaware that they also need to be updated.

### 2 5 Overloading of servers

If servers are not adequately dimensioned, then at some point the point is reached where they no longer meet the requirements of the users. Depending on the type of systems involved, this can have a variety of negative effects, such as the servers or services being temporarily unavailable or data loss occurring. Overloading a single server in complex IT landscapes can cause problems or failures for other servers.

Triggers for the overload of information systems can be that

* installed services or applications are misconfigured, unnecessarily consuming memory
* existing storage capacities are exceeded,
Numerous requests at the same time overstrain a system and overload the processors
* too much computing power is claimed by the services or
* a large number of messages will be sent at the same time.
