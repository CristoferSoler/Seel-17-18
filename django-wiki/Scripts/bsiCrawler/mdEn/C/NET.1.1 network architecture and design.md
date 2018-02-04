Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Most institutions today require computer networks for their business operations. B. information and data exchanged and distributed applications can be realized. Not only are traditional networks, partner institutions and the Internet integrated into such networks, but they are increasingly integrating mobile devices and elements that are assigned to the Internet of Things (IoT). In addition, cloud networks and services for Unified Communication and Collaboration (UCC) are increasingly being used over computer networks. The benefits of doing so are undeniable. But the many terminals and services are also increasing the risks. That's why it's important to protect your own network with a secure network architecture. To do this, for example, it is necessary to plan how a local area network (LAN) or a wide area network (WAN) can be set up safely. Similarly, only limited trusted external networks, eg. As the Internet or customer networks are properly connected.

In order to ensure a high level of security, additional safety-relevant aspects must be taken into consideration. For example, different clients and device groups are securely separated at the network level and their communication is controlled by firewall techniques. Another important security element especially in the client area is the network access control (see NET.1.3 * Network Access Control *).

### 1.2 Objective

The aim of this module is to establish information security as an integral part of the network architecture and the network design.

### 1.3 Delimitation

The module contains basic requirements that must be observed and fulfilled when networks are planned, constructed and operated. Requirements for the safe operation of the corresponding network components, including safety components such. As Firewalls and Intrusion Detection Systems / Intrusion Prevention Systems (IDS / IPS), are not the subject of this module. These are handled in the block group NET.3 * Network Components *.

The focus of this module is on wired networks and data communication. However, general architectural and design requirements, e.g. For example, separate security zones and segments for all network technologies. Further specific requirements for network areas such as wireless LAN (WLAN) or storage area networks (SAN) are dealt with in the block groups NET.2 * wireless networks * or in the block SYS.1.8 * storage systems *. In addition, the topics UCC and Voice over IP (VoIP) as well as the underlying security infrastructure are not discussed in this module, but are treated in the respective modules NET.4.2 * VoIP * and NET.4.5 * Unified Communications *.

Specific security requirements for Virtual Private Clouds and Hybrid Clouds are not the focus of this module (see OPS.3.2 * Cloud Providers * and OPS.3.4 * Managed Security Services *).

The network management is considered in the context of the zoning and segmentation, all further topics of the network management are treated in the building block NET.1.2 * network management *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​*** *** network architecture and design:

### 2 1 Failure or inadequate performance of communication links
If the communication links are insufficiently sized or if their performance is no longer sufficient due to technical failures or due to a denial-of-service (DoS) attack, eg B. Clients communicate only limited with servers. As a result, the access times to internal and external services (eg cloud services) increase, which are sometimes only limited or even unusable. Also, any business-related information is no longer available. As a result, production downtime can occur, for example, or essential business processes fail.

### 2 2 Insufficiently secured network access

Is the internal network connected to the Internet and the transition not sufficiently protected, z. For example, because no firewall is used or misconfigured, attackers can access and copy or manipulate the institution's sensitive information.

### 2 3 Improper construction of networks

If a network is improperly set up or expanded incorrectly, unsafe network topologies and network configurations can arise. This makes it easier for attackers to find security holes, penetrate the institution's internal network and extract information, manipulate data or disrupt entire production systems. Also, attackers in a faulty network, which the security systems can only monitor to a limited extent, remain unrecognized for longer.
