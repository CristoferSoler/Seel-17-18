1 description
--------------

### 1.1 Introduction

Wireless LANs (WLANs) can be used to set up wireless local area networks or extend existing wired networks. To date, almost all WLAN components available on the market are based on the IEEE 802.11 standard and its additions. A special role is played by the manufacturer consortium Wi-Fi Alliance, which has created an industry standard based on the IEEE 802.11 standard with "Wi-Fi". The Wi-Fi Alliance confirms with the Wi-Fi seal of approval that a device has passed certain interoperability and conformance tests.

Due to the usually simple installation, WLANs are also used to temporarily set up networks, for example at trade fairs or smaller events. In addition, in public places, such as airports or train stations, network access via so-called hotspots can be offered. This allows mobile users to connect to the Internet or their corporate network. Communication then generally takes place between a central access point, the access point, and the WLAN component of the terminal (for example via a WLAN USB stick or an integrated WLAN function).

### 1.2 Objective

This module aims to systematically show how WLANs can be safely set up and operated in an institution.

### 1.3 Delimitation

The module contains basic requirements that must be observed and fulfilled when setting up and operating WLANs. Requirements for secure use of WLANs are not the subject of this module. Secure use of WLANs is covered in the NET.2.2 * WLAN usage * block. Likewise, the operation of hotspots (see NET.2.3 * Operation of hotspots *) is not discussed here.

WLANs can be operated in two different modes according to the needs of an operator and the hardware equipment available. In ad hoc mode, two or more mobile devices equipped with a wireless network card communicate directly with each other. Since WLANs in ad-hoc mode can set up and configure autonomously, ie without fixed infrastructure, and thus establish a fully meshed parallel network infrastructure, the ad hoc mode is unsuitable in an environment to be protected. This will not be considered further below. In most cases, WLANs operate in infrastructure mode, which means H. the communication of the clients and the connection to wired LAN segments takes place via the access point.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​WLAN operation:

### 2 1 Failure or malfunction of a wireless network

In radio networks, information is transmitted by means of electromagnetic radio waves. If other electromagnetic sources radiate energy in the same frequency spectrum, they can interfere with wireless communication and in extreme cases prevent the operation of the WLAN. This can be caused by other radio systems and devices, such as Bluetooth, microwave ovens or other wireless networks. In addition, denial-of-service attacks are possible. For example, sending certain control and management signals repeatedly may cause the wireless network to become unavailable.

### 2 2 Missing or inadequate planning of the WLAN deployment

Planning errors often turn out to be particularly serious, since it is easy to create comprehensive security gaps. If the use of WLANs is not or insufficiently planned, a variety of problems can arise, such as the following:

* Confidential data could be read, for example if WLAN standards are used that are no longer state-of-the-art (eg WEP for encryption).* The transmission capacity may be insufficient. As a result, bandwidth-intensive applications can not be used with the required quality of service.
### 2 3 Missing or inadequate regulations for WLAN use

In the case of a WLAN infrastructure that is not centrally administered, the access points in the default setting are usually preconfigured with no or only insufficient security mechanisms. For example, if an employee includes an unapproved or unsecured access point in an internal network of the institution due to a lack of regulations, he undermines virtually all the security measures taken in the LAN, such as: For example, the security gateway (firewall) protects against unauthorized external access.

### 2 4 Unsuitable selection of authentication methods

If authentication methods and mechanisms are missing or insufficient, security gaps can arise. For example, the IEEE 802.1X (Port Based Network Access Control) standard defines the EAP (Extensible Authentication Protocol). Some of the described EAP methods contain vulnerabilities, eg. For example, EAP-MD5 is vulnerable to man-in-the-middle or dictionary attacks. If EAP-MD5 is used, passwords can be guessed and communication can be intercepted.

### 2 5 Incorrect configuration of the WLAN infrastructure

Access points and other WLAN components (eg WLAN controllers) offer a large number of configuration settings, which in particular also concern security functions. If wrong settings are made here, either no communication via an access point is possible or communication takes place unprotected or with too low a level of protection.

### 2 6 Insufficient or missing Wi-Fi security mechanisms

In the delivery state, WLAN components are often configured so that no or only a few security mechanisms are activated. Moreover, some of the mechanisms are inadequate and do not provide adequate protection. Even today, various WLAN components are used, the only insufficient security mechanisms such. B. WEP support. In part, these devices can not even be upgraded to stronger security mechanisms. If such devices are used, an attacker can easily listen to all communications and gain access to confidential information.

### 2 7 Listening to the WLAN communication

Since radio is a medium that several users can share ("shared medium"), the data transmitted via WLANs can be easily monitored and recorded. If the data is not or insufficiently encrypted, transmitted payload data can be easily obtained. In addition, radio networks or the radio waves transmitted often exceed the limits of the self-occupied premises, so that data are also broadcast in areas that can not be controlled and secured by the users or an institution.

### 2 8 Imitation of a valid access point (rogue access point)An attacker can pretend to be part of the WLAN infrastructure by installing their own access point with a properly chosen SSID near a client. This fake access point is called a rogue access point. If this provides the WLAN client with a higher transmission power than the real access point, the client will use it as the base station if two-sided authentication is not enforced. In addition, the real access point could be turned off by a denial-of-service attack. Users log on to a network that only pretends to be the destination network. This makes it possible for an attacker to listen to the communication. Poisoning or spoofing methods also allow an attacker to fake a false identity or to redirect network traffic to his systems. So he can eavesdrop and control the communication. Especially in public radio networks (so-called hotspots) a rogue access point is a popular means of attack.

### 2 9 Unprotected LAN access at the access point

If access points are visible and mounted without physical protection, an attacker can switch between the access points and the switch infrastructure to monitor all network traffic. Even if the communication with WPA2 is encrypted, this poses a threat because these methods only secure the air interface, but do not consider the Ethernet connection further.

### 2 10 hardware damage

Hardware damage can cause radio traffic to be disturbed. In the worst case, the WLAN can even fail completely. This applies in particular to WLAN devices that are installed outside protected areas (eg to cover open spaces). You are exposed to additional hazards, such as intentional damage by attackers or environmental damage caused by weather or lightning.

### 2 11 Theft of an access point

Are WLAN access points unsecured in transit ways attached, z. B. installed directly under the ceiling or in areas with heavy public traffic, they can be stolen. This makes it possible, for example, to read out a shared-secret key for authentication on the RADIUS server or the key used (for example for WPA2 personnel). With this information can then be accessed unauthorized access to the WLAN.

3 requirements
---------------

The following are specific requirements for Wi-Fi operation. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### NET.2.1.A1 Definition of a strategy for the use of WLANs [Head IT]

Before WLANs are used in an institution, it MUST be determined which general strategy the institution adopts with regard to WLAN usage. In particular, it MUST be clarified and stipulated in which organizational units, for which applications and for what purpose WLANs are used and what information may be transmitted here. Likewise MUST be determined in which spatial areas WLANs are to be built.In addition MUST be determined in the planning phase, who is responsible for the administration of the different WLAN components, which interfaces there are between the persons involved in the operation, and when what information must be exchanged between the responsible persons.

#### NET.2.1.A2 Selection of a suitable WLAN standard [planner]

In order to avoid a malfunction of the WLAN, WLAN-MUST first determine which of the systems operated by the institution (eg microwave devices, Bluetooth) in the ISM band at 2.4 GHz and in the 5 GHz Radiate ribbon.

In addition, the existing security mechanisms of the individual WLAN standards MUST be weighed against each other. In general, it MUST be ensured that only be used as a generally secure method for authentication and encryption. Only after the individual standards have been evaluated in detail, a specific WLAN standard can be set. The reasons for the decision MUST be documented.

Devices that have to fall back on unsafe ones from recognized safe procedures must NOT be included in the planning.

#### NET.2.1.A3 Selection of suitable crypto procedures for WLAN [Planner]

In order to operate a WLAN safely, communication via the air interface MUST be completely cryptographically secured. Cryptographic methods less secure than WPA2 MAY NOT be used.

If WPA2 is used with pre-shared keys (WPA2-PSK), then a complex key with a minimum length of 20 characters MUST be used. In addition, this MUST be changed regularly.

#### NET.2.1.A4 Appropriate installation of access points [building services]

Access points MUST be mounted securely. In addition MUST be taken to ensure that the propagation of radio waves in areas that are not to be supplied by the WLAN is reduced as much as possible. Outdoor installations MUST be protected from the effects of the weather and electrical discharges such as: B. Lightning be protected suitable.

#### NET.2.1.A5 Secure base configuration of access points

Access Points MUST NOT be used in the configuration of the delivery state. Preset SSIDs (service set identifiers), access passwords or cryptographic keys MUST be changed immediately after commissioning. In addition, insecure administration accesses (eg Telnet or HTTP) MUST be disabled. Access Points MUST be administered encrypted.

#### NET.2.1.A6 Secure configuration of the WLAN clients

In order to be able to operate an internal WLAN infrastructure safely, all the WLAN clients coupled with it should also be securely configured. Suitable requirements for secure configuration of clients can be found in the SYS.2.1 * General Client * and NET.2.2 * WLAN Usage * block. In addition, the following WLAN-specific requirements MUST be met:

* If the WLAN interface is not used for a long time, it MUST be deactivated.
* It MUST be ensured that no security zones are linked by means of WLAN communication and thus established protective measures are bypassed.
#### NET.2.1.A7 Structure of a Distribution System [Planner]

When building a distribution system, it MUST be decided in principle whether to physically or logically disconnect VLANs on the access switches of the wired LAN.

#### NET.2.1.A8 Behavioral rules for WLAN security incidents

In the event of a security incident, IT operations MUST take appropriate countermeasures (see also DER.2.1 * Incident Management *):

