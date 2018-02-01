#B 3,302 routers and switches
## Description 
Networks are playing an increasingly important role as parts of the IT infrastructure because applications today are increasingly operating over local or wide area networks. The availability, integrity and confidentiality of networks must be ensured and at least meet the requirements of the applications for the protection of these three basic information security standards.

A network consists of active and passive network technology. Passive network technology is primarily understood as structured cabling. These include patch fields (cable distributors that can be configured via patch panels), protective cabinets and junction boxes at the workstation. Active network technology includes, for example, hubs, bridges, switches and routers. In modern networks, switches today often replace hubs and bridges. A failure of one or more components of the active network technology (routers and switches) can lead to a complete shutdown of the entire IT infrastructure. Because these components form the backbone of the IT infrastructure, routers and switches must be protected against unauthorized access and manipulation.

The functionality of routers is described in M .2.276 How a router works. The measure M 2.277 How a switch works describes how a switch works. The main functional differences of the active network components shown in the following figure are briefly explained.



Kollisionsdomne

A collision domain is understood to be a single segment in the network access method CSMA / CD (Carrier Sense Multipe Access with Collision Detection). All devices that are connected in the same segment are part of this collision domain. If two devices attempt to send a packet to the network at the same time, this is called a collision. Both devices then wait a certain period of randomly chosen length and then try again to send the packet. This waiting time reduces the effective bandwidth available to the devices.

Broadcast DOMAIN

Broadcast information is not directed to a particular terminal, but to all neighboring terminals. Those devices in a network that receive the respective broadcast information of the other devices together form a broadcast domain. Devices that are grouped in a broadcast domain do not need to be in the same collision domain. In the case of the IP protocol, this is also referred to as an IP subnet. For example, the stations with IP addresses from 192.168.1.1 to 192.168.1.254 in a subnet mask of IP 255.255.255.0 form a broadcast domain.

stroke

Hubs work on the OSI layer 1 (bit-transfer layer). All connected devices are in the same collision domain and thus in the same broadcast domain. Hubs are now being replaced by access switches (see M 2.277 How a Switch Works).

bridge

Bridges connect networks on OSI layer 2 (link layer) and segment collision domains. Each segment or port on a bridge forms its own collision domain. All connected stations are normally part of a broadcast domain. Bridges can also be used to interconnect networks with different topographies (Ethernet, Token Ring, FDDI, etc.) on the OSI layer 2 (transparent bridging, translational bridging). Mainly bridges were used for load distribution in networks. The relief is achieved by the fact that a bridge no longer forwards each data packet as a central transition between two network segments. A bridge contains an internal MAC address table, which shows in which connected segment corresponding MAC addresses are available. If, for example, the bridge receives a data packet for a station in sub-segment B from sub-segment A, the data packet is forwarded. If, in contrast, the bridge receives a data packet from sub-segment A for a station from sub-segment A, this data packet is not transferred to sub-segment B. As a result, a relief of the sub-segment B is achieved. Nowadays bridges are replaced by switches.

Layer 2 Switch

Conventional Layer 2 switches connect networks on OSI layer 2. Each switch port forms its own collision domain. Normally, all connected stations are part of a broadcast domain. This means that a Layer 2 switch uses the destination MAC address in the MAC header as the decision criterion for which port to forward incoming data packets. Despite the similar functioning, there are two main differences to Bridges:

* A switch usually connects much more sub-segments to each other than a bridge.
* The structure of a switch is based on Application Specific Interface Circuits (ASICs). This allows a switch to transport data packets from one segment to another much faster than a bridge. Different switching technologies are described in M 2.277 how a switch works.


Occasionally, switches are also referred to as multiport bridges.

router

Routers work on the OSI layer 3 (network layer) and transmit data packets based on the destination IP address in the IP header. Each interface on a router represents its own broadcast domain and thus also a collision domain. Routers are able to connect networks with different topographies. Routers are used to segment local area networks or to connect local area networks over wide area networks. A router identifies a suitable connection between the source system or source network and the destination system or destination network. In most cases, this is done by passing the data packet to the next router, the so-called Next Hop. Further aspects are described in M .2.276 How a router works.

Routers must analyze each IP packet before forwarding. This leads to delays and thus to a lower data throughput compared to classic switches.

Layer 3 switch and Layer 4 switch

