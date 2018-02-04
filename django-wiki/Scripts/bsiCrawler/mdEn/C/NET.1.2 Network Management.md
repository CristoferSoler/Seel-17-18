Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Reliable network management is a prerequisite for the secure and efficient operation of modern networks. This requires network management to fully integrate all network components and implement appropriate measures to protect management communications and infrastructure.

Network management includes many important functions, such as: For example, network monitoring, component configuration, event handling, and logging. Another important function is reporting, which can be created as a common platform for the network and IT systems. Alternatively, it can be implemented as a single platform or as part of the individual management components.

The network management infrastructure consists of central management systems (eg SNMP server), administration terminals with software for management access, decentralized management agents, dedicated management tools (eg probes or specific measuring instruments) , Management protocols (such as SNMP or SSH), and management interfaces (such as dedicated Ethernet ports or console ports).

### 1.2 Objective

The aim of this module is to establish information security as an integral part of network management.

### 1.3 Delimitation

This module considers the necessary components and conceptual tasks for network management. The counterpart in the system management for networked clients and servers is described in the block SYS.5 * System Management *.

The present module specifies the basic requirements of the module NET.1.1 * Network architecture and design. * It also discusses how to build and secure network management and how to protect its communications. However, details regarding the protection of network components, in particular their management interfaces, are dealt with in the component groups NET.2 and NET.3.

The management of the passive network infrastructure is dealt with in the building blocks of the infrastructure (building block layer INF) or industrial IT (building block layer IND). Therefore, these topics are not included in this module.

The logging addressed in this module should be integrated into a comprehensive logging and archiving concept. (see OPS.1.1.5 * Logging *).

The subject of outsourcing is not dealt with in detail in this module. Further requirements are described in the module OPS.2.1 * Outsourcing *.

General considerations for the safe, efficient and orderly operation of network management are described in this module only if it goes beyond the general requirements of the module OPS.1.1.1 * General IT Operations *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in network management:

### 2 1 Unauthorized access to central network management components

If attackers succeed in accessing network management solutions, eg. For example, by unpatched security holes or insufficient network separation, they can control and reconfigure all network components connected there. So you can z. B. to access sensitive information, redirect network traffic or disrupt the entire network sustainable.

### 2 2 Unauthorized access to individual network components

If attackers succeed in accessing individual network components, they can control and manipulate the respective component. Any traffic routed via the network component can thus be compromised. In addition, further attacks can be prepared to penetrate deeper into the institution's network.

### 2 3 Unauthorized interference with network management communication
If the management communication is intercepted and manipulated, active network components can be misconfigured or controlled in this way. This can violate network integrity and limit the availability of the network infrastructure. In addition, the transmitted data can be recorded and viewed.

### 2 4 Insufficient time synchronization of network management components

If the system time of the network management components is insufficiently synchronized, the logging data may not be correlated with each other, or the correlation may lead to incorrect statements, since the different timestamps of events have no common basis. This can not properly govern events that have occurred and problems can not be resolved. As a result, for example, security incidents and data outflows can go undetected.