* At the transfer point of the WLAN communication into the internal LAN, the communication SHOULD be selectively blocked per SSID, access point or even for the complete WLAN infrastructure in the event of an attack on the WLAN.* If access points have been stolen, security measures MUST be implemented to prevent the access point from being abused.
* If WLAN clients have been stolen and certificate-based authentication is used, client certificates MUST be blocked.
The possible consequences of safety-critical events MUST be investigated. Ultimately MUST be excluded that stolen devices are used without authorization to access the network of the institution.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state of the art in WLAN operation. They SHOULD be implemented in principle.

#### NET.2.1.A9 Secure connection of WLANs to a LAN [planner]

If WLANs are connected to a LAN, the transition between WLANs and LAN should be secured, for example by a packet filter. The access point SHOULD be integrated taking into account the requirement NET.2.1.A7 * Structure of a Distribution System *.

#### NET.2.1.A10 Creation of a security policy for the operation of WLANs

Based on the general security policy of the institution, the essential core aspects for the secure use of WLANs SHOULD be specified. The guideline SHOULD be known to all those involved in the construction and operation of WLANs and should be the basis for their work. The implementation of the content required by the Directive SHOULD be reviewed on a regular basis. The results SHOULD be sensibly documented.

#### NET.2.1.A11 Suitable selection of WLAN components

If it has been decided to set up a WLAN infrastructure, the results of the planning phase SHOULD be used to create a list of requirements that can be used to evaluate the products available on the market. If WLAN components are procured, attention should be paid not only to security but also to data protection and compatibility of the WLAN components.

#### NET.2.1.A12 Use of a suitable WLAN management solution

In order to be able to guarantee an optimal configuration of the WLAN components from a security point of view, a central management solution SHOULD be used. The scope of the solution used SHOULD be in line with the requirements of the WLAN strategy.

#### NET.2.1.A13 Regular security checks in WLANs

WLANs SHOULD regularly be checked to see if any security vulnerabilities exist. In addition SHOULD search for unauthorized installed access points within the provided WLANs. Furthermore, the performance SHOULD be measured. The results of safety checks SHOULD be traceable documented and compared with the target state. Deviations SHOULD be investigated.

#### NET.2.1.A14 Regular audits of the WLAN components

For all components of the WLAN infrastructure (access points, distribution system, WLAN management solution, etc.) SHOULD check regularly whether all established security measures have been implemented and correctly configured. Publicly established access points SHOULD regularly be randomly checked for violent opening or manipulation attempts. The audit results SHOULD be traceable documented and compared with the target state. Deviations SHOULD be investigated.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### NET.2.1.A15 Using a VPN to Secure WLANs (CI)With increased protection requirements, a VPN SHOULD be used to additionally secure the communication via the WLAN infrastructure. Further information can be found in the module NET.3.3 * VPN *.

#### NET.2.1.A16 Additional protection for the connection of WLANs to a LAN (CIA)

If a WLAN infrastructure is connected to a LAN, the transition between WLANs and LAN should be additionally secured in accordance with the higher protection requirement.

#### NET.2.1.A17 Securing Communication Between Access Points (C)

The communication between the access points via the radio interface and the LAN SHOULD be encrypted in order to ensure the confidentiality of the transmitted data, for example roaming information or access data of users.

#### NET.2.1.A18 Using Wireless Intrusion Detection / Wireless Intrusion Prevention Systems (CIA)

In order to detect security incidents and vulnerabilities in a timely manner and initiate appropriate countermeasures, wireless intrusion detection systems or wireless intrusion prevention systems should be used.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on hazards and security measures in the area of ​​"WLAN operation" can be found in the following publications, among others:

* #### [BSIDKS] Wireless communication systems and their security aspects

  

 Federal Office for Information Security (BSI), 2009 <https://www.bsi.bund.de/DE/Publikationen/Broschueren/Drahtloskom/drahtloskom.html>

 
* #### [ISIWLAN] BSI Internet Security Standard (ISi Series)

  

 Secure connection of local networks to the Internet (Isi-LANA), Federal Office for Information Security (BSI), 2014
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/ standard criteria / ISi series / ISi-LANA / lana_node.html)

 
* #### [NIST800153] NIST Special Publication 800-153

  

 Guidelines for Securing Wireless Local Area Networks (WLANs), NIST, 02-2012 http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-153.pdf

 
* #### [NIST80097] NIST Special Publication 800-97

  

 Establishing Wireless Robust Security Networks, A Guide to IEEE 802.11, NIST, 02.2007
 <Http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-97.pdf>

 
* #### [TR03103] Technical Guideline Secure Wireless LAN

  

 Federal Office for Information Security (BSI), 2005 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03103/index\_htm.html]https://www.bsi.bund.de /DE/Publikationen/TechnischeRichtlinien/tr03103/index_htm.html)

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "WLAN operation".

* G 0.9 Failure or malfunction of communication networks
* G 0.15 Listening
* G 0.16 Theft of devices, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.23 Unauthorized intrusion into IT systems
* G 0.24 Destruction of equipment or data media
* G 0.25 Failure of devices or systems
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.40 Denial of Service
* G 0.43 Importing messages
* G 0.44 Unauthorized intrusion into premises
The cross reference tables can be found in the download area due to their size.