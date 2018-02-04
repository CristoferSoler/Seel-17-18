Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Routers and switches form the backbone of today's IT networks. Failure of one or more of these devices may result in the complete shutdown of the entire IT infrastructure. They must therefore be specially secured.

Routers work on the OSI layer 3 (network layer) and transmit data packets based on the destination IP address in the IP header. Routers are able to connect networks with different topographies. They are used to segment local area networks or to connect local area networks over wide area networks. A router identifies a suitable connection between the source system or source network and the destination system or destination network. In most cases, this is done by passing the data packets to the next router.

Switches originally worked on OSI Layer 2, but now they are available with different features. Manufacturers usually identify the devices with the OSI layer being supported. This gave rise to the terms layer 2, layer 3 and layer 4 switch, although layer 3 and layer 4 switches are actually already functionally routers. The originally different functions of switches and routers are thus often combined on one device.

### 1.2 Objective

The module describes how routers and switches are operated safely.

### 1.3 Delimitation

There is a large selection of different routers and switches from different manufacturers available in the market. The module does not describe specific requirements for specific products. He is as far as possible kept manufacturer independent.

By blending the functionality of routers and switches, most of the requirements can be used for both routers and switches. The present module does not differentiate between the device types.

Today, almost all operating systems also offer routing functionality. This block does not specify requirements for enabled routing functions in operating systems.

In addition, aspects of infrastructural safety (eg suitable installation or power supply or cabling) are not listed in this module, but can be found in the respective building blocks of the layer INF * Infrastructure *.

This module does not describe requirements for how virtual routers and switches can be protected. Security aspects of virtual active network components are dealt with in the module NET.1.4 * Network Virtualization *. Similarly, it will not address any existing firewall features of routers and switches. In addition, the block NET.3.2 * Firewall * must be implemented. Some aspects of network design and management are also relevant to the use of routers and switches and are mentioned in the context of the requirements. Further information on the structure, design and management of a network can be found in the building blocks NET.1.1 * Network architecture and design * and NET.1.2 * Network management *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to * routers and switches *:

### 2 1 Distributed Denial of Service (DDoS)

In a DDoS attack on a protected network, for example, by TCP SYN flooding or UDP packet storm, the router can fail due to the many network connections that need to be processed. This can result in certain services in the Local Area Network (LAN) becoming unavailable or the entire LAN failing.

### 2 2 Manipulation

If an attacker succeeds in gaining unauthorized access to a router or switch, he can reconfigure the devices or start additional services. For example, the configuration can be changed to block services, clients, or entire network segments.

### 2 3 Software vulnerabilities or errors
Routing and switch manufacturers regularly release updates and patches to address software bugs and known vulnerabilities in their products. However, if these are not recorded or played too late, the router or switch can be successfully attacked. This makes it possible for attackers to manipulate systems so that business-critical data drains, services fail, or entire production processes stand still.

### 2 4 Incorrect configuration of a router or switch

Routers and switches ship with a standard configuration in which many services are enabled. For example, login banners reveal the model and version number of the device. If routers and switches with insecure factory settings are used productively, they can be accessed more easily without authorization. This can lead to z. B. Services are no longer available.

### 2 5 Incorrect planning and conception

Many institutions plan and design the use of routers and switches incorrectly. Among other devices are procured, which are not sufficiently dimensioned, z. For example, in terms of port number or performance. As a result, a router or switch is already overloaded when used for the first time. As a result, services or entire networks may not be accessible and the error must be corrected consuming.

### 2 6 Incompatible active network components

Compatibility problems can arise in particular if existing networks are supplemented by active network components from other manufacturers or if networks are operated with network components from different manufacturers. If active network components with different implementations of the same communication method are operated together in one network, individual subareas of the network, certain services or even the entire network can fail.

### 2 7 MAC flooding

In MAC flooding, an attacker sends many requests with changing source MAC addresses to a switch. Once the switch has reached the limits of the MAC addresses it can store, it will send all requests to all IT systems on the network. This allows the attacker to see the network traffic.

### 2 8 spanning tree attacks

In spanning tree attacks, an attacker sends so-called Bridge Protocol Data Units (BPDUs) with the aim of making the switches look at their own (malicious) switch as a root bridge. This redirects network traffic through the attacker's switch so that it can log all information sent through it. As a result, he can initiate DDoS attacks and force the network to rebuild the spanning tree topology through inappropriate BPDUs, causing the network to fail.

### 2 9 GARP attacks

For Gratuitous ARP (GARP) attacks, the attacker sends unsolicited ARP responses to specific victims or to all IT systems on the same subnet. In this spoofed ARP response, the attacker enters his MAC address as a mapping to a foreign IP address and causes the victim to change his ARP table so that network traffic is now sent to the attacker instead of the valid target. Thereby he can record the communication between the victims or manipulate them.