Layer 3 and Layer 4 switches are switches that also provide routing functionality. Layer 2 switches use the destination MAC address in the MAC header of a packet to decide to which port data packets are forwarded. A Layer 3 switch treats data packets the first time like a router (destination IP address in the IP header). All subsequent data packets from the sender to this receiver are then forwarded to the OSI layer 2 (destination MAC address in the MAC header). As a result, such a switch can achieve a much higher throughput rate than a conventional router.

Another distinguishing feature between a router and a Layer 3 switch is the number of ports used to connect individual terminals. A layer 3 switch usually has a much larger port density.

The Routing feature allows Layer 3 or Layer 4 switches in local area networks to replace traditional LAN-to-LAN routers.

demarcation

This module describes the dangers and measures involved in using routers and switches. The distinction between routers and switches is made more difficult by the introduction of the designations Layer-2-Switch, Layer-3-Switch or Layer-4-Switch by different manufacturers. Merging the functionality of routers and switches allows most of the actions described to be applied to both routers and switches.

There is a large selection of different routers and switches from different manufacturers available on the market. The description of the measures and hazards in this module is kept in a way that it is as independent as possible from the manufacturer.

In addition to the cross-cutting aspects and the infrastructural measures, the use of routers and switches requires consideration of module B 4.1 Local networks. The B 4.2 Network and System Management module is of particular importance when it comes to integrating the active network components into comprehensive network and system management. When using a router as a packet filter or as a dial-in option, the blocks B 3.301 Security gateway (Firewall) and B 4.4 VPN must also be taken into account.

In addition to specially produced devices, various operating systems (for example, various Unix derivatives, Windows 2000, etc.) offer routing functionality. This means that a router can consist of a corresponding computer with two or more network adapters and a standard operating system. In smaller local networks, this may be a cost-effective alternative. In addition to the security measures described in this module, the security measures of the operating system used (Unix, Windows 2000, etc.) must be taken into account when operating such a router.



## Countermeasures 
The security measures assigned to this block are based on the life cycle of the active network components. Actions are described which are categorized into the following cycles:

* Planning and designing the use of routers and switchesThe use of routers and switches must be planned carefully. The functions of routers and switches are described in M .2.276 Operation of a router and M 2.277 functioning of a switch. Typical application scenarios of routers and switches that can be helpful in planning and design can be found in M .2.278 Typical deployment scenarios for routers and switches.
* Defining a Security Strategy for Routers and SwitchesBefore purchasing active network components (see M 2.280 Criteria for Procurement and Appropriate Selection of Routers and Switches), a security strategy must be defined and documented for the secure operation of the devices ( see M .2.279 Creating a security policy for routers and switches). Subsequently, suitable network coupling elements can be selected, which can then be safely integrated into the existing network infrastructure. During this phase, it is also important to train the administrators for the secure administration (see M .3.38 Administrator training for routers and switches).
* Configuration and Commissioning of Routers and Switches When configuring and commissioning routers and switches, a number of important security measures must be taken into account. Uncertain default configurations of network components often pose a considerable security risk. Therefore, the configuration must be checked during commissioning and adjusted. When commissioning routers and switches, the secure installation of the systems plays a major role (see M  4.201 Secure local basic configuration of routers and switches and M 4.202 Secure network basic configuration of routers and switches). When using routers, care must also be taken to ensure that the routing protocols are used safely. Depending on the purpose, access control lists (ACLs) should be configured on routers (see M 5.111 Setting up access control lists on routers). In this case, but also in normal operation, the system configuration must be carefully documented (see M 2.281 Documentation of the System Configuration of Routers and Switches). In addition, routers are often used to securely dial in and establish virtual private networks (VPNs). When setting up VLANs on switches, there are a few security issues to consider. In summary, M 4.203 Router and Switch Configuration Checklist documents a checklist for the secure configuration of routers and switches.
* Secure Operation of Routers and SwitchesNotes for the safe operation of routers and switches can be found in M 2.282 Regular control of routers and switches, M 2.283 Software maintenance on routers and switches, and M 6.91 Backup and recovery for routers and switches. Aspects of logging on routers and switches are described in M 4.205 Logging on Routers and Switches. Security issues that are important in the event of a failure are described in M 6.92 Emergency Preparedness for Routers and Switches.
* Security Issues When Routers and Switches Expire Saved configuration files and log files on routers and switches reveal information about the network structure. When decommissioning active network components, the notes from M .2.284 Safe commissioning of routers and switches must be taken into account.


Below are the measures to consider when using routers and switches:



